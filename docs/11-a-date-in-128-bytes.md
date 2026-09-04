# 11 — a date in a hundred and twenty-eight bytes: a fourth point for a question the third disc left open

*Measure: one 32-bit field in `/rom_tags`, read on four discs, against a
question the platform notes asked and could not close with three.*

## Read the neighbours first, and this session did not

**The 3DO platform notes already have this field.** The third disc derived it,
published all three values, proposed the 1904 epoch, and marked it
`[1 of 1]` — *"derived once and only observed three times"* — with an open
question at the end of the document:

> **8. NEW: is the `0x0c` `rom_tags` record a pressing date?** Three values,
> monotone in press order, all three landing in 1993–1995 under a 1 January
> 1904 epoch and nowhere possible under any other, with the first **twenty-five
> days before its disc's documented release**. **A fourth disc with a known
> pressing date settles it** — and if it does, this platform has a build-date
> series it was thought not to have.

This session found the field independently, re-derived the epoch by a different
route, wrote a tool for it, and only then read the notes. **That is the second
time in one session that a thing presented as new was already published next
door** — the first is the volume label in
[03](03-the-file-system-a-fourth-time.md) — and both are in
[15](15-corrections.md). The session brief's rule 6 says to take a figure from
another repository's `docs\` rather than from your head; **the failure here was
worse, because it was not a figure but a whole finding.**

What follows is therefore **not a discovery**. It is a fourth point on a
three-point series, a second and independent argument for the epoch, and a tool
that makes both reproducible. That is what the notes asked a fourth disc for.

## The sentence three sessions have written, and it is still true

> The Opera file system stores no dates at all — no volume creation timestamp,
> no per-file mtime.

True, and re-derived here. **It is not the same sentence as "this disc carries
no date"**, and the second is what this session's own briefing concluded from
it:

> The only clocks in the object are the two SDK build stamps, and they date
> **the toolchain**, not the game.

There is a third clock, it is 32 bits wide, and it is in the second sector of
every one of these discs.

## The field

`/rom_tags` is 128 bytes at block 1 — four 32-byte records
([05](05-the-boot-chain.md)). One of them, type `0x0c`, carries a single
non-zero number and nothing else:

```
  2  type 0x0c  sub 0x0000   A 2859874196 (0xaa763794)   B 0
```

Read on all four 3DO discs in this collection, the same record gives four
numbers, and **they rise monotonically**:

```
Crash 'n Burn     0xa8b496ae   2,830,407,342
Slayer            0xaa763794   2,859,874,196
SSF2T             0xab382bd6   2,872,585,174
Wolfenstein 3D    0xac737cff   2,893,249,791
```

Four values, four discs, in an order — and the gaps between them are 341, 147
and 239 days if the unit is a second. That much is arithmetic. The epoch is the
part that has to be argued.

## Choosing the epoch, twice, by two different routes

**The platform notes' argument is the better one and it is theirs**: the 1904
epoch is *"the epoch this platform already uses for the 80-bit extended floats
in every `COMM` chunk on every one of these discs"*. That is an internal
argument from a second, unrelated use of the same epoch in the same objects,
and this session did not think of it.

The argument below was made before that one was read. It is kept because it is
independent and because it is mechanised, not because it is better. Two
constraints, both internal to the four objects:

1. **the disc's date must fall after that disc's own SDK build stamp** — an
   independent clock, printed in plain text by a different tool into a
   different file (`/System/Folios/operamath`, `/System/Scripts/STARTOPERA`);
2. **the gap must be under five years**, because a studio does not ship on a
   toolchain build it took half a decade to use.

```
python tools/romtags.py --epochs
```

| epoch | after its own SDK stamp | and within five years |
|---|---|---|
| 1900-01-01 | **0 of 4** | 0 of 4 |
| **1904-01-01 (Macintosh)** | **4 of 4** | **4 of 4** |
| 1970-01-01 (Unix) | 4 of 4 | **0 of 4** |
| 1980-01-01 | 4 of 4 | **0 of 4** |

**The first constraint alone settles nothing**, and saying so is the point:
1904, 1970 and 1980 all pass it. It is the second that separates them. Unix
time puts every pressing in the **2060s** and 1980 in the **2070s**, sixty-six
and seventy-six years after the toolchain that built them; 1900 puts Crash 'n
Burn four years *before* its own SDK.

**Only 1904 passes both, on four of four.**

## The result

| disc | `0x0c` | pressed | its own SDK stamp | gap |
|---|---|---|---|---|
| Crash 'n Burn | `a8b496ae` | **1993-09-09 08:15:42** | `operamath` 1993-08-14 | 26 days |
| **Slayer** | `aa763794` | **1994-08-16 09:29:56** | `operamath` 1994-05-10 | 98 days |
| Super Street Fighter II Turbo | `ab382bd6` | **1995-01-10 12:19:34** | `operamath` 1994-05-10 | 245 days |
| Wolfenstein 3D | `ac737cff` | **1995-09-06 16:29:51** | `startopera` 1994-08-06 | 396 days |

Four discs, four dates, four gaps between twenty-six days and thirteen months,
every one of them positive and every one of them plausible for a title going
from a frozen SDK to a pressing plant. **Nothing in that table was assumed:
every left-hand value is four bytes off a disc and every right-hand value is a
string in a different file on the same disc.**

## Why the Macintosh epoch is not a surprise, and why that is not the argument

This disc says "Macintosh" four separate ways, and every one of them is cheap:

- **`/AppStartup` uses `\r` line endings** and nothing else
  ([05](05-the-boot-chain.md));
- **the four one-byte `junk` files each contain `0x0d`**, a carriage return
  ([03](03-the-file-system-a-fourth-time.md));
- **three sound files are at 22,255 Hz**, the Macintosh 22.254545 kHz rate
  rounded, where the other fifty-nine are at a clean 22,050
  ([09](09-a-soundtrack-uncompressed.md));
- and now **a date counted from 1904-01-01**.

**Three of those four are 3DO's and not this studio's.** `/AppStartup`, the
`junk` files and `/rom_tags` all live in the platform's half of the disc and
are byte-identical or structurally identical with the twin's. Only the 22,255 Hz
sound files belong to the studio. **The control matters**: the Mac-hosted
toolchain is the console vendor's, and the one trace that is the studio's own
is the one [09](09-a-soundtrack-uncompressed.md) leans on.

The epoch argument above does not rest on any of it. It rests on the two
constraints and the four SDK stamps. **The Macintosh evidence is the reason the
answer is unsurprising, not the reason it is believed** — which is the right way
round, and the wrong way round is how four sessions of this collection have
been getting the packer question wrong.

## What this changes

**It answers open question 8 as far as four points can.** The notes asked for a
fourth disc *with a known pressing date*; this is a fourth disc **without**
one, so the outside check is still a single point — Crash 'n Burn's, twenty-five
days before its documented release. What the fourth value adds is a fourth
monotone point, a fourth positive gap against a fourth independent SDK stamp,
and the mechanised epoch test. **The question narrows and does not close**, and
it is written into the notes that way.

**The collection's own chronology was wrong.** Every document in these four
repositories that ordered the discs did it by copyright line, SDK stamp or
release year, and on that basis Super Street Fighter II Turbo — same SDK build
as Slayer, to the second — sat beside it or before it. It was pressed **147
days after**. The thesis table in [01](01-one-pressing.md) and
[09](09-a-soundtrack-uncompressed.md) now carries pressing dates instead of
years, and Slayer comes second of four rather than joint-second.

**And it gives [08](08-the-sixty-eight-bytes.md) a direction.** The one file in
116 that differs between the two twins is a serial driver, and Slayer's copy is
the one with a `kprintf` left in it. Slayer's copy is also the **earlier**
one — by 147 days, on a clock neither disc's authors controlled. That is one
data point and it is consistent with the trace having been removed rather than
added.

## What is not claimed

- **that `0x0c` is a mastering date rather than a build date.** It is later
  than the SDK stamp on four of four and that is all the ordering the objects
  support. Whether the number is written when the image is built or when the
  glass master is cut is not visible from here;
- **the time zone.** The value is treated as seconds and printed without
  offset. The SDK stamps say `PDT`; this one says nothing;
- **that the field means the same thing on discs outside this collection.**
  Four is four;
- **anything about types `0x05`, `0x07`, `0x0d` or `0x10`.** `romtags.py`
  prints their fields and names none of them.

## The tool

`romtags.py` was written here. `--validate` runs five negative controls and one
positive:

```
ok  : an empty file                        refused -- 0 bytes is not a whole number of 32-byte records
ok  : 33 bytes                             refused -- 33 bytes is not a whole number of 32-byte records
ok  : a record not beginning 0x0f          refused -- record 0 begins 0x01, not 0x0f
ok  : an AIFF header                       refused -- record 0 begins 0x46, not 0x0f
ok  : 2,048 bytes of iamaduck              refused -- record 0 begins 0x69, not 0x0f
ok  : positive control (one 0x02 record)   accepted, type 0x02 A=74291 B=147
```

`--app` checks the `0x02` record against an `opera.py --list` listing and
**fails loudly** when no file in the listing begins at that block with that
length — which it did, on the first run, because the listing's type column
contains spaces and the parser was too strict. A refusal that is really a
parser bug is the failure mode this whole pipeline exists to catch, and it took
one run to catch it.
