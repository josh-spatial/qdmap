"""Main module."""

import matplotlib.pyplot as plt
import numpy as np

import qdmap.qdcalc as qd
from qdmap.qdsites import PES

# TODO: write a while loop for input
# TODO: add facilities to a list (?)

facility_number = input('Enter the facility number: ')
type_code = input("Enter the facility's type code: ")
s1 = PES(facility_number, type_code)
s1.neq_1_1 = input(f"Enter Facility No. {s1.facility_no}'s HD 1.1 limit (kg): ")
s1.neq_1_1 = float(s1.neq_1_1)
s1.neq_1_2_1 = input(f"Enter Facility No. {s1.facility_no}'s HD 1.2.1 limit (kg): ")
s1.neq_1_2_1 = float(s1.neq_1_2_1)
print(s1.site_info())
print(s1.limit_info())
print(s1.qd_info())

# Plot the function based on numpy arrays.
# create the plot

X = np.linspace(0, s1.neq_1_1, 100)
Y = qd.bd1_array(X)

fig, ax = plt.subplots()
ax.plot(X, Y, color='green')
# fig.savefig("figure.pdf")
# provide plotting parameters
plt.title("QD vs. NEW")
plt.ylabel("QD (m)")
plt.xlabel("NEQ (kg)")
plt.legend([f"Fac. No. {s1.facility_no.capitalize()} BD 1"])
fig.show()

# # Plot it!
# plt.show()

# print all the attributes:
# for attribute, value in s1.__dict__.items():
    # print(attribute, value)
