# World generation and spatial composition

**Domain:** Geological authoring, terrain construction, habitat inputs and spatial validation. **Status:** Planned experiment, not an implementation decision.

## Principle

Generate credible *relationships* between rock, drainage, coast, vegetation and navigability, then deliberately intensify the most engaging features. Do **not** simulate full geological time at runtime. The goal is a persistent beautiful world, not a numerical geological research model.

**Explicit aesthetic mandate:** The Stalthosian Archipelago favors dense, evocative terrain, sheltered mossy ravines and inlets, dramatic outcrops and irregular drowned uplands over strict average-frequency geological realism. Judge the balance inside a traversable environment rather than settling it from paper dimensions.

## Layered offline pipeline

1. **Ancient foundation:** assign crustal blocks, strata, resistant rock belts, uplifts, faults, fold orientation, basins and erodibility fields across one connected ancestral landmass.
2. **Long erosion:** derive drainage networks and watersheds; cut tributary hollows, dissect uplands, widen softer valleys, leave resistant crests, buttes, mesas, pinnacles and talus slopes.
3. **Deposits and groundwater:** place alluvial terraces, sands, clays, rubble, hard caps, water tables and spring lines consistent with lithology.
4. **Fragmentation and inundation:** model relative submergence at successive geological ages. Old valley networks become branching marine inlets; ridgelines become crooked peninsulas; high remnants become islands.
5. **Coastal modification:** add wave-exposed headlands, sheltered coves, sea caves, spits, boulder shores, skerries and steep inaccessible landings according to wave exposure and substrate.
6. **Present-day drainage:** solve current freshwater flow, sinks, tidal reaches, marshes, floodplains and seasonal pools. The pre-flooding river network and contemporary catchments must remain distinguishable.
7. **Microhabitat parameters:** derive sun/shade, wind shelter, rain exposure, moisture, soil, substrate, salinity, and canopy potential.
8. **Ecological population:** distribute plant communities and animal niches based on these fields, not noise-layer palettes.
9. **Visual/streaming preparation:** generate geometry, mesh overlays, material masks, collisions, chunk dependencies, instances, and distant appearance from the same world state.
10. **Manual/agent composition review:** identify landmarks and weak areas; strengthen selected landforms while rerunning hydrological and navigational validation.

An optional 'feature interest' field may bias local relief, rare formations, ravine intersections or visual juxtaposition. It cannot simply scatter arbitrary arches/waterfalls unrelated to geology.

## Terrain representation

- Heightfield or streamed terrain tiles for broad ground.
- Local real 3D meshes or SDF/voxel patches for undercuts, arches, overhangs, caves, ledges and vertical cliffs.
- Blended material and collision interfaces; no visible seams at terrain/rock mesh intersections.
- Offline erosion and geometry processing only for ordinary terrain evolution; runtime floods temporarily cover preset areas, with rare discrete debris/rockfall. No routine stream migration, sediment transport or terrain erosion simulation.
- Stable seeds and landmark identities. Don't regenerate a known rock tower into a different shape when its tile reloads.

## Player-scale composition

Compose on four nested scales:
- Whole island: strong silhouette, ridge directions, wet/dry gradients, sea gap logic.
- Watershed: connected routes, stream network, floodplain or gorge progression and sightlines.
- Home range: sheltered resting areas, accessible food and freshwater, alternate travel routes, nearby distinct microhabitats.
- Contact scale: rocks, roots, mud, logs, pools, moss, fern stands and convincing place-to-place transitions.

A 30-meter rock gully is significant to a juvenile animal. Include natural alternatives and occasional difficult one-way passages without deliberate platformer obstacles.

## Animal-scale traversability and direct-control test surfaces

Provide actual navigable/collision surfaces and material properties suitable for competent species-specific locomotion: traction, support/softness, step clearance, usable turning space, sloped creek margins and water-to-land exits. Off-line broad connectivity is useful for **destination navigation and finding technical defects**, but a pathfinding rejection is never a hard barrier against direct player movement if the local physics allows an attempt.

The default direct-steering locomotor controller handles ordinary footing and **small local obstacle corrections**. A larger bypass falls outside HeroView's central-third-wide *screen-space lateral detour allowance*, whereupon HeroSim stops the animal to inspect the obstacle until player direction changes or control releases. This screen-space policy is not a terrain-generation classification: don't sculpt all boulders into safe bypasses or guarantee passages for every life stage. Test a low rock, a branch, a tall boulder and an actual impassable ravine bank in both direct and destination intent modes.

## Benchmark landscape: Splitstone

Build **one roughly 1×1 km traversable test patch** before deciding larger regional proportions. It should include:
- A continuous stream descending through a fractured rocky ravine into a more open valley.
- One substantial visible bluff/outcrop or caprock remnant.
- Sheltered wet hollow/seep and moss-covered rocks.
- Mixed open and closed woodland, ground vegetation and a small reachable freshwater margin.
- Multiple plausible routes and a couple of physically inaccessible cliffs.

Scale based on **juvenile-dinosaur travel speed, camera height and browsing behavior**, not human walking height. A separate full-watershed sketch (~5 km) is a reference for future extension, not a fixed requirement.

## Generation variants and acceptance

Make interest density, relief, ravine branching, prominence of resistant strata, small rock features, openness, cover, and hydrological variability adjustable. Generate three or more profiles of identical seeds and inspect them in motion.

Compare:
- landmark recognizability and travel curiosity;
- watershed continuity and believable drainage;
- apparent ecological viability;
- route diversity/terrain traps;
- excessive feature repetition or geometric motifs;
- asset density and CPU/GPU build/runtime cost.

A successful generated scene should allow ordinary stretches of woodland between dramatic places. No universal spacing rule for points of interest.

## Outputs needed by other domains

Geography mesh and collision; terrain stratigraphy/material IDs; slope/aspect; stable streams/springs and floodplain masks; **precomputed moisture/suitability fields from water proximity, relative elevation, soils and climate**; canopy and soil fields; fauna-accessible surfaces and routes; coastline/tide/salt maps; landmark persistent IDs; spatial chunk hierarchy and source seed provenance.

Engine-neutral export is preferred until rendering experiments select Flax or Wicked. See [Geography](geography.md) and [Ecology](ecology-and-hydrology.md).

**Simulation boundary:** world generation supplies static terrain/water/soil inputs. [StalthosSim](stalthos-sim.md) supplies weather and short-lived flood conditions; [FloraSim](flora-sim.md) determines which plants thrive; [StalthosState](simulation-architecture.md) stores persistent biological/geographical identities.
