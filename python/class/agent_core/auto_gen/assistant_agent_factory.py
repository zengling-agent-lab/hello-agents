from autogen_agentchat.agents import AssistantAgent, UserProxyAgent

from prompt.auto_gen.manager_prompt_template import PRODUCT_MANAGE_PROMPT_TEMPLATE, ENGINEER_MANAGE_PROMPT_TEMPLATE, \
    CODE_REVIEWER_MANAGE_PROMPT_TEMPLATE, USER_PROXY_MANAGE_PROMPT_TEMPLATE


class AssistantAgentFactory:
    def __init__(self, model_client):
        # 实例属性，整个类所有实例方法都可以访问 self.model_client
        self.model_client = model_client

    def create_product_manager(self):
        """创建产品经理智能体"""
        return AssistantAgent(
            name="ProductManager",
            model_client=self.model_client,  # 从实例取model_client
            system_message=PRODUCT_MANAGE_PROMPT_TEMPLATE,
        )

    def create_engineer(self):
        """创建软件工程师智能体"""
        return AssistantAgent(
            name="Engineer",
            model_client=self.model_client,
            system_message=ENGINEER_MANAGE_PROMPT_TEMPLATE,
        )

    def create_code_reviewer(self):
        """创建代码审查员智能体"""
        return AssistantAgent(
            name="CodeReviewer",
            model_client=self.model_client,
            system_message=CODE_REVIEWER_MANAGE_PROMPT_TEMPLATE,
        )

    def create_user_proxy(self):
        """创建用户代理智能体"""
        return UserProxyAgent(
            name="UserProxy",
            description=USER_PROXY_MANAGE_PROMPT_TEMPLATE,
        )