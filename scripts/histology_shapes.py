# /// script
# dependencies = [
#   "napari[pyqt6,optional]",
#   "pooch",
#   "napari-geojson",
#   "napari-tiff",
# ]
# ///

import zipfile
from pathlib import Path
import pooch
from typing import cast

import napari
from napari.layers import Shapes

# Define data directory
data_dir = Path(__file__).parent / 'data'
data_dir.mkdir(exist_ok=True)

# Download the geojson zip file using pooch
geojson_zip_path = pooch.retrieve(
    url="https://github.com/user-attachments/files/20297173/CMU-1-nucs.geojson.zip",
    known_hash="55184a6e9d2525207dffc49cc6251fcb2a8edde142bd9b29c4064bcdbea63d78",  # Will compute hash on first download
    path=data_dir,
    fname="CMU-1-nucs.geojson.zip",
)

# Extract the geojson file from the zip
geojson_path = data_dir / "CMU-1-nucs.geojson"
if not geojson_path.exists():
    with zipfile.ZipFile(geojson_zip_path, 'r') as zip_ref:
        zip_ref.extractall(data_dir)

# Download the SVS file using pooch
svs_path = pooch.retrieve(
    url="https://openslide.cs.cmu.edu/download/openslide-testdata/Aperio/CMU-1-JP2K-33005.svs",
    known_hash="9a1923cd9bcb260ba4d99d64f8d6e32550648c332ba48817f920662f3a513420",  # Will compute hash on first download
    path=data_dir,
    fname="CMU-1-JP2K-33005.svs"
)
viewer = napari.Viewer()

image = viewer.open(svs_path, plugin='napari-tiff')

geojson_layers = viewer.open(
    str(geojson_path),
    plugin='napari-geojson',
    face_color = 'yellow',
    opacity=0.7,
)
shapes = geojson_layers[0]

face_colors = shapes.face_color.copy()

face_colors[0] = (0, 0, 0, 0)
shapes.face_color = face_colors

viewer.fit_to_view(margin=0)

if __name__ == '__main__':
    napari.run()