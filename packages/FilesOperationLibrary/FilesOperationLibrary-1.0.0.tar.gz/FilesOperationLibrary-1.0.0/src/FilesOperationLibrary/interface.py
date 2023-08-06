# -*- coding: utf-8 -*-
"""
:created on: 2018/8/28

:copyright: 
:author: leo
:contact: 
"""

import logging
import os
import shutil
from  store import Store
from .handle_xml import XmlHandler
from .handle_txt import TxtHandler
from .handle_ftp import FtpHandler
from .handle_ftp import SFtpHandler
from .handle_csv import CsvHandler
from .handle_bin import BinHandler
from .handle_xls import XlsHandler
from .unzip_file import ArchiveFile
from .handle_log import OperateLog
from .exception import TAFileException


class OperateXml(object):
    """for setup/teardown/modify/add/remove/get xml file
    """

    def __init__(self):
        self.store = Store()

    def setup_xml(self, src_file, save_path=None, **kwargs):
        """setup xml file

        :param string src_file: the source xml file
        :param string save_path: the save xml file name.if None will use source file name
        """
        hander = XmlHandler()
        if not save_path:
            save_path = src_file
        hander.setup(src_file, save_path)
        self.store.add(hander, alias=kwargs.get('alias'))

    def teardown_xml(self, **kwargs):
        """teardown xml file
        """
        alias = kwargs.get('alias')
        self.store.get(alias).teardown()
        self.store.remove(alias=kwargs.get('alias'))

    def modify_xml_text(self, *args, **kwargs):
        """modify xml node text

        :param string args: such as .//managedObject[@class="LNBTS"]/p[@name="actDLCAggr"]:false
        """
        alias = kwargs.get('alias')
        self.store.get(alias).modify_node_text(*args)

    def modify_xml_attribute(self, *args, **kwargs):
        """modify xml node attribute

        :param string args: such as .//managedObject[@class\="NOKLTE:LNCEL_TDD"]:@version\=TL17_1610_01_1610_02
        """
        alias = kwargs.get('alias')
        self.store.get(alias).modify_node_attribute(*args)

    def add_xml_node(self, *args, **kwargs):
        """add xml node

        :param string args: such as .//managedObject[@class="LNBTS"]/list[@name="qciTab6"]/item:<p name="nbrDl">10240</p>
        """
        alias = kwargs.get('alias')
        self.store.get(alias).add_node(*args)

    def delete_xml_node(self, *args, **kwargs):
        """delete xml node

        :param string args: such as .//managedObject[@class="LNCEL"][@distName="0"]/list/item/p[@name="dFpucchF1b"]
        """
        alias = kwargs.get('alias')
        self.store.get(alias).delete_node(*args)

    def read_xml_text(self, *args, **kwargs):
        """get xml node text value

        :param string args: such as .//managedObject[@class="LNCEL"][@distName="0"]/list/item/p[@name="dFpucchF1b"]
        """
        alias = kwargs.get('alias')
        return self.store.get(alias).get_node_text(*args)

    def read_xml_attribute(self, *args, **kwargs):
        """get xml node attribute value

        :param string args: such as .//managedObject[@class\="NOKLTE:LNCEL_TDD"]:@version
        """
        alias = kwargs.get('alias')
        return self.store.get(alias).get_node_attribute(*args)


class OperateTxt(object):
    """for setup/teardown/modify/add/remove/get txt file
    """

    def __init__(self):
        self.store = Store()

    def setup_txt(self, src_file, save_path=None, **kwargs):
        """setup txt file

        :param string src_file: the source txt file
        :param string save_path: the save txt file name.if None will use source file name
        """
        hander = TxtHandler()
        if not save_path:
            save_path = src_file
        hander.setup(src_file, save_path)
        self.store.add(hander, alias=kwargs.get('alias'))

    def teardown_txt(self, **kwargs):
        """teardown txt file
        """
        alias = kwargs.get('alias')
        self.store.get(alias).teardown()
        self.store.remove(alias=kwargs.get('alias'))

    def modify_txt_node(self, *args, **kwargs):
        """modify txt node

        :param string args: such as 0x10042:0x0A691892  0x10043:51015
        """
        alias = kwargs.get('alias')
        self.store.get(alias).modify_node(*args)

    def add_txt_node(self, *args, **kwargs):
        """add txt node
        :param string args: such as '0x10301:1#MAC L2' or '0x10302:2'
        """
        alias = kwargs.get('alias')
        self.store.get(alias).add_node(*args)

    def delete_txt_node(self, *args, **kwargs):
        """delete txt node

        :param string args: such as '0x10049'
        """
        alias = kwargs.get('alias')
        self.store.get(alias).delete_node(*args)

    def read_txt_node(self, *args, **kwargs):
        """get txt node text value

        :param string args: such as '0x10040'
        """
        alias = kwargs.get('alias')
        return self.store.get(alias).get_node_text(*args)


class FtpUploadDownload(object):
    """upload and download files
    """

    def __init__(self):
        self.ftp_handler = FtpHandler()
        self.sftp_handler = SFtpHandler()
        self.store = Store()

    def ftp_download(self, host, port, usr, pwd, remote, local=None, **kwargs):
        """ftp download file
        :param host: such as '192.168.255.1'
        :param port: such as 21
        :param usr: username such as 'admin'
        :param pwd: password such as 'admin'
        :param remote: file in host such as '/tmp/rat_psconfig.xml'
        :param local: file path to save in local such as 'example/config1/rat1.xml','example/config1/', 'rat1.xml', None
        """
        self.store.add(self.ftp_handler, alias=kwargs.get('alias'))
        alias = kwargs.get('alias')
        self.store.get(alias).connect_ftp(host, port, usr, pwd)
        dnload_file = self.store.get(alias).ftp_download(remote, local)
        self.store.get(alias).close_ftp()
        self.store.remove(alias=kwargs.get('alias'))
        return dnload_file

    def ftp_upload(self, host, port, usr, pwd, local, remote=None, **kwargs):
        """ftp upload file
        :param host: such as '192.168.255.1'
        :param port: such as 21
        :param usr: username such as 'admin'
        :param pwd: password such as 'admin'
        :param local: file in local such as '/tmp/rat_psconfig.xml'
        :param remote: file path to save in host such as '/tmp/tmp1/rat_psconfig_test1.xml', '/tmp/tmp1/', 'rat_psconfig_test1.xml', None
        """
        self.store.add(self.ftp_handler, alias=kwargs.get('alias'))
        alias = kwargs.get('alias')
        self.store.get(alias).connect_ftp(host, port, usr, pwd)
        self.store.get(alias).ftp_upload(local, remote)
        self.store.get(alias).close_ftp()
        self.store.remove(alias=kwargs.get('alias'))

    def sftp_download(self, host, port, usr, pwd, remote, local=None, **kwargs):
        """sftp download file or dir recursively
        :param host: such as '192.168.255.1'
        :param port: such as 22
        :param usr: username such as 'admin'
        :param pwd: password such as 'admin'
        :param remote: file in host such as '/tmp/rat_psconfig.xml' or folder '/tmp/'(NOT '/tmp')
        :param local: file path to save in local such as 'example/config1/rat1.xml','example/config1/', 'rat1.xml', None
        """
        self.store.add(self.sftp_handler, alias=kwargs.get('alias'))
        alias = kwargs.get('alias')
        dl_file = self.store.get(alias).sftp_download(host, port, usr, pwd, remote, local)
        self.store.remove(alias=kwargs.get('alias'))
        return dl_file

    def download_latest_file(self, host, port, usr, pwd, remote, local=None, **kwargs):
        """sftp download file
        :param host: such as '192.168.255.1'
        :param port: such as 22
        :param usr: username such as 'admin'
        :param pwd: password such as 'admin'
        :param remote: path in host such as '/tmp/'
        :param local: file path to save in local such as 'example/config1/rat1.xml','example/config1/', 'rat1.xml', None
        :param filter in **kwargs: such as: filter = PM.*.xml
        """
        self.store.add(self.sftp_handler, alias=kwargs.get('alias'))
        alias = kwargs.get('alias')
        self.store.get(alias).sftp_download_latest_file(host, port, usr, pwd, remote, local, filter=kwargs.get('filter'))
        self.store.remove(alias=kwargs.get('alias'))

    def sftp_upload(self, host, port, usr, pwd, local, remote=None, **kwargs):
        """sftp upload file
        :param host: such as '192.168.255.1'
        :param port: such as 22
        :param usr: username such as 'admin'
        :param pwd: password such as 'admin'
        :param local: file in local such as '/tmp/rat_psconfig.xml'
        :param remote: file path to save in host such as '/tmp/tmp1/rat_psconfig_test1.xml', '/tmp/tmp1/', 'rat_psconfig_test1.xml', None
        """
        self.store.add(self.sftp_handler, alias=kwargs.get('alias'))
        alias = kwargs.get('alias')
        self.store.get(alias).sftp_upload(host, port, usr, pwd, local, remote)
        self.store.remove(alias=kwargs.get('alias'))


class OperateCsv(object):
    """for csv file
    """

    def __init__(self):
        self.store = Store()

    def read_csv_columns(self, source_file, *cared_title, **kwargs):
        """read_csv_columns to read csv specific one or more columns.

        +--------------------+------+------------------------------------+
        | Input Paramaters   | Man. | Description                        |
        +--------------------+------+------------------------------------+
        | source_file        | yes  | Path of csv file                   |
        +--------------------+------+------------------------------------+
        | cared_title        | yes  | one or more cared column's title   |
        +--------------------+------+------------------------------------+
        | return             | [colA_list] or [[colA_list], [colB_list]] |
        +--------------------+------+------------------------------------+

        Example:

        +------------------+--------------+-------------+------------+
        | read_csv_columns | /opt/xxx.csv | Time        |            |
        +------------------+--------------+-------------+------------+
        | read_csv_columns | /opt/xxx.csv | Time        | SFN        |
        +------------------+--------------+-------------+------------+

        """

        result = []
        csv_obj = CsvHandler(source_file, cared_title[0])
        self.store.add(csv_obj, alias=kwargs.get('alias'))
        result = csv_obj.get_csv_columns_list(*cared_title)
        self.store.remove(alias=kwargs.get('alias'))
        return result


class OperateBin(object):
    """for bin file
    """

    def __init__(self):
        self.store = Store()
        self.file_object = ''
        self.bin_handler = BinHandler(self.file_object)

    def read_bin_file(self, bin_file, tag_name, **kwargs):
        """read_bin_file to read bin file's text by tag name.
          <SwVersion>5912129</SwVersion>
          tag_name: SwVersion
          text: 5912129

        +--------------------+------+-------------------------------+
        | Input Paramaters   | Man. | Description                   |
        +--------------------+------+-------------------------------+
        | bin_file           | yes  | Path of bin file              |
        +--------------------+------+-------------------------------+
        | tag_name           | yes  | tag name in bin file <xxx>    |
        +--------------------+------+-------------------------------+
        | return             | tag name's text                      |
        +--------------------+--------------------------------------+

        Example:

        +----------+---------------+--------------+------------+
        | ${value} | read_bin_file | /opt/xxx.bin | SwVersion  |
        +----------+---------------+--------------+------------+

        """
        with open(bin_file, 'r+b') as self.file_object:
            self.bin_handler = BinHandler(self.file_object)
            self.store.add(self.bin_handler, alias=kwargs.get('alias'))
            try:
                value = self.bin_handler.find_tag_position(tag_name)
            except TAFileException:
                err_info = 'NOT FOUND'
                return err_info
            self.store.remove(alias=kwargs.get('alias'))
            return value[0][1].decode('utf-8')

    def modify_bin_file(self, bin_file, tag_name, new_value, **kwargs):
        """replace_text_in_bin_file to modify bin file's text by tag name,
           the new value should have the same length with old one.
           <SwVersion>5912129</SwVersion>
           tag_name: SwVersion
           text: 5912129

        +--------------------+------+------------------------------------------------+
        | Input Paramaters   | Man. | Description                                    |
        +--------------------+------+------------------------------------------------+
        | bin_file           | yes  | Path of bin file                               |
        +--------------------+------+------------------------------------------------+
        | tag_name           | yes  | Tag name in bin file <xxx>                     |
        +--------------------+------+------------------------------------------------+
        | new_value          | yes  | New value should have same length with old one |
        +--------------------+------+------------------------------------------------+

        Example:

        +---------------------------------+--------------+-----------+---------+
        | modify_bin_file                 | /opt/xxx.bin | SwVersion | 5912128 |
        +---------------------------------+--------------+-----------+---------+

        """
        with open(bin_file, 'r+b') as self.file_object:
            self.bin_handler = BinHandler(self.file_object)
            self.store.add(self.bin_handler, alias=kwargs.get('alias'))
            try:
                self.bin_handler.replace_text_in_bin_file(tag_name, new_value)
            except TAFileException:
                err_info = 'Fail to modify'
                return err_info
            self.store.remove(alias=kwargs.get('alias'))


class OperateXls(object):
    """for excel file
    """

    def __init__(self):
        self.store = Store()
        self._log = logging.getLogger(__name__)
        self._log.setLevel(logging.DEBUG)

    def read_excel_cell(self, source_file, sheet_name, x_cell, y_cell, **kwargs):
        """read_excel_cell to read excel specific cell.

        +--------------------+------+-------------------------------------------+
        | Input Paramaters   | Man. | Description                               |
        +--------------------+------+-------------------------------------------+
        | source_file        | yes  | Absolute path of excel file               |
        +--------------------+------+-------------------------------------------+
        | sheet_name         | yes  | sheet name in excel file                  |
        +--------------------+------+-------------------------------------------+
        | x_cell             | yes  | the number of row(start value is zero)    |
        +--------------------+------+-------------------------------------------+
        | y_cell             | yes  | the number of column(start value is zero) |
        +--------------------+------+-------------------------------------------+

        excel demo:

        +----+------+------+------+-----+
        |0   |A     |B     |C     |D    |
        +----+------+------+------+-----+
        |1   |0,0   |0,1   |0,2   |0,3  |
        +----+------+------+------+-----+
        |2   |1,0   |1,1   |1,2   |1,3  |
        +----+------+------+------+-----+
        |3   |2,0   |2,1   |2,2   |2,3  |
        +----+------+------+------+-----+
        |4   |3,0   |3,1   |3,2   |3,3  |
        +----+------+------+------+-----+

        Example:

        +--------------------+--------------+---------+----+----+
        |read_excel_cell     |/opt/xxx.xls  |Sheet1   |1   |2   |
        +--------------------+--------------+---------+----+----+

        """
        xls = XlsHandler(source_file, sheet_name)
        self.store.add(xls, alias=kwargs.get('alias'))
        xls.open_excel()
        content = xls.read_cell(x_cell, y_cell)
        self.store.remove(alias=kwargs.get('alias'))
        return content

    def modify_excel_cell(self, source_file, sheet_name, x_cell, y_cell, in_value, **kwargs):
        """write_excel_cell to write or modify excel specific cell.
           make sure the excel file is closed when you use this keyword.

        +--------------------+------+-------------------------------------------+
        | Input Paramaters   | Man. | Description                               |
        +--------------------+------+-------------------------------------------+
        | source_file        | yes  | Absolute path of excel file               |
        +--------------------+------+-------------------------------------------+
        | sheet_name         | yes  | sheet name in excel file                  |
        +--------------------+------+-------------------------------------------+
        | x_cell             | yes  | the number of row(start value is zero)    |
        +--------------------+------+-------------------------------------------+
        | y_cell             | yes  | the number of column(start value is zero) |
        +--------------------+------+-------------------------------------------+
        | in_value           | yes  | new value need to write or modify         |
        +--------------------+------+-------------------------------------------+

        excel demo:

        +----+------+------+------+-----+
        |0   |A     |B     |C     |D    |
        +----+------+------+------+-----+
        |1   |0,0   |0,1   |0,2   |0,3  |
        +----+------+------+------+-----+
        |2   |1,0   |1,1   |1,2   |1,3  |
        +----+------+------+------+-----+
        |3   |2,0   |2,1   |2,2   |2,3  |
        +----+------+------+------+-----+
        |4   |3,0   |3,1   |3,2   |3,3  |
        +----+------+------+------+-----+

        Example:

        +--------------------+--------------+--------+---+---+-----+
        |modify_excel_cell   |/opt/xxx.xls  |Sheet1  |1  |2  |333  |
        +--------------------+--------------+--------+---+---+-----+

        """
        xls = XlsHandler(source_file, sheet_name)
        self.store.add(xls, alias=kwargs.get('alias'))
        # file operation, if exist, copy and modify, if not create one
        if os.path.isfile(source_file):
            xls.open_excel()
        else:
            xls.create_excel()

        # sheet operation, if exist, get index, if not create one
        xls.get_sheet_index(sheet_name)

        # cell operation
        xls.write_cell(x_cell, y_cell, in_value)

        # modification save
        xls.save()
        self.store.remove(alias=kwargs.get('alias'))


class UnzipFile(object):
    """for unzip .zip file
    """
    def __init__(self):
        self.store = Store()
        self._log = logging.getLogger(__name__)
        self._log.setLevel(logging.DEBUG)

    def unzip_file(self, source_file, to_path=None, **kwargs):
        """
        Uncompress '.gz','.tar','.tar.bz2','.tar.gz','.tgz','.tz2','.docx','.egg','.jar','.odg','.odp','.ods','.xlsx','.odt','.pptx','.zip' file
        +------------------+------+--------------------------------+
        | Input Parameters | Man. | Description                    |
        +------------------+------+--------------------------------+
        | source_file      | yes  | Path of compressed file        |
        +------------------+------+--------------------------------+
        | to_path          | no   | Path to save uncompressed file |
        +------------------+------+--------------------------------+

        Example:

        +------------------+------------------------------------------------+----------------------------------+
        | unzip_file       | /home/ute/ta_kiss_files/example/snapshot.zip   | /home/ute/ta_kiss_files/example  |
        +------------------+------------------------------------------------+----------------------------------+

        The uncompressed files is saved to /home/ute/ta_kiss_files/example/snapshot/...

        """
        if source_file.endswith(('.tar.gz', '.tar.bz2')):
            source_file_name = os.path.splitext(os.path.splitext(source_file)[0])[0]
        else:
            source_file_name = os.path.splitext(source_file)[0]

        if to_path is None:
            to_path = source_file_name
        else:
            to_path = os.path.join(to_path, os.path.basename(source_file_name))

        if os.path.isdir(to_path):
            shutil.rmtree(to_path)
        unzip_handler = ArchiveFile()
        self.store.add(unzip_handler, alias=kwargs.get('alias'))
        unzip_handler.deep_unzip_file(source_file, to_path)
        self.store.remove(alias=kwargs.get('alias'))


class FilesOperationLibrary(OperateXml, OperateTxt, FtpUploadDownload, OperateCsv, OperateBin, OperateXls, UnzipFile, OperateLog):
    """handle xml/tst/ftp/sftp/csv/bin/excel/unzip/split_log
    """
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self):
        self._log = logging.getLogger(__name__)
        self._log.setLevel(logging.DEBUG)
        OperateXml.__init__(self)
        OperateTxt.__init__(self)
        OperateCsv.__init__(self)
        OperateBin.__init__(self)
        OperateXls.__init__(self)
        FtpUploadDownload.__init__(self)
        UnzipFile.__init__(self)
        OperateLog.__init__(self)
