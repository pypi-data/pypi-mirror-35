import os
import subprocess

from tokenizers_collection import ltp_data_base_dir
from tokenizers_collection.download_then_unzip import download_extract_zip


def post_install_action():
    # download the latest license for nlpir
    subprocess.call("pynlpir update", shell=True)

    if not os.path.exists(ltp_data_base_dir):
        os.mkdir(ltp_data_base_dir)

    if not os.path.isdir(ltp_data_base_dir):
        raise Exception("{} must be a directory".format(ltp_data_base_dir))

    download_extract_zip(
        'http://ospm9rsnd.bkt.clouddn.com/model/ltp_data_v3.4.0.zip',
        ltp_data_base_dir
    )


def get_ltp_data_file():
    for root, dirs, files in os.walk(ltp_data_base_dir, topdown=False):
        if 'cws.model' in files:
            return os.path.join(root, 'cws.model')

    raise Exception("Not found 'cws.model' in {}".format(ltp_data_base_dir))


if __name__ == "__main__":
    post_install_action()
