# -*- coding: UTF-8 -*-
__author__ = "余洋"
__doc__ = "Rename"
"""
  * @File    :   Rename.py
  * @Time    :   2024/11/06 20:15:37
  * @Author  :   余洋
  * @Version :   0.0.1
  * @Contact :   yuyangit.0515@qq.com
  * @License :   (C)Copyright 2019-2024, 希洋 (Ship of Ocean)
  * @Desc    :   
"""
import re
from typing import Any, Callable, List
from pathlib import Path


class Rename:

    def rename(
        self,
        file_path: Path | str | None = None,
        source_pattern: str | None = None,
        target_pattern: str | Callable[[Any], str] | None = None,
        deep_start: int = -1,  # 0 => 绝对路径所有, -1 => 最后文件名.
        deep_count: int = 1,  # -1 => 递归所有, 0 => 仅当前, 1 => 当前+1级, 2 => 当前+2级, ...
        count: int = 0,  # 匹配次数
    ) -> Path | None:
        if file_path is None or source_pattern is None or target_pattern is None:
            return None
        file_path_parts = None
        if isinstance(file_path, str):
            file_path = Path(file_path)
        if deep_start == 0:
            file_path_parts = file_path.parts
        elif deep_start == -1:
            file_path_parts = file_path.parts[-1:]
        else:
            file_path_parts = file_path.parts[deep_start : deep_start + deep_count]
        if len(file_path_parts) > 0:
            file_path = "/".join(file_path_parts)
            if file_path_parts[0] == "/":
                file_path = file_path[1:]
        result = re.sub(source_pattern, target_pattern, file_path, count=count)
        if result is None:
            return None
        return Path(result)
