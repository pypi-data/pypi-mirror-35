#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SSBJ test case - http://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/19980234657.pdf
Original Python implementation for OpenMDAO integration developed by
Sylvain Dubreuil and Remi Lafage of ONERA, the French Aerospace Lab.
Original files taken from: https://github.com/OneraHub/SSBJ-OpenMDAO
The files were adjusted for optimal use in KADMOS by Imco van Gent.
"""
from __future__ import absolute_import, division, print_function

import sys

import numpy as np
from lxml import etree

from kadmos.utilities.xml_utils_openlego import xml_safe_create_element

from ssbjkadmos.config import root_tag, x_tc, x_h, x_M, x_AR, x_Lambda, x_Sref, x_WT, x_ESF, x_Theta, x_CDmin, x_Cf, \
    x_L, x_D, x_fin, x_dpdx
from ssbjkadmos.tools.SsbjDiscipline import SsbjDiscipline
from ssbjkadmos.utils.execution import run_tool
from ssbjkadmos.utils.math import polynomial_function


class Aerodynamics(SsbjDiscipline):  # AbstractDiscipline

    @property
    def description(self):
        return u'Aerodynamic analysis discipline of the SSBJ test case.'

    def generate_input_xml(self):
        root = etree.Element(root_tag)
        doc = etree.ElementTree(root)

        xml_safe_create_element(doc, x_tc, 0.05)
        xml_safe_create_element(doc, x_h, 45000.0)
        xml_safe_create_element(doc, x_M, 1.6)
        xml_safe_create_element(doc, x_AR, 5.5)
        xml_safe_create_element(doc, x_Lambda, 55.0)
        xml_safe_create_element(doc, x_Sref, 1000.0)
        xml_safe_create_element(doc, x_WT, 49909.58578)
        xml_safe_create_element(doc, x_ESF, 1.0)
        xml_safe_create_element(doc, x_Theta, 0.950978)
        xml_safe_create_element(doc, x_CDmin, 0.01375)
        xml_safe_create_element(doc, x_Cf, 0.75)

        return etree.tostring(doc, encoding='utf-8', pretty_print=True, xml_declaration=True)

    def generate_output_xml(self):
        root = etree.Element(root_tag)
        doc = etree.ElementTree(root)

        xml_safe_create_element(doc, x_L, 49909.58578)
        xml_safe_create_element(doc, x_D, 12193.7018)
        xml_safe_create_element(doc, x_fin, 4.093062)
        xml_safe_create_element(doc, x_dpdx, 1.0)

        return etree.tostring(doc, encoding='utf-8', pretty_print=True, xml_declaration=True)

    @staticmethod
    def execute(in_file, out_file):
        doc = etree.parse(in_file)
        z0 = float(doc.xpath(x_tc)[0].text)
        z1 = float(doc.xpath(x_h)[0].text)
        z2 = float(doc.xpath(x_M)[0].text)
        z3 = float(doc.xpath(x_AR)[0].text)
        z4 = float(doc.xpath(x_Lambda)[0].text)
        z5 = float(doc.xpath(x_Sref)[0].text)
        WT = float(doc.xpath(x_WT)[0].text)
        ESF = float(doc.xpath(x_ESF)[0].text)
        Theta = float(doc.xpath(x_Theta)[0].text)
        CDMIN = float(doc.xpath(x_CDmin)[0].text)
        x_aer = float(doc.xpath(x_Cf)[0].text)

        if z1 <= 36089.0:
            V = 1116.39 * z2 * np.sqrt(abs(1.0 - 6.875E-6 * z1))
            rho = 2.377E-3 * (1. - 6.875E-6 * z1) ** 4.2561
        else:
            V = 968.1 * abs(z2)
            rho = 2.377E-3 * 0.2971 * np.exp((36089.0 - z1) / 20806.7)
        CL = WT / (0.5 * rho * (V ** 2) * z5)
        Fo2 = polynomial_function([ESF, abs(x_aer)], [1, 1], [.25] * 2, "Fo2")

        CDmin = CDMIN * Fo2 + 3.05 * abs(z0) ** (5.0 / 3.0) \
                * abs(np.cos(z4 * np.pi / 180.0)) ** 1.5
        if z2 >= 1:
            k = abs(z3) * (abs(z2) ** 2 - 1.0) * np.cos(z4 * np.pi / 180.) \
                / (4. * abs(z3) * np.sqrt(abs(z4 ** 2 - 1.) - 2.))
        else:
            k = (0.8 * np.pi * abs(z3)) ** -1

        Fo3 = polynomial_function([Theta], [5], [.25], "Fo3")
        CD = (CDmin + k * CL ** 2) * Fo3
        L = WT
        D = CD * 0.5 * rho * V ** 2 * z5
        fin = WT / D
        dpdx = polynomial_function([z0], [1], [.25], "dpdx")

        root = etree.Element(root_tag)
        doc = etree.ElementTree(root)
        xml_safe_create_element(doc, x_L, L)
        xml_safe_create_element(doc, x_D, D)
        xml_safe_create_element(doc, x_fin, fin)
        xml_safe_create_element(doc, x_dpdx, dpdx)
        doc.write(out_file, encoding='utf-8', pretty_print=True, xml_declaration=True)


if __name__ == "__main__":

    analysis = Aerodynamics()
    run_tool(analysis, sys.argv)
