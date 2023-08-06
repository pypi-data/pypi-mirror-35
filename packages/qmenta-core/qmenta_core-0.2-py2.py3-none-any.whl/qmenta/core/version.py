try:
    FileNotFoundError
except NameError:
    # Python 2 does not have FileNotFoundError
    FileNotFoundError = IOError


def create(release, revfile=None):
    """
    Create a version string composed of the release version and the (optional)
    revision number read from a file. The release version will be postfixed
    with '.dev' + revision number.

    It is recommended to use::

        git rev-list --count HEAD > qmenta_module/python/qmenta/module/REVISION

    to set the revision number for internal development releases, and to
    not create the REVISION file when creating a public release so that the
    version equals ``major.minor`` from the release string.

    Parameters
    ----------
    release : str
        The release number. Example: '2.1'
    revfile : str
        The filename of the revision file.
        Example: '/home/ubuntu/python/qmenta/module/REVISION'.
        It must be a text file containing **only** the revision number.

    Raises
    ------
    ValueError
        When no release version is given

    Returns
    -------
    str
        The composited version. Examples: '2.1' if revfile does not exist,
        or '2.1.dev333' if revfile exists and contains revision '333'.
    """
    if not release:
        raise ValueError('No release string specified')

    revision = None
    try:
        with open(revfile) as f:
            revision = f.read().strip()
    except FileNotFoundError:
        pass
    except TypeError:
        # no revfile set
        pass

    if revision:
        v = '.'.join([release, 'dev' + revision])
    else:
        v = release
    return v
