import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from IPython.core.pylabtools import figsize

# set page configuration
st.set_page_config(page_title="Data visualizer",
                   layout="centered",
                   page_icon="📊")

#Title
st.title("📊  Data Visualizer - web app")

# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

folder_path = f"{working_dir}/data"

# list the files present in the data folder
files_list = [f for f in os.listdir(folder_path) if f.endswith(".csv")]

# Dropdown for all the files
selected_file = st.selectbox("Select a file", files_list, index=None)

if selected_file:
    file_path = os.path.join(folder_path, selected_file)

    # reading the csv file as pandas dataframe
    df = pd.read_csv(file_path)

    col1, col2 = st.columns(2)

    columns = df.columns.tolist()

    with col1:
        st.write("")
        st.write(df.head())

    with col2:
        #user selection of df columns
        x_axis = st.selectbox("Select the X-axis", options=columns + ["None"])
        y_axis = st.selectbox("Select the Y-axis", options=columns + ["None"])

        plot_list = ["Line Plot", "Bar Chart", "Scatter Plot", "Distribution Plot", "Count Plot"]

        selected_plot = st.selectbox("Select the Plot", options=plot_list)

    # button to generate plots
    if st.button("Generate Plot"):
        fig, ax = plt.subplots(figsize=(6,4))

        if selected_plot == "Line Plot":
            sns.lineplot(x=df[x_axis], y=df[y_axis],ax=ax)
        elif selected_plot == "Bar Chart":
            sns.barplot(x=df[x_axis], y=df[y_axis],ax=ax)
        elif selected_plot == "Scatter Plot":
            sns.scatterplot(x=df[x_axis], y=df[y_axis],ax=ax)
        elif selected_plot == "Distribution Plot":
            sns.histplot(df[x_axis], kde=True, ax=ax)
        elif selected_plot == "Count Plot":
            sns.countplot(x=df[x_axis], ax=ax)


        # adjust label sizes
        ax.tick_params(axis="x", labelsize=10)
        ax.tick_params(axis="y", labelsize=10)

        # title axes labels
        plt.title(f"{selected_plot} of {y_axis} vs {x_axis}", fontsize=12)
        plt.xlabel(x_axis, fontsize=10)
        plt.ylabel(y_axis, fontsize=10)

        st.pyplot(fig)