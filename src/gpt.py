import openai
import os

GPT_MODEL = "gpt-3.5-turbo"


class GPTClient:
    def __init__(self, gpt_model=GPT_MODEL) -> None:
        self.gpt_model = gpt_model
        openai.api_key = os.getenv("OPEN_AI_API_KEY")
        openai.organization = "org-Dblzvd76olnntly83Upvwr2f"

    def summarize_policy(self, policy):
        instructions = """
You are an agent whose purpose is to answer questions regarding privacy policies.
If you can't find an answer to a specific question, please reply: "I don't have enough information".
"""
        questions = [
            "What types of personal information are collected?",
            "How is personal information collected from users?",
            "What is the purpose for collecting user data?",
            "Is the collected data shared with third parties?",
            "What methods are used for data storage and security?",
        ]
        responses = []
        for question in questions:
            response = openai.ChatCompletion.create(
                messages=[
                    {'role': 'system', 'content': instructions},
                    {'role': 'user', 'content': 'Regarding this privacy policy:'},
                    {'role': 'user', 'content': policy},
                    {'role': 'user', 'content': question},
                ],
                model=self.gpt_model,
                temperature=0,
            )
            responses.append(response['choices'][0]['message']['content'])
        return responses
