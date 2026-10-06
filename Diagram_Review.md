# Diagram review — Basic 7 Integrated Science mock series

Every figure in the 22 papers, reproduced exactly as it renders, with a verdict.
Figures render in **Consolas** in the `.docx` and inside code fences in the `.md`, which is the right call — but see P1.

## Headline numbers

| | |
| --- | --- |
| Papers with a figure | **10 of 22** |
| Papers with no figure at all | **12** |
| Papers with more than one figure | **1** (Living Cells) |
| Figures appearing in Section A | **0** |
| Figures drawn as 'empty rectangle + (i)/(ii)/(iii)' | **6 of 10** |

---

## P1 · Materials

**3 / 10**

```
| P | Q | R |
|---|---|---|
| `•   •   •   •` | `•   •    •  •` | `•            ` |
| `•   •   •   •` | `  •   •   •  ` | `        •    ` |
| `•   •   •   •` | `•    •   •  •` | `    •        ` |
| `•   •   •   •` | `   •  •   •  ` | `          •  ` |
```

*NOT A FIGURE — rendered as a markdown table of bullet rows (lines 323-326 of the .md), one table row per line of the diagram. Reads as a 4x3 grid inside cell borders, not as three containers of particles. It is also the only 'diagram' not inside a monospace code fence, so it depends entirely on the viewer keeping the inline-code font.*

---

## P2 · Living Cells (2 figures: animal cell, plant cell)

**7 / 10**

```
              . - - - - - - - - - - - - - - - - - .
            /   2  .  .  .  .  .  .  .  .  .  .  .  \
           /     .                                .   \
    1 --> |    .        ______________             .  |
          |   .        /      3       \             . |
          |   .        \______________/             . |
          |    .                                    .  |
          |    .       4   (    ~    )              .  |
           \    .  .  .  .  .  .  .  .  .  .  .  .  . /
            ' - - - - - - - - - - - - - - - - - - - - '
```
```
     1 -> =======================================
     2 -> ---------------------------------------
          |  3  .  .  .  .  .  .  .  .  .  .  .  |
          |  .         ____________               |
          |  .     6  /            \     4        |
          |  .        \____________/  _________   |
          |  .                       |         |  |
          |  .     5  ( o )   ( o )  |         |  |
          |  .                       |_________|  |
          |  .  .  .  .  .  .  .  .  .  .  .  .   |
           ---------------------------------------
           =======================================
```

*Good — genuinely pictorial and recognisable. Defect: the right-hand edge drifts by one column. ANIMAL_CELL lines 4-6 close at col 54 but lines 7-8 close at col 55; PLANT_CELL line 3 closes at col 49 while the rest close at col 50. In Consolas that is a visible one-character jog in the membrane. Label '2' also sits on the membrane line, which reads as if it points at the wall rather than the cytoplasm.*

---

## P3 · Earth Science (water cycle)

**8 / 10**

```
                        2  CONDENSATION
                 (water vapour cools and forms clouds)
                    ^                             |
                    |                             v
                    |                  3  PRECIPITATION
    1  EVAPORATION  |                    (water falls as rain)
 (the sun heats     |                             |
  water and it      |                             v
  rises as vapour)  |          RIVERS * LAKES * OCEANS * SOIL
                    ^                             ^
                    |                             |
                    |                  4  TRANSPIRATION
                    |           (water vapour lost from leaves)
                    +--------------------------------+
```

*Best of the set. Real arrows, labelled stages, and the annotations carry information rather than just position. Only quibble: the bottom '+---...---+' rail is cryptic — most pupils will not read it as 'the earth's surface'.*

---

## P4 · Life Cycle of Organisms (housefly)

**7 / 10**

```
       1                      2                       3                      4
  +---------+           +-----------+           +-----------+          +-----------+
  |   EGG   | ------->  |   LARVA   | ------->  |   PUPA    | -------> |   ADULT   |
  +---------+           +-----------+           +-----------+          +-----------+
  laid in moist         hatches from the        rests inside a         has wings, flies
  decaying matter       egg; feeds and          brown case; changes    and lays eggs
                        grows                   into an adult
       ^                                                                     |
       |                                                                     |
       +------ the adult lays eggs and the whole cycle begins again ----------+
```

*Clear four-stage cycle with an explicit return arrow. Defect: the EGG box is 9 characters wide while LARVA/PUPA/ADULT are 11, and the '------->' arrows have uneven gaps, so the cycle looks lopsided rather than evenly spaced.*

---

## P7 · Human Body — Digestion

**8 / 10**

```
   1   +-------------+
       |    MOUTH    |    teeth chew the food; saliva mixes with it
       +-------------+
              |
   2          |    OESOPHAGUS (gullet): the food is pushed downwards
              |
       +-------------+
   3   |   STOMACH   |    the food is churned with gastric juice
       +-------------+
              |
   4          |    SMALL INTESTINE: digestion is finished here and
              |    the digested food is absorbed into the blood
              |
       +-------------+
   5   |    LARGE    |    water is absorbed; the faeces are formed
       |  INTESTINE  |
       +-------------+
              |
         rectum and anus
```

*Strong. The best-aligned box diagram in the series: every box closes at cols 7 and 21 with the connector column at 14. The annotations down the right-hand side do real teaching work.*

---

## P8 · Solar System (inner planets)

**4 / 10**

```
               THE INNER PLANETS (not drawn to scale)

   Sun                    each planet moves round the Sun
    *                     along its own path (orbit)
    |
    |     1         2          3           4
    +----(o)-------(o)--------(o)---------(o)
    |
    +------------------------------------------------->
       nearest the Sun

                          --->
                    furthest of the four
```

*Weakest proper figure. No border, and it is the raggiest of all — line lengths run from 0 to 57 characters. The Sun '*', the 'o' planet rail, and the orphan '--->' and 'furthest of the four' lines below do not cohere into one figure. The four planets are identical circles, so position is the only cue.*

---

## P16 · Agricultural Tools (hoe)

**5 / 10**

```
                            (i)
                             |
                             v
              +------------------------------+
              |                              |
              |                              |
              +------------------------------+
                             |
                             |
                  +----------------------+
                  |                      |
                  |         (ii)         |
                  |                      |
                  +----------------------+
                             ^
                             |
                           (iii)
```

*Three empty rectangles. There is no hoe shape — no tapered blade, no angled neck. The (i)/(ii)/(iii) are purely positional, so the pupil gets no information from the drawing itself.*

---

## P13 · Conversion and Conservation (torch)

**7 / 10**

```
  DRY CELL            WIRES               BULB
+----------+ ---> +------------+ ---> +----------+
|   (i)    |      |    (ii)    |      |  (iii)   |
|  ENERGY  |      |   ENERGY   |      |  ENERGY  |
+----------+      +------------+      +----------+
                                           |
                                           v
                                      +----------+
                                      |   (iv)   |
                                      |  ENERGY  |
                                      +----------+
```

*Clean and well aligned, with a sensible branch down to wasted heat. A genuine flow diagram rather than a labelled box. Works well.*

---

## P12 · Electricity and Electronics (circuit)

**8 / 10**

```
        (1)             (2)
       SWITCH        RESISTOR
   +-----/ /----------[======]----+
   |                              |
   |                              |
   |                              |
   |     (3)         (4)          |
   +-----| |---------->|----------+
       BATTERY          LED
   (two dry cells in series)
```

*Strong. Uses real symbol conventions — '/ /' for the switch, '[====]' for the resistor, '| |' for the cells, '>|' for the LED. Correctly aligned: both rails close at col 34.*

---

## P15 · Force and Motion 2 (lever)

**5 / 10**

```
        (i)                               (iii)
         |                                  |
         v                                  v
   +----------------------------------------------+
   |                     BAR                      |
   +----------------------------------------------+
                          ^
                          |
                        (ii)
                         /\
                        /  \
   ------------------------------------------------
```

*Recognisable, but the effort and load arrows land at cols 9 and 44 on a bar that spans cols 3 to 50 — so effort and load appear inset from the ends instead of at them, which slightly muddles the physics.*

---

## P17 · Waste Management (compost pit)

**5 / 10**

```
                          (i)
                           |
      +-----------------------------------------+
      |                                         |
      +-----------------------------------------+
      |                                         |
      |                  (ii)                   |
      |                                         |
      +-----------------------------------------+
      |                                         |
      |                                         |
      +-----------------------------------------+
                           ^
                           |
                         (iii)
```

*Three identical stacked compartments, so nothing distinguishes them visually. The (iii) arrow points up from beneath the bottom rail, which is ambiguous: it could mean the third compartment or something underneath the pit.*

---

## Papers with no figure at all

These twelve carry no diagram, chart or map anywhere:

- Strand1_Materials
- Strand2_AnimalProduction
- Strand2_CropProduction
- Strand3_Ecosystem
- Strand3_FarmingSystems
- Strand4_Energy
- Strand4_ForceAndMotion1
- Strand5_ClimateChange
- Strand5_HumanHealth1
- Strand5_HumanHealth2
- Strand5_ScienceAndIndustry
- Strand5_UnderstandingTheEnvironment

**The two that hurt most:**

- **Strand4_ForceAndMotion1** — force, friction, gravity and magnetism is the most diagram-dependent
  topic in the whole B7 syllabus, and it has no figure. A force-arrow sketch or a magnet-field
  diagram would lift that paper considerably.
- **Strand3_Ecosystem** — food chains and food webs are inherently graphical; a simple
  maize → grasshopper → lizard → hawk chain would do more than a paragraph of text.

Also worth a figure: **Strand5_ClimateChange** (a greenhouse-effect sketch),
**Strand5_UnderstandingTheEnvironment** (a landform cross-section showing plateau/plain/
mountain/valley), **Strand4_Energy** and **Strand2_CropProduction**.

---

## Cross-cutting weaknesses

**1. One visual grammar, used six times.** The torch, the hoe, the pit, the lever, and parts of
the cell diagrams are all 'a rectangle with (i)/(ii)/(iii) floating inside'. Once a pupil has
seen two, the third teaches nothing new. The strongest figures in the set are the ones that are
*pictorial* — the water cycle, the digestive system and the circuit — because the drawing itself
carries information and the blanks test whether the pupil can read it.

**2. Nothing in Section A.** A BECE objective section routinely carries a figure-based item.
All ten figures sit in Section B theory only.

**3. Never more than one per paper.** Living Cells is the only paper with two.

**4. No scale or orientation notes** except on the inner-planets figure.

---

## What I would fix, in priority order

| # | Fix | Effort |
| --- | --- | --- |
| 1 | Rebuild the **inner planets** figure — border it, even out the line lengths, drop the orphan '--->' lines | small |
| 2 | Fix the **one-column jogs** in the two cell diagrams | small |
| 3 | Give **P1 Materials** a real bordered figure instead of the bullet table | small |
| 4 | Even out the **EGG box width and arrow spacing** in the life cycle | small |
| 5 | Move the **lever's** effort/load arrows out to the ends of the bar | small |
| 6 | Disambiguate the **pit's** (iii) arrow and differentiate the three layers | small |
| 7 | Add a figure to **Force and Motion 1** and **Ecosystem** | medium |
| 8 | Add figures to Climate Change and Understanding the Environment | medium |
| 9 | Give the **hoe** an actual blade shape rather than three rectangles | medium |
| 10 | Put one figure-based item into Section A of each paper | larger |