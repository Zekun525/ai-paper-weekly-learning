# 第 5 课：分支、Pull Request 与小步审查

## 本课产物

使用功能分支修改学习文档，通过 Pull Request 合并回 `main`。

高质量开源项目把改动拆成可审查的小单元。本课借鉴的不是某个框架代码，而是高星 GitHub 项目普遍采用的协作方法：一项任务、一个分支、一个清晰 PR。

## 实践

```powershell
git switch -c docs/add-learning-goal
```

在 README 中补充一条你自己的学习目标，然后：

```powershell
git diff
git add README.md
git commit -m "docs: add personal learning goal"
git push -u origin docs/add-learning-goal
```

在 GitHub 创建 PR。描述必须包含：

- 为什么改；
- 改了什么；
- 如何验证；
- 是否有暂未解决的问题。

审查 diff 后合并，再同步本地：

```powershell
git switch main
git pull --ff-only
git log --oneline --graph --decorate -6
```

## 闯关与验收

- [ ] PR 只解决一个问题。
- [ ] PR 中没有无关文件。
- [ ] 描述包含验证证据。
- [ ] 合并后本地 `main` 与 GitHub 一致。

提交给老师：PR 链接，并解释“为什么不直接在 main 上一直改”。
