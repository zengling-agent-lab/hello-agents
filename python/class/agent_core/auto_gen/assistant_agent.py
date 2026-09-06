import asyncio

from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination

from agent_core.auto_gen.assistant_agent_factory import AssistantAgentFactory
from llm_adapter.autogen_client import create_openai_model_client

from autogen_agentchat.ui import Console

llm = create_openai_model_client()
factory = AssistantAgentFactory(llm)

# 定义团队聊天和协作规则
team_chat = RoundRobinGroupChat(
    participants=[
        factory.create_product_manager(),
        factory.create_engineer(),
        factory.create_code_reviewer(),
        factory.create_user_proxy()
    ],
    termination_condition=TextMentionTermination("TERMINATE"),
    max_turns=20,
)


async def run_software_development_team():
    # ... 初始化客户端和智能体 ...

    # 定义任务描述
    task = """我们需要开发一个比特币价格显示应用，具体要求如下：
            核心功能：
            - 实时显示比特币当前价格（USD）
            - 显示24小时价格变化趋势（涨跌幅和涨跌额）
            - 提供价格刷新功能

            技术要求：
            - 使用 Streamlit 框架创建 Web 应用
            - 界面简洁美观，用户友好
            - 添加适当的错误处理和加载状态

            请团队协作完成这个任务，从需求分析到最终实现。"""

    # 异步执行团队协作，并流式输出对话过程
    result = await Console(team_chat.run_stream(task=task))
    return result