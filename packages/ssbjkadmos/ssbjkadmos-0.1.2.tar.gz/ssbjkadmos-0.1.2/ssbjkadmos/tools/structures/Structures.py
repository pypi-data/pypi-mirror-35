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

from ssbjkadmos.config import root_tag, x_tc, x_AR, x_Lambda, x_Sref, x_lambda, x_section, x_WO, x_WE, x_WFO, \
    x_L, x_Nz, x_WT, x_WF, x_sigma1, x_sigma2, x_sigma3, x_sigma4, x_sigma5, x_Theta
from ssbjkadmos.tools.SsbjDiscipline import SsbjDiscipline
from ssbjkadmos.utils.math import polynomial_function
from ssbjkadmos.utils.execution import run_tool
from kadmos.utilities.xml_utils_openlego import xml_safe_create_element


class Structures(SsbjDiscipline):  # AbstractDiscipline

    @property
    def description(self):
        return u'Structural analysis discipline of the SSBJ test case.'

    def generate_input_xml(self):
        root = etree.Element(root_tag)
        doc = etree.ElementTree(root)

        xml_safe_create_element(doc, x_tc, 0.05)
        xml_safe_create_element(doc, x_AR, 5.5)
        xml_safe_create_element(doc, x_Lambda, 55.0)
        xml_safe_create_element(doc, x_Sref, 1000.0)
        xml_safe_create_element(doc, x_lambda, 0.25)
        xml_safe_create_element(doc, x_section, 1.0)
        xml_safe_create_element(doc, x_WO, 25000.)
        xml_safe_create_element(doc, x_WE, 5748.915355)
        xml_safe_create_element(doc, x_WFO, 2000.)
        xml_safe_create_element(doc, x_L, 49909.58578)
        xml_safe_create_element(doc, x_Nz, 6.0)

        return etree.tostring(doc, encoding='utf-8', pretty_print=True, xml_declaration=True)

    def generate_output_xml(self):
        root = etree.Element(root_tag)
        doc = etree.ElementTree(root)

        xml_safe_create_element(doc, x_WT, 49909.58578)
        xml_safe_create_element(doc, x_WF, 7306.20261)
        xml_safe_create_element(doc, x_sigma1, 1.12255)
        xml_safe_create_element(doc, x_sigma2, 1.08170213)
        xml_safe_create_element(doc, x_sigma3, 1.0612766)
        xml_safe_create_element(doc, x_sigma4, 1.04902128)
        xml_safe_create_element(doc, x_sigma5, 1.04085106)
        xml_safe_create_element(doc, x_Theta, 0.950978)

        return etree.tostring(doc, encoding='utf-8', pretty_print=True, xml_declaration=True)

    def execute(self, in_file, out_file):
        doc = etree.parse(in_file)
        z0 = float(doc.xpath(x_tc)[0].text)
        z3 = float(doc.xpath(x_AR)[0].text)
        z4 = float(doc.xpath(x_Lambda)[0].text)
        z5 = float(doc.xpath(x_Sref)[0].text)
        x0 = float(doc.xpath(x_lambda)[0].text)
        x1 = float(doc.xpath(x_section)[0].text)
        L = float(doc.xpath(x_L)[0].text)
        WE = float(doc.xpath(x_WE)[0].text)
        NZ = float(doc.xpath(x_Nz)[0].text)
        WO = float(doc.xpath(x_WO)[0].text)
        WFO = float(doc.xpath(x_WFO)[0].text)

        b = np.sqrt(abs(z5 * z3)) / 2.0
        R = (1.0 + 2.0 * x0) / (3.0 * (1.0 + x0))

        t = z0 * z5 / (np.sqrt(abs(z5 * z3)))

        Fo1 = polynomial_function([x1], [1], [.008], "Fo1")

        WT_hat = L
        WW = Fo1 * (0.0051 * abs(WT_hat * NZ) ** 0.557 * \
                    abs(z5) ** 0.649 * abs(z3) ** 0.5 * abs(z0) ** (-0.4) \
                    * abs(1.0 + x0) ** 0.1 * (0.1875 * abs(z5)) ** 0.1 \
                    / abs(np.cos(z4 * np.pi / 180.)))
        WFW = 5.0 / 18.0 * abs(z5) * 2.0 / 3.0 * t * 42.5
        WF = WFW + WFO
        WT = WO + WW + WF + WE

        Sigma0 = polynomial_function([z0, L, x1, b, R], [4, 1, 4, 1, 1], [0.1] * 5, "sigma[1]")
        Sigma1 = polynomial_function([z0, L, x1, b, R], [4, 1, 4, 1, 1], [0.15] * 5, "sigma[2]")
        Sigma2 = polynomial_function([z0, L, x1, b, R], [4, 1, 4, 1, 1], [0.2] * 5, "sigma[3]")
        Sigma3 = polynomial_function([z0, L, x1, b, R], [4, 1, 4, 1, 1], [0.25] * 5, "sigma[4]")
        Sigma4 = polynomial_function([z0, L, x1, b, R], [4, 1, 4, 1, 1], [0.30] * 5, "sigma[5]")

        Theta = polynomial_function([abs(x1), b, R, L], [2, 4, 4, 3], [0.25] * 4, "twist")

        root = etree.Element(root_tag)
        doc = etree.ElementTree(root)
        xml_safe_create_element(doc, x_WF, WF)
        xml_safe_create_element(doc, x_WT, WT)

        xml_safe_create_element(doc, x_sigma1, Sigma0)
        xml_safe_create_element(doc, x_sigma2, Sigma1)
        xml_safe_create_element(doc, x_sigma3, Sigma2)
        xml_safe_create_element(doc, x_sigma4, Sigma3)
        xml_safe_create_element(doc, x_sigma5, Sigma4)

        xml_safe_create_element(doc, x_Theta, Theta)

        doc.write(out_file, encoding='utf-8', pretty_print=True, xml_declaration=True)


if __name__ == "__main__":

    analysis = Structures()
    run_tool(analysis, sys.argv)
