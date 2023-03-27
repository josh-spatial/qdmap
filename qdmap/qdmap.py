"""Main module."""


from qdsites import PES


# Test the code.
# ====================
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

# Try to interate over the attributes:
for attribute, value in s1.__dict__.items():
    print(attribute, value) # TODO Figure out why the bd1_1_1 is still zero after entering a value.