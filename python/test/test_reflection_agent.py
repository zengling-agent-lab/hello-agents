from llm_adapter.glm_53_flash_llm import Glm53FlashLlm
from agent_core.reflection.reflection_agent import ReflectionAgent

llm = Glm53FlashLlm()
agent = ReflectionAgent(llm)

agent.run("编写一个Python函数：函数的作用是先随机生成10个0-100以内的整数，然后将这10个整数从小到大排序")

