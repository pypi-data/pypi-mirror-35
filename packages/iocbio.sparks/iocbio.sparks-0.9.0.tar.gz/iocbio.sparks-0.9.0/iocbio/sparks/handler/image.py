# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#  Copyright (C) 2018
#   Laboratory of Systems Biology, Department of Cybernetics,
#   School of Science, Tallinn University of Technology
#  Authors: Martin Laasmaa and Marko Vendelin
#  This file is part of project: IOCBIO Sparks
#
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QObject, QSettings
from PyQt5.QtGui import QTransform

import numpy as np
import copy
import os
from scipy import ndimage
from scipy.stats import linregress
from scipy.interpolate import UnivariateSpline, LSQUnivariateSpline
from collections import namedtuple, OrderedDict

from ..calc.auto_detect import get_sparks, AutoDetect
from .experiment import ExperimentHandler

import iocbio.sparks.worker as worker
import iocbio.sparks.info as info


# NB! Parameters names should be still different

### parameters used for image normalization
NDesc = namedtuple("NDesc", ["human_short", "human_long", "default", "sqltype", "pytype"])
NormalizationParameters = OrderedDict([
    ["bg", NDesc("Background", "Background intensity measured without cells [AU]", 0.0, "DOUBLE PRECISION", float)],
    ["min_area", NDesc("Minimal area", "Minimal area covered by spark [pixels]", 50, "INTEGER", int)],
    ["accept_as_possible_area", NDesc("Minimal spark intensity", "Acceptable relative intensity to consider as a spark area", 2.0, "DOUBLE PRECISION", float)],
    ["accept_as_possible_peak", NDesc("Minimal spark peak", "Acceptable relative intensity to consider as a spark peak", 3.8, "DOUBLE PRECISION", float)],
    ["sigma_time", NDesc("Boxcar blur in time [ms]", "Size of uniform filter applied in time", 3.0, "DOUBLE PRECISION", float)],
    ["sigma_space", NDesc("Boxcar blur in spatial coordinate [microm]", "Size of uniform filter applied along spatial coordinate", 0.25, "DOUBLE PRECISION", float)],
    ["median_time", NDesc("Median filter in time [ms]", "Size of the median filter window in time", 6.0, "DOUBLE PRECISION", float)],
    ["median_space", NDesc("Median filter in spatial coordinate [microm]", "Size of the median filter window along spatial coordinate", 0.6, "DOUBLE PRECISION", float)],
    ["window", NDesc("Distance between spline nodes for F0 calculation [s]", "Note that the distance between nodes should be significantly larger than expected sparks time-constants", 5, "DOUBLE PRECISION", float)],
    ])

### parameters used for automatic spark detection
SparkDetectorParameters = OrderedDict([
    ["spark_detector_buffer_space", NDesc("Space around automatically detected spark [microm]",
                                          "Extra space on the image added around area detected as a spark along spatial axis",
                                          1.0, "DOUBLE PRECISION", float)],
    ["spark_detector_buffer_time", NDesc("Time around automatically detected spark [ms]",
                                         "Time before and after added around area detected as a spark along temporal axis",
                                         4.0, "DOUBLE PRECISION", float)],
    ])


class NormalizeImageSignals(QObject):
    sigNormalizedImage = pyqtSignal(str, np.ndarray)
    sigProperty = pyqtSignal(str, float)


class NormalizeImage(worker.Job):
    Parameters = NormalizationParameters

    def __init__(self, dt, dx, data=None, **kwargs):
        worker.Job.__init__(self)

        self.dt = dt
        self.dx = dx

        for key in kwargs:
            if key not in self.Parameters:
                raise KeyError('Argument "%s" not allowed.' % key)

        for key, value in self.Parameters.items():
            if key in kwargs:
                setattr(self, key, kwargs[key])
            else:
                setattr(self, key, value.default)

        self.signals = NormalizeImageSignals()

        if data is not None:
            self.set_data(data)

    def get_parameters(self):
        d = {}
        for key in self.Parameters:
            d[key] = getattr(self, key)
        return d

    def set_parameter(self, **kwargs):
        for key, value in kwargs.items():
            if key in self.Parameters:
                setattr(self, key, value)
            else:
                raise KeyError('Argument "%s" not allowed.' % key)

    def set_data(self, data):
        self.data = data

    def run_job(self):
        self.normalize()

    def medblu(self, image):
        mb = ndimage.median_filter(image, size=(self.med_time, self.med_space))
        mb = ndimage.uniform_filter(mb, [int(round(self.sigma_time/1e3/self.dt)),
                                         int(round(self.sigma_space/1e6/self.dx))])
        return mb

    def normalize(self):
        info.info('Using following parameters for normalization:')
        for key in self.Parameters:
            info.info('Normalization parameter %s: %f' % (key, getattr(self, key)))
        data = self.data.astype(np.float)
        data -= self.bg

        filtered = np.zeros(data.shape)
        corrected_mean = np.zeros(data.shape)
        corrected_mean_medblu = np.zeros(data.shape)
        corrected_meansd = np.zeros(data.shape)
        corrected_meansd_medblu = np.zeros(data.shape)
        f0 = np.zeros(data.shape)

        x = np.arange(0, data.shape[0])
        w_size = int(np.ceil(self.window / self.dt))
        no_knots = np.floor((x.size - w_size) / w_size)
        knots = np.linspace(0, x.size, no_knots+2, dtype=int)[1:-1]

        iterations = [i+1 for i in range(10)]
        tol = 1.e-6
        f0_last = np.zeros(data.shape)

        self.med_time = int(round(self.median_time/1e3/self.dt))
        self.med_space = int(round(self.median_space/1e6/self.dx))
        info.info('Used median filter: %d pixels along spatial coordinate and %d pixels along time' % (self.med_space,self.med_time))
        if self.med_space < 3 or self.med_time < 3:
            msg = "Too small window for median filter, please increase it. As it is, you tried to use the filter with %d pixels along spatial coordinate and %d pixels along time" % (self.med_space,self.med_time)
            info.error('Normalization error', 'Median filter window too small', msg)
            return

        for iteration in iterations:
            if self.expired(): return

            for i in range(data.shape[1]):
                t_trace = data[:,i]

                try:
                    if iteration == iterations[0]:
                        spl = LSQUnivariateSpline(x, t_trace, knots)
                    else:
                        filt_ind = np.where(filtered[:,i] < 0.5)
                        spl = LSQUnivariateSpline(x[filt_ind], t_trace[filt_ind], knots)
                except:
                    msg = 'Failed to find F0 due to the spline fitter error. Please adjust the parameters for image correction'
                    info.error('Normalization error', 'Failed to find F0', msg)
                    return

                so = spl(x)
                if so.min() <= 0.0:
                    msg = 'Failed to fit line %d due to low or abrupt changes in intensity. Setting this line to the background level.' % i
                    info.warning(msg)
                    so = t_trace.copy()

                if so.min() <= 0.0:
                    msg = 'Image background level is set to too high value (background = %.3f) or too many sparks were detected reducing the available data required for background correction. Jobs cancelled.\n\nConsider lower value for the image background.' % self.bg
                    info.error('Normalization error', 'Background too large', msg)
                    return

                sqrt_so = np.sqrt(so)

                corrected_mean[:,i] = (t_trace - so)
                corrected_meansd[:,i] = (t_trace - so) / sqrt_so
                f0[:,i] = so

            corrected_meansd_medblu = self.medblu(corrected_meansd)

            std = ndimage.standard_deviation(corrected_meansd_medblu, filtered, index=[0])[0]
            filtered = get_sparks(corrected_meansd_medblu, std,
                                  accept_as_possible_area=self.accept_as_possible_area,
                                  accept_as_possible_peak=self.accept_as_possible_peak,
                                  min_area=self.min_area)

            err = np.linalg.norm(f0 - f0_last) / f0.size
            info.info("Image normalizer: Iter %d: tol=%f" % (iteration, err))
            if err < tol:
                break
            else:
                f0_last = copy.copy(f0)

        mF0 = f0.mean()
        corrected_meansd *= np.sqrt(mF0)
        std_meansd = ndimage.standard_deviation(corrected_meansd_medblu, filtered, index=[0])[0]
        corrected_meansd += (self.bg + mF0)

        corrected_meansd_medblu *= np.sqrt(mF0)
        std_meansd_medblu = ndimage.standard_deviation(corrected_meansd_medblu, filtered, index=[0])[0]
        corrected_meansd_medblu += (self.bg + mF0)

        corrected_mean += (self.bg + mF0)
        corrected_mean_medblu = self.medblu(corrected_mean)

        # send results
        self.signals.sigProperty.emit('property: meansd std', std_meansd)
        self.signals.sigProperty.emit('property: meansd std_medblu', std_meansd_medblu)
        self.signals.sigProperty.emit('property: mF0', mF0)
        self.signals.sigProperty.emit('property: bg', self.bg)
        self.signals.sigProperty.emit('property: accept_as_possible_peak', self.accept_as_possible_peak)
        self.signals.sigProperty.emit('property: accept_as_possible_area', self.accept_as_possible_area)
        self.signals.sigProperty.emit('property: min_area', self.min_area)
        self.signals.sigNormalizedImage.emit('Corrected Mean', corrected_mean)
        self.signals.sigNormalizedImage.emit('Corrected Mean MedBlu', corrected_mean_medblu)
        self.signals.sigNormalizedImage.emit('Corrected MeanSD', corrected_meansd)
        self.signals.sigNormalizedImage.emit('Corrected MeanSD MedBlu', corrected_meansd_medblu)
        self.signals.sigNormalizedImage.emit('F0', f0)

        filtered[filtered > 0.5] = 1
        self.signals.sigNormalizedImage.emit('Filtered', filtered.astype(np.uint8))


class Image(QObject):
    sigUpdated = pyqtSignal(str)
    sigRoiAdd = pyqtSignal(list, bool)
    sigImageNormalized = pyqtSignal(bool)

    ALL = 'ALL'

    database_table = "image"
    settings_group = "image"

    @staticmethod
    def database_schema(db):
        psql = ""

        keys = list(NormalizationParameters.keys())
        keys.sort()
        for k in keys:
            psql += '"' + k + '"' + " " + NormalizationParameters[k].sqltype +","

        db.query("CREATE TABLE IF NOT EXISTS " + db.table(Image.database_table) +
                 "(experiment_id text PRIMARY KEY, " + psql +
                 "FOREIGN KEY (experiment_id) REFERENCES " +
                 db.table(ExperimentHandler.database_table) + "(experiment_id) ON DELETE CASCADE)")

    @staticmethod
    def set_defaults(defaults):
        settings = QSettings()
        for k, v in defaults.items():
            if k in NormalizationParameters or k in SparkDetectorParameters:
                if isinstance(v, bool):
                    v = int(v)
                settings.setValue(Image.settings_group + "/" + k, v)

    @staticmethod
    def default_parameters():
        keys = list(NormalizationParameters.keys())
        keys.sort()
        return keys

    def __init__(self, raw, dt, dx, experiment_id, database):
        QObject.__init__(self)

        self.raw = raw
        self.normalization_region = [0, self.raw.shape[0]]
        self.dt = dt
        self.dx = dx
        self.experiment_id = experiment_id
        self.database = database

        self.processed_offset = [0, 0]
        self.processed = {}

        self.normalization_parameters = {}
        settings = QSettings()
        keys = Image.default_parameters()
        for k in keys:
            if isinstance(NormalizationParameters[k].default, bool):
                v = bool(int(( settings.value(Image.settings_group + "/" + k,
                                              defaultValue = NormalizationParameters[k].default) )))
            else:
                v = NormalizationParameters[k].pytype( settings.value(Image.settings_group + "/" + k,
                                                       defaultValue = NormalizationParameters[k].default) )
            self.normalization_parameters[k] = v

        # load normalization parameters from the database if available
        if self.database is not None:
            psql = ""
            keys = list(NormalizationParameters.keys())
            for k in keys:
                psql += '"' + k + '",'
            psql = psql[:-1]
            # only one row is expected
            for row in self.database.query("SELECT " + psql + " FROM " +
                                           self.database.table(Image.database_table) +
                                           " WHERE experiment_id=:eid", eid=self.experiment_id):
                for i in range(len(keys)):
                    self.normalization_parameters[keys[i]] = row[i]

        for key, value in SparkDetectorParameters.items():
            setattr(self, key,
                    value.pytype( settings.value(Image.settings_group + "/" + key,
                                                 defaultValue = value.default) ) )


    def normalize(self, t0, t1, **kwargs):
        [it0, it1], _ = self.get_array_indices([[t0, t1],[0,0]])
        new_normalization_parameters = kwargs

        proceed = False
        if self.normalization_region != [it0, it1]:
            # print('self.normalization_region', self.normalization_region, [it0, it1])
            proceed = True

        for k, v in kwargs.items():
            # print('kwargs key', k, v, self.normalization_parameters[k])
            if v != self.normalization_parameters[k]:
                # print('\tkwargs key', k, v, self.normalization_parameters[k])
                proceed = True
                break

        if not proceed:
            return

        self.normalization_region = [it0, it1]
        self.normalization_parameters.update(kwargs)

        self.processed = {}
        self.processed_offset = [it0, 0]
        self.sigUpdated.emit(Image.ALL)

        worker.workPool.drop_all()

        normalizer = NormalizeImage(self.dt, self.dx, **self.normalization_parameters)
        parameters = normalizer.get_parameters()
        normalizer.set_data(self.raw[it0:it1, :])
        normalizer.signals.sigNormalizedImage.connect(self._update_processed)
        normalizer.signals.sigProperty.connect(self._update_processed)
        normalizer.start()
        self.sigImageNormalized.emit(self.image_normalized())

        if self.database is not None:
            self.database.query("DELETE FROM " + self.database.table(Image.database_table) +
                                " WHERE experiment_id=:eid",
                                eid=self.experiment_id)

            pvals = { "eid": self.experiment_id }
            pnames = "experiment_id, "
            args = "(:eid,"
            for k in NormalizationParameters.keys():
                pnames += '"' + k + '",'
                args += ":" + k + ","
                pvals[k] = parameters[k]

            pnames = pnames[:-1]
            args = args[:-1] + ")"
            self.database.query("INSERT INTO " + self.database.table(Image.database_table) +
                                "(" + pnames + ") VALUES " + args,
                                **pvals)

    def detect_sparks(self):
        # in this routine, only meansd version is used, no need to specify it separately
        corrected_medblu = self.get_slice('Corrected MeanSD MedBlu')
        std = self.get_property('meansd std_medblu')
        mF0 = self.get_property('mF0')
        bg = self.get_property('bg')
        accept_as_possible_peak = self.get_property('accept_as_possible_peak')
        accept_as_possible_area = self.get_property('accept_as_possible_area')
        min_area = self.get_property('min_area')
        if corrected_medblu is None or std is None or mF0 is None or bg is None:
            msg = "Not ready with image normalization, please wait till its normalized"
            info.error('Please wait', 'Please wait', msg)
            return

        corrected_medblu = corrected_medblu - bg - mF0
        detector = AutoDetect(corrected_medblu, std=std,
                              accept_as_possible_area=accept_as_possible_area,
                              accept_as_possible_peak=accept_as_possible_peak,
                              min_area=min_area)
        detector.signals.sigRegion.connect(self._auto_region)
        detector.start()

    def _auto_region(self, r):
        b0, b1 = self.normalization_region
        r[0], r[2] = r[0]+b0, r[2]+b0
        dx = int(round(self.spark_detector_buffer_space/1e6/self.dx))
        dt = int(round(self.spark_detector_buffer_time/1e3/self.dt))
        r[0] = max(0,r[0]-dt)
        r[2] = min(self.raw.shape[0]-1,r[2]+dt)
        r[1] = max(0,r[1]-dx)
        r[3] = min(self.raw.shape[1]-1,r[3]+dx)

        # skip region if on the border of the image
        if r[0]<=b0 or r[1]<=0 or r[2]>=self.raw.shape[0]-1 or r[3]>=self.raw.shape[1]-1:
            return

        self.sigRoiAdd.emit(r, False)

    def _update_processed(self, name, image):
        self.processed[name] = image
        self.sigUpdated.emit(name)
        self.sigImageNormalized.emit(self.image_normalized())

    def get_raw_time_slice(self, t0, t1):
        [it0, it1], _ = self.get_array_indices([[t0, t1],[0,0]])
        return self.raw[it0:it1, :]

    def get_slice(self, name, slc=None):
        if name == 'Raw':
            if slc is None: return self.raw
            [t0, t1], [x0, x1] = slc
            return self.raw[t0:t1, x0:x1]

        if name in self.processed:
            image = self.processed[name]
            if slc is None:
                return image
            else:
                [t0, t1], [x0, x1] = slc
                b0, b1 = self.normalization_region
                if t0 > b0 and t1 < b1:
                    to, xo = self.processed_offset
                    return image[t0-to:t1-to, x0-xo:x1-xo]

                return None

        return None

    def get_property(self, name):
        """ returns property from self.processed list, if key is not found returns None"""
        return self.processed.get('property: ' + name)

    def get_array_indices(self, coords):
        """ mapping physical coordinates to raw image indices
        coords = [[t0, t1], [x0, x1]] t = time, x = space
        returns respective raw image indices
        """
        [t0, t1], [x0, x1] = coords
        return [int(round(t0/self.dt)), int(round(t1/self.dt))], [int(round(x0/self.dx)), int(round(x1/self.dx))]

    def get_physical_coords(self, indices):
        """ mapping raw image indices to physical coordinates
        indices = [[t0, t1], [x0, x1]] t = time, x = space
        returns respective physical coordinates
        """
        [t0, t1], [x0, x1] = indices
        return [t0*self.dt, t1*self.dt], [x0*self.dx, x1*self.dx]

    @property
    def get_image_filename(self):
        return self.database.query("SELECT filename FROM " +
                                   self.database.table(ExperimentHandler.database_table) +
                                   " WHERE experiment_id=:eid", eid=self.experiment_id)[0][0]

    @property
    def get_image_filepath(self):
        return os.path.dirname(self.get_image_filename)

    def image_normalized(self):
        if self.get_slice('Corrected Mean MedBlu') is not None:
            return True
        return False
