#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'database_UI.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import db_manager, sys, network, key_actor_UI, key_term_UI

class Ui_window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.dbu = db_manager.DatabaseUtility()
        self.graph = network.SocialNetwork()

    def setupUi(self, window):
        window.setObjectName("window")
        window.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.database_view_label = QtWidgets.QLabel(self.centralwidget)
        self.database_view_label.setObjectName("database_view_label")
        self.verticalLayout.addWidget(self.database_view_label)
        self.database_viewer = QtWidgets.QTreeWidget(self.centralwidget)
        self.database_viewer.setObjectName("database_viewer")
        self.verticalLayout.addWidget(self.database_viewer)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.available_table_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.available_table_label.sizePolicy().hasHeightForWidth())
        self.available_table_label.setSizePolicy(sizePolicy)
        self.available_table_label.setObjectName("available_table_label")
        self.verticalLayout_2.addWidget(self.available_table_label)
        self.table_list = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_list.sizePolicy().hasHeightForWidth())
        self.table_list.setSizePolicy(sizePolicy)
        self.table_list.setObjectName("table_list")
        self.verticalLayout_2.addWidget(self.table_list)
        self.load_db_btn = QtWidgets.QPushButton(self.centralwidget)
        self.load_db_btn.setObjectName("load_db_btn")

        # Load selected database
        self.load_db_btn.clicked.connect(self.load_table)
        self.verticalLayout_2.addWidget(self.load_db_btn)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.show_graph = QtWidgets.QPushButton(self.centralwidget)
        self.show_graph.setObjectName("show_graph")

        # Display network graph when clicked
        self.show_graph.clicked.connect(self.load_graph)
        self.verticalLayout_2.addWidget(self.show_graph)
        self.actors_btn = QtWidgets.QPushButton(self.centralwidget)
        self.actors_btn.setObjectName("actors_btn")
        self.verticalLayout_2.addWidget(self.actors_btn)

        # Open metrics in UI
        self.actors_btn.clicked.connect(self.show_metric)

        self.terms_btn = QtWidgets.QPushButton(self.centralwidget)
        self.terms_btn.setObjectName("terms_btn")
        self.verticalLayout_2.addWidget(self.terms_btn)

        # Open clustering in UI
        self.terms_btn.clicked.connect(self.show_key_terms)

        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(window)
        self.statusbar.setObjectName("statusbar")
        window.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(window)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("window", "Enron Database"))
        self.database_view_label.setText(_translate("window", "Database"))
        self.available_table_label.setText(_translate("window", "Avaliable Tables"))
        self.load_db_btn.setText(_translate("window", "Load Table"))
        self.show_graph.setText(_translate("window", "Show Network Graph"))
        self.actors_btn.setText(_translate("window", "Show Main Actors"))
        self.terms_btn.setText(_translate("window", "Show Key Terms"))
        self.menuFile.setTitle(_translate("window", "File"))
        self.actionExit.setText(_translate("window", "Exit"))

    def update_tree(self, table_name):
        col = self.dbu.get_columns(table_name)
        table = self.dbu.get_table(table_name)

        self.database_viewer.setColumnCount(len(col))

        for c in range(len(col)):
            self.database_viewer.headerItem().setText(c, col[c][0])

        self.database_viewer.clear()

        for item in range(len(table)):
            QtWidgets.QTreeWidgetItem(self.database_viewer)
            for value in range(len(table[item])):
                self.database_viewer.topLevelItem(item).setText(value, str(table[item][value]))

    def update_tables(self):
        tables = self.dbu.get_table_names()

        names = []
        for c in range(len(tables)):
            names.append(tables[c][0])
        self.table_list.addItems(names)

    def load_table(self):
        table = self.table_list.currentItem().text()
        self.update_tree(table)

    def load_graph(self):
        self.graph.find_connections()
        self.graph.construct_graph()
        self.graph.draw_graph()

    def show_metric(self):
        self.window = QtWidgets.QMainWindow()
        self.actors = key_actor_UI.Ui_key_actor_window()
        self.actors.setupUi(self.window)
        self.actors.update_tree()
        self.window.show()

    def show_key_terms(self):
        self.window = QtWidgets.QMainWindow()
        self.term = key_term_UI.Ui_key_term_window()
        self.term.setupUi(self.window)
        self.term.update_tree()
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_window()
    ui.setupUi(window)
    ui.update_tree('employeelist')
    ui.update_tables()
    window.show()
    sys.exit(app.exec_())

