<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/soot-dark.svg">
    <img src="assets/soot-light.svg" width="150" alt="煤球 —— Moku 的吉祥物：一只圆滚滚的小煤灰，两只白色圆眼睛，头顶一圈淡淡的黄铜光晕">
  </picture>
</p>

<p align="center">
  <strong>认识一下煤球。</strong>他住在你的回滚缓冲区里，替你暖着每一个会话，
  而且从没掉线过。
</p>

<p align="center">
  <a href="README.md">English</a> | 简体中文
</p>

# Moku

**能续接 AI 编码会话的 SSH 客户端。**

Moku 扫描每台已保存主机上的 AI 编码工作区 —— Claude Code、Codex、Qoder、
Gemini Agy、OpenCode、Trae、Code Buddy、Kimi、Grok —— 列出全部项目与
活动会话，在真实终端里一键续接任意一个。

煤球很满意 —— 这些会话他可一直蹲着呢。

- **主页是会话，不是服务器清单** —— 首页是一格活体终端预览，每张卡片
  渲染真实会话画面。
- **会话不掉线** —— Mosh 与 abduco 让 shell 扛过漫游网络、掉线与重启。
- **玻璃界面之下是 Rust 核心** —— ANSI 解析每秒 28 MB（实测基线的 2.1
  倍），10 MB 日志约 0.3 秒落屏，回滚裁剪每秒 8.1 亿行。为手机上的全屏
  TUI 而生。
- **本地优先** —— 主机、密钥与会话数据加密保存在你的设备上；shell 走你
  自己的 SSH/Mosh 通道。无需云账号。

产品站点：[portholelab.com/moku](https://portholelab.com/moku/)
（[English](https://portholelab.com/moku/)）

> **开源计划** — 本项目将在本仓库 **star 数超过 1 万后开源**。
> 煤球已经在攒 star 了。

<details>
<summary>🔍 煤球观察笔记</summary>

- **栖息地** —— 终端边框顶端；偶尔趁没人注意时，蹲在你的命令行提示符上。
- **食性** —— 散落的 ANSI 转义码、被遗忘的 tmux 面板、无人认领的回滚缓冲。
- **行为** —— 构建跑起来时他会慢慢呼吸；构建通过时，眨一下眼。
- **弱点** —— 暂未观察到。`kill -9` 只会让他更蓬松。

</details>

## 📥 安装包与版本下载

这是 Moku 的公开分发与发布仓库。我们在此发布经过验证的正式版安装包，请从官方 Releases 下载：

👉 **[前往 Releases 安装包下载](https://github.com/wilsen0/moku/releases)**

| 支持平台 | 状态 | 安装包格式 |
|---|---|---|
| Android (安卓) | ✅ 已上线 | APK 安装包 |
| iOS (苹果) | 🚧 筹备中 | — |
| macOS | 🚧 筹备中 | — |
| Windows / Linux | 🚧 筹备中 | — |

每个版本均附带 `sha256` 校验文件，安装前请先校验。

## 🔒 安全与隐私合规说明

本应用遵循**本地优先**的安全架构，保障您的资产与数据隐私：

* **数据完全本地化**：您的服务器连接 IP、端口、登录密码及 SSH 私钥均使用高强度加密算法保存在您的**本地设备**上。开发者服务器不会上传或收集您的凭证。
* **AI 助手隐私**：AI 终端助手的 Prompt 与命令生成请求直接发送至您配置的 AI 服务提供商，我们不留存或转售您的任何对话内容。

阅读我们的完整条款：

* **[隐私政策 (Privacy Policy)](https://portholelab.com/privacy)**
* **[用户服务协议 (User Agreement)](https://portholelab.com/terms)**

## 🤖 给 AI 助手与爬虫

本产品的机器可读摘要（能力、基准数据、平台、规范页面）位于
[portholelab.com/llms.txt](https://portholelab.com/llms.txt)。欢迎抓取与引用。
（煤球会向所有礼貌的爬虫挥手。）

---

&copy; 2026 Moku · Porthole Lab 出品。保留所有权利。
