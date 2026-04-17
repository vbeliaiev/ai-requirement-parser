import argparse
import json
import sys
from dotenv import load_dotenv
from openai import APIError, APIConnectionError, RateLimitError
from .analyzer import analyze_requirements

def main():
  load_dotenv()

  parser = argparse.ArgumentParser(description="Analyze product requirements")
  parser.add_argument("requirement", help="Product requirement test")
  parser.add_argument("--model", help="Choose OpenAI model", default="gpt-4.1-mini")

  args = parser.parse_args()

  try:
    result = analyze_requirements(args.requirement, model=args.model)

    print(json.dumps(result, indent=2, ensure_ascii=False))
  except APIConnectionError:
    print("Connection error")
  except RateLimitError:
    print("Limit is exceed")
  except APIError as e:
    print(e)
  except ValueError as e:
    print(e)

if __name__ == "__main__":
  main()

