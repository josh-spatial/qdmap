# This module defines the classes for sites used in qdmap.
#=========================
# DONE fix the errors in the bd1() function. Maybe I should rethink how I'm doing this.
# Maybe I can make a child class of Site for PESite. In that class is where I bring in the Limit class
# or just leave it as attributes within the PESite class? I think I'm making this too complicated.

import qdcalc as qd


class Site:
    """Represents a site. PES or ES only?"""

    def __init__(self, facility_no, kind):
        self.facility_no = facility_no
        self.kind = kind

    def site_info(self):
        """Return formatted info about the site."""
        site_info = f"Facility No.: {self.facility_no}\n\tType: {self.kind}"
        return site_info
    
class PES(Site):
    """Represents aspects of a site, specific to potential explosion sites."""
    def __init__(self, facility_no, kind):    # Initialize attributes of parent class.
        super().__init__(facility_no, kind)
        self.neq_1_1 = 0
        self.neq_1_2_1 = 0
        self.mce_1_2_1 = 0
        self.neq_1_2_2 = 0
        self.neq_1_2_2 = 0
        self.neq_1_2_3 = 0
        self.mce_1_2_3 = 0
        self.neq_1_3_1 = 0
        self.neq_1_3_2 = 0

    def limit_info(self):
        """Return formatted info about the NEQ limits."""
        limit_info = f"\tHD 1.1: \t{self.neq_1_1} kg \n\tHD 1.2.1: \t{self.neq_1_2_1} kg"
        return limit_info

    @property
    def bd1_1_1(self):
        """Returns BD1 blast distance from a given net explosives quantity (NEQ) in kg."""
        # import numpy as np
        # bd1 = np.where(q < 30_000, 0.35 * q ** (1/3), 0.44 * q ** (1/3))
        # return bd1

        # Use the qdcalc bd1 function instead of defining function inside the class
        return qd.bd1(self.neq_1_1)

    def qd_info(self):
        """Return formatted info about the QDs."""
        qd_info = f"QD Info:\nHD 1.1 QDs:\n\tBD1: \t{self.bd1_1_1:.1f} m"
        return qd_info


