import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------
# Load Dataset
# ----------------------------------
df = pd.read_csv(
    "API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv",
    skiprows=4
)

latest_year = "2023"

# ----------------------------------
# Remove rows without population
# ----------------------------------
population = df[["Country Name", latest_year]].dropna()
# Remove regions and aggregates
remove_list = [
    "World",
    "IDA & IBRD total",
    "IBRD only",
    "IDA total",
    "High income",
    "Low income",
    "Middle income",
    "Lower middle income",
    "Upper middle income",
    "Low & middle income",
    "Early-demographic dividend",
    "Late-demographic dividend",
    "East Asia & Pacific",
    "East Asia & Pacific (excluding high income)",
    "Europe & Central Asia",
    "Latin America & Caribbean",
    "Middle East & North Africa",
    "North America",
    "South Asia",
    "Sub-Saharan Africa",
    "European Union",
    "OECD members",
    "Least developed countries: UN classification",
    "Post-demographic dividend",
    "Pre-demographic dividend",
    "Arab World",
    "Fragile and conflict affected situations"
]

population = population[
    ~population["Country Name"].isin(remove_list)
]
# Top 10 Countries
top10 = population.sort_values(
    by=latest_year,
    ascending=False
).head(10)


# Graph 1

plt.figure(figsize=(12,6))

bars = plt.bar(
    top10["Country Name"],
    top10[latest_year],
    color="steelblue",
    edgecolor="black"
)

plt.title("Top 10 Most Populous Countries (2023)",
          fontsize=16,
          fontweight="bold")

plt.xlabel("Country", fontsize=12)
plt.ylabel("Population", fontsize=12)

plt.xticks(rotation=40, ha="right")

plt.grid(axis="y", linestyle="--", alpha=0.4)

for bar in bars:
    plt.text(
        bar.get_x()+bar.get_width()/2,
        bar.get_height(),
        f'{bar.get_height()/1e9:.2f}B',
        ha='center',
        fontsize=9
    )

plt.tight_layout()

plt.savefig("Top10_Populated_Countries.png", dpi=300)

plt.show()

# ===========================================================
# Graph 2
# Distribution of Countries by Income Group
# ===========================================================

income_groups = {
    "High income":86,
    "Upper middle income":54,
    "Lower middle income":50,
    "Low income":25
}

plt.figure(figsize=(9,5))

bars = plt.bar(
    income_groups.keys(),
    income_groups.values(),
    color=["royalblue",
           "orange",
           "gold",
           "crimson"],
    edgecolor="black"
)

plt.title(
    "Distribution of Countries by Income Group",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Income Group", fontsize=12)
plt.ylabel("Number of Countries", fontsize=12)

plt.grid(axis="y",
         linestyle="--",
         alpha=0.4)

plt.xticks(rotation=30)

for bar in bars:
    plt.text(
        bar.get_x()+bar.get_width()/2,
        bar.get_height()+1,
        str(int(bar.get_height())),
        ha='center',
        fontsize=10,
        fontweight="bold"
    )

plt.tight_layout()

plt.savefig("Income_Group_Distribution.png", dpi=300)

plt.show()