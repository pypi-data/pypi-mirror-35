
def mkv(container):
    """Changes the `container` format to the MKV format."""
    container.extension = '.mkv'
    container.save()
    return container

def m4v(container):
    """Changes the `container` format to the M4V format."""
    container.extension = '.m4v'
    container.save()
    return container

