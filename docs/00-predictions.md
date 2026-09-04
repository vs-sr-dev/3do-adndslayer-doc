# 00 — predictions: written before the fourth disc was opened

*Measure: what I expected of this pressing, written down before I ran a single
tool of my own against it, so that being wrong costs something countable.*

Written after reading the session brief, the six files in `_pre/`, the three
neighbouring 3DO repositories' `docs/`, the
[3DO platform notes](https://github.com/vs-sr-dev/3do-platformnotes-doc), and
**the docstrings of the tools I intend to point at this object** — and before
running any of them. Scored in the scoring chapter.

Each clause carries two tags. `method` or `content` says whether it is a claim
about how the work will have to go or about what the object contains.
`inherited` or `open` says whether it re-tests somebody else's measurement or
is this session's own bet. **The two score columns are never added together.**

Section §A restates what was handed to me and is worth **no points**.

---

## What this disc is, in one paragraph, before it is opened

*Advanced Dungeons & Dragons — Slayer*, 3DO, USA, 1994. One CHD, one
`MODE1_RAW` track, 151,340 sectors, **no audio tracks at all**. An Opera file
system with 582 files. Three quarters of it is uncompressed AIFF; another
eighteenth is three Cinepak movies; the game itself is one 299 KB ARM binary
and about ten megabytes of cels and animations. **It names nobody in any
string, and its entire credit roll is inside a 24.6 MB video.**

## The three things I am actually betting on

1. **The `ANIM`/`CCB ` container is already readable and the pre-briefing aimed
   the wrong tool at it.** `celdecode.py` takes a file; `ccbread.py` — its own
   import — takes a **tree**, and implements the exact chunk rule the
   pre-briefing derived by hand. C05–C10.
2. **"Slayer shipped raw samples" is half false.** Fifty-nine of the eighty-one
   files are 8-bit mono. A studio that halves its bit depth has made a
   compression decision; it just made it in the sampler and not in the codec.
   C15–C18.
3. **The `/AppStartup` case mismatch is inside a comment** and therefore is not
   a mismatch at all. C31.

## Calibration, re-derived by adding

The open-clause series, *predicted minus obtained*, thirteen objects:

```
+10.5  +7.5  +5.0  +2.0  -14.0  -2.0  +9.0  0.0  +19.75  +5.25  -4.10
-3.40  +9.30
```

Summed by command: **44.80 over 13, mean +3.4462**, amplitude 33.75, median
+5.00, four negatives of thirteen. The brief's correction to itself checks out:
the first twelve sum to **35.50**, mean **+2.9583**, against the +3.35 that was
published. **No global offset is applied**, because the thirteenth overshoot had
a single named cause — four clauses betting one substantive bet — and correcting
for a cause that is not present today would make this worse.

**Predicted totals, from `tools/predcount.py`:**

```
document      : docs\00-predictions.md
clauses        : 36
  inherited    : 6
  open         : 30
  method       : 7
  content      : 29

the cross-tabulation, which is the one that matters:
  inherited method  : 3
  inherited content : 3
  open      method  : 4
  open      content : 26

TWO TOTALS, NEVER SUMMED TOGETHER:
  inherited predicted : 5.80 of 6
  open      predicted : 19.50 of 30

content share of the open clauses : 26 of 30 = 86.7 %
```

**Predicted: inherited 5.80 of 6, open 19.50 of 30** — 65.0 % of the open
column. **This header is written from `predcount.py`'s output and the first
version of it was wrong**: I wrote 11 inherited and 25 open by hand and the
command counted 6 and 30. That is the fourth session in a row in which the
command caught a hand-added total, and it is the whole reason the rule exists.

**On the 86.7 % content share, and the prescription that says to write fewer.**
The tool prints a warning here and I am declining it, with the brief's own
reason: *the label measures the difficulty of the assertion, not the quality of
the intuition.* Twenty-six `content` clauses out of thirty open ones is what an
object with an unopened container and an unargued thesis honestly produces. A
session that rewrote half of them as `method` would score better and find less,
and the scoring chapter will report the two columns separately so that the
choice is visible rather than laundered.

---

## §A — what the briefing already told me, and which therefore proves nothing

- **A.1** One CHD v5, **200,769,302 bytes**, logical 370,480,320, hunk 19,584,
  unit 2,448, 151,340 units, compressors `cdlz` `cdzl` `cdfl`, ratio 54.2 %,
  header SHA-1 `13e835442a6a82458759293e8e2073526be45c3e`, data SHA-1
  `75c1b50db7795c400f78a6adc8e2c822860ca9d1`, file's own SHA-1
  `126b1dcc03007b1482cd9583edb2c2754cb5effa`. One track, `MODE1_RAW`,
  `SUBTYPE:NONE`, `FRAMES:151340`, `PREGAP:0`. Extracts to **355,951,680 bytes**
  = 151,340 × 2,352.
- **A.2** **No audio tracks.** First of the four 3DO discs here with none.
- **A.3** 151,340 / 333,000 = **45.4474 %** of a 74-minute CD, against Crash 'n
  Burn 307,446 (92.3261 %), SSF2T 151,704 (45.5568 %), Wolfenstein 3D 56,702
  (17.0276 %). **364 sectors short of SSF2T.**
- **A.4** `sectormap3do.py`: file 133,224 (88.0296 %), copy 2, dir 40, dircopy
  45, `iamaduck` 17,729 (11.7147 %), zero 300 (0.1982 %), other **0**,
  double-claimed **0**. 151,040 blocks declared, **300 sectors past the declared
  volume**.
- **A.5** Label `CD-ROM`, empty comment, identifier 155,699,688 (`0x0947C9E8`),
  block size 2,048, 151,040 blocks declared, root dir id 906,723,034, root 1
  block, **seven copies** at 74,605–74,608 and 134,219–134,221, all seven
  byte-identical. `--label` computes **128 bytes**; `--list` reports
  `/Disc label` at **132**.
- **A.6** **582 files, 24 directories, 272,214,595 bytes, 573 distinct SHA-1,
  0 unreadable.**
- **A.7** By extension: `.aiff` 81 / 208,953,812 / **76.7607 %** / mean H 7.5064;
  `.stream` 3 / 50,266,112 / 18.4656 %; `.anim` 141 / 9,916,684 / 3.6430 %; no
  extension 68 / 1,445,529 / 0.5310 %; `.celA` 176 / 1,302,348 / 0.4784 %;
  `.cel` 12 / 200,764 / 0.0738 %; `.celB` 31 / 65,472 / 0.0241 %; `.dsp` 63 /
  54,158 / 0.0199 %; `.ROM`/`.rom` 6 / 7,180; `.font` 1 / 2,536.
- **A.8** Seven duplicate groups, 223,455 bytes stored twice: Mind Flayer =
  Sword Wraith (62,220), Carrion Crawler = Purple Worm (56,804), Gelatinous Cube
  = Slime (52,748), Ghost = Shade (43,276), two `ViewChar.anim` (6,208),
  `Ceiling7.celB` = `T3Ceiling.celB` (2,196), and **four one-byte `junk` files**.
- **A.9** `aiffread.py`: 81 files, 208,931,420 bytes of sample data,
  **22:30.04**, 63 containers that do not close — the `.dsp` files, correctly
  refused. Kinds: 59 × AIFF 22,050/8/mono, 18 × 44,100/16/stereo, 3 × 22,255/8/
  mono, 1 × 44,100/16/mono. **Every one is codec `NONE`.** Largest single file
  `/data/sounds/music/Atmosphere I.aiff`, 24,690,874 bytes, 2:19.97.
- **A.10** Audio tree by count: `/data/sounds/music` 19, `growls` 43, `squeals`
  8, `/data/sounds/*.aiff` 10, `/System/Audio/aiff` 1 (`sinewave.aiff`, SDK).
- **A.11** 63 `.dsp` in `/System/Audio/dsp`, 54,158 bytes, **not audio**; they
  are the Opera audio folio's DSP instrument patches.
- **A.12** Magic bytes: 141 `.anim` files open `ANIM` + u32 (74 with length
  0x30, 67 with 0x20); of the 219 files with a cel extension, **180 open `CCB `
  and 39 open `ANIM`**. Container is IFF-style, big-endian, 4-byte tag + u32
  length. `ANIM` is 0x20 or 0x30, `CCB ` is 0x50.
- **A.13** The three `.stream` movies chunk-walk to **residue zero, 3 of 3**:
  `Intro.stream` 17,367,040 (SHDR 1, CTRL 1, FILM 1327, SNDS 242, FILL 265);
  `Credits.stream` 24,641,536 (1, 1, **1225**, 279, 376); `EndGame.stream`
  8,257,536 (1, 1, 834, 153, 126). **3,386 FILM chunks in total.**
- **A.14** `aifcensus.py`: **41 AIF images**; `SWI &11` at 0x10 41/41, entry
  0x100 41/41, flags 32 41/41, image base 0 41/41, debug size 0 41/41; **reloc
  target == ro + rw 39 of 41**, `ro + rw + 4` **2 of 41**; **5 compressed, all
  in `/System`**. By directory: root 1, System 38, data 2. The three that are
  this game's: `/LaunchMe` 299,312 (ro 219,692, rw 38,684, H 5.859),
  `/data/Player` 53,084, `/data/StorageTuner` 32,608.
- **A.15** `/LaunchMe` has 906 printable runs of ≥ 6 characters, loads
  `3DO.cel`, `TSR.cel`, `ADD.cel`, `Slayer.cel`, `HLion.anim`, `SSI.anim`,
  `XSlayer`, `slayer1.font`, `StorageTuner`, `Player`, and writes
  `/NVRAM/Slayer Game`. Counted in it: `Entertainment` 0, `Strategic` 0,
  `Simulations` 0, `Copyright` 0, `(C)` 0, **any four digits beginning `19`: 0**.
- **A.16** The only dated strings are 3DO's own:
  `operamath.dev 21.10.603 05/10/94 21:49:54 stan port1_3`,
  `Tue May 10 21:49:54 PDT 1994`,
  `$Id: startopera,v 1.16 1994/04/05 22:18:25 vertex Exp $`, and
  `Copyright 1993 The 3DO Company` in `boot_code`.
- **A.17** **`sdkdiff.py` against SSF2T: 116 files each, 487,653 against 487,585
  bytes, 115 identical, 1 changed, 0 removed, 0 added. The one change is
  `Drivers/CPORT49.ROM`, 1,400 → 1,332, −68 bytes.** Against Wolfenstein 3D:
  36 identical, 51 changed, 29 removed, 39 added. Against Crash 'n Burn: 25
  identical, 67 changed, 24 removed, 2 added.
- **A.18** `crossall.py` with `--skip`: 83 repositories swept, **114 of 573
  hashes appear elsewhere** — SSF2T 141 lines, Wolfenstein 73, Crash 'n Burn 25,
  and ten `pc-*` repositories with one each. Roots 1–6 give zero.
- **A.19** Collection denominator: **244 directories, 123 `*-doc`, 84 with a
  `notes\`**, over seven roots. Six of the 123 are 3DO.
- **A.20** `/signatures` 335,872 bytes, 164 blocks, 330,596 non-zero —
  **335,872 exactly on all four 3DO discs**, four different SHA-1.
  `/rom_tags` 128 bytes, opens `0f 0d 00 00 00 00 00 00 00 00 00 01 00 00 14 30`.
  `/AppStartup` 160 bytes of readable text.
- **A.21** The published thesis column, taken from the neighbours' own `docs/`:
  Crash 'n Burn **0.3230 %** recorded sound and ~77 % identified; SSF2T
  **86.2465 %** and 87.3403 %; Wolfenstein 3D **59.7896 %** and 71.1132 %.
  SSF2T's 63 AIFF-C files are SDX2 at 44.1 kHz stereo for **50:38.08**.
- **A.22** The nine inherited tool defects, of which the ninth is
  `celdecode.py`'s `PermissionError` on a directory. The pre-briefing's `_work/`
  was 628,329,664 bytes and was deleted.

**Everything above is worth zero. What follows is worth points.**

---

## §B — the clauses

### The medium, and the reader

**C01** `method` `inherited` — `chdman.exe info` reproduces A.1 field for field,
and an independent SHA-1 of the `.chd` taken here matches
`126b1dcc03007b1482cd9583edb2c2754cb5effa` at 200,769,302 bytes. The extracted
track is exactly 355,951,680 bytes. *Predicted: 1.0*

**C02** `content` `inherited` — `iso9660.py` **refuses this image**, and refuses
it for a stated reason rather than a traceback: there is no `CD001` at sector
16. The refusal is a measurement and it goes in the sheet. *Predicted: 0.9*

**C03** `method` `inherited` — `sectormap3do.py` reproduces A.4 exactly:
151,340 attributed, **0 in `other`, 0 double-claimed**, `iamaduck` 17,729. No
sector of this disc is unexplained on the first pass. *Predicted: 1.0*

**C04** `content` `open` — **the label's two lengths reconcile as arithmetic and
`--label` is the one that is wrong.** The on-disc record is **132 bytes**, which
is `100 + 4 × 8`, and the eighth 32-bit word is the root's *own* first block
rather than an eighth copy; `--label` computes `100 + 4 × (last_copy + 1)` over
the seven entries it chose to call copies and loses the word it has already
consumed. **Predicted resolution: 132 is right, 128 is short by exactly one
pointer, and the disc's own `avail_copies`/`root_copies` field will say 8 or the
array will have 8 slots.** *Predicted: 0.4*

**C05** `method` `open` — **`ccbread.py census TREE` is the missing reader and
it already exists.** The pre-briefing's "nothing in 443 tools walks it" is
wrong: `ccbread.py` implements four-character tag plus big-endian u32 length
including the eight-byte header, tiling to the last byte, and its `census`
subcommand takes a **directory**. It runs on `_work/files` unmodified and needs
no new tool for the walk. *Predicted: 0.9*

**C06** `content` `open` — **219 of 219 files with a cel extension close at
residue zero** under that rule. Both magics — the 180 `CCB ` and the 39 `ANIM` —
tile completely. *Predicted: 0.8*

**C07** `content` `open` — **141 of 141 `.anim` files also close at residue
zero**, giving **360 of 360** containers over the two extensions and 10.2 MB.
Any failure will be a single file and not a class. *Predicted: 0.7*

**C08** `content` `open` — **the difference between the 0x20 and the 0x30 `ANIM`
chunk is four extra 32-bit words, not a different format**, and the first six
words are common to both. The 0x30 form is the later or richer one and carries
per-frame timing the 0x20 form leaves implicit. *Predicted: 0.4*

**C09** `content` `open` — **the `ANIM` chunk carries a count field whose value
equals the number of `CCB ` chunks that follow it in the same file**, and that
identity closes on a clear majority of the 180 `ANIM`-headed files. The word
`0x000000c6` = 198 seen in the first file is **not** that field. *Predicted: 0.3*

**C10** `content` `inherited` — the two independent encodings of width and
height that `ccbread.py` proved on the first disc — word 16 against PRE1 bits
0..9, word 17 against PRE0 bits 6..15 — **agree on 100 % of the CCBs on this
disc**, and every `CCB ` chunk is exactly 80 bytes. *Predicted: 0.9*

**C11** `content` `open` — `celdecode.py` decodes at least one cel of this disc
to a PNG without modification, and the arithmetic identity
`rowbytes = (woffset + 2) × 4`, `payload = rowbytes × height` closes on the
unpacked cels here as it did on the first disc. **No frame of any cel is
published.** *Predicted: 0.6*

### The sixty-eight bytes

**C12** `content` `open` — **the 68 bytes are one contiguous run.** There is a
`k` such that Slayer's `CPORT49.ROM` equals SSF2T's for its first `k` bytes and
equals it again from `k + 68` to the end: a deletion, not a rewrite.
*Predicted: 0.5*

**C13** `content` `open` — **`CPORT49.ROM` is not an AIF image.** The six
`/System/Drivers/*.ROM` files are not among the 41 that `aifcensus.py` counted;
they carry a 3DO ROM-tag or a driver header instead, and the file contains at
least one printable driver-name string. *Predicted: 0.7*

**C14** `content` `open` — **the 68 bytes are data and not code**: the removed
run is dominated by ASCII, zero padding, or a table of small integers, and does
not disassemble as a plausible run of ARM instructions. The two discs' serial
driver differs by a *table*, not by an *algorithm*. *Predicted: 0.4*

### The audio, which is the thesis

**C15** `method` `inherited` — `aiffread.py` reproduces A.9 to the frame:
**81 files, 22:30.04, codec `NONE` on 81 of 81**, and **63 correct refusals** on
the `.dsp` files. *Predicted: 1.0*

**C16** `content` `open` — **the "uncompressed" charge is half wrong, and the
arithmetic says so.** Fifty-nine of the eighty-one files are **8-bit**, which is
a 2:1 decision taken in the sampler rather than in the codec. **The 18 files at
44,100/16/stereo will hold more than 90 % of the 208,953,812 audio bytes**, so
the thesis is not "the studio did not compress" but "the studio compressed the
effects and not the music". *Predicted: 0.8*

**C17** `content` `open` — **SDX2 at exactly 2:1 would have freed 104,476,906
bytes = 51,014 sectors**, taking the disc from 151,340 to about **100,326
sectors, 30.13 % of a CD**, and the audio share from 76.7607 % down to about
62.3 %. I will publish that table. *Predicted: 0.8*

**C18** `content` `open` — **the boring answer is the right one and it is not
the whole answer.** The disc is 45 % full and nothing was at stake; but the
three files at **22,255 Hz** — the Macintosh rate, unresampled — say the audio
was dropped in from a Mac without a conversion pass, and a pipeline with no
conversion pass is a pipeline with no place to put a codec. **Absence of a tool,
not abundance of space, is the better explanation and the object supplies the
evidence for it.** *Predicted: 0.4*

**C19** `content` `open` — **the 19 files in `/data/sounds/music` are music and
not narration**, and the owner of this machine will confirm it. The 43 growls
and 8 squeals are creature vocalisations. *Predicted: 0.8*

### The credits, which are a decision before they are a measurement

**C20** `method` `open` — `cvidmovie.py --census` runs on all three `.stream`
files without modification and reports **3,386 `FILM` chunks**, and it decodes
at least one frame of `Credits.stream` to a raster. *Predicted: 0.8*

**C21** `content` `open` — **`Credits.stream`'s video is 320 × 240**, the 3DO's
standard NTSC raster, and the 1,225 `FILM` chunks are one frame each, giving
between 60 and 130 seconds of roll at a rate between 10 and 20 frames per
second. *Predicted: 0.6*

**C22** `content` `open` — **the roll names at least twenty distinct people**,
and it names the studio and the year that no string on the disc contains. **Only
its shape is published**: screen count, role count, person count, and the fact
that a year appears. **No name, no frame, no still.** The owner of this machine
asked for exactly this and the reasoning is written out rather than assumed.
*Predicted: 0.7*

**C23** `content` `open` — **`HLion.anim` and `SSI.anim` decode to the two
studios' logos**, and the logos say in pixels what no string says: the disc's
makers are identifiable from the object without decoding a single credit frame.
That is the argument that makes the volume question real. *Predicted: 0.5*

### The programs

**C24** `content` `inherited` — `aifcensus.py` reproduces A.14: 41 images,
41 of 41 on `SWI &11`, entry 0x100, flags 32, image base 0, debug size 0, and
**39 of 41 on the relocation identity**. The exception the third disc found
reproduces on the fourth. *Predicted: 1.0*

**C25** `content` `open` — **the two images that break the relocation identity
are both in `/System`**, and **at least one of them is among the five compressed
images**. They are not `/LaunchMe`, `/data/Player` or `/data/StorageTuner`.
*Predicted: 0.6*

**C26** `content` `open` — **`/LaunchMe` is the whole program.** There is no
overlay, no second code file and no archive: `/data/Player` and
`/data/StorageTuner` are separately-launched utilities named in `/LaunchMe`'s
strings, not code it loads into itself. *Predicted: 0.7*

### The small things, which is where the fourth disc earns its keep

**C27** `content` `open` — **the `/AppStartup` case mismatch is inside a
comment.** All three lines of that 160-byte file begin `##`; the sentence that
says `$boot/Launchme` is prose about what the system will do, not an instruction
the shell executes. **There is no case mismatch in the boot path, and the
pre-briefing's question dissolves.** *Predicted: 0.8*

**C28** `content` `open` — **the 300 zero sectors are the last 300 of the
track**, physical 151,040 through 151,339 inclusive, contiguous, and are exactly
the sectors the volume label does not declare. The two facts are the same fact
stated twice. *Predicted: 0.8*

**C29** `content` `open` — **no arithmetic relates 74,605 to 134,219**, to
151,040, to 151,340 or to each other in any form this session will accept as a
rule. Seven copies in runs of four and three is a mastering artefact and the
honest answer is that its placement is unexplained. *Predicted: 0.7*

**C30** `content` `open` — **the ten single crossings into `pc-*` repositories
are one hash, not ten**: the SHA-1 of the one-byte `junk` file, which appears
four times here. **The byte is `0x0a`.** *Predicted: 0.5*

**C31** `content` `open` — **43 growls, 39 distinct.** The four sharing pairs in
A.8 are the only duplicates inside that directory, and the bestiary is 43 named
AD&D creatures voiced by 39 recordings — a content finding about a licence, not
about a codec. *Predicted: 0.8*

**C32** `content` `open` — **`protscan.py --all-files` reports zero markers over
all 582 files**, and the seven MS-DOS readers written for the previous object —
`dosimage.py`, `exepack.py`, `popmsg.py`, `ppc.py`, `hsc.py`, `pcspk.py`,
`cga.py` — **refuse 100 % of what they are shown here**. Both are negative
controls and both are reported with their denominators. *Predicted: 0.9*

### The collection, and the platform

**C33** `content` `open` — `crossall.py --skip` reproduces **114 crossings of
573**, and the collection re-measures at **123 `*-doc` repositories**, with the
`notes\` count moving from 84 to **85** once this repository has one.
*Predicted: 0.7*

**C34** `content` `open` — **this disc breaks at least one mark the platform
notes carry as `[2 of 2]`**, and the strongest candidate is anything those notes
say about Red Book audio, because this is the first of the four with **no audio
track at all**. It also supplies at least three genuine `[4 of 4]` lines,
`/signatures` at 335,872 bytes among them. *Predicted: 0.7*

**C35** `method` `open` — **the denominator is decided before it is used and
there is exactly one for coverage: the user area, 151,340 × 2,048 =
309,944,320 bytes.** The 272,214,595 bytes of files is a numerator against it
(87.83 %) and the 200,769,302-byte `.chd` is a property of the compression and
not of the disc. **Identified coverage lands between 90 % and 97 %**, above all
three neighbours, because three quarters of the object is a public format that
opens for free. *Predicted: 0.6*

**C36** `method` `open` — **this session produces platform-notes text and does
not write it into that repository**, produces no correction to
`pc-linksthechallengeofgolf-doc`'s three outstanding ones, and finishes at
**seventeen documents**, with `_work/` between 0.9 and 1.6 GB — the second
largest in the series, as the brief predicted before measuring it.
*Predicted: 0.6*

---

## What would make this a bad set of predictions

Two failure modes, named in advance.

**The first is the one the calibration keeps punishing:** a cluster of clauses
that look independent and are one bet. **C05–C07 are one bet** — that the chunk
rule the pre-briefing derived by hand is the rule `ccbread.py` already
implements — and if it is wrong all three fall together. That is priced in:
their predicted total is 2.4 of 3, not 2.7.

**The second is a search that cannot fire**, which is this brief's own
prescription. Every clause above that says *zero* — C02's refusal, C32's markers,
C27's absent mismatch — names the thing being searched for and the file that
would contain it, so that a zero is a zero and not a typo in a needle.
