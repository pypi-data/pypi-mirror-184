# NWP Downloading Utilities

## Development

Setting up a development space

```sh
conda create --name nwpdl-dev python=3.9
conda activate nwpdl-dev
conda install numpy xarray pandas
conda install -c conda-forge pyresample
conda install -c conda-forge netCDF4
conda deactivate nwpdl-dev
conda activate nwpdl-dev
```

## Build and Distribute

Setup environment

```sh
conda create --name nwpdl-build python=3.9
conda activate nwpdl-build
pip install --upgrade pip
pip install --upgrade build
pip install --upgrade twine
```

Build and upload

```sh
python -m build
python -m twine upload --repository testpypi dist/* 
```

Test build

```sh
conda create --name nwpdl-test python=3.9
conda activate nwpdl-test
pip install --index-url https://test.pypi.org/simple/ --no-deps nwp-dl-utils
```
