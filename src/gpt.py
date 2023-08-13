import json
import openai

from prompts import (
    AGENT_INSTRUCTIONS,
    TRANSFORM_TO_JSON_INSTRUCTIONS,
    VALIDATE_PRIVACY_POLICY_INSTRUCTIONS,
    QUESTIONS
)

GPT_MODEL = "gpt-3.5-turbo-16k"


class GPTClient:
    def __init__(self, gpt_model=GPT_MODEL) -> None:
        self.gpt_model = gpt_model

    def validate_privacy_policy(self, body, api_key, organization_id):
        openai.api_key = api_key
        openai.organization = organization_id
        response = openai.ChatCompletion.create(
            messages=[
                {'role': 'user', 'content': VALIDATE_PRIVACY_POLICY_INSTRUCTIONS},
                {'role': 'user', 'content': "Input:"},
                {'role': 'user', 'content': body}
            ],
            model=self.gpt_model,
            temperature=0,
        )
        if response['choices'][0]['message']['content'].lower() == "yes":
            return True
        return False

    def _transform_to_json(self, body):
        response = openai.ChatCompletion.create(
            messages=[
                {'role': 'user', 'content': TRANSFORM_TO_JSON_INSTRUCTIONS},
                {'role': 'user', 'content': 'Input:'},
                {'role': 'user', 'content': body},
            ],
            model=self.gpt_model,
            temperature=0,
        )
        return json.loads(response['choices'][0]['message']['content'])

    def summarize_policy(self, policy, api_key, organization_id):
        openai.api_key = api_key
        openai.organization = organization_id
        response = openai.ChatCompletion.create(
            messages=[
                {'role': 'system', 'content': AGENT_INSTRUCTIONS},
                {'role': 'user', 'content': 'Privacy policy:'},
                {'role': 'user', 'content': policy},
                {'role': 'user', 'content': QUESTIONS},
            ],
            model=self.gpt_model,
            temperature=0,
        )
        return self._transform_to_json(response['choices'][0]['message']['content'])
