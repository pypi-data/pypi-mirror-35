This is pynng.
==============

Ergonomic bindings for [nanomsg next generation] \(nng), in Python.
pynng provides a nice interface on top of the full power of nng.  nng makes it
easy to communicate between processes on a single computer or computers across
a network.  Like, really easy.  So easy, even an old chunk of coal like me can
do it.

Goals
=====

Provide a Pythonic, works-out-of-the box on Windows and Unix-y platforms.  Like
nng itself, the license is MIT, so it can be used without restriction.

This project is in early stages now; support for Mac is non-existent, support
for Windows is limited.  None of the installation is automated.

TODO
====

* Right now I'm modifying the CMake build file to set
  `CMAKE_POSITION_INDEPENDENT_CODE`.  This avoids problems when linking into
  the final .so file, but there is probably a better way to do it.
  Additionally, I only do this on Linux; on Windows I leave CMake alone.
* Generating the API file is fragile, becuase it is not remotely C syntax
  aware; it's just dumb old sed.
* Do the right thing for 32/64 bit Python on Windows.
* Support Mac
* Automate the binding building
  - setup.py should do everything;  it needs to build the nng library, and it
    needs to make sure to use the right compiler version on Windows depending
    on the Python version (ugh!).  Mac and Linux should Just Work™.
  - setup.py also needs to handle any necessary patching of the CMakeLists
    files.  paiiiin.

[nanomsg next generation]: https://nanomsg.github.io/nng/index.html
