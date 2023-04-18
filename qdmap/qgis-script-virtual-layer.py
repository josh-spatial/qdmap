# script to add the quantity-distances in a virutal fields for the activate layer
# ****
# Note: The QGIS Python scripts provided here work as intended for a single QD function. But they may need to be improved to loop through multiple functions or adapted to be used with GeoPandas Geodataframes.

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

# Adding a buffer layer based on a QD.
processing.runAndLoadResults("native:buffer", {
		# update the INPUT based on my new Google Drive folder.
    'INPUT':'/Users/josh/My Drive (wustner@gmail.com)/programming/qgis/pes_g.gpkg|layername=pes_g',
    'DISTANCE':QgsProperty.fromExpression('"blast_dist_1_hd_1_1"'),
    'SEGMENTS':40,
    'END_CAP_STYLE':0,
    'JOIN_STYLE':0,
    'MITER_LIMIT':2,
    'DISSOLVE':False,
    'OUTPUT':'TEMPORARY_OUTPUT'})
