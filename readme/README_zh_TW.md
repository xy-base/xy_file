<!--
 * @Author: yuyanget 845262968@qq.com
 * @Date: 2024-10-18 20:12:00
 * @LastEditors: yuyanget 845262968@qq.com
 * @LastEditTime: 2024-10-18 20:18:30
 * @FilePath: /xy_file/readme/README_zh_TW.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# xy_file

- [简体中文](README_zh_CN.md)
- [繁体中文](README_zh_TW.md)
- [English](README_en.md)

## 說明
簡單檔操作工具，特殊功能為不同路徑匹配規則的添加。

## 程式碼庫

- <a href="https://github.com/xy-base/xy_file.git" target="_blank">Github位址</a>  
- <a href="https://gitee.com/xy-base/xy_file.git" target="_blank">Gitee位址</a>

## 安裝

```bash
pip install xy_file
```

## 使用

###### 1. 命令行
```bash
# 刪除目前的目錄下所有 py 文稿檔
xy_file -w clean -g "*.py"

```

###### 2. python腳本

```python
from xy_file.File import File
from pathlib import Path

touch_file_path = Path.cwd().joinpath("test.txt")
# 創建檔案當該檔案路徑為空
file_path = File.touch(touch_file_path)
# 如果file_path不為空 說明創建空檔成功
```

## 捐贈

如果小夥伴們覺得這些工具還不錯的話，能否請咱喝一杯咖啡呢?  

![Pay-Total](./Pay-Total.png)

## 聯繫方式

```
微信: yuyangiit
郵箱: 845262968@qq.com
```