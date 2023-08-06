# mainly copied from
# https://techoverflow.net/2018/01/16/downloading-reading-a-zip-file-in-memory-using-python/

import requests
import io
import zipfile


def download_extract_zip(url, unzip_dir):
    """
    Download a ZIP file and extract its contents in memory
    yields (filename, file-like object) pairs
    """
    response = requests.get(url)
    with zipfile.ZipFile(io.BytesIO(response.content)) as zipfile_object:
        zipfile_object.extractall(unzip_dir)
