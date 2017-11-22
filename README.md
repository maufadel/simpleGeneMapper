# simpleGeneMapper
A simple class to map gene names/accession numbers/UniProt IDs/etc to other denominations in a dataframe.

## How to use
To quickly map several ids in a Pandas dataframe, is enough to call the method map_genes and specify a few parameters:
```python
from GeneMapper import GeneMapper
import pandas as pd

gm = GeneMapper()

full_data = pd.read_csv('dataframe.csv')
print(gm.map_genes(fr='STRING_ID', to='ACC',
                   df = full_data,
                   orig_cols = ['protein1', 'protein2'],
                   dest_cols = ['acc1', 'acc2']).head())
```

Also, if you would like to use your own mapping dictionary, you can use the method:
```python
gm.add_mapping_to_df(df, final_map_dict, orig_cols, dest_cols)
```
