# Requirement Analyzer

CLI tool that analyzes product requirements using OpenAI. Extracts features and technical modules from text descriptions.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

## Configuration

```bash
cp .env.example .env
# add your OPENAI_API_KEY to .env
```

## Usage

```bash
analyze "Build a chat app with authentication and file sharing"
```

Output:
```json
{
  "features": ["chat", "authentication", "file sharing"],
  "modules": ["messaging service", "auth module", "storage"]
}
```

## Tests

```bash
pytest tests/ -v
```
