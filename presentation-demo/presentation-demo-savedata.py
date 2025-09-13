from skimage.io import imread

import napari

title = """From the outside, in:
    How the napari community supports users
    and empowers transition to contribution
SciPy 2025 - July 11"""

author = "@TimMonko: napari & University of Minnesota"

img = imread(r'./data/tribolium.tif')
labels = imread(r'./data/tribolium_labels.tif')

viewer = napari.Viewer()

image = viewer.add_image(
    img,
    name='tribolium',
    colormap='plasma',

)
labels = viewer.add_labels(
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


font = viewer.window._qt_viewer.console._control.font()
font.setPointSize(22)
viewer.window._qt_viewer.console._control.setFont(font)
viewer.window._qt_viewer.toggle_console_visibility()

viewer.fit_to_view(margin=0)

if __name__ == '__main__':
    napari.run()