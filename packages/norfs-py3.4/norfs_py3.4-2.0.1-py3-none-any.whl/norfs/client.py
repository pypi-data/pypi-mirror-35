
from norfs.filesystem import BaseFileSystemObject, Directory, File
from norfs.fs.base import BaseFileSystem
from norfs.copy.base import Copier

class FileSystemClient():
    "\n    :class:`norfs.client.FileSystemClient` provides a way to access the file system objects of a given file system. It\n    is a handy class that provides easy access to \x16:class:`norfs.filesystem.File` and\n    :class:`norfs.filesystem.Directory` instances. It is usually obtained using :mod:`norfs.helpers`::\n\n        import norfs.helpers\n\n        local_fs_client = norfs.helpers.local()\n\n        memory_fs_client = norfs.helpers.memory()\n\n        import boto3\n        s3_fs_client = norfs.helpers.s3(s3_client=boto3.client('s3'))\n\n    A :class:`norfs.client.FileSystemClient` exposes the following interface:\n    "

    def __init__(self, fs):
        ' Constructor for :class:`norfs.client.FileSystemClient` s. '
        self._fs = fs

    @property
    def fs(self):
        ' The :class:`norfs.filesystem.BaseFileSystemObject` the client is managing. '
        return self._fs

    def dir(self, path):
        ' Returns a :class:`norfs.filesystem.Directory` instance for the given path in the managed file system. '
        return Directory(self.fs, path)

    def file(self, path):
        ' Returns a :class:`norfs.filesystem.File` instance for the given path in the managed file system. '
        return File(self.fs, path)

class CopyClient():
    "\n    :class:`norfs.client.CopyClient` provides a unified simple copy API for any :class:`norfs.filesystem.File` or\n    :class:`norfs.filesystem.Directory` from any file system.  It is usually accessed by using\n    :func:`norfs.helpers.get_copy_client`::\n\n        import norfs.helpers\n\n        local = norfs.helpers.local() cp_local_only = norfs.helpers.get_copy_client(local)\n\n        cp_local_only.copy(local.file('source_file.txt'), local.file('target_file.txt'))\n\n\n        memory = norfs.helpers.memory()\n\n        import boto3 s3 = norfs.helpers.s3(s3_client=boto3.client('s3'))\n\n        cp_for_all = norfs.helpers.get_copy_client(local, s3, memory)\n\n        cp_for_all.copy(s3.file('myBucket/source_file.txt'), local.file('target_file.txt'))\n\n    :func:`norfs.helpers.get_copy_client` returns a :class:`norfs.client.CopyClient` instance configured with copy\n    strategies for each of the file system clients passed.\n\n    A :class:`norfs.copy.base.Copier` can have copy policies set for a pair of source and destination file systems to\n    implement a better strategy of copying between them than read source and write destination.\n    :func:`norfs.helpers.get_copy_client` helps you by setting these for you.\n\n    A :class:`norfs.client.CopyClient` exposes the following interface:\n    "

    def __init__(self, copier):
        ' Constructor for CopyClients. '
        self._copier = copier

    @property
    def copier(self):
        ' The :class:`norfs.copy.base.Copier` instance managed by the client. '
        return self._copier

    def copy(self, src, dst):
        ' Copies ``src`` to ``dst``, no mater the file systems they are on. ``src`` and ``dst`` can by both\n        :class:`norfs.filesystem.File` or :class:`norfs.filesystem.Directory`.  The only operation not supported is\n        copying from a :class:`norfs.filesystem.Directory` into a :class:`norfs.filesystem.File` as it does not make\n        sense.\n\n        If source is a :class:`norfs.filesystem.Directory` and destination is a :class:`norfs.filesystem.File` it raises\n        a :class:`TypeError`.\n\n        On copy failure it raises a :class:`norfs.fs.base.FileSystemOperationError`.\n        '
        self._copier.copy(src.copy_object(), dst.copy_object())
