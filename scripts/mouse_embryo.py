# /// script
# dependencies = [
#   "napari[pyqt6,optional]",
#   "pooch",
# ]
# ///

import napari
import pathlib
import pooch

# Create a data cache directory
data_dir = pathlib.Path(__file__).parent / 'data'
data_dir.mkdir(exist_ok=True)

# Use pooch to download and cache the file
url = "https://api.mousephenotype.org/tracker/media/emb2/8/9/0/19/843/40869/603913_download.nrrd"

data_path = pooch.retrieve(
    url=url,
    known_hash=None,  # Set to None to skip hash verification
    path=str(data_dir),
    fname="mouse_embryo.nrrd",
    progressbar=True,
)

viewer = napari.Viewer()
viewer.open(data_path)  # data_path is already a string from pooch.retrieve

if __name__ == '__main__':
    napari.run()
