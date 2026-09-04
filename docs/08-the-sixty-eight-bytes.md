# 08 — the sixty-eight bytes: two operating systems, one difference, and it is a debug print

*Measure: the only file in 116 that differs between this disc's copy of
Portfolio OS and its twin's, located to the instruction and read.*

## The setup

```
python tools/sdkdiff.py _work/files ../3do-superstreetfighter2turbo-doc/_work/files
```

```
A = Slayer   116 files, 487,653 bytes
B = SSF2T    116 files, 487,585 bytes

identical (byte for byte) : 115
present on both, changed  :   1
only on A (removed)       :   0
only on B (added)         :   0

  Drivers/CPORT49.ROM     1,400 -> 1,332     -68 bytes
```

Two games, two publishers, two studios with no reason to have spoken to each
other — an AD&D dungeon crawler and a Capcom arcade port — and **their copies
of the console's operating system differ by sixty-eight bytes in one serial
driver.** The rest of that comparison is [chapter 12](12-against-the-collection.md).
This chapter reads the sixty-eight.

## Where they are

**Not in one contiguous deleted run.** The two files share a common prefix of
**three bytes** and a common suffix of **zero**, because the length is stored
at offset +4 and the last 64 bytes are a per-file signature; everything between
is shifted.

Aligning on the code instead:

```
Slayer                                SSF2T
  e5 d1 10 1d   LDRB r1,[r1,#0x1d]      e5 d1 10 1d
  e5 c0 10 13   STRB r1,[r0,#0x13]      e5 c0 10 13
  e5 d0 30 13   LDRB r3,[r0,#0x13]      -
  e5 d0 20 12   LDRB r2,[r0,#0x12]      -
  e5 d0 10 11   LDRB r1,[r0,#0x11]      -
  e2 8f 0f 01   ADD  r0,pc,#4           -
  ef 01 00 0e   SWI  &01000e            -
  e1 a0 f0 0e   MOV  pc,lr              e1 a0 f0 0e   MOV pc,lr
  "Stamped event pod %d position %d generic %d\n\0"   -
  00 00 00 00                           -
  e1 a0 c0 0d   MOV  r12,r13            e1 a0 c0 0d
```

**Five instructions and a format string.**

```
  5 instructions x 4 bytes            = 20
  "Stamped event pod %d position %d generic %d\n" + NUL  = 44
  one zero word of padding            =  4
                                      ----
                                        68
```

**The sixty-eight bytes are one `kprintf` call.** Three `LDRB`s load the
arguments out of the structure the function has just written — bytes at +0x11,
+0x12 and +0x13, which are the three `%d`s in order — `ADD r0,pc,#4` points at
the format string sitting immediately past the `MOV pc,lr`, and `SWI &01000e`
is a kernel call. The function then returns as it did before.

`printable runs >= 5` over each file:

```
Slayer : ['Stamped event pod %d position %d generic %d', 'jtJ|V', 'Uy\hY']
SSF2T  : []
```

The last two are inside the 64-byte signature and are noise. **Slayer's copy of
this driver is the only file in either `/System` tree that contains a sentence,
and the sentence is a developer's trace.**

## Which one is the odd one out

The instinct is that Slayer's copy is the debug build and the twin's is clean.
This chapter will not say that, for a reason the bytes give:

**the two files are separate compilations, not one file with a block cut out.**
The function *after* the trace differs in register allocation:

```
Slayer  e9 2d d8 70   STMDB r13!,{r4,r5,r6,r11,r12,lr,pc}   then r6, r4, r5
SSF2T   e9 2d d8 30   STMDB r13!,{r4,r5,r11,r12,lr,pc}      then r5, r3, r4
```

One register apart, all the way down, with identical structure. A tool that
patched out a `kprintf` would not have renumbered the registers of the next
function; **a compiler recompiling the same source with one statement more or
less would.**

So what is measured is: one of these two drivers was built from a source file
that had a debug statement in it and the other from one that did not, and the
two builds were made separately. **Which came first is not in the bytes.** Both
discs carry the identical `operamath.dev 21.10.603 05/10/94 21:49:54 stan
port1_3` stamp, so the *folio* build is the same to the second; the driver was
built on its own schedule and this comparison cannot order it.

`/rom_tags` can, and it says Slayer was pressed on **1994-08-16** and Super
Street Fighter II Turbo on **1995-01-10**, 147 days later
([11](11-a-date-in-128-bytes.md)). **The disc with the debug trace is the
earlier one.** That is a consistent story and it is one data point; it is
offered as such and not as a rule.

## What it is not

It is not a difference between the two games. Neither studio wrote this file —
it is `/System/Drivers/CPORT49.ROM`, a 3DO serial-port driver, shipped in the
licensee kit, and the 115 files around it are byte-identical. **Two studios
received two builds of one driver from the same vendor, four months apart, and
pressed them without looking.**

It is not a bug either: a `kprintf` on an event-pod path is exactly the kind of
line that gets left in a driver nobody expects a customer to see the console
output of. The 3DO has no console for it to print to in a retail unit.

## Why this is the smallest useful diff this collection has

Two shipped consumer products, from unrelated developers, whose shared
operating system differs by **one function's worth of source**. Every other
cross-object comparison in this collection is between versions of the same
thing or between things with nothing in common. This one is neither: it is two
independent recipients of one vendor's binary, and the delta is legible in its
entirety in eleven lines of ARM.

The other three neighbours, for scale:

| against | identical | changed | removed | added |
|---|---|---|---|---|
| **Super Street Fighter II Turbo** | **115** | **1** | **0** | **0** |
| Wolfenstein 3D | 36 | 51 | 29 | 39 |
| Crash 'n Burn | 25 | 67 | 24 | 2 |
