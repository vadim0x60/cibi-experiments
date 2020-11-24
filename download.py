from zipfile import ZipFile
from urllib.request import urlopen
from shutil import rmtree
from io import BytesIO
from os import path

experiments_dir = path.dirname(__file__)
for subdir in path.listdir(experiments_dir):
    if path.isdir(subdir):
        rmtree(subdir)

resp = urlopen('https://surfdrive.surf.nl/files/index.php/s/Dzhu0tMETlKHPom/download')
ZipFile(BytesIO(resp.read())).extractall(experiments_dir)

