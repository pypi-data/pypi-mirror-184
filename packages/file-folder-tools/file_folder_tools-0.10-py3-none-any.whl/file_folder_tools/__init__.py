import tempfile
from flexible_partial import FlexiblePartialOwnName
from tempfile import SpooledTemporaryFile
from list_all_files_recursively import get_folder_file_complete_path
import pickle
import shutil
import sys
from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend as crypto_default_backend
import xxhash
from touchtouch import touch
import os
import ctypes
import msvcrt
import subprocess
from ctypes import wintypes
import stat


def rm_dir(path, dryrun=True):
    if not os.path.exists(os.path.join(path)):
        return False
    allfolders = {}
    for file in get_folder_file_complete_path(path):
        print(f"Deleting file: {file.path} ", end="\r")
        allfolders[file.folder] = ""
        try:
            if not dryrun:
                os.remove(file.path)
        except Exception as fe:
            print(fe)
            pass
    try:
        for newp in reversed(sorted(list(allfolders.keys()), key=lambda x: len(x))):
            try:
                print(f"Deleting folder: {newp}", end="\r")
                if not dryrun:
                    shutil.rmtree(newp)
            except Exception as fe:
                print(fe)
                continue

        if not dryrun:
            shutil.rmtree(path)
    except Exception as fa:
        print(fa)

    return True


def tempfolder():
    tempfolder = tempfile.TemporaryDirectory()
    tempfolder.cleanup()
    if not os.path.exists(tempfolder.name):
        os.makedirs(tempfolder.name)

    return tempfolder.name, _get_remove_folder(tempfolder.name)


def tempfolder_and_files(fileprefix="tmp_", numberoffiles=1, suffix=".bin", zfill=8):
    tempfolder = tempfile.TemporaryDirectory()
    tempfolder.cleanup()
    allfiles = []

    for fi in range(numberoffiles):
        tempfile____txtlist = os.path.join(
            tempfolder.name, f"{fileprefix}_{str(fi).zfill(zfill)}{suffix}"
        )
        allfiles.append(tempfile____txtlist)
        touch(tempfile____txtlist)

    return (
        [(k, _get_remove_file(k)) for k in allfiles],
        tempfolder.name.split(os.sep)[-1],
        tempfolder.name,
    )


def _get_remove_folder(folder):
    return FlexiblePartialOwnName(rm_dir, f"rm_dir({repr(folder)})", True, folder)


def _get_remove_file(file):
    return FlexiblePartialOwnName(os.remove, f"os.remove({repr(file)})", True, file)


def get_tmpfile(suffix=".bin"):
    tfp = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
    filename = tfp.name
    filename = os.path.normpath(filename)
    tfp.close()
    touch(filename)
    return filename, _get_remove_file(filename)


def create_spooledtempfile_with_content(content: bytes):
    f = SpooledTemporaryFile()
    f.seek(0)
    f.write(content)
    f.seek(0)
    return f


def create_folder_if_not_there(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


def safeprint(s):
    try:
        print(s)
    except UnicodeEncodeError:
        if sys.version_info >= (3,):
            print(s.encode("utf8").decode(sys.stdout.encoding, "ignore"))
        else:
            print(s.encode("utf8"))


def get_file_hash(filepath):
    with open(filepath, "rb") as f:
        file_hash = xxhash.xxh3_128()
        while chunk := f.read(8192):
            file_hash.update(chunk)
        hexdig = file_hash.hexdigest()
        return hexdig


def get_hash_from_variable(variable):
    file_hash = xxhash.xxh3_128()
    try:
        file_hash.update(variable)
    except Exception:
        file_hash.update(repr(variable))
    hexdig = file_hash.hexdigest()
    return hexdig


def what_is_it(path):
    if os.path.exists(path):
        if os.path.isfile(path):
            return "file"
        if os.path.isdir(path):
            return "dir"
        if os.path.islink(path):
            return "link"
    return None


def generate_ssh_key(file_path, public_exponent=65537, key_size=2048):

    key = rsa.generate_private_key(
        backend=crypto_default_backend(),
        public_exponent=public_exponent,
        key_size=key_size,
    )

    private_key = key.private_bytes(
        crypto_serialization.Encoding.PEM,
        crypto_serialization.PrivateFormat.PKCS8,
        crypto_serialization.NoEncryption(),
    )

    public_key = key.public_key().public_bytes(
        crypto_serialization.Encoding.OpenSSH, crypto_serialization.PublicFormat.OpenSSH
    )
    touch(file_path)
    with open(file_path, mode="wb") as f:
        f.write(b"key: " + private_key + b"\n" + b"public_key: " + public_key)
    return private_key, public_key


def concat_files(filenames, output):
    with open(output, "wb") as wfd:
        for f in filenames:
            with open(f, "rb") as fd:
                shutil.copyfileobj(fd, wfd)


def maximize_console(lines=None):

    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    user32 = ctypes.WinDLL("user32", use_last_error=True)
    SW_MAXIMIZE = 3
    kernel32.GetConsoleWindow.restype = wintypes.HWND
    kernel32.GetLargestConsoleWindowSize.restype = wintypes._COORD
    kernel32.GetLargestConsoleWindowSize.argtypes = (wintypes.HANDLE,)
    user32.ShowWindow.argtypes = (wintypes.HWND, ctypes.c_int)

    fd = os.open("CONOUT$", os.O_RDWR)
    try:
        hCon = msvcrt.get_osfhandle(fd)
        max_size = kernel32.GetLargestConsoleWindowSize(hCon)
        if max_size.X == 0 and max_size.Y == 0:
            raise ctypes.WinError(ctypes.get_last_error())
    finally:
        os.close(fd)
    cols = max_size.X
    hWnd = kernel32.GetConsoleWindow()
    if cols and hWnd:
        if lines is None:
            lines = max_size.Y
        else:
            lines = max(min(lines, 9999), max_size.Y)
        subprocess.check_call("mode.com con cols={} lines={}".format(cols, lines))
        user32.ShowWindow(hWnd, SW_MAXIMIZE)


def enableLUA_disableLUA(enable=True):
    command = ""
    if enable is False:
        command = rf"""reg.exe ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 0 /f"""
    if enable is True:
        command = rf"""reg.exe ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 1 /f"""
    os.system(command)


def is_file_being_used(f):
    if os.path.exists(f):
        try:
            os.rename(f, f)
            return False
        except OSError as e:
            return True
    return None


def read_pkl(filename):
    with open(filename, "rb") as f:
        data_pickle = pickle.load(f)
    return data_pickle


def write_pkl(object_, savepath):
    touch(savepath)
    with open(savepath, "wb") as fa:
        pickle.dump(object_, fa)


def get_absolute_path_from_file(path):
    return os.path.abspath(os.path.expanduser(path))


def update_edit_time_of_file(path):
    os.utime(path, None)


def is_file_read_only(path):
    r"""True - read-only, False -> writable
    is_file_read_only(r"F:\bat.png")"""
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            return False
        else:
            return True
    return None


def get_filesize(path):
    if os.path.exists(path):

        return os.path.getsize(path)
    return None


def set_file_writeable(path):
    return os.chmod(path, stat.S_IWRITE)


def set_file_read_only(path):
    r"""set_file_read_only(path=r"F:\bat.png")"""
    return os.chmod(path, stat.S_IREAD)


def encode_filepath(path):
    return os.fsencode(path)


def decode_filepath(path):
    return os.fsdecode(path)


def stat_S_ISUID_Set_user_ID_on_execution(path):
    os.chmod(path, stat.S_ISUID)


def stat_S_ISGID_Set_group_ID_on_execution(path):
    os.chmod(path, stat.S_ISGID)


def stat_S_ENFMT_Record_locking_enforced(path):
    os.chmod(path, stat.S_ENFMT)


def stat_S_ISVTX_Save_text_image_after_execution(path):
    os.chmod(path, stat.S_ISVTX)


def stat_S_IREAD_Read_by_owner(path):
    os.chmod(path, stat.S_IREAD)


def stat_S_IWRITE_Write_by_owner(path):
    os.chmod(path, stat.S_IWRITE)


def stat_S_IEXEC_Execute_by_owner(path):
    os.chmod(path, stat.S_IEXEC)


def stat_S_IRWXU_Read_write_and_execute_by_owner(path):
    os.chmod(path, stat.S_IRWXU)


def stat_S_IRUSR_Read_by_owner(path):
    os.chmod(path, stat.S_IRUSR)


def stat_S_IWUSR_Write_by_owner(path):
    os.chmod(path, stat.S_IWUSR)


def stat_S_IXUSR_Execute_by_owner(path):
    os.chmod(path, stat.S_IXUSR)


def stat_S_IRWXG_Read_write_and_execute_by_group(path):
    os.chmod(path, stat.S_IRWXG)


def stat_S_IRGRP_Read_by_group(path):
    os.chmod(path, stat.S_IRGRP)


def stat_S_IWGRP_Write_by_group(path):
    os.chmod(path, stat.S_IWGRP)


def stat_S_IXGRP_Execute_by_group(path):
    os.chmod(path, stat.S_IXGRP)


def stat_S_IRWXO_Read_write_and_execute_by_others(path):
    os.chmod(path, stat.S_IRWXO)


def stat_S_IROTH_Read_by_others(path):
    os.chmod(path, stat.S_IROTH)


def stat_S_IWOTH_Write_by_others(path):
    os.chmod(path, stat.S_IWOTH)


def stat_S_IXOTH_Execute_by_others(path):
    os.chmod(path, stat.S_IXOTH)

