# 15 — corrections: the brief's, the pre-briefing's, and this session's

*Measure: every figure and claim that turned out wrong, with the wrong version
left visible beside the right one and the command that settles it.*

## The brief's, and the first one is the largest number in the repository

**B.1 — the thesis figure was on the wrong denominator.** The brief said:

> il tuo è 76,7607 % ma di roba non compressa

and asked for it to go in the column beside the neighbours' 0.3230 %,
86.2465 % and 59.7896 %. **Those three are shares of the user area; 76.7607 %
is a share of the bytes in files.** The comparable figure is **67.4093 %**.

```
python tools/thesis3do.py _work/files 151340 151040
  user data in track x2048   file bytes 67.4166 %   SSND 67.4093 %
```

Nine and a third percentage points, and it is rule 3 of the brief — *every
figure names its denominator* — failing inside the brief. [01](01-one-pressing.md),
[09](09-a-soundtrack-uncompressed.md).

**B.2 — `HLion.anim` does not exist.** The brief and the pre-briefing both
quote it, from a string scan of `/LaunchMe`. The file on the disc is
`/data/Lion.anim`, and the binary agrees:

```
offset 114407  ...\x00\x03\xaa  H  L i o n . a n i m \x00\x00\x00\x00
114408 mod 4 == 0     114407 mod 4 == 3
```

**The string begins at the word-aligned address and the `H` is the last byte of
the preceding literal-pool word `0x0003aa48`.** An unaligned scan read one byte
of a constant as the first letter of a filename. It is the brief's own
second lesson — *a short marker is a claim about a position, not about a file* —
in its cheapest form. [07](07-forty-one-binaries.md).

**B.3 — "everyone who made this game is inside a 24-megabyte movie" is half
wrong.** No string on the disc names the studio, the publisher, the licensor or
the year: that half is checkable and true. But **`/data/ADD.cel`, 12,736
bytes**, decodes in one command to a licence screen whose small print carries
the licensor, its town, the publisher and **©1994 twice**. The credit roll adds
the twenty people and nothing else corporate. **The expensive thing was never
necessary for the corporate answer.**
[10](10-three-films-and-a-credit-roll.md).

**B.4 — the container had a reader.** "*niente in 443 tool li cammina*" and
"*non è presente un lettore `ANIM`/`CCB `*". `ccbread.py` has walked exactly
this chunk rule since the first 3DO disc and its `census` subcommand **takes a
directory**. [06](06-the-container.md).

**B.5 — the label's two lengths were not an open question.** The brief presented
`132` against `128` as an unreconciled contradiction printed by one tool. The
third disc's repository scored the reconciliation at 1.0 fourteen months ago and
the platform notes carry it as `[2 of 2]`. [03](03-the-file-system-a-fourth-time.md).

## The pre-briefing's

**P.1 — the ten `pc-*` crossings do not exist.** `_pre/neighbours.txt` reported
`crossall.py` finding "*ten `pc-*` repositories, 1 each*". Re-run, the crossings
are **114 of 573, all three of them 3DO discs, and zero PC repositories**. What
the pre-briefing read was a *different list six lines above*: the twelve
repositories that contain a zero-length file, **exactly ten of which are
`pc-*`**. This disc has no zero-length file and cannot cross with them.
[12](12-against-the-collection.md).

**P.2 — there are 370 containers, not 360.** 219 cel-extension files plus 141
`.anim` is 360; ten more are cels **with no extension at all**, named
`3DO Cel`, `Alert Cel`, `Help Cel` and so on, 101,108 bytes.
[06](06-the-container.md).

**P.3 — `/rom_tags` holds six records and declares four.** The pre-briefing
quoted its first sixteen bytes and its 128-byte length. The **block** holds
192 bytes of records; types `0x10` and `0x05` sit past the declared end and are
invisible to `opera.py --extract`. The twin does the same.
[05](05-the-boot-chain.md).

**P.4 — the `/AppStartup` case mismatch is not a mismatch.** `_pre/formats.txt`
asked *"whether the Opera file system cares"*. **Every line of the file is a
comment**; the sentence naming `Launchme` is prose. And the console does not
compare filenames at all — `/rom_tags` record `0x02` addresses the boot binary
by block. [05](05-the-boot-chain.md).

**P.5 — "the only clocks in the object are the two SDK build stamps" is
false**, and the pre-briefing inherited that from three sessions of this
collection. The `0x0c` `rom_tags` record is a date.
[11](11-a-date-in-128-bytes.md).

**P.6 — one `FILM` chunk per stream is a header.** The pre-briefing counted
1,327 / 1,225 / 834 `FILM` chunks and called them video chunks. The films
declare and contain **1,326 / 1,224 / 833 frames**; the extra chunk is `FHDR`.
[10](10-three-films-and-a-credit-roll.md).

**P.7 — `celdecode.py`'s `PermissionError` was filed as defect nine and the
defect is real, but it was the wrong tool.** Guarding `open()` against a
directory is worth doing; it would not have opened the container.

## This session's, and the biggest one is a process failure

**S.1 — THE NEIGHBOURS WERE NOT READ FIRST, AND IT COST THREE FINDINGS.**

The platform notes already contained, before this disc was opened:

- **the 132-byte label**, its zero word at +128 and the fill starting at +132
  with `duck`, `[2 of 2]`;
- **the `/rom_tags` `0x0c` date**, all three values, the 1904 epoch, and a
  *better* argument for that epoch than this session's — *"the epoch this
  platform already uses for the 80-bit extended floats in every `COMM` chunk on
  every one of these discs"* — with an open question asking a fourth disc for
  exactly the point this disc supplies;
- **that the 1993 disc's `junk` byte is `0x0a` and the later discs' is `0x0d`**,
  which this session predicted wrongly as `0x0a` (C30) while measuring `0x0d`.

**Three results were available for the price of reading one file first**, and
this session wrote a tool and a chapter before reading it. Rule 6 of the brief
says to take a figure from another repository's `docs\` rather than from your
head; **what was not read here was not a figure but three findings.**
[11](11-a-date-in-128-bytes.md), [13](13-the-platform-notes.md).

**S.2 — the predictions header was wrong and the command caught it.**
`docs/00-predictions.md` was first written claiming 11 `inherited` and 25
`open` clauses totalling 8.80 and 15.90. `predcount.py` counted **6 and 30,
totalling 5.80 and 19.50**. Fourth session running in which the command caught a
hand-added total; the corrected header is in the document with the error named.

**S.3 — C16's arithmetic was right and its argument was wrong.** The clause
predicted that the 8-bit files would matter and that the 16-bit files would hold
more than 90 % of the audio bytes. They hold **97.9986 %**, which *destroys* the
point the clause was making: the effects were halved and the effects are two per
cent of the sound. The number scored and the conclusion did not.

**S.4 — C17 applied a 2:1 codec to 8-bit material.** SDX2 stores one byte per
16-bit sample; on 8-bit source it buys nothing. Predicted 104,476,906 bytes
freed; the answer is **102,379,300**, and the method error was worth 2,097,606
bytes.

**S.5 — C12 said the 68 bytes were one contiguous deleted run.** They are one
contiguous *inserted* run in the code, but the files share a **three-byte
common prefix and a zero-byte common suffix**, because the length lives at +4
and the last 64 bytes are a per-file signature. The clause was stated as a
byte-level identity and the byte-level identity is false.
[08](08-the-sixty-eight-bytes.md).

**S.6 — C25 was wrong in every particular.** It predicted the two
relocation-identity exceptions would be in `/System` and at least one
compressed. They are **`/LaunchMe` and `/data/StorageTuner`**, neither in
`/System`, neither compressed. [07](07-forty-one-binaries.md).

**S.7 — C29 said the root copies' placement is unexplained and half of it is
explained.** The first run begins at the block immediately after `/signatures`
ends; both `iamaduck` regions begin at the block immediately after a root-copy
run. Only the second run's offset resists.
[03](03-the-file-system-a-fourth-time.md), [04](04-every-sector.md).

**S.8 — C31's "39 distinct recordings" was the hash census's answer and it is
too high.** Two further exact tests bring it to **36**, and the owner's ear says
lower still. The clause matched the hash and the hash was not the measurement.
[09](09-a-soundtrack-uncompressed.md).

**S.9 — C21 predicted 320 × 240 and the films are 280 × 160.**

**S.10 — C36 predicted this session would produce platform-notes text and not
write it.** **The owner of that repository instructed otherwise mid-session**
and it was written and pushed. The prediction was about this session's conduct
and this session did the other thing; the clause is scored as wrong regardless
of whose decision it was.

**S.11 — `_work/` came in at 630,463,335 bytes** against a predicted 0.9–1.6 GB.
Second largest in the series, as predicted; outside the range, as not.

**S.12 — C19 was answered while it was being written.** The owner's report on
the music arrived during the drafting of §B, before the clause was scored and
after it was written. It is scored at half and the timing is recorded in
`notes/owner-observations.txt` rather than quietly ignored.

## Tool defects, and the list is now twelve

The nine inherited, unchanged and unfixed — fixing an inherited tool silently is
worse than reporting it, because the next session reads the list and not the
diff:

1. `bmp.py` never says how many files it opened
2. `pe.py` refuses a non-PE with a traceback
3. `wavcheck.py` lower-cases the filename but not `--ext`
4. `checkscore.py` skips bolded table rows in silence
5. `controltat.py` `IndexError` on any file shorter than 199 bytes
6. `mdmd.py` prints two verdict words, so `grep -c REFUSED` undercounts
7. `crossall.py` `--skip` defaults to empty; the docstring promises an
   automatic self-skip that does not happen
8. `crossall.py` `repositories swept` counts only repositories where a 40-hex
   token was found
9. `celdecode.py` `PermissionError` when given a directory

and three found here:

10. **`pcspk.py` has no refusal path.** It reports PC-speaker note tables inside
    an ARM binary. A tool that cannot return nothing cannot be a negative
    control.
11. **`cga.py` has no refusal path.** Same, for CGA frames.
12. **`iso9660.py` refuses correctly and exits 0.** A script counting refusals
    by exit status counts this as a pass.

And two behaviours that are not defects and are worth writing down because both
cost time:

- **`ccbread.py census` counts `CCB ` chunks, one per file on this disc**, and
  says so accurately. It is not a container census and was read as one;
- **`celdecode.py --all` decodes cels, not frames.** On a 198-frame animation it
  correctly reports *"1 of 1 cels decoded"*. The question it answers is not the
  question the filename suggests.

## What the pre-briefing got right, which is most of it

Every figure in §A of [00](00-predictions.md) reproduced: the CHD table, the
sector map to the sector, the 582 files and 573 hashes, the extension census,
22:30.04, the 41 ARM images and their 39-of-41, the three streams closing at
residue zero, the 115-of-116, the 114 crossings, and the seven duplicate groups.
**Six errors in a six-file pre-briefing that ran ten tools, and the six are
listed above.** The previous session's found six in twelve files.
