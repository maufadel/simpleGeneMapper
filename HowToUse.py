#!/usr/bin/env python

'''
    File name: HowToUse.py
    Author: Mauricio Fadel Argerich
    Date created: 21/11/2017
    Date last modified: 21/11/2017
    Python Version: 3.5.4
'''

from GeneMapper import GeneMapper
import pandas as pd

gm = GeneMapper()

full_data = pd.read_csv('dataframe.csv')
print(gm.map_genes(fr='STRING_ID', to='ACC',
                   df = full_data,
                   orig_cols = ['protein1', 'protein2'],
                   dest_cols = ['acc1', 'acc2']).head())