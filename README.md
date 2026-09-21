# python-utils

> 一套轻量、零依赖的 Python 常用工具函数，主打「复制即用」。

## 安装
    pip install git+https://github.com/c991china/python-utils.git

或在项目里作为 git 子树 / 子模块引入。

## 模块
- `python_utils.fs`：文件系统助手
  - `tree(root)` 打印目录树
  - `read_text(path)` / `write_text(path, text)`
  - `iter_files(root, ext=None)` 递归遍历文件

## 快速试用
    python examples/demo.py

## 生态联动
- 种子项目 **[@22178384/project-seed](https://github.com/22178384/project-seed)** 直接依赖本库——装好它，`project-seed` 才能跑起来。
- 更多脚本片段见 [@c991china/dev-snippets](https://github.com/c991china/dev-snippets)。
