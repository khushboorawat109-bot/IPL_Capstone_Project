import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("🏏 IPL Data Analysis")

df = pd.read_csv("ipl.csv")

st.subheader("IPL Dataset")
st.dataframe(df)

st.subheader("Basic Information")
st.write("Number of matches:", len(df))

st.subheader("Matches by Season")

season_count = df["season"].value_counts().sort_index()

fig, ax = plt.subplots()
season_count.plot(kind="bar", ax=ax)
ax.set_xlabel("Season")
ax.set_ylabel("Number of Matches")
st.pyplot(fig)
