import os
from config import version


def execute(command):
    os.popen(command)


execute("rd /S /Q dist")
execute("rd /S /Q build")
execute("rd /S /Q android_manager.egg-info")
execute("python setup.py bdist_wheel")
execute("python setup.py sdist")
execute("twine upload dist/*")
execute("git add .")
execute(f"git commit -am \"Version {version} Release.\"")
execute("git push origin master")
