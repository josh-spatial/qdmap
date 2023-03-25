# This module defines the classes for sites used in qdmap.
#=========================
# DONE fix the errors in the bd1() function. Maybe I should rethink how I'm doing this.
# Maybe I can make a child class of Site for PESite. In that class is where I bring in the Limit class
# or just leave it as attributes within the PESite class? I think I'm making this too complicated.

import qdcalc as qd



class Site:
    """Represents a site. PES or ES only?"""

    def __init__(self, facility_no, type):
        self.facility_no = facility_no
        self.type = type

    def site_info(self):
        """Return formatted info about the site."""
        site_info = f"Facility No.: {self.facility_no}\n\tType: {self.type}"
        return site_info
    
class PES(Site):
    """Represents aspects of a site, specific to potential explosion sites."""
    def __init__(self, facility_no, type):    # Initialize attributes of parent class.
        super().__init__(facility_no, type)
        self.neq_1_1 = 0
        self.neq_1_2_1 = 0
        self.mce_1_2_1 = 0
        self.neq_1_2_2 = 0
        self.neq_1_2_3 = 0
        self.bd1_1_1 = qd.bd1(self.neq_1_1)
        self.bd1_2_1 = qd.bd1(self.mce_1_2_1)

    def limit_info(self):
        """Return formatted info about the NEQ limits."""
        limit_info = f"\tHD 1.1: \t{self.neq_1_1} kg \n\tHD 1.2.1: \t{self.neq_1_2_1} kg"
        return limit_info

    # def bd1_1_1(self):
    #     """Returns BD1 blast distance from a given
    #       quantity (Q) in kg."""
    #     # import numpy as np
    #     # bd1 = np.where(q < 30_000, 0.35 * q ** (1/3), 0.44 * q ** (1/3))
    #     # return bd1
    #     if self.neq_1_1 < 30_000:
    #         self.bd1_1_1 = 0.35 * self.neq_1_1 ** (1/3) 
    #     else:
    #         self.bd1_1_1 = 0.44 * self.neq_1_1 ** (1/3)
    #     return self.bd1_1_1

    def qd_info(self):
        """Return formatted info about the QDs."""
        qd_info = f"\n\tBD1: \t{self.bd1_1_1} m"
        return qd_info


#class Limit:
#    """Represents the explosives limits for each Hazard Division."""
#
#    def __init__(self, neq_1_1=0, neq_1_2_1=0):
#        """Initialize the class and define Hazard Divisions."""
#        self.neq_1_1 = neq_1_1
#        self.neq_1_2_1 = neq_1_2_1
#
#    def limit_info(self):
#        """Return formatted info about the NEQ limits."""
#        limit_info = f"\tHD 1.1: \t{self.neq_1_1} kg \n\tHD 1.2.1: \t{self.neq_1_2_1} kg"
#        return limit_info
    
#class QD:
#    """Calculates the quantity-distances from a given NEQ."""
#
#    def __init__(self):
#        pass
#
#    def bd1(self, q):
#        """Returns BD1 blast distance from a given
#          quantity (Q) in kg."""
#        # import numpy as np
#        # bd1 = np.where(q < 30_000, 0.35 * q ** (1/3), 0.44 * q ** (1/3))
#        # return bd1
#        if q < 30_000:
#            self.bd1 = 0.35 * q ** (1/3) 
#        else:
#            self.bd1 = 0.44 * q ** (1/3)
#        return self.bd1
#
#    def qd_info(self):
#        """Return formatted info about the QDs."""
#        qd_info = f"\n\tBD1: \t{self.bd1} m"
#        return qd_info


# Test the code.
# ====================
facility_number = input('Enter the facility number: ')
type_code = input("Enter the facilitie's type code: ")
s1 = PES(facility_number, type_code)
s1.neq_1_1 = input(f"Enter Facility No. {s1.facility_no}'s HD 1.1 limit (kg): ")
s1.neq_1_1 = float(s1.neq_1_1)
s1.neq_1_2_1 = input(f"Enter Facility No. {s1.facility_no}'s HD 1.2.1 limit (kg): ")
s1.neq_1_2_1 = float(s1.neq_1_2_1)
print(s1.site_info())
print(s1.limit_info())
# print(f"\t\tBD1: {s1.bd1_1_1():.1f} m") # TODO Bug: Float not callable?

# Try to interate over the attributes:
for attribute, value in s1.__dict__.items():
    print(attribute, value) # TODO Figure out why the bd1_1_1 is still zero after entering a value.
    