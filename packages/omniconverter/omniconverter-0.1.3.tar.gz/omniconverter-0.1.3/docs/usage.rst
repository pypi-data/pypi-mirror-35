=====
Usage
=====

To use Omniconverter in a project::

    >>> from omniconverter import Converter
    
    >>> converter = Converter()

    >>> array = [1,2,3,"abc",5]

    >>> x = converter.array_to_string(array)

    >>> print(x)
    
    "123abc5"
