def magic_string():
    magic_string.x = getattr(magic_string, 'x', 0) + 1
    return 'Holberton, ' + (magic_string.x - 1) + 'Holberton'
