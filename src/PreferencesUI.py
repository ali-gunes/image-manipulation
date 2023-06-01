# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'PreferencesUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import qdarktheme


class Ui_PreferencesWindow(object):
    def setupUi(self, PreferencesWindow, MainWindow, AboutWindow, controlsDynamicIsland, manipulationDynamicIsland):
        PreferencesWindow.setObjectName("PreferencesWindow")
        PreferencesWindow.resize(523, 371)
        font = QtGui.QFont()
        font.setPointSize(10)
        PreferencesWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/icons/university.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PreferencesWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(PreferencesWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.appearance_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.appearance_groupBox.setObjectName("appearance_groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.appearance_groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.themeSelector_label = QtWidgets.QLabel(self.appearance_groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.themeSelector_label.setFont(font)
        self.themeSelector_label.setObjectName("themeSelector_label")
        self.horizontalLayout.addWidget(self.themeSelector_label)
        self.themeSelector_comboBox = QtWidgets.QComboBox(self.appearance_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.themeSelector_comboBox.sizePolicy().hasHeightForWidth())
        self.themeSelector_comboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.themeSelector_comboBox.setFont(font)
        self.themeSelector_comboBox.setObjectName("themeSelector_comboBox")
        self.horizontalLayout.addWidget(self.themeSelector_comboBox)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.font_label = QtWidgets.QLabel(self.appearance_groupBox)
        self.font_label.setObjectName("font_label")
        self.horizontalLayout_3.addWidget(self.font_label)
        self.fontComboBox = QtWidgets.QFontComboBox(self.appearance_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fontComboBox.sizePolicy().hasHeightForWidth())
        self.fontComboBox.setSizePolicy(sizePolicy)
        # Filtered the fonts for only the Latin alphabet for UI consistency
        self.fontComboBox.setWritingSystem(QtGui.QFontDatabase.Latin)
        self.fontComboBox.setFontFilters(
            QtWidgets.QFontComboBox.MonospacedFonts | QtWidgets.QFontComboBox.ProportionalFonts | QtWidgets.QFontComboBox.ScalableFonts)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fontComboBox.setCurrentFont(font)
        self.fontComboBox.setObjectName("fontComboBox")
        self.horizontalLayout_3.addWidget(self.fontComboBox)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fontSize_label = QtWidgets.QLabel(self.appearance_groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fontSize_label.setFont(font)
        self.fontSize_label.setObjectName("fontSize_label")
        self.horizontalLayout_2.addWidget(self.fontSize_label)
        self.fontSize_spinBox = QtWidgets.QSpinBox(self.appearance_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fontSize_spinBox.sizePolicy().hasHeightForWidth())
        self.fontSize_spinBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fontSize_spinBox.setFont(font)
        self.fontSize_spinBox.setMinimum(6)
        self.fontSize_spinBox.setProperty("value", 10)
        self.fontSize_spinBox.setObjectName("fontSize_spinBox")
        self.horizontalLayout_2.addWidget(self.fontSize_spinBox)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.appearance_groupBox)
        self.controlIslandAlign_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.controlIslandAlign_groupBox.setObjectName("controlIslandAlign_groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.controlIslandAlign_groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.controlIslandAlignLeft_radioButton = QtWidgets.QRadioButton(self.controlIslandAlign_groupBox)
        self.controlIslandAlignLeft_radioButton.setObjectName("controlIslandAlignLeft_radioButton")
        self.verticalLayout.addWidget(self.controlIslandAlignLeft_radioButton)
        self.controlIslandAlignRight_radioButton = QtWidgets.QRadioButton(self.controlIslandAlign_groupBox)
        self.controlIslandAlignRight_radioButton.setObjectName("controlIslandAlignRight_radioButton")
        self.verticalLayout.addWidget(self.controlIslandAlignRight_radioButton)

        self.controlIslandLockWidth_checkBox = QtWidgets.QCheckBox(self.controlIslandAlign_groupBox)
        self.controlIslandLockWidth_checkBox.setObjectName("self.controlIslandLockWidth_checkBox")
        self.verticalLayout.addWidget(self.controlIslandLockWidth_checkBox)

        self.verticalLayout_3.addWidget(self.controlIslandAlign_groupBox)
        self.manipulationIslandAlign_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.manipulationIslandAlign_groupBox.setObjectName("manipulationIslandAlign_groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.manipulationIslandAlign_groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.manipulationIslandAlignTop_radioButton = QtWidgets.QRadioButton(self.manipulationIslandAlign_groupBox)
        self.manipulationIslandAlignTop_radioButton.setObjectName("manipulationIslandAlignTop_radioButton")
        self.verticalLayout_2.addWidget(self.manipulationIslandAlignTop_radioButton)
        self.manipulationIslandAlignBottom_radioButton = QtWidgets.QRadioButton(self.manipulationIslandAlign_groupBox)

        self.manipulationIslandAlignBottom_radioButton.setObjectName("manipulationIslandAlignBottom_radioButton")
        self.verticalLayout_2.addWidget(self.manipulationIslandAlignBottom_radioButton)

        self.manipulationIslandLockHeight_checkBox = QtWidgets.QCheckBox(self.manipulationIslandAlign_groupBox)
        self.manipulationIslandLockHeight_checkBox.setObjectName("manipulationIslandLockHeight_checkBox")
        self.verticalLayout_2.addWidget(self.manipulationIslandLockHeight_checkBox)

        self.verticalLayout_3.addWidget(self.manipulationIslandAlign_groupBox)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        PreferencesWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(PreferencesWindow)
        self.statusbar.setObjectName("statusbar")
        PreferencesWindow.setStatusBar(self.statusbar)

        self.retranslateUi(PreferencesWindow)
        QtCore.QMetaObject.connectSlotsByName(PreferencesWindow)

        # region Font Control Events
        self.fontComboBox.currentFontChanged.connect(
            lambda: self.changeFont(PreferencesWindow, MainWindow, AboutWindow))

        self.fontSize_spinBox.valueChanged.connect(lambda: self.changeFont(PreferencesWindow, MainWindow, AboutWindow))
        # endregion

        # region Theme Control Events
        self.themeSelector_comboBox.addItems(qdarktheme.get_themes())
        self.themeSelector_comboBox.currentTextChanged.connect(self.themeController)
        # endregion

        # region Dynamic Island Align Events
        # For control island
        self.controlIslandAlignLeft_radioButton.clicked.connect(
            lambda: self.islandAlign(MainWindow, controlsDynamicIsland, "alignLeft"))
        self.controlIslandAlignRight_radioButton.clicked.connect(
            lambda: self.islandAlign(MainWindow, controlsDynamicIsland, "alignRight"))
        self.controlIslandLockWidth_checkBox.clicked.connect(
            lambda: self.lockIslands("lockWidth", controlsDynamicIsland))

        # For manipulation island
        self.manipulationIslandAlignTop_radioButton.clicked.connect(
            lambda: self.islandAlign(MainWindow, manipulationDynamicIsland, "alignTop"))
        self.manipulationIslandAlignBottom_radioButton.clicked.connect(
            lambda: self.islandAlign(MainWindow, manipulationDynamicIsland, "alignBottom"))
        self.manipulationIslandLockHeight_checkBox.clicked.connect(
            lambda: self.lockIslands("lockHeight", manipulationDynamicIsland))
        # endregion


    def retranslateUi(self, PreferencesWindow):
        _translate = QtCore.QCoreApplication.translate
        PreferencesWindow.setWindowTitle(_translate("PreferencesWindow", "Preferences"))
        self.appearance_groupBox.setTitle(_translate("PreferencesWindow", "Appearance"))
        self.themeSelector_label.setText(_translate("PreferencesWindow", "Theme:"))
        self.themeSelector_comboBox.setStatusTip(_translate("PreferencesWindow", "Select a theme from the dropdown "))
        self.font_label.setText(_translate("PreferencesWindow", "Font:"))
        self.fontComboBox.setStatusTip(_translate("PreferencesWindow", "Change the font across the entire app"))
        self.fontSize_label.setText(_translate("PreferencesWindow", "Size:"))
        self.fontSize_spinBox.setStatusTip(
            _translate("PreferencesWindow", "Increase or decrease the font size across the entire app"))
        self.controlIslandAlign_groupBox.setTitle(_translate("PreferencesWindow", "Change Controls Island's Position"))
        self.controlIslandAlignLeft_radioButton.setStatusTip(
            _translate("PreferencesWindow", "Set control island to align left"))
        self.controlIslandAlignLeft_radioButton.setText(
            _translate("PreferencesWindow", "Set control island to align left"))
        self.controlIslandAlignRight_radioButton.setStatusTip(
            _translate("PreferencesWindow", "Set control island to align right"))
        self.controlIslandAlignRight_radioButton.setText(
            _translate("PreferencesWindow", "Set control island to align right"))

        self.controlIslandLockWidth_checkBox.setStatusTip(
            _translate("PreferencesWindow", "Lock control island's width"))
        self.controlIslandLockWidth_checkBox.setText(
            _translate("PreferencesWindow", "Lock control island's width"))

        self.manipulationIslandAlign_groupBox.setTitle(
            _translate("PreferencesWindow", "Change Manipulation Island's Position"))
        self.manipulationIslandAlignTop_radioButton.setStatusTip(
            _translate("PreferencesWindow", "Set manipulation island to align top"))
        self.manipulationIslandAlignTop_radioButton.setText(
            _translate("PreferencesWindow", "Set manipulation island to align top"))
        self.manipulationIslandAlignBottom_radioButton.setStatusTip(
            _translate("PreferencesWindow", "Set manipulation island to align bottom"))
        self.manipulationIslandAlignBottom_radioButton.setText(
            _translate("PreferencesWindow", "Set manipulation island to align bottom"))

        self.manipulationIslandLockHeight_checkBox.setStatusTip(
            _translate("PreferencesWindow", "Lock manipulation island's height"))
        self.manipulationIslandLockHeight_checkBox.setText(
            _translate("PreferencesWindow", "Lock manipulation island's height"))

        self.label.setText(_translate("PreferencesWindow",
                                      "Tip: You can adjust both the control island\'s and manipulation island\'s align position by dragging them with a left mouse button click (LMB click)."))

    # Call the setStyleSheet method for every callable window and set the font accordingly to fontComboBox
    def changeFont(self, PreferencesWindow, MainWindow, AboutWindow):
        font = self.fontComboBox.currentText()
        fontSize = self.fontSize_spinBox.value()
        styleSheet = f"font: {fontSize}pt {font}"
        PreferencesWindow.setStyleSheet(styleSheet)
        MainWindow.setStyleSheet(styleSheet)
        AboutWindow.setStyleSheet(styleSheet)

    # Control the theme from the theme comboBox
    def themeController(self):
        if self.themeSelector_comboBox.currentText() == "dark":
            qdarktheme.setup_theme(custom_colors={"primary": "#FCCD60"}, theme="dark")
        elif self.themeSelector_comboBox.currentText() == "light":
            qdarktheme.setup_theme(custom_colors={"primary": "#000000"}, theme="light")
        else:
            qdarktheme.setup_theme(theme="auto")

        # qdarktheme.setup_theme(custom_colors={"primary": "#000000"}, theme="light")

    # Align the dock widgets to allowed areas
    def islandAlign(self, MainWindow, dynamicIsland, objectName):
        if objectName == "alignLeft":
            MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), dynamicIsland)

        elif objectName == "alignRight":
            MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), dynamicIsland)

        elif objectName == "alignTop":
            MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), dynamicIsland)

        elif objectName == "alignBottom":
            MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea.BottomDockWidgetArea, dynamicIsland)
            # This one is different because of some weird glitch, Qt does not allow me to set an integer for the bottom area so I forced it with keywords

    # Lock the island's maximum size policies
    def lockIslands(self, lockType, dynamicIsland):
        if (lockType == "lockWidth") and (self.controlIslandLockWidth_checkBox.isChecked()):
            dynamicIsland.setMaximumWidth(75)
        elif (lockType == "lockWidth") and (self.controlIslandLockWidth_checkBox.isChecked() == False):
            dynamicIsland.setMaximumWidth(524287)
        elif (lockType == "lockHeight") and (self.manipulationIslandLockHeight_checkBox.isChecked()):
            dynamicIsland.setMaximumHeight(100)

        elif (lockType == "lockHeight") and (self.manipulationIslandLockHeight_checkBox.isChecked() == False):
            dynamicIsland.setMaximumHeight(524287)
