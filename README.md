# Tottenham-vs-Leeds-Shot-Analysis
## Tottenham vs Leeds — xG Tactical Shot Analysis
## Overview

This project is a football analytics match report built with Python using shot-level event data from the Tottenham vs Leeds match.

The analysis focuses on:

Expected Goals (xG)
Shot locations
Tactical attacking patterns
Player finishing efficiency
Set-piece effectiveness
Shot-type analysis

The goal of this project is to simulate a professional football scouting and tactical analysis workflow using data visualization and performance metrics.

## Objective

The objective of this analysis was to evaluate:

Which team created the better scoring opportunities
How chances were created
Which players contributed most to attacking threat
Which shot types generated the highest value
Tactical differences between both teams
## Data Used
Dataset Information

The dataset contains shot-level match events including:

## Column	Description
X, Y	Shot coordinates
xG	Expected Goals value
result	Shot outcome
player	Shooter
h_a	Home/Away indicator
situation	Open play, corners, penalties
shotType	Right foot, left foot, header
minute	Match minute
Total Shots Analyzed
27 shot events
## Tools & Libraries
Python
Pandas
Matplotlib
mplsoccer
Seaborn
## Key Findings
1️⃣ Leeds generated higher total xG
Team	Total xG
Leeds	1.87
Tottenham	1.50
Insight

Leeds created slightly higher-quality chances overall despite Tottenham controlling more open-play sequences.

2️⃣ Tottenham dominated open-play attacking phases
Team	Open Play xG
Tottenham	1.02
Leeds	0.53
Insight

Tottenham generated stronger structured attacking pressure through open-play buildup.

3️⃣ Leeds were more efficient from corners
Team	Corner xG
Leeds	0.58
Tottenham	0.43
Insight

Leeds converted fewer set-piece situations into higher-quality opportunities.

4️⃣ Right-foot shots produced the highest attacking value
Shot Type	xG per Shot
Right Foot	0.149
Header	0.093
Left Foot	0.088
Insight

Most dangerous attacks ended with right-foot finishes inside central penalty-box zones.

5️⃣ Richarlison underperformed expected goals

| Player | xG | Goals |
|---|---|
| Richarlison | 0.75 | 0 |

Insight

Richarlison generated strong attacking positions but failed to convert high-quality chances.

## Visualizations
⚽ Shot Map
Shot locations for both teams
Bubble size scaled by xG
Goals highlighted separately
🔥 Shot Heatmap
Displays attacking concentration zones
Reveals spatial attacking patterns
📊 Situation-Based xG Analysis
Open play vs set pieces
Tactical chance creation comparison
🎯 Player xG Contribution
Identifies key attacking contributors
Measures finishing efficiency
## Tactical Implications
Tottenham
Strengths
Strong open-play structure
Central penalty-box penetration
High attacking shot volume
Weaknesses
Finishing inefficiency
Lower set-piece effectiveness
Leeds
Strengths
Efficient set-piece execution
Clinical high-impact moments
Weaknesses
Lower sustained open-play pressure
Less consistent buildup structure
## Actionable Recommendations
Tottenham
Improve shot conversion efficiency
Increase cutback opportunities
Optimize set-piece routines
Leeds
Improve open-play progression
Maintain set-piece focus
Increase sustained box occupation
## Example Visuals
Shot Map

<img width="837" height="549" alt="image" src="https://github.com/user-attachments/assets/f7fb982a-e4ce-4b56-ba57-47b5b11d1771" />


# Example:
plt.savefig("shot_map.png", dpi=300, bbox_inches='tight')
Heatmap

<img width="799" height="534" alt="image" src="https://github.com/user-attachments/assets/99cd798b-7311-4853-8015-ed30f4ab0b07" />


## Future Improvements
xG flow timeline
Pass network analysis
Player influence zones
Interactive Streamlit dashboard
Match momentum analysis
## Project Structure
Tottenham-vs-Leeds-Shot-Analysis/
│
├── data/
│   └── "tottenham_vs_leeds.csv"
│
├── visuals/
│   ├── shot_map.png
│   └── heatmap.png
│       app22.py
├── notebooks/
│   └── analysis.ipynb
│
├── README.md
│
└── requirements.txt
## Author

Stephen Yaw Ayamah
Football Data Analyst | Python | xG Analysis | Tactical Scouting

## Project Goals

This project was built to:

Practice football analytics workflows
Develop tactical scouting analysis
Build portfolio-ready visualizations
Simulate real-world analyst reporting
