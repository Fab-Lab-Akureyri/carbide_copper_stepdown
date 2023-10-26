# carbide_copper_stepdown

## Hvað er þetta / What is it?

****

Við hjá [Fab Lab Akureyri](https://www.fla.is/) notum stundum [Caride copper](https://copper.carbide3d.com/) til að gera NC/G-code skrár fyrir rafrásarfræsun. Helsti gallinn við það er að það býður ekki upp á útskurðinn í þrepum, en það minnkar:

- Álag á fræsinn
- Líkur á að platan losni frá
- Hávaða

Við Chat-GPT 4 útbjuggum því þessa skriptu sem breytir NC kóðanum fra Carbide3D frá því að fara eina umferð, yfir í að fara þrjár umferðir með 1/3 dýpt í hverri.

****

At [Fab Lab Akureyri](https://www.fla.is/) we sometimes use [Carbide Copper](https://copper.carbide3d.com/) to create NC/G-code files for PCB production. It's main flaw is the cutout generated has no option of `stepdown` or doing the passes in multiple steps, which minimzes:

- Stress on the mill
- Chances of the plate coming loose
- Noise

Chat-GPT 4 and I made this script which modifies the NC code from Carbid3D from a single pass to three passes, each with 1/3 of original Z depth. 

## Aðgát / _Warning_

Gætið að því að þetta virkar eingöngu fyrir útskurðarskrár! / _This is only meant for cutout files!_ 

Vinsamlegast notið síðu eins og t.d. [NC Viewer](https://ncviewer.com/) til að staðfesta virkni! / _Please use sites like [NC Viewer](https://ncviewer.com/) to verify the modified file!_ 

**Engin ábyrgð er tekin á einu né neinu! / _We accept no responsibility!_**

## Notkun / _Running the script_

### Vefviðmót / Online version

Kíkið [hingað](https://www.fla.is/tol/gcode_modifier/) / Go [here](https://www.fla.is/tol/gcode_modifier/) 
