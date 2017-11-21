#!/usr/bin/env python

'''
    File name: GeneMapper.py
    Author: Mauricio Fadel Argerich
    Date created: 21/11/2017
    Date last modified: 21/11/2017
    Python Version: 3.5.4
'''

from bioservices import *
import pandas as pd

class GeneMapper:
    u = None

    def __init__(self):
        self.u = UniProt(verbose=False)

    def map_genes(self, fr, to, df, orig_cols, dest_cols):
        # Get list of genes that we need to map.
        genes_set = set()
        for oc in orig_cols:
            genes_set.update(set(df[oc].unique()))

        map_bio_acc = self.u.mapping(fr=fr, to=to, query=' '.join(map(str, genes_set)))
        final_map_dict = {}
        for k, v in map_bio_acc.items():
            final_map_dict[k] = v[0]

        return self.add_mapping_to_df(df, final_map_dict, orig_cols, dest_cols)


    def add_mapping_to_df(self, df, mapping_dictionary, orig_cols, dest_cols):
        print('Mapping df...')

        # Getting number of origin columns, we need it to do itertuples
        # on the dataframe, fastest way to iterate over it.
        orig_idx = []
        for o in range(0, len(orig_cols)):
            for c_idx in range(0, len(df.columns)):
                if df.columns[c_idx] == orig_cols[o]:
                    orig_idx.append(c_idx + 1)

        # We will give feedback to the user while the task is running.
        # For this we will print every 10% of the rows are mapped.
        size = len(df)
        i = 0
        for t in df.itertuples():
            if i % int(size * 0.1) == 0:
                print(str((i / size) * 100) + '% done')

            i += 1

            # We map every column on orig_cols.
            for o in range(0, len(orig_cols)):
                if mapping_dictionary.get(t[orig_idx[o]]) != None:
                    df.at[t[0], dest_cols[o]] = mapping_dictionary.get(t[orig_idx[o]])
                else:
                    df.at[t[0], dest_cols[o]] = '?'

        return df