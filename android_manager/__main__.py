import platform

from android_manager.caller import run
from android_manager.downloader import *


def run_windows():
    def extra_func():
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            "AndroidPhoneManager")

    adb_path = os.path.join(
        absolute_path,
        "dependencies",
        "Windows",
        "adb.exe")
    aapt_path = os.path.join(
        absolute_path,
        "dependencies",
        "Windows",
        "aapt.exe")
    fastboot_path = os.path.join(
        absolute_path,
        "dependencies",
        "Windows",
        "fastboot.exe"
    )
    run(adb_path, aapt_path, fastboot_path, extra_func)


def run_linux():
    adb_path = os.path.join(absolute_path, "dependencies", "Linux", "adb")
    aapt_path = os.path.join(absolute_path, "dependencies", "Linux", "aapt")
    fastboot_path = os.path.join(absolute_path, "dependencies", "Linux", "fastboot")

    run(adb_path, aapt_path, fastboot_path)


def run_darwin():
    adb_path = os.path.join(absolute_path, "dependencies", "macOS", "adb")
    aapt_path = os.path.join(absolute_path, "dependencies", "macOS", "aapt")
    fastboot_path = os.path.join(absolute_path, "dependencies", "macOS", "fastboot")
    run(adb_path, aapt_path, fastboot_path)


def main():
    if "Windows" == platform.system():
        if not os.path.exists(os.path.join(absolute_path, "dependencies", "Windows")):
            download_windows()
        run_windows()
    elif "Linux" == platform.system():
        if not os.path.exists(os.path.join(absolute_path, "dependencies", "Linux")):
            download_linux()
        run_linux()
    else:
        if not os.path.exists(os.path.join(absolute_path, "dependencies", "macOS")):
            download_darwin()
        run_darwin()


if __name__ == "__main__":
    main()
