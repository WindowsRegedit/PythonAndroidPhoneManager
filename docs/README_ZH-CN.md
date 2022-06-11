### Python 版 Android 管理器

[English Docs](https://github.com/WindowsRegedit/PythonAndroidPhoneManager/README.md)

#### 描述
这是 WindowsRegedit 编写而成的 Python 版 Android 管理器。

#### 软件截图
![light_theme_zh-cn.png](https://github.com/WindowsRegedit/PythonAndroidPhoneManager/docs/dark_theme-zh-cn.png)
<font color="grey">浅色主题</font>
![dark_theme_zh-cn.png](https://github.com/WindowsRegedit/PythonAndroidPhoneManager/docs/light_theme-zh-cn.png)
<font color="grey">深色主题</font>

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
打开源代码，你可以发现一个 "translations" 文件夹。<br>

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
所有键都是需要被翻译的。<br>
将新翻译文件保存为 "LanguageName.json" 的格式,<br>
这个程序就会自动检测到它的。<br>

**请发布issues**

#### 更新记录
##### v5
新标签 "FastBoot(危险区域)"。<br>
它包含解锁手机（需要bootloader解锁码）<br>
在设置里，添加了更改主题的代码。<br>
并且切换语言与更改主题的时候都是自动先切换到已选的语言。<br>
PS: 不需要再重新启动才能更改了!!!!!!

##### v4
新板块 “软件包操作”！<br>
包括搜索已安装的软件包，卸载、安装软件包。<br>
更改“安装软件包”到“软件包操作”板块。<br>

##### v3.3
支持``pip``安装了！<br>
更多信息请阅读[安装](#安装)板块。

##### v3.0
从这个版本以后，就需要网络连接了，但它使用了更少的磁盘空间。<br>

##### v2.0
第二个版本！<br>
支持多平台
(像 Windows, macOS 和 Linux系统)<br>

##### v1.0
Android 管理器 第一版！<br>
这是一个关键的版本。<br>
它包含：<br>
 - 翻译支持<br>
 - APK / APEX 文件安装支持.<br>
 - 分析 APK 文件 支持.<br>
问题:<br>
最近只支持Windows系统。<br>