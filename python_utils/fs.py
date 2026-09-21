"""文件系统助手：目录树、文本读写、递归遍历。"""
from __future__ import annotations

import os
from typing import Iterator, Optional


def tree(root: str, max_depth: int = 3) -> str:
    """返回 root 的目录树字符串（类似 `tree` 命令）。"""
    lines: list[str] = [root]
    _walk(root, "", 0, max_depth, lines)
    return "\n".join(lines)


def _walk(path: str, prefix: str, depth: int, max_depth: int, out: list[str]) -> None:
    if depth >= max_depth:
        return
    try:
        entries = sorted(os.listdir(path))
    except PermissionError:
        return
    for i, name in enumerate(entries):
        last = i == len(entries) - 1
        connector = "└── " if last else "├── "
        full = os.path.join(path, name)
        out.append(f"{prefix}{connector}{name}")
        if os.path.isdir(full):
            extension = "    " if last else "│   "
            _walk(full, prefix + extension, depth + 1, max_depth, out)


def read_text(path: str, encoding: str = "utf-8") -> str:
    """读取文本文件全部内容。"""
    with open(path, "r", encoding=encoding) as fh:
        return fh.read()


def write_text(path: str, text: str, encoding: str = "utf-8") -> None:
    """写入文本文件（自动建父目录）。"""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding=encoding) as fh:
        fh.write(text)


def iter_files(root: str, ext: Optional[str] = None) -> Iterator[str]:
    """递归产出 root 下的文件路径；ext 可过滤后缀（含点，如 '.py'）。"""
    for dirpath, _dirs, files in os.walk(root):
        for name in files:
            if ext is None or name.endswith(ext):
                yield os.path.join(dirpath, name)
