"""python-utils 演示。"""
from python_utils import tree, read_text, write_text, iter_files
import os
import tempfile


def main():
    d = tempfile.mkdtemp(prefix="pu_demo_")
    write_text(os.path.join(d, "a.txt"), "hello")
    os.makedirs(os.path.join(d, "sub"))
    write_text(os.path.join(d, "sub", "b.md"), "# hi")
    print(tree(d))
    files = list(iter_files(d))
    print("\n全部文件：", files)
    print("读取 a.txt ->", read_text(os.path.join(d, "a.txt")))


if __name__ == "__main__":
    main()
