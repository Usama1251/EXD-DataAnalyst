import matplotlib.pyplot as plt
import numpy as np

# chemicalExports = np.arange(0.82, 0.94, 0.02)
# years = list(range(2011, 2023, 2))
# medicineExports = np.arange(0.791, 0.851, 0.01)
# fig, ax = plt.subplots()

# ax.plot(years, chemicalExports, label="Chemicals", marker="o", c='b', ls='-', lw=2)
# ax.plot(years, medicineExports, label="Medicines", marker="x", c='b', ls=':', lw=2)
# plt.title("LCI Exports")
# ax.set_xlabel("Years")
# ax.set_ylabel("Amount (Million US$)")
# plt.legend(loc="best")
# plt.annotate("Peak of chemical Exports ", xy=(2016, 0.92))
# plt.grid(True)
# # plt.legend(['Chemicals', 'Medicines'])
# plt.savefig("mychart.png")
# plt.show()

# chemicalExports = np.arange(0.82, 0.94, 0.02)
# years = list(range(2011, 2023, 2))
# medicineExports = np.arange(0.791, 0.851, 0.01)

# fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)

# ax1.plot(years, chemicalExports, label="Chemicals", marker="o", c='b', ls='-', lw=2)

# ax1.set_title("LCI Chemical Exports in last 12 years")
# ax1.set_xlabel("Years")
# ax1.set_ylabel("Amount (Million US$)")


# ax2.plot(years, medicineExports, label="Medicines", marker="x", c='b', ls=':', lw=2)
# ax2.set_title("LCI Medicine Exports in last 12 years")
# ax2.set_xlabel("Years")
# ax2.set_ylabel("Amount (Million US$)")

# plt.tight_layout()
# plt.legend(loc="best")
# plt.show()

# student = ['Usama','Mobeen', 'Zia']
# english = [78,82,90]

# fig, ax =plt.subplots()
# ax.bar(student, english, width=0.5)

# #adding labels
# ax.set_xlabel("Number of Students")
# ax.set_ylabel("English Marks")

# #adding title
# plt.title("Distribution of Marks")

# plt.show()

# languages = ['Python', 'C++', 'Laravel']
# students = [5, 10, 15]

# fig, ax = plt.subplots()

# ax.bar(languages, students, width=0.5)

# ax.set_xlabel("Languages")
# ax.set_ylabel("Number of Students")

# plt.title("Distribution of Students")

# plt.show()

# languages = ['Python', 'C++', 'Laravel']
# students = [5, 10, 15]

# fig, ax = plt.subplots()

# ax.scatter(languages, students)

# ax.set_xlabel("Languages")
# ax.set_ylabel("Number of Students")

# plt.title("Distribution of Students")

# plt.show()

# labels = ['paperoni', 'cheese', 'bbq', 'veggie', 'pineaple']
# sizes = [28, 22, 18, 20, 12]
# explode = [0.05, 0, 0, 0, 0.12]

# plt.figure(figsize=(7, 6))
# plt.pie(
#     sizes,
#     labels= labels,
#     explode=explode, 
#     autopct="%.1f%%",
#     startangle=90, 
#     shadow= True
# )

# plt.title("Claa Pizza Toppings Poll")
# plt.axis("equal")
# plt.show()

# labels = ['paperoni', 'cheese', 'bbq', 'veggie', 'pineaple']
# sizes = [28, 22, 18, 20, 12]

# plt.figure(figsize=(7, 6))
# plt.pie(
#     sizes,
#     labels= labels,
#     autopct="%.1f%%",
#     startangle=90, 
#     pctdistance=0.8,
#     shadow= True
# )

# plt.title("Class Pizza Toppings Poll")
# plt.axis("equal")
# plt.show()

# labels = ['paperoni', 'cheese', 'bbq', 'veggie', 'pineaple']
# sizes = [28, 22, 18, 20, 12]

# plt.figure(figsize=(7, 6))
# plt.pie(
#     sizes,
#     labels= labels,
#     autopct="%.1f%%",
#     startangle=140, 
#     pctdistance=0.8,
#     shadow= True
# )

# center_circle = plt.Circle((0,0), 0.55, fc = "white")
# plt.gca().add_artist(center_circle)
# plt.title("Class Pizza Toppings Poll")
# plt.axis("equal")
# plt.show()

# students = ['usama', 'mobeen', 'zia']
# subjects = ['math', 'science', 'physics']
# marks = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]

# plt.figure(figsize=(7,5))
# plt.imshow(marks, cmap="rainbow_r")

# plt.xticks(range(len(subjects)), subjects)
# plt.yticks(range(len(students)), students)
# plt.colorbar(label="Marks")
# plt.title("Students Marks Heatmap")
# plt.tight_layout()
# plt.show()

# products = ['Apple', 'Ipad', 'Dell', 'HP', 'Lenova']
# months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']

# Sales = [
#     [120, 100, 130, 140, 150],
#     [300, 78, 200, 250, 280],
#     [250, 80, 220, 240, 260],
#     [221, 90, 210, 230, 250],
#     [170, 72, 180, 200, 220]
# ]

# plt.figure(figsize=(7, 5))

# plt.imshow(Sales, cmap="Blues_r")

# plt.xticks(range(len(months)), months)
# plt.yticks(range(len(products)), products)

# plt.colorbar(label="Sales")

# plt.title("Products Sales Heatmap")

# plt.tight_layout()
# plt.show()

mks = np.array([65, 85, 72, 45, 87, 69, 61, 80, 77, 73, 66, 200])

fig, ax = plt.subplots()

ax.boxplot(x=mks, patch_artist=True)

ax.set_title("Box Plot for Subject Marks")
ax.set_xlabel("Advanced Python Programming")
ax.set_ylabel("Marks")

ax.yaxis.grid(True)

plt.show()
