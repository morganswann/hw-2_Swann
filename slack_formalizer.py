import anthropic

client = anthropic.Anthropic()

SYSTEM_PROMPT = """You are a professional business communication assistant.
Your job is to rewrite casual Slack messages into polished, professional workplace emails or messages.
Keep the same meaning and intent, but use formal grammar, proper punctuation, and a respectful tone.
Be concise — match the brevity of the original message and do not add extra sentences, sign-offs, or unsolicited advice.
Do not add unnecessary filler. Return only the rewritten message, nothing else."""

def formalize_message(casual_message: str) -> str:
    """Takes a casual Slack message and returns a professional version."""
    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=[
            {"role": "user", "content": f"Rewrite this message professionally:\n\n{casual_message}"}
        ]
    )
    return message.content[0].text


def run_eval(eval_cases: list[dict]) -> None:
    """Runs the formalizer on a list of eval cases, prints results, and saves to results.txt."""
    header = "=" * 60
    title = "SLACK MESSAGE FORMALIZER — EVAL RUN"

    print(header)
    print(title)
    print(header)

    lines = [header, title, header]

    for i, case in enumerate(eval_cases, 1):
        output = formalize_message(case["input"])

        case_lines = [
            f"\n[Case {i}]",
            f"INPUT:    {case['input']}",
            f"EXPECTED: {case['expected']}",
            f"OUTPUT:   {output}",
            "-" * 60,
        ]

        for line in case_lines:
            print(line)
        lines.extend(case_lines)

    with open("results.txt", "w") as f:
        f.write("\n".join(lines) + "\n")
    print("\nResults saved to results.txt")


# Sample eval cases
EVAL_CASES = [
    {
        "input": "hey can u send me that thing we talked abt asap",
        "expected": "Hi, could you please send me the document we discussed at your earliest convenience? Thank you."
    },
    {
        "input": "yo the meeting got moved to 3 fyi",
        "expected": "Just a heads-up — the meeting has been rescheduled to 3:00 PM."
    },
    {
        "input": "i think the client is kinda upset abt the delay lol",
        "expected": "I believe the client may be concerned about the recent delay."
    },
    {
        "input": "can someone pls fix the bug its been like forever",
        "expected": "Could someone please look into resolving this bug? It has been outstanding for quite some time."
    },
    {
        "input": "btw i wont be in tmrw, just so u know",
        "expected": "Just a quick note — I will not be available tomorrow."
    },
]


if __name__ == "__main__":
    # Run eval
    run_eval(EVAL_CASES)

    # Interactive mode
    print("\n\n[INTERACTIVE MODE] Type a casual message to formalize (or 'quit' to exit):")
    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() in ("quit", "exit", "q"):
            break
        if user_input:
            result = formalize_message(user_input)
            print(f"Formalized: {result}")
