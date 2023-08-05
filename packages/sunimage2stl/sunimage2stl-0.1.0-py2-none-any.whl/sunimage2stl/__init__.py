"""
sunimage2stl
============
Provides 
    1. A way to retrieve xrt Images
        - Plot them in 2D and 3D
        - Convert them to flat stl 
        - Convert them to hemispherical mesh
    2. A Way to input select images of solar features
        - Plot them in 2D
        - Convert them to flat stl    
How to use the documentation
----------------------------
View the function's documentation strings using the built-in ``help`` function:
  >>> help(function)
----------------------
3Dplot
    contains all the xrt data retrieval and processing, 3D spherical meshes etc.
ImagePlot
    contains all the partial sun functionality, plots any png
"""
import threeDplot
import imagePlot
