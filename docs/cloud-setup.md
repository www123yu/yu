# GitHub 云端配置指南

## 1. 账号与仓库

本项目使用 [`www123yu/yu`](https://github.com/www123yu/yu)，主分支为 `main`。在 Codex 中选择仓库时，确认所连接 GitHub 账号为 `www123yu`。

若无法加载仓库，先核对已连接的用户名，再检查该 GitHub 应用是否获得本仓库访问权限。网页登录状态与已保存的应用授权账号需要分别确认。

## 2. 本地获取与提交

克隆现有仓库并进入目录：

```bash
git clone https://github.com/www123yu/yu.git
cd yu
```

先确认 Git 已配置自己的提交姓名与邮箱。按 README 安装 Python 环境，完成修改后执行检查，再提交和推送：

```bash
python -m pip check
python -m ruff check .
python examples/check_environment.py
git add .
git status --short
git commit -m "Describe the research change"
git push
```

首次推送按 Git 的登录提示完成 GitHub 授权。提交前检查 `git status --short`，确认没有账号凭据、许可证、未获授权的数据或第三方商业模型。

## 3. 云端开发与自动检查验收

1. 在仓库的 `Code → Codespaces` 下创建 `main` 的云端环境。`.devcontainer/devcontainer.json` 会定义 Python 环境及安装步骤；参见 [开发容器说明](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers)。
2. 安装结束后，在云端终端执行 README 的三个检查命令，确认退出码均为 0。配置文件修改后，重建容器使修改生效。
3. 打开 `Actions`，确认首次提交触发的检查通过。若页面要求启用 Actions，按页面提示启用后，从该工作流运行 `Run workflow`。
4. 提交一份实际模型或分析脚本，再运行对应的科研验证。当前环境检查不会运行任何商业仿真器。
5. 按账户页面核对 Codespaces 和 Actions 的用量与预算，并在使用结束后停止不再需要的 Codespace。创建方法见 [Codespaces 快速开始](https://docs.github.com/en/codespaces/quickstart)。

本地静态检查通过不能替代一次真实的 Codespaces 创建和 Actions 运行。只有两者均验收后，才可记为“云端配置完成”。

## 4. 模型、大文件与数据

`.slx` 等二进制模型按二进制管理，不做文本合并。小模型可先正常入库；频繁修改的二进制模型和大文件可按项目实际情况启用 Git LFS。LFS 不自动安装、不预设配额或计费安排；GitHub 对普通文件及 LFS 文件有不同的限制，添加前查阅 [Git LFS 说明](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage)。

若明确决定用 LFS 管理后续加入的 `.slx` 模型，先安装 Git LFS，再执行：

```bash
git lfs install
git lfs track "*.slx"
git add .gitattributes
```

这不会迁移旧历史。若模型已进仓库且需要迁移，应另行规划迁移和协作者同步。

保留仿真源文件、初始化和参数脚本；缓存和可重新生成的波形通常不提交。原始实验数据与处理后数据分开，保留单位、仪器/软件版本、采样频率、工况、处理步骤、来源及校验值。需要发布的数据集可使用正式数据存储服务，并在仓库记录 DOI 或稳定链接。

正式研究运行后，可保存完整 Python 包清单：

```bash
python -m pip freeze > results/python-environment.txt
```

与结果一起另存系统、Python 版本和 Git 提交 ID；该清单针对实际操作系统，不承诺跨平台二进制环境一致。

## 5. 商业仿真器的后续配置

MATLAB / Simulink、PLECS、LTspice 在本模板中提供文件管理结构。它们没有因为存在于 GitHub 仓库就自动获得云端安装、许可证或执行能力。

需要 MATLAB / Simulink 自动化时，可进一步选用 [MathWorks 的 GitHub Actions 集成](https://www.mathworks.com/help/matlab/matlab_external/use-matlab-with-github-actions.html)，再按所用产品、仓库可见性、支持范围和许可证配置。PLECS / LTspice 则需针对所用版本确认安装与批处理接口；也可以选择已安装并有使用权限的自托管运行器。

后续添加仿真工作流时，明确记录执行软件版本、许可方式、模型输入、求解配置、预期指标与容差。不要在缺少仿真器或许可证的情况下，把代数检查或示例输出描述成完整仿真验证。
