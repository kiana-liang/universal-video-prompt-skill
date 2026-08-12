<!-- sync-source: verifiability.zh-CN.md sha256:0c41709a8210 -->

# Verifiability

One rule underneath everything: **an instruction you cannot check on the output
is one you cannot debug either.** Rewrite intent as observable result.

> **This file describes the shape of failures; it gives no copyable elements.**
> All concrete case elements (texture words, prohibition wordings, shot
> breakdowns) live in the isolation area
> [case-library.zh-CN.md](case-library.zh-CN.md). Per
> [constitution](constitution.md) rule 2: **write your own from the criteria
> here first, and only then open the case library.**

This does not mean writing more. An observable phrasing is usually **shorter
than the pile of adjectives it replaces**, because it commits to one reading
instead of hedging between several.

## End states

The highest-leverage item in the method. Do not ask for "keep it consistent" —
write what is **visible** when this stage stops.

Shape: not "continues doing X", but **what is on screen and where, at the moment
this stage stops**. (Example → case library D1)

An end state must be **visible**. "She feels relieved" is not an end state; "her
shoulders drop, the furrow between her brows releases" is.

### The same thing in three forms

End states are not only a text device — every input modality has its equivalent,
and they combine:

| Form | Carrier | Use when |
|---|---|---|
| Stage end state | Text | Default. Multi-event films |
| Keyframe sequence | Images — each image **is** one stage's end state | You can draw or generate those stages |
| Boundary frame | Video — the seam between source and extension | Extending or continuing existing footage |

A keyframe sequence needs **explicit order**, one role per image:

```text
Use @image1 through @image4 as keyframes, in order.
@image1 is the first frame: <opening composition and subject state>.
@image2 is the second keyframe: <stage 1's visible end state>.
@image3 is the third keyframe: <stage 2's visible end state>.
@image4 is the final frame: <closing composition and subject state>.
The video passes through these states in order, with continuous motion between them.
```

Separate images align better than several stages tiled into one grid. Keyframes
control **stage order and key states**, not frame-by-frame replication.

### Write an extension's boundary on the correct side

**Extending forwards** (after the source): first write the continuation of the
source's **final frame**, then what happens next.

**Extending backwards** (before the source): write the new content first, then
write the source's **first frame as the explicit end state of the segment you
are generating**. Writing only "then it connects to the source video" is a known
failure — it makes characters and effects from later in the source appear early,
or the picture keeps changing after it reaches the target state.

Also state what **must not appear early**: `material belonging to after the
source begins must not appear early in the backward-extension segment`.

## Anchor emotion to observable cues

An emotion word gives direction only; the performance stays wide open. Pin it
down: instead of naming the emotion, write **two to four visible changes in the
body**. (Example → case library D2)

**Two to four cues are enough for one emotional turn.** Listing every facial
detail does not add control; the cues start fighting each other. Available:
gaze direction and movement, brow tension, mouth, breathing, throat, hands,
posture.

For multiple turns, trigger on **events** rather than timestamps:

```text
When <the first event> happens, <the first observable reaction>.
When <the second event> happens, <a change in gaze, breathing or expression>.
After confirming <the key information>, <the subject>'s suppressed feeling
surfaces through <observable behaviour>.
```

Event triggers survive a change of model better than time triggers, because they
do not depend on timing adherence.

## Intensity and pacing also have to become observable

"Fast / slow / quiet / tense / charged / dynamic" are **intensity adjectives**,
with the same defect as emotion words: direction given, execution wide open.

⚠️ **"Slow" has one failure of its own: the model reads it as "nothing happens in
this stage".**

Observed: a stage written as "the slowest, quietest stage of the film" came back
as the subject holding one pose and drifting slowly, with **none of the events
specified for that stage occurring**. And in rhythm design **the trough is
exactly where events matter most** — it works through "small amplitude but clear
causality", not through "no action".

The fix: **do not write the intensity word. Write what happens in that stage,
and connect the tension through causality.**

```text
weak:    this is the slowest, quietest stage of the film
strong:  <subject> reaches very slowly toward <target>; the instant they touch it,
         <external event> happens and <subject> snatches back
```

Same spec, only this one place changed, everything else word-for-word identical:
that stage then played out in full, and reproduced in the two versions after it.

**Test**: before writing an intensity word, ask — **which event carries this
stage's intensity?** If you cannot answer, that stage will probably idle.

## Pick the property that carries the concept

Making a line checkable is necessary but not sufficient. **A lock can be fully
satisfied and completely ineffective.**

**Shape of the failure**: you locked property A, the model satisfied A
completely, and the thing you actually wanted is gone — because the property
carrying the concept was B, and A was merely a common side effect of B.

One observation walked the whole shape: locking "stay flat, do not render
realistically" was obeyed strictly by two different models, both returning
smooth even vector outlines. Flat? Yes. Hand-drawn? Not at all. **The lock aimed
at "flatness", while the property carrying the concept was "visible tool
marks".** Renaming the medium by its **tool** and demanding visible working
marks reversed the same model's behaviour outright. (Wordings → case library A1)

A general corollary: **property A is "the category of the result"; property B is
"the process that produces it".** Describing the process usually locks down what
you want better than describing the category.

Before trusting a lock, ask: **could the model satisfy this sentence and still
lose the thing I want?** If yes, the lock is aimed at a side effect rather than
a cause.

This failure has a distinct signature: **the output matches the spec line by
line, and anyone who knows the reference sees immediately that it is wrong.**
When that happens, do not add more locks — go find the property that actually
carries the concept and name it specifically.

## Name the mechanism, not just the effect

A subjective effect usually has more than one physical route. Write only the
effect and the model picks one — often not the one you meant.

**Shape of the failure**: rewriting a line to make the effect "sound stronger"
makes the result worse, because the rewrite deleted the only **mechanism cue**
in the original, forcing the model onto another route to the same effect — and
that route is mutually exclusive with a lock elsewhere.

One observation walked the whole shape: a description moved from a **scale**
mechanism (filling a known structure) to a **volume** mechanism (three-
dimensional, advancing on the camera). Subjectively fiercer; the output
collapsed from a flat graphic into a realistic solid object — because volume
requires solidity, and the whole film depended on a flatness lock.
(Wordings → case library A2)

One effect, two mechanisms:

| Effect wanted | Mechanism A | Mechanism B |
|---|---|---|
| Oppression | **Scale**: fills the frame / spans a known structure | **Volume**: solid, advancing on you |
| Grandeur | Subject small against a known reference | Wide lens, high angle |
| Intimacy | Tight framing | Shallow depth of field, soft light |
| Speed | Motion blur, objects sweeping past | Camera shake, cut density |

Before writing an effect word, ask: **how many ways are there to achieve this?**
More than one, and one of them conflicts with a lock elsewhere → you must state
which.

**⚠️ The reference structure a mechanism depends on must actually exist in the
scene.** A scale anchor like "fills / spans a known structure" only works when
that structure is written into the scene description; give the model a different
structure and it silently switches to the second-best route. **Either write the
anchor into the global scene, or do not rely on it.** (Example → case library A2)

The signature here is unusual: **one lock quietly cancels another.** The film
satisfies the effect and violates a constraint elsewhere, and the two lines have
no literal relationship — in the scale-versus-volume case, rewriting one sentence
in the final stage broke a texture rule written three stages earlier.

## Write in pictures, add specifications as insurance

The three sections above share one underlying cause, worth stating directly
because it governs how every line is phrased.

**A model's training data is described pictures, not stipulated requirements.**
A sentence that reads like shot description lands; a sentence that reads like a
specification has to be translated into a picture first, and the translation is
where it goes wrong.

The difference in shape:

| Written as picture — lands | Written as specification — needs translating |
|---|---|
| Name the **tool and its visible marks** | Declare **the texture category to achieve** |
| Describe **what is on screen, how big, where** | Declare **what it must not be** |
| Describe **what changes in the body** | Declare **the emotion to convey** |

The same information, in the left column, is packaged inside **a described
picture** the model reads directly. (Line-by-line examples → case library A3)

### But specifications are not forbidden — they are insurance

Do not read the above as "never write definitions". The strongest observed
version **used both**: build the shot in pictures first, then append one
explicit definition pinning the property that must not slip.
(Original wording → case library A3)

Three phrasings, measured:

| Phrasing | Result |
|---|---|
| Specification only, no picture anchor | A realistic solid skull — failure |
| Specification-led, picture anchor missing | Correct, but wordy |
| **Picture first, specification appended** | **The best texture of any version** |

So it is a **priority order, not an exclusion**: **describe pictures by default;
when an effect must be preserved and description alone could be misread, append
one explicit definition.**

### Whether a line earns its place: one test only

**Does this sentence add a new constraint, or restate a consequence of an
existing one?** Only the latter is noise.

Shape: **keep** "what happens in the scene"; **delete** "and therefore it
appears to be…" — the second follows necessarily from the first. Deleting one
such consequence was observed to change nothing in the output.
(Example → case library A4)

**This is why "shorter is better" is the wrong summary.** Three places in the
same film hold up **precisely because they were written long**: the medium named
by its tool, the per-stage restatement that rescued one model's texture, and an
explicit statement of a scene fact that was easy to misread. **Noise is not
length. Noise is restatement.**

### What to leave to the model

| You decide | Leave to the model |
|---|---|
| Medium, palette, scale anchors, subject posture, what happens in each stage | The shape of the host structure, where secondary elements land, how to compose within the stated intent |

Specifying implementation detail suppresses the priors that make the model good.
Observed: giving a secondary structure a specific geometric shape performed
**worse** than not writing it — the model's own choice echoed the scene's
architectural logic better. (Example → case library A5)

Same mechanism as "a text staging beats feeding a storyboard grid": **hand over
"what you want", not "how to do it".**

## Craft terms: keep the term, append the description

Any term whose recognition is uncertain — obscure words, words used
inconsistently across the industry, words named after a film, a director or a
platform trend — gets written twice:

```text
<term> + <target subject> + <visible change> + <foreground/background> + <direction or speed>
```

(Two filled examples → case library D3)

A model that knows the term takes the shortcut; one that does not follows the
description. One prompt serves both — which is also why this beats maintaining a
per-model dialect table.

**Usually fine unqualified**: shot sizes, basic camera moves (push, pull, pan,
follow, orbit, handheld), basic angles (low, high, first-person).

**Usually needs a description**: dolly zoom, bullet time, speed ramp, bounce
ramp, rack focus, whip-pan transitions, match cut.

Aperture, focal length and shutter values can be written, but **stating the
visible result you want is usually more controllable than giving numbers alone**.

## References: always write both halves

A reference-role statement without "what must not be taken" is incomplete.
Shape: **`<asset> controls <the few things it alone is responsible for>. Do not
take its <the few things most likely to leak in>.`**
(One example per modality → case library D4)

When a reference video already defines the motion accurately, **write only which
properties to inherit**. Describing the same motion again in text fights with the
reference.

## Anti-patterns

| Do not write | Why it fails | Write instead |
|---|---|---|
| `keep it consistent` | Nothing to check | A visible end state |
| `cinematic`, `high quality`, `masterpiece` | No visual commitment | Specific light, palette, texture |
| `she looks sad` | The performance is unconstrained | 2–4 observable cues |
| `@image1 through @image4 define four characters` | States no mapping | One binding line per subject |
| `make it epic` | Unfalsifiable | Scale cues: what is in frame, how small the subject is beside it |
| `perfect lip sync` | Not an instruction | Supply audio, name the speaker |
| `no bad hands, no artefacts, no blur…` | A copied blacklist unrelated to this film | The two or three risks this film actually has |
| `three actions within one second` | An impossible pacing demand | One stage per action |

## Limits worth stating honestly

Verifiable phrasing raises the hit rate; it does not make generation
deterministic.

- Timestamps allocate a **time budget**, **not** frame-accurate cut points —
  an action may land slightly either side of a boundary
- Boundary frames join visually; they are not a pixel-exact edit splice
- Multi-reference work means **selecting and combining the right asset for each
  moment**, not making every asset appear at once
- Content that must be exact — signage, formulas, product specs — is a
  **capability** question: probe the model, record it, then **degrade the
  writing** (shorter strings, wider tracking, larger type, graphic symbols) —
  do not move the requirement out of the film

## Related

- [case-library.zh-CN.md](case-library.zh-CN.md) — concrete instances of every
  principle here (**write your own first**)
- [spec-format.md](spec-format.md) — which bucket each line belongs to
- [portability.md](portability.md) — which phrasings survive a change of model
- [checklist.md](checklist.md) — pre-submission review
