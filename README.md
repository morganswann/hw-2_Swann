# HW-2: Slack Message Formalizer

A Claude-powered tool that rewrites casual Slack messages into polished, professional workplace communications.

## Business Workflow

**Workflow:** Slack Message Formalization

**User:** A workplace employee who needs to communicate professionally but writes in casual, shorthand style.

**Input:** A casual Slack message (e.g., "hey can u send me that thing we talked abt asap")

**Output:** A professional rewritten message (e.g., "Could you please send me the item we discussed at your earliest convenience?")

**Value:** Saves time and reduces communication errors in professional settings by instantly converting informal language into clear, respectful, grammatically correct messages — without the employee needing to manually rephrase each one.

## Usage

```bash
python3 slack_formalizer.py
```

Runs a built-in eval suite followed by an interactive mode where you can type any casual message and receive a formalized version.

## Requirements

- Python 3
- `anthropic` package (`pip install anthropic`)
- `ANTHROPIC_API_KEY` environment variable set
