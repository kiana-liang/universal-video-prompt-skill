<!-- sync-source: portability.zh-CN.md sha256:85c7c0b3c561 -->

# Portability

The spec is portable; the lines inside it are not all portable. Sort every line
into one of three layers, because each needs different handling — and only one
of them can be written once and used everywhere.

| Layer | What it is | Handling | Stored in |
|---|---|---|---|
| **Language** | Structure and observable description | Write it as-is | The spec |
| **Bias** | Words that counter one model's default tendency | Measured per model | The model profile |
| **Capability** | What the interface can physically accept | Probe, then degrade | The model profile |

The most common cross-model error is **treating a bias-layer line as a
language-layer line** — copying an anti-default suffix that worked on one model
to another and assuming it still helps.

## Language layer — portable

- The three-bucket structure and scope discipline
- End states, in all three forms
- Observable emotion cues
- Term plus description, written twice
- Reference roles written as "controls X, do not take Y"
- Event-triggered progression

These depend on nothing but the model understanding language. Write them once.

## Bias layer — measure, never assume

Every generative model has defaults it regresses to. Bias-layer text exists to
counter **that model's** defaults, so it does not migrate:

| Phrasing | Why it belongs to the bias layer |
|---|---|
| `keep real pores and skin texture` | It counters a smoothing/beautifying default. On a model that already renders rough skin it **overshoots**, and the face gets dirty |
| `no subtitles, no background music` | Only needed where spurious subtitles and music actually appear |
| Specific transition vocabulary | Recognition varies; some words are culturally scoped |
| `@image1` versus `Reference Image 1` | Interface addressing syntax |
| A negatives list as a whole | Every model fails differently |

Two of these need special handling.

### Anti-default suffixes: overshoot is a real failure

Do not copy an anti-default phrase across without checking the target's
baseline. The test is cheap: same spec, one run with the phrase, one without. If
**the version without** already meets or exceeds the goal, then in this
observation the phrase is working against you — record the observation, and do
not promote it to "this phrase does not work". **Record both results** — that is
what the "did not take effect as expected / overshot" field exists for.

### Addressing syntax: the one thing that must be translated

This is the common case where description cannot substitute. When a model
expects a particular token to bind an asset, that token must be emitted exactly,
or the binding is lost. Keep the mapping in the profile, translate at compile
time, and **leave the surrounding sentence structure alone**.

## Capability layer — probe, then degrade

These are not comprehension gaps. They are hard limits on what the interface
accepts.

| Capability | Why it matters |
|---|---|
| Reference addressing and count | Determines how much of a multi-reference spec survives |
| Multi-shot in one generation | Determines how many shots fit in one request |
| Hard cut support | Same |
| Duration ceiling | Determines how many stages fit per request |
| Timing adherence | Determines whether second-level granularity is honest |
| Audio: native / reference-only / none | Determines whether audio lines belong in the prompt at all |

### Probing

No profile means no assumptions. Run the smallest test that settles the
question, then record it. In ascending order of cost, stopping as soon as the
spec is satisfiable:

1. **Read the published specification** — reference ceiling, duration,
   resolution. Trust the actual model page over documentation samples; HTTP 200
   is not confirmation, read the page content to confirm the model exists.

   ⚠️ **Published enums are assumptions, not limits.** Documented ranges are
   often narrower than what can actually be submitted, and a page can contradict
   itself — one page was observed stating three different duration ranges in
   three places. **Submit the value you actually want and let the API answer.**

   The error is asymmetric: trusting a too-narrow doc → the spec is silently
   degraded → the run succeeds → nothing in the output reveals that a better
   configuration was available. Nobody notices.

   > ⚠️ **"Rejected means no task and no charge" holds only on a direct vendor
   > route.** On an **aggregator** it may not: the gateway does not validate at
   > submit time, returns success, creates the prediction, and the upstream
   > rejects it afterwards (`status=failed`, `executionTime=0`). **"Task
   > created" does not mean the parameter was accepted.** When probing limits
   > through an aggregator, expect a created-then-failed task rather than a
   > submit-time error — and probe the parameter with the shortest duration and
   > lowest resolution rather than with a full job.

2. **One minimal generation** — everything behaviour-dependent needs this.
   Timing adherence and multi-shot capability cannot be read; they have to be
   run.

3. **Record immediately, including failures.** An unrecorded probe gets re-run at
   full price by the next person.

The single most valuable probe: run the same spec once at `stages` and once at
`second-level`, and measure the deviation between requested and actual beats.
That one comparison settles the model's default granularity.

> ⚠️ **"Once each" is not enough on a high-variance model.** Observed: in one
> such comparison, the **within-arm** variance of two numeric indicators (cut
> count, near-static frame ratio) was ≥ the between-arm difference — cut count
> differed twofold within the same arm, and near-static ratio by 10.5 percentage
> points. At n=1 per arm the test fills no field and only yields a conclusion
> that will not hold.
>
> Two companion practices:
> - **At least n=2 per arm.** Measure within-arm variance first, then check
>   whether the between-arm difference exceeds it
> - **The decision threshold is only valid after both arms have been measured.**
>   Extrapolating a threshold from one arm's variance backfires — that
>   "pre-check" is itself an n=1 conclusion
>
> If the comparison comes back as "no measurable difference", that is a valid
> result too: take the looser setting per "the loosest granularity that meets
> the constraint", and note the sample size in the profile.

### Degrading

| Missing capability | Degrade to |
|---|---|
| Multi-reference addressing | One image locks identity; carry the rest in text |
| Multi-shot in one generation | One shot per request, chained on boundary frames |
| Reference count below spec | Merge roles by priority: identity > key prop > scene > style |
| Duration below spec | Split into stages that each stand alone, then chain on boundary frames |
| Weak timing adherence | Drop to stages plus end states |
| No native audio | Rewrite audio lines into what the picture can carry — do not move them out of the film |
| Single-image I2V only | First frame as the only visual lock; everything else in text |

**A degrade must be reported.** A silently degraded spec looks identical to one
that ran as written, which makes the output unexplainable and quietly
contaminates anything built on top of it.

## Fair comparison

If the purpose is comparison rather than delivery, degrading destroys the
comparison itself — you end up comparing two different specs. A controlled
comparison requires:

- The spec sits in the **intersection** of both models' capabilities. Do not
  compare a 30-reference model against a 9-reference model using a
  30-reference spec
- **Translate only the addressing syntax**; keep every other word identical
- **Exclude bias-layer lines** from the comparison, or run them as a separate
  variable. An anti-default suffix tuned for model A is a handicap given to
  model B
- Record what you held back for this. A comparison whose constraints are
  unstated reads like a general conclusion when it is only a narrow one

## Related

- [model-profile-schema.md](model-profile-schema.md) — which fields to record
- [verifiability.md](verifiability.md) — the language layer in full
- [spec-format.md](spec-format.md) — where each layer's content sits in the spec
