# Codex 云端环境配置

本说明用于 Codex Cloud。GitHub Codespaces 的开发容器配置另见 `cloud-setup.md`；两者的环境需要分别实际创建和验收。

## 连接与选择仓库

1. 在“创建云端环境”窗口确认 GitHub 账号为 `www123yu`。
2. 选择 `www123yu/yu` 仓库和 `main` 分支，点击“开始设置”（Get started）。
3. 若仓库列表没有更新，先刷新，并检查 GitHub 应用是否获得该仓库的访问权限。

## 可直接交给环境设置助手的说明

```text
请为这个电力电子科研仓库配置 Python 3.12 云端环境。

安装 requirements-dev.txt；需要 Notebook 时再安装 requirements-notebooks.txt。
默认安装 NumPy、SciPy、Matplotlib、Pandas、SymPy、python-control 和 Ruff。

安装完成后实际执行并报告：
python -m pip check
python -m ruff check .
python examples/check_environment.py

环境用于数值分析、控制设计、符号推导、绘图与数据处理。
MATLAB/Simulink、PLECS、LTspice 当前只管理源模型；如要运行，先确认软件安装、
操作系统和许可证，不把理想 Buck 的代数检查描述成开关仿真。

不启动 Web 服务，不设置外部端口，不加入账号口令或许可证。
请记录实际安装的 Python 和依赖版本，并指出任何尚未完成的检查。
```

若界面需要安装命令，并且 Python 3.12 已准备好，可使用：

```bash
python -m pip install -r requirements-dev.txt
python -m pip check
python -m ruff check .
python examples/check_environment.py
```

安装依赖时应允许连接所需 Python 包索引和文件下载站点；任务运行期间的外网范围按实际研究需求配置。

## 验收

查看环境设置报告，确认三项检查实际通过、没有缺失访问或未完成安装；保存配置并发布环境。出现发布完成提示后，再从该环境启动研究任务。

仓库里的 `.devcontainer/devcontainer.json` 为 Codespaces 定义环境，不能单凭该文件就认定 Codex Cloud 已配置。GitHub Actions 也需要在仓库中实际运行后验收。

参考 [OpenAI 官方云端环境说明](https://learn.chatgpt.com/docs/environments/cloud-environments)。
