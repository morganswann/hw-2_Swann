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
