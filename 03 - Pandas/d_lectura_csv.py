#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 10:07:29 2020

@author: dev-11
"""
# d_lectura_csv.py

# 03_pandas
#   d_lectura_csv.py
#   data
#      artworw.csv

import pandas as pd
import os

path = "/home/dev-11/Documents/Github/py-eguez-sarzosa-vicente-adrian/03 - Pandas/data/artwork_data.csv"

# "C://Users//USRBET//Documents//GitHub//py-eg"
# "./data/artwork_data.csv"

df1 = pd.read_csv(
    path,
    nrows=10)

columnas = ['id', 'artist', 'title',
            'medium', 'year',
            'acquisitionYear', 'height',
            'width', 'units']

df2 = pd.read_csv(
    path,
    nrows=10,
    usecols = columnas)

df3 = pd.read_csv(
    path,
    usecols = columnas,
    index_col = 'id')



path_guardado = "/home/dev-11/Documents/Github/py-eguez-sarzosa-vicente-adrian/03 - Pandas/data/artwork_data.pickle"
# artwork_data.pickle

df3.to_pickle(path_guardado)

df4 = pd.read_pickle(path_guardado)







