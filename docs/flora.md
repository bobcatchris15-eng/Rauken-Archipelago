# Flora and fungal life

**Domain:** Plant/fungal anatomy, life histories, habitat roles and food supply. **Status:** Initial fictional roster and research constraints, not final taxa.

## Biological foundation

The late Cretaceous supports flowering plants, conifers/other gymnosperms, diverse ferns, horsetails, cycads, wetland monocots, mosses and fungi. Avoid portraying the world as only cycads and ferns, or as a modern temperate grassland. Grass lineages existed by the Late Cretaceous, but modern grass-dominated savannas must not be the default.

Invent derived species and common names for The Stalthosian Archipelago. Fossil leaf forms and pollen can guide shapes but usually do not specify whole-plant branching, color, soft tissue, toxicity or ecological role. Mark inferred traits accordingly.

The flagship sauropod is a **generalist browser with real preferences and consequences**, primarily using shrubs, tender herbs, horsetails, accessible fern species, young conifer shoots and some fruit/reproductive parts. It cannot eat arbitrary 'green biomass' equally well.

## Visual biodiversity mandate — around 200 recognizable plant forms

The aim is not twenty biologically elaborate simulated plants. It is **a luxuriant catalog of about 200 convincing, visually distinctive plant forms/species-level morphotypes**, expandable without limit, distributed plausibly across island habitats. Prioritize silhouette, branching, leaf/frond shapes, venation, arrangement, layering and near-photoreal surface response. One hundred indistinguishable recolors do **not** satisfy that goal.

The [Plant visual catalog](plant-visual-catalog.md) owns morphology-profile fields, an illustrative 200-form spread across plant architectures, distribution principles and visual QA. The table below is **a sample community and foundation for asset tooling**, not the whole species roster. Add any specific requested plant without requiring it to pass a food-web niche test. Fungi, bryophytes and background vegetation can add further diversity.

**Plant biology depth is optional** unless nearby browsing, prominent damage, a fallen tree or other visibly consequential interaction needs it. Most species can share habitat/season appearance and edible-tag templates with seeded instances or coarse patches. Morphological fidelity is the priority.

## Plant community — flagship Main Island woodland

Working organisms (names optional/provisional):

| Form | Working name | Habitat and structure | Sauropod role |
|---|---|---|---|
| Araucarian-like large conifer | Splitcrown | Tall irregular tiered crown; big barked trunk and root flare in old woodland | Sapling/low shoots, fallen foliage; strong structural habitat |
| Taxodioid-like river conifer | Riverplume | Fine branchlets, wetter ground, floodplain patches | Young shoots possible; shade/seasonal litter |
| Early broadleaf tree | Mottleleaf | Spreading 4–12 m tree, variable foliage, abundant juvenile shrubs | Shoots and low branches |
| Palm-like monocot | Fan-crown | Coastal/wet lowland fan leaves and fibrous stem | Limited young foliage or fruits where suitable |
| Riparian flexible shrub | Softbough | Dense, 1–3 m, thin leaves and arching branches | Key juvenile daily browse; deflection and local regrowth |
| Sunlit woody shrub | Copperleaf | Red-toned young growth, terraced woodland edges | Seasonal tender browse |
| Drought-tolerant shrub | Spindlebrush | Narrow waxy leaves, lower sandy plains | Lower quality or drought fallback |
| Small-fruited shrub | Knuckleberry | Branching clusters with small fruits | Leaves and seasonally fruit |
| Rock-fracture shrub | Cleftroot | Shallow roots over stone, crevice specialist | Occasional sheltered browse, structural cover |
| Royal-fern analogue | Royal frond | Moist woodlands, large fronds | Young fronds variably palatable |
| Giant marattioid-like fern | Basketfern | Tall, architectural, humid hollows | Distinct large leaves; slower recovery |
| Branching disturbance fern | Forkfern | Scoured slopes, sunny openings, tangled mats | Patchy browse and dense cover |
| Horsetail | Jointreed | Segmented vertical thickets in wet soil | Important forage candidate; silica and age matter |
| Strap-leaved marsh herb | Ribbonherb | Damp hollow rosettes | Tender foliage |
| Seasonal angiosperm herb | Spearleaf | Soft stems, open damp woodland | Important seasonal food |
| Low flowering ground cover | Beadflower / creeping broadleaf | Clearing and riparian patches | Juvenile low browse and insect resource |
| Grass and grasslike forms | Needlegrass analogue | Tufts, disturbed sand/gravel, not blanket savanna | Incidental, especially young growth |
| Cycad analogues | Stonecrown / Tallcrown | Rocky slopes, open woodland, stiff rosettes | Mostly structural; chemical defenses, avoid default safe forage |
| Aquatic angiosperms | Waterstar | Pools, backwaters, shallows | Variable food; wetland structure |
| Cliff mosses / liverworts / lichens | Multiple | Rock seepage, rotten wood and stable shaded soil | Moisture and appearance, not significant staple browse |
| Gilled, bracket, crust and coral fungi | Multiple | Logs, litter, soil, damp hollows | Decomposition, episodic fruiting, incidental consumption |

This table is not a commitment that all species coexisted in the exact real Maastrichtian Hațeg Basin. All Stalthos taxa are fictional.

## Island divergence

- Rainridge: shade-tolerant ferns, persistent epiphytes, tall sheltered broadleaf growth, humid rock-face specialists.
- Stone Island: limestone cracks, drought-tolerant leaf structures, sinkhole refuges and spring-associated flora.
- Outer Reach: mineral-stressed low woody parasols, waxy leaves, exposed crown forms on the Iron Crown and comparatively rich isolated Green Hollows.
- Main Island: continuum of rocky upland conifers, deeply wooded ravines, broadleaf riparian patches and sandy lowland herbs; isolated caprock buttes create dry/talus niches.

Related plants should share visible morphology and reproductive traits across islands, not be unrelated theme-park species.

## Plant simulation requirements

Each taxon/profile defines:
- Body plan, botanical reference group, potential mature dimensions and growth stages.
- Branching/leaf arrangement, roots, stems, foliage turnover and reproductive structures.
- Establishment (light, moisture, substrate and soil chemistry).
- Seasonal phenology, regrowth, reproduction, dispersal.
- **Simple forage tags:** accessible parts (leaf/shoot/fruit/seed), approximate palatability/nutrition, water content and notable defenses/silica where visually or behaviorally meaningful—not a precise nutrient chemistry model.
- Browsing accessibility by animal height and mechanical interaction envelope.
- Disturbance response: flood, drought, branch damage, trampling, death, decomposition.

Use normalized biological properties where evidence is unknown; nutritional values are experimental parameters, not fossil measurements. Avoid translating in-vitro rumen fermentation data directly into sauropod-specific calories.

## FloraSim lifecycle

**FloraSim** owns individual trees, distinctive shrubs, plant colonies and fungi independently of render chunks. Permanent species/habitat suitability is mostly map-generated (soil, moisture, water distance and relative elevation); **StalthosSim** supplies coarse seasonal/weather condition signals, not historical weather reconstruction. FloraSim updates growth lazily on **batched spatial-state requests** or discrete browsing/storm events; **no per-rendered-plant polling**.

Prominent tree geometry uses stable IDs/seeds and saved **conspicuous** structural exceptions in **StalthosState**; normal branches/foliage need not be individually persisted. **InteractionsCore** coordinates immediate local feeding/visible change, not a complete biomass ledger. See [FloraSim](flora-sim.md).

## Food, regeneration and display

The dinosaur approaches eligible flora; a reach and preference query identifies edible parts. Feeding animation directs to actual branches/fronds/patches and updates consumed biomass. Shoots disappear, bend or reduce density plausibly. A plant with repeated grazing can show reshaping or depletion across visits.

Do not use the same geometry technique for all plants. Woody trees, ferns, segmented reeds, moss and broadleaf shrubs have distinct morphology and wind/material needs. This document owns **organism shape and behavior**; the visual and toolkit documents own rendering representation.

## Initial production set

Before the full flora catalog, build six reference assets/species to exercise production: Splitcrown (tree), Softbough (interactive edible shrub), Jointreed (dense stems), Royal frond (fine leaflets), Basketfern (large architectural fronds), and bracket fungus on decomposing wood (substrate integration).

**Superseded breadth targets:** the former 25–35-per-watershed / 80–120-archipelago estimates are no longer the catalog ambition. Target **around 200 visually recognizable plant morphotypes across the archipelago**, with any additional requested taxa welcome; see [Plant visual catalog](plant-visual-catalog.md). A local watershed should still have coherent dominant plants rather than all 200 at once. Begin with six reference species to prove the authoring pipeline, then expand visual families progressively; this is **not** 200 detailed biological simulators or a mandatory immediate production gate.

## Research needed

Maastrichtian vegetation by climate/substrate in European islands; conifer and angiosperm branching analogues; horsetail and fern digestibility variation; cycad toxins and feeding specialists; Cretaceous monocots and grasses; fern pinna morphologies; rooting/substrate in rock cliffs; sapling growth and herbivory feedback; fungal fruiting and decay.

## Boundaries

No shader recipes or polygon counts here: [Visual direction](visual-direction.md). No engine APIs: [Rendering experiments](rendering-experiments.md). No CLI generator contract: [Asset toolkit](asset-toolkit.md).
