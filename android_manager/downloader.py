import os
import tempfile
import zipfile

import requests

from caller import absolute_path

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33"
}
WINDOWS_ADB_URL = "https://dl.google.com/android/repository/platform-tools-latest-windows.zip"
WINDOWS_AAPT_URL = "https://dl.androidaapt.com/aapt-windows.zip"
LINUX_ADB_URL = "https://dl.google.com/android/repository/platform-tools-latest-linux.zip"
LINUX_AAPT_URL = "https://dl.androidaapt.com/aapt-linux.zip"
MACOS_ADB_URL = "https://dl.google.com/android/repository/platform-tools-latest-darwin.zip"
MACOS_AAPT_URL = "https://dl.androidaapt.com/aapt-macos.zip"


def download_tools(adb_url, aapt_url, system):
    print(f"Downloading {system} ADB Tools ......")
    with open(os.path.join(tempfile.gettempdir(), "temp.zip"), "wb") as f:
        f.write(requests.get(adb_url, headers=headers).content)
    with zipfile.ZipFile(os.path.join(tempfile.gettempdir(), "temp.zip")) as f:
        print("Extracting ......")
        f.extractall(os.path.join(absolute_path, "dependencies"))
        os.rename(
            os.path.join(
                absolute_path,
                "dependencies",
                "platform-tools"),
            os.path.join(
                absolute_path,
                "dependencies",
                system))
    print("Done!")
    print(f"Downloading {system} AAPT Tools ......")
    with open(os.path.join(tempfile.gettempdir(), "temp.zip"), "wb") as f:
        f.write(requests.get(aapt_url, headers=headers).content)
    with zipfile.ZipFile(os.path.join(tempfile.gettempdir(), "temp.zip")) as f:
        print("Extracting ......")
        f.extractall(os.path.join(absolute_path, "dependencies", system))
    print("Done!")


def download_windows():
    download_tools(WINDOWS_ADB_URL, WINDOWS_AAPT_URL, "Windows")


def download_linux():
    download_tools(LINUX_ADB_URL, LINUX_AAPT_URL, "Linux")


def download_darwin():
    download_tools(MACOS_ADB_URL, MACOS_AAPT_URL, "macOS")
