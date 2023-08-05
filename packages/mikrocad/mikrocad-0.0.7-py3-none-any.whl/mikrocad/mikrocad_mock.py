# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 13:04:52 2015

@author: twagner
"""

### imports ###################################################################
import logging
import numpy as np
import os

### imports from ##############################################################
from ctypes import c_char_p

### relative imports from #####################################################
from .fd3 import FD3Reader

###############################################################################
logging.getLogger('mikrocad').addHandler(logging.NullHandler())

### LMI MikroCAD premium mock up ##############################################
class MikroCAD_Mock:
    error_dict = {
            'load_measurement': -2021,
            'parameter': -2031,
            'initialise': -2001,
            'uninitialised': -2003
    }

    limit_dict = {
            'brightness': (1, 20),
            'dynamic mode': (0, 2),
            'projector': (0, 1),
            }

    program_path = c_char_p()
    
    def __init__(self, parameterDict):
        self.logger = logging.getLogger('mikrocad')

        self.error_measurement = self.error_dict['uninitialised']

        Nx = 1624
        Ny = 1236
        Nxy = Nx * Ny

        self.liveOn = False

        self.dummyImage = np.random.randint(0, 255, Nxy, dtype='uint8')


        self.paraDict = {
            'brightness': 7,
            'projector': 1,
            'dynamic mode': 2,
            'x-size': Nx,
            'y-size': Ny,
            'invalidValue': -10010,
            'max projection area x-size': 1.608,
            'max projection area y-size': 1.787,
            'shutterCam': 0,
            'shutterTimeBaseCam': 0,
            'x-scale': 0.00305,
            'x-scale_ref': 0.00305,
            'y-scale': 0.00305,
            'y-scale_ref': 0.00305,
            'z-scale': 0.0001,
        }

        self.ptrScan = np.zeros(Nxy, dtype='int16')

        self.paraName = {
            11: 'brightness',
            12: 'dynamic mode',
            16: 'projector',
            21: 'x-size',
            22: 'y-size',
            111: 'x-scale',
            112: 'y-scale',
            113: 'z-scale',
            114: 'x-scale_ref',
            115: 'y-scale_ref',
            201: 'max projection area x-size',
            202: 'max projection area y-size',
        }
    
    def _GFM_DeinitializeMeasurementModule(self):
        # void method to deinitialise the measurement module
        pass
        
    def _GFM_GetCameraImage(self, value):
        return self.dummyImage
       
    def _GFM_GetInvalidProfileValue(self):
        return self.paraDict['invalidValue']
        
    def _GFM_GetMeasParameterFloat(self, parameterID, pointer_to_parameter):
        paraName = self.paraName[parameterID]
        value = self.paraDict[paraName]
        
        parameter = pointer_to_parameter.contents
        parameter.value = value
        
        return 0
        
    def _GFM_GetMeasParameterInt(self, parameterID, pointer_to_parameter):

        if parameterID in self.paraName.keys():
            paraName = self.paraName[parameterID]
            value = self.paraDict[paraName]
            
            parameter = pointer_to_parameter.contents
            parameter.value = value

            error = 0
        else:
            error = -2031

        return error

    def _GFM_GetMeasParameterLimitsInt(self, parameterID, p0, p1):
        parameter = p0.contents
        parameter.value = 0
        
        parameter = p1.contents
        parameter.value = 10
        
        return 0
        
    def _GFM_GetMeasProgCatalogName(self, index):
        return b'Standard'

    def _GFM_GetMeasProgItemName(self, i, j):
        return b'Standard'
            
    def _GFM_GetNumMeasProgCatalogs(self):
        return 1
       
    def _GFM_GetNumberMeasProgItems(self, index):
        return 1

    def _GFM_HaltContinueLiveImage(self, liveOn):
        self.liveOn = not self.liveOn
        liveOn.contents.value = self.liveOn
        
        return 0
        
    def _GFM_InitializeMeasurementModule(self):
        
        filepath = self.program_path.value.decode()
        filename = 'Measurement.dll'
        fullfile = os.path.join(filepath, filename)

        if os.path.isfile(fullfile):
            self.error_measurement = 0
            error = 0
        else:
            error = self.error_dict['load measurement']
        
        return error

    def _GFM_MeasParameterAvailable(self, parameter_id, available):
        isAvailable = True if parameter_id in self.paraName.keys() else False
        available.contents.value = isAvailable
        
        return 0
        
    def _GFM_Measurement(self, value):
        # Set raw datapoints
        # from myfilereader import kantenprofil
        filepath = "data"
        filename = "mounting_plate.fd3"
        fullfile = os.path.join(filepath, filename)
        fd3 = FD3Reader(fullfile)
        self.ptrScan = fd3.Image

        self.paraDict['xScale'] = fd3.dx
        self.paraDict['yScale'] = fd3.dy
        self.paraDict['zScale'] = fd3.dz
        
        return self.error_measurement

    def _GFM_ProjectPattern(self, patternID):
        return 0
        
    def _GFM_ProjectImage(self, image):
        return 0

    def _GFM_PtrToCameraData(self):
        return 0
    
    def _GFM_PtrToProfileData(self):
        return self.ptrScan
        
    def _GFM_PtrToValidData(self):
        return 0

    def _GFM_ResetProjectionArea(self):
        pass

    def _GFM_SaveCameraData(self, filename, fileFormat):
        return 0
        
    def _GFM_SaveProfileData(self, filename, fileFormat, colorMode):
        return 0

    def _GFM_SetLanguage(self, language):
        return 0
        
    def _GFM_SetMeasParameterInt(self, parameterID, value):
        parameterName = self.paraName[parameterID]

        para_min, para_max = self.limit_dict[parameterName]

        if value >= para_min and value <= para_max:

            self.logger.debug(
                "Setting %s with id %i to %i",
                parameterName, parameterID, value)
    
            self.paraDict[parameterName] = value

            error = 0

        else:
            error = self.error_dict['parameter']

            self.logger.error(
                "Error %i setting %s with id %i to %i",
                error, parameterName, parameterID, value)

        return error

    def _GFM_SetProgramPath(self, path):
        self.program_path = path
        return 0

    def _GFM_SetProjectionArea(self, dSizeX, dSizeY, dX0, dY0, Rotation):
        return 0
        
    def _GFM_StartLiveImage(self, handle, i1, i2, b):
        self.liveOn = True
        return 0

    def _GFM_StopLiveImage(self):
        self.liveOn = False

    def  _GFM_WriteLogFile(self, value):
        return 0
