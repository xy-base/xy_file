# -*- coding: UTF-8 -*-
__author__ = "余洋"
__doc__ = "Manager"
"""
  * @File    :   Manager.py
  * @Time    :   2024/11/06 20:24:27
  * @Author  :   余洋
  * @Version :   0.0.1
  * @Contact :   yuyangit.0515@qq.com
  * @License :   (C)Copyright 2019-2024, 希洋 (Ship of Ocean)
  * @Desc    :   
"""
from pathlib import Path
import os
import shutil
from typing import Callable, Any
from xy_console.utils import *

from .types import FileType
from .Operation.Rename import Rename
from .Operation.Search import Search


class Manager:

    def rglob_clean(
        self,
        keyword: str | None = None,
        work_dir: Path = Path.cwd(),
        file_type: FileType = FileType.ANY,
        ignore_hidden_files: bool = True,
        log_info=printt,
        log_error=print_e,
        log_success=print_s,
        should_delete_delegate: Callable[[list[Path]], bool],
    ):
        if not log_info or not callable(log_info):
            log_info = printt
        if not log_error or not callable(log_error):
            log_error = printt
        if not log_success or not callable(log_success):
            log_success = printt

        if not os.access(work_dir, os.W_OK):  # type: ignore
            raise PermissionError(f"当前工作目录({work_dir})没有写入权限!!!")
        if not keyword:
            raise ValueError(
                "请传入关键字(-r)的参数进行过滤, -r支持Linux文件名通配符搜索",
            )
        file_path_list = []
        invalidate_file_path_list = []
        search_result = (
            work_dir.rglob(keyword)
            if isinstance(keyword, str) and isinstance(work_dir, Path) and work_dir.exists()
            else []
        )
        if not search_result or not isinstance(search_result, list) or len(search_result) == 0:
            log_info("暂无匹配文件或目录")
            return
        file_path_list = []
        invalidate_file_path_list = []
        for work_glob in search_result:
            search: Search = Search()
            search.keyword = keyword
            search.work_dir = work_dir
            search.file_type = file_type
            search.ignore_hidden_files = ignore_hidden_files
            validated_path = search.validated_path(work_glob)
            if isinstance(validated_path, Path):
                file_verbose_name = FileType.verbose_name(validated_path)
                msg = f"将要删除... => [{file_verbose_name}] {validated_path}"
                log_info(msg)
                file_path_list.append(validated_path)
            else:
                invalidate_file_path_list.append(validated_path)
        if not file_path_list:
            log_info("暂无匹配文件或目录")
            return
        validate_delegate = should_delete_delegate != None and callable(should_delete_delegate)
        if validate_delegate:
            log_info(f"是否需要删除以上路径对应的文件或目录等, 共计: ( {len(file_path_list)} ) ==>")
        else:
            log_info("不进行删除...")
            return
        should_delete = validate_delegate and should_delete_delegate(file_path_list) == True
        if (should_delete == True):
            log_info("开始删除...")
            success_file_path_list = []
            fail_file_path_list = []
            for file_path in file_path_list:
                try:
                    file_verbose_name = FileType.verbose_name(file_path)
                    log_info(f"正在删除... => [{file_verbose_name}] {file_path} ")
                    if file_path.is_dir():
                        shutil.rmtree(file_path)
                    else:
                        file_path.unlink()
                    success_file_path_list.append(file_path)
                except:
                    fail_file_path_list.append(file_path)
            if not fail_file_path_list:
                log_success("全部删除完成 !!!")
            else:
                for file_path in fail_file_path_list:
                    file_verbose_name = FileType.verbose_name(file_path)
                    msg = f"还未删除... => [{file_verbose_name}] {file_path}"
                    log_error(msg)
                log_error(f"还剩下以上文件或目录未删除(共计: {len(fail_file_path_list) if isinstance(fail_file_path_list, list) else 0}): ==>")
                log_error("="*50)
        else:
            log_info("取消删除...")
    def match_clean(self,
        keyword: str | None = None,
        work_dir: Path = Path.cwd(),
        file_type: FileType = FileType.ANY,
        ignore_hidden_files: bool = True,
        log_info=printt,
        log_error=print_e,
        log_success=print_s,
        should_delete_delegate: Callable[[list[Path]], bool],
    ):
        if not log_info or not callable(log_info):
            log_info = printt
        if not log_error or not callable(log_error):
            log_error = printt
        if not log_success or not callable(log_success):
            log_success = printt

        if not os.access(work_dir, os.W_OK):  # type: ignore
            raise PermissionError(f"当前工作目录({work_dir})没有写入权限!!!")
        if not keyword:
            raise ValueError(
                "请传入关键字(-k)的参数进行过滤, -k支持正则表达式匹配符进行搜索",
            )
        file_path_list = []
        invalidate_file_path_list = []
        search_result = work_dir.rglob("**")
        file_path_list = []
        invalidate_file_path_list = []
        for work_glob in search_result:
            search: Search = Search()
            search.keyword = keyword
            search.work_dir = work_dir
            search.file_type = file_type
            search.ignore_hidden_files = ignore_hidden_files
            validated_path = search.validated_path(work_glob)
            if isinstance(validated_path, Path) and search.match(validated_path) == True:
                file_verbose_name = FileType.verbose_name(validated_path)
                msg = f"将要删除... => [{file_verbose_name}] {validated_path}"
                log_info(msg)
                file_path_list.append(validated_path)
            else:
                invalidate_file_path_list.append(validated_path)
        if not file_path_list:
            log_info("暂无匹配文件或目录")
            return
        validate_delegate = should_delete_delegate != None and callable(should_delete_delegate)
        if validate_delegate:
            log_info(f"是否需要删除以上路径对应的文件或目录等, 共计: ( {len(file_path_list)} ) ==>")
        else:
            log_info("不进行删除...")
            return
        should_delete = validate_delegate and should_delete_delegate(file_path_list) == True
        if (should_delete == True):
            log_info("开始删除...")
            success_file_path_list = []
            fail_file_path_list = []
            for file_path in file_path_list:
                try:
                    file_verbose_name = FileType.verbose_name(file_path)
                    log_info(f"正在删除... => [{file_verbose_name}] {file_path} ")
                    if file_path.is_dir():
                        shutil.rmtree(file_path)
                    else:
                        file_path.unlink()
                    success_file_path_list.append(file_path)
                except:
                    fail_file_path_list.append(file_path)
            if not fail_file_path_list:
                log_success("全部删除完成 !!!")
            else:
                for file_path in fail_file_path_list:
                    file_verbose_name = FileType.verbose_name(file_path)
                    msg = f"还未删除... => [{file_verbose_name}] {file_path}"
                    log_error(msg)
                log_error(f"还剩下以上文件或目录未删除(共计: {len(fail_file_path_list) if isinstance(fail_file_path_list, list) else 0}): ==>")
                log_error("="*50)
        else:
            log_info("取消删除...")
    def search_clean(
        self,
        keyword: str | None = None,
        work_dir: Path = Path.cwd(),
        file_type: FileType = FileType.ANY,
        ignore_hidden_files: bool = True,
        log_info=printt,
        log_error=print_e,
        log_success=print_s,
        should_delete_delegate: Callable[[list[Path]], bool],
    ):
        if not log_info or not callable(log_info):
            log_info = printt
        if not log_error or not callable(log_error):
            log_error = printt
        if not log_success or not callable(log_success):
            log_success = printt

        if not os.access(work_dir, os.W_OK):  # type: ignore
            raise PermissionError(f"当前工作目录({work_dir})没有写入权限!!!")
        if not keyword:
            raise ValueError(
                "请传入关键字(-k)的参数进行过滤, -k支持正则表达式匹配符进行搜索",
            )
        file_path_list = []
        invalidate_file_path_list = []
        search_result = work_dir.rglob("**")
        file_path_list = []
        invalidate_file_path_list = []
        for work_glob in search_result:
            search: Search = Search()
            search.keyword = keyword
            search.work_dir = work_dir
            search.file_type = file_type
            search.ignore_hidden_files = ignore_hidden_files
            validated_path = search.validated_path(work_glob)
            if isinstance(validated_path, Path) and search.search(validated_path) == True:
                file_verbose_name = FileType.verbose_name(validated_path)
                msg = f"将要删除... => [{file_verbose_name}] {validated_path}"
                log_info(msg)
                file_path_list.append(validated_path)
            else:
                invalidate_file_path_list.append(validated_path)
        if not file_path_list:
            log_info("暂无匹配文件或目录")
            return
        validate_delegate = should_delete_delegate != None and callable(should_delete_delegate)
        if validate_delegate:
            log_info(f"是否需要删除以上路径对应的文件或目录等, 共计: ( {len(file_path_list)} ) ==>")
        else:
            log_info("不进行删除...")
            return
        should_delete = validate_delegate and should_delete_delegate(file_path_list) == True
        if (should_delete == True):
            log_info("开始删除...")
            success_file_path_list = []
            fail_file_path_list = []
            for file_path in file_path_list:
                try:
                    file_verbose_name = FileType.verbose_name(file_path)
                    log_info(f"正在删除... => [{file_verbose_name}] {file_path} ")
                    if file_path.is_dir():
                        shutil.rmtree(file_path)
                    else:
                        file_path.unlink()
                    success_file_path_list.append(file_path)
                except:
                    fail_file_path_list.append(file_path)
            if not fail_file_path_list:
                log_success("全部删除完成 !!!")
            else:
                for file_path in fail_file_path_list:
                    file_verbose_name = FileType.verbose_name(file_path)
                    msg = f"还未删除... => [{file_verbose_name}] {file_path}"
                    log_error(msg)
                log_error(f"还剩下以上文件或目录未删除(共计: {len(fail_file_path_list) if isinstance(fail_file_path_list, list) else 0}): ==>")
                log_error("="*50)
        else:
            log_info("取消删除...")

    def rglob_files(self, keyword: str | None = None, work_dir: Path = Path.cwd(), file_type: FileType = FileType.ANY, ignore_hidden_files: bool = True, log_info=printt, log_error=print_e, log_success=print_s,):
        if not log_info or not callable(log_info):
            log_info = printt
        if not log_error or not callable(log_error):
            log_error = printt
        if not log_success or not callable(log_success):
            log_success = printt

        if not os.access(work_dir, os.W_OK):  # type: ignore
            raise PermissionError(f"当前工作目录({work_dir})没有写入权限!!!")
        if not keyword:
            raise ValueError(
                "请传入关键字(-r)的参数进行过滤, -r支持Linux文件名通配符搜索",
            )
        file_path_list = []
        search_result = (
            work_dir.rglob(keyword)
            if isinstance(keyword, str) and isinstance(work_dir, Path) and work_dir.exists()
            else []
        )
        if not search_result or not isinstance(search_result, list) or len(search_result) == 0:
            log_info("暂无匹配文件或目录")
            return
        file_path_list = []
        for work_glob in search_result:
            search: Search = Search()
            search.keyword = keyword
            search.work_dir = work_dir
            search.file_type = file_type
            search.ignore_hidden_files = ignore_hidden_files
            validated_path = search.validated_path(work_glob)
            if isinstance(validated_path, Path):
                file_verbose_name = FileType.verbose_name(validated_path)
                msg = f"查找到... => [{file_verbose_name}] {validated_path}"
                log_info(msg)
        if not file_path_list:
            log_info("暂无匹配文件或目录")
            return
        else:
            log_info("取消通配符匹配...")
    
    def search_files(
        self,
        keyword: str | None = None,
        work_dir: Path = Path.cwd(),
        file_type: FileType = FileType.ANY,
        ignore_hidden_files: bool = True,
        log_info=printt,
        log_error=print_e,
        log_success=print_s,
    ):
        if not log_info or not callable(log_info):
            log_info = printt
        if not log_error or not callable(log_error):
            log_error = printt
        if not log_success or not callable(log_success):
            log_success = printt

        if not os.access(work_dir, os.W_OK):  # type: ignore
            raise PermissionError(f"当前工作目录({work_dir})没有写入权限!!!")
        if not keyword:
            raise ValueError(
                "请传入关键字(-k)的参数进行过滤, -k支持正则表达式匹配符进行搜索",
            )
        file_path_list = []
        search_result = work_dir.rglob("**")
        file_path_list = []
        for work_glob in search_result:
            search: Search = Search()
            search.keyword = keyword
            search.work_dir = work_dir
            search.file_type = file_type
            search.ignore_hidden_files = ignore_hidden_files
            validated_path = search.validated_path(work_glob)
            if isinstance(validated_path, Path) and search.search(validated_path) == True:
                file_verbose_name = FileType.verbose_name(validated_path)
                msg = f"查找到... => [{file_verbose_name}] {validated_path}"
                log_info(msg)
                file_path_list.append(validated_path)
        if not file_path_list:
            log_info("暂无匹配文件或目录")
            return

    def rename_files(
        self,
        work_dir: Path,
        source_pattern: str | None = None,
        target_pattern: str | Callable[[Any], str] | None = None,
        deep_start: int = -1,  # 0 => 绝对路径所有, -1 => 最后文件名.
        deep_count: int = 1,  # -1 => 递归所有, 0 => 仅当前, 1 => 当前+1级, 2 => 当前+2级, ...
        count: int = 0,,
        file_type: FileType = FileType.ANY,
        ignore_hidden_files: bool = True,
        log_info=printt,
        log_error=print_e,
        log_success=print_s,
        should_delete_delegate: Callable[[list[Path]], bool],
    ):
        pass

    def touch_files(
        self,
    ):
        pass

    def quick_touch_files(self,):
        pass

    def random_touch_files(self,):
        pass