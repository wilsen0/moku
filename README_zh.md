<p align="center">
  <img src="assets/brand_mark.png" width="100" alt="Moku 吉祥物 煤球">
</p>

<h1 align="center">Moku</h1>

<p align="center">
  <strong>AI 编程会话，随开随续。</strong><br>
  专为多端打造、能无缝续接 AI 编程会话的现代化 SSH 工作区。
</p>

<p align="center">
  <a href="https://mokuapp.dev/zh/">官方产品站</a> ·
  <a href="https://github.com/wilsen0/moku/releases">安装包下载</a> ·
  <a href="https://github.com/wilsen0/moku/discussions/1">10k Stars 开源路线图</a> ·
  <a href="README.md">English</a> | 简体中文
</p>

<p align="center">
  <a href="https://www.producthunt.com/products/moku?embed=true&utm_source=badge-featured&utm_medium=badge&utm_campaign=badge-moku" target="_blank" rel="noopener noreferrer"><img alt="Moku - The SSH workspace that resumes your AI coding sessions | Product Hunt" width="250" height="54" src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=1244350&theme=neutral"></a>
</p>

<p align="center">
  <img alt="平台支持: iOS 16+ | Android 8+ | macOS | Linux | Windows" src="https://img.shields.io/badge/平台-iOS%20|%20Android%20|%20macOS%20|%20Linux%20|%20Windows-blue?style=flat-square">
  <img alt="终端引擎: Rust Core" src="https://img.shields.io/badge/终端核心-Rust%20Core-orange?style=flat-square">
  <img alt="开发框架: Flutter" src="https://img.shields.io/badge/框架-Flutter-cyan?style=flat-square">
  <a href="https://github.com/wilsen0/moku/discussions/1"><img alt="开源计划: 10k Stars 开源" src="https://img.shields.io/badge/开源计划-10k%20Stars%20开源-brightgreen?style=flat-square"></a>
</p>

<p align="center">
  <video src="https://github.com/wilsen0/moku/raw/main/film/moku-film.mp4" poster="https://github.com/wilsen0/moku/raw/main/film/poster.jpg" controls playsinline width="720"></video>
</p>

---

Moku 自动扫描远程主机上的 AI 编程工作区 —— **Claude Code、OpenAI Codex、Qoder、Antigravity (Agy)、OpenCode、MiniMax Code、Oh My Pi、DeepSeek Harness、Trae、Code Buddy、Kimi、Grok**，聚合项目与历史会话，手机/电脑上随时一键续接中断的编程任务。

界面之下搭载了 **自研高性能 Rust 终端核心** 与 **Mosh/abduco 级会话防掉线架构**，专为移动端与桌面端的流畅命令行操作而生。

---

## 核心亮点

### AI 编程工作区与会话续接
- **多端自动扫描**：跨 Linux、macOS 与 Windows 全矩阵扫描各大 AI 编程助手留下的工作区与会话数据。
- **一键无缝续接**：无需手动翻找 Session ID，点击即刻在真实终端中唤醒并恢复会话上下文。
- **纯原生零依赖**：完全复用现有 SSH 加密通道探测，**服务端无需安装任何常驻 Agent 或守护进程**。

### Rust 驱动的下一代终端引擎
- **ANSI 解析达 28+ MB/s**：实测 baseline 的 2.1 倍吞吐，大流日志瞬间完成解析。
- **10 MB 日志约 0.3 秒上屏**：超十万行日志顺滑滚屏，无卡顿、不发烫。
- **回滚缓冲区裁剪达每秒 8.1 亿行**：日志越猛，性能优势越明显。

### 永不掉线的网络与会话韧性
- **无感网络漫游**：集成原生 **Mosh** 协议，Wi-Fi 与 5G 移动蜂窝网络之间无缝切换不掉线。
- **会话持久留存**：结合 **abduco** 进程托管技术，网络突发中断或客户端重启后会话依然完好保留。

### 专为现代开发者打造的交互体验
- **活体终端网格主页**：告别单调枯燥的静态服务器列表，主页呈现各终端的实时预览卡片。
- **手感细腻的虚拟键盘**：专为移动端优化的 `Ctrl`、`Alt`、`Esc` 粘滞修饰键、自定义命令面板与手势光标导航。
- **全能运维工具箱**：内置极速 SFTP 远程文件管理与代码编辑、服务器状态实时监控（CPU/内存/磁盘/网络）、Docker 容器管理及进程监视。

### 本地优先与零信任隐私架构
- **凭证设备端加密存储**：所有服务器 IP、端口、密码与 SSH 私钥仅在设备本地加密保存，无中心云端数据库。
- **AI 请求直接通信**：终端 AI 助手直连您自行配置的服务商 API，绝不经过任何第三方转发或留存。

---

## 支持的 AI 编程助手与 CLI

| AI 编程助手 / CLI | 唤起命令 | 状态与数据存储机制 | 续接支持度 |
|---|---|---|:---:|
| **Claude Code** | `claude` | `~/.claude/projects/` | ✅ (`--resume`) |
| **OpenAI Codex** | `codex` | `~/.codex/sessions/` | ✅ 完美支持 |
| **Antigravity CLI** | `agy` | `~/.gemini/antigravity-cli/` | ✅ 完美支持 |
| **Qoder** | `qodercli` | `~/.qoder/projects/` | ✅ 完美支持 |
| **OpenCode** | `opencode` | `~/.local/share/opencode/opencode.db` | ✅ 完美支持 |
| **MiniMax Code** | `mcode` | `~/.minimax/v2/sqlite/runtime-state.sqlite` | ✅ (`--session <id>`) |
| **Oh My Pi / Pi** | `omp` / `pi` | `~/.omp/agent/sessions/` | ✅ (`--resume <id>`) |
| **DeepSeek Harness** | `dsh` | `~/.dsh/sessions/` | ✅ 会话扫描支持 |
| **Trae CLI** | `trae` | `~/.trae/projects/` | ✅ 完美支持 |
| **Code Buddy** | `codebuddy` | `~/.codebuddy/projects/` | ✅ 完美支持 |
| **Kimi Code** | `kimi` | `~/.kimi-code/` | ✅ 完美支持 |
| **Grok CLI** | `grok` | `~/.grok/sessions/` | ✅ 完美支持 |

---

## Moku 与传统 SSH 客户端对比

| 核心维度 | Moku | 传统 SSH 工具 |
|---|---|---|
| **AI 编程会话** | 自动发现、项目聚合、一键续接 | ❌ 无法识别（需手动翻找命令与 ID） |
| **主页视觉呈现** | 实时活体终端状态网格 | ❌ 枯燥的静态服务器地址列表 |
| **网络抗抖动与漫游** | 原生 Mosh 漫游 + abduco 会话守护 | ❌ 切换网络即刻断连抛错 |
| **终端渲染引擎** | 自研 Rust 核心（ANSI 28 MB/s 吞吐） | ⚠️ 传统 JS/WebView 或简单控件（大日志易卡死） |
| **服务端侵入性** | 纯净 SSH 通道探测（零 Agent 部署） | 纯净 SSH |
| **数据与隐私架构** | 100% 本地加密存储，AI 直连用户端点 | 多数依赖云端同步或中心服务器中转 |

---

## Rust 终端核心实测性能基准

| 工作负载 | Rust 核心 | Flutter AOT 基准 | 相对加速比 |
|---|---:|---:|:---:|
| **ANSI 流解析吞吐** | 28.07 MB/s | 13.39 MB/s | **2.10×** |
| **10 MiB 大日志瞬时输出** | 34.96 MB/s | 11.21 MB/s | **3.12×** |
| **窗口尺寸重排 (Reflow)** | 117.31 次/秒 | 99.46 次/秒 | **1.18×** |
| **回滚缓冲区饱和追加** | 408.79k 行/秒 | 171.09k 行/秒 | **2.39×** |
| **回滚缓冲区高速裁剪** | 813.59M 行/秒 | 70.53M 行/秒 | **11.54×** |

---

## 安装包与版本下载

经过签名验证的正式版安装包已发布在 GitHub Releases：

**[前往 GitHub Releases 下载安装包](https://github.com/wilsen0/moku/releases)**

| 平台 | 当前状态 | 发布格式 |
|---|---|---|
| **Android (安卓)** | ✅ 已上线 | APK 安装包 (`arm64-v8a`) |
| **iOS (苹果)** | ✅ 已上架 | [App Store](https://apps.apple.com/app/id6800746191) · [TestFlight 公测](https://testflight.apple.com/join/w7CFhrRT)（国区兜底） |
| **macOS** | 🚧 筹备中 | DMG / Universal 二进制 |
| **Windows / Linux** | 🚧 筹备中 | MSIX / AppImage / DEB |

*每个版本均附带 `sha256` 校验和，建议在安装前核验。*

> **开源计划** —— 本仓库 star 数超过 **1 万**后，项目将开放源代码。煤球已经在攒 star 了。

---

## 交流与反馈

- **QQ 交流群：`1081368637`**（天才程序员会议厅）— QQ 扫码加入：

  <img src="assets/qq-group.jpg" width="280" alt="Moku QQ 交流群二维码">

- 也可以在 [GitHub Discussions](https://github.com/wilsen0/moku/discussions) 提问题、聊需求，中英文都欢迎。

---

## 安全与隐私合规说明

本地优先，不是口号，是架构：

- **数据不出设备** —— 服务器地址、密码、SSH 私钥均加密保存在本地，我们没有存储您服务器凭证的远程数据库。
- **AI 请求直达您的服务商** —— 终端 AI 助手直接请求您配置的 API 端点，我们不查看、不留存。

阅读完整条款：[隐私政策](https://mokuapp.dev/privacy) · [用户协议](https://mokuapp.dev/terms)

---

## 给 AI 助手与爬虫

本产品的机器可读摘要（能力、基准数据、平台、规范页面）位于 [mokuapp.dev/llms.txt](https://mokuapp.dev/llms.txt)。欢迎抓取与引用。（煤球会向所有礼貌的爬虫挥手。）

<details>
<summary>煤球观察笔记</summary>

- **栖息地** —— 终端边框顶端；偶尔趁没人注意时，蹲在你的命令行提示符上。
- **食性** —— 散落的 ANSI 转义码、被遗忘的 tmux 面板、无人认领的回滚缓冲。
- **行为** —— 构建跑起来时他会慢慢呼吸；构建通过时，眨一下眼。
- **弱点** —— 暂未观察到。`kill -9` 只会让他更蓬松。

</details>

---

<sub>© 2026 Porthole Lab · 煤球是像素画的，和我们爱的所有东西一样。</sub>
