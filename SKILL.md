---
name: universal-video-prompt-skill
description: >-
  Write one model-agnostic video prompt spec, then compile it to whichever
  video model you can actually call. Use for cross-model prompt work, model
  comparison matrices, reusing one brief across providers, or when the target
  model is not yet available and the work must proceed on another one.
  中文触发：写视频决策清单 / 决策清单（＝英文的 spec，同一个东西）/ 跨模型提示词 /
  一份提示词跑多个模型 / 换模型不用重写 / 多模型对比矩阵 / 模型档案 /
  想用的模型还没开 API 先用别的跑 / 从成片或别人的提示词反推提示词 /
  片型换皮 / 三桶（全局·锁·时序）/ 末态 / 可验证性 / 多段接龙。
---
<!-- sync-source: workflow.zh-CN.md sha256:21f18f4d3275 -->

# Universal Video Prompt Skill

Write the spec once. Compile it per model. **A spec is not a prompt**: it is the
decisions a prompt encodes, kept separate from the dialect that expresses them.

## Language route

- **English request** → follow this file and the `*.md` references.
- **Chinese request** → read [the Chinese workflow](references/workflow.zh-CN.md)
  first, then the matching `*.zh-CN.md` files.
- Model IDs, JSON keys, commands, media placeholders and audio symbols are code.
  Do not translate them.

**Terminology — one concept, two names.** English `spec` and Chinese
**「决策清单」** are the *same thing*. A user writing in Chinese may still type
`spec`; a user writing in English may quote 决策清单. Treat them as
interchangeable and answer in the language the user used. **File names are
cross-language identifiers and stay English** — `spec-format.zh-CN.md` is the
Chinese text about 决策清单, despite the `spec` in its name.

**Three references exist only in Chinese, by design** — the case library, the
film-type library, and the observations file. They hold concrete wordings from
specific films; translating them would mint a *second* set of skins, and the
next person would not know which to copy. Read them in Chinese and relay what
the user needs.

## What this skill does and does not do

It reduces wasted iterations by fixing failures already paid for. **It does not
sign off on output.** Every rule has exceptions, and the judgement belongs to
the person making the film — especially on **motion, pacing and overall tone**,
which neither rules nor stills can cover. Treat it as a set of defaults worth
departing from with a reason, not a checklist that certifies a result.

## 0. Constitution — read this first

Twelve meta-rules govern how this skill is used and they **override any specific
advice elsewhere in it**. Full text (Chinese, authoritative):
[constitution.md](references/constitution.md).

**On examples (1–4)**

1. An example is not DNA — it is **one sample of the skin**
2. Fill order is **write first, look second** — write the slot from this film
   alone, and only then open the examples
3. Examples are **physically isolated**, not held back by self-discipline.
   A rule can be a skin too
4. Adjacent slots must not draw examples from the same film

**On slots (5–7)**

5. **No slot is mandatory.** Empty is a decision, and needs no justification
6. **The slot set is open.** Content that fits nothing gets a new slot
7. **Wrong bucket is the number-one error**

**On boundaries (8–12)**

8. A model profile **never deletes a slot from the master**
9. Do not write *your belief about model capability* into a rule — a profile
   records "I wrote X, I observed Y", never "X does not work"
10. **Write the spec in full first, then let hard constraints trigger a
    degrade.** "I suspect this model handles it poorly" is not a hard constraint
11. Do not promote a default that grew out of one scenario into a global rule
12. **Rules do not replace review**

Recorded per-model observations live in
[observations.zh-CN.md](references/observations.zh-CN.md) and are **not read
while writing** — only for post-hoc diagnosis and hard-constraint degrades.
Under-writing because of a belief about capability leaves **no trace in the
output**: you see the effect fall short and cannot find the cause, because the
line was never written.

## 1. Two axes govern every line you write

### Scope — what does this line govern?

| Bucket | Governs | Contents |
|---|---|---|
| 1 · Global | The whole video | Film type (named-term synthesis + counterweight prohibitions), scene, style, one-sentence director's premise, camera principle, 〔as needed〕persistent overlay, 〔as needed〕technique vocabulary |
| 2 · Locks | Anything that must not drift | Identity, 〔if refs〕reference roles, audio source, 〔if any〕supporting cast, continuity, 〔if content risk〕negatives |
| 3 · Time | One beat or stage | Stage events and their end states |
| **+** | Whatever this film needs that the rows above cannot hold | **Slots you add**, placed in the bucket owning their scope |

A line in the wrong bucket is the most common cause of drift — global rules
buried inside beat 1 stop applying at beat 4.

**This table is a list of available tools, not a to-do list.** Three companion
rules, detailed in [spec-format](references/spec-format.md):

- **No mandatory slots.** Ask "does this film need it?" — if not, leave it empty
  and give no reason
- **The two 〔as needed〕 slots need judgement.** They were generalised from one
  family of high-information-density film types; on a film that works through
  negative space, filling them **actively hurts it**
- **Add a slot rather than force-fit.** Forcing content into a slot with a
  different scope is a variant of the wrong-bucket error

**Restate the two or three most expensive locks at the physical end of the
prompt** (recency helps). This is a writing convention, not a fourth bucket —
the content still belongs to buckets 1 and 2 and appeared there first.

### Verifiability — can this line be checked after generation?

| Do not write | Write instead |
|---|---|
| `keep it consistent` | the **visible** end state of each stage |
| `tense`, `warm`, `oppressive` | 2–4 observable cues: gaze, brow, mouth, breathing, hands |
| `rack focus` | `rack focus: focus moves from the foreground leaves to the person behind them; leaves go soft, the face resolves` |
| `use these references` | what each reference **controls, and what must not be taken from it** |
| `make it fast-paced` | a time budget per stage |

A line that cannot be checked cannot be debugged. Full patterns in
[verifiability](references/verifiability.md).

## 2. Write the spec

Fill the three buckets. Skip what does not apply; do not pad. **An empty slot
needs no justification.**

When the input is not a subject but **a finished film, a reference image, or
someone else's prompt, work backwards** — see
[slot-filling](references/slot-filling.md). Reverse-engineering must not
invent a premise: the premise is already in the artefact.

```text
[1 GLOBAL]  film type (term synthesis + counterweights) · scene · style ·
            director's premise (one sentence) · camera principle ·
            〔as needed〕persistent overlay · 〔as needed〕technique vocabulary
[2 LOCKS]   identity · 〔if refs〕reference roles (controls X, do not take Y) ·
            audio source · 〔if any〕supporting cast · continuity ·
            〔if content risk〕negatives
[3 TIME]    granularity (see §3) · stages · end state per stage
[+ ADDED]   whatever this film needs that the rows above cannot hold
```

**Reusing a proven film type?** Work through that type's skin list and refill
every item from scratch — `film-type term synthesis`, `overlay elements` and
`technique vocabulary` are the three most often carried over wholesale. After
ticking every box, **check direction once more**: do these terms point the same
way as this film? See [film-type-dna](references/film-type-dna.md).

**Do not re-derive the premise** — load the DNA, re-skin, and adapt the DNA's
own logic to the new skin.

### Two rules about the premise slot

- **It is not mandatory.** It is the one slot that *cannot be derived from the
  others* — that makes it irreplaceable, not required. One recorded film ran
  successfully with this slot empty.
- **Write the "why", not the "what to do every time".** An execution rule
  ("after every beat, do X") placed in the premise slot **acquires the
  premise's authority and becomes unbreakable**, then contradicts its own
  execution. Rules belong in the technique vocabulary or the time bucket.

## 3. Choose time granularity before writing bucket 3

Granularity is a **prior decision**. Writing beats at second precision and then
downgrading means rewriting them.

| Granularity | Write | Use when |
|---|---|---|
| **None** | Event order only | One continuous action, mood pieces, single shots. Timestamps here fragment the shot: the model invents pauses to hit the marks |
| **Stages + end states** | Stage 1/2/3, one primary change each | Most narrative work. **Default** |
| **Second-level** | `[start–end s]` | Only under an external hard constraint: music, lip sync, reference handoff, a brand reveal that must land at a fixed time |

Second-level costs **model freedom**, not author effort. Too much content in one
range causes over-cutting or dropped events. **Take the loosest granularity that
still meets the constraint.**

### Do not decide this silently

| Signal | Action |
|---|---|
| Music or voiceover track supplied | Second-level. Do not ask |
| User says mood piece, one-take, single shot | None. Do not ask |
| Explicit hard beat (brand reveal at 0:07, lip sync, reference handoff) | Second-level. Do not ask |
| **Multi-event narrative, no external constraint** | **Ask** |

When you ask, **recommend with a reason** — never present a bare menu. An
experienced creator confirms or overrides at a glance; everyone else learns the
criterion. Do not ask again for a re-skin: granularity is a DNA field.

Timestamps allocate a **time budget**, not frame-accurate cut points. Content
that must be exact — signage, formulas, product specs — is a **capability**
question: probe the target model, record it, then **degrade the writing**
(shorter strings, wider tracking, larger type, graphic symbols instead of text)
rather than moving the requirement out of the video.

## 4. Compile the spec to a target model

| Layer | Contents | Handling |
|---|---|---|
| **Language** | Buckets, end states, observable cues, term-plus-description | Portable as written |
| **Bias** | Anti-default suffixes, negatives, transition vocabulary, reference-addressing dialect | One profile per model. **Measured, never assumed** |
| **Capability** | Reference count, multi-shot in one generation, hard cuts, duration, timing adherence | Probe, then degrade |

The most common cross-model error is **treating a bias-layer line as a
language-layer line** — copying an anti-default suffix that worked on one model
to another and assuming it still helps.

Load the target's [model profile](references/model-profile-schema.md). No
profile means no assumptions: run the smallest probe that settles the question,
record it, and degrade the spec to what the model actually supports. **Report a
degrade; never let it pass silently.**

### ⚠️ Published enums are assumptions, not limits

Documented ranges are often **narrower than what the API accepts**, and a single
page can contradict itself (one page was observed stating three different
duration ranges in three places). **Submit the value you actually want and let
the API answer.**

The error is asymmetric: trusting a too-narrow doc → the spec is silently
degraded → the run succeeds → nothing in the output reveals that a better
configuration was available.

> ⚠️ **"Rejected means no task and no charge" holds only on a direct vendor
> route.** On an **aggregator** it may not: the gateway does not validate at
> submit time, returns success, creates the prediction, and the upstream
> rejects it afterwards (`status=failed`, `executionTime=0`). **"Task created"
> does not mean the parameter was accepted.** When probing limits through an
> aggregator, expect a created-then-failed task rather than a submit-time error —
> and probe that parameter with the shortest duration and lowest resolution
> rather than with a full job.

### Term plus observable description beats a dialect table

```text
<term> + <target subject> + <visible change> + <foreground/background> + <direction or speed>
```

A model that knows the term takes the shortcut; one that does not follows the
description. One prompt serves both. Reserve real dialect translation for
interface-level differences — **reference addressing** (`@image1` versus
`Reference Image 1`) is the main one.

### Degrade rules

| Missing capability | Degrade to |
|---|---|
| Multi-reference addressing | One image locks identity; carry the rest in text |
| Multi-shot in one generation | One shot per request, chained on boundary frames |
| Reference count below spec | Merge roles by priority: identity > key prop > scene > style |
| Duration below spec | Split into stages that each stand alone, then chain on boundary frames |
| Weak timing adherence | Drop to stages plus end states |
| No native audio | Rewrite audio lines as things the picture can carry (visible sound-source action, mouth shapes, vibration) — do not move them out of the film |
| Single-image I2V only | First frame as the only visual lock; everything else in text |

## 4.5 Chaining multiple segments

For a segment that follows another generated segment, **look at the previous
segment's actual end state first**, then make a **continue / clear** choice for
every subject in it — writing neither means it will be kept, and possibly
amplified.

⚠️ **Chaining is not extension; their seam defaults point in opposite
directions** — an extension hides the seam, whereas in chaining the seam *is*
the hard cut. Details in
[spec-format](references/spec-format.md#chaining-multiple-segments-only-when-a-previous-segment-exists).

## 5. Transitions

The skeleton is one line: **name the transition type at the cut point.**

**Do not attach global default prohibitions to transitions.** Any "never use
transition class X" rule belongs to a specific scenario, not to the skeleton —
it may be right there and wrong elsewhere, where that same transition is the
technique itself. Judge it by constitution rule 11: a rule's scope is the
scenario it was validated in.

**Every transition this film needs goes into the prompt**, typed at its cut
point — flash frames, whip cuts, wipes included. Whether a given model executes
one well is a **profile** question to be measured, never something the spec
gives up on in advance.

⚠️ **Do not drop a transition because another tool could do it more cheaply.**
That is a workflow judgement, and this skill makes none — it describes what the
film *is*, and everything in it is produced by the model. Pre-emptively ruling
out a class of technique guarantees that the profile field for that class stays
empty forever.

**Physical transitions** (occlusion, match-object, action relay, push/pull
through, material spread) deserve explicit naming — they depend on in-frame
material relationships the model needs stated to act on.

## 6. Review

Check in order and **stop at the first failure** — later checks are wasted on a
wrong identity.

1. **Identity** — right subject, right count, no duplicates or swaps
2. **Locks** — every bucket-2 lock held
3. **End states** — each stage landed on its stated visible state
4. **Motion and seams** — no drift, no teleporting props
5. **Audio** — source, language, sync as written

Regenerate only what failed. A lock that breaks repeatedly on one model is a
**profile finding** — record it in the bias layer instead of rewriting the spec.

**⚠️ Stills have a blind spot.** Extracted frames settle texture, composition,
identity and end states. They say **nothing** about motion quality, transition
smoothness, pacing or audio sync — a piece can win on every still and lose on
all four. Never issue an overall verdict from stills alone: either watch it, or
state which half your conclusion covers.

Not a minor caveat. In one comparison stills favoured model A on every
measurable axis while the reviewer watching playback preferred model B
decisively — the entire disagreement lived in motion and rhythm.

## 7. Execution

A compiled prompt is provider-agnostic. Hand it to whatever can run the target
model.

An aggregator has the least friction when one spec targets several models: one
credential reaches all of them, and a shared execution environment is what lets
output differences be attributed to the **model** rather than the pipeline. An
uncontrolled comparison is not worth running. Atlas Cloud is this skill's
documented default for that reason; **a user-specified provider always wins**.

Whatever the route, generation costs money and these rules hold:

1. Record the prediction ID and the stage **the moment you submit**
2. `starting` / `queued` / `pending` / `processing` are all active — poll the
   same ID, **never submit a second task for the same stage**
3. Inspect the artefact before starting anything that depends on it.
   **Task completed ≠ local file usable** — a download can truncate
4. `failed` / `timeout` / `canceled` are terminal. A retry is an explicit
   decision: report the old ID and the added cost first
5. Zero or missing processing time, a slow artefact, a local polling timeout, a
   stopped process, a status-query error — **none of these is failure**. Keep
   the ID and resume polling
6. `continue` means resume the existing task. It is never permission to retry

A status lookup is read-only and **must never be replaced by a generation
call**. See [execution](references/execution.md).

## References

| File | Read it for |
|---|---|
| [constitution.md](references/constitution.md) | **Before starting.** Twelve meta-rules that override all specific advice |
| [VALIDATION.zh-CN.md](VALIDATION.zh-CN.md) | How hard a given rule is. Each marked ✅ controlled / ⚠️ reasoned default / ❌ unvalidated |
| [spec-format.md](references/spec-format.md) | The full template, slot criteria, the three questions every prohibition must pass |
| [slot-filling.md](references/slot-filling.md) | Filling empty slots; working backwards from a film, a reference image or someone's prompt |
| [verifiability.md](references/verifiability.md) | End states, observable cues, picture language versus spec language |
| [portability.md](references/portability.md) | The three layers, probes, degrade decisions |
| [film-type-dna.md](references/film-type-dna.md) | Extracting DNA, re-skinning, checking direction after the ticks |
| [film-types.zh-CN.md](references/film-types.zh-CN.md) | ⛔ Five **skins already run**. Confirm same class before opening |
| [model-profile-schema.md](references/model-profile-schema.md) | Profile fields and how to measure them |
| [observations.zh-CN.md](references/observations.zh-CN.md) | ⛔ **Not read while writing.** Per-model observations, for post-hoc diagnosis and hard-constraint degrades only |
| [case-library.zh-CN.md](references/case-library.zh-CN.md) | ⛔ **Write your own slots first.** Every copyable concrete element lives here |
| [execution.md](references/execution.md) | Provider routes, credentials, polling, resume |
| [checklist.md](references/checklist.md) | Pre-submission review |
