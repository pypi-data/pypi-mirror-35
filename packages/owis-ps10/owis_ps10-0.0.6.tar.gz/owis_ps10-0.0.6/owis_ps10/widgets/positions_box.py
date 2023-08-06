# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QButtonGroup, QGridLayout, QGroupBox, QPushButton
# from PyQt5.QtWidgets import QToolButton

class PositionsBox(QGroupBox):
    def __init__(self, **kwargs):

        self.button_labels = tuple()
        title = ''
        self.unit = ''
        
        for key, value in kwargs.items():
            if key == 'button_labels':
                self.button_labels = value
            elif key == 'title':
                title = value
            elif key == 'unit':
                self.unit = value

        super(PositionsBox, self).__init__(title)
        
        self.initUI()
        
    def initUI(self):
        self.button_group = QButtonGroup()
        self.button_group.setExclusive(True)
        
        layout = QGridLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        
        row_col = ((0, 0), (0, 1), (1,0), (1, 1))
        
        for i, key in enumerate(self.button_labels):
            btn_name = '_'.join(('btn', key))
            btn_text = key + self.unit
            
            button = QPushButton(btn_text)
            button.setAccessibleName(key)
            button.setCheckable(True)
            button.setFixedWidth(40)
            self.button_group.addButton(button)
            
            row, col = row_col[i]
            layout.addWidget(button, row, col)
            
            setattr(self, btn_name, button)
        
        self.setLayout(layout)
    
if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    
    app = QApplication([])
    
    mw = PositionsBox()
    mw.show()
    
    app.exec_()