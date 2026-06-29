import json

from anthropic import Anthropic

from config import ANTHROPIC_API_KEY
from tools.definitions import TOOLS
from tools.dispatcher import execute_tool


class Agent:

    def __init__(self):

        self.client = Anthropic(api_key=ANTHROPIC_API_KEY)

        self.messages = []

    def chat(self, user_message: str):

        # Remember the user's message
        self.messages.append({
            "role": "user",
            "content": user_message
        })

        while True:

            response = self.client.messages.create(
                model="claude-haiku-4-5",
                max_tokens=1024,
                messages=self.messages,
                tools=TOOLS
            )

            # Claude is finished
            if response.stop_reason != "tool_use":

                self.messages.append({
                    "role": "assistant",
                    "content": response.content
                })

                return response.content[0].text

            # Save Claude's response containing tool calls
            self.messages.append({
                "role": "assistant",
                "content": response.content
            })

            tool_results = []

            # Claude may request several tools
            tool_uses = [
                block
                for block in response.content
                if block.type == "tool_use"
            ]

            for tool_use in tool_uses:

                print(f"Calling {tool_use.name}({tool_use.input})")

                result = execute_tool(tool_use)

                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": tool_use.id,
                    "content": json.dumps(result)
                })

            # Give ALL tool results back to Claude
            self.messages.append({
                "role": "user",
                "content": tool_results
            })