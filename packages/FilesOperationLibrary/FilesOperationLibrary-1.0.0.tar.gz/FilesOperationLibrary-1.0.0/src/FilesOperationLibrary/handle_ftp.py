# -*- coding: utf-8 -*-
"""
:created on: 6-09-2017

:copyright: 
:author: leo
:contact: 
"""

import logging
import os
import re
import shutil
import pysftp
import FtpLibrary


class FtpHandler(object):
    """ftp download and upload
    """
    def __init__(self):
        self._log = logging.getLogger(__name__)
        self._log.setLevel(logging.DEBUG)
        self._host = None
        self._port = None

    def connect_ftp(self, host, port, usr, pwd, **kwargs):
        """connect ftp
        """
        self._host = host
        self._port = port
        FtpLibrary.ftp_connect(self._host, usr, pwd, self._port)

    def close_ftp(self, **kwargs):
        """ftp close
        """
        FtpLibrary.ftp_close()

    def ftp_download(self, remote, local, **kwargs):
        """ftp download
        """
        if '*.*' in remote:
            file_list = []
            remote_folder = remote.strip('*.*')
            FtpLibrary.cwd(remote_folder)
            for f in FtpLibrary.dir():
                if not f.startswith('d'):
                    file_list.append(self._ftp_download_one_file(f.split()[-1], '%s/' % local))
            return file_list
        else:
            return self._ftp_download_one_file(remote, local)

    def _ftp_download_one_file(self, remote, local):
        if local is not None and os.path.split(local)[0] != '':
            if os.path.exists(os.path.split(local)[0]) is False:
                os.makedirs(os.path.split(local)[0])
            if os.path.split(local)[1] == '':
                local = local + '/' + os.path.split(remote)[1]
        elif local is not None and os.path.split(local)[0] == '':
            local = os.getcwd() + '/' + local
        else:
            local = os.getcwd() + '/' + os.path.split(remote)[1]
        FtpLibrary.download_file(remote, local)
        return local

    def ftp_upload(self, local, remote, **kwargs):
        """ftp upload
        """
        current_dir = FtpLibrary.pwd()
        if remote is not None and os.path.split(remote)[0] != '':
            try:
                FtpLibrary.cwd(os.path.split(remote)[0])
            except (IOError, OSError):
                FtpLibrary.mkd(os.path.split(remote)[0])
                self._log.info('make dir; %s', os.path.split(remote)[0])
        elif remote is not None and os.path.split(remote)[0] == '':
            remote = current_dir + '/' + remote
        else:
            remote = current_dir

        if os.path.split(remote)[1] == '':
            remote = remote + '/' + os.path.split(local)[1]

        FtpLibrary.cwd(current_dir)
        local = os.path.normpath(local)
        remote = os.path.normpath(remote)
        FtpLibrary.upload_file(local, remote)


class SFtpHandler(object):
    """sftp download and upload
    """
    def __init__(self):
        self._log = logging.getLogger(__name__)
        self._log.setLevel(logging.DEBUG)
        self.sftp = None

    def sftp_download(self, host, port, usr, pwd, remote, local=None, **kwargs):
        """sftp download
        """
        if local is not None and os.path.split(local)[0] != '':
            if os.path.exists(os.path.split(local)[0]) is False:
                os.makedirs(os.path.split(local)[0])
            if os.path.split(local)[1] == '':
                local = local + '/' + os.path.split(remote)[1]
        elif local is not None and os.path.split(local)[0] == '':
            local = os.getcwd() + '/' + local
        else:
            local = os.getcwd() + '/' + os.path.split(remote)[1]

        local = os.path.normpath(local)

        with pysftp.Connection(host, username=usr, password=pwd, port=int(port)) as sftp:
            if os.path.split(remote)[1] != '':
                sftp.get(remote, local)
                ret = local
            else:
                localpath = os.path.join(local, remote.split('/')[-2])
                if os.path.isdir(localpath) is True:
                    shutil.rmtree(localpath)
                sftp.get_r(remote, local)
                ret = None
            sftp.close()
            return ret

    def mtime(self, filename):
        """return the creation time of the file
        """
        return self.sftp.stat(filename).st_mtime

    def sftp_download_latest_file(self, host, port, usr, pwd, remote, local=None, **kwargs):
        """sftp download the latest file with the same file name but different time stamps
        """
        filefilter = kwargs.get('filter')
        with pysftp.Connection(host, username=usr, password=pwd, port=int(port)) as self.sftp:
            try:
                self.sftp.chdir(remote)
                self._log.debug('sftp walking to %s', remote)
            except (IOError, OSError):
                self._log.debug("sftp cd to dir '%s' failed!", remote)

            sftp_curr_dir = self.sftp.getcwd()

            statfiles = list("%s/%s" % (sftp_curr_dir, filename) for filename in self.sftp.listdir(sftp_curr_dir) if re.search(filefilter, filename))
            sorted_statfiles = list(sorted([filename for filename in statfiles], key=self.mtime))
            try:
                target_file = sorted_statfiles[-1]
            except (IndexError, NameError):
                self._log.debug("'%s' not found!", filefilter)

            if local is None:
                local = os.getcwd()
            if '.' not in os.path.basename(local):
                local = os.path.join(local, target_file.split('/')[-1])
            if os.path.exists(os.path.split(local)[0]) is False:
                os.makedirs(os.path.split(local)[0])

            self.sftp.get(target_file, local)
            self.sftp.close()

    def sftp_upload(self, host, port, usr, pwd, local, remote=None, **kwargs):
        """sftp upload
        """
        with pysftp.Connection(host, username=usr, password=pwd, port=int(port)) as sftp:
            current_path = ['', sftp.getcwd()][sftp.getcwd() is not None]
            if remote is not None and os.path.split(remote)[0] != '':
                if sftp.exists(os.path.split(remote)[0]) is not True:
                    sftp.makedirs(os.path.split(remote)[0])
                    self._log.info('make dir; %s', os.path.split(remote)[0])
            elif remote is not None and os.path.split(remote)[0] == '':
                remote = current_path + '/' + remote
            else:
                remote = current_path + '/' + os.path.split(local)[1]

            if remote is not None and os.path.split(remote)[1] == '':
                remote = remote + '/' + os.path.split(local)[1]

            local = os.path.normpath(local)
            remote = os.path.normpath(remote)

            sftp.put(local, remote)
            sftp.close()


if __name__ == '__main__':
    pass
