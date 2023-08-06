import sys
import os
import unittest
path = os.path.abspath('../')
sys.path.append(path)
from piomart.piomart_download import GetFiles


class TestQueries(unittest.TestCase):
    def test_download_ftp(self):
        GetFiles("Danio_rerio").download_ftp()
        files_list = ["Danio_rerio.GRCz11.93.gtf.gz"]
        for files in files_list:
            file_path = os.path.join(path, files)
            assert os.path.isfile(files) == True, "{} does not exist in the directory".format(file_path)

        for files in files_list:
            file_path = os.path.join(path, files)
            os.remove(files)

    def test_unzip(self):

        GetFiles("gorilla_gorilla").unzip()
        files_list = ["Gorilla_gorilla.gorGor4.93.gtf"]
        for files in files_list:
            file_path = os.path.join(path, files)
            assert os.path.isfile(files) is True, "{} does not exist in the directory".format(file_path)

        for files in files_list:
            file_path = os.path.join(path, files)
            os.remove(files)



    # def test_download_ftp_all(self):

    #     #Test that the download function is working
    #     GetFiles("Macaca_fascicularis","release-93",True).download_ftp()

    #     files_list = ["Macaca_fascicularis.Macaca_fascicularis_5.0.93.abinitio.gtf.gz"
    #                   ,"Macaca_fascicularis.Macaca_fascicularis_5.0.93.chr.gtf.gz"
    #                   ,"Macaca_fascicularis.Macaca_fascicularis_5.0.93.gtf.gz","CHECKSUMS"]
    #     for files in files_list:
    #         file_path = os.path.join(path, files)
    #         assert os.path.isfile(files) == True, "{} does not exist in the directory".format(file_path)

    #     for files in files_list:
    #         file_path = os.path.join(path, files)
    #         os.remove(files)

if __name__ == '__main__':
    unittest.main()
