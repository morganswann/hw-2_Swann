import anthropic

client = anthropic.Anthropic()

# Revision 2 (final) system prompt
SYSTEM_PROMPT = """You are a professional business communication assistant.
Your job is to rewrite casual Slack messages into polished, professional workplace emails or messages.
Keep the same meaning and intent, but use formal grammar, proper punctuation, and a respectful tone.
Be concise — match the brevity of the original message.
Do not add greetings, sign-offs, or sentences not implied by the original message.
Do not add unnecessary filler. Return only the rewritten message, nothing else."""

def formalize_message(casual_message: str, system_prompt: str = None) -> str:
    """Takes a casual Slack message and returns a professional version."""
    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1024,
        system=system_prompt or SYSTEM_PROMPT,
        messages=[
            {"role": "user", "content": f"Rewrite this message professionally:\n\n{casual_message}"}
        ]
    )
    return message.content[0].text


def run_eval(eval_cases: list[dict], output_file: str = "results.txt", system_prompt: str = None) -> None:
    """Runs the formalizer on a list of eval cases, prints results, and saves to output_file."""
    header = "=" * 60
    title = "SLACK MESSAGE FORMALIZER — EVAL RUN"

    print(header)
    print(title)
    print(header)

    lines = [header, title, header]

    for i, case in enumerate(eval_cases, 1):
        output = formalize_message(case["input"], system_prompt)

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

    with open(output_file, "w") as f:
        f.write("\n".join(lines) + "\n")
    print(f"\nResults saved to {output_file}")


# Eval cases (matches eval_set.md Cases 1–7)
EVAL_CASES = [
    {   # Case 1 — Normal
        "input": "hey can u send me that thing we talked abt asap",
        "expected": "Could you please send me the item we discussed at your earliest convenience?"
    },
    {   # Case 2 — Normal
        "input": "yo the meeting got moved to 3 fyi",
        "expected": "Just a heads-up — the meeting has been rescheduled to 3:00 PM."
    },
    {   # Case 3 — Edge Case (Already Professional)
        "input": "Please be advised that the project deadline has been moved to Friday, April 18th. Kindly plan accordingly.",
        "expected": "Please be advised that the project deadline has been moved to Friday, April 18th. Kindly plan accordingly."
    },
    {   # Case 4 — Normal
        "input": "hey can we move our 2pm tmrw? something came up",
        "expected": "Would it be possible to reschedule our 2:00 PM meeting tomorrow? Something has come up on my end."
    },
    {   # Case 5 — Normal
        "input": "just finished the report fyi, its in the shared folder",
        "expected": "Just a heads-up — the report has been completed and is available in the shared folder."
    },
    {   # Case 6 — Normal
        "input": "hey can u take a look at my draft and let me know what u think",
        "expected": "Could you please review my draft and share your feedback when you get a chance?"
    },
    {   # Case 7 — Likely Failure (Sarcasm)
        "input": "oh great another meeting",
        "expected": "I note that another meeting has been scheduled."
    },
]

PROMPT_INITIAL = """You are a professional business communication assistant.
Your job is to rewrite casual Slack messages into polished, professional workplace emails or messages.
Keep the same meaning and intent, but use formal grammar, proper punctuation, and a respectful tone.
Do not add unnecessary filler. Return only the rewritten message, nothing else."""

PROMPT_REVISION_1 = """You are a professional business communication assistant.
Your job is to rewrite casual Slack messages into polished, professional workplace emails or messages.
Keep the same meaning and intent, but use formal grammar, proper punctuation, and a respectful tone.
Be concise — match the brevity of the original message.
Do not add unnecessary filler. Return only the rewritten message, nothing else."""

PROMPT_REVISION_2 = SYSTEM_PROMPT


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
