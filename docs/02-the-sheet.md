# 02 — the sheet: every figure with the command that remakes it

*Measure: the object's numbers, one to a line, each beside the command that
produces it, so that nothing in this repository has to be taken on trust.*

Commands are run from the repository root with `_work/` built by the two
extraction steps at the top. `chdman.exe` lives in `3do-platformnotes-doc/bin/`.

## The container

| figure | value | command |
|---|---|---|
| CHD file | 200,769,302 B | `chdman.exe info -i "Slayer (USA).chd"` |
| CHD SHA-1 (header) | `13e835442a6a82458759293e8e2073526be45c3e` | as above |
| data SHA-1 | `75c1b50db7795c400f78a6adc8e2c822860ca9d1` | as above |
| the file's own SHA-1 | `126b1dcc03007b1482cd9583edb2c2754cb5effa` | `python -c "import hashlib;..."` |
| version | 5 | `chdman.exe info` |
| logical size | 370,480,320 B | `chdman.exe info` |
| hunk / unit | 19,584 / 2,448 B | `chdman.exe info` |
| hunks / units | 18,918 / 151,340 | `chdman.exe info` |
| compressors | `cdlz` `cdzl` `cdfl` | `chdman.exe info` |
| ratio | 54.2 % | `chdman.exe info` |
| tracks | **one**, `MODE1_RAW`, `SUBTYPE:NONE`, `PREGAP:0` | `chdman.exe info` |
| **audio tracks** | **zero** | `chdman.exe info` |
| extracted | 355,951,680 B = 151,340 × 2,352 | `chdman.exe extractcd -i ... -ob _work/slayer.bin` |

## The pressing

| figure | value | command |
|---|---|---|
| sectors | 151,340 | `python tools/sectormap3do.py _work/slayer.bin` |
| user area (**the denominator**) | 309,944,320 B | 151,340 × 2,048 |
| share of a 74-minute CD | **45.4474 %** | 151,340 / 333,000 |
| blocks the label declares | 151,040 | `python tools/opera.py _work/slayer.bin --label` |
| sectors past the declared volume | **300**, all zero, contiguous at 151,040–151,339 | `sectormap3do.py` |
| `iamaduck` mastering fill | 17,729 sectors = **11.7147 %** | `sectormap3do.py` |
| sectors owned by nothing and not fill | **0** | `sectormap3do.py` |
| double-claimed blocks | **0** | `sectormap3do.py` |

## The volume

| figure | value | command |
|---|---|---|
| label | `CD-ROM`, comment empty | `opera.py --label` |
| identifier | 155,699,688 = `0x0947C9E8` | `opera.py --label` |
| block size | 2,048 | `opera.py --label` |
| root directory | id 906,723,034, **1 block** | `opera.py --label` |
| `last_root_copy` field | **6**, so seven entries | `opera.py --label`, and the raw bytes at +0x60 |
| root copies | 74,605–74,608 and 134,219–134,221, all seven byte-identical | `opera.py --label` |
| label record, computed | **128 B** = 100 + 4 × 7 | `opera.py --label` |
| label record, as a directory entry | **132 B**, type `*lbl`, block 0, 2 copies | `opera.py --list` |
| the four bytes between them | a zero `u32` at +128; the fill starts at +132 with `duck` | raw dump of sector 0 |

## The file system

| figure | value | command |
|---|---|---|
| files / directories | **582 / 24** | `python tools/opera.py _work/slayer.bin --list` |
| bytes in files | 272,214,595 = 87.8269 % of the user area | `--list` |
| distinct SHA-1 | **573 of 582** | `python tools/hashall.py _work/files` |
| duplicate groups | 7, 223,455 B stored twice | `hashall.py` |
| unreadable | 0 | `--list` |
| ISO 9660 | **refused**: `descriptors : 0` | `python tools/iso9660.py _work/slayer.bin --vd` |

## The container this session opened

| figure | value | command |
|---|---|---|
| containers | **370** — 180 begin `ANIM`, 190 begin `CCB ` | `python tools/animwalk.py census _work/files` |
| closing at residue zero | **370 of 370** | as above |
| chunks | 3,782, tiling 11,586,376 B | as above |
| `PDAT` chunks (frames) | **2,516** | as above |
| frames that render | **2,516 of 2,516** | `python tools/animwalk.py frames _work/files --census` |
| `CCB ` chunk length | 80 B on 370 of 370 | `animwalk census` |
| width/height, two encodings | agree on **370 of 370** | `python tools/ccbread.py census _work/files` |
| `ANIM` word 2 == `PDAT` count | **159 of 180** | `animwalk census` |
| the 21 exceptions | all in `/data/walls`, all with one `PDAT` | `animwalk census` |
| negative controls | 7 refused, 1 positive control accepted | `python tools/animwalk.py validate` |

## The sound

| figure | value | command |
|---|---|---|
| AIFF files | **81** | `python tools/aiffread.py _work/files` |
| codec | **`NONE` on 81 of 81** | as above |
| sample data | 208,931,420 B | as above |
| running time | **22:30.04** | as above |
| container overhead | 22,392 B = 0.0107 % of the files | `thesis3do.py` |
| the thesis | **67.4093 %** of the user area | `python tools/thesis3do.py _work/files 151340 151040` |
| 44,100/16/stereo | 18 files, 204,749,780 B = **97.9986 %** of the sample data | derived from `aiffread.py`'s table |
| 22,050/8/mono | 59 files, 4,143,905 B | as above |
| 22,255/8/mono | **3 files** — the Macintosh rate, unresampled | as above |
| `.dsp` files | 63, **correctly refused**: *no COMM* | `aiffread.py` |
| SDX2 at 2:1 on the 16-bit material | would free **102,379,300 B** = 49,990 sectors | [09](09-a-soundtrack-uncompressed.md) |

## The films

| figure | value | command |
|---|---|---|
| `.stream` files | 3, 50,266,112 B | `opera.py --list` |
| `Intro.stream` | 280 × 160, rate field 15, **1,326 frames** | `python tools/cvidmovie.py ... --census` |
| `Credits.stream` | 280 × 160, rate field **12**, **1,224 frames** = 102.00 s | as above |
| `EndGame.stream` | 280 × 160, rate field 15, **833 frames** | as above |
| frames decoded | **3,383 of 3,383**, 0 overruns | as above |
| macroblocks accounted for | 2,800 per frame, on 3,383 of 3,383 | as above |
| credit screens | **17**, held a median 3.83 s each | [10](10-three-films-and-a-credit-roll.md) |

## The programs

| figure | value | command |
|---|---|---|
| ARM images | **41** | `python tools/aifcensus.py _work/files` |
| `SWI &11` at 0x10 / entry 0x100 / flags 32 / base 0 / debug 0 | **41 of 41** each | as above |
| reloc target == `ro + rw` | **39 of 41** | as above |
| the two exceptions | **`/LaunchMe` and `/data/StorageTuner`**, both `ro + rw + 4` | `aifcensus.py`, per-image rows |
| compressed images | 5 of 41, all in `/System` | as above |
| this game's binaries | 3: `/LaunchMe` 299,312 B, `/data/Player` 53,084, `/data/StorageTuner` 32,608 | as above |

## The boot chain

| figure | value | command |
|---|---|---|
| `/rom_tags` | 128 B at block 1, **four 32-byte records** | `python tools/romtags.py _work/files/rom_tags` |
| record `0x02` | block 74,291, 147 blocks = **`/LaunchMe` exactly** | `romtags.py --app notes/listing.txt` |
| record `0x0c` | `0xAA763794` → **1994-08-16 09:29:56** (1904 epoch) | `romtags.py --epochs` |
| `/AppStartup` | 160 B, `\r` line endings, **every line a comment** | `python -c` over the file |
| `/signatures` | 335,872 B, 164 blocks, 330,596 non-zero | `hashall.py`, `opera.py --list` |
| driver ROMs | 6, magic `dead**` + u32 length at +4, 72-byte trailer `0000012c ffffffff` + 64 B | raw dump |
| `CPORT49.ROM` vs the twin's | 1,400 vs 1,332 — **one `kprintf` and its format string** | [08](08-the-sixty-eight-bytes.md) |

## Against the collection

| figure | value | command |
|---|---|---|
| `/System` vs Super Street Fighter II Turbo | **115 identical of 116** | `python tools/sdkdiff.py _work/files ../3do-superstreetfighter2turbo-doc/_work/files` |
| vs Wolfenstein 3D | 36 identical, 51 changed, 29 removed, 39 added | as above |
| vs Crash 'n Burn | 25 identical, 67 changed, 24 removed, 2 added | as above |
| hash crossings | **114 of 573** | `python tools/crossall.py notes/sha1-all.txt --collection d:/Homebrew7 --skip 3do-adndslayer-doc` |
| by repository | SSF2T 141 lines, Wolfenstein 73, Crash 'n Burn 25, **PC repositories 0** | as above |
| collection denominator | **245 directories, 123 `*-doc`, 85 with a `notes\`** | a directory count over seven roots |

## The negative controls, which are measurements

| figure | value | command |
|---|---|---|
| copy-protection markers | **0** across 11 schemes; positive control fires on 575 files | `python tools/protscan.py --all-files _work/files` |
| `exepack.py` | **582 of 582 refused** | `find ... -print0 \| xargs -0 python tools/exepack.py --refuse` |
| `dosimage.py` | **582 of 582 refused** | `... --refuse-check` |
| `ppc.py` | 582 of 582 refused | `... --census` |
| `hsc.py` | 582 of 582 refused | `... ` |
| `pcspk.py`, `cga.py` | **no refusal path at all** — they "find" notes and CGA frames in an ARM binary | [14](14-what-is-not-here.md) |
| toolbox control scan | 445 files, 0 forbidden control bytes, all three positive controls fire | `python tools/toolscan.py tools .py` |
