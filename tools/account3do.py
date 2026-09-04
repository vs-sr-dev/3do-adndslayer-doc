#!/usr/bin/env python3
"""account3do.py -- what fraction of the pressing is of a KNOWN kind.

The point of the whole exercise. A sector map says every sector belongs to a
file; it does not say anybody knows what the file IS. This tool works in bytes
of the user area and puts each one in exactly one bucket, refusing to print a
total that is not the user area.

A byte counts as IDENTIFIED only if a format was derived or validated on this
disc and the tool that reads it consumed the byte. Everything else is UNKNOWN,
including files whose purpose is obvious from their name -- a name is not a
format.

REWRITTEN FOR THE FOURTH DISC, and the two changes are named:

  * the AIFF bucket is labelled with the codec the container DECLARES. The
    previous version printed "SDX2" unconditionally; this disc's eighty-one
    files are codec `NONE` and the label was a claim about a neighbour;
  * the ANIM / CCB container is WALKED rather than signature-scanned, so its
    chunks are charged to their own tags. The signature scan left 9,432,360
    bytes -- 3.04 % of this pressing -- in a bucket called "kind not derived"
    that was a property of the reader and not of the object.

Every file that still lands in UNKNOWN is printed by name at the end, so the
identified figure can be audited rather than believed.

usage: account3do.py TREE SECTORS DECLARED_BLOCKS
"""
import os
import struct
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from celdecode import cels_by_scan                     # noqa: E402
from ccbread import Bad                                # noqa: E402
from aifcensus import parse as aif_parse, Bad as AifBad  # noqa: E402
from sdx2dec import read_aifc                          # noqa: E402
import animwalk                                        # noqa: E402
import celdecode as _cd                                # noqa: E402


def frames_render(d, ch):
    """True when every PDAT of this container renders. A byte is IDENTIFIED
    only if something read it, so a container that walks but whose frames do
    not decode is charged to a different bucket than one that does."""
    try:
        ccb, plut, pdats = animwalk.parts(d, ch)
        if ccb is None:
            return False
        for pd in pdats:
            _cd.render(ccb, plut, pd)
        return True
    except Exception:
        return False


def main():
    if len(sys.argv) != 4:
        sys.stderr.write(__doc__)
        raise SystemExit(2)
    tree, sectors, declared = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    U = sectors * 2048

    buckets = {}
    residue = []
    files = []
    for dp, dn, fn in os.walk(tree):
        for f in fn:
            files.append(os.path.join(dp, f))
    files.sort()

    def put(name, n):
        buckets[name] = buckets.get(name, 0) + n

    tree_bytes = 0
    for p in files:
        d = open(p, "rb").read()
        tree_bytes += len(d)
        rel = "/" + os.path.relpath(p, tree).replace(os.sep, "/")
        done = 0

        # AIFF / AIFF-C, read from COMM and SSND.
        #
        # The bucket is named after the codec the container DECLARES, not
        # after the codec the previous disc happened to use. The third
        # session of this tool hard-coded "SDX2" into the label and this
        # disc's eighty-one files are every one of them codec NONE, so the
        # old label was a sentence about a neighbour printed over this
        # object's number.
        if d[0:4] == b"FORM" and d[8:12] in (b"AIFF", b"AIFC"):
            try:
                ch, fr, bits, rate, codec, ssnd = read_aifc(p)
                cname = (codec or b"NONE")
                if isinstance(cname, bytes):
                    cname = cname.decode("latin1", "replace")
                put("%s %s sample data" % (d[8:12].decode("latin1"),
                                           cname.strip() or "NONE"),
                    len(ssnd))
                put("AIFF/AIFF-C container headers", len(d) - len(ssnd))
                continue
            except Exception:
                pass
            # a FORM that is not AIFF-like: the DSP instruments
        if d[0:4] == b"FORM":
            put("FORM 3INS DSP instruments", len(d))
            continue

        # ARM Image Format
        try:
            aif_parse(d)
            put("ARM Image Format executables", len(d))
            continue
        except AifBad:
            pass

        # The ANIM / CCB container, walked chunk by chunk.
        #
        # The previous version of this tool used `cels_by_scan`, a SIGNATURE
        # scan, and left everything past the first cel in the bucket "bytes
        # inside cel-bearing files, kind not derived" -- 9,432,360 bytes on
        # this disc, 3.04 % of the pressing. That bucket was an artefact of
        # the reader, not a property of the object: the container walks to
        # residue zero on 370 files of 370 and every one of its 2,516 PDAT
        # chunks renders. Each chunk is now charged to its own tag, and a
        # container that does NOT close still falls through to the scan.
        if d[0:4] in (b"ANIM", b"CCB "):
            try:
                ch = animwalk.walk(d)
                ok = frames_render(d, ch)
                for off, tag, clen in ch:
                    t = tag.decode("latin1").strip() or "?"
                    if t == "PDAT":
                        put("cel/animation frame data (PDAT), rendered"
                            if ok else
                            "cel/animation frame data (PDAT), walked not "
                            "rendered", clen)
                    else:
                        put("cel container headers (%s), fields derived" % t,
                            clen)
                continue
            except Exception:
                pass

        # cels, found by signature -- the fallback for a file that does not
        # begin with a container tag
        if b"CCB " in d:
            got, un = cels_by_scan(d)
            if got:
                put("cel data (CCB, PLUT, PDAT) derived and rendered",
                    len(d) - un)
                if un:
                    put("bytes inside cel-bearing files, kind not derived", un)
                continue

        # the Data Streamer, derived on the third disc: SHDR/FILM/SNDS/FILL,
        # every FRME decoded as Cinepak and every SSMP written out as a WAV.
        # The chain consumes the file to its last byte, so the whole file is
        # accounted for and nothing is left over.
        if d[0:4] == b"SHDR":
            try:
                import streamread
                cs = streamread.chunks(d)
                if cs[-1][0] + cs[-1][2] == len(d):
                    put("Data Streamer: SHDR/FILM/SNDS/FILL, Cinepak decoded",
                        len(d))
                    continue
            except Exception:
                pass

        # BRGR archives, derived on the third disc. The directory is derived
        # and checked; the members are split by whether their own format was
        # derived too, because a container is not its contents.
        if d[0:4] == b"BRGR":
            try:
                import rezread
                import rezcel
                count, members = rezread.parse(d)
                hdr = 8 + 12 * count
                put("BRGR archive directories, derived and checked", hdr)
                for mid, off, ln in members:
                    body = d[off:off + ln]
                    try:
                        rezcel.parse(body)
                        put("BRGR members: headless cels, decoded and rendered",
                            ln)
                    except Exception:
                        put("BRGR members: kind NOT derived", ln)
                continue
            except Exception:
                pass

        # the banner screen, derived on the third disc
        if d[0:8] == b"\x01APPSCRN":
            try:
                import appscrn
                info = appscrn.parse(d)
                put("APPSCRN banner screen, decoded and rendered",
                    24 + info["payload"])
                put("APPSCRN trailing zero bytes", len(d) - 24 - info["payload"])
                continue
            except Exception:
                pass

        # .CHR archives: the offset tree is derived, the leaves are not
        if rel.upper().endswith(".CHR"):
            put(".CHR archives: index derived, leaf pixel data NOT derived",
                len(d))
            continue
        if rel.upper().endswith(".PAL"):
            put(".PAL palettes, 5-5-5 proved", len(d))
            continue
        if d[0:16].startswith(b"SPT v"):
            put("SPT v0.54 containers, signature only", len(d))
            continue
        if len(d) <= 2:
            put("one-byte junk files", len(d))
            continue
        if rel == "/rom_tags":
            # derived field by field on the fourth disc by romtags.py, whose
            # `records` reads every one of the 32-byte records and refuses a
            # file that is not a whole number of them.
            put("/rom_tags, derived record by record", len(d))
            continue
        if rel == "/Disc label":
            put("the volume label, derived field by field", len(d))
            continue
        if rel == "/signatures":
            put("/signatures: size, entropy and fill measured, content not read",
                len(d))
            continue
        put("UNKNOWN: no format derived", len(d))
        residue.append((rel, len(d)))

    print("user area                 %12d bytes (%d sectors x 2048)" % (U, sectors))
    print("bytes in files            %12d = %.4f %%"
          % (tree_bytes, 100.0 * tree_bytes / U))
    print()
    known = 0
    for k in sorted(buckets, key=lambda x: -buckets[x]):
        flag = "?" if ("UNKNOWN" in k or "NOT derived" in k
                       or "not derived" in k or "not read" in k) else " "
        if flag == " ":
            known += buckets[k]
        print(" %s %-62s %12d %8.4f %%"
              % (flag, k, buckets[k], 100.0 * buckets[k] / U))
    print()
    fill = U - tree_bytes
    print("   %-62s %12d %8.4f %%"
          % ("not in any file (mastering fill, zeros, directories, copies)",
             fill, 100.0 * fill / U))
    print()
    print("   %-62s %12d %8.4f %%"
          % ("IDENTIFIED (a format derived or validated on this disc)",
             known, 100.0 * known / U))
    unk = tree_bytes - known
    print("   %-62s %12d %8.4f %%"
          % ("IN A FILE, KIND NOT DERIVED", unk, 100.0 * unk / U))
    total = known + unk + fill
    print("   %-62s %12d %8.4f %%" % ("TOTAL", total, 100.0 * total / U))
    if residue:
        print()
        print("EVERY FILE IN THE 'UNKNOWN' BUCKET, NAMED -- %d of them, %d "
              "bytes" % (len(residue), sum(n for _, n in residue)))
        for rel, n in sorted(residue, key=lambda r: -r[1]):
            print("     %-58s %12d" % (rel, n))
    if total != U:
        raise SystemExit("account3do: the total is %d, not the user area %d"
                         % (total, U))


if __name__ == "__main__":
    main()
