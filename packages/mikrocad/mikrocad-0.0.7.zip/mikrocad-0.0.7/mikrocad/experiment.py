# -*- coding: utf-8 -*-

### imports ###################################################################
import numpy as np

### relative imports from #####################################################
# from .sample import Sample

###############################################################################
class Experiment(dict):
    def __init__(self):
        pass               

    def add_sample(self, **kwargs):
        sample = Sample(self, **kwargs)
        sample_name = kwargs['name']
        
        self[sample_name] = sample
        
        return sample
    
    def read_scan_data(self, **kwargs):
        data = np.array([], dtype='int16')
        name = 'scan'
        scale = (1, 1, 1)
        
        for key, value in kwargs.items():
            if key == 'data':
                data = value
            elif key == 'i_NaN':
                i_NaN = value
            elif key == 'scale':
                scale = value
            elif key == 'name':
                name = value
        
        dx, dy, dz = scale        
        Nx, Ny = data.shape

        z_median = np.zeros(Ny, dtype='int')
        z_median = np.median(data[:-1,:], axis=0, out=z_median)
        i_valid = np.where(z_median > i_NaN)[0]
        iy_0 = i_valid[0]
        iy_1 = i_valid[-1]

        self.Nx2 = Nx // 2
        self.Ny2 = Ny // 2
        
        x_offset = dx * self.Nx2
        x = dx * np.arange(Nx) - x_offset
        
        y_offset = dy * self.Ny2
        y = dy * np.arange(Ny) - y_offset
        y = y[iy_0:iy_1]

        Z = dz * data
        Z[data == i_NaN] = np.nan
        Z = Z[:, iy_0:iy_1]
        
        sample = self.add_sample(name=name, x=x, y=y, Z=Z)
        return sample
        
###############################################################################
class Sample:
    alpha_deg = 40
    
    def __init__(self, parent, **kwargs):
        self.name = kwargs['name']
        self.x = kwargs['x']
        self.y = kwargs['y']
        # self.I = kwargs['I']
        self.Z = kwargs['Z']
        
    def estimate_wafer_thickness(self):
        alpha = np.radians(self.alpha_deg)
        cos_alpha = np.cos(alpha)
        sin_alpha = np.sin(alpha)
        tan_alpha = np.tan(alpha)
        
        ly = self.y[-1] - self.y[0]
        # lz = np.nanmax(self.Z) - np.nanmin(self.Z)
        ly_max = 4
        lz_max = 2
        ly_min = lz_max * tan_alpha
        t = ly * cos_alpha - lz_max * sin_alpha

        t_max = ly_max * cos_alpha - lz_max * sin_alpha
        print(ly_min, t_max)

        return t        
        