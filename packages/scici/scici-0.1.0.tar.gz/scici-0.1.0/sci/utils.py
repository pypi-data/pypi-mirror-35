from pint.quantity import _Quantity
from sci import units
from pint.errors import UndefinedUnitError

def check_units(value, dimension: str):
    """ Check if units are of a certain dimension
    
    Parameters
    ---------- 
    value: `pint.quantity._Quantity`
        The pint :class:`pint.quantity._Quantity` to check
    dimemension: `str`
        Desired dimensionality of value

    Returns
    -------
    result: `bool`
        If the units are of the desired dimension, returns True.

    Raises
    ------
    ValueError
        Raised if the unit dimensions are incorrrect or the
        the value is not a pint unit quantity.

    Examples
    --------
    >>> check_units(100 * units.millilters, '[length]^3')
    True

    Notes
    -----
    See the pint_ documentation for more examples on dimensionality.

    .. pint_: https://pint.readthedocs.io/en/latest/wrapping.html#checking-dimensionality
    """
    try:
        if value.check(dimension):
            return True
        else:
            raise ValueError(f'{value} must contain pint units of dimension {dimension}.')
    except AttributeError:
        raise ValueError(f'{value} does contain pint units.(must be of dimension {dimension}).')


def filter_dict_values(input: dict, filter):
    ''' Filter dictionary values through a function called filter 
    
    This function will look recursively through nested dictionaries
    and call filter(value) on all dictionary values.

    Parameters
    ---------- 
    input: `dict`
        Input dictionary to filter
    filter: `callable``
        Function for filtering dictionary values.
        This is called in form filter(value)

    Returns
    -------
    filtered: `dict`
        Returns filtered dictionary     
    ''' 
    for k, v in input.items():
        if isinstance(v, dict):
            input[k] = filter_dict_values(v, filter)
        else:
            input[k] = filter(v)
    return input

def stringify(input):
    '''Convert pint quantities into strings
    
    Parameters
    ----------
    input: `pint.quantity._Quantity`
        Pint unit quantity

    Returns
    -------
    output: `str``
        input as a string
    '''
    if isinstance(input, _Quantity):
        return str(input)
    else:
        return input

def pintify(input: str):
    ''' Convert strings into pint quantities 
    
    Parameters
    ---------- 
    input: `str`
        String to be converted to pint quantity 
    
    Returns
    -------
    result: `pint.quantity._Quantity`
        input as a pint quantity
    ''' 
    try:
        return units(input)
    except UndefinedUnitError:
        return input

def check_kwargs(key, caller, **kwargs):
    ''' Check if kwargs has a needed field 
    
    Parameters
    ---------- 
    key: `str`
        keyword to look for in kwargs
    
    Returns
    -------
    value
        The value of the kwargs[key]
    params: `dict``
        The params dictionary (without the returned key/value pair)
    
    Raises
    ------
    ValueError
        Raised if the key does not exist in kwargs
    
    ''' 
    if not kwargs.get(key):
        raise ValueError('''{} needs to be an argumentwhen instantating a {}.'''
                            .format(key, caller))
    else:
        value = kwargs.pop(key)
        return value, kwargs