# -*- coding: utf-8 -*-

### imports ###################################################################
import numpy as np

###############################################################################
class Points(object):
    def __init__(self, **kwargs):

        for key, value in kwargs.items():
            if key == 'points':
                self.xyz = value

    def copy_or_replace(self, **kwargs):
        copy = True
        raw = False
        
        for key, value in kwargs.items():
            if key == 'copy':
                copy = value
            elif key == 'points':
                xyz = value
            elif key == 'raw':
                raw = value
        
        if copy:
            if raw:
                # somewhat useless
                return xyz
            else:
                # default
                return Points(points=xyz)
        else:
            if raw:
                # 
                return xyz
            else:
                self.xyz = xyz
                return self

    def select_points_above(self, n, a, **kwargs):
        '''find points above a plane defined by Hessian Form n * x = a
           n: normal vector
           a: distance from origin
        '''

        copy = True
        preserve_shape = True
        raw = False

        for key, value in kwargs.items():
            if key == 'copy':
                copy = value
            elif key == 'preserve_shape':
                preserve_shape = value
            elif key == 'raw':
                raw = value
        
        b = np.dot(self.xyz, n)
        
        if preserve_shape:
            i_NaN = np.where(b <= a)
            
            if copy:
                xyz = np.copy(self.xyz)
            else:
                xyz = self.xyz
                
            xyz[i_NaN, :] = np.NaN
        else:
            xyz = self.xyz[b > a]
            
            if not copy:
                self.xyz = xyz
                
        if copy:
            if raw:
                # somewhat useless
                return xyz
            else:
                # default
                return Points(points=xyz)
        else:
            if raw:
                # 
                return xyz
            else:
                self.xyz = xyz
                return self
        

    def select_points_below(self, n, a, **kwargs):
        '''find points above a plane defined by Hessian Form n * x = a
           n: normal vector
           a: distance from origin
        '''
    
        b = np.dot(self.xyz, n)

        kwargs['points'] = self.xyz[b < a]

        return self.copy_or_replace(**kwargs)

    def select_points_in_axis_range(self, lim, **kwargs):
        '''find points within axis limits
           lim: tuple of minimum and maximum value
        '''
        
        axis = 0
        
        if 'axis' in kwargs.keys():
            axis = kwargs['axis']
        
        if copy:        
            iSelect = np.all(
                (lim[0] < self.XYZ[:,axis], self.XYZ[:,axis] < lim[1]),
                axis = 0)
            
            XYZ = self.XYZ[iSelect]
        

    def rotate_around_world_z(self, alpha=np.pi/2, **kwargs):
        copy = True
        raw = False
        
        for key, value in kwargs.items():
            if key == 'copy':
                copy = copy
            elif key == 'raw':
                raw = raw

        sin_alpha = np.sin(alpha)
        cos_alpha = np.cos(alpha)
        
        R = np.array([
            [cos_alpha, -sin_alpha, 0],
            [sin_alpha, cos_alpha, 0],
            [0, 0, 1]])

        points_rotated = R.dot(self.xyz.T).T

        if copy:
            return Points(points=points_rotated)
        
        if raw:
            return points_rotated
        else:
            self.xyz = points_rotated
            return self
                
###############################################################################
if __name__ == '__main__':
    a = 0.5
    alpha_deg = 5
    alpha = np.radians(alpha_deg)
    e_z = (0, 0, 1)
    
    cube = np.array(
        [
            [0, 0, 0],
            [1, 0, 0],
            [1, 1, 0],
            [0, 1, 0],
            [0, 0, 1],
            [1, 0, 1],
            [1, 1, 1],
            [0, 1, 1],
        ],
        dtype=np.float64)
    
    cube_points = Points(points=cube)
    
    rotated_cube_points = cube_points.rotate_around_world_z(alpha)
    
    # copy, preserve_shape, raw = False, False, False
    copy, preserve_shape, raw = True, False, False
    
    print(copy, preserve_shape, raw)
    
    points_above = cube_points.select_points_above(
            e_z, a, copy=copy, preserve_shape=preserve_shape, raw=raw)

    print('cube')
    print(cube)
    
    print('cube_points')
    print(cube_points.xyz)
    
    if raw:
        print('Raw points above:', a)
        print(points_above)
    else:
        print('Points above:', a)
        print(points_above.xyz)


    
    '''
    points_below_raw = cube_points.select_points_below(e_z, a, raw=True)
    print('Points below:', a)
    print(points_below_raw)
    '''