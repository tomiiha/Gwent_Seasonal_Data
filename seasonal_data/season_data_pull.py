# Packages
import os
import pandas as pd

def data_finder(pick_season):
    all_files = [x for x in os.listdir() if x.endswith('.csv')]
    main_df = pd.read_csv(all_files[pick_season])
    return main_df
