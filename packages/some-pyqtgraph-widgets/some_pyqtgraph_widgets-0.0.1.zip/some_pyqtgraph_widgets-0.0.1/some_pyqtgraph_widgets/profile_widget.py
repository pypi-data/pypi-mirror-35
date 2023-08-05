# -*- coding: utf-8 -*-

### imports ###################################################################
import numpy as np
import pyqtgraph as pg

###############################################################################        
class ProfileItem(pg.PlotDataItem):
    def __init__(self, x, y):
        super(ProfileItem, self).__init__()
        self.setSymbolBrush = (255, 255, 255, 255)
        
        self.setData(x, y)

###############################################################################        
class SemiMask(list):
    def __init__(self, tw=700, back=False):
        super(SemiMask, self).__init__()

        sm_A = 76
        sm_B = 508
        sm_Cx = 51
        sm_Cy = tw / 3
        sm_D = 76
        sm_M = tw / 2

        xu = (0, sm_A, 0)
        yu = (-sm_D, 0, 0)
        
        xl = (sm_B, sm_Cx, sm_Cx, sm_B, sm_B)
        yl = (-sm_M, -sm_M ,-sm_Cy, 0, -sm_M)

        if back:
            yu = -yu - tw
            yl = -yl - tw

        maskPen = pg.mkPen(width=0, color='r')
        maskBrush = pg.mkBrush(color='r')

        upperMask = pg.PlotDataItem(
                xu, yu, pen=maskPen, fillLevel=1, brush=maskBrush)

        lowerMask = pg.PlotDataItem(
                xl, yl, pen=maskPen, fillLevel=1, brush=maskBrush)
        
        self.append(upperMask)
        self.append(lowerMask)
        
###############################################################################
class ProfileWidget(pg.GraphicsLayoutWidget):
    '''
        show profile in ROI
        show template
    '''
    
    def __init__(self):
        super(ProfileWidget, self).__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Profile')
        layout = self.addLayout(row=1, col=1)

        ### view box to draw profile and semi mask
        self.viewBox = layout.addViewBox(row=1, col=0, lockAspect=True)

        ### grid
        gridItem = pg.GridItem()
        self.viewBox.addItem(gridItem)
        
    def addProfile(self, x, y, roi=False):
        

        xmin = np.min(x)
        xmax = np.max(x)
        dx = xmax - xmin
        
        ymin = np.min(y)
        ymax = np.max(y)
        dy = ymax -ymin
        
        lower_left = (xmin, ymin)
        widht_height = (dx, dy)

        if roi:
            plt = ProfileItem(np.array(x) - xmin, np.array(y) - ymin)
            self.addROI(lower_left, widht_height)
            plt.setParentItem(self.roi)
        else:
            self.viewBox.addItem(plt)
        
    def addItems(self, item_list):
        for item in item_list:
            self.viewBox.addItem(item)
            
    def addROI(self, lower_left, width_height):
        self.roi = pg.ROI(lower_left, width_height, removable=True)
        
        ## handles rotating around center
        self.roi.addRotateHandle([0, 0], [1, 0])
        self.roi.addRotateHandle([1, 0], [0, 0])
        
        ## handles rotating around opposite corner
        self.roi.addRotateHandle([0.5, 0], [0.5, 1])
        self.roi.addRotateHandle([0, 1], [0.5, 0.5])

        self.viewBox.addItem(self.roi)
