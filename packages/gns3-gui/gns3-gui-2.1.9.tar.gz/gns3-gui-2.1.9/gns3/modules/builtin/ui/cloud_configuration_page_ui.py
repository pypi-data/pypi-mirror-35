# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/grossmj/PycharmProjects/gns3-gui/gns3/modules/builtin/ui/cloud_configuration_page.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_cloudConfigPageWidget(object):
    def setupUi(self, cloudConfigPageWidget):
        cloudConfigPageWidget.setObjectName("cloudConfigPageWidget")
        cloudConfigPageWidget.resize(1000, 378)
        self.verticalLayout = QtWidgets.QVBoxLayout(cloudConfigPageWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uiTabWidget = QtWidgets.QTabWidget(cloudConfigPageWidget)
        self.uiTabWidget.setObjectName("uiTabWidget")
        self.EthernetTab = QtWidgets.QWidget()
        self.EthernetTab.setObjectName("EthernetTab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.EthernetTab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.uiEthernetComboBox = QtWidgets.QComboBox(self.EthernetTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiEthernetComboBox.sizePolicy().hasHeightForWidth())
        self.uiEthernetComboBox.setSizePolicy(sizePolicy)
        self.uiEthernetComboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.uiEthernetComboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.uiEthernetComboBox.setObjectName("uiEthernetComboBox")
        self.gridLayout_3.addWidget(self.uiEthernetComboBox, 0, 0, 1, 1)
        self.uiAddEthernetPushButton = QtWidgets.QPushButton(self.EthernetTab)
        self.uiAddEthernetPushButton.setObjectName("uiAddEthernetPushButton")
        self.gridLayout_3.addWidget(self.uiAddEthernetPushButton, 0, 2, 1, 1)
        self.uiAddAllEthernetPushButton = QtWidgets.QPushButton(self.EthernetTab)
        self.uiAddAllEthernetPushButton.setObjectName("uiAddAllEthernetPushButton")
        self.gridLayout_3.addWidget(self.uiAddAllEthernetPushButton, 0, 3, 1, 1)
        self.uiDeleteEthernetPushButton = QtWidgets.QPushButton(self.EthernetTab)
        self.uiDeleteEthernetPushButton.setEnabled(False)
        self.uiDeleteEthernetPushButton.setObjectName("uiDeleteEthernetPushButton")
        self.gridLayout_3.addWidget(self.uiDeleteEthernetPushButton, 0, 5, 1, 1)
        self.uiEthernetListWidget = QtWidgets.QListWidget(self.EthernetTab)
        self.uiEthernetListWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.uiEthernetListWidget.setObjectName("uiEthernetListWidget")
        self.gridLayout_3.addWidget(self.uiEthernetListWidget, 1, 0, 1, 6)
        self.uiEthernetWarningPushButton = QtWidgets.QPushButton(self.EthernetTab)
        self.uiEthernetWarningPushButton.setText("")
        self.uiEthernetWarningPushButton.setObjectName("uiEthernetWarningPushButton")
        self.gridLayout_3.addWidget(self.uiEthernetWarningPushButton, 0, 1, 1, 1)
        self.uiShowSpecialInterfacesCheckBox = QtWidgets.QCheckBox(self.EthernetTab)
        self.uiShowSpecialInterfacesCheckBox.setObjectName("uiShowSpecialInterfacesCheckBox")
        self.gridLayout_3.addWidget(self.uiShowSpecialInterfacesCheckBox, 2, 0, 1, 2)
        self.uiRefreshEthernetPushButton = QtWidgets.QPushButton(self.EthernetTab)
        self.uiRefreshEthernetPushButton.setObjectName("uiRefreshEthernetPushButton")
        self.gridLayout_3.addWidget(self.uiRefreshEthernetPushButton, 0, 4, 1, 1)
        self.uiEthernetListWidget.raise_()
        self.uiEthernetComboBox.raise_()
        self.uiAddEthernetPushButton.raise_()
        self.uiDeleteEthernetPushButton.raise_()
        self.uiAddAllEthernetPushButton.raise_()
        self.uiShowSpecialInterfacesCheckBox.raise_()
        self.uiEthernetWarningPushButton.raise_()
        self.uiRefreshEthernetPushButton.raise_()
        self.uiTabWidget.addTab(self.EthernetTab, "")
        self.TAPTab = QtWidgets.QWidget()
        self.TAPTab.setObjectName("TAPTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.TAPTab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.uiDeleteTAPPushButton = QtWidgets.QPushButton(self.TAPTab)
        self.uiDeleteTAPPushButton.setEnabled(False)
        self.uiDeleteTAPPushButton.setObjectName("uiDeleteTAPPushButton")
        self.gridLayout_2.addWidget(self.uiDeleteTAPPushButton, 1, 5, 1, 1)
        self.uiTAPListWidget = QtWidgets.QListWidget(self.TAPTab)
        self.uiTAPListWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.uiTAPListWidget.setObjectName("uiTAPListWidget")
        self.gridLayout_2.addWidget(self.uiTAPListWidget, 2, 0, 1, 6)
        self.uiTAPLineEdit = QtWidgets.QLineEdit(self.TAPTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiTAPLineEdit.sizePolicy().hasHeightForWidth())
        self.uiTAPLineEdit.setSizePolicy(sizePolicy)
        self.uiTAPLineEdit.setObjectName("uiTAPLineEdit")
        self.gridLayout_2.addWidget(self.uiTAPLineEdit, 1, 1, 1, 1)
        self.uiAddTAPPushButton = QtWidgets.QPushButton(self.TAPTab)
        self.uiAddTAPPushButton.setObjectName("uiAddTAPPushButton")
        self.gridLayout_2.addWidget(self.uiAddTAPPushButton, 1, 2, 1, 1)
        self.uiTAPComboBox = QtWidgets.QComboBox(self.TAPTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiTAPComboBox.sizePolicy().hasHeightForWidth())
        self.uiTAPComboBox.setSizePolicy(sizePolicy)
        self.uiTAPComboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.uiTAPComboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.uiTAPComboBox.setObjectName("uiTAPComboBox")
        self.gridLayout_2.addWidget(self.uiTAPComboBox, 0, 1, 1, 5)
        self.uiAddAllTAPPushButton = QtWidgets.QPushButton(self.TAPTab)
        self.uiAddAllTAPPushButton.setObjectName("uiAddAllTAPPushButton")
        self.gridLayout_2.addWidget(self.uiAddAllTAPPushButton, 1, 3, 1, 1)
        self.uiRefreshTAPPushButton = QtWidgets.QPushButton(self.TAPTab)
        self.uiRefreshTAPPushButton.setObjectName("uiRefreshTAPPushButton")
        self.gridLayout_2.addWidget(self.uiRefreshTAPPushButton, 1, 4, 1, 1)
        self.uiTabWidget.addTab(self.TAPTab, "")
        self.UDPTab = QtWidgets.QWidget()
        self.UDPTab.setObjectName("UDPTab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.UDPTab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.uiUDPTunnelSettingsGroupBox = QtWidgets.QGroupBox(self.UDPTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiUDPTunnelSettingsGroupBox.sizePolicy().hasHeightForWidth())
        self.uiUDPTunnelSettingsGroupBox.setSizePolicy(sizePolicy)
        self.uiUDPTunnelSettingsGroupBox.setObjectName("uiUDPTunnelSettingsGroupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.uiUDPTunnelSettingsGroupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.uiRemoteHostLineEdit = QtWidgets.QLineEdit(self.uiUDPTunnelSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRemoteHostLineEdit.sizePolicy().hasHeightForWidth())
        self.uiRemoteHostLineEdit.setSizePolicy(sizePolicy)
        self.uiRemoteHostLineEdit.setMinimumSize(QtCore.QSize(80, 0))
        self.uiRemoteHostLineEdit.setObjectName("uiRemoteHostLineEdit")
        self.gridLayout_4.addWidget(self.uiRemoteHostLineEdit, 2, 1, 1, 1)
        self.uiRemotePortLabel = QtWidgets.QLabel(self.uiUDPTunnelSettingsGroupBox)
        self.uiRemotePortLabel.setObjectName("uiRemotePortLabel")
        self.gridLayout_4.addWidget(self.uiRemotePortLabel, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uiAddUDPPushButton = QtWidgets.QPushButton(self.uiUDPTunnelSettingsGroupBox)
        self.uiAddUDPPushButton.setObjectName("uiAddUDPPushButton")
        self.horizontalLayout.addWidget(self.uiAddUDPPushButton)
        self.uiDeleteUDPPushButton = QtWidgets.QPushButton(self.uiUDPTunnelSettingsGroupBox)
        self.uiDeleteUDPPushButton.setEnabled(False)
        self.uiDeleteUDPPushButton.setObjectName("uiDeleteUDPPushButton")
        self.horizontalLayout.addWidget(self.uiDeleteUDPPushButton)
        spacerItem = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout_4.addLayout(self.horizontalLayout, 4, 0, 1, 2)
        self.uiRemotePortSpinBox = QtWidgets.QSpinBox(self.uiUDPTunnelSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRemotePortSpinBox.sizePolicy().hasHeightForWidth())
        self.uiRemotePortSpinBox.setSizePolicy(sizePolicy)
        self.uiRemotePortSpinBox.setMaximum(65535)
        self.uiRemotePortSpinBox.setProperty("value", 20000)
        self.uiRemotePortSpinBox.setObjectName("uiRemotePortSpinBox")
        self.gridLayout_4.addWidget(self.uiRemotePortSpinBox, 3, 1, 1, 1)
        self.uiUDPNameLineEdit = QtWidgets.QLineEdit(self.uiUDPTunnelSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiUDPNameLineEdit.sizePolicy().hasHeightForWidth())
        self.uiUDPNameLineEdit.setSizePolicy(sizePolicy)
        self.uiUDPNameLineEdit.setObjectName("uiUDPNameLineEdit")
        self.gridLayout_4.addWidget(self.uiUDPNameLineEdit, 0, 1, 1, 1)
        self.uiRemoteHostLabel = QtWidgets.QLabel(self.uiUDPTunnelSettingsGroupBox)
        self.uiRemoteHostLabel.setObjectName("uiRemoteHostLabel")
        self.gridLayout_4.addWidget(self.uiRemoteHostLabel, 2, 0, 1, 1)
        self.uiLocalPortSpinBox = QtWidgets.QSpinBox(self.uiUDPTunnelSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiLocalPortSpinBox.sizePolicy().hasHeightForWidth())
        self.uiLocalPortSpinBox.setSizePolicy(sizePolicy)
        self.uiLocalPortSpinBox.setMaximum(65535)
        self.uiLocalPortSpinBox.setProperty("value", 30000)
        self.uiLocalPortSpinBox.setObjectName("uiLocalPortSpinBox")
        self.gridLayout_4.addWidget(self.uiLocalPortSpinBox, 1, 1, 1, 1)
        self.uiLocalPortLabel = QtWidgets.QLabel(self.uiUDPTunnelSettingsGroupBox)
        self.uiLocalPortLabel.setObjectName("uiLocalPortLabel")
        self.gridLayout_4.addWidget(self.uiLocalPortLabel, 1, 0, 1, 1)
        self.uiUDPNameLabel = QtWidgets.QLabel(self.uiUDPTunnelSettingsGroupBox)
        self.uiUDPNameLabel.setObjectName("uiUDPNameLabel")
        self.gridLayout_4.addWidget(self.uiUDPNameLabel, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem1, 5, 0, 1, 1)
        self.gridLayout_5.addWidget(self.uiUDPTunnelSettingsGroupBox, 0, 0, 1, 1)
        self.uiUDPTunnelsGroupBox = QtWidgets.QGroupBox(self.UDPTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiUDPTunnelsGroupBox.sizePolicy().hasHeightForWidth())
        self.uiUDPTunnelsGroupBox.setSizePolicy(sizePolicy)
        self.uiUDPTunnelsGroupBox.setObjectName("uiUDPTunnelsGroupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.uiUDPTunnelsGroupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.uiUDPTreeWidget = QtWidgets.QTreeWidget(self.uiUDPTunnelsGroupBox)
        self.uiUDPTreeWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.uiUDPTreeWidget.setObjectName("uiUDPTreeWidget")
        self.verticalLayout_2.addWidget(self.uiUDPTreeWidget)
        self.gridLayout_5.addWidget(self.uiUDPTunnelsGroupBox, 0, 1, 1, 1)
        self.uiTabWidget.addTab(self.UDPTab, "")
        self.MiscTab = QtWidgets.QWidget()
        self.MiscTab.setObjectName("MiscTab")
        self.gridLayout = QtWidgets.QGridLayout(self.MiscTab)
        self.gridLayout.setObjectName("gridLayout")
        self.uiNameLabel = QtWidgets.QLabel(self.MiscTab)
        self.uiNameLabel.setObjectName("uiNameLabel")
        self.gridLayout.addWidget(self.uiNameLabel, 0, 0, 1, 1)
        self.uiNameLineEdit = QtWidgets.QLineEdit(self.MiscTab)
        self.uiNameLineEdit.setObjectName("uiNameLineEdit")
        self.gridLayout.addWidget(self.uiNameLineEdit, 0, 2, 1, 1)
        self.uiDefaultNameFormatLabel = QtWidgets.QLabel(self.MiscTab)
        self.uiDefaultNameFormatLabel.setObjectName("uiDefaultNameFormatLabel")
        self.gridLayout.addWidget(self.uiDefaultNameFormatLabel, 1, 0, 1, 2)
        self.uiDefaultNameFormatLineEdit = QtWidgets.QLineEdit(self.MiscTab)
        self.uiDefaultNameFormatLineEdit.setObjectName("uiDefaultNameFormatLineEdit")
        self.gridLayout.addWidget(self.uiDefaultNameFormatLineEdit, 1, 2, 1, 1)
        self.uiSymbolLabel = QtWidgets.QLabel(self.MiscTab)
        self.uiSymbolLabel.setObjectName("uiSymbolLabel")
        self.gridLayout.addWidget(self.uiSymbolLabel, 2, 0, 1, 2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.uiSymbolLineEdit = QtWidgets.QLineEdit(self.MiscTab)
        self.uiSymbolLineEdit.setObjectName("uiSymbolLineEdit")
        self.horizontalLayout_7.addWidget(self.uiSymbolLineEdit)
        self.uiSymbolToolButton = QtWidgets.QToolButton(self.MiscTab)
        self.uiSymbolToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiSymbolToolButton.setObjectName("uiSymbolToolButton")
        self.horizontalLayout_7.addWidget(self.uiSymbolToolButton)
        self.gridLayout.addLayout(self.horizontalLayout_7, 2, 2, 1, 1)
        self.uiCategoryLabel = QtWidgets.QLabel(self.MiscTab)
        self.uiCategoryLabel.setObjectName("uiCategoryLabel")
        self.gridLayout.addWidget(self.uiCategoryLabel, 3, 0, 1, 2)
        self.uiCategoryComboBox = QtWidgets.QComboBox(self.MiscTab)
        self.uiCategoryComboBox.setObjectName("uiCategoryComboBox")
        self.gridLayout.addWidget(self.uiCategoryComboBox, 3, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 399, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 4, 1, 1, 2)
        self.uiTabWidget.addTab(self.MiscTab, "")
        self.verticalLayout.addWidget(self.uiTabWidget)

        self.retranslateUi(cloudConfigPageWidget)
        self.uiTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(cloudConfigPageWidget)

    def retranslateUi(self, cloudConfigPageWidget):
        _translate = QtCore.QCoreApplication.translate
        cloudConfigPageWidget.setWindowTitle(_translate("cloudConfigPageWidget", "Cloud configuration"))
        cloudConfigPageWidget.setWhatsThis(_translate("cloudConfigPageWidget", "<html><head/><body><p>A cloud node allows you to connect your project to the &quot;real world&quot; (a network or host) using either an Ethernet interface, a TAP interface (Linux only) or even an UDP tunnel. <span style=\" font-weight:600;\">Please be aware that Wifi interfaces may not work properly.</span></p></body></html>"))
        self.uiAddEthernetPushButton.setText(_translate("cloudConfigPageWidget", "&Add"))
        self.uiAddAllEthernetPushButton.setText(_translate("cloudConfigPageWidget", "&Add all"))
        self.uiDeleteEthernetPushButton.setText(_translate("cloudConfigPageWidget", "&Delete"))
        self.uiEthernetListWidget.setSortingEnabled(True)
        self.uiShowSpecialInterfacesCheckBox.setText(_translate("cloudConfigPageWidget", "&Show special Ethernet interfaces"))
        self.uiRefreshEthernetPushButton.setText(_translate("cloudConfigPageWidget", "&Refresh"))
        self.uiTabWidget.setTabText(self.uiTabWidget.indexOf(self.EthernetTab), _translate("cloudConfigPageWidget", "Ethernet interfaces"))
        self.uiDeleteTAPPushButton.setText(_translate("cloudConfigPageWidget", "&Delete"))
        self.uiTAPListWidget.setSortingEnabled(True)
        self.uiAddTAPPushButton.setText(_translate("cloudConfigPageWidget", "&Add"))
        self.uiAddAllTAPPushButton.setText(_translate("cloudConfigPageWidget", "&Add all"))
        self.uiRefreshTAPPushButton.setText(_translate("cloudConfigPageWidget", "&Refresh"))
        self.uiTabWidget.setTabText(self.uiTabWidget.indexOf(self.TAPTab), _translate("cloudConfigPageWidget", "TAP interfaces"))
        self.uiUDPTunnelSettingsGroupBox.setTitle(_translate("cloudConfigPageWidget", "UDP tunnel settings"))
        self.uiRemoteHostLineEdit.setText(_translate("cloudConfigPageWidget", "127.0.0.1"))
        self.uiRemotePortLabel.setText(_translate("cloudConfigPageWidget", "Remote port:"))
        self.uiAddUDPPushButton.setText(_translate("cloudConfigPageWidget", "&Add"))
        self.uiDeleteUDPPushButton.setText(_translate("cloudConfigPageWidget", "&Delete"))
        self.uiUDPNameLineEdit.setText(_translate("cloudConfigPageWidget", "UDP tunnel 1"))
        self.uiRemoteHostLabel.setText(_translate("cloudConfigPageWidget", "Remote host:"))
        self.uiLocalPortLabel.setText(_translate("cloudConfigPageWidget", "Local port:"))
        self.uiUDPNameLabel.setText(_translate("cloudConfigPageWidget", "Name:"))
        self.uiUDPTunnelsGroupBox.setTitle(_translate("cloudConfigPageWidget", "UDP tunnels"))
        self.uiUDPTreeWidget.headerItem().setText(0, _translate("cloudConfigPageWidget", "Name"))
        self.uiUDPTreeWidget.headerItem().setText(1, _translate("cloudConfigPageWidget", "Local port"))
        self.uiUDPTreeWidget.headerItem().setText(2, _translate("cloudConfigPageWidget", "Remote host"))
        self.uiUDPTreeWidget.headerItem().setText(3, _translate("cloudConfigPageWidget", "Remote port"))
        self.uiTabWidget.setTabText(self.uiTabWidget.indexOf(self.UDPTab), _translate("cloudConfigPageWidget", "UDP tunnels"))
        self.uiNameLabel.setText(_translate("cloudConfigPageWidget", "Name:"))
        self.uiDefaultNameFormatLabel.setText(_translate("cloudConfigPageWidget", "Default name format:"))
        self.uiSymbolLabel.setText(_translate("cloudConfigPageWidget", "Symbol:"))
        self.uiSymbolToolButton.setText(_translate("cloudConfigPageWidget", "&Browse..."))
        self.uiCategoryLabel.setText(_translate("cloudConfigPageWidget", "Category:"))
        self.uiTabWidget.setTabText(self.uiTabWidget.indexOf(self.MiscTab), _translate("cloudConfigPageWidget", "Misc."))

