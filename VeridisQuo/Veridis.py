__author__ = 'Umut Karci'
from os.path import expanduser, exists
from os import makedirs, remove
from gzip import compress, decompress
import json


class Veridis:
    """Veridis is the class that does all the logging and reading jobs
    example usage is;
        file_name = Veridis.dump(data)
        data = Veridis.load(file_name, delete=True)"""
    main_folder = expanduser("~/.vq/")
    map_file = main_folder + ".map"
    primitive_types = {"s": str, "i": int, "f": float, "c": complex}

    @classmethod
    def __len__(cls):
        return len(cls._load_map(cls.map_file))

    @classmethod
    def __getitem__(cls, item):
        return cls.load(item+".vd")

    @classmethod
    def _check_type(cls, data):
        """This method determines if can we dump and load the data"""
        for data_name, data_type in cls.primitive_types.items():
            if isinstance(data, data_type):
                return True, data_name

    @classmethod
    def _check_folders(cls):
        """This method checks for main folder"""
        if not exists(cls.main_folder):
            makedirs(cls.main_folder)
        if not exists(cls.map_file):
            with open(cls.map_file, "w+") as empty_map:
                json.dump({}, empty_map)
                empty_map.close()

    @staticmethod
    def _key_exists(key, dict_keys):
        if key in dict_keys:
            return True
        return False

    @classmethod
    def _dump_eval(cls, data, data_type):
        """This method prepares data to dump, maps data and returns file_name"""
        cls._check_folders()
        data_map = cls._load_map(cls.map_file)
        bytes_data = str(data).encode("UTF-8")
        initial_file_no = 0
        while cls._key_exists(str(initial_file_no) + ".vd", data_map.keys()):
            initial_file_no += 1
        file_name = str(initial_file_no) + ".vd"
        data_map[file_name] = data_type
        cls._dump_data(bytes_data, file_name)
        cls._dump_map(data_map, cls.map_file)
        return file_name

    @classmethod
    def _load_eval(cls, file_name, delete):
        """This method prepares data to return, if wanted, removes the data"""
        data_map = cls._load_map(cls.map_file)
        data_type = data_map[file_name]
        read_data = cls._load_data(file_name)
        data = decompress(read_data).decode("UTF-8")
        original_data = cls.primitive_types[data_type](data)
        if delete:
            remove(cls.main_folder + file_name)
            del data_map[file_name]
            cls._dump_map(data_map, cls.map_file)
        return original_data

    @classmethod
    def _dump_data(cls, data, file_name):
        """This method dumps given data to file"""
        with open(cls.main_folder + file_name, "w+b") as dump_file:
            dump_file.write(compress(data, compresslevel=5))
            dump_file.close()

    @classmethod
    def _load_data(cls, file_name):
        """This method loads data from given file_name and returns data"""
        with open(cls.main_folder + file_name, "r+b") as dump_file:
            read_data = dump_file.read()
            dump_file.close()
        return read_data

    @staticmethod
    def _dump_map(map_data, map_file):
        """This method dumps map file"""
        with open(map_file, "w+") as json_file:
            json.dump(map_data, json_file)
            json_file.close()

    @staticmethod
    def _load_map(map_file):
        """This method loads map file and returns it"""
        with open(map_file, "r+") as json_file:
            read_map = json.load(json_file)
            json_file.close()
        return read_map

    @classmethod
    def dump(cls, data):
        """This method dumps your data and returns a file name"""
        can_log, data_type = cls._check_type(data)
        if can_log:
            file_name = cls._dump_eval(data, data_type)
            return file_name
        else:
            raise Exception("Unsupported Format")

    @classmethod
    def load(cls, file_name, delete=False):
        """This method loads your data from the file, also removes optionally"""
        data = cls._load_eval(file_name, delete)
        return data