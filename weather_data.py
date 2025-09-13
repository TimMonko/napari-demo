# /// script
# dependencies = [
#   "napari[pyqt6,optional,docs]",
# ]
# ///
import napari
import xarray as xr

# function to convert xarray metadata to napari layer metadata
def get_scale_translate(dataset, array_name):
    array = getattr(dataset, array_name)
    dims = [getattr(dataset, dim) for dim in array.dims]
    translate = [float(d[0]) for d in dims]
    scale = [float(d[1] - d[0]) for d in dims]
    return {'scale': scale, 'translate': translate}

sst = xr.tutorial.open_dataset('ersstv5')
viewer, sst_layer = napari.imshow(
        sst.sst,
        name='sea surface temp',
        **get_scale_translate(sst, 'sst'),
        colormap='magma',
        )
viewer.dims.axis_labels = sst.sst.dims
viewer.axes.visible = True
viewer.camera.orientation2d = ('up', 'right')

napari.run()