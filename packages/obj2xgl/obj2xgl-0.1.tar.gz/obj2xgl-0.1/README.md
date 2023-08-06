# obj2xgl

`obj2xgl` converts a 3D model stored as a Wavefront (`.obj`) file into a C file
which can be linked into a program. The `x` in the name means that `obj2xgl`
supports not just OpenGL, but also other 3D graphic toolkits.


## Supported toolkits

* OpenGL
  - Immediate mode
  - Call lists (SOON!)
* Nintendo DS and 3DS (via [libnds](https://github.com/devkitPro/libnds))
  - Immediate mode
  - Call lists (SOON!)
* Nintendo Wii and Gamecube (via [libogc](https://github.com/devkitPro/libogc)) (SOON!)


## Examples

Please see the `examples` directory for a few examples on how to use this program.


## Useful links:

- [OpenGL ES reference documentation](https://registry.khronos.org/OpenGL/index_es.php)
