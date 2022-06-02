import ctypes
import os
import json
import re
import tempfile
import threading
import subprocess
import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qt_material import apply_stylesheet


absolute_path = os.path.dirname(__file__)
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
    "AndroidPhoneManager")

ADB_PATH = os.path.join(absolute_path, "dependencies", "adb.exe")
AAPT_PATH = os.path.join(absolute_path, "dependencies", "aapt.exe")
translation = {}
if os.path.exists(os.path.join(absolute_path, "translations", "history.txt")):
    with open(os.path.join(absolute_path, "translations", "history.txt"), "r", encoding="utf-8") as f:
        with open(os.path.join(absolute_path, "translations", f.read()) + ".json", "r", encoding="utf-8") as f2:
            translation = json.load(f2)


def get_translation(trans):
    return translation.get(trans, trans)


def get_all_devices():
    output = subprocess.check_output([ADB_PATH, "devices"])
    res = re.findall("(.*)\t(.*)", output)
    return res


def get_full_description(device_name):
    output = subprocess.check_output([ADB_PATH, "devices", "-l"])
    res = re.findall(
        f"{device_name}.*\\s(.*\\S).*\\sproduct:(.*\\S).*\\smodel:(.*\\S).*\\sdevice:(.*\\S).*\\stransport_id:(.*\\S)",
        output)
    result = []
    for r in res:
        result.append({get_translation("Device Status"): get_translation(r[0]),
                       get_translation("Device Product"): r[1],
                       get_translation("Device Model"): r[2],
                       get_translation("Transport ID"): r[4]})
    result = result[0]
    result[get_translation("Screen Resolution")] = re.search("Physical size: (.*)",
                                                             subprocess.check_output(
                                                                 [ADB_PATH, "-s", device_name, "shell", "wm",
                                                                  "size"])).group(1)
    result[get_translation("Android-ID")] = subprocess.check_output(
        [ADB_PATH, "-s", device_name, "shell", "settings", "get", "secure", "android_id"]).strip()

    result[get_translation("IPv4 Address")] = re.search(
        "inet addr:(.*) Mask:", subprocess.check_output([ADB_PATH, "shell", "ifconfig"])).group(1)
    return result


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
        self.addTab(self.common_tab, get_translation("Common"))
        self.addTab(self.analyzer_tab, get_translation("Analyze APK"))
        self.addTab(self.settings_tab, get_translation("Settings"))
        self.resize(800, 800)


class Settings(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(get_translation("App Settings"))
        self.setWindowIcon(
            QIcon(
                os.path.join(
                    absolute_path,
                    "dependencies",
                    "favicon.ico")))
        self.resize(800, 800)
        self.layout = QGridLayout()
        self.languages = QComboBox(self)
        self.langs = os.listdir(
            os.path.join(
                absolute_path,
                "translations")) + ["English"]
        if "history.txt" in self.langs:
            self.langs.remove("history.txt")
        for lang in range(len(self.langs)):
            self.langs[lang] = self.langs[lang].replace(".json", "")
        self.languages.addItems(self.langs)
        self.languages.setCurrentText(get_translation("Language"))
        self.confirm_button = QPushButton(get_translation("Confirm"), self)
        self.confirm_button.clicked.connect(self.confirm)
        self.layout.addWidget(self.languages, 0, 0)
        self.layout.addWidget(self.confirm_button, 1, 0)
        self.setLayout(self.layout)

    def confirm(self):
        global translation
        with open(os.path.join(absolute_path, "translations", "history.txt"), "w", encoding="utf-8") as f:
            f.write(self.languages.currentText())
        if self.languages.currentText() == "English":
            os.remove(os.path.join(absolute_path, "translations", "history.txt"))
        else:
            with open(os.path.join(absolute_path, "translations", "history.txt"), "w", encoding="utf-8") as f:
                f.write(self.languages.currentText())
        QMessageBox.information(
            self,
            get_translation("Success"),
            get_translation("Successfully changed language"))
        QMessageBox.information(
            self,
            get_translation("Restart"),
            get_translation("Please restart the program"))


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
        self.select_file_button = QPushButton(get_translation("Select File"))
        self.select_file_button.clicked.connect(self.select_file)
        self.file_path = QLineEdit(self)
        self.file_path.setReadOnly(True)
        self.layout.addWidget(self.file_path, 0, 1)
        self.layout.addWidget(self.select_file_button, 0, 0)
        self.result = QTreeWidget(self)
        self.layout.addWidget(self.result, 1, 0)
        self.setLayout(self.layout)

    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, get_translation("Select File"), "", f"{get_translation('APK File')}(*.apk)")
        if file_path:
            self.file_path.setText(file_path)
            self.analyze_file(file_path)

    def set_element(self, k, v, root):
        t = QTreeWidgetItem(root)
        t.setText(0, f"{k}：{v}")
        return t

    def analyze_file(self, file_path):
        self.result.clear()
        result = subprocess.check_output(
            [AAPT_PATH, "dump", "badging", file_path])
        common = QTreeWidgetItem(
            self.result, [
                get_translation("Common Message")])
        common_msgs = re.search(
            "package: " + " ".join(["(.*)='(.*)'" for i in range(7)]), result).groups()
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
            self.result, [
                get_translation("Localization Message")])
        locales = re.search("locales: (.*)", result).group(1).split(" ")[1:]
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

        self.result.addTopLevelItem(localization)
        self.result.addTopLevelItem(common)


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QGridLayout()
        self.devices = QTableWidget(self)
        self.devices.setColumnCount(2)
        self.devices.setRowCount(15)
        self.devices.setHorizontalHeaderLabels(
            [get_translation("Device Name"), get_translation("Device Status")])
        self.devices.cellPressed.connect(self.getPosContent)
        self.device_name = None
        self.refresh_button = QPushButton(get_translation("Refresh"), self)
        self.status = QTextEdit(self)
        self.status.setFixedHeight(200)
        self.status.setReadOnly(True)
        self.install_button = QPushButton(get_translation("Install App"), self)
        self.reboot_button = QPushButton(
            get_translation("Reboot Device"), self)
        self.root_button = QPushButton(
            get_translation("Get Root Permission"), self)
        self.shell_button = QPushButton(
            get_translation("Run Shell Command"), self)
        self.root_button.clicked.connect(self.root)
        self.reboot_button.clicked.connect(self.reboot)
        self.install_button.clicked.connect(self.install_app)
        self.refresh_button.clicked.connect(self.update_devices)
        self.shell_button.clicked.connect(self.shell)
        self.layout.addWidget(self.refresh_button, 0, 1)
        self.layout.addWidget(self.devices, 0, 0)
        self.layout.addWidget(self.shell_button, 0, 2)
        self.layout.addWidget(self.status, 1, 0)
        self.layout.addWidget(self.install_button, 1, 1)
        self.layout.addWidget(self.reboot_button, 1, 2)
        self.layout.addWidget(self.root_button, 1, 3)
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
            self.install_button.show()
            self.root_button.show()
            self.reboot_button.show()
            self.shell_button.show()
        except BaseException:
            pass

    def update_devices(self):
        devices = get_all_devices()
        self.devices.clear()
        self.status.clear()
        self.install_button.hide()
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
        # self.show()

    def install_app(self):
        if not self.device_name:
            QMessageBox.warning(
                self,
                get_translation("Warning"),
                get_translation("Please Select A Device"))
            return
        file_name = QFileDialog.getOpenFileName(
            self, get_translation("Please Select An Installer"), "",
            "APK Files (*.apk);;APEX Files (*.apex);;All Files (*)")
        file_name = file_name[0]
        if file_name and self.device_name:
            self.installer = Installer(file_name, self.device_name)
            self.installer.show()

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
        result = subprocess.check_output(
            [ADB_PATH, "-s", self.device_name, "root"])
        if not result.strip():
            QMessageBox.information(
                self, get_translation("Info"), "获取root权限成功")
        else:
            QMessageBox.warning(self, get_translation(
                "Warning"), "获取root权限失败\n错误：" + result)

    def shell(self):
        if not self.device_name:
            QMessageBox.warning(
                self,
                get_translation("Warning"),
                get_translation("Please Select A Device"))
            return
        with open(os.path.join(tempfile.gettempdir(), "androidShellBootLoader.bat"), "w") as f:
            f.write("@echo off\n")
            f.write("title Android Shell\n")
            f.write("echo 安卓终端\n")
            f.write("echo 在使用过程中，有可能会导致设备无法正常运行，请谨慎使用\n")
            f.write(f"adb -s {self.device_name} shell\n")
            f.write("exit 0\n")
        os.system(
            f"start {os.path.join(tempfile.gettempdir(), 'androidShellBootLoader.bat')}")


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
        self.reboot_types = [get_translation(i) for i in
                             ["Normal Reboot",
                              "Reboot to Recovery",
                              "Reboot to Bootloader",
                              "Reboot to SideLoad",
                              "Reboot to Sideload-Auto-Reboot"]]
        self.layout = QGridLayout()
        self.layout.addWidget(
            QLabel(
                get_translation("Please Select Reboot Method:")),
            0,
            0)
        self.reboot_selection = QComboBox(self)
        self.reboot_selection.addItems(self.reboot_types)
        self.layout.addWidget(self.reboot_selection, 0, 1)
        self.reboot_button = QPushButton(get_translation("Reboot"), self)
        self.reboot_button.clicked.connect(self.reboot)
        self.layout.addWidget(self.reboot_button, 0, 2)
        self.setLayout(self.layout)

    def reboot(self):
        reboot_type = self.reboot_selection.currentText()
        if reboot_type == self.reboot_types[0]:
            external_cmd = ""
        elif reboot_type == self.reboot_types[1]:
            external_cmd = "bootloader"
        elif reboot_type == self.reboot_types[2]:
            external_cmd = "recovery"
        elif reboot_type == self.reboot_types[3]:
            external_cmd = "sideload"
        elif reboot_type == self.reboot_types[4]:
            external_cmd = "sideload-auto-reboot"
        subprocess.check_output(
            [ADB_PATH, "-s", self.device_name, "reboot", external_cmd])
        QMessageBox.information(self, get_translation(
            "Info"), get_translation("Reboot Successfully"))


class Installer(QWidget):
    def __init__(self, file_name, device_name):
        super().__init__()
        self.setWindowTitle(get_translation("Android Phone Manager"))
        self.setWindowIcon(
            QIcon(
                os.path.join(
                    absolute_path,
                    "dependencies",
                    "favicon.ico")))
        self.file_name = file_name
        self.device_name = device_name
        self.loading_icon = QMovie(
            os.path.join(
                absolute_path,
                "dependencies",
                "loading.gif"))
        self.layout = QGridLayout()
        self.loading = QLabel(self)
        self.loading.setMovie(self.loading_icon)
        self.loading_icon.start()
        threading.Thread(target=self.install).start()
        self.layout.addWidget(self.loading)
        self.setLayout(self.layout)

    def install(self):
        cmd = subprocess.Popen(
            [ADB_PATH, "-s", self.device_name, "install", self.file_name])
        cmd.wait()
        self.loading_icon.stop()
        self.close()


def main():
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='light_teal.xml')
    tab = Tabs()
    tab.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
