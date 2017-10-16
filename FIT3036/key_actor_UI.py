#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'key_actor.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import main_actors

class Ui_key_actor_window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.actors = main_actors.EnronGraph()

    def setupUi(self, key_actor_window):
        key_actor_window.setObjectName("key_actor_window")
        key_actor_window.resize(373, 600)
        self.centralwidget = QtWidgets.QWidget(key_actor_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.metric_combo_box = QtWidgets.QComboBox(self.centralwidget)
        self.metric_combo_box.setObjectName("metric_combo_box")
        self.verticalLayout.addWidget(self.metric_combo_box)

        # Add metric titles
        metric_titles = ["Degree", "Closeness", "Betweenness", "Eigenvector"]
        self.metric_combo_box.addItems(metric_titles)

        self.metric_tree = QtWidgets.QTreeWidget(self.centralwidget)
        self.metric_tree.setObjectName("metric_tree")

        # ComboBox item changed
        self.metric_combo_box.currentIndexChanged.connect(self.update_tree)

        # Set headings
        self.metric_tree.headerItem().setText(0, "Employee Name")
        self.metric_tree.headerItem().setText(1, "Score")
        self.metric_tree.resizeColumnToContents(0)

        self.verticalLayout.addWidget(self.metric_tree)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        key_actor_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(key_actor_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 373, 25))
        self.menubar.setObjectName("menubar")
        key_actor_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(key_actor_window)
        self.statusbar.setObjectName("statusbar")
        key_actor_window.setStatusBar(self.statusbar)

        self.retranslateUi(key_actor_window)
        QtCore.QMetaObject.connectSlotsByName(key_actor_window)

    def retranslateUi(self, key_actor_window):
        _translate = QtCore.QCoreApplication.translate
        key_actor_window.setWindowTitle(_translate("key_actor_window", "Key Actors"))

    def update_tree(self):
        self.metric_tree.clear()

        metric_name = str(self.metric_combo_box.currentText())

        if metric_name == "Degree":
            metric_set = self.actors.metric_degree
        elif metric_name == "Closeness":
            metric_set = self.actors.metric_closeness
        elif metric_name == "Betweenness":
            metric_set = self.actors.metric_betweennness
        elif metric_name == "Eigenvector":
            metric_set = self.actors.metric_eigenvector
        else:
            metric_set = self.actors.metric_degree

        for metric in range(len(metric_set)):
            QtWidgets.QTreeWidgetItem(self.metric_tree)
            for value in range(len(metric_set[metric])):
                self.metric_tree.topLevelItem(metric).setText(value, str(metric_set[metric][value]))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    key_actor_window = QtWidgets.QMainWindow()
    ui = Ui_key_actor_window()
    ui.setupUi(key_actor_window)
    ui.update_tree()
    key_actor_window.show()
    sys.exit(app.exec_())

