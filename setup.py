import os
import shutil
from setuptools import setup, find_packages


__version__ = "3.0"
# 移除构建的build文件夹
CUR_PATH = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(CUR_PATH, "build")
if os.path.isdir(path):
    print("del dir ", path)
    shutil.rmtree(path)


def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths


extra_files = package_files('android_manager')

with open("requirements.txt", "r", encoding="utf-8") as f:
    requires = f.read()
    requires = requires.split("\n")

setup(
    name="android-manager",
    author_email="admin@wufan.fun",
    author="Fan Wu",
    description="Python Android Manager",
    keywords="GUI Android",
    url="https://wufan.fun/",
    project_urls={
        "Source Code": "https://github.com/WindowsRegedit/PythonAndroidPhoneManager",
    },
    version=__version__,
    package_dir={"": "."},
    entry_points={
        "console_scripts": [
            "android-manager = android_manager.main:main"
        ]
    },
    install_requires=requires,
    tests_require=[
        'pytest>=3.3.1',
        'pytest-cov>=2.5.1',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        # 'Programming Language :: Python :: 3.10',
        # 'Programming Language :: Python :: 3.11',
    ],
    # long_description=open("README.rst", encoding="utf-8").read(),
    packages=find_packages()
)
