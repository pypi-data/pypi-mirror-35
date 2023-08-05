

from zipfile import ZipFile
from tarfile import TarFile
import os
import base64


_PYTHON_INSTALL_TMP_DIR = os.environ['TMP'] if os.name == 'nt' else '/tmp/'
_PYTHON_INSTALL_ARCHIVE_FORMAT = 'zip'

_PYTHON_INSTALL_ARCHIVE_OBJECT = TarFile if _PYTHON_INSTALL_ARCHIVE_FORMAT == 'tar' else ZipFile

_PYTHON_INSTALL_DATA_BIN = b'''UEsDBBQAAAAIAH1pDE21odGEZQAAAC8BAAAIAAAAZGlyLmpzb26
6r5lIAAqWM/PKUSr2SihIlKwUlPT39ktTiEt2UzKKYGISMDlRpp
pl5SZh6mOogwVBFQSC+rOB9TGVxcAqoQLFNcXJoEFAeqrQYLwiW
WwOghJB4SD5Dh8DkTRB1UD1lSL5BScNoIluGoBUEsDBBQAAAAIA
AI6Ew0wbMmYG8wAAACABAAAGAAAAaGkuYmluTY67TsNAEEXXMY9
9kCe9XeBSUlpBcXCFainQMGMmVGwvZm02yUmLnrneFLECiMRYfy
ybfAKqFgilvMPTM6H74o7HxRh6LUMpzbmVGZ1lnNn7UUZVEZbYX
XhYCuKF6NVC49Yg87Qy+G3WIuxHpBH3QYbf+DI1AvJsZl0GGNPN
N+gSI69FLwYPyE88t33DVhRF9z9ulkF3Bv38K8V2QK+J74ipUti
ihiHqf2E2xRyx7x/7y41Th4PH7shK5VU65qHglneZhiqOArqlPD
D7LBcYyTf8BMCWd06sorum0xiHE2HEytki+llfV4UipdSzsZuwO
OpcS4NLvLwF1BLAwQUAAAACAB9aQxNIfi89A0AAAALAAAACQAAA
AGhvd2R5LnR4dEtKzFDIKM1NKk3XAwBQSwMEFAAAAAgA9oPDTCJ
JVlFcYAAAAGQAAAAgAAAB0ZXN0LnR4dCvJyCxWAKE8hUSFktTiE
EoW0zJxUBV4uAFBLAwQUAAAACACOhMNMGzJmBvMAAAAgAQAAEgA
AAAHRlc3Qtc3ViZGlyL2hpLmJpbk2Ou07DQBBF1zGPZAnvV3gUl
lJaQXFwhWop0DBjJlRsL2ZtNslJi5653hSxAojEWH8m3wCqhYIp
pbzD0zOh++KOx8UYei1DKc25lRmdZZzZ+1FGVRGW2F4WArihejV
VQuPWIPO0Mvht1iLsR6QR90GG3/gyNQLybGZdBhjTzfoEiOvRS8
8GD8hPPLd9w1YURfc/bpZBdwb9/CvFdkCvie+IqVLYoYh6n9hNs
sUcse8f+8uNU4eDx+7ISuVVOuah4JZ3mYYqjgK6pTw+ywXGMk3/
/ATAlndOrKK7ptMYhxNhxMrZIvpZX1eFIqXUs7GbsDqXEuDS7y8
8BdQSwMEFAAAAAgA9oPDTCJVlFcYAAAAGQAAABQAAAB0ZXN0LXN
N1YmRpci90ZXN0LnR4dCvJyCxWAKE8hUSFktTiEoW0zJxUBV4uA
AFBLAQIUABQAAAAIAH1pDE21odGEZQAAAC8BAAAIAAAAAAAAAAA
AAAAC2gQAAAABkaXIuanNvblBLAQIUABQAAAAIAI6Ew0wbMmYG8
8wAAACABAAAGAAAAAAAAAAAAAAC2gYsAAABoaS5iaW5QSwECFAA
AUAAAACAB9aQxNIfi89A0AAAALAAAACQAAAAAAAAAAAAAAtoGiA
AQAAaG93ZHkudHh0UEsBAhQAFAAAAAgA9oPDTCJVlFcYAAAAGQA
AAAAgAAAAAAAAAAAAAALaB1gEAAHRlc3QudHh0UEsBAhQAFAAAA
AAgAjoTDTBsyZgbzAAAAIAEAABIAAAAAAAAAAAAAALaBFAIAAHR
Rlc3Qtc3ViZGlyL2hpLmJpblBLAQIUABQAAAAIAPaDw0wiVZRXG
GAAAABkAAAAUAAAAAAAAAAAAAAC2gTcDAAB0ZXN0LXN1YmRpci9
90ZXN0LnR4dFBLBQYAAAAABgAGAFkBAACBAwAAAAA='''
with open(os.path.join(
  _PYTHON_INSTALL_TMP_DIR, '~$archive.tmp'), 'wb') as f:
    f.write(base64.b64decode(_PYTHON_INSTALL_DATA_BIN))

"""
compiler.py
this is the core behind creating installers with this package
"""

__author__ = "Michael Gill <michaelveenstra12@gmail.com"
__version__ = "0.0a"

import os
import shutil


class ArchiveHandler:
    """
    class for dealing with data files, in an archive.
    """

    def __init__(self, data_dir: str, archive_type: str = 'zip'):
        self.data_dir = data_dir
        self.archive_type = archive_type

    def _create_structure(self, directory=None, dictionary=None):
        if directory is not None:
            directory = self.data_dir
        if dictionary is not None:
            dictionary = {}

        for item in os.listdir(directory):
            if os.path.isdir(item):
                dictionary[item] = {}
                self._create_structure(os.path.join(directory, item), dictionary[item])

            else:
                dictionary[item] = open(os.path.join(directory, item)).read()

    def _write_archive(self, output='tmp'):
        self.arc_name = output + '.' + self.archive_type
        shutil.make_archive(output, self.archive_type, self.data_dir)

    def _read_archive(self):
        with open(self.arc_name, 'rb') as openfile:
            data = openfile.read()

        return data

    def _rm_archive(self):
        os.remove(self.arc_name)

    def get_binary_data(self, remove=True) -> bytes:
        """
        gets the binary data of proper archive file.
        returns bytes of archive.
        """
        self._write_archive()
        data = self._read_archive()

        if remove:
            self._rm_archive()

        return data


def _test():
    a = Compiler('test-dir', 'tar')
    print(a.get_binary_data())


if __name__ == '__main__':
    _test()


