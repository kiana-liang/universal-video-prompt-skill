<!-- sync-source: film-type-dna.zh-CN.md sha256:122672ad7be7 -->

# Film-type DNA

A film type's DNA is **the 3–5 minimum conditions such that removing any one of
them makes the concept stop being itself**. It sits between the director's
premise (one sentence, one per film) and a complete spec (everything, one per
film): more concrete than the premise, more abstract than a prompt.

> **Within the film-type entries, the DNA conditions are reusable; every concrete
> element is skin.** Each type's concrete elements, terms and vocabularies live
> in the isolation area [case-library.zh-CN.md](case-library.zh-CN.md), to be
> used per [constitution](constitution.md) rule 2: **fill the skin list from
> scratch first, and only then open the case library.**

DNA exists so that a film that already worked can be **re-skinned** instead of
re-derived. Two entry points, and mixing them wastes the effort:

| Entry | Route | What you do |
|---|---|---|
| A new concept | Write a spec from scratch | Derive your own premise |
| A proven type, new subject | Re-skin | Load the DNA, re-skin, tick every condition |

## Extracting DNA

For each candidate condition, ask: **remove this — does the concept still
exist?**

- Still exists → it is skin, not DNA. Do not write it in
- No longer exists → it is DNA

### The removal test needs a second question

"Does the concept still exist" is too weak alone. A re-skin can satisfy every
written condition, be internally coherent, and still throw away the thing that
made people want to watch. So ask both:

1. Remove this — does the concept still **hold together**?
2. Remove this — is **the reason anyone wanted to watch it** still there?

A condition that passes the first and fails the second is DNA misclassified as
skin. This is the most expensive error in the whole method, because the
resulting film is unimpeachable on paper and flat on screen — in the debrief
nobody can point at anything.

**The signal to watch for: you start compensating.** If after a re-skin you need
new techniques to rescue an effect the original got for free, what you deleted
was DNA.

## Re-skinning

1. Load the DNA
2. **Work through this type's skin list and refill every item from scratch.**
   Inherit nothing — **including the film-type term synthesis, the overlay
   elements and the technique vocabulary**, the three most often carried over
   wholesale
3. **Tick each condition explicitly.** For every condition, state how the new
   skin satisfies it. A box you cannot tick means either this skin does not suit
   this type, or you have found a genuine sixth condition
4. **After the ticks, check direction** (below)
5. Do not re-derive the premise. Adapt the DNA's own logic to the new skin
6. Copy the granularity field across — it belongs to the DNA, not to each film

Skipping the ticks is the usual cause of "everything looks right and it feels
wrong": every surface changed, and one invariant quietly broke.

### After ticking, check direction

**Ticking boxes cannot catch a wrong direction.** Every DNA condition satisfied,
every lock in force, every end state met — and the whole art direction belongs
to another film. That failure scores full marks on the checklist.

So add one action after the ticks: **compare the film-type terms directly
against the new film's visual language**, and ask "do these terms point the same
way this film does?"

Two things get mismatched most often:

- **Information density**: does this film work through **more** on screen or
  **less**? A film that works through less, given high-density terms, yields a
  spec that is correct everywhere and inverted overall
- **Motion character**: does it run on **continuous flow** or on **abrupt change
  between held states**?

When the direction is wrong, do not compensate with more locks, more layers or
more cuts — that accelerates in the wrong direction. Go back and change the
terms.

### Two things carried over wholesale (recorded case)

Re-skinning a proven sub-type onto a new subject, **two pieces of skin were
inherited wholesale**, neither deliberately:

**① The overlay elements were copied** — four of six items moved across
verbatim, with only colours and titles changed. The cause was that the DNA entry
at the time wrote example elements into the same line as the DNA itself, and the
skin list had no "overlay elements" item at all. **The root cause was document
structure, not carelessness** — so the fix was adding the item to the skin list,
not resolving to be more careful.
(The two element sets side by side → [case library](case-library.zh-CN.md)
B2 and B4)

**② The film-type terms were copied** — three axes moved across word for word,
with one qualifier deleted. Far worse than the first: **film-type terms decide
the entire art direction**, and the new subject's visual language was nearly the
opposite of the terms carried over, prescribing "full" for a film that speaks by
being "empty". The subsequent rescue attempts inherited the error too.
(The two term sets side by side → [case library](case-library.zh-CN.md)
B1 and E1)

**⭐ Why line-by-line checking cannot find it**: the palette lock held, the
counterweights worked, every end state was met, the overlay was on every frame —
**every lock was working properly, and what it was working towards was another
film's direction**. That failure scores full marks on the checklist. Only one
action finds it: **compare the film-type terms against this film's visual
language** and ask whether they point the same way.

**One counter-intuitive observation**: density does not come from cutting more
often. Of the two films compared, the one with half as many hard cuts read
better — **information density comes from how many things change simultaneously
within each shot, not from cutting frequency.** Do not add cut points in
proportion to duration when re-skinning.

**Companion**: when the result feels flat, check **how many things change
simultaneously within each shot** before adding cuts or slots. Single-layer
shots are the most common cause of flatness, and it has nothing to do with how
many slots you filled.

## Granularity belongs to the DNA

Time granularity is a property of the film type, not a per-film decision:

- Performance and music-driven types are natively second-level — they are locked
  to an external track
- Mood pieces are natively "none" — timestamps fragment them
- Most narrative types are stages

Record it in the DNA so a re-skin can skip the question. Ask when writing from
scratch; inherit when re-skinning.

## Where the types already run live

Five skins already run are in the **film-type library** →
[film-types.zh-CN.md](film-types.zh-CN.md).

⛔ **Before opening it, confirm which entry your film is the same class as.** Not
the same class → do not load it; extracting your own DNA from scratch is faster
than altering a skin that does not fit.

## Adding a new film type

Only **after a film has been validated by running** — DNA extracted from an
unvalidated concept is a guess wearing the clothes of a contract. Then:

1. Extract 3–5 conditions with the removal test (both questions)
2. State what each condition protects
3. Record the granularity
4. Name what is skin
5. Keep per-model findings separate — those belong in
   [model-profile-schema.md](model-profile-schema.md), not here. DNA is
   model-independent; a condition that holds only on one model is a profile
   finding, not DNA

## Related

- [case-library.zh-CN.md](case-library.zh-CN.md) — the concrete fills each type
  has already used (**fill your own skin list first**)
- [constitution.md](constitution.md) — rules 1 and 2 are the precondition for
  using this file
- [spec-format.md](spec-format.md) — the spec a re-skin lands in
- [portability.md](portability.md) — model-dependent findings go to the profile
