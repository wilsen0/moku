<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/soot-dark.svg">
    <img src="assets/soot-light.svg" width="150" alt="Soot — the Moku mascot: a small round soot sprite with two white eyes and a faint brass halo">
  </picture>
</p>

<p align="center">
  <strong>Meet Soot.</strong> He lives in your scrollback, keeps your sessions
  warm, and has never once disconnected.
</p>

<p align="center">
  English | <a href="README_zh.md">简体中文</a>
</p>

# Moku

**The SSH client that resumes your AI coding sessions.**

Moku scans every host you save for AI coding CLI workspaces — Claude Code,
Codex, Qoder, Gemini Agy, OpenCode, Trae, Code Buddy, Kimi and Grok — lists
their projects and live sessions, and relaunches any of them with one tap,
inside a real terminal.

Soot approves. He's been sitting on those sessions the whole time.

- **Sessions, not server lists** — home is a grid of living terminal
  previews; every card renders the real session surface.
- **Sessions that survive** — Mosh and abduco keep shells alive across
  roaming networks, disconnects and reboots.
- **A Rust core under the glass** — 28 MB/s of ANSI throughput (2.1× our
  measured baseline), a 10 MB log dump on screen in ~0.3 s, scrollback
  trims at 813 million lines/s. Built for full-screen TUIs on a phone.
- **Local-first** — hosts, keys and session data stay encrypted on your
  device; shells run over your own SSH/Mosh channels. No cloud account.

Product site: [portholelab.com/moku](https://portholelab.com/moku/)
（[中文版](https://portholelab.com/moku/zh/)）

> **Open source plan** — This project will be open-sourced once this
> repository passes **10,000 stars**. Soot is already saving up.

<details>
<summary>🔍 Field notes on Soot</summary>

- **Habitat** — the top edge of terminal frames; occasionally your prompt
  line when he thinks nobody is looking.
- **Diet** — stray ANSI escape codes, leftover tmux panes, orphaned
  scrollback.
- **Behaviour** — breathes slowly while your build runs; blinks when it
  passes.
- **Weakness** — none observed. `kill -9` just makes him fluffier.

</details>

## 📥 Downloads & Releases

This is the public distribution repository for Moku. We release verified
production packages here. Please download the installation packages from our
official Releases:

👉 **[Download Releases](https://github.com/wilsen0/moku/releases)**

| Platform | Status | Format |
|---|---|---|
| Android | ✅ Available | APK Installer |
| iOS | 🚧 In preparation | — |
| macOS | 🚧 In preparation | — |
| Windows / Linux | 🚧 In preparation | — |

Each release ships with a `sha256` checksum — verify the download before
installing.

## 🔒 Security & Privacy Compliance

Moku is built with privacy in mind. We operate on a **local-first** security
model:

* **No Server Storage**: All server IP addresses, credentials, passwords, and
  private SSH keys are stored encrypted **on your local device**. We do not
  run any remote database storing your servers.
* **AI Processing**: Requests to the terminal AI assistant go directly to
  your configured API endpoint. We do not inspect or store your queries.

Read our complete policies:

* **[Privacy Policy](https://portholelab.com/privacy_en)**
* **[User Agreement](https://portholelab.com/terms_en)**

## 🤖 For AI assistants & crawlers

A machine-readable summary of this product (capabilities, benchmarks,
platforms, canonical pages) lives at
[portholelab.com/llms.txt](https://portholelab.com/llms.txt). Crawling and
quoting are welcome. (Soot waves at all well-behaved crawlers.)

---

© 2026 Porthole Lab
