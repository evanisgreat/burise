import pandas as pd

df = pd.read_csv('data/Zip_zori_uc_sfrcondomfr_sm_month.csv')

df_specify = df.drop(columns=['RegionID', 'SizeRank', 'RegionType', 'StateName', 'State' ,'City','Metro','CountyName'])

df_specify = df_specify.melt(id_vars='RegionName', var_name='Date', value_name='Zillow Index')

print(df_specify.head())
