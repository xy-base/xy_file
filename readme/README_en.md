<!--
 * @Author: yuyanget 845262968@qq.com
 * @Date: 2024-10-18 20:12:00
 * @LastEditors: yuyanget 845262968@qq.com
 * @LastEditTime: 2024-10-18 20:16:14
 * @FilePath: /xy_file/readme/README_en.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# xy_file

- [简体中文](README_zh_CN.md)
- [繁体中文](README_zh_TW.md)
- [English](README_en.md)


## Description
Easy File tools, especially for regular.

## Source Code Repositories

- <a href="https://github.com/xy-base/xy_file.git" target="_blank">Github</a>  
- <a href="https://gitee.com/xy-base/xy_file.git" target="_blank">Gitee</a>

## 安装

```bash
pip install xy_file
```

## How to use

###### 1. Terminal
```bash
# Delete all py files under current work folder.
xy_file -w clean -g "*.py"

```

###### 2. python script

```python
from xy_file.File import File
from pathlib import Path

touch_file_path = Path.cwd().joinpath("test.txt")
# create file if it not exists
file_path = File.touch(touch_file_path)
# if file_path is not empty, it means you created the file successful.
```


## Donate

If you think these tools are pretty good, Can you please have a cup of coffee?  

![Pay-Total](./Pay-Total.png)  


## Contact

```
WeChat: yuyangiit
Mail: 845262968@qq.com
```