import openai
import os

GPT_MODEL = "gpt-3.5-turbo"


class GPTClient:
    def __init__(self, gpt_model=GPT_MODEL) -> None:
        self.gpt_model = gpt_model
        openai.api_key = os.getenv("OPEN_AI_API_KEY")
        openai.organization = "org-Dblzvd76olnntly83Upvwr2f"

    def answer(self, txt, question):
        query = f"""Use the below privacy policy to answer the subsequent question. If the answer cannot be found, write "I don't know."

        Privacy policy:
        \"\"\"
        {txt}
        \"\"\"

        Question: {question}?"""

        response = openai.ChatCompletion.create(
            messages=[
                {'role': 'system', 'content': 'You answer questions about the contents of the following privacy policy.'},
                {'role': 'user', 'content': query},
            ],
            model=GPT_MODEL,
            temperature=0,
        )

        return response['choices'][0]['message']['content']
