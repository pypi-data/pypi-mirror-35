# -*- coding: utf-8 -*-

### imports ###################################################################
import logging
import os

### imports from ##############################################################

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QVBoxLayout

if os.name == "posix":
    from PyQt5.QtWidgets import QWidget
else:
    from PyQt5.QAxContainer import QAxWidget as QWidget

###############################################################################
class LiveWidget(QWidget):
    _brightness = 7
    control = "Hello.UserControl"
    _handle = 1234
    _item = 'notch'

    def __init__(self, live_image=True):
        super(LiveWidget, self).__init__()
        self.logger = logging.getLogger('mikrocad')

        self.live_image = live_image

        self.initUI()

    def initUI(self):
        if self.live_image:
            # request ActiveX live image control
            self.live_image = self.setControl(self.control)

        if not self.live_image:
            # mock up
            self.label = QLabel()
            self.pixmap = QPixmap()        
            self._set_pixmap()
       
            layout = QVBoxLayout()
            layout.addWidget(self.label)
            self.setLayout(layout)

        self.setFixedSize(512, 512)

    @property
    def brightness(self):
        return self._brightness
    
    @brightness.setter
    def brightness(self, value):
        self._brightness = value
        
        if not self.live_image:
            self._set_pixmap()

    @property
    def handle(self):
        if self.live_image:
            self._handle = self.dynamicCall('getHandle()')
            self.logger.debug('Live image widget handle: %i', self._handle)
        
        return self._handle

    @property
    def item(self):
        return self._item
    
    @item.setter
    def item(self, value):
        self._item = value
        
        if not self.live_image:
            self._set_pixmap()

    def _set_pixmap(self):
        brightness_str = '%02i' % self.brightness
        filename = self.item + '__brightness_' + brightness_str + '.png'
        fullfile = os.path.join('data', filename)

        self.logger.debug('loading %s', fullfile)

        is_loaded = self.pixmap.load(fullfile)

        if is_loaded:
            pixmap_scaled = self.pixmap.scaled(512, 512, Qt.KeepAspectRatio)
            self.label.setPixmap(pixmap_scaled)
        else:
            self.logger.error('Could not load %s', fullfile)

