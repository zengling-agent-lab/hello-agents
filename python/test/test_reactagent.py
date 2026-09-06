from llm_adapter.glm_53_flash_llm import Glm53FlashLlm
from tool.tool_register import ToolRegister
from parser.react_parser import ReactParser
from agent_core.react.react_agent import ReActAgent
from tool.search_weather_tool import search

llm = Glm53FlashLlm()
tool_register = ToolRegister()
tool_register.registerTool("天气查询工具", "查询天气工具", search)
parser = ReactParser()

agent = ReActAgent(
    llm_client=llm,
    tool_register=tool_register,
    parser=parser,
    max_step=5
)

res = agent.run("上海今天天气怎么样")
print(res)
