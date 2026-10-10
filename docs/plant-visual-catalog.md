# Plant visual catalog — richness before botanical machinery

**Status:** Expandable visual-biodiversity design, not a locked taxonomy or content limit. **Working breadth ambition:** **around 200 recognizably different plant appearances/species-level morphotypes** across the Stalthosian Archipelago, with additional fungi, mosses, lichens, seasonal forms and individual variation. **Two hundred is a creative diversity goal, not a mandatory first-release gate or maximum allowed number.** A requested individual plant species/form can always be included regardless of category allocation or whether a simulated niche 'needs' it.

## Desired illusion

A camera-level woodland should seem naturally overgrown with **many independently recognizable structures**: canopy outlines, shrubs, odd leaves, fern architectures, vines, marsh plants, seedlings, broken vegetation, litter and fungi. **Two hundred believable silhouettes and leaf systems are preferable to twenty intricately simulated plant species.** If tradeoffs are needed, spend work on reference-based mesh/branching/leaf construction, surface response, composition, habitat blending and nonrepetitive variation; not invisible individual growth, genetics or nutrient chemistry.

Count **distinct morphology**, not skins or individual instances. Ten slightly different green materials on the same branched mesh are not ten recognizable plants. Related fictional species may legitimately share a family look, but each cataloged form should carry noticeable morphological cues at its typical viewing distance.

## Production profile for each visual plant form

- **Visual identity and source inspiration:** fictional working name/ID, broad botanical family or morphological analogy, references/evidence caveats.
- **Whole-plant silhouette:** height/spread, architecture/branching, root flare/trunk posture, crown density, leaf/rosette cluster placement; young/mature distinctions if prominent.
- **Leaf/frond architecture:** overall shape, margins/lobes, venation, pinnation, phyllotaxis, curvature, thickness, underside, petiole/rachis arrangement and branch attachment.
- **Surface/color:** bark, wax, hairs, edge wear, translucency, normal/roughness variation, age and wet/dry differences without visual noise.
- **Composition:** island, substrate, light/moisture aspect, canopy layer, grouping tendency, density/rarity, neighbors, seasonal flower/fruit/crown changes.
- **Minimum scene behavior:** wind/stiffness, age/season variation, one interaction type if conspicuously browsable or pushable. Most plants need **no complex individual physiology**.
- **Production linkage:** generator family, seed+parameter schema, source/master/optimized assets, validation/turntable previews and hardware/LOD constraints.

## Suggested visual diversity coverage (illustrative, not quotas)

| Morphological collection | Example visual profiles | Variation worth authoring |
|---|---:|---|
| Conifers and other large gymnosperms | 22 | Tiered crowns, branch whorls, needle/scale sprays, squat wind forms and drooping riparian forms |
| Early flowering trees | 28 | Layered branching, leaf arrangement, lobes, venation, irregular crowns and seasonal leaf behavior |
| Shrubs and woody understory | 34 | Arching/spherical/spiny/thicket structure; contrasting leaves, fruit clusters and low browsing silhouettes |
| Ferns and fern allies | 35 | Pinna shapes, branching fronds, epiphytic rosettes, tree-fern crowns, drooping walls and delicate clumps |
| Horsetails and rush-like forms | 13 | Jointed stems, branch whorls, reed curtains, bog tufts and hard-edged vertical stems |
| Flowering herbs and ground rosettes | 33 | Broad/lobed/strap/compound leaves, inflorescence architecture, height and seasonal blooms |
| Cycads, ginkgo-like and other distinctive seed plants | 10 | Stout crowns, fan leaves, rigid pinnate rosettes, branching trunks, unusual reproductive structures |
| Aquatics and marsh plants | 12 | Floating leaves, emergent rosettes, submerged ribbon growth, wetland margins |
| Climbers, vines and epiphytes | 13 | Twining vs clinging, tendrils, pendant masses, perched rosettes, bark-embedded forms |
| **Total working palette** | **200** | These are suggested profile slots, not a demand for 200 per-plant simulators |

Fungi (gilled/bracket/coral forms), mosses, lichens and forest-floor material mixtures can **expand beyond** this palette. Their exact count does not constrain other plants. No false implication that every listed form is a demonstrated Maastrichtian species.

## Habitat composition and island individuality

- **Main Island:** Baraboo-style rocky woodland, mossy ravines, shaded creek terraces, broad sandy lowlands and isolated butte crowns each receive visually different mixtures; some recognizable lineages bridge them.
- **Rainridge:** dripping ferns, fine-leafed damp canopy, climbing growth, cliff rosettes, epiphytes, fungal structures and sheltered broadleaf thickets.
- **Stone Island:** dry open limestone canopies, cliff-rooted shrubs, karst hollow verdure, surprising spring-fed enclaves, tough or waxy leaves.
- **Outer Reach:** wind-pressed plateau woody forms, mineral-substrate specialists, strongly contrasting spring-fed Green Hollows and coastal spray-tolerant vegetation.
- **Avoid biome wallpaper:** not random scatter from a single global distribution. A few locally dominant forms give habitats coherence; uncommon understory and transitional forms give them discovery value. Allow repetitions in the *right* habitat, but avoid conspicuous identical assets in close view.

## Share geometry machinery, not necessarily appearance

Build **botanical form generators** by true structural family, e.g. branch-bearing trees, layered shrubs, compound ferns, jointed horsetails, rosettes, vines, aquatics. Use automated high-resolution sourced geometry and calibrated materials, then generate LODs/instancing and validation shots. Shared code should support strongly different parameters and source textures; don't produce 200 reskinned copies of six primitives.

**Simulation should be shallow by default:**
- **Most plants:** deterministic seed + habitat/season + morphology profile + density/instance position; no individual runtime biology or saved record.
- **Browsable patches:** small cover/density/available-forage tags and visible nipped variants, with lazy approximate recovery.
- **Prominent long-lived trees, important interactive shrubs and conspicuous events:** compact persistent tree/fall/pruning/appearance exceptions so observed changes remain believable.
- **Very close contact:** geometry/leaf bend/push and finite displayed foliage where visible; motion and contact accuracy outrank nutrient precision.

A small set of edible quality tags is enough to distinguish soft tender foliage, stiff or silica-rich plants, fruits, toxins or inedible structural leaves. Do not require a unique botanical growth model, nutrient network or per-leaf agent for every visual species.

## Camera-based diversity QA

1. **Silhouette atlas:** neutral-background turntables at consistent scale, including crown/ground footprint and characteristic leaf or frond close-up. A random selection of 20 profiles should be distinguishable even without color.
2. **Leaf atlas:** side-by-side shape, margin, venation and arrangement; identify accidental duplicates caused by generator defaults.
3. **Real habitat scenes:** test dense mixed understory, tree crowding, lighting, wind, contact and seasonal variation at juvenile Hero Beast head height—not just sterile specimen renders.
4. **Repeat-exposure test:** several minutes strolling through each habitat should not make a handful of shapes dominate every sightline through obviously identical repetition.
5. **Performance gate:** instance culling, shader costs, material/atlas reuse and streaming fit 1080p GTX1080/early Ryzen at the agreed 30fps floor, with visual quality judged in same-scene comparisons.
6. **Open-ended additions:** adding the user's desired plant requires a morphology profile, reference/asset and placement tags; **never** force expansion of FloraSim just to satisfy a food-chain or population-balance model.

## Authoring sequence, not a 200-species prerequisite

First, use the existing six reference plants to validate the authoring/rendering pipeline. Next, exercise **radically contrasting morphology families** in a mixed scene; produce variation atlases and automated quality comparisons. Expand the form catalog progressively as tools become reliable. Catalog richness should never require completing 200 detailed ecological records before a visually satisfying woodland can be rendered.

**Related:** [Flora](flora.md), [FloraSim](flora-sim.md), [Fauna catalog](fauna-actor-catalog.md), [Ecology](ecology-and-hydrology.md), [Asset toolkit](asset-toolkit.md), [Visual direction](visual-direction.md), [Geography](geography.md).
