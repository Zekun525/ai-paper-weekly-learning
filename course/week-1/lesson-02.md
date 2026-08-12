# 第 2 课：工作区、暂存区与第一次提交

## 本课产物

完成一次只包含预期文件的提交，并能解释工作区、暂存区和仓库历史的区别。

## 核心概念

- **工作区**：你正在编辑的文件。
- **暂存区**：下一次提交准备包含的快照。
- **提交**：写入 Git 历史、带有说明和唯一编号的快照。

`git add` 不是上传，`git commit` 也不是上传。上传到 GitHub 要等远程仓库配置完成后使用 `git push`。

## 先预测

1. 修改文件但不执行 `git add`，它会进入下一次提交吗？
2. `git add` 后再次修改同一文件，提交包含哪一版？
3. `git commit` 成功后，GitHub 会自动出现内容吗？

## 跟做

逐条运行并观察状态变化：

```powershell
git status
git diff
git add README.md course
git diff --staged
git status
git commit -m "docs: build AI engineering learning roadmap"
git status
```

提交前必须阅读 `git diff --staged`。如果暂存了不想提交的文件，使用：

```powershell
git restore --staged 文件路径
```

## 闯关与验收

- [ ] `git status` 显示工作区干净。
- [ ] `git log -1 --oneline` 能看到刚才的提交。
- [ ] 能用自己的话解释为什么暂存区让提交更可控。

提交给老师：三道预测答案、提交前的 `git diff --staged --stat`、提交后的 `git status` 和一句原理解释。
