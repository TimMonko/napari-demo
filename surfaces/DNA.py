# /// script
# dependencies = [
#   "napari[pyqt6,optional]",
#   "vispy",
# ]
# ///

from vispy.io import read_mesh
import napari
from pathlib import Path

# Get the directory of this script to build correct path
data_path = Path(__file__).parent / 'data' / '1BNA.obj.gz'

vertices, faces, _, _ = read_mesh(str(data_path))

viewer = napari.Viewer(ndisplay=3)
viewer.window.resize(1000, 700)

layer = viewer.add_surface((vertices, faces), name='1BNA', shading='smooth')

viewer.camera.angles = (90, 0, 90)

napari.run()
