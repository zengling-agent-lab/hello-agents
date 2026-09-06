from agent_core.plan_and_solve.plan_and_solve_agent import PlanAndSolveAgent
from llm_adapter.glm_53_flash_llm import Glm53FlashLlm

llm = Glm53FlashLlm()
agent = PlanAndSolveAgent(llm)

agent.run("一个水果店周一卖出了15个苹果。周二卖出的苹果数量是周一的两倍。周三卖出的数量比周二少了5个。请问这三天总共卖出了多少个苹果?")
