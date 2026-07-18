# Nwagụ Aneke Syllabary — Structured Source Transcription

> **Date:** 2026-04-27
> **Source:** Omniglot chart GIF (archived), visually examined
> **Method:** Manual row/column count from chart image
> **Auditor:** Opus critique pass — source-only, no PAGC assumptions

---

## Chart Title

**"SYLLABARY OF THE NWAGỤ ANEKE SCRIPT"**

---

## Column Headers (Vowels)

Reading left to right from the chart:

| Col | Label | Likely Phoneme | Confidence |
|-----|-------|---------------|------------|
| 1 | a | /a/ | HIGH |
| 2 | i | /i/ | HIGH |
| 3 | o | /o/ | HIGH |
| 4 | u | /u/ | HIGH |
| 5 | e | /e/ | HIGH |
| 6 | i | /ɪ/ (ị) | HIGH — likely the −ATR variant |
| 7 | o | /ɔ/ (ọ) | HIGH — likely the −ATR variant |
| 8 | u | /ʊ/ (ụ) | HIGH — likely the −ATR variant |

**Column count: 8** ✅

> [!NOTE]
> The 8 columns correspond to Standard Igbo's 8-vowel system (a, e, i, ị, o, ọ, u, ụ), reordered as (a, i, o, u, e, ị, ọ, ụ). The chart header appears to show the ATR pairs grouped together. **This matches PAGC's claim of 8 modifiers.**

---

## Row Labels (Consonants)

Reading top to bottom from the chart's left column:

| Row | Label | Likely Phoneme | Notes |
|-----|-------|---------------|-------|
| 1 | b | /b/ | |
| 2 | ch | /tʃ/ | |
| 3 | d | /d/ | |
| 4 | f/v | /f/ or /v/ | **Combined row.** Single printed row labeled "f/v". This is the only source of the 26-vs-27 ambiguity. |
| 5 | g | /ɡ/ | |
| 6 | gb | /ɡ͡b/ | Labio-velar stop |
| 7 | gh | /ɣ/ | Voiced velar fricative |
| 8 | gw | /ɡʷ/ | Labialized velar |
| 9 | h | /h/ | |
| 10 | j | /dʒ/ | |
| 11 | k | /k/ | |
| 12 | kp | /k͡p/ | Labio-velar stop |
| 13 | kw | /kʷ/ | Labialized velar |
| 14 | l | /l/ | |
| 15 | m | /m/ | |
| 16 | n | /n/ | |
| 17 | ṅ | /ŋ/ | Velar nasal |
| 18 | ny | /ɲ/ | Palatal nasal |
| 19 | nw | /nʷ/ | Labialized nasal |
| 20 | p | /p/ | |
| 21 | r | /r/ or /ɾ/ | |
| 22 | s | /s/ | |
| 23 | t | /t/ | |
| 24 | w | /w/ | |
| 25 | y | /j/ | |
| 26 | z | /z/ | Last row |

**Printed row count: 26** ✅

### The 26 vs 27 Distinction

**Source-grounded count:** The published chart shows **26 consonant rows × 8 vowel columns.**

Only a reinterpretation of the combined f/v row (row 4) as two underlying phonemes can recover a 27-base claim. Therefore, **27 is not directly source-evident from the chart alone.**

The real question PAGC must answer is: does "base" mean *printed row count* (26) or *underlying phonemic base count* (27, if f/v splits)? This is a definitional choice, not an empirical discovery.

---

## 🚨 Internal Inconsistency — Now Resolved

The BMCG spec (`BMCG_SPEC_V0_1.md`, line 69) states:

```
| **PAGC Matrix** | Consonant (26) | Vowel (8) | Logograph (100+) |
```

But INDEX.md and most PAGC files claim **27 bases**.

**Resolution:** The BMCG spec's count of 26 matches the chart's printed row count. The "27" in other files likely reflects a phonemic reinterpretation where the f/v row is split into two bases. The chart itself shows 26.

---

## Logographic Symbols ("Full Word Symbols")

The chart includes a right-hand column labeled **"Full Word Symbols"** listing logographs with their glosses. Reading from the chart:

| # | Word | English Gloss (inferred) | Semantic Domain |
|---|------|------------------------|-----------------|
| 1 | ubosi | day | Time |
| 2 | uche | thought/wisdom | Cognition |
| 3 | avo | ? | Unknown |
| 4 | ovia | ? | Unknown |
| 5 | oga | master/boss | Social role |
| 6 | nga | ? | Unknown |
| 7 | ogbenye | poor person | Social/moral |
| 8 | ogbu | killer | Social/moral |
| 9 | ugwu | respect/honor | Moral/equity |
| 10 | ije | journey/walking | Action |
| 11 | aku | wealth | Economic |
| 12 | ike | strength/power | Physical/social |
| 13 | uka | church/gathering | Institution |
| 14 | akwa | cloth/crying | Material/emotion |
| 15 | akwukwo | book/leaf | Material/knowledge |
| 16 | alo | counsel/advice | Moral/governance |
| 17 | ili | burial/eating | Ritual/sustenance |
| 18 | ana | land/ground | Territory |
| 19 | enu | sky/up | Space |
| 20 | uno | house | Dwelling |
| 21 | onwa | moon/month | Time/celestial |
| 22 | aro | thought/year | Cognition/time |
| 23 | iru | face/arrival | Body/action |
| 24 | asato | ? | Unknown |
| 25 | osu | outcast (caste term) | Social/moral |
| 26 | ewu | goat | Animal |
| 27 | uwa | world/life | Cosmological |
| 28 | uzo | road/way | Space/path |
| 29 | izu | week | Time |
| 30 | oya | ? | Unknown |

**Logograph count: ~30 visible in chart** (PAGC claims "100+" — the chart shows only a subset)

### Semantic Domain Analysis of Logographs

| Domain | Count | Examples |
|--------|-------|---------|
| Moral/equity/social | ~8 | ugwu, ogbenye, ogbu, osu, alo, ike, oga |
| Time/celestial | ~4 | ubosi, onwa, izu, aro |
| Space/territory | ~3 | ana, enu, uzo |
| Cognition/knowledge | ~3 | uche, aro, akwukwo |
| Material/economic | ~3 | aku, akwa, uno |
| Ritual/cosmological | ~3 | uwa, ili, uka |
| Body/action | ~3 | ije, iru, ewu |
| Unknown/uncertain | ~4 | avo, ovia, nga, asato, oya |

> [!IMPORTANT]
> **The logographs show a concentration in moral/social and temporal domains.** This is consistent with PAGC's "lexical cache of high-frequency moral/equity terms" hypothesis — but it does NOT prove the hypothesis. The chart shows ~30 logographs; whether there are 100+ in the full corpus (exercise books) is unknown.

---

## Matrix Regularity Assessment

From visual inspection of the chart:

- Most cells appear filled with a unique glyph
- Some cells appear to have simpler or possibly derived forms
- A few cells may be empty or contain uncertain content (hard to tell from image resolution)
- The chart is generally **regular** — it looks like a systematic grid, not a sparse or irregular table

**Assessment:** The chart IS organized as a matrix, but whether this organization reflects Aneke's original conception or Azuonye's editorial choice for the paper is unknown.

---

## Summary of Source-Observed Counts

| Element | PAGC Claim | Source-Observed | Confirmed? |
|---------|-----------|----------------|-----------|
| Vowel columns | 8 | **8** | ✅ YES |
| Consonant rows | 27 | **26–28 (uncertain)** | ⚠️ CLOSE BUT UNCONFIRMED |
| Total CV symbols | 216 | **~200–224 (depends on row count and empty cells)** | ⚠️ UNCONFIRMED |
| Logographs in chart | 100+ | **~30 visible** | ❌ Chart shows only ~30 |
| Matrix structure | Generative grammar | **Pedagogical chart** | ⚠️ INTERPRETATION DIFFERS |

---

## Blocking Actions

1. **Download and read Azuonye 1992 PDF** — will give exact consonant inventory and whether the chart is Azuonye's organization or Aneke's
2. **Locate Ahamefula & Mbah 2011** — independent linguistic count
3. **Resolve the 26 vs 27 internal inconsistency** in PAGC files
