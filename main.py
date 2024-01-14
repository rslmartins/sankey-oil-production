# Import packages
import pandas as pd
from pySankey.sankey import sankey
import matplotlib.pyplot as plt

# Load data and filter
# https://ourworldindata.org/grapher/oil-production-by-country
df = pd.read_csv("oil-production-by-country.csv")

df_1972 = df.loc[df.Year==1972,["Entity", "Oil production (TWh)"]].sort_values("Oil production (TWh)",ascending=False).set_index("Entity").drop(["World",
"Non-OECD (EI)",
"Non-OPEC (EI)",
"OPEC (EI)",
"High-income countries",
"OPEC (Shift)",
"Asia",
"Middle East (EI)",
"Middle East (Shift)",
"Upper-middle-income countries",
"Persian Gulf (Shift)",
"OECD (EI)",
"North America",
"North America (EI)",
"OECD (Shift)",
"North America (Shift)",
"Lower-middle-income countries",
"Eurasia (Shift)",
"CIS (EI)",
"Africa (Shift)",
"Africa (EI)",
"Africa",
"South and Central America (EI)",
"South America",
"Central and South America (Shift)",
"Asia Pacific (EI)",
"Asia and Oceania (Shift)",
"Europe (EI)",
"Europe (Shift)",
"European Union (27)",
"EU28 (Shift)",
"Europe",
],axis=0).reset_index().head(25).rename({"Oil production (TWh)": "1972 Production"}, axis=1).replace({"USSR": "Russia"})
df_1972 = df_1972.reset_index()
df_1972["1972 Rank"] = df_1972["index"].apply(lambda x: f"{x+1} ") + df_1972["Entity"]
df_1972.drop(["index"],axis=1,inplace=True)

df_2022 = df.loc[df.Year==2022,["Entity", "Oil production (TWh)"]].sort_values("Oil production (TWh)",ascending=False).set_index("Entity").drop(["World",
"Non-OECD (EI)",
"Non-OPEC (EI)",
"OPEC (EI)",
"High-income countries",
"Asia",
"Middle East (EI)",
"Upper-middle-income countries",
"OECD (EI)",
"North America",
"North America (EI)",
"Lower-middle-income countries",
"CIS (EI)",
"Africa (EI)",
"Africa",
"South and Central America (EI)",
"South America",
"Asia Pacific (EI)",
"Europe (EI)",
"European Union (27)",
"Europe",
],axis=0).reset_index().head(50).rename({"Oil production (TWh)": "2022 Production"}, axis=1)
df_2022 = df_2022.reset_index()
df_2022["2022 Rank"] = df_2022["index"].apply(lambda x: f"{x+1} ") + df_2022["Entity"]
df_2022.drop(["index"],axis=1,inplace=True)

df_final = df_1972.merge(df_2022, how="left")

# Create Sankey diagram again
sankey(
    left=df_final["1972 Rank"],
    leftWeight= df_final["1972 Production"],
    right=df_final["2022 Rank"],
    rightWeight=df_final["2022 Production"], 
    aspect=60,
    fontsize=12.5,
)

# Get current figure
fig = plt.gcf()

# Set size in inches
fig.set_size_inches(18, 18)

# Set the color of the background to white
fig.set_facecolor("w")
plt.title("Top countries by oil production (1972-2022)", fontsize=18)

# Save the figure
fig.savefig("sankey.png",
            bbox_inches="tight",
            dpi=150)
plt.show()
