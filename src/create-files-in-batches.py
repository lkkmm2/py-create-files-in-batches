# -*- coding: utf-8 -*-
"""
====================================================================
一键创建标准项目结构
====================================================================

【使用步骤】
    1. 修改下面的【用户配置区】：
        ① PARENT_DIR   —— 项目存放在哪个目录（父目录）
        ② PROJECT_NAME —— 项目文件夹的名字
    2. 直接运行本脚本（python create_project.py 或点运行按钮）
    3. 到 PARENT_DIR 目录下就能看到创建好的项目结构

【说明】
    - 脚本只创建文件/目录，不会覆盖已有文件的内容
    - Windows 路径请用 r"..." 或 "D:/..." 的写法
    - 想改项目结构，只需要修改 sub_dirs 和 files_content 两个变量
====================================================================
"""

from pathlib import Path
import os
import json


# ==================================================================
# ★★★★★★★★★★★★★★  【用户配置区】  ★★★★★★★★★★★★★★
# ==================================================================
# 只需要改下面这两处，其他地方都不用动
# ==================================================================

# ------------------------------------------------------------------
# ① 【指定项目存放位置】—— 改这里！
# ------------------------------------------------------------------
# 项目会在这个目录下创建。
#
# 常用写法示例：
#   Windows 某个盘：     PARENT_DIR = r"D:\projects"
#   Windows 用正斜杠：   PARENT_DIR = "D:/projects"
#   macOS / Linux：      PARENT_DIR = "/home/yourname/projects"
#   家目录（~ 表示）：   PARENT_DIR = "~/projects"
#   当前脚本所在目录：   PARENT_DIR = "."
#
# ★ 注意：Windows 路径前面一定要加 r，避免 \ 被当作转义字符
# ------------------------------------------------------------------
PARENT_DIR = r"D:\xiangmu"          # <<< 改这里：项目存放位置


# ------------------------------------------------------------------
# ② 【指定项目名称】—— 改这里！
# ------------------------------------------------------------------
# 会在 PARENT_DIR 下创建名为 PROJECT_NAME 的文件夹。
#
# 建议命名：
#   - 使用英文、数字、下划线、短横线
#   - 不要用中文或空格，避免后续 import 出问题
#
# 例如：
#   "fruit-image-classification"
#   "cat_vs_dog"
#   "my_project"
# ------------------------------------------------------------------
PROJECT_NAME = "project-python-关于完整创建完整的项目流程"   # <<< 改这里：项目名称

# ==================================================================
# ★★★★★★★★★★  【用户配置区】结束，以下不用改】  ★★★★★★★★★★
# ==================================================================


def create_project(parent_dir: str, project_name: str) -> Path:
    """
    在指定父目录下，创建一个标准项目结构。

    参数:
        parent_dir   : 父目录路径（字符串），例如 "D:/projects" 或 "."
        project_name : 项目文件夹名（字符串）

    返回:
        项目根目录的 Path 对象
    """

    # ============================================================
    # 步骤 1：确定并创建项目根目录
    # ============================================================
    # expanduser() ：支持 "~/xxx" 这种家目录写法
    # resolve()    ：转为绝对路径，方便打印和后续定位
    # mkdir        ：parents=True 表示父目录也会自动创建
    #                exist_ok=True 表示目录已存在也不报错
    # ============================================================
    root = Path(parent_dir).expanduser().resolve() / project_name
    root.mkdir(parents=True, exist_ok=True)
    print(f"[1/3] 已创建项目根目录：{root}")

    # ============================================================
    # 步骤 2：创建所有子目录
    # ============================================================
    # 想增删目录，就修改下面这个列表即可。
    # 例如要再加一个 "tests" 目录，就在列表末尾加一行 "tests",
    # ============================================================
    sub_dirs = [
        "configs",              # 配置文件目录（config.yaml）
        "data/raw",             # 原始数据（不上传 Git）
        "data/processed",       # 处理后的数据（不上传 Git）
        "data/sample",          # 少量示例数据（可上传）
        "src",                  # 源代码目录
        "notebooks",            # Jupyter 实验笔记
        "weights",              # 模型权重（不上传 Git）
        "outputs/logs",         # 训练日志输出
        "outputs/figures",      # 训练图表输出
        "images",               # README 用到的图片
        "scripts",              # 辅助脚本（shell 等）
    ]

    for d in sub_dirs:
        # 每个子目录都用 parents=True，确保多级目录也能一次创建
        (root / d).mkdir(parents=True, exist_ok=True)

    print(f"[2/3] 已创建 {len(sub_dirs)} 个子目录")

    # ============================================================
    # 步骤 3：创建文件并写入初始内容
    # ============================================================
    # 字典结构：
    #   键 = 相对于项目根目录的文件路径
    #   值 = 写入该文件的内容（"" 表示创建空文件）
    #
    # 想增删文件或修改初始内容，直接改这个字典即可。
    # ============================================================
    files_content = {

        # ---------- 根目录下的文件 ----------
        ".gitignore": (
            "# ---------- 数据（不上传） ----------\n"
            "data/raw/\n"
            "data/processed/\n"
            "weights/*.pth\n"
            "outputs/\n"
            "\n"
            "# ---------- Python 缓存 ----------\n"
            "__pycache__/\n"
            "*.py[cod]\n"
            ".venv/\n"
            "venv/\n"
            ".env\n"
            "\n"
            "# ---------- IDE ----------\n"
            ".idea/\n"
            ".vscode/\n"
        ),
        "README.md": (
            "# Project\n\n"
            "## 简介\n"
            "在这里写项目简介。\n\n"
            "## 目录结构\n"
            "见项目根目录下的说明。\n"
        ),
        "requirements.txt": (
            "# 依赖库列表，例如：\n"
            "# torch==2.2.0\n"
            "# torchvision==0.17.0\n"
            "# numpy\n"
            "# pandas\n"
            "# pyyaml\n"
        ),
        # LICENSE 默认为空文件，可自行粘贴 MIT / Apache 等协议文本
        "LICENSE": "",

        # ---------- configs/ ----------
        "configs/config.yaml": (
            "# 超参数与路径配置示例\n"
            "seed: 42\n"
            "batch_size: 32\n"
            "epochs: 20\n"
            "lr: 0.001\n"
            "data_dir: data/raw\n"
            "output_dir: outputs\n"
        ),

        # ---------- src/ ----------
        "src/__init__.py": "",   # 空文件，让 src 变成 Python 包
        "src/dataset.py": '"""数据加载模块：定义 Dataset / DataLoader。"""\n',
        "src/model.py":   '"""模型定义模块：定义网络结构。"""\n',
        "src/train.py":   '"""训练脚本：模型训练入口。"""\n',
        "src/predict.py": '"""推理脚本：加载权重并预测。"""\n',
        "src/utils.py":   '"""工具函数：日志、随机种子、指标等。"""\n',

        # ---------- notebooks/ ----------
        # 写入一个最小的合法 .ipynb，可直接用 Jupyter 打开
        "notebooks/01_eda.ipynb": json.dumps(
            {
                "cells": [],
                "metadata": {},
                "nbformat": 4,
                "nbformat_minor": 5,
            },
            indent=1,
        ),

        # ---------- weights/ ----------
        # 占位文件，训练完成后会用真实权重替换
        "weights/best_model.pth": "",

        # ---------- images/ ----------
        # 占位文件，README 用到时用真实图片覆盖
        "images/sample.png": "",
        "images/result.png": "",

        # ---------- scripts/ ----------
        "scripts/download_data.sh": (
            "#!/usr/bin/env bash\n"
            "# 下载数据脚本示例：\n"
            "# wget <数据下载地址> -P data/raw/\n"
        ),
    }

    # 遍历字典，逐个创建文件
    for rel_path, content in files_content.items():
        path = root / rel_path

        # 保险起见，再次确保父目录存在（例如 src、configs 等）
        path.parent.mkdir(parents=True, exist_ok=True)

        # 已存在的文件不覆盖，避免误删你的内容
        if not path.exists():
            path.write_text(content, encoding="utf-8")

    print(f"[3/3] 已创建 {len(files_content)} 个文件")

    # ============================================================
    # 额外处理：给 shell 脚本加可执行权限
    # ============================================================
    # Linux / macOS 需要执行权限，Windows 没有这个概念，跳过
    # ============================================================
    sh_path = root / "scripts" / "download_data.sh"
    if os.name != "nt":        # nt 表示 Windows
        os.chmod(sh_path, 0o755)

    return root


# ==================================================================
# 主程序入口
# ==================================================================
if __name__ == "__main__":
    # 按【用户配置区】里的配置创建项目
    project_path = create_project(PARENT_DIR, PROJECT_NAME)

    print("-" * 60)
    print(f"项目创建完成：{project_path}")
    print("后续可以在终端执行：")
    print(f'    cd "{project_path}"')
    print("    git init")
    print("    pip install -r requirements.txt")