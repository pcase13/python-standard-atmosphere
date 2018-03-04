# python-standard-atmosphere
Python package for creating pressure and temperature profiles of the standard atmosphere for use with geophysical models. This package will only calcualate good values up to 86km.

## Giving Credit Where it's Due
This package is mostly translated from a similar Fortran90 module created by Ralph Carmichael, Public Domain Aeronautical Software.

## Details, Details, Details
The package uses the 1976 standard atmosphere. If alt > 86, the values returned will not be correct, but they will not be too far removed from the correct values for density.
