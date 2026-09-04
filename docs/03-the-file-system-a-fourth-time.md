# 03 — the file system, a fourth time: two numbers for one label, and the answer was next door

*Measure: the Opera volume header field by field, the seven root copies where
they actually sit, and the reconciliation of a 132 that a neighbour had already
published.*

## The label, byte by byte

Sector 0 of the track carries the volume label, and `opera.py --label` prints
it. Here it is against the raw bytes, which is the only way to settle what
follows:

```
rec_type 1   sync b'ZZZZZ'   version 1   flags 0
+0x08  comment  32 bytes, all zero
+0x28  label    32 bytes, 'CD-ROM' then zeros
+0x48  identifier      155,699,688  (0x0947C9E8)
+0x4c  block size            2,048
+0x50  block count         151,040
+0x54  root dir id     906,723,034
+0x58  root dir blocks           1
+0x5c  root dir block size   2,048
+0x60  last_root_copy            6
+0x64  the copy array: 74605 74606 74607 74608 134219 134220 134221
+0x80  00 00 00 00
+0x84  'duckiamaduck...'
```

Seven entries, because `last_root_copy` is **6**. All seven blocks are
byte-identical.

## The two lengths, and neither tool is broken

The session brief handed this over as an unreconciled contradiction: `--list`
reports `/Disc label` at **132 bytes**, `--label` computes **128**, same tool,
same disc. It is not a contradiction and it is not new.

- **128 is the record's own arithmetic.** `100 + 4 × (last_root_copy + 1)` =
  100 + 28. The tool is right; its docstring's 132 is the *directory entry* of
  the first disc it read, quoted next to the formula and easy to misread as
  the formula's output. Every one of the four discs has seven copies, so no
  disc has ever made the formula produce 132.
- **132 is on the disc.** It is the `byte_count` of the directory entry for
  `/Disc label`, an independent field written by the mastering tool, and the
  fill physically begins at +132 with `duck`. The four bytes between are a zero
  `u32` at +128 — an eighth, unused slot.

**Two fields, two definitions, four bytes apart, and both are correct about
different things.**

**And the third disc already published exactly this.** `3do-wolfenstein3d-doc`'s
scoring chapter carries, at 1.0:

> **C03** — the label record is 132 bytes, the word at +128 is zero, the fill
> starts at +132 with `duck`

Every clause of that reproduces here on the fourth disc. **The pre-briefing
that opened this session presented as an open question a thing a neighbouring
repository had answered and scored**, and this session's own prediction C04 bet
a wrong mechanism on it — that the array had eight slots and `--label` was
dropping one — instead of reading the neighbour first. Both are in
[15](15-corrections.md).

That makes it **`[4 of 4]`**: the label record is 132 bytes as a file and
`100 + 4 × (last_root_copy + 1)` as a record, on every 3DO disc measured.

## Where the seven copies are, and the first run is explained

```
copies  74605 74606 74607 74608   134219 134220 134221
gaps        1     1     1  59611       1     1
```

Two runs, of four and three. The three earlier discs found seven copies in
three layouts -- 5 + 2, 7 + 0 and 6 + 1 -- and published *"three discs, three
layouts, no rule"*. **This is a fourth layout, 4 + 3, and the count of seven is
`[4 of 4]`.** Four discs, four layouts, still no rule: the count survives a
fourth point and the arrangement is refuted a fourth time.

The placement is not arbitrary, and here the previous sessions' "no arithmetic
relates them" is **half wrong**:

```
/LaunchMe     blocks  74,291 .. 74,437   147 blocks
/System       block   74,438              the directory, 1 block
/data         blocks  74,439 .. 74,440    the directory, 2 blocks
/signatures   blocks  74,441 .. 74,604   164 blocks
root copies   blocks  74,605 .. 74,608   <- the block after /signatures ends
```

**The first run begins at the block immediately after the signature block
ends.** That is an arithmetic relation and it holds to the block, with nothing
skipped: `/LaunchMe`, the two directory blocks, `/signatures` and the first four
root copies are **one contiguous run of 318 blocks, 74,291 through 74,608**,
which is what a mastering tool laying out the bootable head of a disc
produces.

**The second run is not explained.** The last file byte on the disc is in block
134,199; the second run sits at 134,219, nineteen blocks later, and the
`iamaduck` fill begins at 134,222 and runs to 151,039. No arithmetic this
session will accept relates 134,219 to 74,605, to 151,040, to 151,340 or to
half of any of them: the gap is 59,614, the halves are 75,670 and 75,520, and
nothing lands. **Published as three offsets and an admission**, which is what
the third disc did with its own.

## The directory tree

582 files in 24 directories. The shape is a game's and not a platform's:

```
/                       11 files        the boot binary, the label, rom_tags,
                                        signatures, AppStartup
/System                116 files        Portfolio OS -- and NOT this game's
/data                   27 files   52,461,370   the three films, the ARM
                                        utilities, the logo cels, the fonts
/data/walls            207 files    1,367,820   the dungeon's surfaces
/data/monsters          43 files    7,157,896   one animation per creature
/data/items             70 files      619,948
/data/interface         21 files      351,436
/data/spells            13 files      188,424
/data/sounds/music      19 files  206,652,152   66.674 % of the pressing
/data/sounds/growls     43 files    2,014,296   one voice per creature
/data/sounds/squeals     8 files      139,198
/data/sounds            10 files      138,798   the named effects
```

**Forty-three monsters and forty-three growls**, one animation and one voice
each, and thirty-nine distinct recordings among the voices. The directory
structure is the bestiary twice over.

**`/System` is a control chosen inside the object**, and every statistic in this
repository that mixes it with `/data` says so. Of the 41 ARM images, 38 are
3DO's; of the 144 files `aiffread.py` opens, 63 are 3DO's DSP patches and are
not audio. See [07](07-forty-one-binaries.md) and
[09](09-a-soundtrack-uncompressed.md).

## Nine files stored twice

573 distinct SHA-1 over 582 files; 223,455 bytes stored more than once, in
seven groups.

```
python tools/hashall.py _work/files
```

| copies | bytes | files |
|---|---|---|
| 2 | 62,220 | `growls/Mind Flayer.aiff` = `growls/Sword Wraith.aiff` |
| 2 | 56,804 | `growls/Carrion Crawler.aiff` = `growls/Purple Worm.aiff` |
| 2 | 52,748 | `growls/Gelatinous Cube.aiff` = `growls/Slime.aiff` |
| 2 | 43,276 | `growls/Ghost.aiff` = `growls/Shade.aiff` |
| 2 | 6,208 | `/data/ViewChar.anim` = `/data/interface/ViewChar.anim` |
| 2 | 2,196 | `walls/Ceiling7.celB` = `walls/T3Ceiling.celB` |
| 4 | 1 | `System/{Daemons,Devices,Drivers,Graphics/Fonts}/junk` |

**The bestiary is 43 named creatures and — after the two tests a hash cannot
run — 36 recordings.** Eight monsters share four voices byte for byte, and the pairings are semantic rather than
alphabetical: a Mind Flayer and a Sword Wraith, a Carrion Crawler and a Purple
Worm, a Gelatinous Cube and a Slime, a Ghost and a Shade. Somebody chose which
creatures could sound the same. **Three more pairs are the same recording and
the hash cannot see them** -- see [09](09-a-soundtrack-uncompressed.md).

**The four `junk` files are one byte, and the byte is `0x0d`** — a carriage
return. They belong to `/System`, so the CR is 3DO's Macintosh-hosted toolchain
and not this studio's; the distinction matters and
[11](11-a-date-in-128-bytes.md) uses it.
