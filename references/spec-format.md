<!-- sync-source: spec-format.zh-CN.md sha256:bfb39523c59b -->

# Spec format

A spec records the decisions behind a prompt, stored separately from the dialect
that expresses them. Write the spec, then compile it. Changing models should not
require rewriting it.

> **This file gives slots, criteria and structural skeletons — no copyable
> elements.** Every concrete case element lives in the isolation area
> [case-library.zh-CN.md](case-library.zh-CN.md). Per
> [constitution](constitution.md) rule 2: **write your own slots from the
> criteria here first, and only then open the case library.**

## Template

> **Read [constitution](constitution.md) groups 1 and 2 first.** The table below
> is **a list of available tools, not a to-do list**: no slot is mandatory, and
> no empty slot counts as a defect. The marks after each slot say **under what
> conditions that slot is usually worth filling** — they are not a priority
> ranking.

```text
[1 GLOBAL]
  film type:        which class of film this is — multi-axis term synthesis
                    + a reference-object anchor + counterweights for each term
  scene:            where, when
  style:            visual treatment, palette, how light behaves
                    (only what is visible; the terminology layer belongs to film type)
  premise:          one sentence — the thought this film exists for
  camera principle: the rule governing the whole film, not a shot list
  persistent overlay: 〔as needed〕the layer pressed onto every frame,
                    and how that layer itself moves
  technique vocab:  〔as needed〕named effects and transitions the film may draw on;
                    not per-beat assignment

[2 LOCKS]
  identity:         who or what must not change, and by which invariants
  reference roles:  〔if refs〕per asset — what it controls, and what must not be taken from it
  audio source:     native, external track, or silent
  supporting cast:  〔if any〕position, and what they must not do
  continuity:       what must hold for the whole film
  negatives:        〔if content risk〕specific risks only

[3 TIME]
  granularity:      none | stages | second-level   (decide before writing the rest)
  stage 1..n:       one primary change each
  end state:        what is visible when this stage stops

[+ ADDED SLOTS]     what this film needs that the rows above cannot hold (see below)
```

Leave unused fields out. **Empty beats padding** — every extra line competes for
attention with the others. **Empty needs no justification**: this film does not
need it, and that is the whole reason.

### Why the two 〔as needed〕 slots are marked out

`persistent overlay` and `technique vocab` were generalised from one family of
high-density graphic film types. For that family they carry a great deal;
**for other types they may carry nothing, and can do harm**.

⚠️ A recorded lesson: while filling slots for a film that speaks through **a wide
colour field and extreme negative space**, both slots were filled by copying a
film built on **dense information layering** — prescribing "full" for a film that
works by being "empty". Every slot filled, every end state met, the whole
direction inverted.

So before filling these two, ask: **does this film's impression come from more
information on screen, or from less?** If less, leave them empty.

## The slot set is open

This table is **the result of one round of generalisation, not an exhaustive
set**. When content fits no existing slot, **add one**, placed in the bucket it
belongs to.

⚠️ **The most common error is not "there is no slot for this" — it is forcing it
into the nearest one.** Force-fitting is a variant of the wrong-bucket error:
once content sits in a slot with a different scope, its scope is wrong too.

Three questions before adding:

1. **What range does it govern?** Whole film → bucket 1; must not drift →
   bucket 2; one beat → bucket 3
2. **Which existing slot has the same scope?** One does → use it. None →
   create one
3. **Can it be checked?** No → rewrite it as an observable result per
   [verifiability](verifiability.md) first

Against bloat: if you cannot say what the new slot governs *and* how it differs
from every existing slot, do not create it.

Reasonable added slots seen in practice (examples, not a list): `material`,
`subtitles and in-frame text`, `music structure`, `colour script`, `how light
behaves`, `delivery specification`. Each is an independent scope in some films
and does not exist at all in others.

## Field notes

### Film type (bucket 1)

**Not a label — a synthesis across axes.** A weak film type reads like a
category name (`a minimal flat vector title sequence`); an effective one gives
this film's coordinates within the industry.

> **The shape of the synthesis is taken from prompts that actually ran; it is
> descriptive. The causal claim "synthesis beats label" has not been isolated** —
> in the comparison observed, the style words changed at the same time as six or
> seven other things. Treat it as a reasoned default.

```text
film type:  <this film's category name within the industry>
            <medium/technique term> + <compositional-grammar term> + <element-vocabulary term>
            reference: <a real product category to anchor against>
            counterweights: <targeted prohibitions against each term's default bias>
```

Three rules of thumb:

**One term per axis; do not stack synonyms.** "Medium/technique", "compositional
grammar" and "element vocabulary" are three different axes. Three words all
saying "what it looks like" say one thing, and compete for attention.

**Terms need real corpus behind them; do not invent phrases.** Test: can this
term be searched in the industry, with a large body of work tagged that way?
Yes → a term. No → a description, which belongs in the `style` slot.

**Add a reference-object anchor.** Point at a real, existing product category
(posters, magazine spreads, tournament key art) — stronger than any adjective.
Do not point at a specific work or an author's name.

#### Counterweight prohibitions

**Every named term is a loan with interest.** You borrow its visual priors, and
you take on its default bias with them. Counterweights are the few prohibitions
that **cancel that bias in a targeted way while keeping the term**.

The shape is this (**illustrative, not a default** — per
[constitution](constitution.md) rule 1, do not carry these elements into your
spec):

```text
<the named term you chose>   ← borrows: <visual priors it brings>
                                bias: <where it pulls by default>
counterweights: <a few prohibitions cancelling that bias, as a group>
```

**A counterweight does not negate the term**: the term stays (its priors are
what you want); only the side effects it drags along are cancelled.

Filling it is three steps: **① what does this term look like by default in the
industry → ② which parts of that default do I not want → ③ write each as a
prohibition.** Step ① has to be honest — if you cannot picture the term's
default, you are not ready to use it.

(Worked fills for two subjects → case library B1, D5)

**Write the borrowing and the repayment together, in this slot; do not dump them
in the `negatives` slot.** Reason: a counterweight is only valid against **the
term it counterweights**. Once separated from its term and stored centrally, it
gets carried over wholesale on the next re-skin and degenerates into a generic
blacklist — the main reason prompts get longer without getting better.

> **This is a reasoned default, not a validated rule.** In the two ground-truth
> prompts observed, one put counterweights next to the term at the top and the
> other put similar content in a trailing negatives section — **the author was
> not self-consistent**. "Adjacent" was chosen on the portability argument
> above, not on a controlled comparison.

Deleting the term to dodge the bias is the weaker move: the bias goes, and so do
the priors you wanted. **Counterweight beats deletion.**

The **number and wording** of counterweights are model-dependent and belong to
the [model profile](model-profile-schema.md); *which term needs
counterweighting* is model-independent.

### Director's premise (bucket 1)

One sentence. Needing two means this is two films. The premise is "the one line
you would keep if you could keep only one", and the tie-breaker when locks
conflict.

A weak premise reads like a genre label (`a cinematic product film`). An
effective one names **the specific thought**, and usually takes the shape
"**because X, the picture must Y**" — binding a physical fact to a visual
decision, so every lock afterwards can be derived from it.
(Example → case library A6)

**But this slot is not mandatory** ([constitution](constitution.md) rule 5). It
is the one slot that *cannot be derived from the others* — that makes it
irreplaceable, not required. The film in case library C ran successfully with
this slot empty.

⚠️ **What goes in this slot is the "why", not the "what to do every time".** An
execution rule ("after every beat, do X") placed here **acquires the premise's
authority and becomes unbreakable**, then contradicts its own execution. Rules
belong in the technique vocabulary or the time bucket. (Recorded misstep → case
library C)

### Persistent overlay (bucket 1, 〔as needed〕)

**Decide whether you need this slot first.** Per the section above: does this
film's impression come from more information on screen, or less? From less →
leave it empty and stop reading here.

If you are filling it, write two halves: **what this layer is made of**, and
**how it moves by itself**. Composition alone gets you a sticker; **movement is
what makes it an overlay**.

⚠️ The second half is the one most often written badly. Sentences like "drifts
slightly with the camera, sweeping continuously" are **unverifiable**, and
generate as a static sticker. Every item needs a countable quantity of motion:
how often it jumps, how many times per second, how fast it scrolls.

```text
persistent overlay: <what this layer is composed of>
                    <how each part moves, with countable quantities>
```

**Before choosing elements, answer one question: what function does this layer
serve in this film?** The elements grow out of that function, not out of "what
films like this usually put on screen". If you cannot state the function, do not
choose elements yet — that means the slot is not thought through, and what you
reach for will be the set you have seen.

(Two fills of the same DNA with different functions → case library B2 and B4.
**Those two element sets have zero overlap** — direct evidence that elements are
skin.)

**Once you decide to fill it, this slot must live in bucket 1.** Written into
one stage, it disappears at the next — what the audience sees is that layer
suddenly vanishing.

**One more judgement: an overlay is not only "needed or not" but "would it harm
this film".** On a film that works through negative space and a wide colour
field, a layer of persistent information cuts away its breathing room.

### Technique vocabulary (bucket 1, 〔as needed〕)

The list of named effects and transitions the whole film **may draw on**. It is
distinct from bucket 3's "which one is used at this cut": the vocabulary is a
library, per-beat assignment is drawing from it.

**Decide whether you need it first.** This slot is only worth having when "a
fixed set of techniques recurring" is itself the style. On a film built around a
single long take or natural continuity, this slot is noise.

#### ⭐ Once you decide to fill it, ask about the source domain first

**Every slot has its own source domain, and different slots may draw on
different ones.**

| Slot | Its source domain is |
|---|---|
| Film-type terms | which system this film's **picture** belongs to |
| **Technique vocabulary** | which system this film's **motion** belongs to |

These two answers are **often not the same system**. If you do not ask them
separately, you will reach for motion vocabulary inside the system that defined
the picture — **a recorded three-version detour**: one film's picture system was
right, but three consecutive versions searched for motion tools inside **that
same system**, and nothing lifted it; switching to another system's vocabulary
worked on the first try. (Named techniques from two systems → case library B3, E4)

So the order is: **first say which system this film's motion belongs to, then
draw named techniques from that system.** If you cannot name the system, do not
fill this slot yet — you have not worked out what makes it move.

```text
technique vocab: <the few named techniques this film may reuse>
                 <which classes of transition are allowed>
                 excluded: <techniques this film explicitly does not want>
```

(Worked fills for two subjects → case library B3, D6)

Three rules of thumb:

- **Use named terms, not descriptions of phenomena.** A technique with a name in
  the industry invokes model priors better than describing what it looks like.
  When recognition is uncertain, use the term-plus-observable-description pattern
  from [portability](portability.md) (examples → case library B3, D6)
- **The exclusion list says "this film does not want that", not "another tool
  does it more cheaply".** The latter is a workflow judgement, and this skill
  makes none; ruling out a class of technique in advance guarantees you never
  measure the model's ability at it
- **Camera principle governs how the camera moves; technique vocabulary governs
  how the picture changes.** Do not mix them

### Reference asset roles (bucket 2)

Always two halves. What it controls, and what must not leak in from it:

```text
<asset> controls <the few things this asset alone is responsible for>.
Do not take its <the few things most likely to leak in>.
```

(One example per modality → case library D4)

**Name and bind every subject individually.** Never write "@image1 through
@image4 define four characters" — that states no mapping at all.

When several images show the same object from different angles, say so, and
state the output count: `the four images define the same lamp. Only one lamp
appears in the whole film.`

### Negatives (bucket 2)

Write specific risks, not a standing blacklist. A negative earns its place when
it names something **this film could actually produce and that is expensive to
redo**. Copying someone else's negative list is the main reason prompts get
longer without getting better.

#### Route it first, then decide whether to write it

For each candidate negative, ask what it counterweights and send it to the slot
that owns it:

| What it counterweights | Send it to |
|---|---|
| **The bias of a named term you chose** | The film-type slot's [counterweights](#counterweight-prohibitions) |
| **Palette / identity / something that must hold film-wide** | The matching bucket-2 slot: continuity, identity, … |
| **Something this film's own content could produce, expensive to redo** | **It stays here. This is a negative** |

**What a real negative looks like**: it counterweights **a specific piece of this
film's content**, points at no term, and survives a change of style words — the
risk is still there. (Example → case library C)

**This slot need not be filled.** Write it if that kind of content risk exists,
leave it empty otherwise — empty is the correct outcome of routing, not an
omission. Conversely, if you find many entries piling up here, run the routing
table first: most are probably counterweights wearing a negative's coat.

One observation: tracing every line of a well-performing prompt's "strict
limits" block back to its source sent **all ten of them elsewhere**, leaving the
negatives slot empty. **That is that film's result, not a general law** — another
subject will have real negatives. (Line-by-line trace → case library B5)

**Name it; do not judge by impression.** A negative's source is often not the
first thing you think of: one that looks like it counterweights a scene setting
may actually counterweight **the film-type term itself** — and it stays valid
even if that scene never appears in the film, as long as the term is still in
the film-type slot.

A surviving negative must pass one check: **name the term or setting it
counterweights, then confirm that thing exists in this spec.** Only if nothing
corresponds after naming it is it dead weight to delete.

Negatives are model-dependent too — see [portability](portability.md).

### End state (bucket 3)

The highest-leverage field in the whole spec. See
[verifiability](verifiability.md).

## Every prohibition, in every slot, passes three questions

⚠️ **This section's scope is the whole spec, not just the negatives slot above.**
The film-type counterweights, the "must not" inside continuity, the "do not" in
the animation method, the "do not take its …" in reference roles — every
prohibition qualifies.

**Prefer to write the effect you want positively.** Saying what you want lands
better than listing what you do not (reasoning in
[verifiability](verifiability.md), "write in pictures, add specifications as
insurance"). A prohibition earns its place only when the thing **would happen if
unwritten, and is expensive when it happens**.

1. **Would it happen if you did not write it?** Many things simply do not —
   **not writing ≈ a negative**. Writing the prohibition is then pure cost: it
   takes budget, competes for attention, and may block what you wanted too
2. **How bad is it if it happens?** Expensive to redo, or it breaks this film's
   core concept → add it. Merely "not as pretty" → skip it; fix it in the skin
   next version
3. **If the model reads this prohibition as "none of this whole category", do I
   still accept that?** The first two decide **whether to add it**; this one
   decides **how to write it**. See below.

### Question three: a prohibition's scope gets widened to the category it belongs to

**You write a point; the model may execute the whole axis that point sits on.**

Two instances from different dimensions. Same mechanism, **different evidence
strength**:

| Prohibition written | Meant to cancel | Widened into | Evidence |
|---|---|---|---|
| "no 3D" | 3D **rendering** (volumetric light, material reflections, soft shadows) | The whole **space** axis — flat painting's own depth devices went with it | ✅ **Measured**: the picture passed every line item but read flat and monotonous; a second reference film proved purely flat rendering can carry real depth |
| "no music" | **Melodic score** | Possibly the whole **audio** axis — ambience and spot effects silenced along with it | ⚠️ **Not measured**: after that block was deleted, the model's own music and effects tracked the story well; but no comparison run kept the block |

A named term's bias "pulls in a direction". What you are cancelling is **that
direction**, not **everything on that axis**.

**The fix is not deleting the prohibition — it is writing the half you want to
keep positively as well**:

```text
weak:    no music
strong:  ambience and spot sound effects, no melodic score

weak:    no 3D
strong:  rendering is flat colour blocks with no volumetric light or material
         reflections; space keeps real depth and front-to-back occlusion
```

⚠️ **This failure is harder to spot than "the prohibition did not hold".** Not
holding means the style drifted — visible at a glance. Over-prohibiting means
**what should have been there never appeared** — every line item passes, the
checklist is a full score. It is isomorphic to
[constitution](constitution.md) rule 10's "under-writing leaves no trace",
occurring one layer down: **you think you switched off one lamp, and you pulled
the breaker.**

### ⚠️ The boundary against constitution rule 10

[Constitution](constitution.md) rule 10 is **one-directional**: it forbids only
"writing less because you think the model handles it poorly". This section looks
like encouragement to write less, so the two must be kept apart — **the
distinction is positive statement versus prohibition**:

| | Default | Reason |
|---|---|---|
| **Positive description** (what you want) | **More rather than less** (rule 10) | Under-writing leaves **no trace** in the output; the cost is an order of magnitude higher |
| **Prohibition** (what you do not want) | **Filter by severity** (this section) | Over-writing is visible and removable — but not free |

The severity tiers come straight from rule 10's table: **something the user
stressed, left out = most severe / not stressed, wanted on watching = add it to
the skin / written too much = light.**

Together they are the full trade-off: rule 10 covers the cost of writing less,
this section covers the cost of writing more.

## Chaining multiple segments (only when a previous segment exists)

⚠️ **Scope**: this section applies only to a segment that **follows another
generated artefact** — never to a first segment, a single-segment film, or an
unchained multi-shot piece ([constitution](constitution.md) rule 11).

The previous segment's end state is this segment's **given**, not the whole of
its locks — buckets 1 and 2 are still written in full from scratch; terms,
parallax and identity all get rewritten.

### Look first, then choose one of two for every subject

```text
continue: state explicitly that it persists, and what keeps it readable under
          the new conditions
clear:    state explicitly that it disappears, and that this segment shows no
          more of that object / its kind / that category
```

**Writing neither = it will be kept, and possibly amplified.** That is the only
reason this section exists.

Two filled templates → case library E7. The counter-case is recorded there too:
a phrasing of "A's outline stretches and deforms into B" was executed as
**enlarging A** — the transformation asked for A→B, but the mechanism specified
was "the same line stretching", and that mechanism's physical result is A
getting bigger.

### Two consequences

- **The end-state slot carries more weight when chaining.** It is not only this
  segment's close, it is the only visual condition the next segment inherits
- **Any unspecified slot propagates down the chain.** What one segment leaves
  unstated, the model fills in for you; that then enters the final frame and
  becomes the next segment's given — deviations accumulate along the chain
  instead of self-correcting (example → [observations](observations.zh-CN.md),
  "unspecified slots get filled by the model")

### ⚠️ Chaining is not extension; their defaults point in opposite directions

| | What the seam should be |
|---|---|
| **Extension / continuation** (the same shot continuing in time) | The seam should be hidden |
| **Chaining** (a new narrative segment, borrowing only a first frame) | **The seam is the hard cut** — it is the technique |

Applying one's default to the other is the ready-made trap of
[constitution](constitution.md) rule 11: two scenarios with similar names and
opposite defaults.

## Two writing conventions

These govern where text sits, not what it says.

**Restate the two or three most expensive locks at the physical end.** Recency
helps. This is not a fourth bucket — the content still belongs to buckets 1 and
2 and appeared there first. Restate two or three, not the whole list.

**When a model writes the spec for you, state the output order explicitly.**
Without it the buckets bleed: global rules end up in beat 3, locks get restated
as events. Put the section names and their order into the instruction.

## Worked example

A complete filled spec lives in the case library →
[case-library.zh-CN.md](case-library.zh-CN.md), case C.

**Write your own before opening it.** When you do look, look at two things only:
**the structure** (which slots are filled, which are empty) and **what it does
not have** (no per-shot durations, no per-stage camera vocabulary, no piles of
adjectives). Its content belongs to that film.

## Common failures

| Symptom | Cause | Fix |
|---|---|---|
| Style holds early, drifts later | A global rule was written into stage 1 | Move it to bucket 1 |
| The model invents extra pauses | Second-level granularity on a continuous action | Drop to stages, or no timing |
| A reference's background leaks in | The role was written half-way | Add the "what must not be taken" half |
| Two subjects merge or swap | Bound as a group instead of individually | One binding line per subject |
| Long prompt, weak result | A pile of adjectives replaced the premise | Write that one sentence |
| The film does not close | The last stage has no end state | State the visible closing condition |
| The overlay is there early, gone later | The overlay was written into one stage | Move it to bucket 1's persistent overlay |
| The overlay generates as a static sticker | The movement half was written unverifiably ("drifts slightly", "sweeps continuously") | Give every item a countable quantity: how often it jumps, how many per second, how fast it scrolls |
| Every end state met, yet the film is flat | **Several possible causes. Do not default to blaming an empty slot** | Check in this order: ① **how many things change simultaneously within each shot** — flatness is usually single-layer shots, unrelated to how many slots you filled; ② were the film-type terms copied from another film (next row); ③ was the premise written as a genre label |
| **Every lock held, every end state met, but the whole art direction belongs to someone else** | **The film-type term synthesis came wholesale from another film** | The synthesis has to grow from *this* film again. **This is the best-hidden failure of all**: every lock is working, and what it is working towards is another film's direction. Line-by-line checking cannot find it — only comparing the terms against this film's visual language can |
| "Full" prescribed for an "empty" film | The two 〔as needed〕 slots were filled by copying a high-density film | Return to the question above: does this film's impression come from more information or less |

## Related

- [case-library.zh-CN.md](case-library.zh-CN.md) — worked fills per slot
  (**write your own first**)
- [verifiability.md](verifiability.md) — how to write each field so it can be
  checked
- [portability.md](portability.md) — which fields survive a change of model
- [film-type-dna.zh-CN.md](film-type-dna.zh-CN.md) — reuse a proven spec instead
  of starting over
