import os
import pkgutil
import uuid

win_mode = True
data_folder_name = "pcm-data"

# Thanks
# https://stackoverflow.com/a/30924555/8062151

CSIDL_PERSONAL = 5 # My Docments
SHGFP_TYPE_CURRENT = 0

try:
    import ctypes.wintypes
except ModuleNotFoundError:
    win_mode = False
    data_folder_name = "." + data_folder_name

def get_documents_folder():
    if win_mode:
        buf = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
        ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_PERSONAL, None, SHGFP_TYPE_CURRENT, buf)
        return buf.value
    else:
        return os.path.expanduser("~")

def get_app_data_folder():
    base = ""
    if win_mode:
        base = os.getenv("APPDATA")
    else:
        base = os.path.expanduser("~")
    return os.path.join(base, data_folder_name)

def data_folder(func):
    path = func()
    ensure_folder(path)
    return path

def ensure_folder(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)

def get_py_module_names(package):
    pkgpath = os.path.dirname(package.__file__)
    module_names = [name for _, name, _ in pkgutil.iter_modules([pkgpath])]
    return module_names

def get_id():
    return str(uuid.uuid4())