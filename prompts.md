# Prompt Revision History: Slack Message Formalizer

---

## Initial Version

```
You are a professional business communication assistant.
Your job is to rewrite casual Slack messages into polished, professional workplace emails or messages.
Keep the same meaning and intent, but use formal grammar, proper punctuation, and a respectful tone.
Do not add unnecessary filler. Return only the rewritten message, nothing else.
```

### Eval Outputs (Initial)

| Case | Input | Output |
|------|-------|--------|
| 1 | hey can u send me that thing we talked abt asap | Could you please send me the document we discussed at your earliest convenience? Thank you. |
| 2 | yo the meeting got moved to 3 fyi | Dear team, Please be advised that the meeting has been rescheduled to 3:00 PM. Kindly update your calendars accordingly. Thank you. |
| 3 | i think the client is kinda upset abt the delay lol | I believe the client may be dissatisfied regarding the delay in our timeline. It would be advisable to address their concerns promptly. |
| 4 | can someone pls fix the bug its been like forever | Could someone please look into resolving this bug? It has been outstanding for quite some time now. I would appreciate any updates on the progress or an estimated timeline for the fix. |
| 5 | btw i wont be in tmrw, just so u know | Just wanted to let you know that I will not be in tomorrow. Please feel free to reach out if you need anything in the meantime. |

### What Went Wrong
The model over-formalized outputs, adding greetings ("Dear team"), sign-offs ("Thank you."), and unsolicited advice ("It would be advisable to address their concerns promptly.") not present in the original messages. Outputs were significantly longer than the inputs.

---

## Revision 1

**Change:** Added `Be concise — match the brevity of the original message.`

```
You are a professional business communication assistant.
Your job is to rewrite casual Slack messages into polished, professional workplace emails or messages.
Keep the same meaning and intent, but use formal grammar, proper punctuation, and a respectful tone.
Be concise — match the brevity of the original message.
Do not add unnecessary filler. Return only the rewritten message, nothing else.
```

### What Changed and Why
Added a direct brevity instruction. The initial prompt said "do not add unnecessary filler" but did not give the model a clear signal about length relative to the input. The new instruction explicitly ties output length to input length.

### Eval Outputs (Revision 1)

| Case | Input | Output |
|------|-------|--------|
| 1 | hey can u send me that thing we talked abt asap | Could you please send me the item we discussed at your earliest convenience? |
| 2 | yo the meeting got moved to 3 fyi | The meeting has been rescheduled to 3:00 for your awareness. |
| 3 | i think the client is kinda upset abt the delay lol | I believe the client is somewhat frustrated about the delay. |
| 4 | can someone pls fix the bug its been like forever | Could someone please look into this bug? It has been outstanding for quite some time. |
| 5 | btw i wont be in tmrw, just so u know | Just a heads-up — I won't be in tomorrow. |

### What Improved
- Extra sentences eliminated across all cases
- "Dear team" greeting and "Thank you." sign-offs removed
- Outputs now closely match the length and scope of the inputs
- Cases 1, 3, 4 noticeably cleaner

### What Stayed the Same / Remaining Issues
- Case 5 still uses a contraction ("won't") instead of fully formal "will not"
- Case 2 adds "for your awareness" which wasn't implied by the original
- No explicit rule preventing greetings or sign-offs — the model is complying by inference, not instruction

---

## Revision 2

**Change:** Added `Do not add greetings, sign-offs, or sentences not implied by the original message.`

```
You are a professional business communication assistant.
Your job is to rewrite casual Slack messages into polished, professional workplace emails or messages.
Keep the same meaning and intent, but use formal grammar, proper punctuation, and a respectful tone.
Be concise — match the brevity of the original message.
Do not add greetings, sign-offs, or sentences not implied by the original message.
Do not add unnecessary filler. Return only the rewritten message, nothing else.
```

### What Changed and Why
Made the constraint against greetings and sign-offs explicit rather than implicit. Revision 1 reduced extra content significantly, but the model could still add phrases like "for your awareness" that weren't in the original. This revision closes that gap with a specific, enumerated rule.

### Eval Outputs (Revision 2)

| Case | Input | Output |
|------|-------|--------|
| 1 | hey can u send me that thing we talked abt asap | Could you please send me the item we discussed at your earliest convenience? |
| 2 | yo the meeting got moved to 3 fyi | Please be advised that the meeting has been rescheduled to 3:00. |
| 3 | i think the client is kinda upset abt the delay lol | I believe the client is somewhat frustrated about the delay. |
| 4 | can someone pls fix the bug its been like forever | Could someone please address this bug? It has remained unresolved for quite some time. |
| 5 | btw i wont be in tmrw, just so u know | Just wanted to let you know that I will not be in tomorrow. |

### What Improved
- Case 2: "for your awareness" padding gone; replaced with the more standard "Please be advised"
- Case 4: Slightly tighter phrasing ("address this bug" vs "look into this bug")
- No greetings or sign-offs in any case

### What Stayed the Same / Remaining Issues
- Case 5 reverted slightly — "Just wanted to let you know" is still an added phrase not in the original; Revision 1 had "Just a heads-up" which was closer to the casual register
- Case 3 unchanged from Revision 1 ("somewhat frustrated" vs expected "concerned") — tone interpretation persists regardless of structural prompt rules
- The explicit no-greetings/sign-offs rule helped Case 2 but had mixed effects elsewhere
