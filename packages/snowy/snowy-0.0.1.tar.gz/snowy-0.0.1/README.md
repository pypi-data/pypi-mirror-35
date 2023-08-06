## Snowy

This is a tiny Python 3 module for manipulating and generating images.
- Simple and flat API. See the [documentation](https://github.prideout.net/snowy/).
- Supports resize and blur with a variety of filters.
- Honors a specified wrap mode for proper boundary behavior.
- Supports simple OpenEXR images (never clamps colors).
- Written purely in Python 3 and accelerated using [numba](https://numba.pydata.org/).
- Efficiently generates gradient noise and distance fields.

Snowy is somewhat similar to [pillow](https://python-pillow.org/) and
[scikit-image](https://scikit-image.org/), but has a small feature set with some unique abilities.
Painting and 2D paths are outside the scope of the library. See
  [pycairo](https://pycairo.readthedocs.io/en/latest/) or
  [skia-pathops](https://github.com/fonttools/skia-pathops).

<!--

travis and pip
  should run docs/generate as well as test_snowy

test the pip installation inside a virtualenv

- Color space
  - tests/gamma_dalai_lama_gray.jpg
  - Just a modicum ... at least in load / save -- is the blurry poodle slightly dark?
    Create a page in "test" and use chrome (test_colorspace.py)
  - Why isn't save doing a "img * 255.0" for PNG images?

open graph tags and thumbnail
  - https://github.prideout.net/snowy/
  - https://cards-dev.twitter.com/validator

TODO items after open source release

  Bug fix
    when saving a solid color image, I think this exception can be thrown:
    "Max value == min value, ambiguous given dtype"
    also, "Lossy conversion from float64 to uint8." warnings are annoying
  Improve the island gen example
    https://twitter.com/prideout/status/981356407202050048
  arbitrary rotation
  reduce_colors and to_svg
  io can have create_movie
    heat wave example
    brownian loop zoom example
  io can have generate_gallery for making HTML, and optional forced width/height/filter
  height field AO
  CPCF's
    try to repro https://twitter.com/prideout/status/981356407202050048
  variable radius blur (radius multiplier is a fn not a constant)
    test with a distance field + gradient
  prefiltering as seen in docs/hoppe
  pixel art scaling algorithm(s)
  add fractal.py
      mandelbrot example from numba
      also this: https://en.wikipedia.org/wiki/Buddhabrot
  generate voronoi or triangulations, like the little test images here:
      http://agea.github.io/tutorial.md/

-->
