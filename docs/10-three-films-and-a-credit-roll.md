# 10 — three films and a credit roll: what the disc says about who made it, and what this repository publishes

*Measure: three Data Streamer films decoded frame by frame, the credit roll's
structure counted rather than transcribed, and a decision about names taken
explicitly instead of by silence.*

## The three films

50,266,112 bytes — **16.2178 % of the pressing** — in three files. The
container is the 3DO Data Streamer, documented on this collection's third disc;
the video is Cinepak, a public format, and `cvidmovie.py` decodes it.

```
python tools/cvidmovie.py "_work/files/data/Credits.stream" --census
```

| file | bytes | size | rate field | frames declared | frames measured |
|---|---|---|---|---|---|
| `Intro.stream` | 17,367,040 | 280 × 160 | 15 | 1,326 | **1,326** |
| `Credits.stream` | 24,641,536 | 280 × 160 | **12** | 1,224 | **1,224** |
| `EndGame.stream` | 8,257,536 | 280 × 160 | 15 | 833 | **833** |

**3,383 frames decoded of 3,383**, zero sub-chunk overruns, and on every single
frame the 2,800 macroblocks of a 70 × 40 grid are all accounted for. The strip
heights sum to the declared 160 on 3,383 of 3,383.

**280 × 160**, not the 320 × 240 this session predicted (C21) — a raster
smaller than the console's own, and smaller than the 320 × 240 the still cels
use. The rate field is 12 on the credits and 15 on the other two, which gives
1,224 / 12 = **102.00 seconds exactly** for the credit roll and 88.4 and 55.5
seconds for the others.

The pre-briefing counted 1,327, 1,225 and 834 `FILM` chunks. **One `FILM` chunk
per film is the `FHDR` header rather than a frame**, and 3,386 − 3 = 3,383.
That reconciles.

`Intro.stream` is a rendered fly-up to a castle at night, bats, and the game's
wordmark. `EndGame.stream` is the same castle destroyed by a beam of light and
the wordmark again. **Neither contains a word of text beyond the title.** All
the text in fifty megabytes of film is in the third file.

## The credit roll, measured

The roll is **not a scroll**. Decoding every frame and counting how many bytes
of the raster change from one frame to the next segments it cleanly:

```
72 segments at a 0.5 % change threshold
  36 held, 36 moving
  of the 36 held: 17 with light on screen, 19 fully black
```

**Seventeen credit screens**, each faded up over about half a second, held
still for a median of **3.83 seconds** (46 frames; range 37 to 48), faded down,
and separated by about three quarters of a second of black. 773 of the 1,224
frames — 63.2 % of the film — are a screen being held. The remaining 36.8 % is
crossfades and black.

Twenty-four megabytes of Cinepak to display seventeen still pictures of text
for a hundred and two seconds. **The frames are 20,132 bytes each on average
and no two of them are the same**, because a crossfade over a texture-mapped
background is exactly the case Cinepak cannot exploit.

## What is in it, and what this repository publishes

The seventeen screens carry, between them:

- **13 distinct role titles** — an executive producer at each of two companies,
  a director, programming, additional programming, art direction, artists, 3D
  modelling and rendering, musical score, sound editing, an associate producer,
  a product test supervisor, quality assurance, and two "special thanks"
  screens;
- **25 credit lines naming 20 distinct people**, five of whom appear more than
  once;
- **two companies**: the developer and the publisher;
- **one year.**

**This repository publishes the counts above and not the names.** No name from
the credit roll appears in these documents. No frame of any film is published,
and `.png` is in `.gitignore` alongside the audio and the cels.

## Why — and this is the first time the clause has been applied

The criterion this pipeline works under gained a clause on the previous object,
written because a 1988 floppy printed two private individuals' street address:

> **Identity and reach are not the same datum.** A datum that *identifies* a
> person is admitted by the criterion. A datum by which a stranger could
> *arrive at* a person is not, however plainly the product printed it and
> however long ago. Contact details are reported as a shape — kind, count and
> location — and never as their digits.

**A credit roll is identity and not reach, so the clause admits it.** Saying so
explicitly is the point: the clause was written yesterday and this is the first
object that has had to apply it rather than generate it, and a rule that is
never tested is not a rule. **Under the criterion as written, this repository
could have transcribed all twenty names and been within it.**

It has not, for a reason the clause does not cover: **the clause says nothing
about volume.**

Twenty names in an indexable repository is not the same act as one. A single
name that a product printed on its title screen is a fact about the product; a
complete personnel list of a games studio in 1994, transcribed into
machine-readable text and pushed to a public host, is a fact about **twenty
people** — most of whom are alive, none of whom chose this, and for whom the
practical difference between "it is in a video on a CD-ROM" and "it is the
first search result" is the whole of the matter. The names have been public for
thirty-one years at 280 × 160, twelve frames a second, four minutes into a
game nobody plays. **Transcribing them changes their reach without adding to
their identity, and reach is the thing the clause protects.**

That is the argument. **The decision was also put to the owner of this machine
before it was taken**, since the disc is his, and he chose the same: publish the
shape, not the names.

**What is published instead** — because it is corporate identity and not
personal data, and because it is the actual answer to the question this disc
asks:

- the game was developed by **Lion Entertainment, Inc.** and published by
  **Strategic Simulations, Inc.**;
- under licence from **TSR, Inc., Lake Geneva, Wisconsin, USA**;
- **© 1994**, both to TSR and to SSI.

## And none of that needed the credit movie

Here is the part the brief did not know, and it reverses the session's premise.

The brief's framing was that **everyone and everything is inside 24.6 MB of
video** — no year, no copyright, no company name in any string on the disc, so
the only way to find out who made this is to decode a film. The first half is
true and checkable: `Entertainment` 0, `Strategic` 0, `Simulations` 0,
`Copyright` 0 outside `/System`, and not one four-digit number beginning `19`
in `/LaunchMe`.

The second half is false. `/data/ADD.cel` is **12,736 bytes — 0.0041 % of the
pressing** — decodes in one command with a tool that has existed for two discs,
and is a licence screen whose
small print reads, in full:

> ADVANCED DUNGEONS & DRAGONS and SLAYER are trademarks owned and used under
> license from TSR, Inc., Lake Geneva WI USA. ©1994 TSR Inc. All Rights
> Reserved. ©1994 Strategic Simulations, Inc. All Rights Reserved.

**The year, the copyright, the licensor, the licensor's town and the publisher
are in a still picture that the console shows before the title screen**, and
that picture is twelve and a half kilobytes. `/data/SSI.anim` is the
publisher's wordmark rendered in 3D; `/data/Lion.anim` is 198 frames and frame
100 of it reads **Lion Entertainment, Inc.**, which is the developer
([06](06-the-container.md)).

So the disc does not hide who made it. **It says so four times, in pixels, in
the first ten seconds, in five files totalling 1,793,536 bytes — 0.5787 % of
the pressing, and a fourteenth of the credit movie alone** — and the
credit roll adds the twenty people and nothing else. The expensive thing was
never necessary for the corporate answer; it was only ever necessary for the
personal one, which is the one this repository declines to publish.

## The abbreviations, expanded from the object and not from memory

The brief listed six abbreviations and said two of them are expandable from the
object itself. They are, and here they are:

| | expansion | where it is proved |
|---|---|---|
| **ADD** | **Advanced Dungeons & Dragons** | `/data/ADD.cel`, in the logo and again in the small print |
| **SSI** | **Strategic Simulations, Inc.** | `/data/Credits.stream`, screen 12: *"for Strategic Simulations, Inc."*; and `/data/SSI.anim` |
| TSR | **not expanded** | the object gives the company as *"TSR, Inc."* and its town, and never spells the initials out |
| CCB | Cel Control Block | inherited from `ccbread.py`, derived on the first disc, **not** provable here |
| AIF | ARM Image Format | inherited, and **not** provable from this object |
| SDX2 | not expanded anywhere on this disc | — |

**TSR is the trap.** The object names the company four times and expands the
letters never, and a session that wrote out the three words behind them would
have been quoting its own memory into a repository that is supposed to quote
bytes. Whatever those letters stand for, **this disc does not say.**
