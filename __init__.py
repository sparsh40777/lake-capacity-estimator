# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LakesAndReservoirsCapacityEstimator
                                 A QGIS plugin
 This plugin helps estimate the lake surface area and cumulative capacity at different lake elevation using depth or elevation raster data.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2025-02-21
        copyright            : (C) 2025 by SPARSH SHEKHAR
        email                : 22m0587@iitb.ac.in
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load LakesAndReservoirsCapacityEstimator class from file LakesAndReservoirsCapacityEstimator.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .LAKE_CAPACITY_ESTIMATOR import LakesAndReservoirsCapacityEstimator
    return LakesAndReservoirsCapacityEstimator(iface)
