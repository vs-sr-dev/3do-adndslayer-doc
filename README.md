# 3do-adndslayer-doc

**Advanced Dungeons & Dragons — Slayer**, 3DO Interactive Multiplayer, USA.
One pressed CD-ROM, documented from a CHD without running or emulating
anything on it.

A dungeon crawler that spends **two thirds of its disc on a soundtrack it did
not compress**, whose operating system is **byte-identical with the disc next
door on 115 files of 116**, and which **names nobody in any string** — but says
who made it, four times, in pixels.

| | |
|---|---|
| **container** | one CHD v5, 200,769,302 B, SHA-1 `126b1dcc03007b1482cd9583edb2c2754cb5effa` |
| **pressing** | one `MODE1_RAW` track, 151,340 sectors, **45.4474 %** of a 74-minute CD |
| **audio tracks** | **zero** — the first of four 3DO discs here with none |
| **pressed** | **1994-08-16 09:29:56**, from the disc's own `/rom_tags` |
| **file system** | Opera, not ISO 9660. **582 files, 24 directories, 272,214,595 B** |
| **hashes** | **573 distinct of 582**, seven duplicate groups |
| **mastering fill** | `iamaduck`, 17,729 sectors = **11.7147 %**, in two regions |
| **unowned sectors** | **0**; double-claimed **0**; 300 zero sectors past the declared volume |
| **the thesis** | **67.4093 % of the user area is recorded sound** — 81 AIFF files, **codec `NONE` on 81 of 81**, **22:30.04** |
| **identified** | **87.6184 %** of the user area, the highest in the collection — and the least impressive, because the object did the work |
| **the game itself** | one 299 KB ARM binary, 370 cel containers, 2,516 frames, a font: **under 4 %** |

## Five things this disc turned out to be

1. **It has a twin, and the twin is 68 bytes away.** Its `/System` and Super
   Street Fighter II Turbo's are **115 identical files of 116**. The one
   difference is a serial-port driver, and the difference is **a `kprintf` call
   and its format string** — five ARM instructions and 44 bytes of
   `"Stamped event pod %d position %d generic %d"`.
   [08](docs/08-the-sixty-eight-bytes.md)

2. **The container nobody had walked, walks.** `ANIM` / `CCB `: **370 files
   closing at residue zero, 370 of 370**, 3,782 chunks, **one `PDAT` per frame**
   and **2,516 of 2,516 frames rendered**. The reader for the chunk rule had
   existed for two discs and had never been aimed here.
   [06](docs/06-the-container.md)

3. **The disc carries its own pressing date**, in a 32-bit field of
   `/rom_tags`, and it reorders the collection: Slayer was pressed **147 days
   before** the disc it shares an SDK build with. **The platform notes had
   already found this and asked a fourth disc for exactly this point** — which
   this session did not read until after it had re-derived it.
   [11](docs/11-a-date-in-128-bytes.md)

4. **Two hundred and nine megabytes of uncompressed music**, when the platform's
   own 2:1 codec was on the same disc and the twin used it. SDX2 would have
   freed **102,379,300 bytes**. The disc was 45 % full, so it cost nothing —
   and the object still supplies evidence about *why*.
   [09](docs/09-a-soundtrack-uncompressed.md)

5. **The credit roll is 17 still screens, 20 people, and this repository
   publishes none of their names.** The clause that permits it was written on
   the previous object and this is the first time it has been *applied*; the
   argument for declining anyway is about volume, which the clause does not
   cover. [10](docs/10-three-films-and-a-credit-roll.md)

## The chapters

| | |
|---|---|
| [00](docs/00-predictions.md) | predictions, written before anything was opened — 36 clauses, two columns |
| [01](docs/01-one-pressing.md) | what it is, on which denominator, and what it keeps and throws away |
| [02](docs/02-the-sheet.md) | the sheet: every figure with the command that remakes it |
| [03](docs/03-the-file-system-a-fourth-time.md) | Opera a fourth time, and a label with two lengths that are both right |
| [04](docs/04-every-sector.md) | all 151,340 sectors, and 2,928 zero sectors of which only 300 are empty |
| [05](docs/05-the-boot-chain.md) | the console does not read the filename, and that is why nobody noticed it was wrong |
| [06](docs/06-the-container.md) | the `ANIM` container: 370 files close, 2,516 frames render |
| [07](docs/07-forty-one-binaries.md) | 41 ARM images, and the two that break the rule are the game's |
| [08](docs/08-the-sixty-eight-bytes.md) | the smallest useful diff this collection has: one debug print |
| [09](docs/09-a-soundtrack-uncompressed.md) | the thesis, the SDX2 arithmetic, and 43 creatures with 36 voices |
| [10](docs/10-three-films-and-a-credit-roll.md) | three films, a credit roll counted not transcribed, and the decision |
| [11](docs/11-a-date-in-128-bytes.md) | a pressing date in 32 bits, and a question the third disc left open |
| [12](docs/12-against-the-collection.md) | 114 crossings of 573, all of them 3DO, and the twin |
| [13](docs/13-the-platform-notes.md) | what was written into the platform checklist, and what it already knew |
| [14](docs/14-what-is-not-here.md) | the refusals, the negative controls, and two tools that cannot say no |
| [15](docs/15-corrections.md) | every wrong figure, left visible: the brief's, the pre-briefing's, this session's |
| [16](docs/16-prediction-scoring.md) | 18.45 of 30 open against 19.50 predicted |

## `notes/`

The measured listings, so every table above can be checked without the disc:
`listing.txt` (582 entries), `sha1-all.txt` (582 records), `sectors.txt`,
`chd.txt`, `label.txt`, `containers.txt`, `frames.txt`, `romtags.txt`,
`aif.txt`, `reuse.txt`, `account.txt`, `crossall.txt`, `sdkdiff-ssf2t.txt`,
and **`owner-observations.txt`** — what the person who owns the disc reported,
attributed, including the one check that ran from bytes to a person and back.

## `tools/`

446 Python files. **Three were written here** and one was rewritten:

- **`animwalk.py`** — walks the `ANIM` / `CCB ` container, censuses its chunks,
  and renders every `PDAT` as a frame. Seven negative controls, one positive;
- **`romtags.py`** — reads `/rom_tags`, checks the `0x02` record against a
  directory listing, and argues the epoch with a table instead of a claim;
- **`aiffreuse.py`** — finds re-used sound that a hash census cannot see: exact
  payloads, contained payloads, and same-length correlations, with an envelope
  ranking that is explicitly **not** a test;
- **`account3do.py`** — **rewritten** for this disc, third session running, and
  the two changes are named in its docstring: the AIFF bucket is labelled with
  the codec the container declares rather than with a neighbour's, and the cel
  container is walked rather than signature-scanned.

**Nothing else was modified.** Twelve inherited tool defects are reported in
[15](docs/15-corrections.md) and none is fixed, because fixing an inherited tool
silently is worse than reporting it.

## What is not in this repository

**No byte of the product**, in any form it takes: no audio, no cel, no film, no
frame decoded into another format, and no name from the credit roll. The
`.chd`, `_work/` and `prompt.txt` are in `.gitignore`, verified in both
directions with `git add -An` and `git ls-files`.
