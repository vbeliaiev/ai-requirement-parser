import json
from openai import OpenAI
from .prompts import SYSTEM_PROMPT

def analyze_requirements(requirements: str, model: str = "gpt-4.1-mini") -> dict:
  """
  It sends requirement to OpenAI and returns parsed dict.

  Raises:
    ValueError: if the result isn't a valid JSON
    openai.APIError: in a case of API problems
  """
  client = OpenAI()

  response = client.responses.create(
    model = model,
    instructions = SYSTEM_PROMPT,
    input = f"Return json. {requirements}",
    text= {"format": {"type": "json_object"}}
  )

  data = json.loads(response.output_text)

  if not isinstance(data, dict):
    raise ValueError("Response is not a JSON object")

  if "features" not in data or "modules" not in data:
    raise ValueError("Response missing required fields: 'features' or 'modules'")

  if not isinstance(data["features"], list) or not isinstance(data["modules"], list):
    raise ValueError("'features' and 'modules' must be arrays")

  return data
