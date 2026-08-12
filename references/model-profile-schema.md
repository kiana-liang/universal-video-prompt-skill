<!-- sync-source: model-profile-schema.zh-CN.md sha256:2893f55b5f0e -->

# Model profile — field definitions

> **This file is a declared exception to [constitution](constitution.md) rule 3
> (physical isolation of examples).** A profile has to contain concrete words —
> "how does this model react to the term *cel-shaded*" is exactly what a profile
> records, and replacing that with a placeholder empties it of meaning.
>
> But keep two things apart: **the concrete words in a profile are "one model's
> measured reaction", not "how you should write".** It answers "I wrote X and
> this model gave me Y", not "you should write X". For fills, go to the
> isolation area [case-library.zh-CN.md](case-library.zh-CN.md), and read
> constitution rules 1 and 2 first.

Profiles are what make this skill **adjust to models** rather than merely
describe them. This file defines the **fields**; each model has its own filled
instance.

Two rules run through every item:

1. **Record measurements, not impressions.** "Timing drifts" is unusable; "in a
   15-second piece the requested beats land about 2 seconds late" compiles into
   a decision
2. **"Unknown" is a legitimate value.** An empty field triggers a probe; a
   guessed field silently contaminates every compile and every comparison built
   on it

## Template

```markdown
# Model profile: <vendor>/<model>

Last verified: <date> · Verified by: <who> · Service: <which one you called>

## Capability layer

| Field | Value | How verified |
|---|---|---|
| Reference addressing syntax | | |
| Reference count ceiling (image / video / audio) | | |
| Asset input format | | |
| Multi-shot in one generation | yes / no / partial | |
| Hard cut support | yes / no | |
| Duration range | | |
| Resolution options | | |
| Native audio | native / reference-only / none | |
| Timing adherence | | |
| Recommended granularity | none / stages / second-level | |
| First frame / first-and-last frame | | |
| Extension or chaining | | |
| Video editing | | |
| Prompt-length tolerance | | |

## Bias layer

| Field | Value | How verified |
|---|---|---|
| Default aesthetic bias | | |
| Anti-default phrasings that worked | | |
| Did not take effect as expected / overshot | | |
| Negative-lock behaviour | | |
| Recognisable transition vocabulary | | |
| Language sensitivity | | |

## Known failure modes

- <what breaks, under what conditions, whether there is a way around it>

## Compile notes

- <special handling required for this model>
```

## Field notes

### Capability layer

**Reference addressing syntax** — the exact token that binds an asset. The one
thing that must be translated rather than described around. **Record it
literally.**

**Reference count ceiling** — record per type, and record a total if one exists.
When a vendor gives both a "stable range" and a "documented ceiling", record
them separately — stability usually starts degrading before the hard ceiling.

**Asset input format** — how the image or video is packaged for submission
(bare base64, a prefixed data URI, a URL, an uploaded asset ID). Worth its own
field because **it is not consistent across routes** — two routes have been
observed to require opposite packaging for the same image, and getting it wrong
means the task never gets created.

**Multi-shot in one generation** — can one request produce ordered shots with
cut points? `partial` means it works but is unstable; say under what conditions
it fails.

**Hard cut support** — separate from multi-shot. Some models produce several
shots but always join them with motion.

**Duration range** — and whether duration is set by parameter or inferred from
the input. Record which task types lock it.

**Native audio** — `native` generates sound, `reference-only` accepts audio
input only, `none` means audio lines should be dropped at compile time.

**Timing adherence** — record the measurement, with the clip length it was
measured at. **Direction matters**: a consistent lateness can be compensated by
writing earlier; instability cannot be compensated at all.

**Recommended granularity** — the conclusion derived from timing adherence. This
is the field the compiler actually reads.

**Prompt-length tolerance** — what this model sacrifices as the prompt grows.
Differences between models are large in practice: one model was observed to lose
its entire opening and dilute its texture locks on a longer prompt, while
another held everything across the same two prompts.

### Bias layer

**Default aesthetic bias** — where it lands with no style instruction. Be
specific: `smoothed, beautified faces`, `CG-looking surfaces`, `oversaturated
grade`. This is what anti-default phrasing has to fight.

**Anti-default phrasings that worked** — phrasings measured to move the output
**on this model**.

**Did not take effect as expected / overshot** — equally valuable, and the field
most often skipped. This is where "a trick imported from another model backfired"
gets recorded.

> ⚠️ **This column records "I wrote X and observed Y in this slot", not "X does
> not work".** Per [constitution](constitution.md) rule 9: a slot's effect
> overflows its own scope, so no single-slot observation supports the conclusion
> "this phrasing is useless" — it may be working elsewhere, in a place you did
> not measure.
> It has happened once: one model's music section was recorded as "ineffective,
> deletable", and a later controlled comparison showed what it changed was the
> picture's rhythm.

**Negative-lock behaviour** — are negatives respected? Which class fails?

**Recognisable transition vocabulary** — which named transitions land without
qualification. Everything else needs term-plus-description.

**Language sensitivity** — does prompt language change the result? Which
language is strongest? Record it too when a term works in only one language.

## Where the filled profiles live

The filled profiles are in the **observation isolation area** →
[observations.zh-CN.md](observations.zh-CN.md).

⛔ **Do not open it while writing a prompt.** It has two legitimate uses: post-hoc
diagnosis after a run (read the whole thing), and compile-time degrading before
submission (**read only the capability-layer entries that would actually error**).
The bias layer and failure modes are never read while writing — the reasoning is
at the top of that file and in [constitution](constitution.md) rule 9.

## Where profiles come from

A profile is the **output** of comparison work, not its precondition. Running one
spec across several models **is** how these fields get filled — which is to say a
comparison matrix is a data-collection exercise, and its deliverable is the
filled table, not just the videos.

The single most informative test: run the same spec once at `stages` and once at
`second-level`, measure the deviation, and fill three fields at once — timing
adherence, recommended granularity, and usually a failure mode as well.

> ⚠️ **"Once each" is not enough on a high-variance model.** Observed: in one
> such comparison the **within-arm** variance of two numeric indicators (cut
> count, near-static frame ratio) was ≥ the between-arm difference — cut count
> differed twofold within one arm, near-static ratio by 10.5 percentage points.
> At n=1 per arm the test fills no field, and yields a conclusion that will not
> hold.
>
> Two companion practices:
> - **At least n=2 per arm.** Measure within-arm variance first, then check
>   whether the between-arm difference exceeds it
> - **A decision threshold is valid only after both arms have been measured.**
>   Extrapolating one from a single arm's variance backfires — that "pre-check"
>   is itself an n=1 conclusion
>
> If the comparison comes back "no measurable difference", that is a valid result
> too: take the looser setting per "the loosest granularity that meets the
> constraint", and note the sample size in the profile.

## Related

- [portability.md](portability.md) — how the compiler consumes these fields
- [checklist.md](checklist.md) — pre-submission review
