# 07 — forty-one binaries: thirty-eight belong to the console, and the two that break the rule belong to the game

*Measure: every ARM Image on the disc against the five-part identity the first
two discs derived, and the identity of the exceptions — which nobody had asked
for.*

## The census

```
python tools/aifcensus.py _work/files
```

```
AIF images                          : 41
SWI &11 at 0x10                     : 41 of 41
entry point 0x100                   : 41 of 41
flags at 0x30 == 32                 : 41 of 41
image base == 0                     : 41 of 41
debug size == 0                     : 41 of 41
reloc target == ro + rw             : 39 of 41
reloc target == ro + rw + 4         :  2 of 41
neither of the three                :  0 of 41
compressed images                   :  5 of 41
```

Five claims at 41 of 41, on a fourth disc. The sixth — the relocation-target
identity — breaks twice, and it broke on the third disc too.

**Three of the forty-one are this game's.** The other thirty-eight are
Portfolio OS, shipped on the disc because that is how a 3DO boots, and
identical byte for byte with the twin's ([12](12-against-the-collection.md)).
Every statistic in this chapter that mixes them says which is which.

| image | bytes | ro | rw | H | compressed |
|---|---|---|---|---|---|
| `/LaunchMe` | 299,312 | 219,692 | 38,684 | 5.859 | no |
| `/data/Player` | 53,084 | 49,928 | 2,616 | 6.095 | no |
| `/data/StorageTuner` | 32,608 | 29,840 | 388 | 5.794 | no |

## Which two, and it is not the two anybody would have guessed

The pre-briefing noted that two of forty-one put `ro + rw + 4` where the other
thirty-nine put `ro + rw`, and said *"which two is one `grep` away"* and did not
run it. This session predicted (C25) that **both would be in `/System`** and at
least one among the five compressed images, on the reasoning that 38 of the 41
are 3DO's.

```
EXCEPTION /LaunchMe            ro=219692 rw=38684 ro+rw=258376 target=258380 diff=+4
EXCEPTION /data/StorageTuner   ro=29840  rw=388   ro+rw=30228  target=30232  diff=+4
```

**Both exceptions are this game's own binaries.** Neither is in `/System`.
Neither is compressed. The prediction was wrong in every particular and the
truth is more interesting than the guess:

```
3DO's thirty-eight images  : 38 of 38 on ro + rw     no exceptions
this game's three images   :  1 of 3  on ro + rw     two exceptions
```

**Thirty-eight images built by the platform holder agree; three built by the
studio disagree two times out of three.** The identity is not a property of the
ARM Image Format — it is a property of a linker invocation, and this disc
carries two of them. `/data/Player`, the third, sits with the thirty-eight.

What the four extra bytes are is not settled here. The relocation branch at
offset 0x04 targets four bytes past the end of the read-write area rather than
its last byte, which is what a linker that emits a zero-length or four-byte
alignment word between the image and its relocation table would produce.
**That is a description of the arithmetic and not a claim about the toolchain**,
and the platform notes get it as a question in [13](13-the-platform-notes.md).

The third disc had already broken this rule after two discs agreed; the
platform notes record it. **The fourth disc breaks it again and adds the thing
the third could not say: which side of the disc the exceptions are on.**

## The five compressed images

```
  path                        stored   stub      H  cond=E  decl/size
  /System/Folios/AUDIOFOLIO    37000    456  7.007   0.147     1.3252
  /System/Folios/GRAFMATH      33328    456  7.010   0.139     1.3475
  /System/Folios/graphix       25204    456  6.960   0.119     1.3768
  /System/Tasks/eventbroker    16028    392  7.036   0.137     1.2670
  /System/Tasks/shell          19264    392  6.916   0.172     1.3090

  H         compressed 6.9156..7.0356   uncompressed 4.9744..6.0948
  cond=E    compressed 0.1186..0.1716   uncompressed 0.5699..0.7608
  the two populations are disjoint on both statistics: True
  images with a stub                : 5 of 5 compressed
  images with a stub, uncompressed  : 0 of 36   (must be 0)
```

**Five of forty-one, all in `/System`, none of them this game's.** The
compression test the third disc is recorded as having broken holds cleanly
here: the two populations are disjoint on entropy *and* on conditional entropy,
the appended decompression stub is present on 5 of 5 and absent on 36 of 36,
and the declared-size ratio agrees with both on 5 of 5. **Three independent
statistics, no overlap, and the negative control at zero.**

Compression on this disc is entirely the platform holder's. The studio shipped
its 385,004 bytes of ARM code raw — which is the same decision it made about
209 megabytes of sound ([09](09-a-soundtrack-uncompressed.md)) and, unlike that
one, cost nothing worth counting.

## `/LaunchMe` says plenty and names nobody

906 printable runs of six characters or more, and the whole interface is in
them:

```
'Dungeon level %d completed.'   'This door leads to the next level.'
'There is no saved game to load.'    'Slayer game is corrupt!'
'Insufficient storage to save game.' 'Do you wish to free some space?'
'Overwrite previously saved game?'   'A = Yes             B = Cancel'
'Current game saved.'                '/NVRAM/Slayer Game'
'Sedrik Lionmane'                    'Magic Missile'
```

and the resources it loads by name: `3DO.cel`, `TSR.cel`, `ADD.cel`,
`Slayer.cel`, `SSI.anim`, `Lion.anim`, `slayer1.font`, `StorageTuner`, `Player`.

Counted over the whole binary: `Entertainment` **0**, `Strategic` **0**,
`Simulations` **0**, `Copyright` **0**, `(C)` **0**, and **any four digits
beginning `19`: 0**. The binary names its makers only as the names of picture
files it loads and states no year at all.

**And one of those filenames does not exist.** The pre-briefing read
`HLion.anim` out of the binary and the disc's file is `/data/Lion.anim`. The
bytes around it settle it:

```
offset 114407  ...\x00\x03\xaa  H  L i o n . a n i m \x00\x00\x00\x00
offset 114408                      L i o n . a n i m
```

`114408 mod 4 == 0`; `114407 mod 4 == 3`. **The string starts at the aligned
address and the `H` is the last byte of the preceding word, `0x0003aa48`.** A
string scan that does not respect alignment reads one character of a literal
pool as the first character of a filename — which is this session's own
headline lesson in its cheapest possible form: *a short marker is a claim about
a position, not about a file.*

## The save game, and the third answer to the same question

`/LaunchMe` writes to `/NVRAM/Slayer Game`, on the console's battery-backed
memory. **There is no file on this disc that any program writes.** Nothing here
was created by anybody playing it, so there is nothing to redact and nothing to
report as a shape.

That is the third distinct answer this collection has recorded to *"what does
this product remember about the person using it?"*: a high-score file with a
name in it, a high-score file with 120 bytes of spaces, and now **no user file
at all.** A measured negative is worth more than a question not asked, and this
one took one `grep` over 582 files.
