# yu · 电力电子科研工作区

面向变换器、逆变器、控制环路及实验数据分析的科研仓库起点。Python 3.12 环境用于数值计算、控制分析、符号推导及数据处理；模型源文件按仿真软件分别管理。

GitHub 仓库：[`www123yu/yu`](https://github.com/www123yu/yu)。

## 开始使用

仓库上传 GitHub 后，打开 `Code → Codespaces → Create codespace on main`。开发容器会安装科研依赖和检查工具。终端可用后运行：

```bash
python -m pip check
python -m ruff check .
python examples/check_environment.py
```

环境检查仅验证安装及理想 Buck 的代数关系，不代表开关级仿真、控制稳定性验证或实验结果。云端环境尚需首次实际创建验证。

如需 Notebook，在终端安装可选依赖：

```bash
python -m pip install -r requirements-notebooks.txt
```

本地使用时，先安装 Python 3.12，创建并激活虚拟环境，再安装 `requirements-dev.txt`。激活命令：Windows PowerShell 为 `.\.venv\Scripts\Activate.ps1`，Linux/macOS 为 `source .venv/bin/activate`。

```bash
python -m venv .venv
# 激活虚拟环境后执行以下命令
python -m pip install -r requirements-dev.txt
```

## 文件放在哪里

| 路径 | 内容 |
| --- | --- |
| `models/simulink/` | MATLAB / Simulink / Simscape 模型与脚本 |
| `models/plecs/` | PLECS 模型、初始化和参数脚本 |
| `models/ltspice/` | LTspice 原理图、网表和自有器件模型 |
| `examples/` | 小型可运行示例与环境检查 |
| `data/` | 原始及处理后数据，见目录说明 |
| `results/` | 波形、图表、指标等运行产物，见目录说明 |
| `docs/` | 配置、复现与研究说明 |

提交模型时同时记录软件版本、依赖工具箱、拓扑、参数与单位、控制和采样周期、求解器设置、运行步骤及判据。参考结果应注明来源、工况与对应提交。

## 自动检查

`.github/workflows/checks.yml` 提供依赖一致性、Python 静态检查和环境示例检查。检查通过只说明这些项目通过；商业仿真器和硬件实验仍需单独运行、记录和核验。

开发容器默认未安装 MATLAB、Simulink、PLECS 或 LTspice。若要自动运行这些软件，需进一步确认操作系统支持、安装方式、许可证以及适合的托管或自托管运行器。

## 配置与复现

首次上传、Codespaces 验收、Git LFS 和商业仿真器说明见 [GitHub 云端配置指南](docs/cloud-setup.md)。在 Codex 中使用仓库见 [Codex 云端环境配置](docs/codex-cloud-setup.md)。根目录依赖文件固定直接依赖版本；进行正式研究时，另保存实际运行环境的完整依赖清单，并记录模型、数据和代码版本。

本模板未代选研究成果的开放许可证。发布源代码、论文附件或数据集前，由作者按实际权属选择许可证并注明第三方来源。
