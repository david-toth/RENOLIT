import os
import pandas as pd
from PIL import Image
import streamlit as st
import plotly.express as px

PATH_TO_RAW_DATA = "./Raw Data"
FILE_PATH = "./Raw Data/qc_data.pkl"
LOGO = Image.open("renolit_logo.png")

WELCOME_MSG = """
Welcome to American Renolit Corp. Quality Control Data Analytics! To use this
system, all you need to do is enter an **Article No.** in the text box
on the left-hand side of the screen and select a **Characteristic** of interest.
If you need to update the database, simply press the **Update Database** button!

_For questions, please email Renolit IT or [David Toth](mailto:dtoth1@nd.edu)_.
"""
def coerce_strings(df, col):
    """
    Coerces any strings in a column
    that should be numeric to a floating point.
    Also ensures that commas are removed.
    """
    for i,j in enumerate(df[col]):
        if type(j) == str:
            j = float(j.replace(',', ''))
            df[col].iloc[i] = j

    return df

def pickle_data(path=PATH_TO_RAW_DATA):
    """
    Combines Excel spreadsheets of quality control
    data into a single file called a pickle file.
    This file is unique to Python, and it is very fast
    to load once created.

    This function expects a path to a folder of raw
    data containing .xlsx files. For example, the path
    should be something like O:/Quality/QC Data Project/

    *************************************************
    IT IS VERY IMPORTANT THAT THE COLUMNS IN EACH RAW
    DATA FILE ARE THE SAME FOR ALL FILES.
    *************************************************
    """

    files = os.listdir(path)
    xlsx_files = [path+"./"+f for f in files if f[-4:] == 'xlsx']

    print("Beginning to read excel sheets...will take a few minutes")
    df_list = [pd.read_excel(f) for f in xlsx_files]
    master_df = pd.concat(df_list)

    master_df.to_pickle(path+"./qc_data.pkl")

def main():
    """
    Runs the browser app to do data analysis.
    """
    df = pd.read_pickle(FILE_PATH)
    st.image(LOGO, format='PNG', use_column_width=True)
    st.title("ARC QC Analytics")
    st.markdown(WELCOME_MSG)

    articleno = st.sidebar.text_area("Article No. (enter on separate lines)",
                                    df['PH Mat. No.'].iloc[0])
    articleno = articleno.split('\n')
    df1 = df[df['PH Mat. No.'].isin(articleno)]
    charac = st.sidebar.selectbox("Characteristic", df1['Charac.'].unique())
    update = st.sidebar.button("Update Database")

    if update:
        pickle_data()

    new_df = df1[(df1['Charac.']==charac)].copy()
    new_df = coerce_strings(new_df, 'Upper tolerance')
    new_df = coerce_strings(new_df, 'Lower tolerance')
    new_df = coerce_strings(new_df, 'Avg')
    new_df.loc[:, 'Upper tolerance'] = new_df['Upper tolerance'].astype('float')
    new_df.loc[:, 'Lower tolerance'] = new_df['Lower tolerance'].astype('float')
    new_df.loc[:, 'Avg'] = new_df['Avg'].astype('float')
    new_df = new_df.rename(columns={'Order:':'Order'})

    st.header("Data")
    st.write(new_df[['Order', 'PH Mat. No.', 'Charac.', 'Upper tolerance',
                        'Lower tolerance']])

    st.header("Chart")
    strip = px.strip(new_df, x='Order', y='Avg', color='PH Mat. No.',
                     labels={'Order':'Order No.', 'Avg':charac,
                        'PH Mat. No.':'Article Number'})
    strip.update_layout(xaxis_type='category')
    st.plotly_chart(strip)

    st.header("Statistics")
    st.write(new_df.groupby('Order')['Avg'].describe())

main()
