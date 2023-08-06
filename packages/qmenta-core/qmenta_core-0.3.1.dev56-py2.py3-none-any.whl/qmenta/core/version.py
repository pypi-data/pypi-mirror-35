from os import path
import yaml


def read(dirname):
    """
    Read the version from a file.

    Parameters
    ----------
    dirname : str
        The directory that contains the ``VERSION`` file

    Raises
    ------
    IOError
        When the input file cannot be read

    Returns
    -------
    str
        The version read from the file
    """
    filename = path.join(dirname, 'VERSION')
    # Can raise IOError
    with open(filename) as f:
        v = f.read()
    return v.strip()


def write(version, dirname):
    """
    Write the given version to the ``VERSION`` file in the specified directory.
    If the file exists, it will be overwritten.

    Parameters
    ----------
    version : str
        The version string to write to the file. Newline will be appended.
    dirname : str
        The directory in which the VERSION file will be written

    Raises
    ------
    IOError
        When the file cannot be written
    """
    filename = path.join(dirname, 'VERSION')
    with open(filename, 'w') as f:
        f.write(version)
        # Without newline don't see the version if we 'cat' the file on Jenkins
        f.write('\n')


def from_build_yaml_and_revfile(dirname):
    """
    Create a version string composed of the release version specified in
    the ``build.yaml`` file and revision in the ``REVISION`` file that are
    located in the specified directory.

    Parameters
    ----------
    dirname : str
        The directory where the ``build.yaml`` and optional ``REVISION`` files
        are located

    Raises
    ------
    IOError
        When the ``build.yaml`` file cannot be read
    KeyError
        When the ``build.yaml`` file does not contain a version
    ValueError
        When the ``version`` in ``build.yaml`` is an empty string,
        or ``build.yaml`` is not a valid YAML file.

    Returns
    -------
    str
        The composited version. Examples: '2.1' if there is no ``REVISION``
        file, or '2.1.dev333' if ``REVISION`` and contains revision '333'.
    """
    # Potential IOError
    with open(path.join(dirname, 'build.yaml')) as build_yaml:
        build_specs = yaml.load(build_yaml)

    if not isinstance(build_specs, dict):
        raise ValueError('Invalid yaml file.')

    release = str(build_specs['version'])
    revfile = path.join(dirname, 'REVISION')
    return from_str_and_revfile(release, revfile)


def from_str_and_revfile(release, revfile=None):
    """
    Create a version string composed of the release version and the (optional)
    revision number read from a file. The release version will be postfixed
    with '.dev' + revision number.

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
    except IOError:
        pass
    except TypeError:
        # no revfile set
        pass

    if revision:
        v = '.'.join([release, 'dev' + revision])
    else:
        v = release
    return v
