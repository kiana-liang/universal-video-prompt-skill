# Universal Video Prompt Skill

<p align="center">
  <b>English</b> · <a href="README.zh-CN.md">简体中文</a>
</p>

**You can copy the prompt. You can't copy the decisions behind it.**

Take a video apart back into its decisions, swap in your own subject, then compile it for whichever model you can actually call.

https://github.com/user-attachments/assets/c521d487-b6fb-403b-8994-9ef484b8f7c0

<sub>Editorial-MG title sequence. Every named term in its film-type synthesis is a loan with interest — you borrow the visual priors, and the default bias comes with them. What holds the style is not the terms but the counterweights written next to them.</sub>

---

## What it's for

### 1. You copied a viral video's prompt and still can't reproduce it

What you copied is the **wording**. What you couldn't copy is the **decision logic** behind it — why *this* term and not that one, which things must never drift, what has to be visible on screen when each stage ends. None of that is in the literal text of a prompt, and all of it determines the result.

So the first use is **working backwards**: recover that set of decisions from a finished video, a reference image, or someone else's prompt, then swap in your own subject and recompile.

⚠️ Working backwards has a trap specific to it: **the precision you can measure on a finished video is not the precision that belongs in your spec.** Measure frame-level audio sync in someone else's piece, copy it in as second-level timestamps, and your version comes out *worse* — because that precision may not have come from the prompt at all. So it takes one extra step, attribution: **did this characteristic come from the prompt, or from the model?**

### 2. A style worked, and you want to reuse it on new subjects

Swapping the subject feels like you only changed the subject. In practice it's very easy to carry the previous film's **art direction** across with it.

This went wrong once for real: the new subject needed *empty* — big flat colour, a lot of negative space — while the style terms carried over pointed at *full*: high density, high saturation. Nearly opposite. The result was a "fill it up" prescription written for a film that speaks by holding back.

**The hard part is that line-by-line checking won't catch it.** Every constraint is working exactly as written; the direction they're working towards belongs to a different film. Full marks on the checklist, and the video is still wrong.

So re-skinning has a fixed procedure: pull out the few conditions this film type genuinely cannot lose (remove any one and it stops being itself), refill everything else from scratch, then **step back and check direction once more** — do these style terms point the same way this film does?

### 3. You wrote a lot, it came out wrong, and you don't know which line to change

Because most of those lines **can't be checked**. "Keep it consistent", "make it tense", "cinematic" — once it's generated you can't tell whether they took effect, so there's nothing to debug.

There's one core move: **rewrite the unverifiable as verifiable.**

| Don't write | Write instead |
|---|---|
| `keep it consistent` | the **visible** end state of each stage |
| `tense` | 2–4 observable cues: gaze, brow, mouth, breathing, hands |
| `make it faster` | a time budget per stage |
| `the slowest, quietest stage` | **what happens** in that stage, with tension carried by causality |

That last row is a measured lesson: a stage written as "the slowest, quietest stage of the film" was read by the model as **"nothing happens in this stage"** — it came back as the subject holding one pose and drifting slowly, with none of that stage's specified events occurring.

### 4. Several versions in, it keeps getting worse, and you can't say what changed

Because the changes are scattered through the prompt with nothing to diff against. A spec **is** a diffable record of decisions — change one thing per version and leave everything else word-for-word identical, and you can finally tell which change did the work.

It's also the only way the sentence "this version is better" holds up.

### 5. The good model is too expensive to gamble on

One roll of the dice on a flagship model pays for ten runs on a cheap one. **Iterate on the cheap one, then run the finished spec on the expensive one** — which only works if both runs use the same spec and you're changing the compile target, not rewriting.

---

## What's inside

**5 film-type DNAs · 4 fully-run cases · 6 model profiles · 20 measured entries.**

The case library isn't templates. It's **prompts that actually ran, together with what they produced** — each entry records *what was written* and *what was observed*:

- **Four models on one identical prompt**, word for word (same spec, submission parameters only)
- One **four-segment chain**, iterated across six versions
- One **complete spec with six of seven global slots filled**, including nine timed stages and an end state for each
- 6 model profiles: SD2.0 / SD2.5 / MiniMax H3 / HappyHorse 1.1 / Kling v3.0 Pro / Turbo
  — addressing syntax, duration ceilings, timing adherence, asset input format, known failure modes
- A zero-dependency rhythm measurement script (`tools/analyze_rhythm.py`), so the numeric findings can be reproduced

Six further entries demonstrate shape only and are **marked as unmeasured** — they show what a slot looks like, not that writing it that way works.

### Four models, one identical prompt

https://github.com/user-attachments/assets/08c4c8d0-f8bc-4d11-8235-e54bfd314ff3

<sub>Same spec, same prompt text, only the submission parameters changed. The differences you see are the models — which is the whole reason a comparison has to be run in one shared execution environment. The full profiles are in <code>examples/cross-model/</code>.</sub>

### A four-segment chain

https://github.com/user-attachments/assets/94c26ae9-0238-40a5-830c-6ece71c25187

<sub>Four segments chained on boundary frames, six versions of iteration. Chaining is not extension: an extension hides the seam, whereas here the seam <em>is</em> the hard cut. Every subject carried over gets an explicit continue-or-clear — write neither and it stays, possibly amplified.</sub>

### One complete spec, start to finish

https://github.com/user-attachments/assets/6912dd5f-757d-4789-bad0-3d91a1c97608

<sub>Nine stages, an end state for each, six of seven global slots filled. The seventh — the director's premise — is empty, and that empty slot is the most instructive thing about this case: no slot is mandatory. Reverse-engineered from one reference film, written before the case library was opened.</sub>

---

## What a "spec" is

It isn't a prompt. It's **the decisions a prompt encodes** — stored separately from the wording that expresses them.

| | Spec | Prompt |
|---|---|---|
| Contents | The lead wears the same coat throughout; by the end of stage 2 the knife is already on the table; the reference controls the face but not the background | `@image1 controls the character's face, hair and coat. Do not take its background or composition.` |
| Relation to the model | **None.** Changing models doesn't change it | **Direct.** It varies per model |
| Form | A slot table in three layers | A block of text you can paste and run |

So the whole idea is: **write the decisions once, translate the rest per model.**

That "rest" is worth naming, because it's where cross-model work goes wrong. Three kinds: **addressing syntax** (`@image1` versus `Reference Image 1`), **anti-default wording** (phrases that fight one specific model's habits), and **duration and resolution enums**. All three differ from vendor to vendor; this skill calls them collectively the **dialect** — translated at compile time, never written into the spec.

> 📌 In the Chinese documentation this concept is called **决策清单** (literally "decision list"). Same thing, two names. **File names stay English** — `spec-format.zh-CN.md` is the Chinese text about specs.

---

## Where to start

1. Install it (see [Install](#install)), then just tell your agent what you want — "work this video backwards into a spec", "take this style and put it on a cat"
2. If you'd rather read first: [`SKILL.md`](SKILL.md) for the main flow → [`constitution.md`](references/constitution.md) for the twelve meta-rules → [`spec-format.md`](references/spec-format.md) for the slot table
3. **If you want to judge how solid it is first**: [`VALIDATION.zh-CN.md`](VALIDATION.zh-CN.md) marks every rule with its evidence strength — ✅ controlled comparison / ⚠️ reasoned default / ❌ unvalidated

---

## Two questions for every line you write

### One: how much does this line govern?

Getting the scope wrong is the most common cause of drift, and the symptom is deceptive: the first few stages are perfectly correct, then it vanishes.

| Layer | Governs | Contents |
|---|---|---|
| ① Global | The whole video | Film type, scene, style, director's premise, camera principle, 〔as needed〕persistent overlay, 〔as needed〕technique vocabulary |
| ② Locks | Anything that must not drift | Identity, 〔if refs〕reference roles, audio source, 〔if any〕supporting cast, continuity, 〔if content risk〕negatives |
| ③ Time | One stage | Stage events, end state per stage |
| **+** | Whatever the rows above can't hold | **Slots you add**, placed in the layer owning their scope |

**A global rule written into stage 1 stops applying at stage 4.**

> 📌 Internally the skill calls these three layers "buckets ①②③". Same thing.

### Two: after it generates, can this line be checked on the output?

A line you can't check is a line you can't debug. See the table in section 3 above for how to rewrite.

⚠️ **Verifiable doesn't mean you locked the right property.** A lock can be fully satisfied and completely ineffective — measured: locking "stay flat, don't render realistically" was obeyed strictly by two different models, both returning smooth vector outlines. Flat? Yes. Hand-drawn? Not at all. The lock aimed at *flatness*, while the property carrying the concept was *visible tool marks*.

**The test: could the model satisfy this sentence and still lose the thing I want?** If yes, the lock is aimed at a side effect rather than a cause.

---

## What a spec looks like

Three layers, each with several slots:

```text
[① GLOBAL]
  film type:        multi-axis term synthesis + a reference-object anchor
                    + counterweights for each term
  scene:            where, when
  style:            visual treatment, palette, how light behaves (only what is visible)
  premise:          one sentence — the thought this film exists for
  camera principle: the rule governing the whole film, not a shot list
  persistent overlay: 〔as needed〕the layer pressed onto every frame,
                    and how that layer itself moves
  technique vocab:  〔as needed〕named effects and transitions the film may draw on

[② LOCKS]
  identity:         who or what must not change, and by which invariants
  reference roles:  〔if refs〕per asset — what it controls, what must not be taken
  audio source:     native, external track, or silent
  supporting cast:  〔if any〕position, and what they must not do
  continuity:       what must hold for the whole film
  negatives:        〔if content risk〕specific risks only

[③ TIME]
  granularity:      none | stages | second-level   (decide before writing the rest)
  stage 1..n:       one primary change each
  end state:        what is visible when this stage stops

[+ ADDED SLOTS]     what this film needs that the rows above cannot hold
```

**This table is a list of available tools, not a to-do list.** No slot is mandatory — empty is a decision, not an omission; and when something fits nothing, add a slot rather than forcing it into the nearest one.

In the complete example in the case library, one of the seven global slots is empty — and **that empty slot is the most instructive thing about it.**

---

## Bone and skin: the part that makes this different

Two words first, because everything below runs on them:

> **Bone = the reusable method.** Criteria, structure, the shape of a failure. Still true on a different film.
> **Skin = one film's specific fill.** Term strings, prohibition wordings, element lists, complete shot breakdowns. True only for that film.

A typical prompt repository hands you a pile of examples to copy. **This one does the opposite — everything copyable is locked in an isolation area, and the main text keeps only bone.**

The reason is the failure in section 2: its root cause was **document structure, not carelessness**. When examples and method sit on the same page, people fill from the examples. "Remind yourself to be careful" doesn't hold; only structure does.

| Isolation area | Guards against | Header |
|---|---|---|
| [`case-library.zh-CN.md`](references/case-library.zh-CN.md) | **Copying too much.** Every copyable concrete element lives here | ⛔ Write your own slots first |
| [`film-types.zh-CN.md`](references/film-types.zh-CN.md) | **Loading the wrong skin.** Five skins already run, grouped by type | ⛔ Confirm same class before opening |
| [`observations.zh-CN.md`](references/observations.zh-CN.md) | **Writing too little.** Per-model observations and failure modes | ⛔ Not read while writing |

The third is the counter-intuitive one: **why isolate "my understanding of what the model can do"?**

Because **writing too little is harder to notice than copying too much**. A wrong copy is visible. But "I didn't write it because I thought the model couldn't do it" leaves **no trace in the output** — you only see the effect fall short, and you can't find the cause, because that line was never there.

The isolation areas are **grouped by film, not by slot**. That's deliberate: to use one of their entries you first have to admit "my film is the same class as this one", and that admission is itself a filter.

---

## The constitution: twelve meta-rules

Rules conflict once there are enough of them, so there's a layer governing *how the rules are used*. The constitution **overrides any specific advice elsewhere in this skill**.

**On examples (four)**

1. An example is not DNA — it's **one sample of the skin**
2. Fill order is **write first, look second** — write the slot from this film alone, and only then open the examples
3. Isolate examples **physically**, not by self-discipline. **A rule can be a skin too**
4. Adjacent slots must not draw examples from the **same film**

**On slots (three)**

5. **No slot is mandatory** — empty is a decision
6. **The slot set is open** — add one rather than force-fit
7. **Wrong layer is the number-one error**

**On boundaries (five)**

8. A model profile **never deletes a slot from the master** — a slot failing on one model is a fact about that profile
9. Don't write *your belief about model capability* into a rule — a profile records "I wrote X, I observed Y", never "X doesn't work"
10. **Write the spec in full first, then let hard constraints trigger a degrade.** "I suspect this model handles it poorly" is not a hard constraint
11. Don't promote **one scenario's default** into a global rule
12. **Rules don't replace review**

Full text → [`references/constitution.md`](references/constitution.md)

### Why rule 10 is one-directional

It forbids "writing less because of an observation" but not "daring to write because of one" — both are the same act, letting one observation decide the next step, but **the cost of being wrong differs by an order of magnitude**:

| Situation | Severity |
|---|---|
| Something the user stressed, left out | **Most severe.** Not "slightly worse" but **not delivered** — and it leaves **no trace** in the output |
| Not stressed, wanted on watching | Normal. Add it to the skin; this is ordinary iteration |
| Written too much | Light. Visible and removable |

**Rules are designed around cost, not around logical symmetry.**

---

## The three layers that change when you change models

The spec is portable; the lines inside it are not all portable. The most common cross-model error is **treating a bias-layer line as a language-layer line** — copying an anti-default suffix that worked on one model to another and assuming it still helps.

| Layer | Contents | Handling | Stored in |
|---|---|---|---|
| **Language** | Three-layer structure, end states, observable cues, term-plus-description | Portable as written | The spec |
| **Bias** | Anti-default suffixes, negatives, transition vocabulary, addressing dialect | One profile per model, **measured only** | The profile |
| **Capability** | Reference count, multi-shot, hard cuts, duration, timing adherence | Probe, then degrade | The profile |

**The dialect-proof pattern is term plus observable description.** A model that knows the term takes the shortcut; one that doesn't follows the description. One prompt serves both.

⚠️ **Published enums are assumptions, not limits.** Documented ranges are often narrower than what the API accepts, and a single page can contradict itself (one page was observed stating three different duration ranges in three places). **Submit the value you actually want and let the API answer.**

> ⚠️ But "rejected means no task and no charge" **only holds on a direct vendor route**. On an aggregator it may not: the gateway doesn't validate at submit time, returns success, creates the task, and the upstream rejects it afterwards. **"Task created" does not mean the parameter was accepted** — so when probing limits through an aggregator, test that parameter with the shortest duration and lowest resolution rather than with a full job.

---

## Repository layout

```text
universal-video-prompt-skill/
├── SKILL.md                          entry point, language routing
├── VALIDATION.zh-CN.md               evidence strength per rule + change log
├── SYNC-STATUS.md                    zh/en sync status (generated)
├── references/
│   ├── constitution.*                ⭐ twelve meta-rules, override everything
│   ├── workflow.zh-CN.md             Chinese main flow
│   ├── spec-format.*                 slot table, criteria, skeletons
│   ├── slot-filling.*                filling empty slots; working backwards
│   ├── verifiability.*               end states, observable cues, mechanism vs effect
│   ├── portability.*                 the three layers, probes, degrading
│   ├── film-type-dna.*               extracting DNA, re-skinning
│   ├── model-profile-schema.*        profile field definitions
│   ├── execution.*                   provider routes, polling, resume
│   ├── checklist.*                   pre-submission review
│   ├── case-library.zh-CN.md         ⛔ isolation · copyable elements
│   ├── film-types.zh-CN.md           ⛔ isolation · five skins already run
│   └── observations.zh-CN.md         ⛔ isolation · per-model observations
├── examples/cross-model/             frozen snapshot of a four-model comparison
└── tools/
    ├── analyze_rhythm.py             objective rhythm measurement, zero deps
    └── check-sync.py                 zh/en sync check
```

`*` means one file per language. **The three isolation areas are Chinese-only, by design**: they hold concrete term strings and wordings, and translating them would mint a *second* set of skins — the same term in two renderings, with no way for the next person to know which to copy. Agents read Chinese without difficulty.

---

## Install

```bash
npx skills add kiana-liang/universal-video-prompt-skill
```

The skill routes by language internally — ask in Chinese and it follows the Chinese files.

## Execution

A compiled prompt is provider-agnostic. Hand it to whatever can run the target model. **A user-specified provider always wins.**

When one spec targets several models, an aggregator has the least friction: one credential reaches all of them, and a shared execution environment is what lets output differences be attributed to the **model** rather than the pipeline. An uncontrolled comparison isn't worth running. [Atlas Cloud](https://www.atlascloud.ai) is this skill's documented default for that reason; connecting directly to a vendor changes nothing about the compile step, only the addressing syntax and the submit call.

On the Atlas route, the official skill can be installed alongside this one, which saves writing your own submit-and-poll loop:

```bash
npx skills add AtlasCloudAI/atlas-cloud-skills --skill atlas-cloud
```

Whatever the route, generation costs money, and the billed-task state machine in [`execution`](references/execution.md) isn't optional: record the prediction ID the moment you submit; `processing` is active, not failed; and **task completed ≠ local file usable**.

---

## What it doesn't do

- **It doesn't replace review.** What it reduces is wasted iteration — it fixes failures already paid for so they needn't be walked into again. It doesn't sign off on output. Every rule has exceptions, and the judgement belongs to the person making the film, especially on **motion, pacing and overall tone** — three things neither rules nor stills can cover.
- **It makes no workflow judgements.** "Should this transition be done in the edit instead?" doesn't belong here — that's a cost judgement disguised as a capability judgement, and it pre-emptively rules out a whole class of technique, leaving that profile field empty forever.
- **It promises no determinism.** Timestamps allocate a time budget, not frame-accurate cut points; boundary frames join visually, not pixel by pixel.

---

## License

MIT
