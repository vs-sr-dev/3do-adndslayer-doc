# 12 — against the collection: this disc has a twin, and 115 files of 116 are the same bytes

*Measure: this pressing's hashes against every other repository on two roots,
and its operating system against the other three 3DO discs, with the
denominators published before the results.*

## The denominators, measured first

```
root      directories     `*-doc`     with a `notes\`
  1                 7           0           0
  2                 6           0           0
  3                 4           0           0
  4                 4           0           0
  5                34           0           0
  6                74          11           2
  7               116         112          83
------------------------------------------------
TOTAL             245         123          85
```

**123 documentation repositories on two roots, 85 with a `notes\`.** The
previous session published 122 and 84; this is 123 because this repository now
exists, and 85 because it now has a `notes\`. The 245 is one higher than the
pre-briefing's 244 for a reason outside this object: a directory appeared in
root 1 during the session.

**Six of the 123 are 3DO**: the four disc repositories, the platform notes, and
a game list.

## The hash crossing

```
python tools/crossall.py notes/sha1-all.txt --collection d:/Homebrew7 \
    --skip 3do-adndslayer-doc
```

```
83 repositories swept, 361 list files, 128,774 hash tokens
CROSSINGS: 114 of my 573 distinct hashes appear in another repository
```

**114 of 573, and every single one is with another 3DO disc:**

| repository | lines |
|---|---|
| `3do-superstreetfighter2turbo-doc` | 141 |
| `3do-wolfenstein3d-doc` | 73 |
| `3do-crashnburn-doc` | 25 |
| **any `pc-*` repository** | **0** |

Root 6 gives zero. Roots 1 to 5 give zero.

**The pre-briefing reported "ten `pc-*` repositories, one each" and there are
none.** What it had found was a different list printed by the same tool six
lines further up:

```
EMPTY-FILE SHA1 (the trap): 32 occurrences in 12 repositories
   dc-dinocrisis-doc x4        pc-allodsonline-doc x2
   pc-bloodandlace-doc x1      pc-brokensword4-doc x1
   pc-canediterracotta-doc x1  pc-capcombeatemupbundle-doc x1
   pc-clic11-doc x9            pc-deadlypremonitiondc-doc x3
   pc-ilmiocomputer0206 x6     pc-residentevil-doc x2
   pc-zerocomico-doc x1        vis-racetheclock-doc x1
   -> excluded from the crossings below.
```

**Exactly ten of those twelve are `pc-*`**, which is where the ten came from.
They are repositories that contain a zero-length file; **this disc contains
none**, so it cannot cross with them, and `crossall.py` says so on its own line
before printing any crossing at all. See [15](15-corrections.md).

This session predicted (C30) that the ten single crossings would turn out to
be one hash — the one-byte `junk` file — and that its byte would be `0x0a`.
**There were no crossings to explain, and the byte is `0x0d`.** The clause was
wrong twice about a thing that did not exist.

## What actually crosses

Almost all 114 are `/System`: Portfolio OS, shipped identically on discs from
unrelated studios. `/AppStartup` crosses too — 160 bytes of commented-out
boilerplate, byte-identical with the twin's ([05](05-the-boot-chain.md)).

**Nothing in `/data` crosses with anything.** Not one cel, not one sound, not
one film, not the boot binary. The game is unique to its disc and the operating
system is not, which is the correct and slightly boring answer, and it is the
first time this collection has been able to state it with a zero on the other
side.

## The twin

```
python tools/sdkdiff.py _work/files ../3do-superstreetfighter2turbo-doc/_work/files
```

| against | files | identical | changed | removed | added | byte delta |
|---|---|---|---|---|---|---|
| **Super Street Fighter II Turbo** | 116 / 116 | **115** | **1** | **0** | **0** | **−68** |
| Wolfenstein 3D | 116 / 126 | 36 | 51 | 29 | 39 | — |
| Crash 'n Burn | 116 / 94 | 25 | 67 | 24 | 2 | — |

**One hundred and fifteen files of one hundred and sixteen, byte for byte.**
Two publishers, two studios that had no reason to speak, a Capcom arcade
conversion and an AD&D dungeon crawler, and their copies of the console's
operating system differ by **sixty-eight bytes in one serial-port driver**.
That difference is read instruction by instruction in
[08](08-the-sixty-eight-bytes.md), and it is a `kprintf`.

By category, the diff is a single line:

```
category       same  changed  removed  added   byte delta
Audio            64        0        0      0          +0
Daemons           1        0        0      0          +0
Devices           1        0        0      0          +0
Drivers           6        1        0      0         -68
Folios            4        0        0      0          +0
Graphics          1        0        0      0          +0
Kernel            3        0        0      0          +0
Programs         32        0        0      0          +0
Scripts           1        0        0      0          +0
Tasks             2        0        0      0          +0
TOTAL           115        1        0      0         -68
```

Sixty-four audio-folio files, thirty-two shell programs, four folios, three
kernel files, an event broker and a shell — **not one byte between them.**

The build stamps agree independently and in plain text:

```
both /System/Folios/operamath
  '@(#) operamath.dev 21.10.603 05/10/94 21:49:54 stan port1_3'
both /System/Scripts/STARTOPERA
  '# $Id: startopera,v 1.16 1994/04/05 22:18:25 vertex Exp $'
```

**The same SDK build, to the second, on two discs from different studios.**

## The SDK across four discs, ordered by a clock the studios did not control

| disc | pressed (`/rom_tags`) | `operamath` | `STARTOPERA` | `/System` files |
|---|---|---|---|---|
| Crash 'n Burn | 1993-09-09 | Sat Aug 14 15:11:26 PDT 1993 | — | 94 |
| **Slayer** | **1994-08-16** | Tue May 10 21:49:54 PDT 1994 | v 1.16, 1994/04/05 | **116** |
| Super Street Fighter II Turbo | 1995-01-10 | Tue May 10 21:49:54 PDT 1994 | v 1.16, 1994/04/05 | 116 |
| Wolfenstein 3D | 1995-09-06 | — | v 1.27, 1994/08/06 | 126 |

**A four-point ordering of SDK revisions, measured from the discs**, which the
platform notes have never had — and the pressing dates that order it come from
[11](11-a-date-in-128-bytes.md) rather than from copyright lines.

The correction that ordering forces: **Slayer was pressed 147 days before Super
Street Fighter II Turbo**, not after or alongside it. Both froze on the same
SDK build in May 1994; one shipped in August and one in January. The 116-file
`/System` is the same 116 files at both dates, which says the licensee kit did
not move between them — and the sixty-eight bytes say one thing in it did.

## The one thing this comparison cannot do

It cannot say which disc's `CPORT49.ROM` is the original. Both carry the same
folio stamp; the driver is not stamped. The pressing dates make Slayer the
earlier of the two, and Slayer is the one with the debug print, which is
consistent with removal rather than addition — **one data point, offered as
one.**

## What was pointed at a neighbour for the first time

`sdkdiff.py` was written two discs ago and had never been aimed at another
object's `/System`. Pointing it there produced the 115-of-116, in one command,
in about a second.

**That is the fourth session in five where the largest cross-object result came
from the cheapest tool in the box, used in a direction nobody had tried.** It
happened twice more inside this session: `ccbread.py census` on a directory
([06](06-the-container.md)) and `romtags.py`'s four-disc comparison
([11](11-a-date-in-128-bytes.md)), neither of which needed anything that did
not already exist.

The prescription that follows is not "write more tools". It is: **before
writing one, run every tool you have against every object you have.** The
inventory is 445 files and this session used about thirty of them.
