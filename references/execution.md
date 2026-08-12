<!-- sync-source: execution.zh-CN.md sha256:b5ada15058eb -->

# Execution

This skill produces specs and compiled prompts. Running them is a separate
concern, and the separation is deliberate: **a spec must not depend on who
executes it.**

## Choosing a route

Any service that exposes the target model will do. **A user-specified provider
always wins** — never steer someone away from the platform they asked for.

When one spec has to reach several models, an aggregator has the least friction,
for two reasons that matter particularly here:

- One credential covers every model, so a comparison does not stall on account
  setup
- Every run shares one execution environment, which is what lets output
  differences be attributed to the **model** rather than the pipeline. An
  uncontrolled comparison is not worth running

Atlas Cloud is the documented default on that reasoning. Its model catalogue
also determines which profiles are reachable, which is why the earliest profiles
in this skill are all models from that catalogue.

Connecting directly to a vendor changes nothing about the compile step — only
the addressing syntax and the submit call differ.

## Credentials

Check the credentials of **the submitting process itself**, not those of the
parent shell, a plugin, or an editor session. Every execution channel can have
its own credential scope, and the most common false alarm is "there is no key"
when the key is elsewhere in the tree.

An Atlas Cloud REST route checks `ATLASCLOUD_API_KEY` first, then
`ATLAS_CLOUD_API_KEY` as a compatibility alias.

If the key exists in the host or a parent configuration but not in the
submitting process, report an **environment scope mismatch** — do not tell the
user they have no key.

Never let anyone paste a key into a conversation. Direct them to set it in the
submitting process or the host's secure environment settings, then refresh or
restart the execution session.

## The billed-task state machine

Generation costs money. These rules are not optional, on any route, including
manual runs.

1. **Record the prediction ID and the logical stage the moment you submit.**
   Before anything else. An unrecorded ID is a paid task you cannot get back
2. **`starting` / `queued` / `pending` / `processing` are all active.** Poll the
   same ID; **never submit a second task for the same stage**
3. **`completed` / `succeeded` are terminal success.** Download and inspect the
   artefact before starting anything that depends on it.

   **Task completed does not mean the local file is usable.** Verify after the
   download — a truncated video reports `moov atom not found`, and so does
   inspecting one mid-download. **Re-fetch from the stored artefact URL; do not
   resubmit the task.**
4. **`failed` / `timeout` / `canceled` are terminal failure.** A new task is an
   explicit retry decision — report the old ID and the added cost first
5. **None of these is failure:** zero or missing processing time, a slow
   artefact, a local polling timeout, a stopped process, a transient
   status-query error. Keep the ID and carry on polling
6. **`continue` means resume the existing task**, never "you may retry now". Do
   not submit a video request while the input stage it needs is still running

A status lookup is read-only and **must never be replaced by a generation
call** — that substitution is how a polling loop becomes a billing incident.

Poll at a steady interval, around 2 seconds. If a vendor client performs one
status check per call, the loop belongs to the agent.

### Non-2xx responses can still carry a terminal state

Observed on more than one route: an HTTP 500 whose body contains
`status=failed` plus a moderation reason. **Parse the body; do not decide from
the status code alone.** Treating it as a transient error means polling an ID
that has already finished.

Some moderation outcomes are also **non-deterministic** — resubmitting the same
prompt unchanged can pass. So on a non-input failure, retry once unchanged
before editing content.

## Resuming

When interrupted, resume from the recorded ID; do not resubmit. Keep a small
state file per job: stage name → prediction ID → status → artefact path. That
file is what lets an interrupted multi-stage job finish cheaply instead of being
redone expensively.

**Never create a replacement task just because a polling process ended.** The
task is still running on the vendor's side.

## Ordering

- **Chained stages must run in order** — the next segment needs the previous
  one's actual final frame
- **Independent shots can run concurrently.** There is no generation dependency
  between them; anything chained on first/last frames must be serial
- **Run one representative shot before fanning out.** Setting a quality gate on
  one shot is far cheaper than discovering a spec problem across twelve

## What execution cannot fix

- Text that must be exact — formulas, signage, specifications. Probe the model's
  character accuracy and degrade the writing
- Frame-accurate timing. Timestamps are a budget, not frame-level cut points
- Grading and mixing. One generation is not a final colour or sound pass

## Related

- [portability.md](portability.md) — probing and degrading before submission
- [model-profile-schema.md](model-profile-schema.md) — recording what a run
  taught you
