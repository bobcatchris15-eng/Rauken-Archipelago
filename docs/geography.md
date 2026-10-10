# The Rauken — geography and island history

**Status:** High-level world direction with provisional dimensions. **Primary value:** evocative geography that invites curious exploration.

## Formation thesis

The Rauken is a deeply eroded, partly drowned continental upland system: ancient resistant ridges, differentiated bedrock, fault-bounded basins, river networks, and long-lived erosion precede marine inundation. The sea enters former valleys, leaving branching rias, headlands, narrow rocky inlets, irregular peninsulas, offshore rock towers and surviving hilltop islands.

**Do not generate four generic islands independently.** Generate (or author against) shared geological structures and drainage history, then separate the highlands at different episodes of relative sea-level change, subsidence and fault motion.

Ria-like inlets are flooded river valleys, *not* cold-climate glacial fjords. The fictional world need not preserve Earth's actual geological history; it should preserve causal legibility.

Four major islands plus scattered islets, reefs and coastal remnants. Islands separated at different times so lineages can diverge differently. Flying fauna and rare rafting/swimming continue limited exchanges.

## Revised scale

Prefer ARK: Survival Evolved-like **landscape density** and travel practicality over enormous literal continental geography. Working *bounding extents*:
- Main Island: about 7–8 km across its longest span; roughly 20–30 km² land.
- Rainridge: 5–6 km maximum span; about 10–15 km².
- Stone Island: 4–5 km; about 5–9 km².
- Outer Reach: 5–6 km; about 8–12 km².
- Scattered small islands, promontories, skerries and shoals.

These are **deliberately provisional** and may prove too small for all desired habitats, drainage relief or isolation narratives. Build representative terrain first and tune dimensions based on traversal. Size estimates are not settled map specifications.

## Island profiles

### Main Island — recently connected core
- Principal reference population and richest connected habitat mosaic.
- One large interior province transitions from **Baraboo Range / Driftless Area-style resistant quartzite-like bluffs and deeply dissected wooded ridges** into **Central Wisconsin Plain-like broad sandy lowland** toward one coast.
- Isolated taller **caprock-preserved buttes/mesas** punctuate the lowland; deliberate Wisconsin Sandstone analogues, potentially unusual buttes with cliff faces, talus and dry crowns.
- Broad enough alluvial valleys and wetlands for functional animal populations.
- Irregular coast where old tributary valleys were drowned; sheltered rocky coves and inland fingers of sea.
- Signatures: secluded mossy ravines, spring-fed rock clefts, great outcrops, visible far-distance butte silhouettes, quiet wooded basins, wet coastal reaches.

### Rainridge — older-separated wet highland
- Proposed last durable terrestrial connection ~6 million years before setting (not fixed).
- Crooked, crescent or split-crown ridges, dramatic exposed needles, deeply branching drowned sounds.
- Rainward valley forests and mossy gorges; cloud/mist-prone high crown; more seasonal and productive leeward basin.
- Mountain passes and constrained drainage create population subdivision even within the island.
- Climate gradients follow rainfall and topography, not arbitrary biome borders.

### Stone Island — comparatively recent isolation
- Proposed isolation ~0.8 million years before setting; revisit under changing sea levels.
- Differentially eroded limestone and mixed sedimentary platform: sinkholes, springs, karst hollows, arches, caves, dry rocky woodland, coastal terraces.
- Surface water often patchy despite underground reserves; enclosed fertile pockets contrast with exposed dry slopes.
- **Less specified than the other islands**; keep concept flexible until a focused pass.

### Outer Reach — oldest persistent separation
- Proposed deep-water isolation ~12 million years before setting (relative chronology important; dates not fixed).
- Very old broken plateau with weathered ultramafic/mineral-rich tracts (potentially laterite), exposed iron-colored high ground, coastal sea towers and eroded escarpments.
- Three primary ecological landscapes: **Iron Crown** open rocky plateau, **Green Hollows** productive spring-fed protected basins, **Outer Teeth** storm-battered stacks, cliffs, broken ridges and occasional sheltered inlets.
- Persistent deep passage prevents recurrent low-sea-level land bridges; exceptional colonization still possible.
- Endemic plants and animal lineages should reflect selection, turnover and dispersal—not cartoonishly frozen 'living fossils'.
- Candidate landmarks: Great Needle, Hidden Basin, Old Table, Stillwater Inlet. Working geographic names only.

## Marine geography and crossings

- Sea is physical terrain, not a travel menu.
- Sheltered channels, marine arms, exposed open-water gaps and rare offshore islets differ in surf, current, salinity, access to landing and fresh water.
- Most terrestrial individuals **never cross**; curiosity may drive an unusual player to attempt a crossing.
- Small swimmers can be swept laterally, exhausted, stranded on dry islets or unable to land at cliffs. No mandatory island progression.
- Some shallow crossings between younger islands may be rarely traversable; Outer Reach remains materially more isolated.

## Feature-density rule

**Compress distances; exaggerate compelling formations; preserve geology and hydrology.** Favor engaging, fairly dense topography over exact probabilistic occurrence of every landform.

Distribution by scale:
- Kilometers: ridges, drainages, drowned sounds, plains.
- Hundreds of meters: ravines, bluffs, saddles, springs, basins, coves.
- Tens of meters: rock alcoves, seep bowls, shelves, fallen trees, small backwaters.
- Meters: crevices, fern pockets, root masses, damp ledges and pebbly margins.

Keep some ordinary spaces: every bend cannot be a cave or waterfall. Interest comes from contrast, landmark sightlines, and layered routes rather than sheer novelty count.

## Reference landscape: Splitstone Valley

A *provisional* ~5 km upland-to-coast stream course on Main Island, developed as a design exercise:
1. Hard-rock spring headwaters and rocky saddles.
2. A deeply shaded gorge ('the Split') with low cascades and boulder passages.
3. Widening middle woodland valley with lower terraces, tributary hollows and a sheltered Seep Bowl.
4. Sandy lower country and isolated caprock butte.
5. Shallow freshwater/brackish transition into a sheltered drowned mouth.

This is a **reference watershed, not fixed map geography**. First test a **fully traversable ~1×1 km patch** with creek, ravines, outcrop, open valley floor, woodland and sheltered wet hollow. Judge density in a build before committing dimensions.

## Open questions

Island orientations; winds and latitude; separation sequence and local relative sea-level history; normal ocean current strength; precise area and relief; how far the Main Island interior transition can compress without feeling like a biome theme park; Stone Island's definitive character.

## Simulation boundary

Landform geometry, stream positions, springs and general moisture/suitability fields are primarily **map-design outputs**, not expensive ongoing geology. [RaukenSim](rauken-sim.md) handles day/night, weather, seasons and exceptional transient flooding; [FloraSim](flora-sim.md) uses those map fields to determine plant growth and health. Organism/geographic identity persists through [RaukenState](simulation-architecture.md).
