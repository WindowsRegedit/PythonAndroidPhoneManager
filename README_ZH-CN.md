### Python 版 Android 管理器

[English Docs](README.md)

#### 描述
这是 WindowsRegedit 编写而成的 Python 版 Android 管理器

#### 软件截图
![img.png](https://fastly.jsdelivr.net/gh/WindowsRegedit/PythonAndroidPhoneManager@master/img.png)

#### 安装
##### 使用``pip``安装：（推荐）
```shell
pip install android-manager
```
使用此命令来启动：
```shell
android-manager
```
##### 使用源码安装：
```shell
git clone https://github.com/WindowsRegedit/PythonAndroidPhoneManager.git
cd PythonAndroidPhoneManager
python setup.py install
```
然后像``Pip``一样启动：
```shell
android-manager
```

#### 翻译支持
打开源代码，你可以发现一个 "translations" 文件夹

比如说中文翻译：
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
  "Package Operation": "对已安装的程序包进行操作",
  "Please Select A Device": "请选择一个设备",
  "Please Select An Installer": "请选择一个安装包",
  "Please Select Reboot Method": "请选择重启方式：",
  "Please restart the program": "请重新启动程序",
  "Reboot": "重启",
  "Reboot Device": "重启设备",
  "Reboot Successfully": "重启成功",
  "Reboot to Bootloader": "重启到Bootloader",
  "Reboot to Recovery": "重启到Recovery",
  "Reboot to SideLoad": "重启到SideLoad(侧载)",
  "Reboot to SideLoad-Auto-Reboot": "重启至SideLoad-Auto-Reboot(侧载并自动重启)",
  "Refresh": "刷新",
  "Restart": "重新启动",
  "Run Shell Command": "运行Shell命令",
  "SDK Version": "SDK版本",
  "Screen Resolution": "屏幕分辨率",
  "Select File": "选择文件",
  "Settings": "设置",
  "Success": "成功",
  "Successfully Get Root Permission": "成功获取Root权限",
  "Successfully changed language": "成功更改语言",
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
  "Find App Package Name": "查找应用名称"
}
```
所有键都是需要被翻译的。

将新翻译文件保存为 "LanguageName.json" 的格式,

这个程序就会自动检测到它的。

[请发布issues]

#### 更新记录
[v4]<br>
新板块 “软件包操作”！
包括搜索已安装的软件包，卸载、安装软件包。
更改“安装软件包”到“软件包操作”板块。

[v3.3]<br>
支持``pip``安装了！<br>
更多信息请阅读[安装](#安装)板块。

[v3.0]<br>
从这个版本以后，就需要网络连接了，
但它使用了更少的磁盘空间。<br>

[v2.0]<br>
第二个版本！<br>
支持多平台
(像 Windows, macOS 和 Linux系统)<br>

[v1.0]<br>
Android 管理器 第一版！<br>
这是一个关键的版本。<br>
它包含：<br>
 - 翻译支持<br>
 - APK / APEX 文件安装支持.<br>
 - 分析 APK 文件 支持.<br>
问题:<br>
最近只支持Windows系统。<br>