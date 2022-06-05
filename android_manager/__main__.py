import os
import platform
from caller import run, absolute_path


def run_windows():
    def extra_func():
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            "AndroidPhoneManager")
    ADB_PATH = os.path.join(
        absolute_path,
        "dependencies",
        "Windows",
        "adb.exe")
    AAPT_PATH = os.path.join(
        absolute_path,
        "dependencies",
        "Windows",
        "aapt.exe")
    run(ADB_PATH, AAPT_PATH, extra_func)


def run_linux():
    ADB_PATH = os.path.join(absolute_path, "dependencies", "Linux", "adb")
    AAPT_PATH = os.path.join(absolute_path, "dependencies", "Linux", "aapt")
    run(ADB_PATH, AAPT_PATH)


def run_darwin():
    ADB_PATH = os.path.join(absolute_path, "dependencies", "macOS", "adb")
    AAPT_PATH = os.path.join(absolute_path, "dependencies", "macOS", "aapt")
    run(ADB_PATH, AAPT_PATH)


if "Windows" == platform.system():
    run_windows()
elif "Linux" == platform.system():
    run_linux()
else:
    run_darwin()
