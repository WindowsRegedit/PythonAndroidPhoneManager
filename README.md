### Android Manager By Python

[中文文档](README_ZH-CN.md)

#### Info
This is an Android Manage App Designed By WindowsRegedit.<br>

#### App Screenshot
![img.png](https://fastly.jsdelivr.net/gh/WindowsRegedit/PythonAndroidPhoneManager@master/img.png)

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
  "Screen Resolution": "屏幕分辨率",
  "Device Product": "设备分类",
  "Device Model": "设备型号",
  "Transport ID": "传输ID",
  "Android-ID": "Android-ID",
  "IPv4 Address": "IPv4地址",
  "Android Phone Manager": "安卓手机管理器",
  "Common": "常用",
  "Analyze APK": "分析APK",
  "Select File": "选择文件",
  "name": "包名",
  "versionCode": "版本代码",
  "versionName": "版本名称",
  "platformBuildVersionName": "平台编译版本名称",
  "platformBuildVersionCode": "平台编译版本代码",
  "compileSdkVersion": "编译SDK版本",
  "compileSdkVersionCodename": "编译SDK版本名称",
  "APK File": "APK文件",
  "Common Message": "常用信息",
  "LaunchAble-activity": "可启动的服务",
  "SDK Version": "SDK版本",
  "Localization Message": "本地化信息",
  "Localization Language": "本地化语言",
  "Application-Label Localization": "应用名称本地化",
  "device": "正常",
  "offline": "离线(OffLine)",
  "unknown": "未知",
  "unauthorized": "未授权",
  "Device Name": "设备名称",
  "Device Status": "设备状态",
  "Refresh": "刷新",
  "Install App": "安装应用",
  "Reboot Device": "重启设备",
  "Get Root Permission": "获取Root权限",
  "Run Shell Command": "运行Shell命令",
  "Warning": "警告",
  "Please Select A Device": "请选择一个设备",
  "Please Select An Installer": "请选择一个安装包",
  "Info": "提示",
  "Successfully Get Root Permission": "成功获取Root权限",
  "Unable To Get Root Permission\nError": "无法获取Root权限\n错误",
  "Android Terminal": "安卓终端",
  "When You Are Using It, May Be Cause The Device Not Able To Run, Please Use Carefully": "在使用过程中，有可能会导致设备无法正常运行，请谨慎使用",
  "Normal Reboot": "正常重启",
  "Reboot to Recovery": "重启到Recovery",
  "Reboot to Bootloader": "重启到Bootloader",
  "Reboot to SideLoad": "重启到SideLoad(侧载)",
  "Reboot to SideLoad-Auto-Reboot": "重启至SideLoad-Auto-Reboot(侧载并自动重启)",
  "Please Select Reboot Method": "请选择重启方式：",
  "Reboot": "重启",
  "Reboot Successfully": "重启成功",
  "Android File Analyzer": "Android文件分析器",
  "Settings": "设置",
  "App Settings": "软件设置",
  "Confirm": "确认",
  "Success": "成功",
  "Successfully changed language": "成功更改语言",
  "Restart": "重新启动",
  "Please restart the program": "请重新启动程序"
}
```
All the keys are needed for translation.<br>
Save the new Translation Files FileName as "LanguageName.json",<br>
The program will Detect It.<br>
[Please Release Issues.]

#### Update Info
[Version 4]<br>
New Block "Package Operation".<br>
Support search packages, uninstall packages and install packages.<br>
Change "Install Package" position to Package Operation.


[Version 3.3]<br>
We support ``pip`` installation now !<br>
For more information, see: 
[Installation](#Installation)

[Version 3.0]<br>
After This Release, it needs internet connection to download ADB And AAPT Files,
But It uses less disk spaces.<br>

[Version 2.0]<br>
Second Release!<br>
It finally supports Multiple System.<br>
(Like Windows, macOS and Linux)<br>

[Version 1.0]<br>
Android Manager First Release!<br>
This is an important release.<br>
It contains:<br>
 - Translation Support.<br>
 - APK / APEX File Install Support.<br>
 - Analyze APK File Support.<br>
Issues:<br>
Only support on Windows Temporarily.<br>