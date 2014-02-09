__author__ = 'Umut Karci'


class Veridis:
    """Veridis is the class that does all the logging and reading jobs
    example usage is;
        file_name = Veridis.dump(data)
        data = Veridis.load(file_name, delete=True)"""

    @classmethod
    def _check_type(cls, data):
        """This method determines if can we dump and load the data"""

    @classmethod
    def _check_folders(cls):
        """This method checks for main folder"""

    @classmethod
    def _dump_eval(cls, data, data_type):
        """This method prepares data to dump, maps data and returns file_name"""

    @classmethod
    def _load_eval(cls, file_name, delete):
        """This method prepares data to return, if wanted, removes the data"""

    @classmethod
    def _dump_data(cls, data, file_name):
        """This method dumps given data to file"""

    @classmethod
    def _load_data(cls, file_name):
        """This method loads data from given file_name and returns data"""

    @staticmethod
    def _dump_map(map_data, map_file):
        """This method dumps map file"""

    @staticmethod
    def _load_map(map_file):
        """This method loads map file and returns it"""

    @classmethod
    def dump(cls, data):
        """This method dumps your data and returns a file name"""

    @classmethod
    def load(cls, file_name, delete=False):
        """This method loads your data from the file, also removes optionally"""