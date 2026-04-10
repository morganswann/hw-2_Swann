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

## Case 3 — Edge Case (Already Professional)

**Input:** "Please be advised that the project deadline has been moved to Friday, April 18th. Kindly plan accordingly."

**Expected output:** The message should be returned largely unchanged, with only minor adjustments if any.

**Note:** Good output should recognize that the message is already professional and avoid over-editing. Rewriting it in a noticeably different style or adding content would be a failure. Ideally the model returns it verbatim or with only trivial rephrasing.

---

## Case 5 — Normal Case

**Input:** "hey can we move our 2pm tmrw? something came up"

**Expected output:** "Would it be possible to reschedule our 2:00 PM meeting tomorrow? Something has come up on my end."

**Note:** Good output should replace casual phrasing ("hey", "tmrw") with formal equivalents, preserve the reason given without elaborating on it, and not add a sign-off or apology not present in the original.

---

## Case 6 — Normal Case

**Input:** "just finished the report fyi, its in the shared folder"

**Expected output:** "Just a heads-up — the report has been completed and is available in the shared folder."

**Note:** Good output should convert "fyi" and "just finished" into professional phrasing, preserve both pieces of information (completion and location), and not add extra context or a greeting.

---

## Case 7 — Normal Case

**Input:** "hey can u take a look at my draft and let me know what u think"

**Expected output:** "Could you please review my draft and share your feedback when you get a chance?"

**Note:** Good output should formalize "take a look" and "let me know what u think" into professional equivalents, drop the casual opener, and not add urgency or a deadline not implied by the original.

---

## Case 4 — Likely Failure Case (Sarcasm)

**Input:** "oh great another meeting"

**Expected output:** A formalized version that captures the negative sentiment, e.g. "I note that another meeting has been scheduled." or "I wanted to flag that the volume of meetings continues to be a concern."

**Note:** Good output should preserve the critical or unenthusiastic tone rather than converting it into something that sounds positive or neutral. A likely failure mode is the model producing something like "I'm looking forward to the upcoming meeting," which inverts the meaning entirely. The model has no reliable way to know the speaker's intent, so a conservative, neutral-but-not-positive rendering is acceptable.
