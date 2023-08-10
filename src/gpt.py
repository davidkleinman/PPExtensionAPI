import json
import openai
import os

from prompts import (
    AGENT_INSTRUCTIONS,
    FORMATTING_INSTRUCTIONS,
    FORMATTING_REPAIR_INSTRUCTIONS,
    QUESTIONS
)

GPT_MODEL = "gpt-3.5-turbo-16k"


class GPTClient:
    def __init__(self, gpt_model=GPT_MODEL) -> None:
        self.gpt_model = gpt_model
        openai.api_key = os.getenv("OPEN_AI_API_KEY")
        openai.organization = "org-Dblzvd76olnntly83Upvwr2f"

    def _repair_formatting(self, body):
        response = openai.ChatCompletion.create(
            messages=[
                {'role': 'user', 'content': FORMATTING_REPAIR_INSTRUCTIONS},
                {'role': 'user', 'content': 'Input:'},
                {'role': 'user', 'content': body},
            ],
            model=self.gpt_model,
            temperature=0,
        )
        return json.loads(response['choices'][0]['message']['content'])

    def summarize_policy(self, policy):
        try:
            response = openai.ChatCompletion.create(
                messages=[
                    {'role': 'system', 'content': AGENT_INSTRUCTIONS},
                    {'role': 'user', 'content': FORMATTING_INSTRUCTIONS},
                    {'role': 'user', 'content': 'Privacy policy:'},
                    {'role': 'user', 'content': policy},
                    {'role': 'user', 'content': 'Questions:'},
                    {'role': 'user', 'content': QUESTIONS},
                ],
                model=self.gpt_model,
                temperature=0,
            )
            return json.loads(response['choices'][0]['message']['content'])
        except json.JSONDecodeError:
            return self._repair_formatting(response['choices'][0]['message']['content'])
