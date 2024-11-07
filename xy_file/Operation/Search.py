# -*- coding: UTF-8 -*-
__author__ = "余洋"
__doc__ = "Search"
"""
  * @File    :   Search.py
  * @Time    :   2024/11/06 20:15:24
  * @Author  :   余洋
  * @Version :   0.0.1
  * @Contact :   yuyangit.0515@qq.com
  * @License :   (C)Copyright 2019-2024, 希洋 (Ship of Ocean)
  * @Desc    :   
"""

import re
from pathlib import Path
from xy_file.types import FileType


class Search:
    file_type: FileType = FileType.ANY
    work_dir: Path = Path.cwd()
    keyword: str = ""
    ignore_hidden_files: bool = True
    regex_flag: re.RegexFlag = re.M

    def validated_path(self, path: Path) -> Path | None:
        path_validate = self.file_type.validate(path=path)
        hidden_file_part = [part for part in path.parts if part.startswith(".")]
        is_hidden_file = not hidden_file_part or len(hidden_file_part) == 0
        ok = path_validate and not (
            is_hidden_file and self.ignore_hidden_files == False
        )
        if ok and path.exists():
            return path
        else:
            return None

    def pattern(self) -> re.Pattern:
        return re.compile(
            self.keyword,
            flags=self.regex_flag,
        )

    def match(
        self,
        path: Path,
    ) -> bool:
        pattern = self.pattern()
        validated_path = self.validated_path(path)
        if isinstance(pattern, re.Pattern) and isinstance(validated_path, Path):
            results = pattern.match(path.as_posix())
            if results != None:
                return True
        return False

    def search(
        self,
        path: Path,
    ) -> bool:
        pattern = self.pattern()
        validated_path = self.validated_path(path)
        if isinstance(pattern, re.Pattern) and isinstance(validated_path, Path):
            results = pattern.search(path.as_posix())
            if results != None:
                return True
        return False
