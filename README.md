# ArchGuard（架构边界防护）

> 提取架构事实、校验依赖契约、输出违规证据；没有真实 CLI 时报告 DESIGN_ONLY。

版本：0.1.0 · 许可证：Apache-2.0

## 定位

把模块依赖、分层与边界约束变成可执行门禁。

当前为插件脚手架：有真实 CLI 时执行并保留证据；无 CLI 时明确输出 DESIGN_ONLY，不冒充通过。

## 安装

codex plugin marketplace add partme-ai/full-stack-plugins
codex plugin add archguard@full-stack-plugins

## 边界

- 不替代其他专业 Guard。
- 不绕过受保护分支、必需检查或人工审批。
