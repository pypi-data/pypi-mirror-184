try:
    from pynut_3ftp.pyNutFtp import nutFtp as ftp
except:
    try:
        from pyNutFtp import nutFtp as ftp
    except:
        print('Online Test...')
        from pyNut import pyNutFtp as ftp

import pytest


# python -m pytest test/test_nutFtp.py



#=============================================================================
# UNIT TEST
#=============================================================================
def test_sftp_PPK_DownloadFile_NoPPKFile():
    str_pathKey_ppk = r'C:\temp_dev\OpenSSH_SG_LGI.ppk'



def test_sftp_PPK_DownloadFile():
    str_pathKey_ppk =   r'C:\Users\laurent.tupin\IHS Markit\HK PCF Services Team - General\Auto_py\file\_input\OpenSSH_SG_LGI.ppk'
    str_FTP_server =    r'sfg.sgx.com'
    str_FTP_uid =       r'sfgmcicmarkit'
    int_FTP_port =      38040
    str_FTP_directory = r'/inbox'
    str_fileName =      'PREDICT_SGLC50CP_{*}.csv'
    str_folderRaw = ''

    # ftp.sftp_PPK_DownloadFile(str_FTP_server, str_FTP_uid, str_FTP_directory, str_fileName, str_folderRaw,
    #                           int_port=int_FTP_port, str_pathKey_ppk=str_pathKey_ppk
    #                           )








