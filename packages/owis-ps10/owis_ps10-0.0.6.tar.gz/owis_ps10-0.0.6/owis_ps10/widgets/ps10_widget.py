# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 08:40:20 2015

@author: hirschbeutel
"""

### imports ###################################################################
import logging
import numpy as np
import yaml

#### imports from #############################################################
from PyQt5.QtCore import pyqtSignal, Qt, QTimer

from PyQt5.QtGui import QKeySequence
from PyQt5.QtGui import QGuiApplication

from PyQt5.QtWidgets import QAction, QHBoxLayout
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QVBoxLayout, QWidget

### relative imports ##########################################################
from .axis_widget import AxisWidget
from .control_box import ControlBox
from .positions_box import PositionsBox
from .warnings import warnChangeWafer, warnMoveToSampleChangePosition
from .warnings import warnNoVacuum, warnWaferNotSuckedIn

### logger ####################################################################
logging.getLogger('owis_widget').addHandler(logging.NullHandler())

###############################################################################
class PS10Widget(QWidget):
    """
    Widget for hardware controls.
    """
    
    config_dict = {}
    
    ### signals
    gotoRef = pyqtSignal()
    gotoScan = pyqtSignal()
    sig_ref = pyqtSignal()

    def __init__(self, hardware, configFilename):
        super(PS10Widget, self).__init__()

        self.logger = logging.getLogger('owis_widget')        

        self.current_reference_state = -1
        self._scanPosition = 0.
        self.scanPositionSave = 0.
        self._succedIn = False
        self._vacuum = False
        self.waitForVacuum = False

        self.scanPositions = {}
        self.maxPositions = {}
        self.flatOffsets = {}

        self.config_filename = configFilename
        self.read_config()
        
        self.msgRef = u"Führe Referenzfahrt durch.\nBitte sicherstellen, dass keine Wafer aufliegen.\nBruchgefahr!"

        self.on_btn_text , self.off_btn_text = self.config_dict['vacuum']
        
        self.hardware = hardware
        
        self.hardware.digitalInput[0].verbosity = 1
        self.hardware.digitalOutput[0].verbosity = 1
        self.initDRTPosition = self.hardware.offsetMark

        self.waitForVacuum = False

        # positions = self.config_dict['positions']
        
        '''
        for position in positions:
            name = position['name']
            self.scanPositions[name] = position['LRT']
            self.maxPositions[name] = position['LRTmax']
            self.flatOffsets[name] = position['LRTflat']
        '''
        
        self.mountPlateType = '6"'
        # self.scanPositionSave = self.scanPositions[self.mountPlateType]
        
        self.initUI()
        self.initEvents()
        self.initTimers()
        self.initActions()
        
    def initUI(self):
        self.posTimer = QTimer()
        
        # icons http://www.flaticon.com/

        for key, value in self.config_dict['distances'].items():
            attr_name = '_'.join((key, 'dist'))
            setattr(self, attr_name, value)
            
        self.lrtBox = AxisWidget('Lineartisch', self.config_dict)
        self.drtBox = AxisWidget('Drehtisch', self.config_dict)
        self.controlBox = ControlBox(self.config_dict)
        
        button_labels = ('3', '4', '6', '8')
        self.posBox = PositionsBox(button_labels=button_labels, unit='"')
        
        button_labels = ('STD', 'HM')
        self.rotBox = PositionsBox(button_labels=button_labels)

        tableLayout = QVBoxLayout()
        tableLayout.addWidget(self.lrtBox)
        tableLayout.addStretch()
        tableLayout.addWidget(self.drtBox)

        owisLayout = QVBoxLayout()
        owisLayout.addWidget(self.controlBox)
        owisLayout.addStretch()
        owisLayout.addWidget(self.posBox)
        owisLayout.addWidget(self.rotBox)
        
        layout = QHBoxLayout()
        layout.addLayout(tableLayout)
        layout.addLayout(owisLayout)
        layout.addStretch()
        self.setLayout(layout)
        
    def initEvents(self):
        self.controlBox.btn_reference.clicked.connect(self.goReference)
        self.controlBox.btn_stop.clicked.connect(self.do_stop)
        self.controlBox.btn_vacuum.clicked.connect(self.do_toggle_vacuum)
        
        self.drtBox.btn_left.clicked.connect(self.do_turn)
        self.drtBox.btn_fast_left.clicked.connect(self.do_turn)
        self.drtBox.btn_right.clicked.connect(self.do_turn)
        self.drtBox.btn_fast_right.clicked.connect(self.do_turn)
        self.drtBox.btn_turn.clicked.connect(self.do_turn)

        self.lrtBox.btn_up.clicked.connect(self.do_move)
        self.lrtBox.btn_down.clicked.connect(self.do_move)
        self.lrtBox.btn_fast_up.clicked.connect(self.do_move)
        self.lrtBox.btn_fast_down.clicked.connect(self.do_move)

        self.posBox.button_group.buttonClicked.connect(self.do_pos)        
        self.rotBox.button_group.buttonClicked.connect(self.do_rot)

    def initTimers(self):
        for key, value in self.config_dict['timers'].items():
            timer_name = '_'.join(('timer', key))
            watcher_name = '_'.join(('watch', key))
            setattr(self, timer_name, QTimer())

            self.logger.info("Starting " + key + " timer")
            refreshTime_ms = 1000 / value

            timer = getattr(self, timer_name)
            timer.start(refreshTime_ms)

            watcher = getattr(self, watcher_name)
            timer.timeout.connect(watcher)

    def initActions(self):
        actionList = [
            ["go to reference","Home", self.goReference],

            ["btn_3", "Ctrl+3", self.do_btn_click],
            ["btn_4", "Ctrl+4", self.do_btn_click],
            ["btn_6", "Ctrl+6", self.do_btn_click],
            ["btn_8", "Ctrl+8", self.do_btn_click],

            ["up", "Up", self.do_move],
            ["down", "Down", self.do_move],
            ["fast_up", "Shift+Up", self.do_move],
            ["fast_down", "Shift+Down", self.do_move],
            
            ["left", "Left", self.do_turn],
            ["right", "Right", self.do_turn],
            ["fast_left", "Shift+Left", self.do_turn],
            ["fast_right", "Shift+Right", self.do_turn],
            ["turn", "PgDown", self.do_turn],

            ["stop", "Esc", self.do_stop],    
        ]

        for a in actionList:
            action = QAction(
                a[0],
                self,
                shortcut=QKeySequence(a[1]),
                triggered=a[2])

            self.addAction(action)

    ### properties
    @property
    def scanPosition(self):
        return self._scanPosition
        
    @scanPosition.setter
    def scanPosition(self, value):
        self._scanPosition = value

    @property
    def suckedIn(self):
        if self.hardware.vacuumInput.value == 1:
            self._suckedIn = True
        else:
            self._suckedIn = False
            
        return self._suckedIn

    @property
    def vacuum(self):
        if self.hardware.vacuumOutput.value == 1:
            self._vacuum = True
        else:
            self._vacuum = False
            
        return self._vacuum

    @vacuum.setter
    def vacuum(self, value):
        if value:
            self.logger.info("Switching on vacuum")
            self.hardware.vacuumOutput.value =  1

            self.initDRTPosition = self.hardware.getPosition(
                self.hardware.AXIS_DRT
            )
    
        else:
            self.logger.info("Switching off vacuum")
            self.hardware.vacuumOutput.value = 0
            
    ### methods
    def checkForReference(self, axis):
        if(not self.hardware.checkReference(axis)):
            msgRef = QMessageBox()

            message = (
                u"Keine Referenzposition gefunden. " +
                u"Jetzt eine Referenzfahrt durchführen?"
            )

            msgRef.setText(message)

            msgRef.setStandardButtons(
                QMessageBox.Ok | QMessageBox.Cancel
            )

            ret = msgRef.exec_()
            
            if(ret == QMessageBox.Ok):
                self.goReference()

    def checkForVacuum(self):
        hasVac = self.vacuum
        
        if(not hasVac and self.hardware.needVacuum):
            warnNoVacuum()
        
        return hasVac

    def checkForSuckedIn(self):
        hasVac = self.checkForVacuum()
        isSuckedIn = self.suckedIn

        if hasVac:
            if(not isSuckedIn and self.hardware.needVacuum):
                warnWaferNotSuckedIn()
        
        return isSuckedIn

    def goReference(self, warning=True):
        if warning:
            if not self.vacuum:
                QMessageBox.warning(self, "Referenzfahrt", self.msgRef)

        self.logger.info('Moving to reference position')
        
        self.hardware.moveRef()

        self.initDRTPosition = self.hardware.reference.drt
        self.sig_ref.emit()

    def goScan(self, position, angle = None):
        self.checkForReference(self.hardware.AXIS_LRT)

        ### move linear        
        self.hardware.moveAbsolute(
            self.hardware.AXIS_LRT,
            position
        )
        
        ### rotate
        if (
            isinstance(angle, (int, int, float)) and
            not isinstance(angle, bool)
        ):
            self.checkForSuckedIn()
            self.hardware.moveAbsolute(self.hardware.AXIS_DRT, angle)

        self.scanPosition = position

    def do_move(self):
        sender = self.sender()

        sender_type = type(sender)

        if (sender_type == QAction):
            sender_name = sender.text()
        else:
            sender_name = sender.accessibleName()
            
        attr_name = '_'.join((sender_name, 'dist'))

        distance = getattr(self, attr_name)

        modifiers = QGuiApplication.keyboardModifiers()

        if modifiers == Qt.ShiftModifier:
            distance *= 0.5
        elif modifiers == Qt.ControlModifier:
            distance *= 0.1

        self.checkForReference(self.hardware.AXIS_LRT)
        self.hardware.moveRelative(self.hardware.AXIS_LRT, distance)

    def do_btn_click(self):
        sender = self.sender()
        sender_name = sender.text()

        button = getattr(self.posBox, sender_name)
        button.click()

    def do_pos(self, button):
        button_key = button.accessibleName()
        self.goto_position(button_key)

    def do_rot(self, button):
        position = button.accessibleName()
        self.goto_angle(position)

    def goto_angle(self, position_key):
        self.checkForReference(self.hardware.AXIS_DRT)
        self.checkForSuckedIn()
        
        position_dict = {
                'STD': 177,
                'HM': 0
                }
        
        angle_deg = position_dict[position_key]
        
        self.hardware.moveAbsolute(self.hardware.AXIS_DRT, angle_deg)
        
    def goto_position(self, button_key):
        position_key = button_key + '"'
        self.checkForReference(self.hardware.AXIS_LRT)

        x_mm = self.config_dict['positions'][position_key]

        ### move linear        
        self.hardware.moveAbsolute(self.hardware.AXIS_LRT, x_mm)
        

    def do_toggle_vacuum(self):
        if self.vacuum == False:
            self.vacuum = True
        else:
            pos = self.hardware.getPosition(self.hardware.AXIS_DRT)

            if(pos != self.initDRTPosition):
                self.logger.info("DRT is rotated. moving back: %s", pos)

                self.hardware.moveAbsolute(
                    self.hardware.AXIS_DRT, self.initDRTPosition
                )

                self.waitForVacuum = True

            else:
                self.vacuum = False

    def do_turn(self):
        sender = self.sender()

        sender_type = type(sender)
        
        if (sender_type == QAction):
            sender_name = sender.text()
        else:
            sender_name = sender.accessibleName()
            
        attr_name = '_'.join((sender_name, 'dist'))

        distance = getattr(self, attr_name)

        modifiers = QGuiApplication.keyboardModifiers()

        if modifiers == Qt.ShiftModifier:
            distance *= 0.5
        elif modifiers == Qt.ControlModifier:
            distance *= 0.1

        self.checkForReference(self.hardware.AXIS_DRT)
        self.checkForSuckedIn()
        self.hardware.moveRelative(self.hardware.AXIS_DRT, distance)

        self.hardware.getCurrentPosition()

    def do_stop(self):
        self.hardware.axisLRT.stop()
        self.hardware.axisDRT.stop()

    def doMoveR(self):
        self.logger.info("moving relative: %s", self.txtMoveR.text())
        self.hardware.moveRelative(1, float(self.txtMoveR.text()))

    def doMoveTheta(self):
        self.logger.info("Move Theta: %", self.txtMoveTheta.text())
        self.hardware.moveRelative(2, float(self.txtMoveTheta.text()))

    def doDiameter(self, diameter):
        self.logger.info("received diameter: %s", diameter)

        if diameter == '76,2':
            plate = 'Wafer3'
        elif diameter == '100':
            plate = 'Wafer4'
        elif diameter == '150':
            plate = 'Wafer6'
        elif diameter == '200':
            plate = 'Wafer8'
        else:
            self.logger.error("wafer diameter not recognized: %s", diameter)
            plate = 'Wafer6'

        lrt, drt = self.hardware.getCurrentPosition()
            
        pos = self.scanPositions[plate]

        if (np.abs(lrt - pos) > 10.0 and lrt > 0.):
            if warnMoveToSampleChangePosition():
                self.logger.info("going to reference position ...")
                self.goReference(warning = False)
                self.logger.info("reference position reached")
    
                warnChangeWafer(diameter)
    
                self.logger.info("plate for %s mm wafer mounted", diameter)

    def read_config(self):
        with open(self.config_filename) as f:    
            self.config_dict = yaml.load(f)
                
    def restoreScanPosition(self):
        self.scanPosition = self.scanPositionSave

    ### watcher        
    def watch_emergency_stop(self):
        emergency = self.hardware.emergency
        
        if self.hardware.emergencyReleased:        
            self.hardware.axisLRT.motorInit()
            self.hardware.axisDRT.motorInit()
            
    def watch_position(self):
        l = self.hardware.getPosition(1)
        alpha = self.hardware.getPosition(2)
        
        self.controlBox.set_position(l, alpha)
        
    def watch_reference(self):
        self.hardware.checkReference(self.hardware.AXIS_DRT)
        self.hardware.checkReference(self.hardware.AXIS_LRT)
        
        if self.current_reference_state != self.hardware.referenceState:
            self.sig_ref.emit()
            
            if self.hardware.maxReferenceState != 3:
                self.controlBox.btn_reference.setStyleSheet(
                        'background-color: red')
            else:
                self.controlBox.btn_reference.setStyleSheet(
                        'background-color: none')

            self.current_reference_state = self.hardware.referenceState
            
    def watch_vacuum(self):
        pos = self.hardware.getPosition(self.hardware.AXIS_DRT)
        
        if (self.waitForVacuum and pos == self.initDRTPosition):
            self.vacuum = False
            self.waitForVacuum = False

        self.update_vacuum_button()

    def update_vacuum_button(self):
        if self.vacuum:
            self.controlBox.btn_vacuum.setText(self.off_btn_text)

            if self.suckedIn == True:
                self.controlBox.btn_vacuum.setStyleSheet(
                    'background-color: green')
            else:
                self.controlBox.btn_vacuum.setStyleSheet(
                    'background-color: orange')
        else:
            self.controlBox.btn_vacuum.setText(self.on_btn_text)

            self.controlBox.btn_vacuum.setStyleSheet(
                    'background-color: none')
            

        


 
