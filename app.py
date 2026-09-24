import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="IPL Data Analysis",
    page_icon="🏏",
    layout="wide"
)

st.title("🏏 IPL Data Analysis Dashboard")
st.write("Exploratory Data Analysis of IPL 2022 matches")

# Load dataset
df = pd.read_csv("IPL.csv")

# -------------------------------
# Dataset Overview
# -------------------------------

st.header("📊 Dataset Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Matches", len(df))

with col2:
    st.metric("Teams", len(set(df["team1"]) | set(df["team2"])))

with col3:
    st.metric("Venues", df["venue"].nunique())

st.dataframe(df, use_container_width=True)


# -------------------------------
# Match Winners
# -------------------------------

st.header("🏆 Matches Won by Teams")

winner_count = df["match_winner"].value_counts()

fig, ax = plt.subplots(figsize=(10, 5))
winner_count.plot(kind="bar", ax=ax)

ax.set_xlabel("Team")
ax.set_ylabel("Number of Wins")
ax.set_title("Number of Matches Won by Each Team")

plt.xticks(rotation=45)
st.pyplot(fig)


# -------------------------------
# Toss Analysis
# -------------------------------

st.header("🪙 Toss Analysis")

col1, col2 = st.columns(2)

with col1:
    toss_winners = df["toss_winner"].value_counts()

    fig, ax = plt.subplots(figsize=(8, 5))
    toss_winners.plot(kind="bar", ax=ax)

    ax.set_title("Tosses Won by Teams")
    ax.set_xlabel("Team")
    ax.set_ylabel("Number of Toss Wins")

    plt.xticks(rotation=45)
    st.pyplot(fig)

with col2:
    toss_decision = df["toss_decision"].value_counts()

    fig, ax = plt.subplots(figsize=(6, 5))
    toss_decision.plot(kind="pie", autopct="%1.1f%%", ax=ax)

    ax.set_ylabel("")
    ax.set_title("Toss Decision")

    st.pyplot(fig)


# -------------------------------
# Top Players
# -------------------------------

st.header("⭐ Player of the Match")

pom = df["player_of_the_match"].value_counts().head(10)

fig, ax = plt.subplots(figsize=(10, 5))
pom.plot(kind="bar", ax=ax)

ax.set_title("Top 10 Players by Player of the Match Awards")
ax.set_xlabel("Player")
ax.set_ylabel("Awards")

plt.xticks(rotation=45)
st.pyplot(fig)


# -------------------------------
# Top Scorers
# -------------------------------

st.header("🏏 Top Scorers")

top_scorers = df["top_scorer"].value_counts().head(10)

fig, ax = plt.subplots(figsize=(10, 5))
top_scorers.plot(kind="bar", ax=ax)

ax.set_title("Players Appearing Most Often as Top Scorer")
ax.set_xlabel("Player")
ax.set_ylabel("Count")

plt.xticks(rotation=45)
st.pyplot(fig)


# -------------------------------
# High Scores
# -------------------------------

st.header("🔥 Highest Individual Scores")

top_scores = df.nlargest(10, "highscore")[
    ["top_scorer", "highscore"]
]

st.dataframe(top_scores, use_container_width=True)


# -------------------------------
# Venues
# -------------------------------

st.header("🏟️ Matches by Venue")

venue_count = df["venue"].value_counts().head(10)

fig, ax = plt.subplots(figsize=(10, 5))
venue_count.plot(kind="bar", ax=ax)

ax.set_title("Top 10 Venues by Number of Matches")
ax.set_xlabel("Venue")
ax.set_ylabel("Matches")

plt.xticks(rotation=45)
st.pyplot(fig)


# -------------------------------
# Match Result
# -------------------------------

st.header("🎯 Match Results")

result_count = df["won_by"].value_counts()

fig, ax = plt.subplots(figsize=(6, 5))
result_count.plot(kind="pie", autopct="%1.1f%%", ax=ax)

ax.set_ylabel("")
ax.set_title("Matches Won by Runs vs Wickets")

st.pyplot(fig)


st.success("IPL analysis completed successfully! 🏏")
