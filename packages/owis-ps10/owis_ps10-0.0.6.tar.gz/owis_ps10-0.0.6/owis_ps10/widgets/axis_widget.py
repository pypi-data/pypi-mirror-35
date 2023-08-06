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
from PyQt5.QtWidgets import QButtonGroup, QGridLayout, QGroupBox
from PyQt5.QtWidgets import QToolButton
from PyQt5.QtGui import QIcon

### logger ####################################################################
logging.getLogger('owis_widget').addHandler(logging.NullHandler())

###############################################################################       
class AxisWidget(QGroupBox):
    def __init__(self, axis, config_dict):
        self.axis = axis

        for key, value in config_dict.items():
            if key == 'distances':
                self.distances = value
            elif key == 'icons':
                self.icon_dict = value
            elif key == 'icon_path':
                self.icon_path = value

        self.button_labels = config_dict[axis]['buttons']
        self.unit = config_dict[axis]['unit']
        
        if self.unit == 'mm':
            self.unit = ' mm'

        super(AxisWidget, self).__init__(self.axis)
        
        self.initUI()
        
    def initUI(self):
        btn_size = QSize(80, 80)
        self.button_group = QButtonGroup()
        icon_size = QSize(46, 46)
        layout = QGridLayout()
        row_col = ((0, 0), (0, 2), (2,0), (2, 2), (4, 1))

        for i, key in enumerate(self.button_labels):
            btn_name = '_'.join(('btn', key))
            icon_filename = self.icon_dict[key]

            icon = QIcon(os.path.join(self.icon_path, icon_filename))
            value = self.distances[key]
            
            if type(value) == int:
                btn_text = u'%+0.0f%s' % (value, self.unit)
            else:
                btn_text = u'%+0.1f%s' % (value, self.unit)

            button = QToolButton()
            button.setAccessibleName(key)
            button.setIcon(icon)
            button.setIconSize(icon_size)
            button.setMinimumSize(btn_size)
            button.setText(btn_text)
            button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

            self.button_group.addButton(button)

            row, col = row_col[i]
            layout.addWidget(button, row, col, 2, 2)

            setattr(self, btn_name, button)

        self.setLayout(layout)
        self.setFixedWidth(190)
