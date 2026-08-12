<!-- sync-source: slot-filling.zh-CN.md sha256:3783e5c4b32d -->

# Filling slots, and working backwards

[spec-format.md](spec-format.md) defines what the slots are. This file is about
**what to do when they are empty**.

The slot table itself is independent of input form. What a user hands you comes
in three kinds, and the target is the same:

| Input | Route | Main risk |
|---|---|---|
| A subject / a story | **Complete** — derive the rest from the premise | Filling with adjectives: looks full, is empty |
| An aesthetic description / a reference image | **Complete + partial reverse-engineering** | Copying "what you see" straight into slot values without attribution |
| A finished film / someone else's prompt | **Reverse-engineer** — recover decisions from the artefact | Treating everything observed as a decision |

**Decide the route before starting.** Mixing them wastes the work: completing
means deriving your own premise, whereas reverse-engineering **must not** — the
premise is already in the artefact, and inventing a new one throws the input
away.

### When the input is one image, first decide whether it is a first frame or a reference

The two are **selected differently**, because different things determine their
position:

| | Position determined by | Therefore |
|---|---|---|
| **First frame** | **Narrative** — it must be frame 0 of the story | No choice about it |
| **Reference image** | **Information content** — it only has to carry a lot | **It can be a setup image that never appears in the film** |

⚠️ **The default move — using the first frame as the reference — often lands on
the weakest frame available.**

Observed: one film opened on the subject curled up asleep — body balled up,
identity invariants invisible, several key elements not yet in shot: the
**lowest**-information frame in the whole piece. Switching to a purpose-made
setup image (subject frontal and centred, every element in its place) let the
same prompt lock seven things at once: medium texture, palette, all of the
subject's identity invariants, object design and layering, compositional rule,
spatial relations, palette range.

**Test: how many locks does this frame carry at once? The frame carrying the most
wins, regardless of where it sits in the film.**

State the cost alongside: you gain information content, but **frame 0 is no
longer pinned** — the opening pose then has to be written explicitly in the
prompt, and that part cannot be skipped.

---

## Completing

When the user gave only a subject, fill in dependency order, not table order:

1. **Write the director's premise first.** One sentence. It is the tie-breaker
   for every slot after it, and the only slot that cannot be derived from the
   others. (It is still not mandatory — see
   [spec-format](spec-format.md#directors-premise-bucket-1))
2. **Film type.** For a proven type, load its DNA and re-skin rather than
   re-deriving (see [film-type-dna.md](film-type-dna.md))
3. **Granularity.** It belongs to the DNA; ask only when writing from scratch,
   and recommend with a reason rather than presenting a bare menu
4. Derive the remaining slots from the premise
5. **Write the negatives last**, and only for what this film could really produce
   and would be expensive to redo

**Empty beats padding.** A slot you cannot fill means either it does not matter
to this film, or the premise is not thought through — neither case is fixed by
adding adjectives.

---

## Working backwards

Recovering filled slots from a finished film, a reference image, or someone
else's prompt.

### Flow

1. **Check objective facts before looking at the picture.** Duration,
   resolution, frame rate, container metadata, whether an audio track exists
2. **Segment the structure.** Cut points, the visible end state of each stage
3. **Work the audio channel** (below)
4. **Fill bucket 1 → 2 → 3**, in that fixed order, or they bleed
5. **Attribute**, and route the results (below)
6. **Write the coverage statement** (below)

### Four rules for working backwards

**① Check container metadata first; it costs almost nothing.**
Producer tags, task IDs, encoder, distribution traces are all in there. It
settles "who generated this", and identifies which parameters are the
distribution pipeline's transcode values and **must not be taken as model
specifications** (a non-standard aspect ratio is usually a transcode crop).

**It cannot settle segment count.** That has to be derived from the model's
duration ceiling, and the ceiling can only be asked about or measured.
**A platform API's parameter enum neither proves the model's ceiling nor lets
you derive segment count.**

**Watch for aggregator behaviour when probing ceilings.** The rule in SKILL.md —
"submit the value you want; a rejection creates no task and costs nothing" —
holds when connecting directly to a vendor; **on an aggregator it may not**. The
gateway does not validate at submit time, returns success, creates the task, and
the upstream rejects it afterwards. Expect a created-then-failed task rather
than a submit-time error. **"Task created" does not mean the parameter was
accepted.**

**② Audio is the highest-density channel, and it can be quantified.**
The volume envelope gives the overall structure (intro / main / drop / outro);
extracting onsets and comparing them against cut points gives hard numbers
instead of impressions. Both bucket 1's film type and bucket 3's stage
boundaries can be read from here.

If there is an audio track, use this channel — do not go by picture alone.

**③ Observation precision ≠ the precision that belongs in the spec.**
This trap is specific to working backwards; it does not exist in the forward
flow. Measuring frame-level audio-picture sync on a finished film and copying
that into second-level timestamps makes the next generation *worse* — because
that precision may not have come from the prompt.

**Working backwards requires one extra step: attribution.** Did this
characteristic come from the prompt, or from the model?

| Attribution | Handling |
|---|---|
| Came from the prompt | Write it into the spec |
| Model-internal behaviour | Record it in the [model profile](model-profile-schema.md), **not in the spec** |
| Caused by the distribution pipeline | Discard it |

Test: at the moment the prompt was written, did this information exist? — but
watch for the reverse trap: **if the author did write it into that same prompt
(music structure, for instance), then it did exist.** Do not assume something is
unspecifiable just because it is generated.

**④ A single-threshold cut detector systematically misses rhythm sections.**
Devices like background inversion and colour-block flicker **do not change
picture content**, only its graphic geometry, and scene detection at ordinary
thresholds does not see them. The result is reading a high-density section that
inverts eight times a second as "one static shot".

Run several thresholds, and extract dense frames (≥6fps) to look with your own
eyes.

### Route the results

What you recover **does not all belong to the spec**. Store it by the three
portability layers:

| Layer | Examples | Goes to |
|---|---|---|
| Language | The slots across all three buckets, end states, observable cues, technique vocabulary | The spec |
| Bias | Observations about anti-default suffixes, which negatives did not take effect as expected, a film-type term's bias strength | The model profile |
| Capability | Duration ceiling, multi-shot in one generation, native audio, timing adherence | The model profile |

**Mixing them is the most expensive error in working backwards**: a rule true
only on one model gets written into the spec, and next time you change models
you carry the previous model's quirks into the prompt.

Likewise, **when extracting film-type DNA from a reverse-engineering pass, a
model-dependent condition is not DNA** (see film-type-dna.md, "Adding a new film
type", item 5).

### The coverage statement is mandatory

Working backwards relies on extracted frames, and extracted frames have a blind
spot (see SKILL.md §6). When delivering the result you must state which half it
covers:

| Dimension | Can stills settle it? |
|---|---|
| Texture, composition, palette, identity, end states | Yes |
| Cut rhythm, audio-picture sync | Yes, and it should be given as numbers |
| In-shot motion quality, interpolation smoothness, deformation | **No** |

Either watch it, or state what is not covered. **Do not issue an overall verdict
from stills** — a film can win on every frame and lose on all of its motion.

---

## After working backwards

What comes out is a filled spec, with the same standing as a hand-written one:
compile it to the target model as usual, review it against
[checklist.md](checklist.md) as usual.

**The way to validate it is reproduction.** Run the recovered spec once and
compare against the original slot by slot. A slot that does not match is a slot
you got wrong — cheaper than any amount of reasoning on paper.

## Related

- [spec-format.md](spec-format.md) — what the slots are
- [verifiability.md](verifiability.md) — how to write slot values so they can be
  checked
- [portability.md](portability.md) — criteria for the three-layer routing
- [film-type-dna.md](film-type-dna.md) — turning what you recovered into
  re-skinnable DNA
- [model-profile-schema.md](model-profile-schema.md) — where the bias and
  capability layers get recorded
