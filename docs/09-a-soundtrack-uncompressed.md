# 09 — a soundtrack, uncompressed: two hundred megabytes for twenty-two minutes, and the codec was on the disc

*Measure: what fraction of this pressing is recorded sound, on the same
denominator the three neighbours used; what SDX2 would have cost; and what the
object itself says about why nobody ran it.*

## The number, and the number the brief handed over

```
python tools/thesis3do.py _work/files 151340 151040
```

**67.4093 %** of the user area is AIFF sample data: 208,931,420 bytes,
**22:30.04**, in **81 files, codec `NONE` on 81 of 81**.

The brief handed over **76.7607 %** and asked for it to go in the column beside
86.2465 %, 59.7896 % and 0.3230 %. It is a true number about a different
question — `.aiff` bytes as a share of *the bytes in files* — and the three
published figures are shares of *the user area*. **Nine and a third percentage
points, from a denominator nobody restated.** The tool prints all eight
readings so the choice is visible:

| | file bytes | SSND payload |
|---|---|---|
| logical bytes × 2,448 | 56.4008 % | 56.3947 % |
| bytes extracted × 2,352 | 58.7029 % | 58.6966 % |
| **user data in the track × 2,048** | 67.4166 % | **67.4093 %** |
| user data the volume declares × 2,048 | 67.5505 % | 67.5432 % |

The published figure is the SSND payload against the track's user data —
numerator *the sound*, not *the sound's packaging*. Container overhead is
22,392 bytes, 0.0107 % of the files, about 276 bytes a file.

| disc | pressed | recorded sound |
|---|---|---|
| Crash 'n Burn | 1993-09-09 | 0.3230 % |
| **Slayer** | **1994-08-16** | **67.4093 %** |
| Super Street Fighter II Turbo | 1995-01-10 | 86.2465 % |
| Wolfenstein 3D | 1995-09-06 | 59.7896 % |

## What it is, and the owner of this machine settled it

Nineteen files in `/data/sounds/music` hold **206,652,152 bytes — 66.674 % of
the whole pressing** — with names like `Atmosphere I`, `Scrolling V`,
`Combat III`, `Nightmare`, `Fanfare II`, `End Game`.

No measurement distinguishes twenty-two minutes of orchestral score from
twenty-two minutes of narration. **The owner of this machine listened and
reported:** the files in `/music` are all background music and each matches its
own filename — atmosphere and ambience pieces, combat pieces, a fanfare. He
also listened to the ten named effects in `/data/sounds` and reported that
`Buzzer`, `Click`, `DoorOpen`, `DoorClose`, `Impact`, `Launch`, `Spell`,
`Swish` and the two `Player … hit` files are, in his words, literally the sounds
their names describe. **Ten of ten filenames truthful.**

That is an observation, attributed to him, recorded in
`notes/owner-observations.txt`, and it is not a measurement. It is also the
only thing in this repository that connects a byte count to a sound, and
without it this chapter would have had to hedge its own title.

## The split, and why "the studio did not compress" needs qualifying

Not all eighty-one files are alike:

| rate / bits / channels | files | sample bytes | share of the sound |
|---|---|---|---|
| 44,100 / 16 / stereo | 18 | 204,749,780 | **97.9986 %** |
| 22,050 / 8 / mono | 59 | 4,143,905 | 1.9834 % |
| 22,255 / 8 / mono | 3 | 28,915 | 0.0138 % |
| 44,100 / 16 / mono | 1 | 8,820 | 0.0042 % |

**Sixty-two of the eighty-one files are 8-bit**, which is a 2:1 decision taken
in the sampler rather than in the codec — every growl, every squeal, every
door. This session predicted (C16) that the split would matter and that the 16-bit
files would hold more than 90 % of the bytes.

They hold **97.9986 %**, and that number **destroys the point the prediction
was making.** Yes, the effects were halved; the effects are two per cent of the
sound. The charge stands undiluted: **eighteen files of music, 195 megabytes,
44.1 kHz sixteen-bit stereo, uncompressed.** The arithmetic was right and the
argument it was built for was wrong, and that is written up in
[15](15-corrections.md).

## What SDX2 would have cost

SDX2 is the platform's own audio codec, **exactly 2:1**, proved on this
collection's second and third discs: it stores one byte per 16-bit sample, so
it halves 16-bit material and does nothing at all for 8-bit material.

| | bytes |
|---|---|
| 16-bit sample data | 204,758,600 |
| the same under SDX2 | 102,379,300 |
| **freed** | **102,379,300** |
| 8-bit sample data (SDX2 buys nothing) | 4,172,820 |

```
sectors freed                  49,990
disc after                    101,351 sectors = 30.4357 % of a 74-minute CD
audio share after                                        62.7517 %
file bytes after                                        169,835,295
```

**A third of the pressing — one hundred and two megabytes — for one command in
a build script.** The disc would have gone from 45.4474 % of a CD to 30.4357 %.

`thesis3do.py` also answers the other direction: at CD-DA rates, 22:30.04 would
be 101,253 sectors of Red Book audio, and the non-audio part of this disc is
30,890 sectors, so **a Red Book pressing would have fitted too**, at 132,143
sectors — 39.6827 % of a CD, still smaller than what was actually pressed. The
studio's choice was worse than either alternative on space.

## Why, and the boring answer is most of it

**The disc is 45 % full.** Nothing was at stake. Nothing had to fit. There was
no second disc, no cut content, no compromise anybody had to argue about, and
a hundred megabytes of a medium that cost the same whether it was written or
not went unwritten. **"It did not matter" is a complete explanation of the
decision and this chapter says so.**

What it is not is a complete explanation of the *situation*, because the twin
disc next door is the control. Super Street Fighter II Turbo is **364 sectors
longer** — one tenth of one per cent — was pressed **147 days later**, carries
**the same SDK build to the second**, and put **50:38.08** on it in SDX2. Two
studios, one console, one toolchain, one disc size, and one of them ran the
codec and the other did not. **The space was not the variable.**

## What the object says about the variable that was

Three things on this disc, each cheap and each pointing the same way.

**One: three sound files are at 22,255 Hz.** `/data/sounds/Buzzer.aiff`,
`Click.aiff` and `DoorOpen.aiff`. 22,255 is the Macintosh 22.254545 kHz rate,
rounded — the rate a Mac records at. The other fifty-nine 8-bit files are at a
clean 22,050. **Three files went from a Macintosh onto a 3DO disc without
passing through anything that would have resampled them**, which means they
passed through nothing at all.

**Two: `/AppStartup` has `\r` line endings and is entirely comments.** Nobody
edited it.

**Three: the `.dsp` files are untouched SDK.** All sixty-three of the Opera
audio folio's instrument patches are on the disc, in `/System/Audio/dsp`,
byte-identical with the twin's — and they include `adpcmmono.dsp`,
`adpcmhalfmono.dsp` and `decodeadpcm.dsp`. **Patches for playing back
compressed audio were pressed onto the disc that compressed none.**

The reading this chapter offers is not that anyone chose raw audio for quality.
It is that **there was no audio pipeline to put a codec in.** A studio that
resamples nothing, edits no boot script and ships the SDK's audio directory
untouched is a studio whose sound went from a recording session to a directory
to a mastering tool. **The absence of a step, not the abundance of space.**

That is an argument from three facts, **one of which fails as a control** and
is kept in view rather than dropped. It is offered as an argument.
The measurement is 67.4093 %; the counterfactual is 102,379,300 bytes; the
control is 364 sectors away and did the other thing. **The explanation is the
part that could be wrong.**

## Forty-three creatures, thirty-six recordings, and the ear was ahead of the hash

`/data/sounds/growls` holds 43 files named for AD&D creatures — one per monster
animation, 2,014,296 bytes, 1:30.79 in total. `hashall.py` finds **four**
byte-identical pairs among them and the answer *"43 creatures, 39 recordings"*
is what a hash census produces.

**It is too low, and the owner of this machine heard why before any tool
looked.** He reported that `Bulette.aiff` is identical in sound to
`Ankheg.aiff` and asked whether they were identical in bytes.

They are, and no hash could have said so:

```
Ankheg.aiff    36,608 bytes of sample data
Bulette.aiff   37,120 bytes -- and Ankheg's 36,608 occur VERBATIM inside it
                              at offset 256, with zero differing bytes
```

**512 bytes of near-silence, 256 at each end, and two different SHA-1s for one
recording.** `aiffreuse.py` was written for this, and it runs three exact tests
of decreasing strictness, each reported separately:

```
python tools/aiffreuse.py _work/files/data/sounds
```

```
1. IDENTICAL PAYLOAD, byte for byte              : 4 pairs
     Carrion Crawler = Purple Worm      Gelatinous Cube = Slime
     Ghost           = Shade            Mind Flayer     = Sword Wraith

2. ONE PAYLOAD VERBATIM INSIDE ANOTHER           : 1 pair
     Ankheg (36,608 B) inside Bulette (37,120 B) at offset 256

3. SAME LENGTH, sample correlation >= 0.990      : 3 pairs
     Crypt Thing  ~ Slithermorph   r=0.999930   gain k=1.91940
     Crypt Thing  ~ Yuan-ti        r=0.999369   gain k=0.95171
     Slithermorph ~ Yuan-ti        r=0.999540   gain k=0.49589

PAIRS CONFIRMED BY AN EXACT TEST                 : 8
```

**The third tier is a triple, and the gains are a factor of two apart.**
`Crypt Thing`, `Slithermorph` and `Yuan-ti` are 72,449 bytes each, correlate
with one another at better than 0.9993 sample for sample, and differ only in
level. In decibels: **`Slithermorph` is 5.66 dB below `Crypt Thing` and 6.09 dB
below `Yuan-ti`, and those two are 0.43 dB apart.** One recording, three
volumes, three creatures, saved three times at 8 bits.

**And this is the one thing in the repository that was checked end to end.**
The owner of this machine was asked to listen to the three afterwards, without
being told what the numbers said, and reported that he hears no difference
between them except that *Slithermorph seems a touch quieter*. **The least
squares fit and the ear picked the same file, in the same direction, on the
only one of the three that differs by more than half a decibel.**

Counting the pairs and the triple: **43 creature names, 36 distinct recordings
that this session can prove.** The hash census's 39 was three too many.

**And 36 is still an upper bound, because the ear goes further than the
arithmetic.** The owner also reports that `Gargoyle.aiff` is the same growl
pitched up, and that most of these are stock library cues — he named one, and
named it as a stock cue from a commercial library, and labelled his own
identification an inference. **This session could not confirm any of it**, and
says so:

- an RMS-envelope ranking over all 3,160 pairs of the 80 sound files is printed
  by `aiffreuse.py` and is explicitly **not a test**: the median unrelated pair
  scores 0.1387 and some clearly unrelated pairs reach 0.93;
- the pairs that ranking puts at the top and the exact tests do **not** confirm
  — `Cockatrice` with `Mind Flayer` at an envelope 1.0000, `Bone Naga` with
  `Spirit Naga` at 0.9617, `Gargoyle` with `Margoyle` at 0.9325 — have
  sample-level correlations of **−0.001, 0.037 and 0.018**. That is nothing;
- resampling `Ankheg` at every ratio from 0.50 to 2.00 and correlating against
  `Gargoyle` peaks at **0.0366**, which is no better than the same search
  against an unrelated file.

**So the pitch-shift hypothesis is reported as unconfirmed with the negative
stated, not omitted.** A resampled, re-quantised 8-bit signal does not survive
sample-level correlation, and an envelope that is generous enough to see
through a pitch shift is too generous to prove one. **The right tool for it is
a spectral comparison this session did not write**, and that is a named gap
rather than a silent one.

One pair sits exactly on the boundary and is worth the line: `Bloodworm` is the
same length as `Carrion Crawler` and `Purple Worm` and correlates with them at
**0.8742** — far above every unrelated pair and far below the 0.99 threshold.
It is not counted, and it is the one place on this disc where the tool's
cut-off is doing visible work.

## The sixty-three files that are not audio, and are counted anyway

`aiffread.py` opens 144 files and refuses 63 of them with *"no COMM"*. Those 63
are `/System/Audio/dsp/*.dsp`, the audio folio's DSP instrument patches. **They
are not sound, they are 3DO's and not this game's, and they are 54,158 bytes —
0.0175 % of the pressing.**

The refusal is the measurement. **Forty-three per cent of what the audio reader
opened on this disc is not audio**, and a session that had reported "144 audio
files" would have been wrong by sixty-three and would have had no way to know:
the files sit one directory away from the AIFF and are the same `FORM`
container, so neither the path nor the magic separates them. **Only opening
them does**, and opening them is what produced the sixty-three refusals.
