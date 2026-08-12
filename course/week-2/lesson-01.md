# 第 7 课：Python 环境与最小纵向切片

## 借鉴并融合

借鉴 [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) 中“小而完整应用”的学习价值：先让一条数据从输入走到输出，再扩充功能。本项目不复制示例代码，而是实现自己的论文周报纵向切片。

## 本课产物

建立 Python 项目骨架，并用 3 篇本地假论文生成一份 Markdown 周报；本课不调用网络和大模型。

建议结构：

```text
src/paper_weekly/     核心代码
tests/                自动测试
data/samples/         可公开的少量样例
reports/              生成结果
pyproject.toml        项目和依赖配置
.env.example          只写变量名，不写真实密钥
```

## 实践任务

1. 创建 `.venv` 并激活。
2. 建立 `pyproject.toml`，安装项目的开发模式。
3. 定义一篇论文最少包含：`id`、`title`、`authors`、`abstract`、`published_at`、`url`。
4. 写一个本地样例加载器和 Markdown 渲染器。
5. 运行一个入口，将 3 篇样例写入 `reports/sample-weekly.md`。

## 验收

- [ ] 新终端根据 README 能重新创建环境。
- [ ] 不联网、不配置密钥也能生成样例报告。
- [ ] 生成物包含标题、作者、摘要和原文链接。
- [ ] 核心逻辑位于 `src/`，不是全堆在一个脚本里。

解释题：为什么先做离线纵向切片，反而会让后续接 API 和大模型更快？
