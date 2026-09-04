# 06 — the container: three hundred and seventy files close to the byte, and a frame is a chunk

*Measure: the `ANIM` / `CCB ` container walked chunk by chunk on every file
that carries it, the residue on each, and how many of its frames render — in
both directions, before a single field is named.*

## What was handed over, and what was actually true

The brief's headline for this session was that 3.74 % of the disc is a
container nobody has a reader for:

> 141 `.anim` files plus **39 files with a `.cel` extension that begin `ANIM`
> instead of `CCB `**: 180 containers, 10.2 MB, and **nothing in 443 tools
> walks it.**

Two of those statements are right and one is wrong, and the wrong one was the
premise of the day's plan.

**`ccbread.py` walks it, and has since the first 3DO disc.** Its `chunks()`
implements exactly the rule the pre-briefing derived by hand — four printable
characters, big-endian `u32` length including the eight-byte header, tiling to
the last byte — and its `census` subcommand takes **a directory**. The
pre-briefing reached instead for `celdecode.py`, which takes a file, handed it
a directory, got a `PermissionError`, and filed that as tool defect number nine.

```
python tools/ccbread.py census _work/files
  files walked                        : 582
  files containing the string 'CCB '  : 370
  CCB chunks parsed                   : 370
  files whose chunk chain closes      : 370
```

**One command, and it had been available for two discs.** This is the fourth
time in five sessions that the largest finding came from the cheapest command
in the box, pointed somewhere nobody had pointed it. It is written up as an
error in [15](15-corrections.md) because it was one.

What `ccbread.py` could *not* say is the thing this chapter is about: it counts
`CCB ` chunks and reports **one per file**, which on a 198-frame animation is
a true number that answers the wrong question.

## The census

`animwalk.py` was written here. It walks the same rule and reports the whole
chunk inventory, and its negative controls run first:

```
python tools/animwalk.py validate
ok  : 2,048 zero bytes                             refused
ok  : the string iamaduck, 2,048 bytes             refused
ok  : a chunk declaring more than the file holds   refused
ok  : a chunk of length 4                          refused
ok  : a tag that is not printable                  refused
ok  : a container with one byte of residue         refused
ok  : an AIFF                                      refused
ok  : positive control (CCB + PDAT)                accepted, 2 chunks
```

Seven refusals and one acceptance. Then:

```
python tools/animwalk.py census _work/files --words
```

```
files seen in the tree                : 582
containers (first tag ANIM or CCB )   : 370
  first tag ANIM                      : 180
  first tag CCB                       : 190
closing at residue zero               : **370 of 370**
failing to close                      : 0
```

**Three hundred and seventy of three hundred and seventy, at residue zero.**
Not one file leaves a byte over and not one declares a chunk longer than
itself.

## And there are ten more containers than anybody had counted

219 files carry a cel extension and 141 carry `.anim`: 360. The census finds
**370**, and the ten extra have **no extension at all**:

```
/data/3DO Cel            7,824      /data/Help Cel          35,164
/data/Alert Cel         16,000      /data/Highlight Cel        168
/data/Background Cel       168      /data/List Cel           4,360
/data/Full Cel          16,020      /data/Options Cel       11,108
/data/Space Free Cel       168      /data/Tile Background   10,128
```

101,108 bytes of cels in files named `... Cel` **with a space and no
extension**. This is the session's third instance of the same lesson in one
object — 39 `.cel` files that are `ANIM`, six `aif*.py` tools that have nothing
to do with `.aiff`, and now ten cels wearing no extension at all. **An
extension is not a format, and the absence of one is not the absence of a
format either.**

## The inventory

```
tag       count          bytes   lengths
PDAT       2516       11522428   1401 distinct, 64..43436
CCB         370          29600   80
XTRA        360           5760   16
PLUT        355          21284   5 distinct, 16..76
ANIM        180           7216   32, 48
CTPT          1             88   88
TOTAL      3782       11586376
unexpected tags: none
```

**Every `CCB ` chunk is exactly 80 bytes, on 370 of 370** — the length
`ccbread.py` derived on the first disc, holding a fourth time. Every `XTRA` is
16 bytes. `PLUT`, the palette, takes five lengths between 16 and 76 and is
absent from 15 containers. `CTPT` appears **once in 3,782 chunks**, in
`/data/monsters/Dracolich.anim`, and is not named here.

And the two independent encodings of the picture's size, which is
`ccbread.py`'s own proof that the CCB field layout is right, hold without
exception:

```
width  == pre1 bits 0..9 + 1      : 370 of 370
height == pre0 bits 6..15 + 1     : 370 of 370
row bytes == ceil(w*bpp/32)*4     : 38 of 38  (unpacked cels only)
```

## The shape, and what a frame is

Forty distinct chunk sequences, and they are variations on one:

```
 177  CCB PLUT XTRA PDAT                      a still cel
  39  ANIM CCB PLUT XTRA PDAT                 an animation of one frame
  20  ANIM CCB PLUT XTRA PDAT PDAT            two frames
  49  ANIM CCB PLUT XTRA PDAT x9              nine frames
   8  CCB PDAT                                a cel with no palette
```

**One `CCB `, one optional `PLUT`, one optional `XTRA`, then one or more
`PDAT`.** The drawing parameters and the palette are stated once; the pixel
data repeats. **A `PDAT` chunk is a frame**, and there are **2,516 of them**
across the 370 containers — 229 containers hold exactly one, and
`/data/Lion.anim` holds 198.

## The one identity this repository will state

The `ANIM` chunk is 0x20 bytes (89 files) or 0x30 (91 files) — six 32-bit words
or ten. **The 0x30 form is the 0x20 form plus four words**; the first six are
common to both, and words 0, 1, 4 and 5 are constant across all 180 files at
`0`, `1`, `0`, `0`.

**Word 2 equals the number of `PDAT` chunks that follow it, on 159 of 180.**

That is stated as a fraction and not as a field name, because the 21 exceptions
are not noise:

```
/data/walls   21 of 21 exceptions
  Wall4D1..D4   word2 = 7   PDAT = 1
  Wall5D0..D4   word2 = 5   PDAT = 1
  Wall6D1..D4   word2 = 5   PDAT = 1     (Wall6D0 says 1, and is right)
  Wall7D1..D4   word2 = 5   PDAT = 1
  Wall8D1..D4   word2 = 5   PDAT = 1
```

**Every exception is a wall texture at a viewing distance, in one directory,
with exactly one frame in it, claiming five or seven.** The `WallND` families
each hold five files, `D0` through `D4` — a texture at five distances.

The obvious reading is that the field counts the family and not the file, and
it is **not adopted, because it fails twice**: `Wall5D`, `Wall7D` and `Wall8D`
say five and are families of five, but **`Wall4D` says seven and is a family of
five**, and `Wall6D0` says one while its four siblings say five. A rule that
holds on three families of five and breaks on the two either side of them is a
pattern somebody's exporter left behind, not a field.

What this chapter will say is: **a field that is the frame count on 159 files
of 180 and is something else in one directory is described, not named.** The
brief asked for exactly this and it is worth repeating: *if you cannot say what
the fields are, say the shape and refuse to name them.*

Words 3 and 6 to 9 are printed by `animwalk.py census --words` and named by
nobody. Word 3 is `0x20000` on 154 of 180. Words 7, 8 and 9 are `0x7fff7fff`,
`0x7fff7fff` and `0x7fff0002` on 57, 52 and 55 files — `0x7fff` is the largest
positive 16-bit integer, which is what an initialiser looks like — and in
`/data/ViewChar.anim` words 8 and 9 read, in ASCII, **`IsWall`**. Six bytes of
somebody's identifier in a field that is `0x7fff7fff` everywhere else is the
signature of uninitialised memory, and this repository says that it looks like
one rather than that it is one.

## Every frame renders

The container closing is a claim about lengths. Whether the bytes inside are
what the format says they are is a different claim, and `celdecode.py` could
not test it: it decodes "the Nth cel of a file", a cel is a `CCB ` chunk, and
there is exactly one per file. On `/data/Lion.anim` it reports **"1 of 1 cels
decoded"** and writes one PNG out of 198 frames.

`animwalk.py frames` pairs the container's single `CCB ` and `PLUT` with each
`PDAT` in turn — which is what the container's own shape says a frame is — and
hands them to `celdecode.render`, imported rather than copied.

```
python tools/animwalk.py frames _work/files --census
containers rendered      : 370
PDAT chunks (frames)     : 2516
frames that render       : **2516 of 2516**
frames that do not       : 0
```

**Two thousand five hundred and sixteen of two thousand five hundred and
sixteen.** In **71 of them — 2.82 % — one row of the image runs past the end of
its `PDAT`** and is drawn as far as it decoded. That is reported rather than
swept: it is a real imperfection, either in the decoder's row arithmetic or in
the last row of certain packed cels, and this session did not chase it.

The bit depths, over the 370 CCBs: 6 bpp on 180, 4 bpp on 163, 16 bpp on 15,
8 bpp on 4, 2 bpp on 6, 1 bpp on 2. **332 of 370 are `PACKED`**, the run-length
form.

## What that buys the accounting

11,586,376 bytes — **3.7382 % of the pressing** — moved out of *"bytes inside
cel-bearing files, kind not derived"* and into a named chunk. The identified
figure went from 84.5751 % to **87.6184 %**, and the whole of that move is this
chapter. See [01](01-one-pressing.md).

## And it reads

One frame, decoded to check that the arithmetic is not merely self-consistent:
**frame 100 of `/data/Lion.anim`, 227 × 156 at 6 bpp, is the developer's
wordmark.** It says who made this game — in an animation, a hundred frames into a
container this collection could not walk this morning, and **without opening the
24.6 MB credit movie at all.** That is [chapter 10](10-three-films-and-a-credit-roll.md).

No frame is published. See [10](10-three-films-and-a-credit-roll.md) for why
that is a decision and not an omission.
