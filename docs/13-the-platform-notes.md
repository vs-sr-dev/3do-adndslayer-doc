# 13 — the platform notes: what a fourth disc owes a checklist whose first rule is against it

*Measure: which of the running 3DO checklist's marks this disc touches, in
which direction — written into that repository, committed and pushed.*

## The rule this chapter is under

`3do-platformnotes-doc/3do-platform-notes.md` was 1,943 lines and covered three
discs when this session opened it. Its opening rule is aimed squarely at a session in this position:

> **A mark is never promoted because nothing contradicted it.** With three discs
> that temptation is at its worst: every line a disc did not touch looks
> confirmed twice over. It is not. **The third disc broke six claims that were
> marked `[2 of 2]`**, and every one of the six had gone uncontradicted for
> fourteen months.

Its reconciliation before this disc: `[3 of 3]` 12, `[2 of 3]` 2, `[1 of 3]` 11,
`[2 of 2]` 41, `[1 of 2]` 10, `[1 of 1]` 14, `[corrected]` 18, `[deleted]` 3,
`[unverified]` 4, `[verified]` 1.

**Forty-one `[2 of 2]` marks are rules invented out of two points.** A fourth
disc's job is not to confirm them.

## The decision, and it was not this session's to make

The session brief said to produce the text and **not** to write it into that
repository, because the previous two sessions had edited their neighbours'
repositories unasked and it is on both their corrections lists.

**The owner of the repository overruled that, in the middle of the session, and
said to edit and push it directly** — *"è come lavoravano le altre pipeline"*.
So it was edited and pushed, as commit
[`252aae0`](https://github.com/vs-sr-dev/3do-platformnotes-doc/commit/252aae0),
**+433 lines, −90**, and the notes now say they cover four discs. What follows
is the same content as a summary of what changed there.

**Nothing was promoted for silence.** Every line below names a claim this disc
actually touched. Thirty-eight `[2 of 2]` marks this disc did not exercise —
`IMAG`, `BRGR`, the banner screen, `.PAL`, ProTracker, a second track — are
still `[2 of 2]`.

## And the notes already knew two things this session found

**This is the chapter's most useful sentence and it is against the session.**
Two of the results written up in these documents as findings were already
published in that file before this disc was opened:

- **the 132-byte volume label**, its zero word at +128 and the fill starting at
  +132 with `duck` — `[2 of 2]` in its §2, and reproduced as
  [03](03-the-file-system-a-fourth-time.md);
- **the `/rom_tags` `0x0c` date and the 1904 epoch** — `[1 of 1]` in its §4,
  with a *better* argument for the epoch than this session's, and an open
  question asking a fourth disc for exactly the point this disc supplies. See
  [11](11-a-date-in-128-bytes.md).

A third came close: the notes record that **the 1993 disc's `junk` byte is
`0x0a` and the later discs' is `0x0d`**, which this session predicted wrongly
(C30) as `0x0a` while measuring `0x0d`.

**Three of this session's results were available for the price of reading one
file first.** That is rule 6 of the brief — *when you quote a figure from
another repository take it from its `docs\`, not from your head* — failing in
its worst form, because what was not read was not a figure but three findings.
It is in [15](15-corrections.md) and it is the session's largest process error.

## Confirmations, and each one is a fourth point

**`[4 of 4]` `iamaduck` mastering fill.** Present, exact string, 17,729 sectors
= 11.7147 % here. `python tools/sectormap3do.py _work/slayer.bin`.

**`[4 of 4]` `/signatures` is 335,872 bytes.** To the byte, on four discs, with
four different SHA-1 and four different non-zero counts (330,596 here). 164
blocks; 164 is not a power of two.

**`[4 of 4]` seven root-directory copies.** Seventh on every disc measured.

**`[4 of 4]` the volume label is 132 bytes as a directory entry and
`100 + 4 × (last_root_copy + 1)` as a record**, with a zero `u32` at +128 and
the fill starting at +132 with `duck`. This is the third disc's `C03` holding a
fourth time; see [03](03-the-file-system-a-fourth-time.md), where it also
answers a question this session's own briefing had reopened.

**`[4 of 4]` the ARM Image header identity, five of its six parts.** `SWI &11`
at 0x10, entry point 0x100, flags 32, image base 0, debug size 0 — **41 of 41**.

**`[4 of 4]` the `CCB ` chunk is 80 bytes** and the two independent encodings of
width and height agree — **370 of 370** here.

**`[4 of 4]` zero sectors owned by nothing and zero double-claimed**, first
pass, `sectormap3do.py`.

## Breaks, and there are four

**BREAK — no audio track.** This is the first of the four discs with **zero**
`TRACK … TYPE:AUDIO`. Whatever the notes say about Red Book on a 3DO disc goes
to `[3 of 4]` at best. `chdman.exe info -i "Slayer (USA).chd"`.

**BREAK — the root-copy layout is a fourth arrangement.** 5 + 2, 7 + 0, 6 + 1
and now **4 + 3**. Four discs, four layouts, no rule; the count of seven
survives and the arrangement does not.
**And a new positive that supersedes the old "no arithmetic relates them":**
on this disc the first run begins at the block immediately after `/signatures`
ends, and **both `iamaduck` regions begin at the block immediately after a
root-copy run**. Whether that holds backwards on the other three is a
re-measurement this session did not make. **It is offered as a question, not a
mark.**

**BREAK — the relocation-target identity, and now with a side.** `ro + rw`
holds on 39 of 41, and the two exceptions are **`/LaunchMe` and
`/data/StorageTuner`** — this game's own binaries. 3DO's thirty-eight images:
38 of 38. The studio's three: 1 of 3. The third disc broke this rule; **the
fourth says which half of the disc breaks it.**

**BREAK — `iamaduck` occupies one region, or two, depending on the disc.** The
second disc's *"one free region because the mastering tool appends"* was
already refuted by the third; this disc has two regions of 911 and 16,818
sectors. The fraction is not a rule either: 7.93 %, 11.51 %, 11.71 %, 23.60 %.

## Additions, and what is genuinely new in each

**`/rom_tags`, which the notes already derived as a table of 32-byte records.**
Three things are new:

- **type `0x02` is the application, addressed by BLOCK.** Field A is a first
  block and field B a length in blocks, and it equals the boot binary's own
  directory entry on **3 of the 3 discs that carry the record**. Crash 'n Burn
  has no `0x02` at all. **The console does not read the filename**, which is why
  four discs spell it `LaunchMe`, `Launchme`, `launchme` and `launchme` without
  consequence — and it **corrects** the notes' standing explanation, which was
  that case folding in the directory is what starts the game;
- **types `0x07` and `0x10` carry a kernel file's size.** `0x07`'s field B
  equals `/System/Kernel/os_code` on **4 of 4** discs — 78,852, 85,896, 85,896
  and 115,520 — and `0x10`'s equals `/System/Kernel/misc_code` on **3 of 3**
  that carry it. `0x0d` is *not* the same thing for `boot_code`: it matches on
  one disc of four;
- **the declared length of `/rom_tags` is not the number of records in its
  block.** This disc's entry says 128 bytes and the block holds **192 — six
  records**, the last two past the declared end where `opera.py --extract` will
  never write them. The twin does the same. The notes had recorded types `0x10`
  and `0x05` as *"third disc only"*; they are on three of four, and only the
  third declares them.

**The `0x0c` date is NOT new** — see the section above — and what this disc
adds to it is the fourth point, the fourth positive gap against a fourth SDK
stamp, and `romtags.py --epochs`.

**THE DRIVER ROM HEADER, of which the notes already had two thirds.** They
record that every `.ROM` declares its own length and that a **512-bit
signature** sits past that length. What is new is small: the `0xdead****` word
at +0 and `0xdea?****` at +16, and the constant pair `0x0000012c` `0xffffffff`
immediately before the signature, on 6 of 6. See [05](05-the-boot-chain.md).

**THE `ANIM` / `CCB ` CONTAINER.** IFF-style, big-endian, four printable
characters plus a `u32` length including the header. **370 containers close at
residue zero, 370 of 370**; 3,782 chunks; tags `ANIM`, `CCB `, `PLUT`, `XTRA`,
`PDAT`, `CTPT`. **One `CCB ` per container and one `PDAT` per frame**; 2,516
frames, **2,516 of 2,516 render**. `ANIM` word 2 is the frame count on 159 of
180 and is **not named**. See [06](06-the-container.md) and
`tools/animwalk.py`.

**THE SDK CHRONOLOGY, WITH PRESSING DATES.** The `operamath` and `STARTOPERA`
stamps date the *toolchain*; the `0x0c` record dates the *pressing*. Both, for
four discs, are in [12](12-against-the-collection.md). The correction it forces:
**Slayer was pressed before Super Street Fighter II Turbo, not after.**

## The questions this disc raises and cannot answer

1. **do both `iamaduck` regions follow a root-copy run on the other three
   discs?** One command each, three discs, and it turns a coincidence into a
   `[4 of 4]` or kills it;
2. **is the relocation-target exception always the title's own binaries?**
   Wolfenstein 3D broke the rule first; nobody asked which images;
3. **does the `0x0c` date exist on 3DO discs outside this collection**, and
   does it order them correctly against their known release dates? Four points
   is four points;
4. **what are `/rom_tags` types `0x05`, `0x07`, `0x0d` and `0x10`?** `0x07`'s
   field B here is 85,896, which is exactly the size of
   `/System/Kernel/os_code` — one coincidence on one disc, deliberately not
   promoted.

## And three corrections owed elsewhere, still owed

`pc-linksthechallengeofgolf-doc` has three corrections produced two sessions
ago and not applied: four of its six executables are Microsoft EXEPACK images,
a chapter-07 claim resting on an untested premise, and the Christmas Eve mtime
pairing. **They are not this object's business, this session did not touch that
repository, and they are still owed.**
