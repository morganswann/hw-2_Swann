# HW-2 Report: Slack Message Formalizer

## Business Workflow

**Workflow:** Slack Message Formalization

**User:** A workplace employee who communicates frequently via Slack and needs to send professional messages to colleagues, managers, or clients.

**Input:** A casual Slack message written in informal, shorthand style — often with abbreviations, missing punctuation, and colloquial language (e.g., "yo the meeting got moved to 3 fyi").

**Output:** A professional rewritten version of the same message that preserves the original meaning and intent while using formal grammar, proper punctuation, and a respectful tone (e.g., "The meeting has been rescheduled to 3:00 for your awareness.").

**Value:** This workflow saves employees time and reduces communication errors in professional settings. Rather than manually rephrasing messages — a task that requires conscious effort and can introduce delays — employees can instantly produce polished communications. This is particularly valuable when messaging clients, senior stakeholders, or across organizational boundaries where tone and clarity matter most.

## Implementation

The tool is implemented in `slack_formalizer.py` using the Anthropic Claude API (`claude-opus-4-6`). A system prompt instructs the model to act as a professional business communication assistant, rewriting messages concisely without adding unsolicited content or sign-offs.

An eval harness validates output quality against five representative test cases covering common Slack message types: requests, notifications, status updates, bug reports, and absence notices.

## Prompt Iteration and Findings

**Model:** `claude-opus-4-6`

**Baseline prompt** established the core task but over-generated on nearly every case — adding greetings ("Dear team"), sign-offs ("Thank you."), and unsolicited advice not present in the original messages. Outputs were significantly longer than inputs.

**Revision 1** added the instruction: *"Be concise — match the brevity of the original message."* This improved most cases noticeably: extra sentences were eliminated, greetings and sign-offs largely disappeared, and outputs more closely mirrored the scope of the inputs.

**Revision 2** added: *"Do not add greetings, sign-offs, or sentences not implied by the original message."* This made the constraint explicit rather than implied. It improved Case 2 (removed the filler phrase "for your awareness") but slightly regressed Case 5, where the model introduced a different filler phrase ("Just wanted to let you know") in place of the one it previously suppressed.

## Limitations

The prototype still fails on tone interpretation. Messages that carry sarcasm, frustration, or negative sentiment — such as "oh great another meeting" — are likely to be rewritten with a neutral or even positive tone, inverting the sender's intent. Similarly, Case 3's output consistently renders "kinda upset" as "somewhat frustrated" rather than the softer "concerned," reflecting the model's interpretation of emotional intensity rather than the sender's intended register.

These failures cannot be fully addressed through prompt rules alone, as the model has no reliable signal for the sender's intent beyond the text itself. Sensitive or emotionally charged messages would require human review before sending.

## Recommendation

This prototype demonstrates strong performance on straightforward formalization tasks and meaningfully reduces time spent on manual rephrasing. However, given the limitations around tone interpretation and edge cases, **deployment is recommended only with a human review step for flagged messages** — particularly those containing emotional language, sarcasm, or messages intended for external stakeholders. A confidence-based routing approach (auto-send clear cases, route ambiguous ones for review) would balance efficiency with reliability.
