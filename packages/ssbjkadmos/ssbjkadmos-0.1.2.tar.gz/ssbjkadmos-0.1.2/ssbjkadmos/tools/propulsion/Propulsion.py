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

from lxml import etree

from ssbjkadmos.config import root_tag, x_h, x_M, x_ESF, x_D, x_Temp, x_SFC, x_WE, x_DT, x_WBE, x_T
from ssbjkadmos.tools.SsbjDiscipline import SsbjDiscipline
from ssbjkadmos.utils.execution import run_tool
from kadmos.utilities.xml_utils_openlego import xml_safe_create_element

from ssbjkadmos.utils.math import polynomial_function


class Propulsion(SsbjDiscipline):  # AbstractDiscipline

    @property
    def description(self):
        return u'Propulsion analysis discipline of the SSBJ test case.'

    def generate_input_xml(self):
        root = etree.Element(root_tag)
        doc = etree.ElementTree(root)

        xml_safe_create_element(doc, x_h, 45000.0)
        xml_safe_create_element(doc, x_M, 1.6)
        xml_safe_create_element(doc, x_T, 0.3126)
        xml_safe_create_element(doc, x_D, 12193.7018)
        xml_safe_create_element(doc, x_WBE, 4360.)

        return etree.tostring(doc, encoding='utf-8', pretty_print=True, xml_declaration=True)

    def generate_output_xml(self):
        root = etree.Element(root_tag)
        doc = etree.ElementTree(root)

        xml_safe_create_element(doc, x_Temp, 1.0)
        xml_safe_create_element(doc, x_ESF, 1.0)
        xml_safe_create_element(doc, x_SFC, 1.12328)
        xml_safe_create_element(doc, x_WE, 5748.915355)
        xml_safe_create_element(doc, x_DT, 0.278366)

        return etree.tostring(doc, encoding='utf-8', pretty_print=True, xml_declaration=True)

    @staticmethod
    def execute(in_file, out_file):
        doc = etree.parse(in_file)
        z1 = float(doc.xpath(x_h)[0].text)
        z2 = float(doc.xpath(x_M)[0].text)
        Xpro = float(doc.xpath(x_T)[0].text)
        D = float(doc.xpath(x_D)[0].text)
        WBE = float(doc.xpath(x_WBE)[0].text)

        Tbar = abs(Xpro) * 16168.6
        Temp = polynomial_function([z2, z1, abs(Xpro)], [2, 4, 2], [.25] * 3, "Temp")
        ESF = (D / 3.0) / Tbar
        SFC = 1.1324 + 1.5344 * z2 - 3.2956E-05 * z1 - 1.6379E-04 * Tbar \
              - 0.31623 * z2 ** 2 + 8.2138E-06 * z2 * z1 - 10.496E-5 * Tbar * z2 \
              - 8.574E-11 * z1 ** 2 + 3.8042E-9 * Tbar * z1 + 1.06E-8 * Tbar ** 2
        WE = 3.0 * WBE * abs(ESF) ** 1.05
        TUAbar = 11484.0 + 10856.0 * z2 - 0.50802 * z1 \
                 + 3200.2 * (z2 ** 2) - 0.29326 * z2 * z1 + 6.8572E-6 * z1 ** 2
        DT = Tbar / TUAbar - 1.0

        root = etree.Element(root_tag)
        doc = etree.ElementTree(root)
        xml_safe_create_element(doc, x_Temp, Temp)
        xml_safe_create_element(doc, x_ESF, ESF)
        xml_safe_create_element(doc, x_SFC, SFC)
        xml_safe_create_element(doc, x_WE, WE)
        xml_safe_create_element(doc, x_DT, DT)
        doc.write(out_file, encoding='utf-8', pretty_print=True, xml_declaration=True)


if __name__ == "__main__":
    analysis = Propulsion()
    run_tool(analysis, sys.argv)
