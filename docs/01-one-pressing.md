# 01 — one pressing: a dungeon that is three quarters music, and a date nobody had found

*Measure: what this object is, on which denominator, how much of it this
repository can name, and what the disc keeps that the file system throws away.*

## The object

One CD-ROM, pressed in 1994. *Advanced Dungeons & Dragons — Slayer*, 3DO
Interactive Multiplayer, USA. A first-person dungeon crawler under TSR's
licence. It arrived as one CHD of **200,769,302 bytes**, SHA-1
`126b1dcc03007b1482cd9583edb2c2754cb5effa`, and nothing else.

```
d:\...\3do-platformnotes-doc\bin\chdman.exe info -i "Slayer (USA).chd"
```

One track, `MODE1_RAW`, `SUBTYPE:NONE`, **151,340 frames, `PREGAP:0`, and no
audio track at all** — the first of the four 3DO discs in this collection with
none. `extractcd` gives 355,951,680 bytes, which is 151,340 × 2,352 exactly.

The file system is not ISO 9660. `iso9660.py` was pointed at the image and
reported **`descriptors : 0`** and `no volume descriptor of type 1`; the
refusal is a measurement and it cost one command. What is there is **Opera**,
the file system of the console's operating system, and `opera.py` — written on
the first 3DO disc of this collection and now reading its fourth — walks it
without a refusal: **582 files, 24 directories, 272,214,595 bytes, 573 distinct
SHA-1, nothing unreadable.**

## The denominator, decided before it was used

There are three candidate numbers and at least two are legitimate. They are
named here so that no figure below has to be re-read against a different one:

| candidate | bytes | what it is |
|---|---|---|
| the CHD | 200,769,302 | a property of **the compressor**, not of the disc |
| the extracted track | 355,951,680 | 2,352 bytes a sector: user data plus sync, header and ECC |
| **the user area** | **309,944,320** | 151,340 × 2,048 — **the denominator** |
| the declared volume | 309,329,920 | 151,040 × 2,048 — 300 sectors short |

**The published denominator is 309,944,320 bytes**: the user data of every
sector physically in the track. It is the one the three neighbouring 3DO
repositories used and changing it would have made every comparison in
[12](12-against-the-collection.md) meaningless. The CHD is excluded on
principle — a better compressor would change it and nothing about the disc
would have moved.

Against it, the file system's 272,214,595 bytes are **87.8269 %** of the
pressing. The other 12.1731 % is [mastering fill and
zeros](04-every-sector.md).

## Coverage: 87.6184 %, and the eighteen files that are not

```
python tools/account3do.py _work/files 151340 151040
```

**271,568,258 bytes — 87.6184 % of the user area — are of a kind this
repository derived or validated on this disc.** That is the highest figure the
collection has recorded, ahead of Super Street Fighter II Turbo's 87.3403 %,
Crash 'n Burn's ~77 % and Wolfenstein 3D's 71.1132 %.

**It is also the least impressive of the four**, and saying so is the point.
Three quarters of this disc is uncompressed AIFF, which is a public format that
opens for free; another sixth is a Cinepak film whose reader existed two discs
ago. **The coverage was won by the object, not by the session.** What the
session actually opened is 3.74 % of the pressing, and it is
[chapter 06](06-the-container.md).

Of the 272,214,595 bytes in files, **646,337 — 0.2085 % of the pressing — are
still unnamed**, and `account3do.py` now prints every one of the eighteen files
by name so the figure can be audited instead of believed:
`/data/MapSquares` (104,324 B), `/data/MatchData` (87,078),
`/System/Kernel/os_code` (85,896), and fifteen smaller.

The accounting tool was **rewritten for this disc**, for the third session
running, and the two changes are named in its docstring. One of them moved the
number: the previous version found cels by signature scan and left 9,432,360
bytes — 3.04 % of the pressing — in a bucket called *"kind not derived"*.
**That bucket was a property of the reader.** The container walks; see
[06](06-the-container.md).

## What this disc is made of

```
python tools/entropy.py --tree _work/files
```

| extension | files | bytes | share of the pressing |
|---|---|---|---|
| `.aiff` | 81 | 208,953,812 | **67.4166 %** |
| `.stream` | 3 | 50,266,112 | 16.2178 % |
| `.anim` | 141 | 9,916,684 | 3.1995 % |
| (none) | 68 | 1,445,529 | 0.4664 % |
| `.celA` | 176 | 1,302,348 | 0.4202 % |
| `.cel` | 12 | 200,764 | 0.0648 % |
| `.celB` | 31 | 65,472 | 0.0211 % |
| `.dsp` | 63 | 54,158 | 0.0175 % |
| `.ROM` / `.rom` | 6 | 7,180 | 0.0023 % |
| `.font` | 1 | 2,536 | 0.0008 % |

**The game is under four per cent of its own disc.** One ARM binary of 299,312
bytes, 370 cel containers holding 2,516 frames, a font, and two small
utilities. Everything else is a soundtrack and three films.

## The thesis, on the denominator the neighbours used

**67.4093 %** of the user area is AIFF sample data — 208,931,420 bytes,
**22:30.04**, in eighty-one files, **codec `NONE` on eighty-one of eighty-one**.

```
python tools/thesis3do.py _work/files 151340 151040
```

| disc | pressed | recorded sound, as a share of the user area |
|---|---|---|
| Crash 'n Burn | 1993-09-09 | 0.3230 % |
| **Slayer** | **1994-08-16** | **67.4093 %** |
| Super Street Fighter II Turbo | 1995-01-10 | 86.2465 % |
| Wolfenstein 3D | 1995-09-06 | 59.7896 % |

The dates in that table are not release dates and are not guesses: they are the
four discs' own `/rom_tags` records, read in [11](11-a-date-in-128-bytes.md).
**They also reorder the collection** — Slayer was pressed before Super Street
Fighter II Turbo, not after, which no session had been able to say.

**The brief that opened this session handed over 76.7607 % and asked for it to
be put in that column.** It is a true number about a different question —
`.aiff` bytes as a share of *the bytes in files* — and the three published
figures are shares of *the user area*. Nine and a third percentage points
separate the two readings of the same sound. See
[15](15-corrections.md), where it is the largest of the corrections.

The soundtrack, why it was not compressed, and what SDX2 would have cost are
[chapter 09](09-a-soundtrack-uncompressed.md). **The owner of this machine
listened to it and reported that all nineteen files in `/data/sounds/music` are
background music matching their own filenames** — which is what settles that
chapter's subject; `notes/owner-observations.txt` records it.

## What this object keeps, and what it throws away

**It keeps no dates in its file system.** Opera stores no volume creation
timestamp and no per-file mtime. Three sessions of this collection have written
that sentence and stopped there.

**This one did not stop there, and the disc does carry a date.** It is in
`/rom_tags`, 128 bytes at block 1, in a 32-byte record of type `0x0c`, and read
as seconds since the Macintosh epoch it says **1994-08-16 09:29:56**. The same
record dates all four discs of this collection into the right order and each
one after its own SDK build stamp. That is [chapter 11](11-a-date-in-128-bytes.md),
and it is the thing this session found that nobody was looking for.

**It keeps no user state at all.** `/LaunchMe` writes its save game to
`/NVRAM/Slayer Game`, on the console's battery-backed memory. Nothing on this
disc was ever written by anybody who played it, so there is nothing here to
redact — the third distinct answer this collection has recorded to the same
question.

**And it throws away every name.** Not one of the 582 files contains, as a
string, the name of the studio, the publisher, the licensor or the year.
`Entertainment` 0, `Strategic` 0, `Simulations` 0, and in `/LaunchMe` not one
four-digit number beginning `19`. All of it is in pixels — and it turns out
**not** to be only in the 24.6 MB credit movie the brief pointed at. Two
hundred kilobytes of still cel carry the year, the copyright, the licensor and
the publisher, and one command reads them. See
[10](10-three-films-and-a-credit-roll.md).
