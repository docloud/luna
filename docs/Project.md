# Project

项目主要由三个子项目构成

`Luna`正处于Alpha，`Jenny`和`Cherry`尚未开始开发

1. [Luna][Luna], 后端服务框架，主要为Restful、RPC服务提供支撑，也是对「 弹性文档引擎」 概念中「 弹性」 和「 引擎」 的诠释，负责了应用层的负载均衡、接口定义、以及部署时对编译层的隔离。
2. [Jenny][Jenny], 前端框架，基于最新的React（用不用flint.js尚不知道）搭建，负责交互逻辑和后端服务的对接，以及 发布/热更新 过程的自动化。
3. [Cherry][Cherry], 文档编译项目，用于实时将用户文本根据预定义好的 EBNF 范式编译成用户指定的格式，这个项目理想的目标是，能够支持流式计算以及 **JIT** ( *Just-In-Time* ) 编译。

[Luna]: http://docloud.github.io/luna	"Luna Project"
[Jenny]: http://docloud.github.io/jenny	"Jenny Project"
[Cherry]: http://docloud.github.io/cherry	"Cherry Project"