import os
import platform
import shutil
from setuptools import setup, find_packages

VERSION = "1.0"
files = []
for a, b, c in os.walk('android_manager'):
    t = []
    for i in c:
        t.append(os.path.join(a, i))
    files.append((a, t))
# 移除构建的build文件夹
CUR_PATH = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(CUR_PATH, "build")
if os.path.isdir(path):
    print("del dir ", path)
    shutil.rmtree(path)


if not "Windows" in platform.platform():
    raise RuntimeError("This package only support Windows.")

with open("requirements.txt", "r", encoding="utf-8") as f:
    requires = f.read()
    requires = requires.split("\n")

setup(
    name="android-manager",
    author_email="admin@wufan.fun",
    author="Fan Wu",
    description="Python Android Manager",
    keywords="Android Manager by Python",
    url="https://wufan.fun/",
    project_urls={
        "Source Code": "https://github.com/WindowsRegedit/PythonAndroidPhoneManager",
    },
    version=VERSION,
    package_dir={"": "."},
    entry_points={
        "console_scripts": [
            "android-manager = android_manager.__main__:main",
        ]
    },
    include_package_data=True,
    install_requires=requires,
    tests_require=[
        'pytest>=3.3.1',
        'pytest-cov>=2.5.1',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Customer Service',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Debuggers',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    long_description=open("README.rst", encoding="utf-8").read(),
    packages=find_packages(),
    data_files=files,
)
