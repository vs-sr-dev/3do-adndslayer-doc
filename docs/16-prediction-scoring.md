# 16 — prediction scoring: 18.45 of 30 open, and the best calibration in five sessions

*Measure: every clause of [00](00-predictions.md) against what was measured,
with the two columns kept apart and the calibration series re-derived by
adding.*

## The totals

```
inherited   5.90 of  6    predicted 5.80    difference -0.10
open       18.45 of 30    predicted 19.50   difference +1.05
```

**The two are never added together.** `inherited` clauses re-test somebody
else's measurement; `open` clauses are this session's own bets, and mixing them
produces a number that means nothing.

**+1.05 on the open column is the smallest miss in five objects** and the third
smallest of the fourteen. The prescription in force — *do not apply a global
offset* — was followed, and the honest reading is that a session which spread
its bets across a container it could actually open, an arithmetic it could
actually do, and four `[4 of 4]` re-derivations landed near its own estimate.
**It is not evidence that the estimate was good; it is one point.**

## Inherited, 5.90 of 6

| | verdict | note | score |
|---|---|---|---|
| C01 | hit | `chdman` reproduces field for field; SHA-1 `126b1dcc…`, 200,769,302 B; extract 355,951,680 = 151,340 × 2,352 | 1.0 |
| C02 | half | `iso9660.py` refuses cleanly — `descriptors : 0` — but **exits 0**, so a refusal counted by exit status reads as a pass. Inherited defect twelve | 0.9 |
| C03 | hit | sector map reproduces exactly: 0 in `other`, 0 double-claimed, duck 17,729 | 1.0 |
| C10 | hit | width/height two encodings agree 370 of 370; every `CCB ` chunk 80 bytes | 1.0 |
| C15 | hit | 81 files, 22:30.04, codec `NONE` 81 of 81, 63 correct refusals on `.dsp` | 1.0 |
| C24 | hit | 41 images, five identities at 41 of 41, relocation target 39 of 41 | 1.0 |

## Open, 18.45 of 30

| | verdict | note | score |
|---|---|---|---|
| C04 | miss | 132 is the directory entry and 128 is the record's own arithmetic, both correct; `last_root_copy` is **6**, not 7, so the predicted mechanism was wrong — and a neighbour had published the reconciliation | 0.25 |
| C05 | hit | `ccbread.py census` takes a directory and walks the container unmodified | 1.0 |
| C06 | hit | 219 of 219 cel-extension files close at residue zero | 1.0 |
| C07 | hit | 141 of 141 `.anim` files close; 370 of 370 counting the ten with no extension | 1.0 |
| C08 | half | the 0x30 form is the 0x20 form plus four words and the first six are common — right. "per-frame timing" — unproven, and the words look like an uninitialised bounding box | 0.5 |
| C09 | miss | the count field equals the **`PDAT`** count, not the `CCB ` count, and `0xc6` = 198 **is** the field on the file it was quoted from. Wrong twice | 0.0 |
| C11 | hit | `celdecode.py` decodes this disc's cels unmodified; the row arithmetic closes 38 of 38 on unpacked cels; no frame published | 1.0 |
| C12 | miss | the insertion is contiguous in the code, but the files share a **3-byte** common prefix and **0-byte** common suffix. The clause was a byte-level identity and the identity is false | 0.3 |
| C13 | half | not an AIF ✓; carries a tagged header with its own length ✓; contains a printable string ✓ — but a `printf` format, not a driver name | 0.7 |
| C14 | half | 48 of the 68 bytes are the format string and its padding, so "mostly data" holds; **20 of them are five real ARM instructions**, so "does not disassemble as plausible ARM" is false | 0.4 |
| C16 | half | the 16-bit files hold **97.9986 %**, above the predicted 90 % — and that number destroys the argument the clause was built for | 0.6 |
| C17 | half | 102,379,300 B freed, 49,990 sectors, 101,351 sectors = 30.4357 %, 62.7517 %. Predicted 104,476,906 / 51,014 / 100,326 / 30.13 % / 62.3 %. The method applied 2:1 to 8-bit material | 0.5 |
| C18 | half | the 22,255 Hz files are there and the argument is made; **one of its three legs fails as a control** — the twin shipped the same unedited `/AppStartup` and did compress | 0.7 |
| C19 | half | music, confirmed by the owner — **but his answer arrived while §B was being written.** Scored at half for that reason and not because it is doubtful | 0.5 |
| C20 | half | all three census cleanly and decode; the count is **3,383 frames**, not 3,386 — one `FILM` per film is the header | 0.7 |
| C21 | miss | **280 × 160**, not 320 × 240. Duration 102.00 s and rate 12 fps both inside the predicted ranges | 0.4 |
| C22 | hit | 20 distinct people, 25 credit lines, 13 roles, two companies, one year; shape published, no name, no frame | 1.0 |
| C23 | half | `SSI.anim` is the publisher's logo ✓ and `Lion.anim` frame 100 is the developer's ✓ — but the clause named `HLion.anim`, **which does not exist** | 0.7 |
| C25 | miss | both exceptions are **`/LaunchMe` and `/data/StorageTuner`**: outside `/System`, uncompressed, and the game's own. Wrong in every particular | 0.0 |
| C26 | half | no overlay, no second code file, no archive; the "separately launched" half is inferred from `/LaunchMe`'s strings and not proved | 0.7 |
| C27 | hit | every line of `/AppStartup` is a comment; zero executable lines; and the console addresses the boot binary by block, so no name is compared at all | 1.0 |
| C28 | hit | 151,040–151,339 inclusive, contiguous, exactly the sectors the label does not declare | 1.0 |
| C29 | miss | the first run begins at the block after `/signatures` ends, and both fill regions begin after a root-copy run. Only the second run resists | 0.4 |
| C30 | miss | there are **zero** `pc-*` crossings — the pre-briefing had read the empty-file list — and the `junk` byte is **`0x0d`**, which the platform notes already said | 0.0 |
| C31 | half | 43 growls and four byte-identical pairs ✓, and the "only duplicates" holds for hashes — but two further exact tests bring it to **36 recordings**, not 39 | 0.5 |
| C32 | half | `protscan.py` 0 of 11 over 582 with the positive control firing ✓; **five** of the seven MS-DOS readers refuse 582 of 582, and two have no refusal path at all | 0.7 |
| C33 | hit | 114 crossings of 573; 123 `*-doc`; `notes\` 84 → 85 | 1.0 |
| C34 | hit | four `[2 of 2]` marks broken, eleven `[4 of 4]` written, `/signatures` at 335,872 among them | 1.0 |
| C35 | half | the denominator was decided first and published ✓; identified is **87.6184 %**, **below** the predicted 90–97 % band | 0.5 |
| C36 | miss | seventeen documents ✓, no correction written into `pc-linksthechallengeofgolf-doc` ✓; but the platform notes **were** written and pushed, and `_work/` is 630,463,335 B against a predicted 0.9–1.6 GB | 0.4 |

## The label split, and the gap narrowed

```
method    7 clauses   5.60 of  7  =  80.0 %
content  29 clauses  18.75 of 29  =  64.7 %
```

**A 15.3-point gap, against 29.3 last session and a five-session run of the
effect at increasing size.** It is the smallest gap this series has recorded
since the effect was first noticed.

**That is not a success and it should not be read as one.** The gap narrowed
because 26 of the 30 open clauses were `content` — 86.7 %, which
`predcount.py` warned about at the time and this session declined to change —
so the `content` column is carrying almost the whole result and there is very
little `method` for it to be compared against. **Seven clauses is not a
population.** The prescription stays where it was: withdrawn at half, the
effect real, and the label measuring the difficulty of the assertion rather
than the quality of the intuition.

## The calibration series, re-derived by adding

```
+10.5  +7.5  +5.0  +2.0  -14.0  -2.0  +9.0  0.0  +19.75  +5.25  -4.10
-3.40  +9.30  **+1.05**
```

**Fourteen objects, sum 45.85, mean +3.2750**, amplitude 33.75, five negatives
of fourteen. The previous session's thirteen summed to 44.80 at +3.4462, and
the brief's own correction of the twelve before that — 35.50 at +2.9583 —
re-derives here too.

**No global offset is applied, for the fourth session running**, and this
object is the reason the prescription keeps looking right: the last four
differences are −4.10, −3.40, +9.30 and +1.05. A session that had corrected for
the two negatives would have been badly wrong on the third; a session that had
corrected for the third would have been wrong on this one.

## What was worth predicting and what was not

**The three clusters paid and one of them paid double.**

- **C05–C07, the container bet**, was priced at 2.4 of 3 and returned **3.0**.
  It was one bet — that the chunk rule the pre-briefing derived by hand is the
  rule `ccbread.py` already implements — and it was right, so all three landed
  together exactly as the risk was described;
- **C27, C28 and C33**, the cheap structural checks, returned 3.0 of 3;
- **C22 and C34** returned 2.0 of 2.

**The losses cluster too, and they have one shape.** C04, C09, C25, C29 and C30
are all clauses that **guessed a mechanism instead of naming a measurement**:
which two images, which slot the label counts, what the count field counts, why
the copies sit where they sit, which hash crosses. Every one of them could have
been written as *"the measurement will be X, taken by command Y"* and scored on
the measurement. **They are 1.05 of 5.**

**And the single largest avoidable loss is not in the table.** C04 and C30 were
both answered in a neighbouring repository before this session started, and C30
was answered *in the platform notes' own correction list*. Reading that file
first would have been worth about a point and a half, and would have changed
[11](11-a-date-in-128-bytes.md) from a discovery into what it actually is.
**That is the prescription this object generates:**

> **Before predicting anything about a platform with a running checklist, read
> the checklist.** Not the neighbour's figures — the neighbour's *findings*.
> Three of this session's results were already in one file, and one of them had
> an open question with this disc's name on it.
