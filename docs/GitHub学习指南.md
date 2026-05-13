# GitHub 学习指南：从理解到熟练使用

> 适合对象：刚开始学习 GitHub，希望系统掌握 GitHub 页面功能、核心概念、Git 基础命令，并能够用于个人学习项目和代码管理的初学者。

---

## 目录

1. [GitHub 是什么](#1-github-是什么)
2. [Git、GitHub、VSCode 的关系](#2-gitgithubvscode-的关系)
3. [GitHub 仓库页面功能介绍](#3-github-仓库页面功能介绍)
4. [GitHub 核心概念中英文对照](#4-github-核心概念中英文对照)
5. [Git 基础工作流](#5-git-基础工作流)
6. [Git 基础指令](#6-git-基础指令)
7. [分支开发与 Pull Request 工作流](#7-分支开发与-pull-request-工作流)
8. [常见问题与解决方法](#8-常见问题与解决方法)
9. [推荐学习路线](#9-推荐学习路线)
10. [机器学习项目中的 GitHub 使用建议](#10-机器学习项目中的-github-使用建议)

---

# 1. GitHub 是什么

GitHub 是一个基于 Git 的代码托管与协作平台。

简单理解：

> Git 负责版本管理，GitHub 负责把代码托管到云端，并支持协作、项目管理、版本发布和自动化流程。

GitHub 可以用于：

- 保存代码和文档
- 管理项目版本
- 多人协作开发
- 记录学习过程
- 展示个人项目
- 发布软件版本
- 使用 Issues 管理任务
- 使用 Pull Request 审查和合并代码
- 使用 GitHub Actions 自动化测试、构建和部署

对于个人学习者，GitHub 的价值不仅是“存代码”，更重要的是建立工程化思维：

> 让你的学习、代码、文档、实验过程都有清晰的版本记录和项目结构。

---

# 2. Git、GitHub、VSCode 的关系

## 2.1 Git 是什么

Git 是一个本地版本控制工具。

它可以记录一个项目从创建到修改的全过程。

例如你今天写了一个 `README.md`，明天修改了内容，后天又增加了代码，Git 都可以记录下来。

你可以理解为：

> Git = 项目的“历史记录系统”。

---

## 2.2 GitHub 是什么

GitHub 是一个远程代码托管平台。

它可以把你本地用 Git 管理的项目上传到云端。

你可以理解为：

> GitHub = 存放 Git 项目的云端平台。

---

## 2.3 VSCode 是什么

VSCode 是代码编辑器。

你可以在 VSCode 中写代码、写文档，也可以通过内置 Git 面板完成：

- 查看文件修改
- 提交 commit
- 推送到 GitHub
- 拉取远程更新
- 切换分支
- 解决冲突

---

## 2.4 三者关系

```text
VSCode：写代码、改文件
Git：记录代码修改历史
GitHub：把 Git 项目上传到云端，支持协作和展示
```

典型流程：

```text
本地写代码 → Git 记录修改 → Push 到 GitHub
```

---

# 3. GitHub 仓库页面功能介绍

进入一个 GitHub 仓库后，通常会看到以下菜单和功能。

---

## 3.1 Code

`Code` 是仓库的核心页面。

主要功能：

- 查看项目文件
- 查看 README 文档
- 切换分支或标签
- 下载代码
- 复制仓库地址
- 在线编辑文件
- 创建新文件

常见按钮：

| 英文 | 中文 | 作用 |
|---|---|---|
| Code | 代码 | 查看项目文件和复制仓库地址 |
| Add file | 添加文件 | 创建或上传文件 |
| Go to file | 跳转文件 | 快速搜索仓库中的文件 |
| Switch branches/tags | 切换分支/标签 | 切换不同分支或版本 |
| Clone | 克隆 | 复制仓库到本地 |
| Download ZIP | 下载 ZIP | 直接下载项目压缩包 |

---

## 3.2 Issues

`Issues` 是问题与任务管理区。

它可以用来记录：

- bug
- 待办事项
- 学习任务
- 功能需求
- 讨论问题

例如在机器学习学习项目中，可以创建：

```text
Issue: 完成线性回归章节
Issue: 补充 XGBoost 原理总结
Issue: 增加 PCA 示例代码
```

Issues 的价值是：

> 把项目中的问题和任务显式记录下来，而不是只靠记忆。

---

## 3.3 Pull requests

`Pull requests` 简称 PR，中文常译为“拉取请求”或“合并请求”。

它的作用是：

> 把一个分支中的修改申请合并到另一个分支。

常见场景：

```text
feature/xgboost → main
```

意思是：

> 把 feature/xgboost 分支中的内容合并进 main 主分支。

PR 通常用于：

- 代码审查
- 合并分支
- 多人协作
- 记录一次功能更新的完整过程

---

## 3.4 Actions

`Actions` 是 GitHub 的自动化工具。

它可以自动完成：

- 代码测试
- 项目构建
- 文档生成
- 自动部署
- 格式检查

例如：

```text
每次 push 后，自动运行 Python 测试
```

初学阶段可以先了解，不需要立即深入。

---

## 3.5 Projects

`Projects` 是 GitHub 的项目管理工具。

可以用看板方式管理任务，例如：

```text
To do → In progress → Done
```

适合用于：

- 学习计划管理
- 项目进度管理
- 多任务跟踪

---

## 3.6 Wiki

`Wiki` 是仓库的知识文档区。

适合放：

- 项目说明
- 技术文档
- 学习笔记
- 使用手册

对于个人学习项目，如果 README 和 notes 已经足够，可以暂时不用 Wiki。

---

## 3.7 Security

`Security` 用于安全相关管理。

包括：

- 安全漏洞提醒
- 依赖风险检测
- 密钥泄露提醒
- 安全策略

初学阶段了解即可。

---

## 3.8 Insights

`Insights` 是仓库数据统计页面。

可以看到：

- commit 统计
- 贡献者统计
- 代码频率
- 分支情况
- 流量情况

适合后期观察项目活跃度。

---

## 3.9 Settings

`Settings` 是仓库设置页面。

可以配置：

- 仓库名称
- 仓库描述
- 默认分支
- 权限
- Pages 部署
- Actions 设置
- 删除仓库

注意：

> 删除仓库是高风险操作，操作前一定要确认。

---

# 4. GitHub 核心概念中英文对照

## 4.1 基础概念

| 英文 | 中文 | 解释 |
|---|---|---|
| Repository / Repo | 仓库 | 一个 GitHub 项目，包含代码、文档、历史记录等 |
| Git | 版本控制工具 | 用于记录项目文件的修改历史 |
| GitHub | 代码托管平台 | 基于 Git 的云端协作平台 |
| Local | 本地 | 你电脑上的项目环境 |
| Remote | 远程 | GitHub 上的项目环境 |
| Clone | 克隆 | 把远程仓库复制到本地 |
| Fork | 派生 / 复刻 | 把别人的仓库复制到自己的账号下 |
| Star | 收藏 / 点星 | 表示关注或收藏某个项目 |
| Watch | 关注通知 | 接收仓库更新通知 |

---

## 4.2 版本管理概念

| 英文 | 中文 | 解释 |
|---|---|---|
| Commit | 提交 | 一次明确的版本记录 |
| Commit message | 提交信息 | 描述这次提交做了什么 |
| Branch | 分支 | 一条独立的开发线 |
| Main branch | 主分支 | 默认稳定分支，通常叫 main |
| Tag | 标签 | 给某个历史版本打标记，例如 v1.0 |
| Release | 发布版本 | 基于 tag 发布的软件版本 |
| History | 历史记录 | 项目所有提交记录 |

---

## 4.3 文件状态概念

| 英文 | 中文 | 解释 |
|---|---|---|
| Working directory | 工作区 | 当前正在编辑的文件区域 |
| Staging area / Index | 暂存区 | 准备提交的文件区域 |
| Repository | 本地仓库 | 已经形成 commit 记录的区域 |
| Modified | 已修改 | 文件被修改但还未暂存 |
| Staged | 已暂存 | 文件已加入下一次提交 |
| Committed | 已提交 | 文件修改已经形成版本记录 |
| Untracked | 未跟踪 | Git 还没有管理的新文件 |

---

## 4.4 协作概念

| 英文 | 中文 | 解释 |
|---|---|---|
| Pull Request / PR | 拉取请求 / 合并请求 | 请求把一个分支合并到另一个分支 |
| Merge | 合并 | 把一个分支的修改合并进另一个分支 |
| Conflict | 冲突 | 多个修改同时影响同一部分内容，需要人工处理 |
| Review | 审查 | 检查别人提交的代码或文档 |
| Issue | 问题 / 任务 | 用于记录 bug、需求、任务和讨论 |
| Assignee | 负责人 | 某个 issue 或 PR 的负责人员 |
| Label | 标签 | 给 issue 或 PR 分类 |
| Milestone | 里程碑 | 一组 issue 或 PR 的阶段性目标 |

---

## 4.5 常见缩写

| 缩写 | 全称 | 含义 |
|---|---|---|
| repo | repository | 仓库 |
| PR | Pull Request | 合并请求 |
| CI | Continuous Integration | 持续集成 |
| CD | Continuous Deployment / Delivery | 持续部署 / 持续交付 |
| CLI | Command Line Interface | 命令行工具 |
| GUI | Graphical User Interface | 图形界面工具 |

---

# 5. Git 基础工作流

Git 最核心的流程是：

```text
修改文件 → 暂存修改 → 提交版本 → 推送到 GitHub
```

对应命令：

```bash
git status
git add .
git commit -m "提交说明"
git push
```

完整理解如下：

```text
工作区 Working Directory
        ↓ git add
暂存区 Staging Area
        ↓ git commit
本地仓库 Local Repository
        ↓ git push
远程仓库 GitHub Remote Repository
```

---

# 6. Git 基础指令

## 6.1 查看 Git 版本

```bash
git --version
```

作用：

> 检查电脑是否安装了 Git。

---

## 6.2 配置用户名和邮箱

```bash
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"
```

作用：

> 设置 commit 记录中的作者信息。

查看配置：

```bash
git config --global --list
```

---

## 6.3 初始化本地仓库

```bash
git init
```

作用：

> 把当前文件夹变成 Git 仓库。

适合场景：

> 你已经在本地创建了项目文件夹，现在想让 Git 管理它。

---

## 6.4 克隆远程仓库

```bash
git clone 仓库地址
```

例如：

```bash
git clone https://github.com/yourname/ml-system-learning.git
```

作用：

> 把 GitHub 上的仓库复制到本地电脑。

---

## 6.5 查看当前状态

```bash
git status
```

作用：

> 查看哪些文件被修改、哪些文件已暂存、当前在哪个分支。

这是最常用的 Git 命令之一。

---

## 6.6 添加文件到暂存区

添加所有修改：

```bash
git add .
```

添加指定文件：

```bash
git add README.md
```

作用：

> 把修改放入暂存区，准备提交。

---

## 6.7 提交修改

```bash
git commit -m "提交说明"
```

例如：

```bash
git commit -m "add linear regression notes"
```

作用：

> 形成一次版本记录。

好的 commit message 应该简洁说明本次修改内容。

---

## 6.8 推送到 GitHub

```bash
git push
```

首次推送新分支时可能需要：

```bash
git push -u origin 分支名
```

例如：

```bash
git push -u origin main
```

作用：

> 把本地 commit 上传到 GitHub。

---

## 6.9 拉取远程更新

```bash
git pull
```

作用：

> 把 GitHub 上的最新修改拉取到本地。

常用场景：

> 在开始写代码前，先 pull 一下，确保本地是最新版本。

---

## 6.10 查看提交历史

```bash
git log
```

简洁查看：

```bash
git log --oneline
```

作用：

> 查看项目历史提交记录。

---

## 6.11 查看分支

```bash
git branch
```

查看本地和远程所有分支：

```bash
git branch -a
```

---

## 6.12 创建分支

```bash
git branch 分支名
```

例如：

```bash
git branch feature/xgboost
```

作用：

> 创建一条新的开发分支。

---

## 6.13 切换分支

推荐使用：

```bash
git switch 分支名
```

例如：

```bash
git switch main
git switch feature/xgboost
```

旧写法：

```bash
git checkout 分支名
```

---

## 6.14 创建并切换分支

推荐使用：

```bash
git switch -c 分支名
```

例如：

```bash
git switch -c feature/xgboost
```

旧写法：

```bash
git checkout -b feature/xgboost
```

---

## 6.15 合并分支

先切回目标分支：

```bash
git switch main
```

再合并其他分支：

```bash
git merge feature/xgboost
```

作用：

> 把 feature/xgboost 的修改合并到 main。

---

## 6.16 删除本地分支

```bash
git branch -d 分支名
```

例如：

```bash
git branch -d feature/xgboost
```

强制删除：

```bash
git branch -D 分支名
```

---

## 6.17 删除远程分支

```bash
git push origin --delete 分支名
```

例如：

```bash
git push origin --delete feature/xgboost
```

---

## 6.18 撤销未暂存的修改

```bash
git restore 文件名
```

例如：

```bash
git restore README.md
```

作用：

> 放弃某个文件在工作区中的修改。

注意：

> 这个操作会丢失未保存到 commit 的修改。

---

## 6.19 取消暂存

```bash
git restore --staged 文件名
```

例如：

```bash
git restore --staged README.md
```

作用：

> 把文件从暂存区移回工作区。

---

## 6.20 回退版本

```bash
git reset --soft commit_id
```

保留修改，只撤销 commit。

```bash
git reset --hard commit_id
```

彻底回退到某个版本，后续修改会丢失。

注意：

> `git reset --hard` 是高风险命令，新手谨慎使用。

---

## 6.21 安全撤销某次提交

```bash
git revert commit_id
```

作用：

> 生成一个新的 commit，用来抵消某次历史提交。

相比 `reset`，`revert` 更适合已经 push 到 GitHub 的提交。

---

## 6.22 临时保存修改

```bash
git stash
```

恢复保存的修改：

```bash
git stash pop
```

作用：

> 临时存放当前未提交的修改，方便切换分支或处理紧急任务。

---

# 7. 分支开发与 Pull Request 工作流

真实开发中，不建议直接在 `main` 分支上随意修改。

更推荐：

```text
main 保持稳定
新功能在 feature 分支开发
开发完成后通过 PR 合并回 main
```

---

## 7.1 标准流程

假设要新增 XGBoost 学习笔记。

### 第一步：从 main 创建新分支

```bash
git switch main
git pull
git switch -c feature/xgboost-notes
```

---

### 第二步：修改文件

例如新增：

```text
machine-learning/tree-models/xgboost.md
```

---

### 第三步：提交修改

```bash
git status
git add .
git commit -m "add xgboost notes"
```

---

### 第四步：推送分支到 GitHub

```bash
git push -u origin feature/xgboost-notes
```

---

### 第五步：在 GitHub 创建 Pull Request

进入 GitHub 仓库页面后，通常会看到：

```text
Compare & pull request
```

点击后：

```text
base: main
compare: feature/xgboost-notes
```

表示：

> 申请把 feature/xgboost-notes 合并进 main。

---

### 第六步：检查并合并 PR

确认内容无误后点击：

```text
Merge pull request
```

合并完成后，可以删除 feature 分支。

---

## 7.2 推荐分支命名

| 类型 | 示例 | 适用场景 |
|---|---|---|
| feature/xxx | feature/xgboost | 新功能 |
| fix/xxx | fix/readme-typo | 修复问题 |
| docs/xxx | docs/ml-framework | 文档修改 |
| experiment/xxx | experiment/transformer | 实验代码 |
| refactor/xxx | refactor/project-structure | 结构重构 |

---

## 7.3 推荐 commit message 写法

| 类型 | 示例 | 含义 |
|---|---|---|
| add | add logistic regression notes | 新增内容 |
| update | update README structure | 更新内容 |
| fix | fix typo in decision tree notes | 修复错误 |
| refactor | refactor project folders | 重构结构 |
| remove | remove outdated files | 删除内容 |

更规范的写法：

```bash
git commit -m "docs: add xgboost notes"
git commit -m "fix: correct typo in README"
git commit -m "refactor: reorganize ml folders"
```

---

# 8. 常见问题与解决方法

## 8.1 main 和 master 有什么区别

它们本质上都是默认主分支名称。

早期很多仓库默认叫：

```text
master
```

现在 GitHub 默认叫：

```text
main
```

新项目一般使用 `main`。

---

## 8.2 Switch branches/tags 是什么

它是 GitHub 页面中的“切换分支 / 标签”入口。

- Branch：分支，表示不同开发线
- Tag：标签，表示某个固定历史版本

常见默认显示：

```text
main
```

表示当前正在查看主分支。

---

## 8.3 为什么我 push 失败

常见原因：

1. 本地没有关联远程分支
2. GitHub 上已有更新，本地不是最新
3. 没有权限
4. 网络问题
5. 认证失败

常见解决：

```bash
git pull
git push
```

首次推送新分支：

```bash
git push -u origin 分支名
```

---

## 8.4 为什么 pull 后出现冲突

因为你和远程仓库都修改了同一个文件的同一部分。

Git 不知道应该保留谁的修改，所以需要人工处理。

冲突文件中通常会出现：

```text
<<<<<<< HEAD
你的本地内容
=======
远程内容
>>>>>>> 分支名
```

你需要手动编辑为最终想保留的内容，然后：

```bash
git add .
git commit -m "resolve merge conflict"
```

---

## 8.5 GitHub 可以直接在线改文件吗

可以。

但建议：

- 小改动可以在线改
- 正式开发建议使用本地 VSCode + Git

原因：

> 本地开发更适合调试、运行代码、管理多个文件。

---

## 8.6 README.md 是什么

`README.md` 是仓库首页默认展示的说明文件。

通常包含：

- 项目介绍
- 项目结构
- 使用方法
- 学习路线
- 安装说明
- 示例代码
- 更新记录

对于学习项目，README 非常重要。

---

## 8.7 .gitignore 是什么

`.gitignore` 用来告诉 Git 哪些文件不要纳入版本管理。

例如 Python 项目中常见：

```gitignore
__pycache__/
.ipynb_checkpoints/
.venv/
.env
*.log
data/raw/
```

作用：

> 避免把缓存、虚拟环境、密钥、大文件、临时文件提交到 GitHub。

---

# 9. 推荐学习路线

## 第一阶段：理解基本概念

目标：

- 知道 GitHub 是什么
- 知道 Git 和 GitHub 的区别
- 理解 repo、commit、branch、push、pull

建议练习：

- 创建一个 GitHub 仓库
- 新建 README.md
- 修改 README.md
- 查看 commit 历史

---

## 第二阶段：掌握基础命令

重点命令：

```bash
git clone
git status
git add
git commit
git push
git pull
```

建议练习：

- 在本地修改 README.md
- 提交 commit
- push 到 GitHub
- 在 GitHub 查看更新

---

## 第三阶段：学习分支

重点命令：

```bash
git branch
git switch
git merge
```

建议练习：

- 创建 feature 分支
- 在 feature 分支修改文件
- 合并回 main
- 删除 feature 分支

---

## 第四阶段：学习 Pull Request

目标：

- 理解 PR 的作用
- 能够从 feature 分支发起 PR
- 能够合并 PR
- 能够查看文件差异

建议练习：

- 创建 `feature/git-notes`
- 修改文档
- push 分支
- 在 GitHub 发起 PR
- 合并到 main

---

## 第五阶段：学习冲突处理

目标：

- 知道冲突为什么发生
- 能够手动解决简单冲突

建议练习：

- 在 GitHub 在线修改 README
- 在本地也修改同一行
- 执行 git pull
- 观察并解决冲突

---

## 第六阶段：学习项目管理功能

重点：

- Issues
- Labels
- Projects
- Milestones

建议练习：

- 用 Issues 管理学习任务
- 用 Labels 区分 bug、docs、feature
- 用 Projects 建一个学习看板

---

## 第七阶段：学习高级功能

后续可以继续学习：

- GitHub Actions
- GitHub Pages
- Releases
- Wiki
- Codespaces
- Dependabot

---

# 10. 机器学习项目中的 GitHub 使用建议

如果你要创建一个机器学习学习项目，例如：

```text
ml-system-learning
```

可以采用如下结构：

```text
ml-system-learning/
│
├── README.md
├── .gitignore
├── requirements.txt
│
├── notes/
│   ├── machine-learning-overview.md
│   ├── supervised-learning.md
│   ├── unsupervised-learning.md
│   └── deep-learning.md
│
├── algorithms/
│   ├── linear-regression/
│   ├── logistic-regression/
│   ├── decision-tree/
│   ├── random-forest/
│   ├── xgboost/
│   └── neural-network/
│
├── projects/
│   ├── ab-test-analysis/
│   ├── churn-prediction/
│   └── recommendation-system/
│
├── datasets/
│   └── README.md
│
└── experiments/
    ├── experiment-001/
    └── experiment-002/
```

---

## 10.1 main 分支放什么

`main` 分支建议保持稳定、干净、可展示。

适合放：

- 已完成笔记
- 已验证代码
- 项目 README
- 稳定版本实验

---

## 10.2 feature 分支放什么

新内容可以先放到 feature 分支。

例如：

```text
feature/linear-regression
feature/xgboost
feature/deep-learning-notes
feature/rag-demo
```

开发完成后再通过 PR 合并回 `main`。

---

## 10.3 Issues 可以怎么用

可以把 Issues 当成学习任务管理工具。

例如：

```text
Issue 1: 完成监督学习总览
Issue 2: 补充逻辑回归数学推导
Issue 3: 实现决策树 sklearn 示例
Issue 4: 整理 XGBoost 与 LightGBM 对比
Issue 5: 完成一个端到端机器学习项目
```

---

## 10.4 Projects 可以怎么用

可以建立一个学习看板：

```text
To do → In progress → Done
```

示例：

| To do | In progress | Done |
|---|---|---|
| SVM 笔记 | XGBoost 笔记 | 线性回归 |
| PCA 代码 | 决策树代码 | 逻辑回归 |
| A/B 测试项目 | 推荐系统项目 | GitHub 基础 |

---

## 10.5 README 建议包含什么

推荐 README 结构：

```markdown
# Machine Learning System Learning

## 项目简介

## 学习路线

## 项目结构

## 已完成内容

## 待完成内容

## 如何运行代码

## 参考资料

## 更新记录
```

---

# 11. 一套最小可行练习

如果你只想快速入门，可以完成以下练习。

## 练习 1：创建仓库

在 GitHub 创建：

```text
github-learning-practice
```

添加：

```text
README.md
```

---

## 练习 2：克隆到本地

```bash
git clone https://github.com/yourname/github-learning-practice.git
```

---

## 练习 3：本地修改 README

```bash
cd github-learning-practice
```

修改 `README.md` 后：

```bash
git status
git add .
git commit -m "update README"
git push
```

---

## 练习 4：创建分支

```bash
git switch -c feature/add-git-notes
```

新增文件：

```text
git-notes.md
```

提交并推送：

```bash
git add .
git commit -m "add git notes"
git push -u origin feature/add-git-notes
```

---

## 练习 5：创建 PR

在 GitHub 页面点击：

```text
Compare & pull request
```

然后合并到 `main`。

---

## 练习 6：删除分支

本地删除：

```bash
git branch -d feature/add-git-notes
```

远程删除：

```bash
git push origin --delete feature/add-git-notes
```

---

# 12. 学习 GitHub 的核心原则

1. 不要只看教程，要边做项目边学。
2. 先掌握 Git 基础，再理解 GitHub 页面。
3. 不要害怕分支，分支是 GitHub 的核心能力之一。
4. 每次 commit 只做一类清晰修改。
5. main 分支保持稳定。
6. README 是项目门面，要认真写。
7. Issues 可以管理学习任务。
8. PR 是工程协作的核心流程。
9. 遇到冲突不要慌，先看冲突标记，再手动保留正确内容。
10. 对机器学习项目来说，GitHub 不只是代码仓库，也是学习作品集。

---

# 13. 最终你应该达到的能力

完成这份学习后，你应该能够：

- 理解 GitHub 的作用
- 看懂 GitHub 仓库页面
- 知道常见英文概念的含义
- 使用 Git 管理本地项目
- 把本地项目上传到 GitHub
- 创建、切换、合并分支
- 发起和合并 Pull Request
- 使用 Issues 管理任务
- 用 GitHub 维护自己的机器学习学习项目

---

# 14. 最推荐的学习方式

建议你不要单独学习 GitHub，而是结合自己的机器学习项目学习。

推荐路径：

```text
创建机器学习仓库
        ↓
写 README
        ↓
本地 clone
        ↓
每天学习一个算法并 commit
        ↓
每个模块开一个 feature 分支
        ↓
用 PR 合并到 main
        ↓
用 Issues 管理待学内容
        ↓
用 Projects 管理整体进度
```

这样你学到的不只是 GitHub 操作，而是真正的工程化项目管理能力。
