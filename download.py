from zipfile import ZipFile
from urllib.request import urlopen
from shutil import rmtree
from io import BytesIO
import os

experiments_dir = os.path.dirname(__file__)
for subdir in os.listdir(experiments_dir):
    if os.path.isdir(subdir):
        rmtree(subdir)

resp = urlopen('https://surfdrive.surf.nl/files/index.php/s/Dzhu0tMETlKHPom/download')
ZipFile(BytesIO(resp.read())).extractall(experiments_dir)

