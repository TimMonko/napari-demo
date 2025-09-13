# Demo Repo for Various napari Presentations

**Work in Progress**

## Setup instructions

You can run scripts with uv without creating an environment due to inline dependency management.

`uv run scripts/weather_data.py`

Create a virtual environment and install napari with optional dependencies.

With uv:

```
uv venv --python 3.12
.venv\Scripts\activate
uv pip install "napari[pyqt6,optional,docs]>=0.6.2"
```

With conda:

```
conda create -n napari-demo python=3.12
conda activate napari-demo
pip install "napari[pyqt6,optional,docs]>=0.6.2"
```

Alternatively, you can make a temporary install of napari with uv:

`uvx --with "napari[pyqt6,optional,docs]>=0.6.2" napari`

## Other Ideas

### Brainrender with napari

`uvx --with "napari[pyqt6,optional]" --with brainrender-napari -p 3.12 napari`
