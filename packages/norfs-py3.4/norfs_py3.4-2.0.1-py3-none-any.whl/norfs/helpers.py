
'\nThe :mod:`norfs.helpers` offers functions that serve as shortcuts for common operations with the library.\n\nThe :mod:`norfs.helpers` contains the following functions:\n'
import norfs.copy.base
import norfs.copy.local
import norfs.copy.s3
import norfs.client
import norfs.fs.local
import norfs.fs.memory
import norfs.fs.s3

def get_copy_client(*args):
    " Helper function to get a :class:`norfs.copy.base.CopyClient` instance configured with copy strategies for the\n    given file systems.\n    This function only sets the built-in :class:`norfs.copy.base.CopyStrategy` s for the built-in file systems, all\n    other will be ignored.\n    For example::\n\n        # Given\n        s3_boto_1 = boto3.client('s3')\n        s3_boto_2 = boto3.client('s3', endpoint_url='http://my.s3.endpoint')\n        local = norfs.helpers.local()\n        s3_1 = norfs.helpers.s3(s3_boto_1)\n        s3_2 = norfs.helpers.s3(s3_boto_2)\n        memory = norfs.helpers.memory()\n\n        # Doing\n        cp = get_copy_client(local, s3_1, s3_2, memory)\n\n        # Is equivalent to\n        copier = norfs.copy.base.Copier(norfs.copy.base.GenericCopyStrategy())\n        copier.set_copy_policy(local.fs, local.fs, norfs.copy.local.LocalToLocalCopyStrategy())\n        copier.set_copy_policy(local.fs, s3_1.fs, norfs.copy.local.LocalToS3CopyStrategy(s3_boto_1))\n        copier.set_copy_policy(local.fs, s3_2.fs, norfs.copy.local.LocalToS3CopyStrategy(s3_boto_2))\n        copier.set_copy_policy(s3_1.fs, local.fs, norfs.copy.s3.S3ToLocalCopyStrategy())\n        copier.set_copy_policy(s3_1.fs, s3_1.fs, norfs.copy.s3.S3ToS3CopyStrategy(s3_boto_1))\n        copier.set_copy_policy(s3_2.fs, local.fs, norfs.copy.s3.S3ToLocalCopyStrategy())\n        copier.set_copy_policy(s3_2.fs, s3_2.fs, norfs.copy.s3.S3ToS3CopyStrategy(s3_boto_2))\n        cp = norfs.client.CopyClient(copier)\n    "
    copier = norfs.copy.base.Copier(norfs.copy.base.GenericCopyStrategy())
    for src in args:
        src_type = type(src.fs)
        for dst in args:
            dst_type = type(dst.fs)
            if (src_type is norfs.fs.local.LocalFileSystem):
                if (dst_type is norfs.fs.local.LocalFileSystem):
                    copy_strategy = norfs.copy.local.LocalToLocalCopyStrategy()
                elif (dst_type is norfs.fs.s3.S3FileSystem):
                    copy_strategy = norfs.copy.local.LocalToS3CopyStrategy(dst.fs._s3_client)
                else:
                    continue
            elif (src_type is norfs.fs.s3.S3FileSystem):
                if (dst_type is norfs.fs.local.LocalFileSystem):
                    copy_strategy = norfs.copy.s3.S3ToLocalCopyStrategy(src.fs._s3_client)
                elif (dst_type is norfs.fs.s3.S3FileSystem):
                    src_s3_client = src.fs._s3_client
                    dst_s3_client = dst.fs._s3_client
                    if (src_s3_client is dst_s3_client):
                        copy_strategy = norfs.copy.s3.S3ToS3CopyStrategy(src_s3_client)
                    else:
                        continue
                else:
                    continue
            else:
                continue
            copier.set_copy_policy(src.fs, dst.fs, copy_strategy)
    return norfs.client.CopyClient(copier)

def local():
    ' Returns a new :class:`norfs.client.FileSystemClient` managing a new instance of\n    :class:`norfs.fs.local.LocalFileSystem`.\n    '
    return norfs.client.FileSystemClient(norfs.fs.local.LocalFileSystem())

def memory(**kwargs):
    ' Returns a new :class:`norfs.client.FileSystemClient` managing a new instance of\n    :class:`norfs.fs.memory.MemoryFileSystem`.\n\n    ``kwargs`` is passed directly to the file system constructor.\n    '
    return norfs.client.FileSystemClient(norfs.fs.memory.MemoryFileSystem(norfs.fs.memory.MemoryDirectory(), **kwargs))

def s3(*args, **kwargs):
    ' Returns a new :class:`norfs.client.FileSystemClient` managing a new instance of\n    :class:`norfs.fs.s3.S3FileSystem`.\n\n    ``args`` and ``kwargs`` are passed directly to the file system constructor.\n    '
    return norfs.client.FileSystemClient(norfs.fs.s3.S3FileSystem(*args, **kwargs))
