# /// script
# dependencies = [
#   "napari[pyqt6,optional]",
# ]
# ///

from skimage.filters import threshold_otsu, threshold_isodata, threshold_triangle, threshold_li
from magicgui import magicgui
from enum import Enum

import napari
from napari.layers import Image
from napari.types import LabelsData

threshold_method = {
    'Otsu': threshold_otsu,
    'Isodata': threshold_isodata,
    'Triangle': threshold_triangle,
    'Li': threshold_li
}

class ThresholdMethods(Enum):
    Otsu = 'Otsu'
    Isodata = 'Isodata'
    Triangle = 'Triangle'
    Li = 'Li'

@magicgui(auto_call=True)
def threshold_widget(image: Image, method: ThresholdMethods = ThresholdMethods.Otsu) -> LabelsData:
    threshold_value = threshold_method[method.value](image.data)
    return image.data > threshold_value

viewer = napari.Viewer()
viewer.window.resize(1000, 700)
viewer.open_sample('napari', 'cells3d')
viewer.window.add_dock_widget(threshold_widget)

if __name__ == "__main__":
    napari.run()
