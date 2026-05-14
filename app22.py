import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from mplsoccer import Pitch

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Tactical Shot Analysis Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# TITLE
# --------------------------------------------------
st.title("⚽ Tottenham vs Leeds - Tactical Shot Analysis")
st.markdown("Expected Goals (xG), shot maps, heatmaps, and performance insights.")

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("tottenham_vs_leeds.csv")
    return df

df = load_data()

if df is None or df.empty:
    st.warning("No data available.")
    st.stop()

# --------------------------------------------------
# DATA ENGINEERING
# --------------------------------------------------
df = df.copy()

df["x"] = df["X"] * 120
df["y"] = df["Y"] * 80
df["goal"] = (df["result"] == "Goal").astype(int)

df["team"] = df.apply(
    lambda r: r["h_team"] if r["h_a"] == "h" else r["a_team"],
    axis=1
)

home = df[df["h_a"] == "h"].copy()
away = df[df["h_a"] == "a"].copy()

away["x"] = 120 - away["x"]
away["y"] = 80 - away["y"]

home_team = home["h_team"].iloc[0]
away_team = away["a_team"].iloc[0]

# --------------------------------------------------
# SIDEBAR FILTERS
# --------------------------------------------------
st.sidebar.header("🎛 Filters")

team_filter = st.sidebar.selectbox("Team", ["All"] + list(df["team"].unique()))
player_filter = st.sidebar.selectbox("Player", ["All"] + list(df["player"].unique()))
min_xg = st.sidebar.slider("Minimum xG", 0.0, float(df["xG"].max()), 0.0)

filtered = df.copy()

if team_filter != "All":
    filtered = filtered[filtered["team"] == team_filter]

if player_filter != "All":
    filtered = filtered[filtered["player"] == player_filter]

filtered = filtered[filtered["xG"] >= min_xg]

home_f = filtered[filtered["h_a"] == "h"].copy()
away_f = filtered[filtered["h_a"] == "a"].copy()

away_f["x"] = 120 - away_f["x"]
away_f["y"] = 80 - away_f["y"]

# --------------------------------------------------
# KPI ROW (like dashboard cards)
# --------------------------------------------------
st.subheader("📊 Match Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(home_team + " xG", round(home_f["xG"].sum(), 2))

with col2:
    st.metric(away_team + " xG", round(away_f["xG"].sum(), 2))

with col3:
    st.metric("Total Shots", len(filtered))

with col4:
    st.metric("Total Goals", filtered["goal"].sum())

# --------------------------------------------------
# MAIN VISUAL GRID
# --------------------------------------------------
colA, colB = st.columns(2)

# ---------------- SHOT MAP ----------------
with colA:
    st.subheader("⚽ Shot Map")

    pitch = Pitch(pitch_type="statsbomb", pitch_color="#1b1b1b", line_color="white")

    fig, ax = plt.subplots(figsize=(7, 5))
    pitch.draw(ax=ax)

    ax.scatter(
        home_f["x"], home_f["y"],
        s=(home_f["xG"] * 800).clip(20, 600),
        c="red",
        alpha=0.7,
        label=home_team
    )

    ax.scatter(
        away_f["x"], away_f["y"],
        s=(away_f["xG"] * 800).clip(20, 600),
        c="blue",
        alpha=0.7,
        label=away_team
    )

    ax.set_title("Shot Map", color="white")
    ax.legend()

    st.pyplot(fig)

# ---------------- HEATMAP ----------------
with colB:
    st.subheader("🔥 Shot Heatmap")

    fig2, ax2 = plt.subplots(figsize=(7, 5))
    pitch.draw(ax=ax2)

    pitch.kdeplot(home_f["x"], home_f["y"], ax=ax2, fill=True, cmap="Reds", alpha=0.4)
    pitch.kdeplot(away_f["x"], away_f["y"], ax=ax2, fill=True, cmap="Blues", alpha=0.4)

    ax2.set_title("Shot Density", color="white")

    st.pyplot(fig2)

# --------------------------------------------------
# LOWER SECTION
# --------------------------------------------------
st.subheader("📈 Team & Player Analytics")

col3, col4 = st.columns(2)

# ---------------- TEAM xG ----------------
with col3:
    team_xg = filtered.groupby("team")["xG"].sum().reset_index()

    fig3, ax3 = plt.subplots()
    ax3.bar(team_xg["team"], team_xg["xG"])
    ax3.set_title("Team xG Comparison")

    st.pyplot(fig3)

with col4:
    player = filtered.groupby("player").agg(
        shots=("goal", "count"),
        xG=("xG", "sum"),
        goals=("goal", "sum")
    ).reset_index()

    player["xG_diff"] = player["goals"] - player["xG"]
    player["conversion_rate"] = player["goals"] / player["shots"].replace(0, 1)

    st.dataframe(player.sort_values("xG_diff", ascending=False))