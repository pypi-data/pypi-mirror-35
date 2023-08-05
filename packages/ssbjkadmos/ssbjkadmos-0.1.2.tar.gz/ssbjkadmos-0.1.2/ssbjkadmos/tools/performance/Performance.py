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

from ssbjkadmos.config import root_tag, x_WT, x_h, x_M, x_fin, x_SFC, x_WF, x_R
from ssbjkadmos.tools.SsbjDiscipline import SsbjDiscipline
from ssbjkadmos.utils.execution import run_tool
from kadmos.utilities.xml_utils_openlego import xml_safe_create_element


class Performance(SsbjDiscipline):  # AbstractDiscipline

    @property
    def description(self):
        return u'Performance analysis discipline of the SSBJ test case.'

    def generate_input_xml(self):
        root = etree.Element(root_tag)
        doc = etree.ElementTree(root)

        xml_safe_create_element(doc, x_h, 45000.0)
        xml_safe_create_element(doc, x_M, 1.6)
        xml_safe_create_element(doc, x_fin, 4.093062)
        xml_safe_create_element(doc, x_SFC, 1.12328)
        xml_safe_create_element(doc, x_WT, 49909.58578)
        xml_safe_create_element(doc, x_WF, 7306.20261)

        return etree.tostring(doc, encoding='utf-8', pretty_print=True, xml_declaration=True)

    def generate_output_xml(self):
        root = etree.Element(root_tag)
        doc = etree.ElementTree(root)

        xml_safe_create_element(doc, x_R, 528.91363)

        return etree.tostring(doc, encoding='utf-8', pretty_print=True, xml_declaration=True)

    @staticmethod
    def execute(in_file, out_file):
        doc = etree.parse(in_file)
        z1 = float(doc.xpath(x_h)[0].text)
        z2 = float(doc.xpath(x_M)[0].text)
        fin = float(doc.xpath(x_fin)[0].text)
        SFC = float(doc.xpath(x_SFC)[0].text)
        WT = float(doc.xpath(x_WT)[0].text)
        WF = float(doc.xpath(x_WF)[0].text)

        if z1 <= 36089.:
            theta = 1.0 - 6.875E-6 * z1
        else:
            theta = 0.7519
        R = 661.0 * np.sqrt(theta) * z2 * fin / SFC * np.log(abs(WT / (WT - WF)))

        root = etree.Element(root_tag)
        doc = etree.ElementTree(root)
        xml_safe_create_element(doc, x_R, R)
        doc.write(out_file, encoding='utf-8', pretty_print=True, xml_declaration=True)


if __name__ == "__main__":
    analysis = Performance()
    run_tool(analysis, sys.argv)
