# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 17:03:06 2016

@author: Cloud User
"""

import pandas as pd
import os


area_titles = 'http://data.bls.gov/cew/doc/titles/area/area_titles.csv'
own_titles = 'http://data.bls.gov/cew/doc/titles/ownership/ownership_titles.csv'
industry_titles = 'http://data.bls.gov/cew/doc/titles/industry/industry_titles.csv'
agglvl_titles = 'http://data.bls.gov/cew/doc/titles/agglevel/agglevel_titles.csv'
size_titles = 'http://data.bls.gov/cew/doc/titles/size/size_titles.csv'


area_titles = pd.read_csv(area_titles)
own_titles = pd.read_csv(own_titles)
industry_titles = pd.read_csv(industry_titles)
agglvl_titles = pd.read_csv(agglvl_titles)
size_titles = pd.read_csv(size_titles)