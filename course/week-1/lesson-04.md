# 第 4 课：GitHub、远程仓库与第一次上传

## 本课产物

在 GitHub 创建一个空仓库，将本地 `main` 分支上传，并能从网页看到提交历史。

## 上传前检查

```powershell
git status
git log --oneline -3
git remote -v
```

不要上传 `.env`、API Key、密码、数据集或大体积生成文件。发现敏感信息时先停止，不要认为“删掉再提交”就一定安全，因为旧提交仍可能保存它。

## GitHub 操作

1. 在 GitHub 新建仓库，例如 `ai-paper-weekly-learning`。
2. 因为本地已有内容，创建时不要额外初始化 README、`.gitignore` 或 License。
3. 复制 GitHub 提供的远程地址。
4. 配置并核对远程：

```powershell
git remote add origin 你的远程地址
git remote -v
git push -u origin main
```

若 `origin` 已存在，先用 `git remote get-url origin` 核对，不要盲目覆盖。

## 闯关与验收

- [ ] GitHub 首页能看到本仓库 README。
- [ ] GitHub 的最新提交编号与 `git rev-parse --short HEAD` 一致。
- [ ] `git status` 显示本地分支与远程同步。
- [ ] 仓库中没有密钥或 `.env`。

提交给老师：GitHub 仓库链接、`git remote -v`（可隐藏用户名之外的敏感部分）以及本地/远程提交编号。
