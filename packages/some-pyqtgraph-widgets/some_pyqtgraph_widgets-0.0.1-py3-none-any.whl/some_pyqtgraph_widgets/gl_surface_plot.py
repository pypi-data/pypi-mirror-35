# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 14:12:39 2015

@author: twagner
"""

# -*- coding: utf-8 -*-

### imports ###################################################################
import numpy as np
import pyqtgraph.opengl as gl

### imports ###################################################################
from pyqtgraph.Qt import QtGui
from some_math.geo.plane import Plane
from some_math.geo.cuboid import Cuboid

###############################################################################
class SurfaceWidget(gl.GLViewWidget):
    def __init__(self, **kwargs):
        super(SurfaceWidget, self).__init__()

        Pmin = np.array((-3, -2, -1))
        Pmax = np.array((3, 2, 1))
        self.cuboid = Cuboid(Pmin, Pmax)
        self.cutEdges = None        
        self.cutPlane = Plane()
        self.item_dict = {}

        for key, value in kwargs.items():
            if key == 'cuboid':
                self.cuboid = value
            elif key == 'cutPlane':
                self.cutPlane = value
            elif key == 'distance':
                self.opts['distance'] = value

        # cuts = self.cuboid.planeCut(self.cutPlane)
        # self.setCutEdges(cuts)

        self.initUI()
        self.initEvents()
        
    def initUI(self):
        ### grid box
        self.gx = gl.GLGridItem()
        self.gx.setSize(2, 4, 1)
        self.gx.rotate(90, 0, 1, 0)
        self.gx.translate(-3, 0, 0)
        # self.gx.translate(-3, 2, 1)
        self.addItem(self.gx)

        self.gy = gl.GLGridItem()
        self.gy.setSize(6, 2, 1)
        self.gy.rotate(90, 1, 0, 0)
        self.gy.translate(0, -2, 0)
        self.addItem(self.gy)
        
        self.gz = gl.GLGridItem()
        self.gz.setSize(6, 4, 1)
        self.gz.translate(0, 0, -1)
        self.addItem(self.gz)
        
        ### x,y,z axis
        axis = gl.GLAxisItem()
        self.addItem(axis)

        ### cut plane
        x = np.array((0, 0, 0, 0, 0))
        y = np.array((-2, 2, 2, -2, -2))
        z = np.array((-1,  -1, 1,  1,  -1))
        pts = np.vstack([x, y, z]).transpose()

        self.cutEdges = gl.GLLinePlotItem(pos=pts, color=(0, 0, 1, 1))
        self.addItem(self.cutEdges)

    def initEvents(self):
        actionList = []
        
        actionList.append(["screenshot", "P, S", self.doScreenShot])        
        actionList.append(["rotate azimut", "Ctrl+A", self.doRotAzimut])        
        actionList.append(["rotate theta", "Ctrl+T", self.doRotTheta])        
        actionList.append(["increase distance", "Ctrl+D", self.doDistance])        

        actionList.append(
            ["decrease distance", "Ctrl+Shift+D", self.doMinDistance]
        )        

        actionList.append(["align with X axis", "Ctrl+X", self.doAlignX])        
        actionList.append(["align with Y axis", "Ctrl+Y", self.doAlignY])        
        actionList.append(["align with Z axis", "Ctrl+Z", self.doAlignZ])        

        for a in actionList:
            action = QtGui.QAction(
                a[0],
                self,
                shortcut = QtGui.QKeySequence(a[1]),
                triggered = a[2])
        
            self.addAction(action)
    
    def doScreenShot(self):
        print("DEBUG: doScreenShot")
        pass
    
    def doRotAzimut(self):
        print (
            "DEBUG: before rotation: azimut, theta",
            self.cutPlane.azimut, self.cutPlane.theta
        )
        
        azimut = (self.cutPlane.azimut + 0.05) % (2 * np.pi)
        self.cutPlane.setAzimut(azimut)
        self.updateCutEdges()
        
        print (
            "DEBUG: after rotation: azimut, theta", self.cutPlane.azimut,
            self.cutPlane.theta
        )

    def doRotTheta(self):
        print("DEBUG: doRotTheta")
        theta = (self.cutPlane.theta + 0.05) % np.pi
        self.cutPlane.setTheta(theta)
        self.updateCutEdges()

    def doDistance(self):
        a = (self.cutPlane.a + 0.05)
        self.cutPlane.setDistance(a)
        self.updateCutEdges()

    def doMinDistance(self):
        a = (self.cutPlane.a - 0.05)
        self.cutPlane.setDistance(a)
        self.updateCutEdges()

    def doAlignX(self):
        print("DEBUG: doAlignX")
        self.cutPlane.setAzimut(0.)
        self.cutPlane.setTheta(0.5 * np.pi)
        self.cutPlane.setDistance(0.)
        self.updateCutEdges()

    def doAlignY(self):
        self.cutPlane.setAzimut(0.5*np.pi)
        self.cutPlane.setTheta(0.5 * np.pi)
        self.cutPlane.setDistance(0.)
        self.updateCutEdges()

    def doAlignZ(self):
        self.cutPlane.setAzimut(0.)
        self.cutPlane.setTheta(0.)
        self.cutPlane.setDistance(0.)
        self.updateCutEdges()

    def cubicGrid(self, Pmin, Pmax):
        self.removeItem(self.gx)
        self.removeItem(self.gy)
        self.removeItem(self.gz)
        
        x = Pmax[0] - Pmin[0]
        y = Pmax[1] - Pmin[1]
        
        self.gz = gl.GLGridItem()
        self.gz.setSize(x = x, y = y, z = 1)
        self.addItem(self.gz)

    def setCutEdges(self, cuts):
        if self.cutEdges is not None:
            self.removeItem(self.cutEdges)

        if len(cuts) >= 3:
            self.cutEdges = gl.GLLinePlotItem(pos = cuts, color = (0, 0, 1, 1))
            self.addItem(self.cutEdges)
        else:
            self.cutEdges = None

    def add_normal(self, name, n, x):
        normal = gl.GLLinePlotItem(color=(1, 0, 0, 1))
        self.addItem(normal)
        self.item_dict[name] = normal
        self.set_normal(name, n, x)

    def add_surface(self, name, x, y, z, ds=10):
        surface = gl.GLSurfacePlotItem(shader='shaded')
        self.addItem(surface)
        self.item_dict[name] = surface
        self.set_surface(name, x, y, z, ds)

    def remove_item(self, name):
        if name in self.item_dict.keys():
            item = self.item_dict.pop(name)
            self.removeItem(item)

    def set_normal(self, name, n, x):
        pts = np.array([[x], [x + n]])        
        self.item_dict[name].setData(pos=pts)
      
    def set_surface(self, name, x, y, z, ds=10):
        if name in self.item_dict.keys():
            x_ds = x[::ds]
            y_ds = y[::ds]
            z_ds = np.copy(z[::ds, ::ds])
            
            self.item_dict[name].setData(x=x_ds, y=y_ds, z=z_ds)
        else:
            self.add_surface(name, x=x, y=y, z=z, ds=ds)

    def updateCutEdges(self):
        print("DEBUG: updateCutEdges")
        cuts = self.cuboid.planeCut(self.cutPlane)
        self.setCutEdges(cuts)
