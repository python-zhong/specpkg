# specpkg - A package that can pack / unpack dictionary into a special archive.
Welcome to use `specpkg`! This package can pack / unpack dictionary into a special archive.

# Installing
You can execute `pip install specpkg` to use it.

# Using
It is very easy to use. Like this:

    from specpkg import pack, unpack
    pack('D:/adir') # will pack it to 'D:/adir.archive'
    unpack('D:/adir.archive') # will unpack it to 'D:/adir.unpacked'

You can also run it in a command line:
> Pack example

    C:\Windows> python -m specpkg pack D:/adir

> Unpack example

    D:> python -m specpkg unpack D:/adir.archive

ENJOY!