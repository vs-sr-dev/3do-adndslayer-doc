# 05 — the boot chain: the console does not read the filename, and that is why nobody noticed it was wrong

*Measure: what the console reads between power-on and the first frame, derived
from the disc's own 128-byte table and checked against the file system's
directory entry on three discs.*

## `/AppStartup`, all 160 bytes of it

The pre-briefing handed over a discrepancy: `/AppStartup` says the system will
start `$boot/Launchme`, and the file on the disc is `/LaunchMe`. **A case
mismatch between a shipped script and a shipped filename, in the object's own
boot path.**

Here is the whole file:

```
b'#\r#  This is the application startup script\r#\r#  This script should
  contain your aliases\r#\r#  After this script is run, the system will
  start $boot/Launchme\r#\r\r'
```

**Every line begins with `#`. There are zero executable lines.** The sentence
that names `Launchme` is prose about what the system will do next, not an
instruction the shell runs, and the file's own second and fourth lines say what
it is *for* — aliases — and it contains none. **There is no case mismatch in
the boot path, because that sentence is not in the boot path.**

It is also not this game's file. `crossall.py` finds `/AppStartup`'s SHA-1
`45083d038615ab40a21d15c2718498bd91052eae` in `3do-superstreetfighter2turbo-doc`
as well: **the two studios shipped the same 160 bytes of commented-out
boilerplate**, along with 115 of the 116 files in `/System`
([12](12-against-the-collection.md)).

And the line endings are `\r` and only `\r` — **Macintosh**, which is the first
of four traces of a Mac-hosted toolchain that this disc carries and
[11](11-a-date-in-128-bytes.md) needs.

## `/rom_tags`: 128 bytes, four records, and the one that matters

```
python tools/romtags.py _work/files/rom_tags --app notes/listing.txt
```

```
  0  type 0x0d  sub 0x0000   A          1        B       5168
  1  type 0x07  sub 0x0010   A          5        B      85896
  2  type 0x0c  sub 0x0000   A 2859874196        B          0
  3  type 0x02  sub 0x0000   A      74291        B        147
```

Four 32-byte records. Every record begins `0x0f`; bytes +16 to +31 are zero on
every record of every disc measured, 20 of 20.

**Record type `0x02` is the application, and it names it by BLOCK.** Field A is
a first block and field B a length in blocks, and against the file system's own
directory entry:

```
  0x02 says block 74291, 147 blocks
  the listing's file at that block with that length: /LaunchMe
```

**It closes exactly.** And it closes on the neighbours too, which is what makes
it a derivation and not a coincidence of two numbers on one disc:

| disc | record `0x02` | the file at that block |
|---|---|---|
| Slayer | 74,291 / 147 | **`/LaunchMe`** |
| Super Street Fighter II Turbo | 139,161 / 166 | **`/Launchme`** |
| Wolfenstein 3D | 42,713 / 47 | **`/launchme`** |
| Crash 'n Burn | *no `0x02` record* | `/launchme` at 179,520 |

**Three discs, three different spellings of the same filename, one identity
that closes on all three.** `LaunchMe`, `Launchme`, `launchme` — and the fourth
disc, the launch title, spells it `launchme` and carries no `0x02` record at
all.

That is the answer to `/AppStartup`. **The console never looks up a name.** It
reads block 1, finds the `0x02` record, and jumps to a block number. The
filename could be anything, and across four discs from four studios it very
nearly is. A comment that spells it `Launchme` while the file says `LaunchMe`
costs nothing because nothing in the chain compares the two.

**Crash 'n Burn having no `0x02` record is the interesting half.** Three records
on the launch title, four here and on the twin, six on the 1995 disc — see
[11](11-a-date-in-128-bytes.md), where the same table dates them.

## The other three records, printed and not named

`0x0d` (A = 1, B = 5,168), `0x07` (sub `0x0010`, A = 5, B = 85,896) and, on
Wolfenstein 3D only, `0x05` and `0x10`. `0x07`'s B of 85,896 is exactly the
size of `/System/Kernel/os_code`, which is suggestive and is not enough: one
coincidence on one disc is not a field assignment, and this session declines to
name it. `romtags.py` prints all of them.

## `/signatures`: 335,872 bytes on four discs of four

| disc | bytes | SHA-1 | non-zero bytes |
|---|---|---|---|
| Crash 'n Burn | 335,872 | `4357a31a…` | 330,536 |
| **Slayer** | **335,872** | `6c08ea0c…` | **330,596** |
| Super Street Fighter II Turbo | 335,872 | `bac1d1ef…` | 331,084 |
| Wolfenstein 3D | 335,872 | `23c2c338…` | 334,500 |

**`[4 of 4]` on the size, to the byte, and `[4 of 4]` on the contents
differing.** 335,872 is 164 blocks exactly, and **164 is not a power of two**,
so the constant is somebody's decision and not the round end of a padded
buffer. Four discs, four studios, two years apart end to end, one size.

This repository reads none of it. Its size, its block count, its non-zero count
and its position are measured; **its content is not decoded and is not
guessed**, and it is on the refusals list in [14](14-what-is-not-here.md).

What can be said is what it is *for*, from the shape of everything around it:
the 3DO required discs to be signed, and 164 blocks of high-entropy data sat
between the boot binary and the root-directory copies on every disc pressed.
[03](03-the-file-system-a-fourth-time.md) shows the four root copies beginning
at the block immediately after it ends.

## `/rom_tags` declares 128 bytes and the block holds 192

The directory entry says 128 bytes, so `opera.py --extract` writes 128 bytes,
so the four records above are all any tool in this pipeline has ever seen on
this disc. **The block holds six.**

```
python -c "...read sector 1's user data..."
  +  0 type 0x0d  A          1  B       5168
  + 32 type 0x07  A          5  B      85896
  + 64 type 0x0c  A 2859874196  B          0
  + 96 type 0x02  A      74291  B        147
  +128 type 0x10  A         69  B       2912   <- past the declared end
  +160 type 0x05  A      74440  B     155648   <- past the declared end
  +224 sixty-four bytes of high-entropy data, different in the two copies
```

**Two records — `0x10` and `0x05` — lie past the declared length**, and the
platform notes record them as *"third disc only"* because the third disc's
`/rom_tags` declares 192 bytes and this one and the twin's declare 128. **They
are on all three; only the byte count differs.** Super Street Fighter II Turbo's
block has the same six records at the same offsets.

Two of the four field-B values are file sizes, and they close exactly:

| record | field B | equals |
|---|---|---|
| `0x07` | 85,896 | **`/System/Kernel/os_code`**, 85,896 B — and on **4 of 4** discs |
| `0x10` | 2,912 | **`/System/Kernel/misc_code`**, 2,912 B — on **2 of 2** that carry it |
| `0x0d` | 5,168 | `/System/Kernel/boot_code` is 5,050 — **1 of 4**, and not adopted |
| `0x05` | 155,648 | not named |

`0x07` against `os_code`: 85,896 here and on the twin, 115,520 on Wolfenstein
3D, 78,852 on Crash 'n Burn — **four discs, four sizes, four exact matches.**
`0x0d` against `boot_code` matches on Crash 'n Burn alone (2,076) and misses by
+118, +118 and −1,744 on the others, so it is **described and not named**.

Record `0x05`'s field A is one less than `/signatures`' first block on **three
of three** discs that carry it: 74,440 against 74,441 here, 139,344 against
139,345 on the twin, 42,766 against 42,767 on Wolfenstein 3D. That is an
identity with an off-by-one in it, which is exactly the shape a "last block
before" field has, and it is reported as the arithmetic rather than as a name.

## The six driver ROMs, and half of this was already written down

`/System/Drivers` holds six files with a `.ROM` or `.rom` extension, 7,180
bytes in total, and **none of them is an ARM Image**: `aifcensus.py` counts 41
AIF images on this disc and not one is a driver.

**Two of the three parts below were already in the platform notes** and are
re-derived here rather than found: that *"every `.ROM` declares its own
length"*, and that a **512-bit signature** sits at the end past that length.
This session read the notes after measuring, which is the wrong order and is in
[15](15-corrections.md). What is new is only the two `0xdea?` tag words and the
constant `0x0000012c` before the signature.

The shape:

```
  +0   u32  0xdead**** -- a magic and a 16-bit value that differs per file
  +4   u32  the file's length in bytes        <- 6 of 6, exactly
  +8   u32  zero
  +12  u32  zero
  +16  u32  0xdea?**** -- a second tagged word
  ...  ARM code
  -72  u32  0x0000012c = 300                  <- 6 of 6
  -68  u32  0xffffffff                        <- 6 of 6
  -64  64 bytes of high-entropy data          <- 6 of 6
```

| file | bytes | word 0 | length at +4 | word 4 |
|---|---|---|---|---|
| `BLINK.ROM` | 900 | `dead99bb` | 900 | `deac941c` |
| `CPORT1.ROM` | 1,708 | `dead99e3` | 1,708 | `deaf3f05` |
| `CPORT41.ROM` | 1,084 | `dead96eb` | 1,084 | `deacead6` |
| `CPORT49.ROM` | 1,400 | `dead9887` | 1,400 | `deac500a` |
| `CPORT4D.ROM` | 1,392 | `dead99a4` | 1,392 | `deafb795` |
| `hello.rom` | 696 | `dead9975` | 696 | `dead6a58` |

**The length field at +4 equals the file's actual length on six of six** —
which is the platform notes' claim, re-derived on a fourth disc and now
`[3 of 3]` on the discs that have drivers. The two `0xdea?` words are **not
named**: their low halves do not reproduce as any checksum this session tried
over any obvious range, and a word that looks like a checksum and is not one is
worse than an unnamed word.

The 64 bytes at the end are the 512-bit signature the notes already identified;
what this disc adds is that they are preceded on 6 of 6 by the constant pair
`0x0000012c` and `0xffffffff`. The same 64-byte shape sits at **+224 of the
`/rom_tags` block**, differing between that file's two copies, which is the
notes' own `[2 of 2]` observation holding a third time.

`CPORT49.ROM` is the one file in all of `/System` that differs from the twin
disc's, and it has [its own chapter](08-the-sixty-eight-bytes.md).
