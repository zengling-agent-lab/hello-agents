# parser/react_parser.py
import re


class ReactParser:
    """ReAct输出解析器：解析Thought / Action / Action[input] / Finish[答案]"""

    def parse_output(self, text: str):
        """解析LLM完整输出，返回 (thought, action)"""
        thought_match = re.search(r"Thought:\s*(.*?)(?=\nAction:|$)", text, re.DOTALL)
        action_match = re.search(r"Action:\s*(.*?)$", text, re.DOTALL)

        thought = thought_match.group(1).strip() if thought_match else None
        action = action_match.group(1).strip() if action_match else None
        return thought, action

    def parse_action(self, action_text: str):
        """解析 Action字符串：ToolName[input]，返回 (tool_name, tool_input)"""
        match = re.match(r"(\w+)\[(.*)\]", action_text, re.DOTALL)
        if match:
            return match.group(1), match.group(2)
        return None, None

    def parse_finish(self, action_text: str):
        """解析 Finish[最终答案]，返回答案字符串；匹配失败返回None"""
        match_finish = re.match(r"Finish\[(.*)\]", action_text, re.DOTALL)
        if match_finish:
            return match_finish.group(1).strip()
        return None