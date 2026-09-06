from llm.HelloAgentsLLM import HelloAgentsLLM
from python.function.Search import search
from react.ReActAgent import ReActAgent
from tool.ToolExecutor import ToolExecutor

if __name__ == '__main__':
    # 1.构造llm客户端
    llm = HelloAgentsLLM()
    # 2.构造工具执行器
    tool_executor = ToolExecutor()
    # 3.注册天气查询工具
    tool_executor.registerTool("天气查询工具", "查询天气的工具", search)
    # 4.实例agent
    agent = ReActAgent(llm_client=llm, tool_executor=tool_executor, max_step=5)
    result = agent.run("北京的天气怎么样")
    print("返回结果", result)
