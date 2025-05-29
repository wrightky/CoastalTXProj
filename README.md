# Along-Coast Reference Frame for the Texas Coast

`coastx` is a simple Python package for reprojecting latitude/longitude coordinates near the Texas coast into a linear, along-coast reference frame.

## Installation

To build from source, clone this repository, navigate to the cloned directory, and then run the following in the desired environment:
```
python -m pip install .
```

**Requirements**: `numpy`, `matplotlib`, and `xarray`

## Example Usage

For some `(N,2)` array `degree_coordinates`, which contains `longitude` in the first column and `latitude` in the second, convert to along-coast coordinates as follows:
```
import coastx

coastal_coordinates = coastx.transform(degree_coordinates)
```
The new array `coastal_coordinates` will contain `distance_along_coast` in the first column and `distance_inland` in the second. The units are still in degrees, but given that `latitude` and `longitude` do not strictly speaking have the same scale, the units should perhaps be considered *pseudo-degrees*. If you would prefer the units be *pseudo-kilometers*, multiply the entire array by a scaling factor of `111.28692`.

Note that any coordinates outside of the reference zone (either too far from the coastline or too far from Texas) will return as `NaN`.

The below example shows a coarsened version of the [Pekel et al.](https://doi.org/10.1038/nature20584) water frequency map for Texas reprojected into the `coastx` reference frame.

<div class="nav3" style="width:800px;">
    <img src="https://github.com/wrightky/CoastalTXProj/blob/main/coastx_proj.png?raw=true" alt="Image" width="100%"></a>
</div>

## Contributing

Please feel free to open an issue or a pull request!