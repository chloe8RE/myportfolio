#INSPECTION, DATA CLEANING

def data_inspect(df, df_name):
    print(f"{df_name} dataset inspection")
    print(f"--------------------------------------------------")
    print(df.info())
    print()
    print('++++++++++')
    print()
    print(f"Check for null percentages for {df_name} dataset:")
    null_percentages = (df.isnull().sum() / len(df)) * 100
    print(null_percentages)
    print()
    print('++++++++++')
    print()
    print(f"Check for no of duplicated values for {df_name} dataset:")
    print(df.duplicated().sum())
    print("++++++++++\n")

def shape_head(df, df_name):
    print(f"{df_name} dataset shape:")
    print(df.shape)
    print()
    print(f"{df_name} dataset head:")
    return df.head()




#EDA

