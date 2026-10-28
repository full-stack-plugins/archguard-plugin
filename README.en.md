# ArchGuard (架构边界防护)

> Rust CLI 与插件桥接完成；缺少 CLI 或契约时返回 PARTIAL。

**Version**: 0.1.1 · **License**: Apache-2.0 · **Skills**: 1

[简体中文](README.md)

## Positioning

ArchGuard is an independent plugin in the Partme Guard family. Its command prefix is archguard. It is installed, versioned and executed independently.

## CLI Commands

| Command | Type |
| :--- | :--- |
| version | 独立入口 |
| doctor | 独立入口 |
| discover | 独立入口 |
| status | 独立入口 |
| check | 独立入口 |

## Installation

Select plugin ID `archguard` from the [Full Stack Plugins marketplace](https://github.com/partme-ai/full-stack-plugins). The repository name `archguard-plugin` is not the plugin ID. The installation ref is `v0.1.1`; whether a host exposes `bin/` on PATH requires host-specific verification.

## Quick Start

~~~bash
archguard version
archguard doctor
archguard status
~~~

## Current Status

Rust CLI 与插件桥接完成；缺少 CLI 或契约时返回 PARTIAL。

No PASS without real execution evidence. Unimplemented capabilities report DESIGN_ONLY or UNVERIFIED.

## Architecture

See product-docs/ArchGuard/ and docs/ for command lifecycle, read-only checks and evidence boundaries.

## Boundaries

- Not merged into a single Partme Guard command.
- Does not replace another Guard's domain decision.
- Does not auto-commit, auto-push or modify user code.

## Verification

~~~bash
python3 -m unittest discover -s tests -v
~~~

## License

Apache-2.0
