class Command:

    def __init__(self, options):
        """
        Command Constructor

        :param options: Contains list of options parsed from docopt (list)
        """

        self._options = options

    def run(self):
        """
        Abstract method run for command

        :return: (None)
        """

        raise NotImplementedError
