# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/dominik/projects/gns3-gui/gns3/modules/docker/ui/docker_vm_configuration_page.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dockerVMConfigPageWidget(object):
    def setupUi(self, dockerVMConfigPageWidget):
        dockerVMConfigPageWidget.setObjectName("dockerVMConfigPageWidget")
        dockerVMConfigPageWidget.resize(613, 524)
        self.verticalLayout = QtWidgets.QVBoxLayout(dockerVMConfigPageWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uiTabWidget = QtWidgets.QTabWidget(dockerVMConfigPageWidget)
        self.uiTabWidget.setObjectName("uiTabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setObjectName("gridLayout")
        self.uiNameLineEdit = QtWidgets.QLineEdit(self.tab)
        self.uiNameLineEdit.setObjectName("uiNameLineEdit")
        self.gridLayout.addWidget(self.uiNameLineEdit, 0, 1, 1, 1)
        self.uiConsoleTypeLabel = QtWidgets.QLabel(self.tab)
        self.uiConsoleTypeLabel.setObjectName("uiConsoleTypeLabel")
        self.gridLayout.addWidget(self.uiConsoleTypeLabel, 6, 0, 1, 1)
        self.uiAdapterLabel = QtWidgets.QLabel(self.tab)
        self.uiAdapterLabel.setObjectName("uiAdapterLabel")
        self.gridLayout.addWidget(self.uiAdapterLabel, 5, 0, 1, 1)
        self.uiCMDLineEdit = QtWidgets.QLineEdit(self.tab)
        self.uiCMDLineEdit.setObjectName("uiCMDLineEdit")
        self.gridLayout.addWidget(self.uiCMDLineEdit, 4, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 8, 0, 1, 1)
        self.uiConsoleHttpPortSpinBox = QtWidgets.QSpinBox(self.tab)
        self.uiConsoleHttpPortSpinBox.setMinimum(1)
        self.uiConsoleHttpPortSpinBox.setMaximum(65535)
        self.uiConsoleHttpPortSpinBox.setObjectName("uiConsoleHttpPortSpinBox")
        self.gridLayout.addWidget(self.uiConsoleHttpPortSpinBox, 8, 1, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.uiSymbolLineEdit = QtWidgets.QLineEdit(self.tab)
        self.uiSymbolLineEdit.setObjectName("uiSymbolLineEdit")
        self.horizontalLayout_7.addWidget(self.uiSymbolLineEdit)
        self.uiSymbolToolButton = QtWidgets.QToolButton(self.tab)
        self.uiSymbolToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiSymbolToolButton.setObjectName("uiSymbolToolButton")
        self.horizontalLayout_7.addWidget(self.uiSymbolToolButton)
        self.gridLayout.addLayout(self.horizontalLayout_7, 3, 1, 1, 1)
        self.uiDefaultNameFormatLabel = QtWidgets.QLabel(self.tab)
        self.uiDefaultNameFormatLabel.setObjectName("uiDefaultNameFormatLabel")
        self.gridLayout.addWidget(self.uiDefaultNameFormatLabel, 1, 0, 1, 1)
        self.uiEnvironmentLabel = QtWidgets.QLabel(self.tab)
        self.uiEnvironmentLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.uiEnvironmentLabel.setWordWrap(False)
        self.uiEnvironmentLabel.setObjectName("uiEnvironmentLabel")
        self.gridLayout.addWidget(self.uiEnvironmentLabel, 10, 0, 1, 1)
        self.uiNetworkConfigEditButton = QtWidgets.QPushButton(self.tab)
        self.uiNetworkConfigEditButton.setObjectName("uiNetworkConfigEditButton")
        self.gridLayout.addWidget(self.uiNetworkConfigEditButton, 11, 1, 1, 1)
        self.uiConsoleTypeComboBox = QtWidgets.QComboBox(self.tab)
        self.uiConsoleTypeComboBox.setObjectName("uiConsoleTypeComboBox")
        self.uiConsoleTypeComboBox.addItem("")
        self.uiConsoleTypeComboBox.addItem("")
        self.uiConsoleTypeComboBox.addItem("")
        self.uiConsoleTypeComboBox.addItem("")
        self.gridLayout.addWidget(self.uiConsoleTypeComboBox, 6, 1, 1, 1)
        self.uiNetworkConfigLabel = QtWidgets.QLabel(self.tab)
        self.uiNetworkConfigLabel.setObjectName("uiNetworkConfigLabel")
        self.gridLayout.addWidget(self.uiNetworkConfigLabel, 11, 0, 1, 1)
        self.uiDefaultNameFormatLineEdit = QtWidgets.QLineEdit(self.tab)
        self.uiDefaultNameFormatLineEdit.setObjectName("uiDefaultNameFormatLineEdit")
        self.gridLayout.addWidget(self.uiDefaultNameFormatLineEdit, 1, 1, 1, 1)
        self.uiNameLabel = QtWidgets.QLabel(self.tab)
        self.uiNameLabel.setObjectName("uiNameLabel")
        self.gridLayout.addWidget(self.uiNameLabel, 0, 0, 1, 1)
        self.uiAdapterSpinBox = QtWidgets.QSpinBox(self.tab)
        self.uiAdapterSpinBox.setMinimum(1)
        self.uiAdapterSpinBox.setObjectName("uiAdapterSpinBox")
        self.gridLayout.addWidget(self.uiAdapterSpinBox, 5, 1, 1, 1)
        self.uiEnvironmentTextEdit = QtWidgets.QTextEdit(self.tab)
        self.uiEnvironmentTextEdit.setObjectName("uiEnvironmentTextEdit")
        self.gridLayout.addWidget(self.uiEnvironmentTextEdit, 10, 1, 1, 1)
        self.uiCategoryComboBox = QtWidgets.QComboBox(self.tab)
        self.uiCategoryComboBox.setObjectName("uiCategoryComboBox")
        self.uiCategoryComboBox.addItem("")
        self.uiCategoryComboBox.addItem("")
        self.uiCategoryComboBox.addItem("")
        self.uiCategoryComboBox.addItem("")
        self.gridLayout.addWidget(self.uiCategoryComboBox, 2, 1, 1, 1)
        self.uiCategoryLabel = QtWidgets.QLabel(self.tab)
        self.uiCategoryLabel.setObjectName("uiCategoryLabel")
        self.gridLayout.addWidget(self.uiCategoryLabel, 2, 0, 1, 1)
        self.uiCMDLabel = QtWidgets.QLabel(self.tab)
        self.uiCMDLabel.setObjectName("uiCMDLabel")
        self.gridLayout.addWidget(self.uiCMDLabel, 4, 0, 1, 1)
        self.uiConsoleResolutionComboBox = QtWidgets.QComboBox(self.tab)
        self.uiConsoleResolutionComboBox.setObjectName("uiConsoleResolutionComboBox")
        self.uiConsoleResolutionComboBox.addItem("")
        self.uiConsoleResolutionComboBox.addItem("")
        self.uiConsoleResolutionComboBox.addItem("")
        self.uiConsoleResolutionComboBox.addItem("")
        self.uiConsoleResolutionComboBox.addItem("")
        self.uiConsoleResolutionComboBox.addItem("")
        self.uiConsoleResolutionComboBox.addItem("")
        self.gridLayout.addWidget(self.uiConsoleResolutionComboBox, 7, 1, 1, 1)
        self.uiSymbolLabel = QtWidgets.QLabel(self.tab)
        self.uiSymbolLabel.setObjectName("uiSymbolLabel")
        self.gridLayout.addWidget(self.uiSymbolLabel, 3, 0, 1, 1)
        self.uiConsoleResolutionLabel = QtWidgets.QLabel(self.tab)
        self.uiConsoleResolutionLabel.setObjectName("uiConsoleResolutionLabel")
        self.gridLayout.addWidget(self.uiConsoleResolutionLabel, 7, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 9, 0, 1, 1)
        self.uiHttpConsolePathLineEdit = QtWidgets.QLineEdit(self.tab)
        self.uiHttpConsolePathLineEdit.setObjectName("uiHttpConsolePathLineEdit")
        self.gridLayout.addWidget(self.uiHttpConsolePathLineEdit, 9, 1, 1, 1)
        self.uiTabWidget.addTab(self.tab, "")
        self.advancedTab = QtWidgets.QWidget()
        self.advancedTab.setObjectName("advancedTab")
        self.uiExtraHostsLabel = QtWidgets.QLabel(self.advancedTab)
        self.uiExtraHostsLabel.setGeometry(QtCore.QRect(10, 10, 152, 82))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiExtraHostsLabel.sizePolicy().hasHeightForWidth())
        self.uiExtraHostsLabel.setSizePolicy(sizePolicy)
        self.uiExtraHostsLabel.setWordWrap(True)
        self.uiExtraHostsLabel.setObjectName("uiExtraHostsLabel")
        self.uiExtraHostsTextEdit = QtWidgets.QTextEdit(self.advancedTab)
        self.uiExtraHostsTextEdit.setGeometry(QtCore.QRect(168, 10, 413, 82))
        self.uiExtraHostsTextEdit.setObjectName("uiExtraHostsTextEdit")
        self.uiTabWidget.addTab(self.advancedTab, "")
        self.verticalLayout.addWidget(self.uiTabWidget)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(dockerVMConfigPageWidget)
        self.uiTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(dockerVMConfigPageWidget)

    def retranslateUi(self, dockerVMConfigPageWidget):
        _translate = QtCore.QCoreApplication.translate
        dockerVMConfigPageWidget.setWindowTitle(_translate("dockerVMConfigPageWidget", "Docker image configuration"))
        self.uiConsoleTypeLabel.setText(_translate("dockerVMConfigPageWidget", "Console type:"))
        self.uiAdapterLabel.setText(_translate("dockerVMConfigPageWidget", "Adapters:"))
        self.label.setText(_translate("dockerVMConfigPageWidget", "HTTP port in the container:"))
        self.uiSymbolToolButton.setText(_translate("dockerVMConfigPageWidget", "&Browse..."))
        self.uiDefaultNameFormatLabel.setText(_translate("dockerVMConfigPageWidget", "Default name format"))
        self.uiEnvironmentLabel.setText(_translate("dockerVMConfigPageWidget", "Environment variables:\n"
"(KEY=VALUE, one per line)"))
        self.uiNetworkConfigEditButton.setText(_translate("dockerVMConfigPageWidget", "Edit"))
        self.uiConsoleTypeComboBox.setItemText(0, _translate("dockerVMConfigPageWidget", "telnet"))
        self.uiConsoleTypeComboBox.setItemText(1, _translate("dockerVMConfigPageWidget", "vnc"))
        self.uiConsoleTypeComboBox.setItemText(2, _translate("dockerVMConfigPageWidget", "http"))
        self.uiConsoleTypeComboBox.setItemText(3, _translate("dockerVMConfigPageWidget", "https"))
        self.uiNetworkConfigLabel.setText(_translate("dockerVMConfigPageWidget", "Network configuration"))
        self.uiNameLabel.setText(_translate("dockerVMConfigPageWidget", "Name:"))
        self.uiCategoryComboBox.setItemText(0, _translate("dockerVMConfigPageWidget", "Router"))
        self.uiCategoryComboBox.setItemText(1, _translate("dockerVMConfigPageWidget", "Switch"))
        self.uiCategoryComboBox.setItemText(2, _translate("dockerVMConfigPageWidget", "Guest"))
        self.uiCategoryComboBox.setItemText(3, _translate("dockerVMConfigPageWidget", "Security device"))
        self.uiCategoryLabel.setText(_translate("dockerVMConfigPageWidget", "Category"))
        self.uiCMDLabel.setText(_translate("dockerVMConfigPageWidget", "Start command:"))
        self.uiConsoleResolutionComboBox.setItemText(0, _translate("dockerVMConfigPageWidget", "1920x1080"))
        self.uiConsoleResolutionComboBox.setItemText(1, _translate("dockerVMConfigPageWidget", "1366x768"))
        self.uiConsoleResolutionComboBox.setItemText(2, _translate("dockerVMConfigPageWidget", "1280x1024"))
        self.uiConsoleResolutionComboBox.setItemText(3, _translate("dockerVMConfigPageWidget", "1280x800"))
        self.uiConsoleResolutionComboBox.setItemText(4, _translate("dockerVMConfigPageWidget", "1024x768"))
        self.uiConsoleResolutionComboBox.setItemText(5, _translate("dockerVMConfigPageWidget", "800x600"))
        self.uiConsoleResolutionComboBox.setItemText(6, _translate("dockerVMConfigPageWidget", "640x480"))
        self.uiSymbolLabel.setText(_translate("dockerVMConfigPageWidget", "Symbol:"))
        self.uiConsoleResolutionLabel.setText(_translate("dockerVMConfigPageWidget", "VNC console resolution:"))
        self.label_2.setText(_translate("dockerVMConfigPageWidget", "HTTP path:"))
        self.uiTabWidget.setTabText(self.uiTabWidget.indexOf(self.tab), _translate("dockerVMConfigPageWidget", "General settings"))
        self.uiExtraHostsLabel.setText(_translate("dockerVMConfigPageWidget", "Extra hosts added to \n"
"/etc/hosts file.\n"
"(hostname:IP, one per line)"))
        self.uiTabWidget.setTabText(self.uiTabWidget.indexOf(self.advancedTab), _translate("dockerVMConfigPageWidget", "Advanced"))

