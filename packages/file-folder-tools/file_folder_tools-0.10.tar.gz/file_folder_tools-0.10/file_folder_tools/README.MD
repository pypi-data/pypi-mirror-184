# Some useful functions for files/folders

```python
# Tested with:
# Python 3.9.13
# Windows 10

pip install file-folder-tools


from file_folder_tools import *

maximize_console(lines=None)


rm_dir(path=r"F:\testdele - Copy", dryrun=True)

safeprint("oioi")

path = r"F:\bat.png"
set_file_read_only(path)
set_file_writeable(path)

stat_S_ENFMT_Record_locking_enforced(path)

stat_S_IEXEC_Execute_by_owner(path)

stat_S_IREAD_Read_by_owner(path)

stat_S_IRGRP_Read_by_group(path)

stat_S_IROTH_Read_by_others(path)

stat_S_IRUSR_Read_by_owner(path)

stat_S_IRWXG_Read_write_and_execute_by_group(path)

stat_S_IRWXO_Read_write_and_execute_by_others(path)

stat_S_IRWXU_Read_write_and_execute_by_owner(path)

stat_S_ISGID_Set_group_ID_on_execution(path)

stat_S_ISUID_Set_user_ID_on_execution(path)

stat_S_ISVTX_Save_text_image_after_execution(path)

stat_S_IWGRP_Write_by_group(path)

stat_S_IWOTH_Write_by_others(path)

stat_S_IWRITE_Write_by_owner(path)

stat_S_IWUSR_Write_by_owner(path)

stat_S_IXGRP_Execute_by_group(path)

stat_S_IXOTH_Execute_by_others(path)

stat_S_IXUSR_Execute_by_owner(path)

tempfolder_string, function_to_remove = tempfolder()

functions_to_remove, files, tempfolder_string_ = tempfolder_and_files(
    fileprefix="tmp_", numberoffiles=10, suffix=".bin", zfill=8
)

update_edit_time_of_file(path)

what_is_it(path)
pklo = read_pkl(filename=r"F:\gutelautschrift.pkl")
write_pkl(object_=pklo, savepath=r"F:\gutelautschrift2.pkl")

concat_files(
    filenames=[r"F:\gutelautschrift.pkl", r"F:\gutelautschrift2.pkl"],
    output="f:\\concatfiles.pkl",
)

create_folder_if_not_there(folder="f:\\testen")

create_spooledtempfile_with_content(content=b"xxxxxx")

decode_filepath(path)

enableLUA_disableLUA(enable=False)

encode_filepath(path)

generate_ssh_key(file_path="f:\\sshtestkey", public_exponent=65537, key_size=2048)

get_absolute_path_from_file(path)

get_file_hash(filepath="appl.py")

get_filesize(path)

get_hash_from_variable(variable="baba")

filestring, removefunction = get_tmpfile(suffix=".bin")

is_file_being_used(path)

is_file_read_only(r"F:\bat.png")



```



