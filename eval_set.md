# Eval Set: Slack Message Formalizer

---

## Case 1 — Normal Case

**Input:** "hey can u send me that thing we talked abt asap"

**Expected output:** "Could you please send me the item we discussed at your earliest convenience?"

**Note:** Good output should fix abbreviations ("u" → "you", "abt" → "about"), replace "asap" with formal phrasing, and preserve the request without adding extra sentences or a sign-off.

---

## Case 2 — Normal Case

**Input:** "yo the meeting got moved to 3 fyi"

**Expected output:** "Just a heads-up — the meeting has been rescheduled to 3:00 PM."

**Note:** Good output should drop the casual openers ("yo", "fyi"), convey the notification concisely, and not add a greeting, closing, or instructions to update a calendar.

---

## Case 6 — Edge Case (Already Professional)

**Input:** "Please be advised that the project deadline has been moved to Friday, April 18th. Kindly plan accordingly."

**Expected output:** The message should be returned largely unchanged, with only minor adjustments if any.

**Note:** Good output should recognize that the message is already professional and avoid over-editing. Rewriting it in a noticeably different style or adding content would be a failure. Ideally the model returns it verbatim or with only trivial rephrasing.

---

## Case 7 — Likely Failure Case (Sarcasm)

**Input:** "oh great another meeting"

**Expected output:** A formalized version that captures the negative sentiment, e.g. "I note that another meeting has been scheduled." or "I wanted to flag that the volume of meetings continues to be a concern."

**Note:** Good output should preserve the critical or unenthusiastic tone rather than converting it into something that sounds positive or neutral. A likely failure mode is the model producing something like "I'm looking forward to the upcoming meeting," which inverts the meaning entirely. The model has no reliable way to know the speaker's intent, so a conservative, neutral-but-not-positive rendering is acceptable.
