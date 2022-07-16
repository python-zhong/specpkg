# StoreData - A package that can pack / unpack dictionary into a special archive.
Welcome to use StoreData! This package can pack / unpack dictionary into a special archive.

# Installing
You can execute `pip install StoreData` to use it.

# Using
It is very easy to use. Like this:

    from StoreData import pack, unpack
    pack('D:/adir') # will pack it to 'D:/adir.archive'
    unpack('D:/adir.archive') # will unpack it to 'D:/adir.unpacked'

You can also run it in a command line:
> Pack example

    C:\Windows> python -m StoreData pack D:/adir

> Unpack example

    D:> python -m StoreData unpack D:/adir.archive

ENJOY!