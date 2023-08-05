# -*- coding: utf-8 -*-

### imports ###################################################################
import numpy as np
import pyqtgraph as pg

###############################################################################
class ImageWidget(pg.GraphicsLayoutWidget):
    '''
        show profile in ROI
        show template
    '''
    
    def __init__(self, user = None):
        super(ImageWidget, self).__init__()

        self.initUI()
        
    def initUI(self):
        
        # A plot area (ViewBox + axes) for displaying the image
        plot_area = self.addPlot(lockAspect=True)
        
        # Item for displaying image data
        self.image_view = pg.ImageItem()
        plot_area.addItem(self.image_view)

        # Isocurve drawing
        self.iso_curve = pg.IsocurveItem(level=0.8, pen='g')
        self.iso_curve.setParentItem(self.image_view)
        self.iso_curve.setZValue(5)

        # Contrast/color control
        self.hist = pg.HistogramLUTItem()
        self.hist.setImageItem(self.image_view)
        self.addItem(self.hist)
        
        # Draggable line for setting isocurve level
        self.iso_line = pg.InfiniteLine(angle=0, movable=True, pen='g')
        self.iso_line.setValue(0.8)
        self.iso_line.setZValue(1000) # bring iso line above contrast controls
        self.iso_line.sigDragged.connect(self.updateIsoCurve)
        
        self.hist.vb.addItem(self.iso_line)
        self.hist.vb.setMouseEnabled(y=False)

        self.nextRow()
        
        self.line_plot = self.addPlot(colspan=2)
        self.line_plot.plot((0, 100), (0, 150))
        
        self.roi = pg.LineSegmentROI([[0, 0], [100, 150]], pen=(5,9))
        self.roi.setZValue(10)
        plot_area.addItem(self.roi)

        self.roi.sigRegionChanged.connect(self.update_roi)

        # self.init_data()

    def init_data(self):      
        # Generate image data
        data = np.random.normal(size=(200, 100))
        data[20:80, 20:80] += 2.
        data = pg.gaussianFilter(data, (3, 3))
        data += np.random.normal(size=(200, 100)) * 0.1

        self.set_data(data)

    def set_data(self, data):      
        self.data = data

        # build isocurves from smoothed data
        self.iso_curve.setData(pg.gaussianFilter(self.data, (2, 2)))

        self.image_view.setImage(self.data)
        self.update_roi()

        print(self.hist.getLevels())
        
    def update_roi(self):
        selected = self.roi.getArrayRegion(self.data, self.image_view)

        self.line_plot.plot(
                selected,
                clear=True,
                pen=None,
                symbolBrush=(255, 255, 255),
                symbolPen='w',
                symbolSize=2)
        
    def updateIsoCurve(self):
        print('update isoline')
        self.iso_curve.setLevel(self.iso_line.value())