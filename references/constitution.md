<!-- sync-source: constitution.zh-CN.md sha256:7de29b17d427 -->

# Constitution

These are meta-rules. They do not govern "how to write a prompt" — they govern
**how this skill is used**. Every one of them takes precedence over any specific
advice found elsewhere in this skill. **When specific advice conflicts with the
constitution, the constitution wins.**

Twelve rules, in three groups.

---

## Group 1 · On examples (four rules)

### 1. An example is not DNA — it is one sample of the skin

Every concrete element anywhere in this skill — a term, a set of overlay
elements, a vocabulary list, a negative — is **one film's fill**, not a default,
not a recommendation, not a starting point.

**No concrete element from any example enters your spec unless you independently
decided this film needs it.**

Test: delete the example entirely — can you still write this slot from the film
itself? If not, you have not thought the slot through, and copying the example
only papers over the blank.

> Not fastidiousness. Observed: while filling slots for a film that speaks
> through **a wide colour field and extreme negative space**, the example from a
> film built on **dense information layering** was copied across — prescribing
> "full" for a film that works by being "empty". Every slot was filled, every
> end state was met, and the entire direction was inverted.

### 2. Fill order is "write first, look second"

**Look only at this film and write the slot. Only after it is written may you
open the examples.**

Looking at examples has exactly two legitimate uses: checking whether you missed
a whole category, and checking whether your wording is verifiable enough. It is
not "filling it in with reference to". Reverse the order and the example becomes
the default answer.

### 3. Isolate examples physically, not by self-discipline

The first two rules are discipline, and discipline fails. So the structure
blocks it too: **no copyable concrete element appears in this skill's main
text** — term strings, prohibition wordings, overlay lists, texture words,
complete shot breakdowns all live only in the isolation area
[case-library.zh-CN.md](case-library.zh-CN.md).

The main text keeps two things: **structural skeletons** (as placeholders) and
**the shape of a failure** (for example "the lock was fully satisfied and
completely ineffective" — that cannot be copied, only understood).

To decide whether a passage stays or gets isolated, ask: **could this be pasted
straight into another film's prompt?** Yes → isolation area. No → it may stay.

⚠️ **A rule can be a skin too.** A specific technique rule or a specific
negative wording is a copyable concrete element **even when it appears as a
counter-example** — this is the category isolation checks skip most often,
because it reads like a "rule" rather than an "element".

Three dispositions, not two:

| Situation | Disposition |
|---|---|
| One film's specific fill, with measurements behind it | **Isolate** (case library / observations) |
| Specific but pointing at **general human bodies or general interfaces**, not at any one film | May stay in the main text (e.g. which body parts carry observable cues; reference-addressing anti-patterns) |
| **Unvalidated but written as a rule**, or already overturned by measurement | **Delete.** It belongs to no film's fill, and keeping it in the isolation area merely relocates the error |

The isolation area is **grouped by film, not by slot**. This is deliberate: to
use one of its entries you must first admit "my film is the same class as this
one", and that admission is itself a filter.

### 4. Adjacent slots must not draw examples from the same film

(This one is for maintainers.) When one film appears too many times in this
skill it becomes the default answer — the reader is no longer filling slots,
they are completing a template they have already seen five times.

Maintenance rule: **each slot's example comes from a different film, and
adjacent slots especially must not share a source.** No single film should
appear noticeably more often than the others.

---

## Group 2 · On slots (three rules)

### 5. No slot is mandatory

Before filling any slot, ask: **does this film need it?**

If the answer is no, leave it empty. **Empty is a decision, not an omission.**
This skill must not diagnose an empty slot as a defect — absence is not a
symptom in itself.

A corollary: do not fill a slot merely because it is there. The slot table is a
list of available tools, not a to-do list.

### 6. The slot set is open — add a slot rather than force-fit

The slot table is **the result of one round of generalisation**, not an
exhaustive set. When content fits no existing slot, **add one**.

⚠️ **The most common error is not "there is no slot for this" — it is forcing it
into the nearest one.** Force-fitting is a variant of rule 7: once content sits
in a slot with a different scope, its scope is wrong too.

Three questions before adding:

1. **What range does it govern?** The whole film / something that must not
   drift / one beat — this decides its bucket
2. **Which existing slot has the same scope?** One does → use it, do not create.
   None does → create
3. **Can it be checked?** No → rewrite it per
   [verifiability](verifiability.zh-CN.md) first, then decide where it goes

Against bloat: if you cannot say what the new slot governs *and* how it differs
from every existing slot, do not create it.

### 7. Wrong bucket is the number-one error

Bucket 1 or 2 content written into bucket 3 stops working at the next beat.

This is not a style question, it is a **scope** question — and the symptom
deceives: the first few beats are perfectly correct, then it vanishes.

Which bucket a line belongs to depends on how much it governs, not on what it
looks like.

---

## Group 3 · On boundaries (five rules)

### 8. A model profile never deletes a slot from the master

A slot failing on one model is **a fact about that profile**, not grounds for
the master to drop the slot.

> The observation that triggered this rule: one model's audio track did not
> follow the BPM values given in the prompt, so it was proposed that the
> audio/music slot was "unsolvable on this route". Two errors in one inference:
> this skill serves every model that can be called, so **one model's behaviour
> is not grounds for deleting a slot**; and that observation covered only the
> audio track, while **the slot turned out to be doing its real work on the
> picture's rhythm** (see rule 9). The correct handling is to record the
> observation in that profile and leave the master untouched.

Likewise: an anti-default suffix, a negative wording, or an addressing dialect
that works on one model must not be promoted into the master. **The master holds
only what is model-independent**; everything else goes to a profile's bias
layer.

### 9. Do not write your belief about model capability into a rule

A profile records **what was observed**, never **"so this slot is useless"**.
The latter is a cross-slot causal claim, and any single observation is
single-slot.

Two reasons:

**① A slot's effect overflows its own scope.** A prompt is not executed
slot-by-slot — something written in the audio slot may change the picture's
rhythm; something in the style slot may change cutting density. So "this slot
does not work on this model" is unreliable on its face: you measured its effect
**on that slot**, not its effect **elsewhere**.

> Observed: one model's music section was judged "ineffective, deletable to save
> prompt budget" (the specified BPM and drum entries did not materialise). A
> later controlled comparison — same spec, one beat-skeleton section appended,
> everything else word-for-word identical — showed it changed the picture:
> cut-point count +23%, standard deviation of interval −26%, baseline motion
> +17%. **The "ineffective" verdict measured audio-track adherence, while its
> real effect was on the picture's rhythm.**

**② Whether to write a slot depends on whether it serves what this film needs,
not on some model's capability.** This skill serves every model that can be
called. Trimming a slot from the master because of one model's behaviour
promotes a single observation into a universal rule — precisely what
[rule 8](#8-a-model-profile-never-deletes-a-slot-from-the-master) forbids, only
in a better-hidden form.

An operating discipline: profiles say "**I wrote X, I observed Y**", never
"**X does not work**". The first is permanently true; the second gets overturned
by the next controlled comparison.

### 10. Write the spec in full first, then let hard constraints trigger a degrade

The order is fixed:

```
① Look only at what this film needs and write the spec in full
② Before submitting, let constraints that would actually error trigger a degrade
   (duration enum, resolution, aspect ratio, reference count, addressing syntax)
③ A degrade must be reported
```

**Only a hard constraint may trigger ②.** "I suspect this model handles it
poorly" is not a hard constraint and is not grounds for trimming the spec.

Doing it in reverse — reading the profile first, then deciding what to write —
is a class of invisible failure this skill has recorded: **"I did not write it
because I thought the model could not do it" leaves no trace in the output.**
A wrong copy is visible; an omission only shows up as "the effect fell short",
and you cannot find the cause, because that line was never there.

Two consequences:

- **Isolate observations**: bias-layer observations and failure modes live in
  [observations.zh-CN.md](observations.zh-CN.md), **not read while writing**,
  only during post-hoc diagnosis. It is the mirror image of the
  [case library](case-library.zh-CN.md) — the case library guards against
  **copying too much**, the observations file against **writing too little**
- **Measurement does not produce rules**: record what you measured, nothing
  more. **Do not derive a rule about "whether something should be written" from
  a sample of n=1 or n=2** — that promotes an observation into a rule, which
  rule 9 forbids

The purpose of this skill is to **get the effect this film needs**.

#### What determines severity: whether the user asked for it, not whether the model can do it

| Situation | Severity | Handling |
|---|---|---|
| **Something the user stressed from the start, left out** | **Most severe** | Not "slightly worse", but **not delivered** — and an omission leaves **no trace**: you see the wrong effect and cannot find the cause, because that line was never written |
| User did not stress it, it did not appear, and on watching you want it | **Normal** | **Just add it to the skin** — change this film's spec, run the next version. This is ordinary iteration, not failure |
| Written too much | Light | A longer prompt; visible and removable |

**Why this rule is one-directional** (it forbids "writing less because of an
observation", not "daring to write because of an observation"): both directions
are the same act — letting one observation decide the next step — but **the cost
of being wrong differs by an order of magnitude**. Rules are designed around
**cost**, not around logical symmetry — forbidding both directions would make
people afraid to write, which manufactures exactly the most severe failure in
the first row.

#### Companion: when something is missing, change the skin or the bone?

| The missing thing is | Change |
|---|---|
| **This film's requirement** (wanted now, not thought of last time) | **The skin.** Change the spec, run the next version |
| **Caused by this skill's structure** (no such slot, missing criterion, misleading example) | **The bone.** And you must be able to say "the next person will trip on the same spot" |

⚠️ Adding a rule to the bone every time something is missing bloats the bone
with one film's requirements. **Default to the skin**; touch the bone only when
the same pit will predictably trip the next person.

### 11. Do not promote one scenario's default into a global rule

A rule that is correct in the scenario it grew out of is not thereby correct
elsewhere.

**Test**: which **scenario** was this rule validated in? That scenario is its
scope, not everything.
**Handling**: keep it in that scenario's own entry; do not raise it to the
master.

**A corollary**: if two situations under the same scenario label have defaults
that point in **opposite** directions, they are two scenarios and must be named
apart — otherwise one inherits the other's default.

⚠️ **An unvalidated rule imported from an outside document must not appear in
this skill's main text in any form, including as a counter-example.** A
counter-example is equally copyable, and a counter-example learned from the
constitution carries the highest authority of all.

(This clause exists because this file broke it: two never-measured technique
rules imported from an outside document once sat here as counter-examples, and
were later overturned outright by measurement. They were deleted, not isolated —
**the isolation area holds "one film's fill", and a wrong rule is no film's
fill.**)

### 12. Rules do not replace review

What this skill reduces is wasted iteration — it fixes failures already paid for
so they need not be walked into again. **It does not sign off on output.**

Every rule has exceptions, exceptions are judgement, and the judgement belongs
to the person making the film. Especially **motion, pacing and overall tone** —
three things neither rules nor stills can cover.

A companion discipline: a conclusion drawn from extracted frames alone must
declare that it covers only the stills half (texture, composition, identity, end
states) and must not be presented as an overall verdict. Observed: stills
favoured model A on every measurable axis while the person watching playback
clearly preferred model B — the whole disagreement lived in motion and pacing.

---

## Related

- [workflow.zh-CN.md](workflow.zh-CN.md) — the main flow (Chinese; the English
  equivalent is [SKILL.md](../SKILL.md))
- [spec-format.zh-CN.md](spec-format.zh-CN.md) — slot table and criteria
- [film-type-dna.zh-CN.md](film-type-dna.zh-CN.md) — DNA versus skin (method)
- [film-types.zh-CN.md](film-types.zh-CN.md) — film-type library, isolation area
- [case-library.zh-CN.md](case-library.zh-CN.md) — example isolation area
- [observations.zh-CN.md](observations.zh-CN.md) — observation isolation area
- [../VALIDATION.zh-CN.md](../VALIDATION.zh-CN.md) — evidence strength per rule
- [model-profile-schema.zh-CN.md](model-profile-schema.zh-CN.md) — profile fields
