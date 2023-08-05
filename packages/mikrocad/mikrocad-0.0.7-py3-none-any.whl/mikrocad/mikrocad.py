# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 13:04:52 2015

@author: twagner
"""

### imports ###################################################################
import logging
import numpy as np
import os
import threading
import yaml

if os.name != "posix":
    import win32com.client

### imports from ##############################################################
from ctypes import CDLL
from ctypes import c_char_p, c_bool
from ctypes import c_byte, c_double
from ctypes import c_int, c_int16, c_short, c_long
from ctypes import c_ubyte
from ctypes import byref, pointer, POINTER

### relative imports from #####################################################
from .mikrocad_mock import MikroCAD_Mock
from .parameter import Parameter

###############################################################################
cShort = c_short()
cInt = c_int()
cLong = c_long()
cDouble = c_double()

###############################################################################
# LMI MikroCAD premium
###############################################################################
class MikroCAD(object):
    '''
    This class binds its methods to the GFM API in Measurement.dll
    '''

    _brightness = 0
    _dynamic_mode = 0
    _projector = 1
    _scale = (0., 0., 0.)
    
    error = None
    file_formats = [".kam", ".bmp", ".jpg"]
    languages = ['german', 'english']
    mockUp = False
    Nx = 1624
    Ny = 1236

    Nxy = Nx * Ny
    image_shape = (Ny, Nx)
    
    def __init__(self, filename):
        self.logger = logging.getLogger('mikrocad')
        self.logger.info("Starting LMI MikroCAD premium")

        self.handle = None
        self._invalidValue = -10010
        self._language = 0
        self.measurement_thread = None
        
        self._programPath = ''
        self.status = 'uninitialised'
        self.task_list = []
        self.temp_path = ''

        self.hardwareParameter = {}
        
        with open(filename) as f:    
            self.hardwareParameter = yaml.load(f)        

        self.hardwareFound = False
        self.LMI_DLL = None

        for key, value in self.hardwareParameter.items():
            if key == 'language':
                self._language = value
            elif key == 'program_path':
                self._programPath = value
            elif key == 'temp_path':
                self.temp_path = value

        #%% properties
        self._dynamic_mode = 0
        self._projectionPattern = 0
        self._shutterCam = 0
        self._shutterTimeBaseCam = 100

        self.hardwareFound = self.searchHardware()
            
        if self.hardwareFound:
            self.loadDLL()
            self.liveImage = True
        else:
            self.switchToEmulator()
            self.liveImage = False
        
        self.logFile = os.path.join(self._programPath, 'gfm.log')
        self.writeLogFile()

        self.language = self._language
        self.programPath = self._programPath

        self.paraDict = {}

        for key, values in self.hardwareParameter['parameters'].items():
            id = values['id']
            cType = values['type']
            
            limits = values['limits'] if 'limits' in values.keys() else False
            
            parameter = Parameter(id, key, cType, limits)
            self.paraDict[key] = parameter

    ### properties
    @property
    def brightness(self):
        self._brightness = self.getParameter('brightness')
        return self._brightness

    @brightness.setter
    def brightness(self, value):
        self.setParameter('brightness', value)

    #%%        
    @property
    def projector(self):
        self._projector = self.getParameter('projector')
        return self._projector

    @projector.setter
    def projector(self, value):
        self.setParameter('projector', value)

    #%%
    @property
    def dynamic_mode(self):
        self._dynamic_mode = self.getParameter('dynamic mode')
        return self._dynamic_mode

    @dynamic_mode.setter
    def dynamic_mode(self, value):
        self.setParameter('dynamic mode', value)

    #%%
    @property
    def invalidValue(self):
        # integer value which corresponds to NaN            
        self._invalidValue = self.LMI_DLL._GFM_GetInvalidProfileValue()
        return self._invalidValue


    #%%
    @property
    def language(self):
        return self._language
        
    @language.setter
    def language(self, value):
        self._language = value
        
        language = self.languages[value]
        self.logger.debug("Language: %s", language)

        self.LMI_DLL._GFM_SetLanguage(value)

    #%%
    @property
    def max_projection_area_x_size(self):
        self._max_projection_area_x_size = self.getParameter(
                'max projection area x-size')
        
        return self._max_projection_area_x_size

    #%%
    @property
    def max_projection_area_y_size(self):
        self._max_projection_area_y_size = self.getParameter(
                'max projection area y-size')
        return self._max_projection_area_y_size

    #%%
    @property
    def Nc(self):
        self._Nc = self.LMI_DLL._GFM_GetNumMeasProgCatalogs()

        return self._Nc

    #%%
    @property
    def programPath(self):
        return self._programPath
        
    @programPath.setter
    def programPath(self, filepath):
        self.logger.debug("path: %s", filepath)
        c_progPath = c_char_p(filepath.encode('utf-8'))

        self.LMI_DLL._GFM_SetProgramPath(c_progPath)

        self._programPath = filepath

    #%%
    @property
    def projectionPattern(self):
        return self._projectionPattern
        
    @projectionPattern.setter
    def projectionPattern(self, value):
        self.logger.debug("projected pattern: %i", value)
        self._projectionPattern = value
        self.LMI_DLL._GFM_ProjectPattern(value)

    #%%
    @property
    def scale(self):
        self._x_scale = self.getParameter('x-scale')
        self._y_scale = self.getParameter('y-scale')
        self._z_scale = self.getParameter('z-scale')

        self._scale = (self._x_scale, self._y_scale, self._z_scale)
        return self._scale

    #%%        
    @property
    def x_scale(self):
        self._x_scale = self.getParameter('x-scale')
        return self._x_scale

    @property
    def x_scale_ref(self):
        self._x_scale_ref = self.getParameter('x-scale_ref')
        return self._x_scale_ref

    @property
    def x_size(self):
        self.Nx = self.getParameter('x-size')
        return self.Nx

    @property
    def y_scale(self):
        self._y_scale = self.getParameter('y-scale')
        return self._y_scale

    @property
    def y_scale_ref(self):
        self._y_scale_ref = self.getParameter('y-scale_ref')
        return self._y_scale_ref

    @property
    def y_size(self):
        self.Ny = self.getParameter('y-size')
        return self.Ny

    @property
    def z_scale(self):
        self._z_scale = self.getParameter('z-scale')
        return self._z_scale

    ### methods
    def deinitMeasurement(self):
        self.logger.info("Deinitialising Measurement module")
        self.LMI_DLL._GFM_DeinitializeMeasurementModule()

    def doMeasure(self):
        self.logger.info("Measuring")
        error = self.LMI_DLL._GFM_Measurement(True)
        
        if error:
            self.logger.error("Error: %s", error)
            return error
        
        shape = Nx, Ny = self.x_size, self.y_size
        Nxy = Nx * Ny
        
        Nx2 = Nx // 2
        Ny2 = Ny // 2

        self.x = self.x_scale * np.arange(Nx)
        self.x -= self.x[Nx2]

        self.y = self.y_scale * np.arange(Ny)
        self.y -= self.y[Ny2]

        # scan data
        self.ptrScan = self.LMI_DLL._GFM_PtrToProfileData()

        # camera data
        self.ptrCam = self.LMI_DLL._GFM_PtrToCameraData()

        # valid data
        self.ptrValid = self.LMI_DLL._GFM_PtrToValidData()

        self.data = np.array(
                self.ptrScan[0:Nxy],
                dtype='int16'
        ).reshape(shape, order='F')

        self.valid = 100 * np.sum(self.data > self.invalidValue) / Nxy

        self.Z = self.data * self.z_scale

        return error

    def initMeasurement(self):
        self.logger.debug("Initialising measurement module")

        # changing to program directory omits Error -2001:
        # Error initialising measurement module
        currentDir = os.getcwd()
        os.chdir(self.programPath)
        error = self.LMI_DLL._GFM_InitializeMeasurementModule()
        os.chdir(currentDir)

        self.initialised = error

        if error:
            self.logger.warning(
                "Could not initialise measurement module: %i", error
            )
            
            self.switchToEmulator()
        
        return error

    def measurement_threaded(self, action='measure', params=None):
        previous_task = self.task_list[-1] if len(self.task_list) else None

        thread = threading.Thread(
                name=action,
                target=self.measurement_thread_target,
                args=(previous_task, action, params))

        self.task_list.append(thread)
        thread.start()

    def measurement_thread_target(self, previous_task, action, parameters):
        for t in threading.enumerate():
            if t == previous_task:
                t.join()
                self.task_list.remove(t)
            
        if action == 'initialise':
            self.status = 'initialising'
            self.initMeasurement()
            self.status = 'initialised'
        elif action == 'join':
            pass
        elif action == 'measure':
            self.status = 'measuring'
            self.doMeasure()
            self.status = 'finished'
        elif action == 'set_parameters':
            self.status = 'setting parameters'
            for key, value in parameters.items():
                self.setParameter(key, value)
            self.status = 'finished'
        elif action == 'deinitialise':
            self.status = 'deinitialising'
            self.deinitMeasurement()
            self.status = 'deinitialised'
        return

    def loadDLL(self):
        dllFile = os.path.join(self._programPath, "Measurement.dll")

        ### look for the DLL file
        if os.path.isfile(dllFile):
            self.dllFound = True

            self.logger.debug("Loading %s", dllFile)
            
            currentDir = os.getcwd()
            os.chdir(self._programPath)

            self.LMI_DLL = CDLL('Measurement')

            # self.Tools_DLL = CDLL('DotNetTransferTools')
            # version: 3.1.6.13

            self.LMI_DLL._GFM_SetProjectionArea.argtypes = [
                    c_double, c_double, c_double, c_double, c_int]

            self.LMI_DLL._GFM_GetCameraImage.restype = POINTER(c_ubyte)
            self.LMI_DLL._GFM_GetInvalidProfileValue.restype = c_int16

            self.LMI_DLL._GFM_GetMeasProgCatalogName.restype = c_char_p
            self.LMI_DLL._GFM_GetMeasProgItemName.restype = c_char_p

            self.LMI_DLL._GFM_LoadDataFile.restype = c_bool

            self.LMI_DLL._GFM_PtrToCameraData.restype = POINTER(c_short)
            self.LMI_DLL._GFM_PtrToProfileData.restype = POINTER(c_short)
            self.LMI_DLL._GFM_PtrToValidData.restype = POINTER(c_byte)

            os.chdir(currentDir)
        else:
            self.dllFound = False
            
            self.logger.error("Could not find file %s", dllFile)

        return self.dllFound

    def measParameterAvailable(self, parameter_id):
        available = c_bool()
        
        error = self.LMI_DLL._GFM_MeasParameterAvailable(
                parameter_id, pointer(available))
        
        if error:
            self.logger.error(
                "Error reading parameter %s: %s", parameter_id, error)
            
            self.error = error
        
        return available.value
        
    def searchHardware(self):
        hardwareFound = False

        if os.name != "posix":
            wmi = win32com.client.GetObject("winmgmts:")
    
            for usb in wmi.InstancesOf("Win32_USBHub"):
                if 'USB\VID_2032&PID_0101' in usb.DeviceID:
                    self.logger.info("Found GFM Alligator")
                    hardwareFound = True
                    break
    
            if not hardwareFound:
                self.logger.warning("Could not find GFM Alligator!")
        else:
            self.logger.warning('POSIX OS detected!')
            
        return hardwareFound

    def switchToEmulator(self):
        self.mockUp = True
        self.logger.warning("Switching to MikroCAD mock up")
        self.LMI_DLL = MikroCAD_Mock(self.hardwareParameter)

    def writeLogFile(self, override=True):
        self.logger.info("Logging to: %s", self.logFile)
        
        if override and os.path.exists(self.logFile):
            os.remove(self.logFile)
        
        self.LMI_DLL._GFM_WriteLogFile(True)

    def setParameter(self, name, value):
        parameter = self.paraDict[name]
        id = parameter.id
        cType = parameter.cType

        self.logger.info("Setting parameter %s to %s", parameter.name, value)
        
        if cType == 'int':
            error = self.LMI_DLL._GFM_SetMeasParameterInt(id, value)
        elif cType == 'long':
            error = self.LMI_DLL._GFM_SetMeasParameterInt(id, value)

        if error:
            self.logger.error(
                "Error setting parameter %s to value %s: %i",
                parameter.name, str(value), error
            )
        else:
            self.getParameter(name)

        return error

    def getParameter(self, name):
        parameter = self.paraDict[name]
        id = parameter.id
        cType = parameter.cType
        cInt1 = c_int()
        error = -1

        if self.hardwareFound:
            if cType == 'int':
                error = self.LMI_DLL._GFM_GetMeasParameterInt(id, byref(cInt))
                parameter.value = cInt.value
            elif cType == 'long':
                error = self.LMI_DLL._GFM_GetMeasParameterInt(id, byref(cLong))
                parameter.value = cLong.value
            elif cType == 'double':
                error = self.LMI_DLL._GFM_GetMeasParameterFloat(
                    id, byref(cDouble)
                )
               
                parameter.value = cDouble.value
        else:
            if cType == 'double':
                error = self.LMI_DLL._GFM_GetMeasParameterFloat(
                    id, pointer(cDouble))
               
                parameter.value = cDouble.value


            elif cType == 'int':
                error = self.LMI_DLL._GFM_GetMeasParameterInt(
                    id, pointer(cInt))
               
                parameter.value = cInt.value


            elif cType == 'long':
                error = self.LMI_DLL._GFM_GetMeasParameterInt(
                    id, pointer(cLong))
               
                parameter.value = cLong.value
            
        if error != 0:
            self.logger.error(
                "Error reading parameter %s: %s", parameter.name, error)
        else:
            if type(parameter.value) in (np.float, np.float64):
                self.logger.debug(
                        "%s: %10.6G", parameter.name, parameter.value)
            else:
                self.logger.debug("%s: %s", parameter.name, parameter.value)

        errorLimits = -1
        
        if parameter.hasLimits:
            if self.hardwareFound:
                errorLimits = self.LMI_DLL._GFM_GetMeasParameterLimitsInt(
                    id,
                    byref(cInt),
                    byref(cInt1)
                )
                
                parameter.lowerLimit = cInt.value
                parameter.upperLimit = cInt1.value
            else:
                c_i0 = c_int()
                c_i1 = c_int()
                
                errorLimits = self.LMI_DLL._GFM_GetMeasParameterLimitsInt(
                    id,
                    pointer(c_i0),
                    pointer(c_i1)
                )
                
                
                parameter.lowerLimit = c_i0.value
                parameter.upperLimit = c_i1.value
                errorLimits = 0

            if errorLimits != 0:
                self.logger.error(
                    "Error reading parameter %s limits: %s", parameter.name,
                    errorLimits
                )
            else:
                self.logger.debug(
                    '%s lower limit: %s', parameter.name, parameter.lowerLimit
                )

                self.logger.debug(
                    '%s upper limit: %s', parameter.name , parameter.upperLimit
                )

        return parameter.value

    def get_meas_prog_catalog_name(self, catalog_index):
        catalog_name = self.LMI_DLL._GFM_GetMeasProgCatalogName(0)
        return catalog_name.decode('utf-8')
        
    def get_meas_prog_item_name(self, catalog_index, item_index):
        itemName = self.LMI_DLL._GFM_GetMeasProgItemName(
                catalog_index, item_index)
        
        return itemName.decode('utf-8')

    def get_number_meas_prog_items(self, catalog_index):
        Ni = self.LMI_DLL._GFM_GetNumberMeasProgItems(catalog_index)
        return Ni

    def save(self, fullfile=None):

        if fullfile is None:
            brightness = self.getParameter('brightness')
            dynamic_mode = self.getParameter('dynamic mode')

            filename = ("test_B" + str(brightness) +
                "_D" + str(dynamic_mode))

            fullfile = os.path.join(self.temp_path, filename)

        error = self.saveCam(fullfile, 2)
        error += self.saveScan(fullfile, 1)
        
        return error

    def saveScan(self, fullfile, fileFormat=0):
        colorMode = 0

        self.logger.info("Saving %s", fullfile)
        
        c_fullfile = c_char_p(fullfile.encode('utf-8'))
        
        error = self.LMI_DLL._GFM_SaveProfileData(c_fullfile, fileFormat,
                                                  colorMode)

        if error != 0:
            self.logger.error("Error: %i", error)

        return error
        
    def saveCam(self, fullfile, fileFormat = 2):

        self.logger.info("Saving %s", fullfile)

        c_fullfile = c_char_p(fullfile.encode('utf-8'))
        
        error = self.LMI_DLL._GFM_SaveCameraData(c_fullfile, fileFormat)

        if error:
            self.logger.error("Error: %i", error)
            
        return error

    def projectImage(self):
        Nx = 1624
        Ny = 1236
        Nxy = Nx * Ny
        
        Nx2 = Nx // 2
        Ny2 = Ny // 2

        width = 50

        '''
        18.07.2018 15:42:14
        bool GFM_ProjectImage(BYTE* pbyImage)
        Parameter Input BYTE* pbyImage = 00124800
        Return value bool  = true
        '''
        
        img = (c_ubyte * Nxy)()
        
        M = np.zeros((Ny, Nx), dtype = np.bool)

        i0 = Nx2 - width
        i1 = Nx2 + width
        
        j0 = Ny2 - width
        j1 = Ny2 + width
        
        M[j0:j1, :] = True
        M[:, i0:i1] = True
        M_flat = M.flatten()

        for i in range(Nxy):
            if M_flat[i]:                
                img[i] = 255

        self.logger.debug('Projecting Image ...')

        self.LMI_DLL._GFM_ProjectImage(img)
                
    def get_camera_image(self):
        ptrImg = self.LMI_DLL._GFM_GetCameraImage(0)

        image_array = np.array(
            ptrImg[:self.Nxy], dtype='uint8'
        ).reshape(self.image_shape, order='C')
    
        return image_array
    
    def start_live_image(self, handle):
        error = self.LMI_DLL._GFM_StartLiveImage(handle, 0, 0, True)

        if error:
            self.logger.error("Error: %i", error)
        else:
            self.handle = handle
            self.liveOn = True
            
        return error      

    def stop_live_image(self):
        self.LMI_DLL._GFM_StopLiveImage()
        self.liveOn = False
        
        return self.liveOn

    def halt_continue_live_image(self):
        liveOn = c_bool()
        self.LMI_DLL._GFM_HaltContinueLiveImage(pointer(liveOn))

        self.liveOn = liveOn.value
        return self.liveOn

    def reset_projection_area(self):
        self.LMI_DLL._GFM_ResetProjectionArea()

    def set_projection_area(self, dx=0.5, dy=0.5, x0=0.1, y0=0.1):
        '''
        Parameter Input double dSizeX = 0
        Parameter Input double dSizeY = 0
        Parameter Input double dX0 = 1
        Parameter Input double dY0 = 1
        Parameter Input eGFMLiveImageRotation Rotation = GFMLiveImageRotation_0
        
        0: GFMLiveImageRotation_0
        1: GFMLiveImageRotation_90
        
        '''
        
        self.LMI_DLL._GFM_SetProjectionArea(2, dy, x0, y0, 0)

    

