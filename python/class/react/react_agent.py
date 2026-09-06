from llm_adapter.glm_53_flash_llm import Glm53FlashLlm
from prompt.react_prompt_template import REACT_PROMPT_TEMPLATE
from tool.tool_register import ToolRegister
from parser.react_parser import ReactParser


class ReActAgent:
    def __init__(

            self,
            llm_client: Glm53FlashLlm,
            tool_register: ToolRegister,
            parser: ReactParser,
            max_step: int = 5
    ):
        self.llm_client = llm_client
        self.tool_register = tool_register
        self.parser = parser  # 注入解析器
        self.max_step = max_step
        self.history = []

    def run(self, question: str):
        """运行ReAct智能体来回答一个问题。"""
        self.history = []
        current_step = 0
        while current_step < self.max_step:
            current_step += 1
            print(f"--- 第 {current_step} 步 ---")

            # 1.格式化提示词
            tools_desc = self.tool_register.getAvailableTools()
            history_str = "\n".join(self.history)
            prompt = REACT_PROMPT_TEMPLATE.format(
                tools=tools_desc,
                question=question,
                history=history_str
            )

            # 2.调用LLM
            messages = [{"role": "user", "content": prompt}]
            response_text = self.llm_client.think(messages=messages)

            if not response_text:
                print("错误:LLM未能返回有效响应。")
                break

            # 3.交给parser解析
            thought, action = self.parser.parse_output(response_text)

            if thought:
                print(f"思考: {thought}")

            if not action:
                print("警告:未能解析出有效的Action，流程终止。")
                break

            # 4.Finish结束分支
            final_answer = self.parser.parse_finish(action)
            if final_answer is not None:
                print(f"🎉 最终答案: {final_answer}")
                return final_answer

            # 5.解析工具调用
            tool_name, tool_input = self.parser.parse_action(action)
            if not tool_name or not tool_input:
                print("警告：解析Action失败，跳过本轮")
                continue

            print(f"🎬 行动: {tool_name}[{tool_input}]")

            tool_function = self.tool_register.getTool(tool_name)
            if not tool_function:
                observation = f"错误:未找到名为 '{tool_name}' 的工具。"
            else:
                observation = tool_function(tool_input)

            print(f"👀 观察: {observation}")

            self.history.append(f"Action: {action}")
            self.history.append(f"Observation: {observation}")

        print("已达到最大步数，流程终止。")
        return None
