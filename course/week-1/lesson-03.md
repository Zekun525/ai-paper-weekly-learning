# 第 3 课：查看历史、比较与安全撤销

## 本课产物

制造一次小改动，分别观察未暂存、已暂存和已提交差异，再安全撤销实验改动。

## 四个问题对应四类命令

| 想知道什么 | 命令 |
|---|---|
| 哪些文件变了 | `git status` |
| 工作区比暂存区多了什么 | `git diff` |
| 暂存区比上次提交多了什么 | `git diff --staged` |
| 历史发生过什么 | `git log --oneline --graph --decorate` |

## 实验

1. 在 `course/glossary.md` 填写一个概念。
2. 依次运行 `git status`、`git diff`。
3. 暂存该文件，再运行 `git diff` 和 `git diff --staged`。
4. 使用 `git restore --staged course/glossary.md` 取消暂存。
5. 确认内容仍在工作区后重新暂存并提交。

安全撤销规则：

- 取消暂存：`git restore --staged 文件`
- 丢弃未提交内容：`git restore 文件`，执行前必须确认内容不再需要
- 撤销已共享提交：优先 `git revert 提交编号`

本课程不使用 `git reset --hard` 作为日常撤销方法。

## 闯关与验收

- [ ] 能从三种 diff 中选对一个回答问题。
- [ ] 完成一次取消暂存但保留内容的操作。
- [ ] 能解释为什么共享历史更适合 `revert`。

提交给老师：一次状态变化记录，以及“我想撤销什么、为什么选择这个命令”的说明。
