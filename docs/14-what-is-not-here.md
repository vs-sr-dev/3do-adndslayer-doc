# 14 — what is not here: the refusals, the negative controls, and the two tools that cannot say no

*Measure: everything this repository declined to open, everything that opened
nothing, and the denominator each of those zeros is a zero of.*

## What was refused, and it is 0.2085 % of the pressing

`account3do.py` prints every file it could not name. Eighteen of them, 310,593
bytes, plus `/signatures` at 335,872 — **646,337 bytes, 0.2085 % of the user
area**, against 87.6184 % identified.

| file | bytes | why it is not here |
|---|---|---|
| `/data/MapSquares` | 104,324 | the dungeon's level data. No structure derived. |
| `/data/MatchData` | 87,078 | named by `/LaunchMe`, no format derived |
| `/System/Kernel/os_code` | 85,896 | 3DO's, and an ARM blob with no AIF header |
| `/data/EndMapSquares` | 7,684 | as `MapSquares` |
| `/System/Kernel/boot_code` | 5,050 | 3DO's |
| `/data/Sans Serif 14` | 4,528 | begins `FONT`; the format is not derived here |
| `/System/Kernel/misc_code` | 2,912 | 3DO's |
| `/data/MapSquaresAlt` | 2,564 | as `MapSquares` |
| `/data/slayer1.font` | 2,536 | begins `FONT` |
| six `/System/Drivers/*.ROM` | 7,180 | header and trailer derived, the ARM code inside not |
| `/System/Scripts/STARTOPERA` | 553 | readable text, and 3DO's |
| `/AppStartup` | 160 | readable text, quoted in full in [05](05-the-boot-chain.md) |
| `/rom_tags` | — | **removed from this list**: derived record by record |
| `/signatures` | 335,872 | size, block count and non-zero count measured; content not read |

**Two of those are readable text and are still counted as unidentified**, which
is deliberate. `/AppStartup` and `STARTOPERA` are quoted, line by line, in
[05](05-the-boot-chain.md); reading a file is not deriving a format, and the
neighbours' figures were computed under the same rule. Changing the rule to
flatter this disc would have made the 87.6184 % incomparable with 87.3403 %,
71.1132 % and ~77 %.

**The level data is the honest gap.** `MapSquares`, `MapSquaresAlt` and
`EndMapSquares` are 114,572 bytes and are the dungeon — the thing a player
walks through. Nothing in this repository opens them, no tool was written for
them, and no guess is offered. Their names come from `/LaunchMe`'s string
table, and **a name is not a format**.

## The forty-one ARM images, past their headers

707,536 bytes — **0.2283 % of the pressing** — of which the header is derived
and the code is not. The coverage rule counts an executable as unidentified
however much of it is read; this disc's executables are 0.23 % of it, so **the
coverage is not lost in the programs.** Yesterday's object was 86 % executable
and this one is a quarter of one per cent.

## The `CTPT` chunk

One occurrence in 3,782 chunks, 88 bytes, in `/data/monsters/Dracolich.anim`.
**One is not a sample.** It is walked, its length closes, and it is not named.

## The `ANIM` words nobody named

Words 3 and 6 to 9 of the `ANIM` chunk. `animwalk.py census --words` prints
their distributions; [06](06-the-container.md) prints the top three of each.
**Word 2 is described as an identity that holds 159 times of 180 and is not
given a name**, because a field that is the frame count on 159 files and
something else on 21 in one directory is a description.

## The pitch-shifted sounds, which is the measurement that failed

[09](09-a-soundtrack-uncompressed.md) confirms eight pairs of re-used
recordings by three exact tests. The owner of this machine reports more — that
`Gargoyle` is another growl pitched up, and that most of the bestiary is stock
library material.

**This session could not measure either**, and the negative is stated with its
numbers: an RMS-envelope ranking puts `Gargoyle` with `Margoyle` at 0.9325 and
`Cockatrice` with `Mind Flayer` at 1.0000, and their **sample-level
correlations are 0.018 and −0.001**; resampling `Ankheg` at every ratio from
0.50 to 2.00 against `Gargoyle` peaks at **0.0366**, no better than against an
unrelated file. **The right tool is a spectral comparison that was not
written**, and the stock-library question needs an external corpus this session
does not admit.

## The two tools that cannot refuse, which is a defect and an illustration

The seven MS-DOS readers written for the previous object were pointed at this
one as free negative controls on another architecture, another decade and
another continent. Five of them work:

```
exepack.py  --refuse          582 of 582 refused
dosimage.py --refuse-check    582 of 582 refused
ppc.py      --census          582 of 582 refused
hsc.py                        582 of 582 refused
popmsg.py   --refuse          refused on every file it was given
```

**`pcspk.py` and `cga.py` have no refusal path at all**, and they duly find
things:

```
python tools/pcspk.py --tables _work/files/LaunchMe
  offset 239868:
    1/4643Hz x2, 4/1164Hz x4, 2/2326Hz x1

python tools/cga.py --scan _work/files/LaunchMe
  the five flattest windows: 224000 (49.4%), 288000 (29.5%), ...
```

**PC-speaker note tables and flat CGA frames, inside an ARM binary from 1994.**
Both are noise, and neither tool has a `--validate` or a `--refuse` to say so.
**A tool that cannot return nothing cannot be a negative control**, and these
two are inherited defects ten and eleven.

## `protscan.py`, and a zero that could not have been anything else

```
python tools/protscan.py --all-files _work/files
  BoG_ 0   SafeDisc 0   SECUROM 0   securom 0   CMS16.DLL 0
  LaserLok 0   CDCOPS 0   StarForce 0   TAGES 0   SETTEC 0   Macrovision 0
  POSITIVE CONTROL: four zero bytes   575 files
```

Eleven markers, eleven zeros, and the positive control fires on 575 files of
582. **The zero is worthless and the chapter says so**, because every one of
those eleven is the *product name of a PC CD-ROM copy-protection scheme*, and
this session's own headline lesson is that **a search for what the producer is
called is not a search.** None of those strings could have appeared on a 3DO
disc pressed in 1994.

**What this disc actually has instead is `/signatures`**, 335,872 bytes of
high-entropy data between the boot binary and the root copies, plus a 512-bit
block at the end of every driver ROM and at +224 of the `/rom_tags` block. The
protection on this platform is a signature, it is present, and `protscan.py`
cannot see it because it was never told to look for it. **The measurement is
"the table does not apply", not "the disc is unprotected".**

## Formats that do not apply, said after looking

```
iso9660.py --vd     descriptors : 0 ; no volume descriptor of type 1
```

The refusal is clean and reasoned, but **its exit code is 0**, so a script
counting refusals by exit status would count this as a pass. Inherited defect
twelve.

`mode1.py`, `cdxa.py`, `subch.py`, `toc.py` and `leadout.py` address structures
a single-track `MODE1_RAW` CHD does not have. The fifteen Android tools, the
four AVI tools, the Copysoft set and the Tales tools address other platforms
entirely. **They were not run, and saying they were not run is the honest form**
— running a Namco archive reader against a 3DO disc to report a zero would be
manufacturing a measurement.

## The budget

`_work/` reached **630,463,335 bytes** — a 355,951,680-byte raw track, a
272,214,595-byte extracted tree, and about two megabytes of PNGs and logs that
are not published. That is the **second largest in the series**, as predicted,
and within four megabytes of what the pre-briefing measured before deleting it.

The last nine sessions: 14,039,770,841 / 1,408,855,740 / 754,254,358 /
482,238,888 / 18,368,483 / 5,378,762 / 2,235,430 / 3,566,054 / **630,463,335**.

## And the thing this repository will not publish

**No name from the credit roll, and no frame of any film or cel.** The
reasoning is in [10](10-three-films-and-a-credit-roll.md) and it is a decision,
taken explicitly, with the argument written out and the owner of the disc
consulted before it was taken. `.png`, `.aiff`, `.cel*`, `.anim` and `.stream`
are all in `.gitignore`, and `git ls-files` is checked in both directions.
