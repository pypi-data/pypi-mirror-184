
MovingClock \_ 生成动态时钟
==================================

|License| |Pypi| |Author| |Github|

安装方法
--------

通过 pip 直接安装

::

   pip install MovingClock

更新

::

   pip install MovingClock --upgrade

使用方法
--------

导入

::

   import MovingClock

使用

::

   MovingClock.main()

**！注意事项！**

import MovingClock **√**

import movingclock **×**

关于作者
--------
Author

*Jason4zh*

Email

*13640817984@163.com*

Package

*https://pypi.org/project/MovingClock/*


::

   print("Thank you for using!")



本次更新修改v3.1.0
------------------

1. 修复了文件调用错误问题(mp3文件不在打包范围内)

*在以前的版本修复中曾修复过此问题，但未修复完成*

*这次修复将原项目中的src文件夹(包含三个mp3)放到了dist可以打包到的MovingClock源代码文件夹*

*修复后src文件夹将会出现在Python/Lib库文件夹中，即可在程序“闹钟”功能中体现*

2. 在 **__init__.py** 中添加了运行本体的功能(即 *if __name__ == "__main__"* 框架)

*可运行.\Username\AppData\Local\Programs\Python\Python36\Lib\site-packages\MovingClock\__init__.py查看样例*

*一些编辑器可使用 Ctrl+鼠标左键  import -> MovingClock <- 以查看*

.. |License| image:: https://img.shields.io/pypi/l/MovingClock
   :target: https://github.com/Jason4zh/MovingClock/blob/main/LICENSE
.. |Pypi| image:: https://img.shields.io/badge/Pypi-v3.1-blue
   :target: https://pypi.org/project/MovingClock
.. |Author| image:: https://img.shields.io/badge/Author-Jason4zh-green
   :target: https://pypi.org/user/Jason4zh
.. |Github| image:: https://img.shields.io/badge/Github-Jason4zh-red
   :target: https://github.com/Jason4zh/MovingClock
