import openai
import os, json
from config import console

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = "org-edLgdM1D3wcQzlvtRAjjUEG9"


class AIModel:
    DAVINCI = "text-davinci-003"
    CURIE = "text-curie-001"
    BABBAGE = "text-babbage-001"
    ADA = "text-ada-001"


def get_ai_answer(prompt: str, model=AIModel.CURIE, temperature=0):
    r = openai.Completion.create(
        engine=model, prompt=prompt, max_tokens=1000, temperature=temperature
    )
    raw_text = r["choices"][0]["text"]
    try:
        data = json.loads(raw_text)
    except Exception as e:
        console.print("load json error. The raw data is returned. ..", style="yellow")
        return raw_text
    else:
        return data
