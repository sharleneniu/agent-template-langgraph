# Agent Template - LangGraph Python

## 项目简介

基于 LangGraph 的智能体项目模板，用户创建项目时自动 fork 此仓库作为开发起点。

## 技术栈

| 类别 | 技术 |
|------|------|
| 语言 | Python 3.11 |
| 智能体框架 | LangGraph |
| LLM 集成 | LangChain |
| 可观测性 | LangSmith（可选） |
| 容器化 | Docker（内置 Dockerfile，用户无需编写） |

## 模板结构

```
agent-template-langgraph/
├── agent/
│   ├── __init__.py
│   ├── main.py           # 入口文件，启动 HTTP 服务
│   ├── graph.py           # LangGraph 图定义
│   ├── nodes.py           # 节点实现
│   ├── state.py           # 状态定义
│   └── tools.py           # 工具定义
├── tests/
│   └── test_agent.py      # 基础测试用例
├── Dockerfile             # 平台提供，用户一般不改
├── requirements.txt       # Python 依赖
├── .env.example           # 环境变量示例
├── .gitignore
└── README.md
```

## Dockerfile

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "-m", "agent.main"]
```

## 用户使用流程

```
1. 在平台创建项目 → 自动 fork 此模板到用户私有仓库
2. 打开 Web IDE → 自动 clone 仓库到工作区
3. 编辑 graph.py、nodes.py、tools.py 实现业务逻辑
4. 终端中 python -m agent.main 本地调试
5. git push 提交代码
6. 在平台点击发布 → 自动基于 Dockerfile 构建镜像
```

## 环境变量

| 变量名 | 说明 | 注入方式 |
|--------|------|---------|
| `LITELLM_API_KEY` | 模型 API Key | 平台自动注入 |
| `LANGSMITH_API_KEY` | LangSmith Key（可选） | 用户自行配置 |
| `AGENT_PORT` | 服务端口，默认 8000 | 平台自动注入 |

## 后续扩展

| 模板 | 说明 |
|------|------|
| ReAct Agent | 基于 ReAct 模式的智能体模板 |
| Multi-Agent | 多智能体协作模板 |
| RAG Agent | 检索增强生成模板 |
| Java Spring AI | Java 语言智能体模板 |
