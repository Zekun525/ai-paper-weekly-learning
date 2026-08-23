# AI 工程学习仓库

这是一个从 Git/GitHub 基础出发，逐步完成真实 AI 项目的学习仓库。

最终作品：**语义通信最新论文自动周报**。它会采集论文、生成摘要与周报，并通过自动化流程定期发布。

## 从这里开始

1. 阅读 [课程说明](course/README.md)。
2. 按 [使用手册](course/HOW-TO-USE.md) 建立每课的学习与验收节奏。
3. 从 [第 1 课：终端、路径与 Git 仓库](course/week-1/lesson-01.md) 开始。
4. 用 [完整路线与产物地图](course/roadmap.md) 理解每周会做出什么。
5. 在 [学习进度](course/progress.md) 中记录已通过验收的内容。
6. 遇到问题时，把排查过程写入 [错误手册](course/error-log.md)。

> 当前处于初始阶段。请按课程顺序实践，不要因为加入了参考项目就提前复制或运行大型框架。

## 仓库内容

| 目录或文件 | 用途 |
|---|---|
| `course/` | 四周课程、练习和学习记录 |
| `course/HOW-TO-USE.md` | 从第一天开始学习、求助和验收的方法 |
| `course/roadmap.md` | 18 课依赖关系、参考项目融合点和每周产物 |
| `course/resources/ai-agent-projects.md` | 与本项目匹配的高 Star AI Agent 项目导读 |
| `course/resources/project-study-template.md` | 阅读开源项目时使用的学习卡模板 |

## 四周路线

- 第 1 周：终端、Git、GitHub、分支、Pull Request 和冲突。
- 第 2 周：Python、HTTP/API、arXiv 论文采集和自动测试。
- 第 3 周：大模型、RAG、摘要生成和静态网页。
- 第 4 周：GitHub Actions、Secrets、定时发布和项目展示。

## 学习目标

- 学会用 Git 和 GitHub 管理真实项目，并使用RAG技术搭建一个 AI 论文周报工具。

## 快速开始

1. 创建虚拟环境并激活。
2. 安装项目到开发模式。
3. 运行样例周报。
4. 运行测试。

```powershell
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
python -m pip install -e .
python -m pip install pytest
paper-weekly
python -m pytest -q

## 开源项目学习原则

- 先理解问题和架构，再运行代码。
- 优先阅读与当前课程阶段直接相关的最小示例。
- 不把其他仓库的源码直接复制进来；自己实现后注明参考来源。
- 使用代码前检查许可证、依赖、安全风险和所需密钥。
- Star 是社区关注度信号，不等于代码质量或适合初学者。

这些项目的优秀部分已被拆进具体课程，不需要你自己猜该学什么。完整融合关系见 [学习路线](course/roadmap.md)，项目原始背景见 [AI Agent 高星项目导读](course/resources/ai-agent-projects.md)。
