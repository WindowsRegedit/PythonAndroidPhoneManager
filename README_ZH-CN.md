### Python 版 Android 管理器

[English Docs](/README.md)

#### 警告
因为在打包时出现了一些问题，所以暂时不会支持二进制安装文件，请使用 源码安装 

#### 描述
这是 WindowsRegedit 编写而成的 Python 版 Android 管理器

#### 软件截图
![img.png](https://fastly.jsdelivr.net/gh/WindowsRegedit/PythonAndroidPhoneManager@master/img.png)

#### 翻译支持
打开源代码，你可以发现一个 "translations" 文件夹

比如说中文翻译：
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
所有键都是需要被翻译的。

将新翻译文件保存为 "LanguageName.json" 的格式,

这个程序就会自动检测到它的。

[请发布issues]

#### 更新记录
[v1.0]
Android 管理器 第一版！

这是一个关键的版本

它包含：

翻译支持

APK / APEX 文件安装支持.

分析 APK 文件 支持.

问题:

最近只支持Windows系统。