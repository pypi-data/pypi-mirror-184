from io import BytesIO

from file_process.csv import CSVFileProcessor
from file_process.exceptions import WrongExtension
from file_process.h5 import H5ADFileProcessor


class FileProcessFactory:  # pylint: disable=too-few-public-methods
    @classmethod
    def get(cls, filename: str, file: BytesIO, **kwargs):
        if filename.endswith('.h5ad'):
            return H5ADFileProcessor(file, **kwargs)
        if filename.endswith('.csv'):
            return CSVFileProcessor(file, **kwargs)
        raise WrongExtension
