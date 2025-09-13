# /// script
# dependencies = [
#   "napari[pyqt6,optional]",
# ]
# ///

from magicgui import magicgui
from skimage.filters import threshold_otsu

import napari
from napari.layers import Image
from napari.types import LabelsData

@magicgui
def threshold_widget(image: Image) -> LabelsData:
    return image.data > threshold_otsu(image.data)

viewer = napari.Viewer()
viewer.window.resize(1000, 700)
viewer.open_sample('napari', 'cells3d')
viewer.window.add_dock_widget(threshold_widget)

if __name__ == "__main__":
    napari.run()
