# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 08:40:20 2015

@author: twagner
"""

### imports ###################################################################
import os

#### imports from #############################################################
from PyQt5.QtCore import QSize
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout, QGroupBox
from PyQt5.QtWidgets import QToolButton
from PyQt5.QtGui import QIcon

###############################################################################
class ToolBox(QGroupBox):
    
    def __init__(self, config_name, **kwargs):
        super(ToolBox, self).__init__()

        self.config_dict = kwargs['config']
        self.config_name = config_name

        for key, value in self.config_dict.items():
            if key == 'icons':
                self.icon_dict = value
            elif key == 'icon_path':
                self.icon_path = value

        self.button_list = self.config_dict[self.config_name]['content']

        self.button_labels = {}

        for key in self.button_list:
            self.button_labels[key] = self.config_dict['buttons'][key]
                
        self.initUI()
        
    def initUI(self):
        btn_size = QSize(110, 110)
        icon_size = QSize(46, 46)
        layout = QGridLayout()
        row_col = ((0, 0), (1, 0), (0, 1), (1, 1))

        for i, key in enumerate(self.button_list):
            btn_text = self.button_labels[key]
            btn_name = '_'.join(('btn', key))

            icon_filename = self.icon_dict[key]
            icon = QIcon(os.path.join(self.icon_path, icon_filename))
            
            button = QToolButton()
            button.setIcon(icon)
            button.setIconSize(icon_size)
            button.setMinimumSize(btn_size)
            button.setText(btn_text)
            button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

            row, col = row_col[i]
            layout.addWidget(button, row, col, Qt.AlignCenter)

            setattr(self, btn_name, button)

        self.setLayout(layout)
