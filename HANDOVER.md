# CS5224 Exam Prep — Agent Handover

> **Update 3 Nov 2026 (exam over):** Joshua finished the exam and changed the purpose of the INDEX from exam study to a **key-concepts reference for industry and interviews**. `Notes/INDEX.md` is now organised by theme (T1-T9, links like "T3-9"), no stars, with a few industry staples marked *(beyond the course)*; the exam-era version is kept as `Notes/INDEX-exam-version.md`. `Notes/print/build.py` now reads the T-section headings and embeds SVG diagrams (`Notes/diagrams/`, redrawn from Joshua's hand sketches). The rest of this file describes the exam-prep period and is kept for history.

Read this in full before doing anything else. The rules here are the current ones. Where an old note disagrees with them, these win.

---

## Who You Are

You are a Cloud Computing tutor and mentor helping Joshua prepare for the **NUS CS5224 exam on Tue 3 Nov 2026** (open book, no internet, no AI, 90 minutes, 25 questions: 20 MCQ + 5 short answer, 30 marks). The goal is real understanding and the ability to apply concepts, not only passing.

---

## Plan and Progress

**Schedule (Joshua, updated 1 Nov evening):** L09, the INDEX format/readability pass and L10 all done Sun 1 Nov; **Mock B next, Mon 2 Nov**; Mock C on Tue 3 Nov (morning; the exam is that evening). There is no L08 lecture file.

| Lecture | Status | Weak spots (details in the log) |
|---|---|---|
| L01 | DONE: 17 scenarios | |
| L02 | DONE: 12 + 3 gap | on-demand self-service vs rapid elasticity; metering (Provisioning/Configuration) vs billing (Business Support) |
| L03 | DONE: 12 + gap set | dedicated pool vs resource pooling architecture |
| L04 | DONE: 11 + gap set | what on-premise vs cloud really loses (connectivity and QoS control); private vs shared storage; cooling drawback; tier choice with numbers |
| L05 | DONE: 9 + gap set | resource type vs virtualisation approach; hardware vs software-instance sharing; leaving the Docker client out of the run trace |
| L06 | DONE: 9 + gap set (about 65%) | asynchronous offloading; fixing statelessness with an external store; chaining FaaS functions by events |
| L07 | DONE: 8 + gap set (about 85%) | k-means mapper output; explaining *why* a fix works; arithmetic under pressure (G5 off by 100x) |
| L09 | DONE 1 Nov: 6 + gap set (about 60%) | configuration vs state file (twice; state does not update itself, plan/apply re-read tracked resources); separate state per environment, not just modules; IaC defines servers, health checks + auto-scaling replace them; apply reverts hand changes |
| L10 | DONE 1 Nov: 6 + gap set (about 75%) | arithmetic slips (gave hours instead of dollars; tier band off by 50 GB); tiered rates charged band by band, not all at the top rate; comparing pie-chart shares instead of dollars (Joshua calls G4 a calculation slip, so no star); building depreciation is fixed, it does not rise at low utilisation; sunk vs integration cost named loosely |
| Mock A (L01-L05) | DONE 31 Oct: 21.5/30 in 31 min | short answers that need two concrete ways, or a design that covers every requirement (spikes, scaling back down, several countries) |
| Mock B | **PAPER WRITTEN 2 Nov, to be sat** (`Notes/mocks/MOCK-B.pdf`, key in `MOCK-B-key.md`) | |
| Mock C | FULL PAPER WRITTEN 3 Nov (`Notes/mocks/MOCK-C.pdf`, `MOCK-C-print-safe.pdf`, key `MOCK-C-key.md`): 25 real + 10 own gotchas, to be sat on exam day | |

**Mock plan (agreed 1 Nov):** Mock B finds weaknesses on the essentials; Mock C is the final gotcha round, aimed at what Mocks A and B showed. Mock C runs on the exam morning (the exam is that evening).
- **Goal: Joshua sees all 75 real past-paper questions exactly once across Mocks A, B and C.** Mock A + Mock B must cover the essentials on their own, so skipping Mock C loses only extra practice.
- **Format:** the real exam's mix (about 4 MCQ to 1 short answer), shuffled across all lectures, timed at the exam pace of about 3.6 min per question. The mocks are longer than 25 questions so that every real question fits.
- **Unused real questions: 51.** These are the 30 L01-L05 ones listed in `Notes/MOCK-log.md`; L06's 13 (24S2 Q18, Q19; 25S1 Q2-5, Q13, Q19; 25S2 Q2, Q7, Q12, Q15, Q25); L09's 2 (25S2 Q13, Q14); L10's 5 (24S2 Q17, Q21; 25S1 Q21, Q24; 25S2 Q8); and 25S1 Q16, which is not mapped to any lecture. **Do not use the L09/L10 ones as scenarios:** write your own scenarios so these stay unseen.

| Mock | Real | Claude's own | Total | Time |
|---|---|---|---|---|
| A (done 31 Oct) | 24 | 1 | 25 | 90 min |
| B (Mon 2 Nov, after L10) | 26: every unused H-priority question in `PAST-PAPER-MAP.md` first, then M | 4: L07 (no past paper covers it) and Mock A's weak spots, as new questions on the same ideas | 30 | ~110 min |
| C (Tue 3 Nov, morning) | 25: all the rest | 10 harder gotchas on the weak spots of Mocks A and B | 35 | ~125 min |

- Mock A's weak spots: trust-boundary direction, VM vs container, elastic vs horizontal, hypervisor isolation, data across several countries, designs that scale back down.
- **After Mock B:** review it and fill the gaps the same evening. The gaps these questions test were deliberately kept out of the INDEX so the mocks stay clean. **Mock C was written in full on 3 Nov at Joshua's request (25 real + 10 own gotchas) as one printable paper; he sat Mock B on 2 Nov (27/36) but had not yet done the gap set.** After Mock C, fold any gap into its INDEX row before the exam.

**All lectures are done and in the INDEX** (L10 added 1 Nov: section with tables 1, 2, 5 and rows 3, 4, 6, 7; Joshua had worked calculations and the cost-per-unit-of-work row removed as self-explanatory (he wants as little arithmetic on the page as possible); See-also links from L01-4, L02-2, L05-12, L07-8; concept map now L01-L10 with a Cost layer; Exam Tactics row 11 "What will it cost?"). Also 1 Nov: L04 rows "datacenter areas" and "datacenter networks" were cut (pure names, never tested in 75 past-paper questions); L04 is now rows 1-9 + table 10. A second clipping pass (1 Nov, 19 fixes) covered the Exam Tactics "Pick by" column and table cells the first pass missed; clarity beats brevity everywhere, including table cells. Exam Tactics table is now Ask | Cues | Pick by, with one "cue → pick" rule per line (`<br>` in the cell; `build.py` allows `<br>` in table cells and gives the table its own column widths in `print.css`); it must stay on one page. Joshua's rule for cutting: keep anything that helps an exam answer, illustrates a concept, links it to reality or makes it clearer. The PDF is 18 pages.

**INDEX format pass: DONE 1 Nov.** L03 renumbered (old rows 6 and 12 merged into tables): table 4 = workload distribution vs service load balancing, table 8 = dynamic scalability vs elastic resource capacity, row 10 = listener (now also holds the anti-oscillation thresholds), row 11 = cloud bursting; all links updated. L07-7 and L09-5 are now tables (L09-5 has a same-numbered follow-on row). L05-8, L06-6 and L07-5 are written as `A → B → C` step chains. A readability pass (also 1 Nov) rewrote 13 tangled or clipped sentences as plain full sentences; Joshua's rule: never shorten into clipped, AI-summary style. The PDF now starts each lecture and Exam Tactics on a new page, with spacing tightened slightly in `print.css` so no lecture spills a few lines onto an extra page (16 pages). L02's pointer-only row 14 (trust boundary, "as in L01-9") was removed and rows 15-18 became 14-17.

**Settled decisions (do not reopen):**
- **L02 slide 19:** the IaaS provider manages the OS. The INDEX says this plainly with no NIST warning; the L02 notes keep the NIST comparison for reference.
- **Elasticity** is "usually automatic", per the slides.
- **FaaS** is a serverless variant close to PaaS, not a fourth service model.
- **Multitenancy** shares one app instance; VMs and containers share a machine.
- **Asynchronous offloading** is not on any slide; its source is the 25S2 Q25 answer key.
- **Joshua's handwritten annotations already found wrong:** "LAMP stack - packaged dev env" (L06 P1 s22). All L07 annotations are correct. L09: s15 "CDK imperative" half right (CDK generates declarative CloudFormation); s35 "drift e.g. Git merge conflicts" wrong example (drift = live system differs from code). L10: s25 "Case B lowest cost" not shown by the slides (pies are shares); s26 "obsolescence" half the reason; s19 intra-cloud free "because necessary" a guess. Slide s26 has two pie labels that do not match their slices.
- **Stars:** keep the current ones; add new ones per lecture under the star rule.

---

## Files

All files are in `/Users/joshualum/Documents/VSCode/CS5224 Exam Prep/`.

| File | Purpose |
|------|---------|
| `Notes/INDEX.md` | Quick reference: concept map, one key-concept section per lecture, Exam Tactics at the end. Joshua revises it on exam morning and uses it during the open-book exam |
| `Notes/INDEX.pdf` | Printable copy. **After every INDEX edit, run `python3 Notes/print/build.py`**. It stops with an error on unsupported Markdown (only headings, pipe tables, `- ` bullets, bold, italic and `code` are allowed). Layout lives in `Notes/print/print.css` |
| `Notes/LNN-<name>.md` | Detailed notes per lecture. `L01-Principles.md` is the model to copy |
| `Notes/LNN-log.md` | Every scenario: the question, Joshua's answer in his own words, the grade and the correct answer. Do not read these at session start. `L01-log.md` is the model |
| `Notes/MOCK-log.md` | Mock results and the unused past-paper questions |
| `Notes/PAST-PAPER-MAP.md` | All 75 past-paper questions mapped to lectures (verified; the "Also" column shows questions that mix lectures) |
| `Notes/cards/LNN-cards.md` | Concept cards per lecture: the source for writing scenarios |
| `CS5224-ALL-COMBINED.pdf` | All lectures + past papers merged (Joshua's search tool in the exam) |
| `Lecture NN - *.pdf` | Lecture slides. They contain Joshua's own handwritten annotations |
| `2425-Sem2-...`, `2526-Sem1-...`, `2526-Sem2-Test-Questions-and-Answers.pdf` | Past papers. Used for mocks (Joshua decided 31 Oct) and as the style reference for scenarios |

Extract PDF text with `pdftotext "filename.pdf" -`.

---

## Sources and Ground Truth

- **The lecture slides are ground truth.** Never justify a claim with "the textbook says". An official definition (e.g. NIST SP 800-145) is used only where the slides are silent or too thin to answer a question. Then say so, grade on the official definition, and put the clarification in the lecture notes and the matching INDEX row. If a source conflicts with the slides, keep the slide wording, and note the conflict in the lecture notes, not in the INDEX.
- **Joshua's handwritten annotations on the slides are not slide content.** Check each one against standard knowledge, tell him plainly when one is wrong, and never copy one into the notes as if it were slide text.
- **Name the source of every claim you state or change:** slide N, a standard definition, or "my reasoning".

---

## How to Teach

### Before each lecture
1. Make the cards. Run DeepSeek for slide text and Haiku for low-text diagram slides (as images), then script-check coverage and spot-check against the slides. For a small deck, Claude may read the slides directly instead (as for L07).
2. Read the matching rows of `PAST-PAPER-MAP.md`.
3. Build a numbered Scenario Plan, put it at the top of the lecture notes file, and show it to Joshua.
4. Start Scenario 1.

### Scenarios
- **Present each scenario cleanly:** no hints, no naming the concept, no links to slides or past papers in the question. Wait for his answer before explaining anything.
- **Test application, not recall** (the exam is open book). A scenario must not be answerable by restating the slides. Use these types: diagnose a symptom, what-if, choose between options with reasons, give two ways, spot the false statement, and look-alike MCQs with five options (the past-paper style). Recall-only items (definitions, lists, the parts of a component, names in order) go in the notes as "reference only (not tested)".
- **Format:** at most two short questions per scenario. Vary the format: mix MCQ and open questions, use multi-part questions on one scenario when it helps, and avoid a fixed rotation. Put an open question before an MCQ when the options would give the answer away.
- **Match past-paper difficulty** (current scenarios are at or slightly above it). Use look-alike concepts as the wrong options.
- **Stay within the lecture's slides;** mixing lectures is for the mocks. Merge scenarios on the same idea or architecture. Test key concepts, not specific slide terms. Where a key concept's slide wording is unclear, put the clarification in the notes instead of testing it. Mark reasoning that goes beyond the slides as (beyond slides) in the notes.
- **Gap set:** one mixed set of 4-5 short questions per lecture, only on concepts he actually got wrong.
- Say how many scenarios remain, but **never cut coverage for time** or propose trimming scenarios or lectures.

### Grading and review
- **Grade strictly.** If he scores 40%, say 40%. State what was right, what was wrong and the full correct answer. Link to the slide concept only in the review.
- **Explain fixes as a mechanism, step by step** (what happens, in what order), not as a one-line label such as "chain by events" or "use an external store".
- Plain, concrete words: expand any term he might not know. He pushes back on vague wording and unexplained jargon.

### After each scenario
1. Append an entry to `LNN-log.md`.
2. Update the lecture notes file (full rewrite, see below).

### Coverage
Before marking a lecture done, check every concept against the slides or cards, not intuition. Name the concepts left untested.

---

## Notes Format

### Lecture notes file (`LNN-<name>.md`)
- Order: Scenario Plan, Detailed Notes (one section per concept), Reference only, Not yet tested.
- Tag claims **(slides, sN)** or **(beyond slides)**. Never present beyond-slide claims as slide content.
- **Always a full rewrite:** read the file, modify it in memory, write it back whole. Incremental edits caused duplication.
- Each concept ends with a one-line "Key one-liner".
- **WARNING box** (`> [!WARNING]`): only for a mistake Joshua actually made that is non-obvious. Format: `**Mistake:** <wrong idea>. <right idea>.` It must be readable months later with no memory of the session. Be selective; existing boxes stay.
- **CAUTION box** (`> [!CAUTION]`, "Exam Trap (MCQ)"): high-severity past-paper MCQ distractors.

### INDEX.md
**Purpose:** key concepts and Joshua's misconceptions, each with enough detail to make sense alone. Plain fact recall stays in the slides, which are searchable, except facts found only inside slide diagrams. There is no page limit, but slide text is never copied without added value. Keep it lean: fold fixes into existing rows rather than adding new ones.

**Structure:**
- Concept map "How the pieces fit together" at the top: one intro sentence plus a Layer | Question | Building blocks | Lecture table. It names building blocks only and points to rows (e.g. L05-13) instead of repeating them.
- One section per lecture, with 3-4 `####` group headings, in lecture order.
- Inside a lecture, rows and comparison tables share one number sequence. "See also L03-10" means lecture 3, row or table 10. After any renumbering, update every link. L01 row 5 and table 5 share a number on purpose.
- **Exam Tactics** at the very end: the only place for exam advice. It holds the design-question checklist (ordered "Ask | Cues | Options | Pick by" rows, one per requirement type the course has a tool for).
- No coverage tracker, no theme map (the See-also links do that job).

**Rows:**
- Label style: `**Label:**`, or `**Label ★:**` for a starred row.
- Full, self-contained sentences that make sense in two months with no context. Clarity over brevity: no clipped, semicolon-heavy text.
- **One row = one storyline.** Split a row only when it is long and its second idea makes sense on its own. Ideas meant to be compared stay together, and short rows are never split.
- **Bold sparingly:** key terms, and in a long row the key outcome where it happens (e.g. "so **no job is lost**"). Too much bold loses its value.
- A fix must make a concept clearer, not only more precise. Drop nuance that adds clutter or breaks a row's self-containedness.
- No source tags, slide numbers, past-paper citations, Q&A, "what I get wrong" statements, names-only lists, exam-tactic advice or meta-comments about the slides. A slide-wording note stays only when the slides use a term in a second meaning an exam could test (e.g. "availability" = how fast resources are ready), stated as content.
- Beyond-slide detail only if it is objective and publicly verifiable (NIST, AWS docs and the like).
- A row that continues a concept from another lecture says only what it adds and ends with "See also LNN-N".
- Do not restructure the INDEX unless asked; fix specific rows only.

**Comparison tables:** each look-alike set gets a small side-by-side table that **replaces** the prose rows it covers. Its value is in the "Cost / Pick it when / Think of it as" rows. Overlap with a slide's own table is fine.

**Examples and analogies:** add one only to an abstract row. It must be everyday (Gmail, a shared house, a restaurant) and make the mechanism click; no trivia (Joshua rejected "Google's PUE is about 1.1"). Skip it if it is weaker than the plain sentence. Reuse the shared pictures and give each picture one meaning: trucks = scaling, hotel = multitenancy, recipe = image, houses on one plot = virtualisation.

**Star rule:** a ★ only for a real misconception (a wrong mental model, or the same mistake made twice). No star for slips, omissions, things he did not mention, or a look-alike mix-up made once. The legend at the top of the Quick Reference says this.

---

## Workflow and Tools

- Workers and subagents only read and extract. Never delegate grading, writing scenarios, explaining concepts or writing notes. Do INDEX passes yourself.
- Card jobs: `WORKER_ALLOW_NO_GIT=1 worker deepseek <brief> 15` (read-only; brief in the session scratchpad). The project is not a git repo, so **Joshua must approve this override for each job.** Run one worker at a time (parallel runs hit "database is locked"). The report is at the end of the `.out` file, after a long transcript (grep for `^# `).
- Before showing Joshua any review result, check every finding against the slide it cites.

---

## Joshua's Preferences

- Honest, strict grading; no encouragement for wrong answers.
- Short, scannable output. Show him the list of changes before making them.
- He wants conceptual answers, not reasoning built from one exam question.
- When he gives meta-feedback on how the session is run, adjust. When he disagrees, answer his actual question before changing files.

---

## Mock papers (written 2 Nov)

- Files in `Notes/mocks/`: `mock_data.py` (question bank and the B/C question order), `build_mocks.py` (run `python3 Notes/mocks/build_mocks.py` to rebuild the PDFs and keys; it asserts every one of the 51 real questions appears exactly once across B and C), `MOCK-B.pdf`, `MOCK-C-part1.pdf` (print versions, no hints, MCQ answer grid with a "guessed" box), and `MOCK-B-key.md`, `MOCK-C-part1-key.md` (answers, source map, marking notes). **Do not show the keys before he sits the paper.**
- **Mock B:** 24 MCQ + 6 short answers = 36 marks, 110 min. 26 real (21 MCQ + 5 SA) + 4 own: OWN-B1 (k-means mapper output), OWN-B2 (video app: separate encoders + queue), OWN-B3 (hypervisor isolation), OWN-B4 (ticket-sale spike, must scale back down).
- **Mock C (full):** 26 MCQ + 9 short answers = 44 marks, 125 min. 25 real (19 MCQ + 6 SA) + 10 own gotchas: L09 x4 (OWN-C1 state vs configuration, C2 separate state per environment, C3 who detects a crashed server, C4 apply reverting a hand change), L07 x3 (C5 log2 ratio arithmetic, C6 why log helps, C7 why the upload server does not wait for encoding), other repeat slips x3 (C8 manual horizontal vs elastic, C9 trust-boundary direction, C10 residency across countries plus scaling back down). Print files: `MOCK-C.pdf` and `MOCK-C-print-safe.pdf` (image copy for his printer, which gave a PostScript rangecheck error on the first PDFs).
- Split rule used: 29 unused real questions were high-confidence, 3 more than fit in B. 24S2 Q3 (PaaS dev environment; duplicates 25S1 Q13 and Q15) went to C, and so did two short answers on the same idea as another B question (24S2 Q21, repeat of 25S1 Q24 pricing; 24S2 Q25, repeat of the hybrid questions). All 11 unused real short answers: B takes 5, C takes 6.
- Joshua's one correction to wording: none yet. Past-paper wording was kept except obvious typos.
