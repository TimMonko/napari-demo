# /// script
# dependencies = [
#   "napari[pyqt6,optional]",
#   "napari-ome-zarr",
# ]
# ///

import napari

viewer = napari.Viewer()
viewer.open('https://uk1s3.embassy.ebi.ac.uk/idr/zarr/v0.4/idr0048A/9846152.zarr/', plugin='napari-ome-zarr')
# viewer.open("https://uk1s3.embassy.ebi.ac.uk/idr/zarr/v0.4/idr0101A/13457537.zarr", plugin="napari-ome-zarr")

if __name__ == "__main__":
    napari.run()
