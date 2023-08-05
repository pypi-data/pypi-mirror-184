from ..colors import __colors__ as colors

def stringColor(cor:str) -> int:
    '''
    Using StringColor:

    >>> import hexacolors
    >>> hexacolors.stringColor('Blue')
    >>> print(hexacolors.listall) #List all colors availables
    '''

    return getattr(colors, cor.lower().replace(' ',''))()