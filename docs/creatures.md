# Creature design

**Domain:** Biological anatomy, growth, behavior and ecological niches. **Status:** Concept/species-archetype planning, not a final bestiary.

## Scientific approach

The Rauken's fauna is invented, but starts with Late Cretaceous anatomy and fossil ecology. Document the evidence tier for each significant character:
- Direct fossil support in related taxa.
- Comparative inference from living birds/crocodilians and other relevant animals.
- Biomechanical/ecological plausibility.
- Deliberate fictional novelty.

Don't interpret a plausible feature as established for a fossil animal. Track which taxa lived in comparable regions/time windows; Hațeg fossil beds are not a snapshot of all coexistence.

## Flagship playable lineage: dwarf insular titanosaur

### Concept
Young juvenile just leaving a familiar nursery/group: a compact, inquisitive long-necked browser with proportionally expressive head and eyes, sturdy quadrupedal movement, **visibly bristly/shaggy nape and upper back**, fine pebbled skin and modest early armor nodules. Growing animal becomes thicker-bodied, increasingly powerful and wrinkled, with conspicuous embedded osteoderms and relatively sparse residual bristles.

The juvenile-to-adult skin-covering transformation is a chosen creative feature. Ontogenetic covering changes have living-animal analogues, but **sauropod quills have no confirmed fossil evidence**. These are fictional keratinous bristles, not a claim that real titanosaurs had feathers.

### Provisional physical envelope
- Starting independent juvenile: roughly 1.3–1.8 m total length.
- Adult: roughly 5–6 m total length.
- Adult mass: early working hypothesis ~0.7–1.2 tonnes; **must be recomputed from volumetric anatomy**, not taken as verified.
- Life-stage scaling cannot be uniform. Head, neck, limbs, trunk and tail have separate proportional development curves.

### Anatomy
- Physically credible sauropod skeleton, extensive neck articulation constrained by plausible movement, muscular tail and four weight-bearing limbs.
- Broadening torso, increasing body mass, changes in limb strength and center of mass with age.
- Region-specific pebbled scales and subtle rosettes, folds at compressive areas, thickened skin over shoulders/hips and major joints; avoid covering entire body in identical giant elephant cracks.
- Osteoderms: spaced subdermal round/oval plates or nodules clustered around upper back, shoulders, hips, potentially tail base. Not continuous ankylosaur armor. Count/placement/growth **fictional**.
- Quills: asymmetrical short stiff tapered filaments on nape/shoulders/dorsum in juveniles; declining proportional prominence, shedding/regional changes and retained smaller clumps in adults. Function hypotheses: communication, juvenile concealment and minor thermoregulation, not proven defenses.
- Age-specific surface wear, healing scars and nonuniform pigmentation. Juveniles may have subtle banding/mottling lost or softened with age.

### Behavior and ecology
- Generalist browser, not an indiscriminate lawnmower. Preferences vary by plant chemistry, quality, availability, season and accessibility.
- Feed within a physically plausible head/neck reach envelope; adjust browsing behavior as height and width increase.
- In ordinary play begins autonomous browsing and drinking when safe, hungry/thirsty and food/water within reach; player commands override.
- Larger adults become less threatened by small predators and more demanding in total food/water, making home ranges and routes change.
- Sociality and parental/nursery behavior require explicit research assumptions; do not assume extended sauropod parental care.

### Required anatomical output later
Scaled skeleton; mass and joint estimates; growth morphs; surface zones; integument-placement maps; armor topology; gait cycles; feeding reach; locomotion/accessibility envelope; color variability; animation interaction anchors. **Not authored in this planning-only phase.**

## Additional candidate playable strategies

1. **Small robust ornithopod-like browser:** adaptable generalist, strong jaw/beak, patterned face and scaly integument.
2. **Small feathered paravian-like opportunist:** highly inquisitive mixed forager with real geometry for silhouette feathers; specific ancestry/ecology intentionally fictional.
3. **Low armored herbivore:** small ankylosaurian-like animal with near-ground feeding strategy and osteoderm anatomy; distinguish from the sauropod's scattered plates.

Candidates should differ in access to food, terrains and shelters, metabolism, sensory priorities and maturation—not merely speed/combat bonuses.

## Nonplayer animals

Develop food-web roles before a species list:
- Herbivores of varied reach, size and food chemistry.
- Small leaf-litter/shoreline opportunists and insectivores.
- Flying animals that can disperse between islands.
- Ambush shoreline/crocodyliform analogues and occasional terrestrial predators.
- Detritivores, invertebrates, pollinators, burrowers and carrion scavengers.

Predators do not possess player-location information. They have territories, energy needs, routines, attention limits and avoidance. Most animal interactions end without combat.

## Island evolution

Lineages share ancestry but diversify under different isolation ages, soil chemistry, rainfall, plant foods and population barriers. Main Island may retain generalists; Rainridge wet-forest adaptations; Stone Island karst/dry-slope adaptations; Outer Reach old plateau specialists. Evolution is constrained by plausible dispersal routes; all lineages don't split in lockstep.

## BeastCore, HeroSim and FaunaSim

**BeastCore** holds reusable metabolism, perception, homeostasis, digestion, injury and age-dependent anatomy rules. **HeroSim** owns the player animal with the highest update responsiveness; **FaunaSim** owns wild individuals/populations with lower rates where acceptable. The same species must follow compatible biological rules in both.

**RaukenSim** supplies environment, **InteractionsCore** finite resources, **SimCore** time and developmental pacing, **RaukenState** identities/history. Juvenile growth must be perceptible in an enjoyable session, while remaining subject to nutrition and shared life history. [Architecture](simulation-architecture.md).

## Rendering interface (not implementation)

Biology emits high-resolution anatomical master and stage-specific descriptions. Rendering receives skinned bodies, quill/armor placement maps, materials, interaction bones, pose-dependent wrinkle regions and morphological parameters. Actual geometry budgets, shaders, rigs and engine choices live in [Visual direction](visual-direction.md), [Rendering experiments](rendering-experiments.md) and [Asset toolkit](asset-toolkit.md).

## Open research

Ontogenetic sauropod skeletons and independent juveniles; osteoderm distribution/function in titanosaurs; fossil skin textures; realistic sauropod browsing envelope and gut throughput; heat budgets across growth; speculative bristle ontogeny; juvenile collision/terrain adaptation; feeding from stiff vs flexible vegetation.
