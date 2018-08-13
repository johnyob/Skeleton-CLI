import sys


def read_file(file_location):
    """
    Reads the file stored at :param file_location

    :param file_location: absolute path for the file to be read (string)
    :return: contents of file (string)
    """

    try:
        with open(file_location, "r") as file:
            return file.read()
    except FileNotFoundError:
        print("Failed to read {0}", file=sys.stderr)
        return ""


def write_file(file_location, data):
    """
    Writes :param data to the file stored at :param file_locations

    :param file_location: absolute path for the file that is being written too (string)
    :param data: data that will be written to the file (string)
    :return: (None)
    """

    with open(file_location, "w") as file:
        file.write(data)
