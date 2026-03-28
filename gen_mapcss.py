#!/usr/bin/env python3
"""Generate SeamarkLightCharacterFixups.validator.mapcss covering light numbers 1-7."""

KEY_VARIANTS = [
    ("seamark:light:character",   "seamark:light:group",   "seamark:light:colour",   "seamark:light:category"),
    ("seamark:light:1:character", "seamark:light:1:group", "seamark:light:1:colour", "seamark:light:1:category"),
    ("seamark:light:2:character", "seamark:light:2:group", "seamark:light:2:colour", "seamark:light:2:category"),
    ("seamark:light:3:character", "seamark:light:3:group", "seamark:light:3:colour", "seamark:light:3:category"),
    ("seamark:light:4:character", "seamark:light:4:group", "seamark:light:4:colour", "seamark:light:4:category"),
    ("seamark:light:5:character", "seamark:light:5:group", "seamark:light:5:colour", "seamark:light:5:category"),
    ("seamark:light:6:character", "seamark:light:6:group", "seamark:light:6:colour", "seamark:light:6:category"),
    ("seamark:light:7:character", "seamark:light:7:group", "seamark:light:7:colour", "seamark:light:7:category"),
]

lines = []

def w(s=""):
    lines.append(s)

def emit_simple_fix(char_key, bad_val, good_val, msg, group):
    w()
    w(f'*["{char_key}"="{bad_val}"] {{')
    w(f'    throwWarning: tr("{char_key}={bad_val} -- {msg}");')
    w(f'    group: tr("{group}");')
    w(f'    fixAdd: "{char_key}={good_val}";')
    w(f'    assertMatch: "node \\"{char_key}\\"={bad_val}";')
    w(f'    assertNoMatch: "node \\"{char_key}\\"={good_val}";')
    w("}")

def emit_fix_with_group(char_key, group_key, bad_val, good_char, good_group, msg, group):
    w()
    w(f'*["{char_key}"="{bad_val}"] {{')
    w(f'    throwWarning: tr("{char_key}={bad_val} -- {msg}");')
    w(f'    group: tr("{group}");')
    w(f'    fixAdd: "{char_key}={good_char}";')
    w(f'    fixAdd: "{group_key}={good_group}";')
    w(f'    assertMatch: "node \\"{char_key}\\"={bad_val}";')
    w(f'    assertNoMatch: "node \\"{char_key}\\"={good_char}";')
    w("}")

def emit_fix_char_only(char_key, bad_val, good_char, msg, group):
    w()
    w(f'*["{char_key}"="{bad_val}"] {{')
    w(f'    throwWarning: tr("{char_key}={bad_val} -- {msg}");')
    w(f'    group: tr("{group}");')
    w(f'    fixAdd: "{char_key}={good_char}";')
    w(f'    assertMatch: "node \\"{char_key}\\"={bad_val}";')
    w(f'    assertNoMatch: "node \\"{char_key}\\"={good_char}";')
    w("}")

def emit_warning_only(char_key, bad_val, msg, group):
    w()
    w(f'*["{char_key}"="{bad_val}"] {{')
    w(f'    throwWarning: tr("{char_key}={bad_val} -- {msg}");')
    w(f'    group: tr("{group}");')
    w(f'    assertMatch: "node \\"{char_key}\\"={bad_val}";')
    w("}")


# === Header ===

w("meta")
w("{")
w('    title: "Seamark light character fixups";')
w('    version: "0,1_2026-02-02";')
w('    description: "Corrects non-conforming seamark:light:character values with obvious fixes";')
w('    author: "watmildon";')
w('    link: "https://github.com/watmildon/josm-validator-rules/blob/main/rules/SeamarkLightCharacterFixups.validator.mapcss";')
w('    baselanguage: "en";')
w('    min-josm-version: 14481;')
w("}")
w()
w("/*")
w("[out:json][timeout:120];")
w("(")
for ck, gk, clk, catk in KEY_VARIANTS:
    w(f'  nwr["{ck}"];')
w(");")
w("out body;")
w(">;")
w("out skel qt;")
w("*/")

# === Uppercase I typos ===

w()
w("/* ============================================================")
w("   Uppercase I instead of lowercase L (FI -> Fl, LFI -> LFl)")
w("   Very common typo, especially from Finnish mappers.")
w("   ============================================================ */")

for ck, gk, clk, catk in KEY_VARIANTS:
    emit_simple_fix(ck, "FI", "Fl",
        "uppercase I instead of lowercase L, should be Fl",
        "Seamark light character typo")

for ck, gk, clk, catk in KEY_VARIANTS:
    emit_simple_fix(ck, "LFI", "LFl",
        "uppercase I instead of lowercase L, should be LFl",
        "Seamark light character typo")

# === Lowercase variants ===

w()
w("/* ============================================================")
w("   Lowercase variants (fl -> Fl, f -> F, oc -> Oc, Lfl -> LFl)")
w("   ============================================================ */")

for ck, gk, clk, catk in KEY_VARIANTS:
    emit_simple_fix(ck, "fl", "Fl",
        "wrong case, should be Fl",
        "Seamark light character wrong case")

for ck, gk, clk, catk in KEY_VARIANTS:
    emit_simple_fix(ck, "f", "F",
        "wrong case, should be F",
        "Seamark light character wrong case")

for ck, gk, clk, catk in KEY_VARIANTS:
    emit_simple_fix(ck, "oc", "Oc",
        "wrong case, should be Oc",
        "Seamark light character wrong case")

for ck, gk, clk, catk in KEY_VARIANTS:
    emit_simple_fix(ck, "Lfl", "LFl",
        "wrong case, should be LFl",
        "Seamark light character wrong case")

# === Uppercase variants ===

w()
w("/* ============================================================")
w("   Uppercase variants (ISO -> Iso, FL -> Fl)")
w("   ============================================================ */")

for ck, gk, clk, catk in KEY_VARIANTS:
    emit_simple_fix(ck, "ISO", "Iso",
        "wrong case, should be Iso",
        "Seamark light character wrong case")

for ck, gk, clk, catk in KEY_VARIANTS:
    emit_simple_fix(ck, "FL", "Fl",
        "wrong case, should be Fl",
        "Seamark light character wrong case")

# === English words ===

w()
w("/* ============================================================")
w("   English words instead of abbreviations (flashing -> Fl)")
w("   ============================================================ */")

for ck, gk, clk, catk in KEY_VARIANTS:
    emit_simple_fix(ck, "flashing", "Fl",
        "should use abbreviation Fl",
        "Seamark light character should use standard abbreviation")

# === Missing dot in alternating ===

w()
w("/* ============================================================")
w("   Missing dot in alternating types (AlFl -> Al.Fl, AlQ -> Al.Q)")
w("   ============================================================ */")

for ck, gk, clk, catk in KEY_VARIANTS:
    emit_simple_fix(ck, "AlFl", "Al.Fl",
        "missing dot, should be Al.Fl",
        "Seamark light character missing dot in alternating")

for ck, gk, clk, catk in KEY_VARIANTS:
    emit_simple_fix(ck, "AlQ", "Al.Q",
        "missing dot, should be Al.Q",
        "Seamark light character missing dot in alternating")

# === Spaces in composite ===

w()
w("/* ============================================================")
w("   Spaces around + in composite characters (Q + LFl -> Q+LFl)")
w("   ============================================================ */")

for ck, gk, clk, catk in KEY_VARIANTS:
    emit_simple_fix(ck, "Q + LFl", "Q+LFl",
        "has spaces around +, should be Q+LFl",
        "Seamark light character formatting")

# === Morse with group in character ===

w()
w("/* ============================================================")
w("   Morse with group in character (Mo(A) -> Mo with group=A)")
w("   ============================================================ */")

for ck, gk, clk, catk in KEY_VARIANTS:
    emit_fix_with_group(ck, gk, "Mo(A)", "Mo", "A",
        "Morse group should be in group tag, not character",
        "Seamark light character has embedded group")

# === Group count in character ===

w()
w("/* ============================================================")
w("   Group count embedded in character field")
w("   Fl(1) -> Fl (group=1 is implied)")
w("   Fl(2) -> Fl with group=2")
w("   Fl(2+1) -> Fl with group=2+1")
w("   ============================================================ */")

for ck, gk, clk, catk in KEY_VARIANTS:
    emit_fix_char_only(ck, "Fl(1)", "Fl",
        "group count is redundant for single flash, should be Fl",
        "Seamark light character has embedded group")

for ck, gk, clk, catk in KEY_VARIANTS:
    emit_fix_with_group(ck, gk, "Fl(2)", "Fl", "2",
        "group count should be in group tag, not character",
        "Seamark light character has embedded group")

for ck, gk, clk, catk in KEY_VARIANTS:
    emit_fix_with_group(ck, gk, "Fl(2+1)", "Fl", "2+1",
        "group should be in group tag, not character",
        "Seamark light character has embedded group")

# === Invalid values (warning only) ===

w()
w("/* ============================================================")
w("   Values that are not light characters -- warning only, no fixup")
w("   These need manual review to determine the correct tagging.")
w("   ============================================================ */")

for ck, gk, clk, catk in KEY_VARIANTS:
    emit_warning_only(ck, "c",
        "not a valid light character, needs manual review",
        "Seamark light character invalid value")

for ck, gk, clk, catk in KEY_VARIANTS:
    emit_warning_only(ck, "green",
        f"this is a colour, not a character. Move to {clk}",
        "Seamark light character invalid value")

for ck, gk, clk, catk in KEY_VARIANTS:
    emit_warning_only(ck, "red",
        f"this is a colour, not a character. Move to {clk}",
        "Seamark light character invalid value")

for ck, gk, clk, catk in KEY_VARIANTS:
    emit_warning_only(ck, "yellow",
        f"this is a colour, not a character. Move to {clk}",
        "Seamark light character invalid value")

for ck, gk, clk, catk in KEY_VARIANTS:
    emit_warning_only(ck, "W",
        f"this is a colour (white), not a character. Move to {clk}",
        "Seamark light character invalid value")

for ck, gk, clk, catk in KEY_VARIANTS:
    emit_warning_only(ck, "Dir",
        f"directional is not a character. Consider {catk}=directional",
        "Seamark light character invalid value")

for ck, gk, clk, catk in KEY_VARIANTS:
    emit_warning_only(ck, "floodlight",
        "not a navigational light character, needs manual review",
        "Seamark light character invalid value")

for ck, gk, clk, catk in KEY_VARIANTS:
    emit_warning_only(ck, "Ro",
        "not a valid light character, needs manual review",
        "Seamark light character invalid value")

for ck, gk, clk, catk in KEY_VARIANTS:
    emit_warning_only(ck, "U",
        "not a valid light character, needs manual review",
        "Seamark light character invalid value")

# === Embedded descriptions (warning only, unnumbered key only) ===

w()
w("/* ============================================================")
w("   Embedded descriptions -- warning only, needs manual cleanup")
w("   These have period, colour, or other info stuffed into character.")
w("   These are one-off values found only on the unnumbered key.")
w("   ============================================================ */")

ck0 = KEY_VARIANTS[0][0]

emit_warning_only(ck0, "LFl W 10s",
    "has embedded description. Should be character=LFl with separate colour and period tags",
    "Seamark light character has embedded description")

emit_warning_only(ck0, "Fl W ev 5 sec",
    "has embedded description. Should be character=Fl with separate colour and period tags",
    "Seamark light character has embedded description")

emit_warning_only(ck0, "Fl(4) W 20s",
    "has embedded description. Should be character=Fl with group=4 and separate colour/period tags",
    "Seamark light character has embedded description")

emit_warning_only(ck0, "FL(2) R 4S 3M",
    "has embedded description. Should be character=Fl with group=2 and separate colour/period tags",
    "Seamark light character has embedded description")

emit_warning_only(ck0, "Fl IMH",
    "unknown suffix, should likely be character=Fl. Needs manual review",
    "Seamark light character has embedded description")

emit_warning_only(ck0, "Fl.(3)W",
    "should be character=Fl with group=3 and separate colour tag",
    "Seamark light character has embedded description")

emit_simple_fix(ck0, "Fl_of1923", "Fl",
    "historical note in character field, should be character=Fl",
    "Seamark light character has embedded description")

emit_warning_only(ck0, "FIso",
    "ambiguous, possibly F+Iso or typo. Needs manual review",
    "Seamark light character has embedded description")


# === Write output ===

import os

content = "\n".join(lines) + "\n"
script_dir = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(script_dir, "SeamarkLightCharacterFixups.validator.mapcss")

with open(out_path, "w", encoding="utf-8", newline="\n") as f:
    f.write(content)

rule_count = content.count("throwWarning")
print(f"Written {out_path}")
print(f"  {rule_count} rules total")

with open(out_path, "rb") as f:
    sample = f.read(50)
print(f"  Has CRLF: {b'\\r\\n' in sample}")