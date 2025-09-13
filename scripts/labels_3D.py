# /// script
# dependencies = [
#   "napari[pyqt6,optional]",
# ]
# ///

import numpy as np
from scipy import ndimage as ndi
from skimage import data, filters, morphology

import napari

cells3d = data.cells3d()
viewer = napari.Viewer()
membranes_layer, nuclei_layer = viewer.add_image(
    cells3d, channel_axis=1, name=['membranes', 'nuclei']
)
membrane, nuclei = cells3d.transpose((1, 0, 2, 3)) / np.max(cells3d)
edges = filters.scharr(nuclei)
denoised = ndi.median_filter(nuclei, size=3)
thresholded = denoised > filters.threshold_li(denoised)
cleaned = morphology.remove_small_objects(
    morphology.remove_small_holes(thresholded, 20**3),
    20**3,
)

segmented = ndi.label(cleaned)[0]

labels_layer = viewer.add_labels(segmented)

viewer.dims.ndisplay = 3
viewer.camera.angles = (-10,35,125)

if __name__ == '__main__':
    napari.run()
