import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# print(tips.head())
# print(tips.shape)
# print(tips.info())
# print(tips.columns)


# numerical_columns = tips.select_dtypes(include="number").columns
# categorical_columns = tips.select_dtypes(include="category").columns

# print("Numerical:", numerical_columns)
# print("Categorical:", categorical_columns)

# sns.scatterplot(data= tips, x="total_bill", y="tip", hue="sex", style= "time")
# plt.show()

# sns.countplot(
#     data=tips,
#     x="day",
#     hue="sex"
# )
# plt.show()

# sns.barplot(
#     data=tips,
#     x='day',
#     hue="sex")
# plt.title("Transacitons by Day and Sex")
# plt.show()

# sns.histplot(
#     data=tips,
#     x="total_bill",
#     kde=True,
# )
# plt.title("Distribution of Total Bill")
# plt.show()

# sns.boxplot(
#     data=tips,
#     x="total_bill",
# )
# plt.title("Distribution of Total Bill")
# plt.show()

# sns.violinplot(
# data=tips,
# x="total_bill",
# )
# plt.title("Distribution of Total Bill")
# plt.show()

# sns.stripplot(
# data=tips,
# x="total_bill",
# jitter=True
# )
# plt.title("Distribution of Total Bill")
# plt.show()

# sns.swarmplot(
# data=tips,
# x="total_bill"
# )
# plt.title("Distribution of Total Bill")
# plt.show()

# sns.regplot(
# data=tips,
# x="total_bill",
# y="tip"
# )
# plt.title("Distribution of Total Bill")
# plt.show()

# sns.lmplot(
# data=tips,
# x="total_bill",
# y="tip",
# hue="sex"
# )
# plt.title("Distribution of Total Bill")
# plt.show()

