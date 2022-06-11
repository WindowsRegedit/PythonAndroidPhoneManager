### Android Manager By Python

[中文文档](https://github.com/WindowsRegedit/PythonAndroidPhoneManager/docs/README_ZH-CN.md)

#### Info
This is an Android Manage App Designed By WindowsRegedit.<br>

#### App Screenshot
![light_theme_en.png](https://github.com/WindowsRegedit/PythonAndroidPhoneManager/light_theme_en.png)
<font color="grey">Light Theme</font>
![dark_theme_en.png](https://github.com/WindowsRegedit/PythonAndroidPhoneManager/dark_theme_en.png)
<font color="grey">Dark Theme</font>


#### Installation
##### Use pip to install (recommend):
```shell
pip install android-manager
```
And to boot like that:<br>
```shell
android-manager
```
##### Use source code to install:
```shell
git clone https://github.com/WindowsRegedit/PythonAndroidPhoneManager.git
cd PythonAndroidPhoneManager
python setup.py install
```
And boot like Pip Installation:
```shell
android-manager
```

#### Translation Support
Open the source, You will see a "translations" folder.<br>
It contains Chinese Support like that:
```json
{
    "APK File": "APK文件",
    "Analyze APK": "分析APK",
    "Android File Analyzer": "Android文件分析器",
    "Android Phone Manager": "安卓手机管理器",
    "Android Terminal": "安卓终端",
    "Android-ID": "Android-ID",
    "App Settings": "软件设置",
    "Application-Label Localization": "应用名称本地化",
    "Common": "常用",
    "Common Message": "常用信息",
    "Confirm": "确认",
    "Confirm Uninstall?": "确定卸载？",
    "Device Model": "设备型号",
    "Device Name": "设备名称",
    "Device Product": "设备分类",
    "Device Status": "设备状态",
    "Get Root Permission": "获取Root权限",
    "IPv4 Address": "IPv4地址",
    "Info": "提示",
    "Install App": "安装应用",
    "Installed Packages Name": "已安装程序名称",
    "LaunchAble-activity": "可启动的服务",
    "Localization Language": "本地化语言",
    "Localization Message": "本地化信息",
    "Normal Reboot": "正常重启",
    "Package Operation": "对程序包进行操作",
    "Please Select A Device": "请选择一个设备",
    "Please Select An Installer": "请选择一个安装包",
    "Please Select Reboot Method": "请选择重启方式：",
    "Reboot": "重启",
    "Reboot Device": "重启设备",
    "Reboot Successfully": "重启成功",
    "Reboot to Bootloader": "重启到Bootloader",
    "Reboot to Recovery": "重启到Recovery",
    "Reboot to SideLoad": "重启到SideLoad(侧载)",
    "Reboot to SideLoad-Auto-Reboot": "重启至SideLoad-Auto-Reboot(侧载并自动重启)",
    "Refresh": "刷新",
    "Run Shell Command": "运行Shell命令",
    "SDK Version": "SDK版本",
    "Screen Resolution": "屏幕分辨率",
    "Select File": "选择文件",
    "Settings": "设置",
    "Successfully Get Root Permission": "成功获取Root权限",
    "Transport ID": "传输ID",
    "Unable To Get Root Permission\nError": "无法获取Root权限\n错误",
    "Uninstall App": "卸载程序",
    "Warning": "警告",
    "When You Are Using It, May Be Cause The Device Not Able To Run, Please Use Carefully": "在使用过程中，有可能会导致设备无法正常运行，请谨慎使用",
    "compileSdkVersion": "编译SDK版本",
    "compileSdkVersionCodename": "编译SDK版本名称",
    "device": "正常",
    "name": "包名",
    "offline": "离线(OffLine)",
    "platformBuildVersionCode": "平台编译版本代码",
    "platformBuildVersionName": "平台编译版本名称",
    "unauthorized": "未授权",
    "unknown": "未知",
    "versionCode": "版本代码",
    "versionName": "版本名称",
    "Find App Package Name": "查找应用名称",
    "FastBoot(Danger Zone)": "FastBoot(危险区域)",
    "Unlock Phone": "解锁手机",
    "Enter Unlock Code": "输入解锁手机码",
    "Not A Valid Format": "不是正确的格式",
    "FAILED (remote: 'check password failed!')\r\nfastboot: error: Command failed\r\n": "错误 (设备: '检查密码失败！')\r\nfastboot: 错误: 命令失败\r\n",
    "FAILED (remote: 'device will reboot after 30S due to 5 times of wrong key.')\r\nfastboot: error: Command failed\r\n": "错误 (设备: '30秒后设备将重启因为输入了5次错误的密码')\nfastboot: 错误: 命令失败\n",
    "FAILED (Status read failed (Too many links))\r\nfastboot: error: Command failed\r\n": "错误 (状态读取失败(太多链接))\nfastboot: 错误: 命令失败\n",
    "Use Light Theme": "使用亮主题",
    "Use Dark Theme": "使用暗主题"
}
```
All the keys are needed for translation.<br>
Save the new Translation Files FileName as "LanguageName.json",<br>
The program will Detect It.<br>
[Please Release Issues.]

#### Update Info
##### Version 5
New Tab "FastBoot(Danger Zone)".<br>
It contains "unlock phone".<br>
In settings, it adds "Change Theme" block.<br>
And change the "Change Language" and "Change Theme" parts default by the last time setting.
PS: NO NEED FOR RESTART TO CHANGE.IT WILL AUTO CHANGE IT!!!!!!

##### Version 4
New Block "Package Operation".<br>
Support search packages, uninstall packages and install packages.<br>
Change "Install Package" position to Package Operation.<br>

##### Version 3.3
We support ``pip`` installation now !<br>
For more information, see: [Installation](#Installation)

##### Version 3.0<br>
After This Release, it needs internet connection to download ADB And AAPT Files, But It uses less disk spaces.<br>

##### Version 2.0
Second Release!<br>
It finally supports Multiple System.<br>
(Like Windows, macOS and Linux)<br>

##### Version 1.0
Android Manager First Release!<br>
This is an important release.<br>
It contains:<br>
 - Translation Support.<br>
 - APK / APEX File Install Support.<br>
 - Analyze APK File Support.<br>
Issues:<br>
Only support on Windows Temporarily.<br>