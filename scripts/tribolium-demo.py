# /// script
# dependencies = [
#   "napari[pyqt6,optional]",
#   "pooch",
# ]
# ///

import scipy.ndimage as ndimage
from skimage import filters, measure, morphology, segmentation
from skimage.io import imread, imsave
import numpy as np
from pathlib import Path
import pooch

import napari

# Define data directory
data_dir = Path(__file__).parent / 'data'
data_dir.mkdir(exist_ok=True)

# Download data using pooch.retrieve and put it in the data directory
raw_path = pooch.retrieve(
    url="https://github.com/clEsperanto/clesperanto_example_data/raw/main/Lund-100MB.tif",
    known_hash=None,  # Will compute hash on first download
    path=data_dir,
    fname="tribolium.tif"
)
labels_path = data_dir / 'tribolium_labels.tif'

# Load the raw image
img = imread(str(raw_path))

# Check if labels already exist, if not create them
if labels_path.exists():
    labels = imread(str(labels_path))
else:
    print("Creating labels from raw image...")
    labels = np.zeros_like(img, dtype=np.uint16)

    for t in range(img.shape[0]):
        print(f"Processing timepoint {t+1}/{img.shape[0]}")
        t_img = img[t, :, :, :]
        # use a tophat filter to remove the background
        img_bs = ndimage.white_tophat(t_img, size=15)

        # blur the image to smooth out noise from the background subtraction
        img_blur = filters.gaussian(img_bs, 1)

        # detect maxima in the blurred image for watershed seeds
        img_spot_maxima = morphology.local_maxima(img_blur)

        # create a threshold mask
        img_otsu = img_blur > filters.threshold_otsu(img_blur)

        # keep only maxima spots that are inside a thresholded area
        img_threshold_spots = img_spot_maxima * img_otsu

        # create a connected components labeling of the thresholded image
        # using the local maxima as markers, as a seed for a voronoi diagram
        img_labeled_spots = measure.label(img_threshold_spots)
        img_labels = segmentation.watershed(
            img_otsu,
            markers=img_labeled_spots,
            mask=img_otsu
        )
        
        labels[t, :, :, :] = img_labels

    imsave(str(labels_path), labels)

viewer = napari.Viewer()

image = viewer.add_image(
    img,
    name='tribolium',
    colormap='plasma',
)

labels_layer = viewer.add_labels(
    labels,
    name='tribolium labels',
    opacity=0.8,
    iso_gradient_mode='smooth'
)

viewer.dims.ndisplay = 3
viewer.dims.axis_labels = ('Time', 'Z', 'Y', 'X')
viewer.grid.enabled = True
viewer.camera.angles = (100, -10, 65)

viewer.axes.visible = True
viewer.scale_bar.visible = True
viewer.scale_bar.unit = 'μm'
viewer.scale_bar.font_size = 20

viewer.fit_to_view(margin=0)

if __name__ == '__main__':
    napari.run()
