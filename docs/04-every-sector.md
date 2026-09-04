# 04 — every sector: the arithmetic closes, and 2,928 sectors are zero but only 300 of them are empty

*Measure: all 151,340 sectors of the track put in exactly one bucket, with
nothing unexplained and nothing counted twice — and the difference between a
sector that is zero and a sector that is free.*

## The map

```
python tools/sectormap3do.py _work/slayer.bin
```

```
physical sectors in the track      : 151,340
blocks the volume label declares   : 151,040
sectors past the declared volume   :     300

  file       133,224   88.0296 %
  copy             2    0.0013 %
  dir             40    0.0264 %
  dircopy         45    0.0297 %
  duck        17,729   11.7147 %
  zero           300    0.1982 %
  other            0    0.0000 %
  TOTAL      151,340  100.0000 %

double-claimed blocks: 0
'other' sectors      : 0 in 0 runs
```

**Zero sectors owned by nothing and zero claimed twice, on the first pass.**
Fourth disc of four with that result.

## The 300, and they are exactly where the label stops

The 300 sectors the volume does not declare are **contiguous, at physical
151,040 through 151,339 inclusive** — the last 300 sectors of the track, and
every one of them all-zero in its user data. So the two facts the pre-briefing
handed over separately —

> the 300 zero sectors, and the 300 sectors past the declared volume

— **are one fact stated twice.** The label declares 151,040 blocks; the disc
was cut with 151,340; the difference was never written.

## But 2,928 sectors are all-zero, and that is the more interesting number

Reading every sector's 2,048 bytes of user data directly rather than through
the file system:

```
all-zero user-data sectors : 2,928 in 684 runs
of which past the declared volume : 300 in one run
of which inside a file            : 2,628
```

**Nine in every ten all-zero sectors on this disc belong to a file.** They are
silence in the soundtrack, transparent runs in cels, and zero padding in the
films — 2,628 sectors, 5,382,144 bytes, 1.7365 % of the pressing, all of it
owned, all of it accounted for, none of it free.

The lesson is the one this collection keeps relearning in different clothes:
**a zero is a value, not an absence.** `sectormap3do.py`'s `zero` bucket counts
*unowned* zero sectors, and its 300 is right precisely because it does not
count the 2,628 that a file paid for. A tool that counted zero sectors without
asking who owned them would have reported 1.9347 % of this disc as empty and
been wrong by an order of magnitude.

## The duck, fourth disc of four

11.7147 % of the pressing is the eight-byte string `iamaduck`, repeated. It is
the 3DO mastering tool's filler and it is present on all four discs of this
collection:

| disc | fill | share of that pressing |
|---|---|---|
| Crash 'n Burn | `iamaduck` | 11.5100 % |
| **Slayer** | `iamaduck` | **11.7147 %** |
| Super Street Fighter II Turbo | `iamaduck` | 7.9339 % |
| Wolfenstein 3D | `iamaduck` | 23.5953 % |

**`[4 of 4]` on the presence of the fill and its exact string.** The fraction is
not a rule and never was: four discs give **7.93 %, 11.51 %, 11.71 % and
23.60 %**, a spread of a factor of three. The two that agree to within a fifth
of a point — Crash 'n Burn's 11.5100 % and this disc's 11.7147 % — are a
coincidence of two very different layouts, and the twin next door, 364 sectors
longer than this disc, is the furthest from it.

**The fill is the mastering tool's and carries nothing of the studio.** No
absolute build path, no filename, no timestamp: `iamaduck` and only
`iamaduck`, exactly as the first three discs found.

## Where the fill actually is, and it follows the root copies

Two regions, measured by reading every sector and testing it against
`iamaduck` × 256 rather than against its first eight bytes:

```
  74,609 ..  75,519      911 sectors
 134,222 .. 151,039   16,818 sectors
                      -------
                      17,729   = the sector map's `duck` bucket, exactly
```

**Each region begins at the block immediately after a run of root-directory
copies.** The first four copies sit at 74,605–74,608 and the fill starts at
74,609; the last three sit at 134,219–134,221 and the fill starts at 134,222.
Two regions, two root-copy runs, two joins that close to the block.

So the whole pressing reads, end to end:

```
       0            the volume label
       1            /rom_tags
       2 ..  74,290 boot_code, then the files; /AppStartup is 74,290
  74,291 ..  74,437 /LaunchMe
  74,438 ..  74,440 the /System and /data directories
  74,441 ..  74,604 /signatures
  74,605 ..  74,608 root copies 1-4
  74,609 ..  75,519 iamaduck
  75,520 .. 134,199 the rest of the files -- the sound and the films
 134,200 .. 134,218 directory and copy blocks (the map's dir/dircopy/copy)
 134,219 .. 134,221 root copies 5-7
 134,222 .. 151,039 iamaduck, to the end of the declared volume
 151,040 .. 151,339 zero, 300 sectors the label does not declare
```

That is a fourth answer to a question the second disc thought it had settled.
Its explanation was *"one free region, because the mastering tool appends"*;
the third disc refuted it with two regions and published *"no rule"*. **This
disc has two regions and a rule the earlier three did not state: the fill goes
where the root copies stop.** Whether that holds backwards is a re-measurement
on three discs this session did not make, and it is written into
[13](13-the-platform-notes.md) as a question rather than a mark.

## What this chapter does not claim

The 300 undeclared sectors could be a mastering minimum, a pad to a round
number, or nothing at all. 151,340 is not a round number in sectors, in
minutes (33:37.87) or in bytes. **151,040 blocks × 2,048 = 309,329,920 bytes,
which is not a round number either.** Neither figure yields to arithmetic and
this chapter declines to invent one.
