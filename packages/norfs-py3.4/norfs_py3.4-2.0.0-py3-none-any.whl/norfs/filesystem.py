
'\n:class:`norfs.filesystem.BaseFileSystemObject` represents any object in the filesystem. It is the most abstract\nrepresentation.\n\nA :class:`norfs.filesystem.BaseFileSystemObject` exposes the following interface:\n'
from norfs.fs.base import BaseFileSystem, DirListResult, FileSystemOperationError, NotAFileError, Path
from norfs.copy.base import CopyDirectory, CopyFile, CopyFileSystemObject

class BaseFileSystemObject():

    def __init__(self, filesystem, path_str, *, _path=None):
        ' Constructor for BaseFileSystemObjects.\n        One of `path_str` and `_path` **MUST** be present.\n        '
        self._fs = filesystem
        self._path = (_path or self._fs.parse_path((path_str or '')))

    @property
    def path(self):
        ' The full, absolute, path of self in the file system. '
        return self._fs.path_to_string(self._path)

    @property
    def uri(self):
        ' The URI that points to self in the file system. '
        return self._fs.path_to_uri(self._path)

    @property
    def name(self):
        ' The name of self. '
        return self._path.basename

    def is_file(self):
        ' Returns whether self is a File. '
        return False

    def is_dir(self):
        ' Returns whether self is a Directory. '
        return False

    def as_file(self):
        ' Returns itself as a :class:`norfs.filesystem.File` instance or raises a\n        :class:`norfs.fs.base.NotAFileError`.\n        '
        raise NotAFileError()

    def as_dir(self):
        ' Returns itself as a Directory instance or raises a :class:`NotADirectoryError`. '
        raise NotADirectoryError()

    def exists(self):
        ' Returns whether self exists in the file system. '
        return self._fs.path_exists(self._path)

    def remove(self):
        ' Tries to remove self from the file system.\n        On failure it raises a :class:`norfs.fs.base.FileSystemOperationError`\n        '
        raise FileSystemOperationError('Cannot remove {0}'.format(str(self)))

    def parent(self):
        ' Return parent :class:`norfs.filesystem.Directory` of self. '
        return Directory(self._fs, None, _path=self._path.parent)

    def copy_object(self):
        return CopyFileSystemObject(self._fs, self._path)

    def __repr__(self):
        return '{0}(fs={1}, path={2})'.format(self.__class__.__name__, self._fs, self.path)

    def __hash__(self):
        return hash(self.__repr__())

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            other_casted = other
            return ((self._path == other_casted._path) and (self._fs == other_casted._fs))
        return False

class Directory(BaseFileSystemObject):

    def is_dir(self):
        ' Returns whether self is a :class:`norfs.filesystem.Directory`. '
        return True

    def as_dir(self):
        ' Returns itself as a :class:`norfs.filesystem.Directory` instance or raises a :class:`NotADirectoryError`.\n        '
        return self

    def list(self):
        ' Returns the contents of the :class:`norfs.filesystem.Directory` in the file system as a list of\n        :class:`norfs.filesystem.BaseFileSystemObject` s.\n\n        If the :class:`norfs.filesystem.Directory` does not exist the list will be empty.\n        '
        contents = self._fs.dir_list(self._path)
        result = []
        for dir_path in contents.dirs:
            result.append(Directory(self._fs, None, _path=dir_path))
        for file_path in contents.files:
            result.append(File(self._fs, None, _path=file_path))
        for other_path in contents.others:
            result.append(BaseFileSystemObject(self._fs, None, _path=other_path))
        return result

    def remove(self):
        ' Tries to remove self from the file system.\n\n        On failure it raises a :class:`norfs.fs.base.FileSystemOperationError`\n        '
        self._fs.dir_remove(self._path)

    def subdir(self, path):
        ' Returns a :class:`norfs.filesystem.Directory` with its path as being the given path relative to the current\n        directory.\n        '
        return Directory(self._fs, None, _path=self._path.child(path))

    def file(self, path):
        ' Returns a :class:`norfs.filesystem.File` with its path as being the given `path` relative to the current\n        directory.\n        '
        return File(self._fs, None, _path=self._path.child(path))

    def copy_object(self):
        return CopyDirectory(self._fs, self._path)

class File(BaseFileSystemObject):

    def is_file(self):
        ' Returns whether self is a :class:`norfs.filesystem.File`. '
        return True

    def as_file(self):
        ' Returns itself as a :class:`norfs.filesystem.File` instance or raises a :class:`norfs.fs.base.NotAFileError`.\n        '
        return self

    def remove(self):
        ' Tries to remove self from the file system.\n\n        On failure it raises a :class:`norfs.fs.base.FileSystemOperationError`\n        '
        self._fs.file_remove(self._path)

    def read(self):
        ' Returns the contents of the file.\n\n        If it fails to read the file a :class:`norfs.fs.base.FileSystemOperationError` will be raised.\n        '
        return self._fs.file_read(self._path)

    def write(self, content):
        ' Sets the contents of the file. If the parent directory does not exist it is created.\n\n        If it fails to write the file a :class:`norfs.fs.base.FileSystemOperationError` will be raised.\n        '
        self._fs.file_write(self._path, content)

    def copy_object(self):
        return CopyFile(self._fs, self._path)
