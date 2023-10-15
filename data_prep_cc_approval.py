import pandas as pd
import numpy as np
from icecream import ic
from sklearn.preprocessing import LabelEncoder


def labelencoder(df):
    for c in df.columns:
        if df[c].dtype == 'object':
            df[c] = df[c].fillna(np.NaN)
            lbl = LabelEncoder()
            lbl.fit(list(df[c].values))
            df[c] = lbl.transform(df[c].values)
    return df


data_file = "orange\data\cc_approvals.data"

df = pd.read_csv(data_file, header=None)
df.columns = ['Gender', 'Age', 'Debt', 
              'Married', 'BankCustomer', 'EducationLevel', 
              'Ethnicity', 'YearsEmployed', 'PriorDefault', 
              'Employed', 'CreditScore', 'DriversLicense', 
              'Citizen', 'ZipCode', 'Income', 
              'ApprovalStatus']
df.drop_duplicates(inplace=True)
# drop the columns for DriversLicense
# and ZipCode
df.drop(["DriversLicense", "ZipCode"], axis=1, inplace=True)
df2 = labelencoder(df)
# ic(df)
ic(df2.isnull().sum())

ic(df2)

# output as csv
df2.to_csv("cc_approval_cleaned.csv")