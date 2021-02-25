import pandas as pd
import plotly.express as px
import pandas as pd
import csv
import plotly.graph_objects as go

# df = pd.read_csv("data.csv")
# print(df.groupby("level")["attempt"].mean())

# fig = go.Figure(go.Bar(
#     x = df.groupby("level")["attempt"].mean(),
#     y = ["Level 1","Level 2","Level 3","Level 4"],
#     orientation = "h"
# ))

# fig.show()

df = pd.read_csv('data.csv')
fig = px.scatter(df,x='level',y='student_id',color="attempt")
fig.show()

