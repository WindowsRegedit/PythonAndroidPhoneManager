import os
import re
import sys
import json
import tempfile
import threading
import subprocess

from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qt_material import apply_stylesheet

absolute_path = os.path.dirname(__file__)

ADB_PATH = ""
AAPT_PATH = ""
FASTBOOT_PATH = ""

translation = {}

with open(os.path.join(absolute_path, "config.json"), "r", encoding="utf-8") as f:
    config = json.load(f)
    lang = config.get("language", "English")
    theme = config.get("theme", "light_teal.xml")
    if lang != "English":
        with open(os.path.join(absolute_path, "translations", lang + ".json"), "r", encoding="utf-8") as f2:
            translation = json.load(f2)
    else:
        translation = {}



def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def get_translation(trans):
    return translation.get(trans, trans)


def execute(command):
    result = subprocess.check_output(command)
    if hasattr(result, "decode"):
        result = result.decode()
    return result


def get_all_devices():
    output = execute([ADB_PATH, "devices"])
    res = re.findall("(.*)\t(.*)", output)
    return res


def get_full_description(device_name):
    output = execute([ADB_PATH, "devices", "-l"])
    try:
        res = re.findall(
            f"{device_name}.*\\s(.*\\S).*\\sproduct:(.*\\S).*\\smodel:(.*\\S)"
            f".*\\sdevice:(.*\\S).*\\stransport_id:(.*\\S)",
            output)[0]
    except IndexError:
        raise

    result = {
        get_translation("Device Status"): get_translation(
            res[0]),
        get_translation("Device Product"): res[1],
        get_translation("Device Model"): res[2],
        get_translation("Transport ID"): res[4],
        get_translation("Screen Resolution"): re.search(
            "Physical size: (.*)",
            execute(
                [
                    ADB_PATH,
                    "-s",
                    device_name,
                    "shell",
                    "wm",
                    "size"])).group(1),
        get_translation("Android-ID"): execute(
                        [
                            ADB_PATH,
                            "-s",
                            device_name,
                            "shell",
                            "settings",
                            "get",
                            "secure",
                            "android_id"]).strip(),
        get_translation("IPv4 Address"): re.search(
                                "inet addr:(.*) Mask:",
                                execute(
                                    [
                                        ADB_PATH,
                                        "shell",
                                        "ifconfig"])).group(1)}

    return result


def run(adb_path, aapt_path, fastboot_path, extra_func=None):
    global ADB_PATH, AAPT_PATH, FASTBOOT_PATH, config, lang
    ADB_PATH = adb_path
    AAPT_PATH = aapt_path
    FASTBOOT_PATH = fastboot_path
    if callable(extra_func):
        extra_func()

    class Tabs(QTabWidget):
        def __init__(self):
            super().__init__()
            self.setWindowTitle(get_translation("Android Phone Manager"))
            self.setWindowIcon(
                QIcon(
                    os.path.join(
                        absolute_path,
                        "dependencies",
                        "favicon.ico")))
            self.common_tab = App()
            self.analyzer_tab = AppAnalyzer()
            self.settings_tab = Settings()
            self.fastboot_tab = FastBoot()
            self.addTab(self.common_tab, get_translation("Common"))
            self.addTab(self.analyzer_tab, get_translation("Analyze APK"))
            self.addTab(
                self.fastboot_tab,
                get_translation("FastBoot(Danger Zone)"))
            self.addTab(self.settings_tab, get_translation("Settings"))
            self.resize(800, 800)

    class FastBoot(QWidget):
        def __init__(self):
            super().__init__()
            self.layout = QGridLayout()
            self.warning = QLabel(get_translation(
                "When You Are Using It, May Be Cause The Device Not Able To Run, Please Use Carefully"), self)
            self.warning.setStyleSheet("color: red")
            self.devices = QTableWidget(self)
            self.devices.setColumnCount(1)
            self.devices.setRowCount(15)
            self.devices.setHorizontalHeaderLabels(
                [get_translation("Device Name")])
            self.devices.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.unlock_phone = QPushButton(
                get_translation("Unlock Phone"), self)
            self.unlock_phone.clicked.connect(self.unlock)
            self.devices.cellPressed.connect(self.getPosContent)
            self.device_name = None
            self.refresh()
            self.refresh_button = QPushButton(get_translation("Refresh"), self)
            self.refresh_button.clicked.connect(self.refresh)
            self.layout.addWidget(self.unlock_phone, 1, 2)
            self.layout.addWidget(self.warning, 0, 0)
            self.layout.addWidget(self.refresh_button, 1, 1)
            self.layout.addWidget(self.devices, 1, 0)
            self.setLayout(self.layout)

        def refresh(self):
            self.devices.clear()
            devices = re.findall("(.*).*\\s+fastboot",
                                 execute([FASTBOOT_PATH, "devices"]))
            for device in range(len(devices)):
                self.devices.setItem(
                    device, 0, QTableWidgetItem(
                        devices[device]))
            self.unlock_phone.hide()

        def getPosContent(self, row, col):
            self.device_name = self.devices.item(row, col).text()
            if not self.device_name:
                return
            self.unlock_phone.show()

        def unlock(self):
            unlock_input = QInputDialog()
            unlock_input.setWindowTitle(get_translation("Enter Unlock Code"))
            unlock_input.setLabelText(get_translation("Enter Unlock Code"))
            unlock_input.setInputMode(QInputDialog.TextInput)
            unlock_input.setTextEchoMode(QLineEdit.Password)
            unlock_input.setContextMenuPolicy(Qt.NoContextMenu)
            unlock_input.setFixedSize(500, 50)
            unlock_input.show()
            if unlock_input.exec() == QInputDialog.Accepted:
                unlock_code = unlock_input.textValue()
                if unlock_code.isdigit() and len(unlock_code) == 11:
                    result = subprocess.run([FASTBOOT_PATH,
                                             "-s",
                                             self.device_name,
                                             "oem",
                                             "unlock",
                                             unlock_code],
                                            check=False,
                                            stderr=subprocess.PIPE).stderr
                    if hasattr(result, "decode"):
                        result = result.decode()
                    if "error" in result:
                        QMessageBox.warning(self, "", get_translation(result))
                    return
                QMessageBox.warning(
                    self, "", get_translation("Not A Valid Format"))

    class Settings(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowIcon(
                QIcon(
                    os.path.join(
                        absolute_path,
                        "dependencies",
                        "favicon.ico")))
            self.resize(800, 800)
            self.setWindowTitle(get_translation("App Settings"))
            self.layout = QGridLayout()
            self.languages = QComboBox(self)
            self.langs = os.listdir(
                os.path.join(
                    absolute_path,
                    "translations"))
            self.langs = [i for i in self.langs if i.endswith(".json")]
            self.langs.append("English")
            for lang in range(len(self.langs)):
                self.langs[lang] = self.langs[lang].replace(".json", "")
            self.languages.addItems(self.langs)
            self.languages.setCurrentText(config.get("language"))
            self.confirm_button = QPushButton(get_translation("Confirm"), self)
            self.confirm_button.clicked.connect(self.confirm)
            self.use_light = QRadioButton(get_translation("Use Light Theme"), self)
            self.use_dark = QRadioButton(get_translation("Use Dark Theme"), self)
            if theme == "light_teal.xml":
                self.use_light.setChecked(True)
            else:
                self.use_dark.setChecked(True)
            self.layout.addWidget(self.languages, 0, 0)
            self.layout.addWidget(self.use_light, 1, 0)
            self.layout.addWidget(self.use_dark, 2, 0)
            self.layout.addWidget(self.confirm_button, 3, 0)
            self.setLayout(self.layout)

        def confirm(self):
            config["language"] = self.languages.currentText()
            if self.use_light.isChecked():
                config["theme"] = "light_teal.xml"
            else:
                config["theme"] = "dark_teal.xml"
            with open(os.path.join(absolute_path, "config.json"), "w", encoding="utf-8") as f:
                json.dump(config, f, ensure_ascii=False)
            restart_program()

    class AppAnalyzer(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowTitle(get_translation("Android File Analyzer"))
            self.setWindowIcon(
                QIcon(
                    os.path.join(
                        absolute_path,
                        "dependencies",
                        "favicon.ico")))
            self.resize(800, 800)
            self.layout = QGridLayout()
            self.select_file_button = QPushButton(
                get_translation("Select File"))
            self.select_file_button.clicked.connect(self.select_file)
            self.file_path = QLineEdit(self)
            self.file_path.setReadOnly(True)
            self.analyze_result = QTreeWidget(self)
            self.layout.addWidget(self.file_path, 0, 1)
            self.layout.addWidget(self.analyze_result, 1, 0)
            self.layout.addWidget(self.select_file_button, 0, 0)
            self.setLayout(self.layout)

        def select_file(self):
            file_path, _ = QFileDialog.getOpenFileName(self, get_translation(
                "Select File"), "", f"{get_translation('APK File')}(*.apk)")
            if file_path:
                self.file_path.setText(file_path)
                self.analyze_file(file_path)

        def set_element(self, k, v, root):
            t = QTreeWidgetItem(root)
            t.setText(0, f"{k}：{v}")
            return t

        def analyze_file(self, file_path):
            self.analyze_result.clear()
            result = execute(
                [aapt_path, "dump", "badging", file_path])
            common = QTreeWidgetItem(
                self.analyze_result, [
                    get_translation("Common Message")])
            common_msgs = re.search(
                "package: " + " ".join(["(.*?)='(.*?)'" for i in range(5)]), result).groups()
            for msg in range(0, len(common_msgs), 2):
                self.set_element(get_translation(
                    common_msgs[msg]), common_msgs[msg + 1], common)
            self.set_element(
                get_translation("LaunchAble-activity"),
                re.search(
                    "launchable-activity: name='(.*?)'",
                    result).group(1),
                common)
            self.set_element(
                get_translation("SDK Version"),
                re.search(
                    "sdkVersion:'(.*?)'",
                    result).group(1),
                common)
            localization = QTreeWidgetItem(
                self.analyze_result, [
                    get_translation("Localization Message")])
            locales = re.search(
                "locales: (.*)",
                result).group(1).split(" ")[
                1:]
            for locale in locales:
                locale_name = locale.replace("'", "")
                locale = self.set_element(
                    get_translation("Localization Language"), locale, localization)
                application_label_locale = re.search(
                    f"application-label-{locale_name}:'(.*?)'", result).group(1)
                self.set_element(
                    get_translation("Application-Label Localization"),
                    application_label_locale,
                    locale)

            self.analyze_result.addTopLevelItem(localization)
            self.analyze_result.addTopLevelItem(common)

    class App(QWidget):
        def __init__(self):
            super().__init__()
            self.layout = QGridLayout()
            self.devices = QTableWidget(self)
            self.devices.setColumnCount(2)
            self.devices.setRowCount(15)
            self.devices.setHorizontalHeaderLabels(
                [get_translation("Device Name"), get_translation("Device Status")])
            self.devices.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.devices.cellPressed.connect(self.getPosContent)
            self.device_name = None
            self.refresh_button = QPushButton(get_translation("Refresh"), self)
            self.status = QTextEdit(self)
            self.status.setFixedHeight(200)
            self.status.setReadOnly(True)
            self.reboot_button = QPushButton(
                get_translation("Reboot Device"), self)
            self.root_button = QPushButton(
                get_translation("Get Root Permission"), self)
            self.shell_button = QPushButton(
                get_translation("Run Shell Command"), self)
            self.packages = QPushButton(
                get_translation("Package Operation"), self)
            self.packages.clicked.connect(self.package_operation)
            self.root_button.clicked.connect(self.root)
            self.reboot_button.clicked.connect(self.reboot)
            self.refresh_button.clicked.connect(self.update_devices)
            self.shell_button.clicked.connect(self.shell)
            self.layout.addWidget(self.refresh_button, 0, 1)
            self.layout.addWidget(self.devices, 0, 0)
            self.layout.addWidget(self.shell_button, 0, 2)
            self.layout.addWidget(self.status, 1, 0)
            self.layout.addWidget(self.reboot_button, 1, 2)
            self.layout.addWidget(self.root_button, 1, 3)
            self.layout.addWidget(self.packages, 0, 3)
            self.setLayout(self.layout)
            self.resize(800, 800)
            self.initUI()

        def getPosContent(self, row, col):
            try:
                self.device_name = self.devices.item(row, 0).text()
                desc = get_full_description(self.device_name)
                write_to = ""
                for i in desc.items():
                    write_to += f"{i[0]}：{i[1]}\n"
                self.status.setText(write_to)
                self.root_button.show()
                self.reboot_button.show()
                self.shell_button.show()
                self.packages.show()
            except BaseException as e:
                pass

        def update_devices(self):
            devices = get_all_devices()
            self.packages.hide()
            self.devices.clear()
            self.status.clear()
            self.root_button.hide()
            self.reboot_button.hide()
            self.shell_button.hide()
            for device in devices:
                self.devices.setItem(
                    devices.index(device),
                    0,
                    QTableWidgetItem(
                        device[0]))
                self.devices.setItem(
                    devices.index(device), 1, QTableWidgetItem(
                        get_translation(device[1])))

        def initUI(self):
            self.setWindowTitle(get_translation("Android Phone Manager"))
            self.setWindowIcon(
                QIcon(
                    os.path.join(
                        absolute_path,
                        "dependencies",
                        "favicon.ico")))
            self.update_devices()

        def reboot(self):
            if not self.device_name:
                QMessageBox.warning(
                    self,
                    get_translation("Warning"),
                    get_translation("Please Select A Device"))
                return
            self.reBoot = Rebooter(self.device_name)
            self.reBoot.show()

        def root(self):
            if not self.device_name:
                QMessageBox.warning(
                    self,
                    get_translation("Warning"),
                    get_translation("Please Select A Device"))
                return
            result = execute(
                [adb_path, "-s", self.device_name, "root"])
            if not result.strip():
                QMessageBox.information(
                    self, get_translation("Info"), get_translation("Successfully Get Root Permission"))
            else:
                QMessageBox.warning(self, get_translation(
                    "Warning"), get_translation("Unable To Get Root Permission\nError") + result)

        def shell(self):
            if not self.device_name:
                QMessageBox.warning(
                    self,
                    get_translation("Warning"),
                    get_translation("Please Select A Device"))
                return
            with open(os.path.join(tempfile.gettempdir(), "androidShellBootLoader.bat"), "w") as f:
                f.write("@echo off\n")
                f.write(f"title {get_translation('Android Terminal')}\n")
                f.write(f"echo {get_translation('Android Terminal')}\n")
                f.write(
                    f"echo {get_translation('When You Are Using It, May Be Cause The Device Not Able To Run, Please Use Carefully')}\n")
                f.write(f"adb -s {self.device_name} shell\n")
                f.write("exit 0\n")
            os.system(
                f"start {os.path.join(tempfile.gettempdir(), 'androidShellBootLoader.bat')}")

        def package_operation(self):
            if not self.device_name:
                QMessageBox.warning(
                    self,
                    get_translation("Warning"),
                    get_translation("Please Select A Device"))
                return
            self.package_window = PackageOperation(self.device_name)
            self.package_window.show()

    class PackageOperation(QWidget):
        def __init__(self, device_name):
            super().__init__()
            self.setWindowTitle(get_translation("Android Phone Manager"))
            self.setWindowIcon(
                QIcon(
                    os.path.join(
                        absolute_path,
                        "dependencies",
                        "favicon.ico")))
            self.cache = {}
            self.layout = QGridLayout()
            self.device_name = device_name
            self.packages = QTableWidget(self)
            self.packages.setColumnCount(1)
            self.packages.setRowCount(100)
            self.packages.setMinimumHeight(300)
            self.packages.setHorizontalHeaderLabels(
                [get_translation("Installed Packages Name")])
            self.packages.cellPressed.connect(self.getPosContent)
            self.packages.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.install_button = QPushButton(
                get_translation("Install App"), self)
            self.uninstall_button = QPushButton(
                get_translation("Uninstall App"), self
            )
            self.refresh_button = QPushButton(
                get_translation("Refresh"), self
            )
            self.search = QLineEdit(self)
            self.search.textChanged.connect(self.search_app)
            self.refresh_button.clicked.connect(self.refresh)
            self.package_name = ""
            self.setLayout(self.layout)
            self.resize(800, 800)
            self.layout.addWidget(self.search, 0, 0)
            self.layout.addWidget(self.packages, 1, 0)
            self.layout.addWidget(self.uninstall_button, 1, 1)
            self.layout.addWidget(self.install_button, 1, 2)
            self.uninstall_button.clicked.connect(self.uninstall_app)
            self.install_button.clicked.connect(self.install_app)
            self.layout.addWidget(self.refresh_button)
            self.refresh()

        def getPosContent(self, row, col):
            self.package_name = self.packages.item(row, col).text()
            print(self.package_name)
            self.uninstall_button.show()
            return

        def install_app(self):
            file_name = QFileDialog.getOpenFileName(
                self, get_translation("Please Select An Installer"), "",
                "APK Files (*.apk);;APEX Files (*.apex);;All Files (*)")
            file_name = file_name[0]
            if file_name and self.device_name:
                self.installer = Installer(file_name, self.device_name)
                del self.installer
                self.refresh()

        def refresh(self):
            self.uninstall_button.hide()
            self.packages.clear()
            packages = execute(
                [ADB_PATH, "shell", "pm", "list", "packages"]).split()
            packages = [i.replace("package:", "") for i in packages]
            for package in packages:
                self.packages.setItem(
                    packages.index(package), 0, QTableWidgetItem(package))

        def uninstall_app(self):
            if not self.package_name:
                QMessageBox.warning(
                    self,
                    get_translation("Warning"),
                    get_translation("Please Select A Device"))
                return
            confirm_install = QMessageBox.information(
                self,
                get_translation("Warning"),
                get_translation("Confirm Uninstall?"),
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.Yes)
            if confirm_install == QMessageBox.Yes:
                self.uninstaller = Uninstaller(
                    self.package_name, self.device_name)
                del self.uninstaller
                self.refresh()

        def search_app(self):
            self.packages.clear()
            packages = execute(
                [ADB_PATH, "shell", "pm", "list", "packages"]).split()
            packages = [i.replace("package:", "")
                        for i in packages if self.search.text() in i]
            for package in packages:
                self.packages.setItem(
                    packages.index(package), 0, QTableWidgetItem(package))

    class Rebooter(QWidget):
        def __init__(self, device_name):
            super().__init__()
            self.setWindowTitle(get_translation("Android Phone Manager"))
            self.setWindowIcon(
                QIcon(
                    os.path.join(
                        absolute_path,
                        "dependencies",
                        "favicon.ico")))
            self.device_name = device_name
            self.reboot_types = {
                get_translation("Normal Reboot"): "",
                get_translation("Reboot to Recovery"): "recovery",
                get_translation("Reboot to Bootloader"): "bootloader",
                get_translation("Reboot to SideLoad"): "sideload",
                get_translation("Reboot to SideLoad-Auto-Reboot"): "sideload-auto-reboot"
            }
            self.layout = QGridLayout()
            self.layout.addWidget(
                QLabel(
                    get_translation("Please Select Reboot Method:")),
                0,
                0)
            self.reboot_selection = QComboBox(self)
            self.reboot_selection.addItems(self.reboot_types.keys())
            self.layout.addWidget(self.reboot_selection, 0, 1)
            self.reboot_button = QPushButton(get_translation("Reboot"), self)
            self.reboot_button.clicked.connect(self.reboot)
            self.layout.addWidget(self.reboot_button, 0, 2)
            self.setLayout(self.layout)

        def reboot(self):
            reboot_type = self.reboot_selection.currentText()
            external_cmd = self.reboot_types[reboot_type]
            execute(
                [adb_path, "-s", self.device_name, "reboot", external_cmd])
            QMessageBox.information(self, get_translation(
                "Info"), get_translation("Reboot Successfully"))

    class Loader(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowTitle(get_translation("Android Phone Manager"))
            self.setWindowIcon(
                QIcon(
                    os.path.join(
                        absolute_path,
                        "dependencies",
                        "favicon.ico")))
            self.loading_icon = QMovie(
                os.path.join(
                    absolute_path,
                    "dependencies",
                    "loading.gif"))
            self.show()
            self.layout = QGridLayout()
            self.loading = QLabel(self)
            self.loading.setMovie(self.loading_icon)
            self.loading_icon.start()
            threading.Thread(target=self.work).start()
            self.layout.addWidget(self.loading)
            self.setLayout(self.layout)

        def work(self):
            self.loading_icon.stop()
            self.close()

    class Installer(Loader):
        def __init__(self, file_name, device_name):
            self.file_name = file_name
            self.device_name = device_name
            super().__init__()

        def work(self):
            cmd = subprocess.Popen(
                [adb_path, "-s", self.device_name, "install", self.file_name])
            cmd.wait()
            self.loading_icon.stop()
            self.close()

    class Uninstaller(Loader):
        def __init__(self, package_name, device_name):
            self.package_name = package_name
            self.device_name = device_name
            super().__init__()

        def work(self):
            cmd = subprocess.Popen([ADB_PATH,
                                    "-s",
                                    self.device_name,
                                    "shell",
                                    "pm",
                                    "uninstall",
                                    "-k",
                                    "--user",
                                    "0",
                                    self.package_name])
            cmd.wait()
            self.loading_icon.stop()
            self.close()

    def main():
        app = QApplication(sys.argv)
        apply_stylesheet(app, theme=theme)
        tab = Tabs()
        tab.show()
        sys.exit(app.exec())

    main()
