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

student = ['Usama','Mobeen', 'Zia']
english = [78,82,90]

fig, ax =plt.subplots()
ax.bar(student, english, width=0.5)

#adding labels
ax.set_xlabel("Number of Students")
ax.set_ylabel("English Marks")

#adding title
plt.title("Distribution of Marks")

plt.show()