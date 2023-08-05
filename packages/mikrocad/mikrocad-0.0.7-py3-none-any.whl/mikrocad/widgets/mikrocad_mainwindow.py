# -*- coding: utf-8 -*-

### imports ###################################################################
import codecs
import logging
import numpy as np
import yaml

### imports from ##############################################################
from PyQt5.QtGui import QKeySequence

from PyQt5.QtWidgets import QAction, QFileDialog, QGridLayout, QGroupBox
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QMainWindow, QProgressBar
from PyQt5.QtWidgets import QTabWidget, QWidget

from some_pyqtgraph_widgets.image_widget import ImageWidget
from some_pyqtgraph_widgets.profile_widget import ProfileWidget
from some_pyqtgraph_widgets.gl_surface_plot import SurfaceWidget

### relative imports from #####################################################
from ..experiment import Experiment
from ..fd3 import FD3Reader

from .mikrocad_live import LiveWidget
from .microcad_measurebox import ToolBox
from .mikrocad_sequencer_widget import SequencerBox

###############################################################################
class MikroCADWindow(QMainWindow):
    config_file = 'config\\mikrocad_widget.cfg'
    
    def __init__(self, mc):
        super(MikroCADWindow, self).__init__()

        with codecs.open(self.config_file, 'r', 'utf-8') as f:
            self.config_dict = yaml.load(f)

        self.logger = logging.getLogger('mikrocad')
        self.mc = mc

        self.initUI()
        self.initEvents()
        self.initActions()

    def initDevice(self):
        self.statusBar().showMessage('initialisiere Scanner')
        self.progress_bar.setValue(50)
        self.mc.initMeasurement()
        self.statusBar().showMessage('Scanner initialisiert', 3000)
        self.progress_bar.reset()

        self.mc.projector = 1
        self.mc.start_live_image(self.handle)

        self.updateBrightness()
        self.updateDynamic()

    def initEvents(self):
        '''
        connect events/signals to functions/slots
        '''

        self.measurement_tools.btn_load.clicked.connect(self.doLoad)        
        self.measurement_tools.btn_save.clicked.connect(self.doSave)
        self.measurement_tools.btn_start.clicked.connect(self.doMeasure)

        self.sequencer_widget.currentTextChanged.connect(self.changeItem)
   
    def initActions(self):

        actionList = [
            ["pattern_1", "F1", self.doToggleProjector],
            ["pattern_2", "F2", self.doPattern],
            ["pattern_3", "F3", self.doPattern],
            ["pattern_4", "F4", self.doPattern],
            ["pattern_5", "F5", self.doPattern],
            ["pattern_6", "F6", self.doPattern],
            ["pattern_7", "F7", self.doPattern],
            ["pattern_8", "Shift+F1", self.doPattern],
            ["pattern_9", "Shift+F2", self.doPattern],
            ["pattern_10", "Shift+F3", self.doPattern],
            ["pattern_11", "Shift+F4", self.doPattern],
            ["pattern_12", "Shift+F5", self.doPattern],
            ["pattern_13", "Shift+F6", self.doPattern],
            ["pattern_14", "Shift+F7", self.doPattern],
            ["pattern_15", "Shift+F8", self.doPattern],
            ["brighter", "Ctrl++", self.doBrighter],
            ["delete", "Del", self.doDeleteJob],
            ["escape", "Escape", self.doCancelJob],
            ["darker", "Ctrl+-", self.doDarker],
            ["dynamic", "Ctrl+^", self.doDynamic],
            ["image", "Ctrl+I", self.doProjectImage],
            ["live", "Ctrl+L", self.doLive],
            ["measure", "Ctrl+M", self.doMeasure]
        ]
        
        for a in actionList:
            action = QAction(
                    a[0],
                    self,
                    shortcut=QKeySequence(a[1]),
                    triggered=a[2])

            self.addAction(action)

    def initUI(self):
        self.live_widget = LiveWidget()
        self.handle = self.live_widget.handle

        self.image_widget = ImageWidget()
        self.measurement_tools = ToolBox('measure', config=self.config_dict)
        
        self.sequencer_box = SequencerBox()
        self.sequencer_widget = self.sequencer_box.sequencer_widget
        
        if self.mc.mockUp:
            receipe = (
                {'name': 'Tisch', 'finished': False},
                {'name': 'Kante', 'finished': False},
                {'name': 'Notch', 'finished': False},
            )
        
            self.sequencer_widget.set_items(receipe)
        
        self.profile_widget = ProfileWidget()
        self.surface_widget = SurfaceWidget()

        self.tab_widget = QTabWidget()
        self.tab_widget.setMinimumSize(800, 800)
        self.tab_widget.addTab(self.surface_widget, "3D Model")
        self.tab_widget.addTab(self.profile_widget, "Einzelprofil")
        self.tab_widget.addTab(self.image_widget, "Höhenbild")

        self.control_tools_layout = QHBoxLayout()
        self.control_tools_layout.addWidget(self.live_widget)

        self.control_box = QGroupBox("Steuerung")
        self.control_box.setFlat(True)
        self.control_box.setLayout(self.control_tools_layout)

        self.control_box.setStyleSheet(
            "QGroupBox {font-size: 14pt; font-weight: bold;}")

        self.measurement_tools_layout = QHBoxLayout()
        self.measurement_tools_layout.addWidget(self.sequencer_box)
        self.measurement_tools_layout.addWidget(self.measurement_tools)

        self.measurement_box = QGroupBox("Messung")
        self.measurement_box.setFlat(True)
        self.measurement_box.setLayout(self.measurement_tools_layout)

        self.measurement_box.setStyleSheet(
            "QGroupBox {font-size: 14pt; font-weight: bold;}")

        self.gridLayout = QGridLayout()
        self.gridLayout.addWidget(self.measurement_box, 0, 0, 1, 6)
        self.gridLayout.addWidget(self.control_box, 3, 0, 6, 6)
        self.gridLayout.addWidget(self.tab_widget, 0, 6, 9, 10)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.gridLayout)
        self.setCentralWidget(self.central_widget)

        self.progress_bar = QProgressBar()
        self.statusBar().addPermanentWidget(self.progress_bar)

        status_widgets = [
                ('pattern', 'P: an'),
                ('brightness', 'B: --'),
                ('dynamic', 'D: --'),
                ('valid', 'V: --- %')
                ]

        for w in status_widgets:
            widget_name = w[0] + '_status_widget'
            text = w[1]
            setattr(self, widget_name, QLabel(text))

            widget = getattr(self, widget_name)
            widget.setFixedWidth(100)
            self.statusBar().addPermanentWidget(widget)

    def closeEvent(self, event):
        self.logger.debug('Closing Application')
        self.mc.projector = 0
        self.mc.deinitMeasurement()
        event.accept()

    def changeItem(self, currentItem):
        print('current', currentItem)
        
        print(self.config_dict)
        
        print(self.mc.hardwareParameter)
        
        self.live_widget.item = currentItem

    def doBrighter(self):
        brightness = self.mc.brightness
        self.mc.brightness = brightness + 1
        self.updateBrightness()

    def doCancelJob(self):
        self.statusBar().showMessage('cancel job', 3000)

    def doDarker(self):
        brightness = self.mc.brightness
        
        if brightness > 1:
            self.mc.brightness = brightness - 1

        self.updateBrightness()

    def doDeleteJob(self):
        self.statusBar().showMessage('delete all jobs', 3000)

    def doDynamic(self):
        dynamic_mode = self.mc.dynamic_mode
        self.mc.dynamic_mode = (dynamic_mode + 1) % 3
        self.updateDynamic()

    def doLive(self):
        ### toggle live image
        live_image = self.mc.halt_continue_live_image()

        if live_image:
            status = 'On'
        else:
            status = 'Off'
        
        msg = 'Live image: %s' % status
        self.statusBar().showMessage(msg, 3000)

    def doLoad(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File')[0]
        fd3 = FD3Reader(filename)
        data = fd3.Image
        i_NaN = fd3.i_nan
        Nxy = fd3.Image.size
        dx, dy, dz = scale = fd3.scale

        experiment = Experiment()
        scan = experiment.read_scan_data(data=data, i_NaN=i_NaN, scale=scale)
        
        valid = 100 * np.sum(data > i_NaN) / Nxy
        self.valid_status_widget.setText('V: %3.0f %%' % valid)

        self.image_widget.set_data(data)

        x_profile = np.linspace(0, 500)
        y_profile = -350 + 20 * np.sqrt(x_profile)    
        
        self.profile_widget.addProfile(x_profile, y_profile, roi=True)
        
        self.surface_widget.set_surface('scan', scan.x, scan.y, scan.Z, ds=10)

    def doMeasure(self):
        ### execute 3D scan
        self.statusBar().showMessage('Messung läuft')
        self.progress_bar.setValue(50)
        
        self.mc.doMeasure()
        self.mc.halt_continue_live_image()        

        data = self.mc.data
        i_NaN = self.mc.invalidValue
        scale = self.mc.scale

        experiment = Experiment()
        scan = experiment.read_scan_data(data=data, i_NaN=i_NaN, scale=scale)

        self.valid_status_widget.setText('V: %3.0f %%' % self.mc.valid)
        self.image_widget.set_data(self.mc.data)

        x = np.linspace(0, 500)
        y = -350 + 20 * np.sqrt(x)    
        self.profile_widget.addProfile(x, y, roi=True)

        x = self.mc.x        
        y = self.mc.y
        Z = self.mc.Z

        self.surface_widget.set_surface('scan', x, y, Z, ds=10)

        self.statusBar().showMessage('Messung fertig', 3000)
        self.progress_bar.reset()

    def doPattern(self):
        '''
        pattern_number  pattern        key
        ----------------------------------
        <0              dark            F1
        0               full            F2
        1               cross           F3
        2               rectangle       F4
        3               circle          F5
        4               window          F6
        5               crossed circle  F7
        '''

        sender_name = self.sender().text()
        pattern_number = int(sender_name.split('_')[1]) - 2

        if pattern_number < 14:
            self.mc.projectionPattern = pattern_number
            self.updatePattern()

    def doProjectImage(self):
        self.logger.info('Project Image')
        
        self.mc.projectImage()

    def doSave(self):
        print('doSave')
        self.mc.save()
        
    def doToggleProjector(self):
        projector = self.mc.projector
        
        if projector:
            self.mc.projector = 0
        else:
            self.mc.projector = 1

        self.updatePattern()
        
    def updateBrightness(self):
        brightness = self.mc.brightness
        self.brightness_status_widget.setText('B: %2i' % brightness)
        self.live_widget.brightness = brightness

    def updateDynamic(self):
        dynamic_mode = self.mc.dynamic_mode
        self.dynamic_status_widget.setText('D: %i' % dynamic_mode)        

    def updatePattern(self):
        pattern_list = [
                'aus',
                'an',
                'Kreuz',
                'Rechteck',
                'Kreis',
                'Fenster',
                'Kreis mit Kreuz',
                '1 Streifen',
                '2 Streifen',
                '4 Streifen',
                '8 Streifen',
                '16 Streifen',
                '32 Streifen',
                '64 Streifen',
                '128 Streifen',]
        
        pattern_number = 0
        projector = self.mc.projector

        if projector:
            pattern_number = self.mc.projectionPattern + 1
        
        pattern_name = pattern_list[pattern_number]
        self.pattern_status_widget.setText('P: %s' % pattern_name)        
        