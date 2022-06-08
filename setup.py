import os
import shutil
from setuptools import setup, find_packages

__version__ = "3.3"
# Thanks to
# https://stackoverflow.com/questions/72513435/how-can-i-create-my-setup-py-with-non-python-files-and-no-python-files-folders
CUR_PATH = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(CUR_PATH, "build")
if os.path.isdir(path):
    print("del dir ", path)
    shutil.rmtree(path)

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
            "android-manager = android_manager.__main__:main"
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
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    package_data={'android_manager': ['dependencies/*', 'translations/*']},
)
