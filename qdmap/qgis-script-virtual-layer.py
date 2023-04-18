# script to add the quantity-distances in a virutal fields for the activate layer
# ****
# The QGIS Python scripts provided here work as intended for a single QD function. But they may need to be improved to loop through multiple functions or adapted to be used with GeoPandas Geodataframes.

from qgis.core import *
from qgis.gui import *

# --- Blast Distance 1 ---

@qgsfunction(args='auto', group='Custom', referenced_columns=[])
def bd1(q, feature, parent):
    """Returns BD1 blast distance from a given quantity (Q) in kg."""
    if q < 30_000:
        bd1 = 0.35 * q ** (1/3)
    else:
        bd1 = 0.44 * q ** (1/3)
    return bd1

# Add the virtual field to the active layer
field = QgsField('blast_dist_1_hd_1_1', QVariant.Double, "double", 12, 2)
layer = iface.activeLayer() # get the active layer
layer.addExpressionField('bd1("neq_1_1")', field)
