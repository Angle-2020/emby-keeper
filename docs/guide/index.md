<script setup>

import Logo from '../components/Logo.vue';

</script>

# 什么是 Embykeeper?

<p align="center">
  <a href='https://github.com/emby-keeper/emby-keeper'>
    <Logo />
  </a>
</p>

Embykeeper 是一个专为 Emby 影视服务器设计的自动化工具. 它主要提供两大核心功能:

1. **自动签到** - 可以自动完成多个站点的 Telegram 机器人每日签到, 以获取积分.

2. **定时保号** - 通过模拟登录和播放视频, 定期保持 Emby 账号的活跃状态, 避免因长期不使用而被回收.

除此之外, Embykeeper 还提供了一些额外功能, 如自动监控抢注邀请码、自动水群、考核辅助等.

项目支持 Python 运行、Docker 部署或云部署, 且完全开源, 不存储任何密钥或隐私信息, 经两年的开发已经在稳定和安全性方面有一定保证.

::: tip 快速安装
希望安装 Embykeeper? 请前往 [**🚀 安装指南**](/guide/安装指南.md).
:::

## 设计初衷与声明

在中文 Emby 社群规则下, 保号要求逐渐苛刻 (部分要求每月登录或每日签到), 这使得休闲时间紧张的人士难以安心使用. 本项目仅旨在帮助该类人群保号, 不鼓励持有大量 Emby 账号而不使用, 导致真正需要的人、为中文影视资源分享和翻译有贡献的人难以获得账号的行为.

开发团队呼吁仅保留 1-2 个较全面质量较高的 Emby 服务器.

本项目仅提供工具, 具体使用形式及造成的影响和后果与开发团队无关.

当您安装并使用该工具, 默认您已经阅读并同意上述声明, 并确认自己并非出于"集邮"目的而安装.

## 账户安全

本项目涉及的一切 Emby 服务器与 Embykeeper 开发团队无关, 在使用 Embykeeper 时造成的一切损失 (包括但不限于 Emby 或 Telegram 账号被封禁或被群封禁) 与开发团队无关.

为了您的账号安全, 推荐使用小号. 运行该工具的 Telegram 账号若通过接码注册, 请使用一段时间再接入本工具.

Embykeeper 将自动向 Embykeeper Auth Bot ([@embykeeper_auth_bot](https://t.me/embykeeper_auth_bot)) 发送信息, 用于在线验证码解析、日志记录、用户验证等, 内容不含任何密码或密钥信息, 或其他敏感隐私信息.
