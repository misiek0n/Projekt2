# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Projekt2Dialog
                                 A QGIS plugin
 Projekt2
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-06-03
        git sha              : $Format:%H$
        copyright            : (C) 2023 by M.Bielecki, M.Chwałek
        email                : m.bielecki1909@o2.pl
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

import numpy as np
import math

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from qgis.core import Qgis, QgsVectorLayer, QgsGeometry, QgsFeature, QgsField, QgsProject, QgsPoint, QgsField, QgsFields
from qgis.core import QgsCoordinateReferenceSystem
from qgis.utils import iface


# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'Projekt2_dialog_base.ui'))


class Projekt2Dialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(Projekt2Dialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.pushButton_rysuj.setVisible(False)
        self.radioButton_m2.setVisible(False)
        self.radioButton_ar.setVisible(False)
        self.radioButton_ha.setVisible(False)
        self.label_jedn_pole.setVisible(False)
        self.pushButton_porow.setVisible(False)
        self.tableWidget_wybrane.setColumnCount(2)
        self.tableWidget_wybrane.setHorizontalHeaderLabels(['Nr', 'h'])
        self.comboBox_obliczenie.currentIndexChanged.connect(self.update_visibility)
        #self.comboBox_obliczenie.currentIndexChanged.connect(self.update_table)
        self.mMapLayerComboBox_layers.currentIndexChanged.connect(self.clear_porow_label)
        self.pushButton_oblicz.clicked.connect(self.calculate_height_diff)
        self.pushButton_oblicz.clicked.connect(self.calculate_field)
        self.pushButton_clear.clicked.connect(self.clear_display)
        self.pushButton_rysuj.clicked.connect(self.create_polygon)
        self.pushButton_porow.clicked.connect(self.compare_area)
        self.pushButton_explore.clicked.connect(self.explore)
        self.mMapLayerComboBox_layers.currentLayer().selectionChanged.connect(self.update_table)

    def update_visibility(self):
        selected_option = self.comboBox_obliczenie.currentText()
        if selected_option == 'Pole powierzchni':
            self.radioButton_m2.setVisible(True)
            self.radioButton_ar.setVisible(True)
            self.radioButton_ha.setVisible(True)
            self.label_jedn_pole.setVisible(True)
            self.pushButton_rysuj.setVisible(True)
            self.pushButton_porow.setVisible(True)
        else:
            self.radioButton_m2.setVisible(False)
            self.radioButton_ar.setVisible(False)
            self.radioButton_ha.setVisible(False)
            self.label_jedn_pole.setVisible(False)
            self.pushButton_rysuj.setVisible(False)
            self.pushButton_porow.setVisible(False)

    def update_table(self):
        selected_option = self.comboBox_obliczenie.currentText()
        self.tableWidget_wybrane.clearContents()
        self.tableWidget_wybrane.setRowCount(0)

        if selected_option == 'Pole powierzchni':
            self.tableWidget_wybrane.setColumnCount(3)
            self.tableWidget_wybrane.setHorizontalHeaderLabels(['Nr', 'X', 'Y'])
            self.update_table_for_surface_area()
        else:
            self.tableWidget_wybrane.setColumnCount(2)
            self.tableWidget_wybrane.setHorizontalHeaderLabels(['Nr', 'h'])
            self.update_table_for_height_difference()

    def update_table_for_surface_area(self):
        if self.comboBox_obliczenie.currentText() != 'Pole powierzchni':
            return
        layer = self.mMapLayerComboBox_layers.currentLayer()
        selected_points = layer.selectedFeatures()

        ID = []
        Xcoord = []
        Ycoord = []

        for point in selected_points:
            idnumber = point['ID']
            ID.append(idnumber)

            xcoord = point['xcoord']
            Xcoord.append(xcoord)

            ycoord = point['ycoord']
            Ycoord.append(ycoord)

        self.tableWidget_wybrane.setRowCount(len(ID))

        for row, data in enumerate(zip(ID, Xcoord, Ycoord)):
            for col, value in enumerate(data):
                item = QtWidgets.QTableWidgetItem(str(value))
                self.tableWidget_wybrane.setItem(row, col, item)

    def update_table_for_height_difference(self):
        if self.comboBox_obliczenie.currentText() != 'Różnica wysokości':
            return
        layer = self.mMapLayerComboBox_layers.currentLayer()
        selected_points = layer.selectedFeatures()

        heights = []
        ID = []

        for point in selected_points:
            zcoord = point['zcoord']
            heights.append(zcoord)

            idnumber = point['ID']
            ID.append(idnumber)

        self.tableWidget_wybrane.setRowCount(len(heights))

        for row, data in enumerate(zip(ID, heights)):
            for col, value in enumerate(data):
                item = QtWidgets.QTableWidgetItem(str(value))
                self.tableWidget_wybrane.setItem(row, col, item)

#UWAGA

    def calculate_height_diff(self):
        if self.comboBox_obliczenie.currentText() != 'Różnica wysokości':
            return
        layer = self.mMapLayerComboBox_layers.currentLayer()
        selected_points = layer.selectedFeatures()
        if len(selected_points) != 2:
            self.label_wynik.setText("Wybrano niewłaściwą liczbę punktów do obliczenia różnicy wysokości")
            iface.messageBar().pushMessage("Błąd",
                                           "Wybrano niewłaściwą liczbę punktów do obliczenia różnicy wysokości",
                                           level=Qgis.Critical,
                                           duration=5)
        else:
            heights = []
            for point in selected_points:
                zcoord = point.attribute(layer.fields().indexFromName('zcoord'))
                heights.append(zcoord)

            ID = []
            for point in selected_points:
                idnumber = point.attribute(layer.fields().indexFromName('ID'))
                ID.append(idnumber)

            delta_height = round(heights[1] - heights[0],5)
            self.label_wynik.setText(f"Różnica wysokosći pomiędzy punktem {ID[1]} i punktem {ID[0]} wynosi: {delta_height} [m]")
            iface.messageBar().pushMessage("Sukces",
                                           "Obliczanie powiodło się",
                                           level=Qgis.Success,
                                           duration=5)
            self.tableWidget_wybrane.setRowCount(len(heights))
            for row, height in enumerate(heights):
                    item = QtWidgets.QTableWidgetItem(str(height))
                    self.tableWidget_wybrane.setItem(row, 1, item)

    def calculate_field(self):
        if self.comboBox_obliczenie.currentText() != 'Pole powierzchni':
            return
        layer = self.mMapLayerComboBox_layers.currentLayer()
        selected_points = layer.selectedFeatures()
        if len(selected_points) < 3:
            self.label_wynik.setText("Wybrano zbyt małą liczbę punktów do obliczenia pola powierzchni")
            iface.messageBar().pushMessage("Błąd",
                                           "Wybrano zbyt małą liczbę punktów do obliczenia pola powierzchni",
                                           level=Qgis.Critical,
                                           duration=5)
        points = [feature.geometry().asPoint() for feature in selected_points]
        centroid = QgsPoint(sum(point.x() for point in points) / len(points),
                            sum(point.y() for point in points) / len(points))
        points.sort(key=lambda point: -math.atan2(point.y() - centroid.y(), point.x() - centroid.x()))
        area = 0.5 * np.abs(
            sum(points[i - 1].x() * points[i].y() - points[i].x() * points[i - 1].y() for i in range(len(points))))
        if self.radioButton_m2.isChecked():
            self.label_wynik.setText(f"Wynik to: {area} metrów kwadratowych")
        elif self.radioButton_ar.isChecked():
            self.label_wynik.setText(f"Wynik to: {area/ 100} arów")
        elif self.radioButton_ha.isChecked():
            self.label_wynik.setText(f"Wynik to: {area/ 10000} hektarów")
        iface.messageBar().pushMessage("Sukces",
                                       "Obliczanie powiodło się",
                                       level=Qgis.Success,
                                       duration=5)

    def create_polygon(self):
        canvas = iface.mapCanvas()
        layer = self.mMapLayerComboBox_layers.currentLayer()
        crs = layer.crs()
        crs_authid = crs.authid()
        selected_features = layer.selectedFeatures()
        if len(selected_features) < 3:
            iface.messageBar().pushMessage("Błąd",
                                           "Wybierz co najmniej 3 punkty do narysowania poligonu.",
                                           level=Qgis.Warning)
            return
        points = [feature.geometry().asPoint() for feature in selected_features]
        centroid = QgsPoint(sum(point.x() for point in points) / len(points),
                            sum(point.y() for point in points) / len(points))
        points.sort(key=lambda point: -math.atan2(point.y() - centroid.y(), point.x() - centroid.x()))
        new_layer = QgsVectorLayer("Polygon?crs=" + crs_authid, "Poligon", "memory")
        provider = new_layer.dataProvider()
        new_layer.startEditing()
        poly_feature = QgsFeature()
        polygon = QgsGeometry.fromPolygonXY([points])
        poly_feature.setGeometry(polygon)
        provider.addFeature(poly_feature)
        new_layer.commitChanges()
        QgsProject.instance().addMapLayer(new_layer)
        canvas.refresh()

    def compare_area(self):
        layer = self.mMapLayerComboBox_layers.currentLayer()
        selected_feature = layer.selectedFeatures()
        layer.startEditing()
        for i in selected_feature:
            area = i.geometry().area()
            layer.changeAttributeValue(i.id(), layer.fields().indexFromName('Powierzchnia'), area)
        layer.commitChanges()
        if self.radioButton_m2.isChecked():
            self.label_porow.setText(f"Wynik to: {area} metrów kwadratowych")
        elif self.radioButton_ar.isChecked():
            self.label_porow.setText(f"Wynik to: {area / 100} arów")
        elif self.radioButton_ha.isChecked():
            self.label_porow.setText(f"Wynik to: {area / 10000} hektarów")

    def clear_porow_label(self):
        self.label_porow.setText('')

    def explore(self):
        file = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', "C:\\")
        self.lineEdit_sciezka.setText(file[0])

    def clear_display(self):
        self.label_wynik.setText('')
        self.clear_porow_label()
        self.mMapLayerComboBox_layers.currentLayer().removeSelection()