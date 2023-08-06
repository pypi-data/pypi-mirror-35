# -*- coding: utf-8 -*-
"""
Authors: Tim Hessels and Gonzalo Espinoza
         UNESCO-IHE 2016
Contact: t.hessels@unesco-ihe.org
         g.espinoza@unesco-ihe.org
Repository: https://github.com/wateraccounting/wa
Module: Products


Description:
This module contains scripts used to create WA+ products (data directly from web).

Examples:
from wa import Products
help(Products)
dir(Products)
"""

from watools.Products import ETref
from watools.Products import ETens

__all__ = ['ETref', 'ETens']

__version__ = '0.1'