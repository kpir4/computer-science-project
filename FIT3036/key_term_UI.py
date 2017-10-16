#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'key_term.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import key_terms

class Ui_key_term_window(object):
    def setupUi(self, key_term_window):
        key_term_window.setObjectName("key_term_window")
        key_term_window.resize(373, 600)
        self.centralwidget = QtWidgets.QWidget(key_term_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.cluster_combo_box = QtWidgets.QComboBox(self.centralwidget)
        self.cluster_combo_box.setObjectName("cluster_combo_box")
        self.verticalLayout.addWidget(self.cluster_combo_box)

        # Add clustering technique titles
        cluster_titles = ["Kmeans", "Birch"]
        self.cluster_combo_box.addItems(cluster_titles)
        
        self.cluster_tree = QtWidgets.QTreeWidget(self.centralwidget)
        self.cluster_tree.setObjectName("cluster_tree")

        # ComboBox item changed
        self.cluster_combo_box.currentIndexChanged.connect(self.update_tree)

        # Set headings
        self.cluster_tree.headerItem().setText(0, "Key Terms  ")
        self.cluster_tree.headerItem().setText(1, "Score")
        self.cluster_tree.resizeColumnToContents(0)
        
        self.verticalLayout.addWidget(self.cluster_tree)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        key_term_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(key_term_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 373, 25))
        self.menubar.setObjectName("menubar")
        key_term_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(key_term_window)
        self.statusbar.setObjectName("statusbar")
        key_term_window.setStatusBar(self.statusbar)

        self.retranslateUi(key_term_window)
        QtCore.QMetaObject.connectSlotsByName(key_term_window)

    def retranslateUi(self, key_term_window):
        _translate = QtCore.QCoreApplication.translate
        key_term_window.setWindowTitle(_translate("key_term_window", "Key Terms"))
        
    def update_tree(self):
        self.cluster_tree.clear()

        cluster_name = str(self.cluster_combo_box.currentText())

        clusters = key_terms.find_key_terms(cluster_name.lower())

        cluster = []
        for i in clusters:
            for j in i:
                cluster.append(j)

        cluster.sort(key=lambda x: x[1], reverse=True)

        for term in range(len(cluster)):
            QtWidgets.QTreeWidgetItem(self.cluster_tree)
            for value in range(len(cluster[term])):
                self.cluster_tree.topLevelItem(term).setText(value, str(cluster[term][value]))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    key_term_window = QtWidgets.QMainWindow()
    ui = Ui_key_term_window()
    ui.setupUi(key_term_window)
    ui.update_tree()
    key_term_window.show()
    sys.exit(app.exec_())

