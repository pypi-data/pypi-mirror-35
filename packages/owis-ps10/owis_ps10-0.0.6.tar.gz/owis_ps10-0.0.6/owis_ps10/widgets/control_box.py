# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 08:40:20 2015

@author: twagner
"""

### imports ###################################################################
import logging
import os

#### imports from #############################################################
from PyQt5.QtCore import QSize
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout, QGroupBox
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QToolButton
from PyQt5.QtGui import QIcon

### logger ####################################################################
logging.getLogger('owis_widget').addHandler(logging.NullHandler())

###############################################################################
class ControlBox(QGroupBox):
    txt_fmt = '%5.1f mm, %5.1f°'
    def __init__(self, config_dict):
        super(ControlBox, self).__init__("Owis")

        self.config_dict = config_dict

        for key, value in config_dict.items():
            if key == 'distances':
                self.distances = value
            elif key == 'icons':
                self.icon_dict = value
            elif key == 'icon_path':
                self.icon_path = value

        self.button_list = config_dict['control']

        self.button_labels = {}

        for key in self.button_list:
            self.button_labels[key] = config_dict[key]
                
        self.initUI()
        
    def initUI(self):
        btn_size = QSize(110, 110)
        icon_size = QSize(46, 46)
        layout = QGridLayout()
        row_col = ((2, 0), (3, 0), (4, 0))

        self.txtPos = QLabel(self.txt_fmt % (0.0, 0.0))
        self.txtPos.setMinimumWidth(110)

        for i, key in enumerate(self.button_list):
            btn_text = self.button_labels[key][0]
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

        layout.addWidget(self.txtPos, 5, 0, Qt.AlignCenter)
        self.setLayout(layout)
        
    def set_position(self, l, alpha):
        self.txtPos.setText(self.txt_fmt % (l, alpha))

