<!-- sync-source: checklist.zh-CN.md sha256:ac92cae0784a -->

# Pre-submission checklist

Run this before spending a generation. Every item corresponds to a failure that
otherwise costs a full run to discover.

## Isolation (mandatory when re-skinning or reusing an existing film type)

- [ ] Was every slot written **from this film first**, rather than filled in
      from the case library?
- [ ] Is the **film-type term synthesis** chosen afresh from *this* film's
      visual language — not the previous film's?
- [ ] If the two 〔as needed〕 slots were filled: does this film's impression
      really depend on **more** information on screen?
- [ ] Beyond ticking the boxes, did you **check direction** — do the terms point
      the same way as this film?
- [ ] Are the empty slots empty by decision, rather than forgotten?

## Spec

- [ ] Is there **one** director's premise? Two premises mean two films.
      (And it is not mandatory — an empty premise slot is a legitimate decision)
- [ ] Does the premise state a **why**, rather than a "do X every time"? An
      execution rule in this slot acquires the premise's authority and becomes
      unbreakable
- [ ] Is every line in the bucket matching its scope? A global rule written into
      one beat stops applying at the next
- [ ] Does every reference have **both halves** — what it controls, and what must
      not be taken from it?
- [ ] Is every distinct subject bound **individually**? Never
      "@image1 through @image4 define four characters"
- [ ] When several references show the same object, is the output count stated?
      (`only one lamp appears in the whole film`)
- [ ] Are references **selected per stage**, rather than required to appear all
      at once?
- [ ] Are the negatives about **this** film? Delete anything copied in that names
      a risk this film does not have

## Every prohibition, in every slot, passes three questions

- [ ] **Would it happen if you did not write it?** Many things simply do not.
      Writing the prohibition then costs budget and attention for nothing
- [ ] **How bad is it if it happens?** Expensive to redo, or it breaks the core
      concept → add. Merely "not as pretty" → skip; fix it in the skin next pass
- [ ] **If the model reads it as "none of this whole category", do I still
      accept that?** You write a point; the model may execute the whole axis it
      sits on. If you do not accept that, write the part you want to keep
      positively as well

## Verifiability

- [ ] Does every stage land on a **visible** state — not an emotion, not
      "continues"?
- [ ] Does each stage have **one** primary change?
- [ ] Is every emotion anchored to 2–4 observable cues?
- [ ] Is every uncommon craft term written as **term + observable description**?
- [ ] Are subject count, clothing, prop ownership and spatial relations stated
      wherever they must hold?
- [ ] Keyframe sequence: is the order explicit? Does each image have exactly one
      role?
- [ ] Extension: is the boundary written on the correct side — when extending
      backwards, is the source's first frame written as the **end state**?
- [ ] Does each line add a **new constraint**, or restate a **consequence** of an
      existing one? The latter is noise — delete it
- [ ] Do effect words state **which mechanism** (scale or volume, tight framing
      or shallow depth of field)?
- [ ] Does the structure a mechanism depends on **actually exist in the scene
      description**?
- [ ] Are intensity and pacing pinned to events? "Slow" gets read as "nothing
      happens in this stage"

## Time

- [ ] Was granularity decided **before** writing beats?
- [ ] Is it the **loosest** granularity that still meets the constraint?
- [ ] If second-level: is there a real external hard constraint, or was it habit?
- [ ] Are the ranges continuous and non-overlapping?
- [ ] Does any range demand an impossible density (several distinct actions in
      one second)?
- [ ] Re-skin: is granularity **inherited from the DNA** rather than asked again?

## Chaining (only when a previous segment exists)

- [ ] Did you look at the previous segment's **actual** end state?
- [ ] Does every subject in it get an explicit **continue or clear**? Writing
      neither means it is kept, and possibly amplified
- [ ] Chaining or extension? Their seam defaults are opposite — an extension
      hides the seam; in chaining the seam *is* the hard cut

## Portability

- [ ] Does the target model have a profile? If not, was a probe run and recorded?
- [ ] Is the reference-addressing syntax emitted in that model's exact form?
- [ ] Is every bias-layer line true **for this model** — not carried over from
      another?
- [ ] Was the anti-default wording checked against this model's baseline for
      **overshoot**?
- [ ] Does the spec fit the model's real reference count, duration and multi-shot
      support?
- [ ] Published enums: did you **submit the value you actually want**? Docs are
      often narrower than reality
- [ ] ⚠️ On an aggregator route, remember that "task created" does not mean the
      parameter was accepted — expect a created-then-failed task, and probe with
      the shortest duration and lowest resolution rather than a full job
- [ ] Was every degrade **reported** rather than applied silently?
- [ ] Comparison runs: does the spec sit in the intersection of both models'
      capabilities, with only the addressing syntax translated?

## Transitions

- [ ] Is every transition this film needs typed at its cut point?
- [ ] ⚠️ Nothing dropped because "another tool would be cheaper" — that is a
      workflow judgement and does not belong here
- [ ] If the spec depends on hard cuts, does this model actually support them?

## Execution

- [ ] Are the credentials in the **submitting** process?
- [ ] Is there somewhere to record the prediction ID before submitting?
- [ ] Is one representative run planned before fanning out?
- [ ] Chained stages: is the order enforced?

## After the run

- [ ] Reviewed in order — identity → locks → stage end states → motion and seams
      → audio, **stopping at the first failure**?
- [ ] Regenerating only what failed?
- [ ] **Artefact verified?** Task completed ≠ local file usable (a truncated
      download reports `moov atom not found`)
- [ ] **Was an overall verdict drawn from stills alone?** Motion, pacing and
      audio sync are invisible in stills. Either watch it, or state which half
      your conclusion covers
- [ ] Did what you learned go into the **profile**, rather than into a patch on
      this one spec?
- [ ] If this film is now validated: is it worth extracting its DNA?

## Related

- [spec-format.zh-CN.md](spec-format.zh-CN.md) ·
  [verifiability.md](verifiability.md) ·
  [portability.md](portability.md) ·
  [execution.md](execution.md)
