# Visual direction and quality contract

**Domain:** How organisms and landscapes must look and move. **Status:** Engine-independent creative specification.

## Aim

Approach the visual credibility of natural-history photography in a warm fictional late-Cretaceous island environment. Protect silhouette, proportion, physically coherent surface response, scale cues, meaningful material variation and environmental contact before spending budget on extreme geometry.

The player's body scale matters: camera near a juvenile dwarf sauropod's head, where common ferns become major forms and a few-meter bank is an obstacle. Every layer must stand up to movement, not just a promotional still.

**Do not equate realism with dull colors.** Creatures and plants may be striking, patterned and unfamiliar, but should have believable pigmentation, wear, function, variation and environment adaptation. Preserve the ancient-feeling irregularity of rock and vegetation.

## Environment image language

- Ancient, heavily eroded, flooded highlands: branching inlets, steep wooded ravines, quartzite-like ribs, caprock buttes, cliffs, boulders, shelters and weathered outcrops.
- Vegetation must follow sun, moisture, wind, substrate, salinity, successional stage and competition rather than uniformly random scattering.
- Excellent **ground integration**: tree root flares, foliage accumulating against rocks, damp margins and seep lines, realistic soil/rock blending, vegetation partly obscuring stems, realistic fallen material.
- Contrast matters: rocky open plateau next to green seep gorge; ordinary woodland before an immense bluff; exposed storm coast vs glassy sheltered inlet.
- Motion: leaves and branches move with correlated wind fields; small structures tremble, trunks bow less; local animals bend nearby plants.
- Sky and light: plausible solar/ambient balance, soft bounce in shade, leaf transmission, restrained haze, wetness after rain. Avoid crushed black woodland shadows or uniformly bright leaves.
- River/coast: freshwater, brackish and marine conditions can look different; shore contact and flowing water direction must be consistent with terrain.

## Biological appearance

### Dwarf sauropod
- Juvenile: true juvenile proportions; small pebbled scales, relatively taut skin, lively head/neck motion, asymmetric **bristly/shaggy nape and dorsal shoulder outline**; low emerging osteoderm bumps.
- Mature: larger body mass and barrel-shaped torso, thickened joints, folds developing around compression regions, weathering, scattered raised embedded osteoderms and much sparser visible bristles.
- Quills are a fictional adaptation. No mammalian coat, no full porcupine suit, no evenly spaced video-game spikes.
- Skin details: large anatomical folds from geometry and corrective shapes, intermediate scale rosettes from normal/roughness maps, fine surface microtexture and region-specific pigmentation.
- Face: eye orientation, blinking, breathing, jaw movement, subtle gaze; avoid human expressions.
- Motion: planted feet on slopes, center-of-mass shifts, tail counterbalance, non-sliding gait, neck compression, appropriate weight and inertia.

### Other animals
Distinct gait/body plans by niche. Feathers use modeled outer feathers where silhouettes matter and simplified body surface elsewhere. Armor must be grounded in anatomy. Population variation must not be just uniformly random colors.

### Plants
An actual fern has a rachis, pinnae, curved fronds and age diversity. Trees have defensible branching and crowns; shrubs display branching hierarchies and young vs mature shoots; horsetails have recognizable segments and colonies. Avoid ubiquitous flat crossed cards.

## Species richness as a visual acceptance criterion

**Fauna breadth:** about 50 non-hero species is an initial flexible actor palette, not a limit. Distinguish species through anatomy, mass, gait, posture, integument, movement rhythms, calls and signature routines. No recolored shared rig counted as a convincing distinct animal without actual structural/movement changes.

**Flora breadth:** about 200 botanical silhouettes/leaf architectures is the expandable working ambition, **not** 200 deep growth simulations. Evaluate branching/crown envelope, frond/pinna shape, leaf outline, venation and placement, rosettes, bark, fruiting structure and habitat form. Make local communities coherent, with repeated dominant species balanced by uncommon discoveries; don't distribute every plant everywhere or fill forests with uniform random noise.

**Mandatory artistic review method:** species silhouette/contact sheets without texture colors, leaf shape/arrangement atlases, life-scale turntables, motion samples and realistic densely planted camera walks. A specimen that looks unique only when labeled has not yet supplied meaningful biodiversity. Judge from the Hero Beast's height and at ordinary travel distance, not just studio macro views. Performance and asset representation must scale with quantity without reducing near-view credibility.

The numbers are **creative directional targets, not fixed limits or release blockers**, and do not constrain requested special animals/plants. See [Fauna actor catalog](fauna-actor-catalog.md) and [Plant visual catalog](plant-visual-catalog.md).

## Material standards

Physically based textures calibrated under neutral test illumination:
- Base color without baked photographic directional light.
- Roughness/normal variation appropriate to bark, rock, skin, waxy leaves, water and organic litter.
- Leaf thickness/transmission approximation; do not require expensive general-purpose subsurface scattering.
- Physically believable scales across assets: stone grains, epidermal detail and bark texture are neither giant nor subpixel noise.
- Wetness and decay come from shared environmental state, not unrelated texture swaps.

High-resolution source masters are retained; game assets are optimized derivatives. No supplied/generated image may become an anatomical authority without actual research verification.

## Non-negotiable motion/contact checks

- No foot sliding, body floating, plant hovering or cliff/terrain seam popping.
- Realistic reach when feeding; selected vegetation visibly changes and recovers.
- Inertia-aware neck and tail motion; subtle pose-dependent wrinkles at key joints.
- Foliage interaction near moving animals, without per-blade physics.
- Detailed local water ripples/foot wetting and plausible mud contact where relevant.
- On-screen spatial repetition should be difficult to notice; generated variants retain species morphology.
- LOD transitions preserve apparent silhouette and color without conspicuous pop or shimmering.

## Authority boundary

**StalthosSim** determines actual weather, wetness and flood; **FloraSim** owns plant condition; **HeroSim** and **FaunaSim** own animal states using **BeastCore**. The renderer may animate each frame but cannot alter biological time, resource ownership or current weather. Plant chunk loading uses **StalthosState** snapshots; **InteractionsCore** publishes changes. See [Architecture](simulation-architecture.md).

## Render-cost-independent acceptance

For every representative asset/scene, preserve: reference provenance, turntables in neutral and outdoor illumination, moving camera passes, near/mid/far comparisons, material diagnostic renders, and roughness/normal/alpha checks. A visual review must approve image quality *and movement*, even if quantitative benchmarks are good.

The 30 FPS hardware target is a separate **engineering gate**, not a license to make assets visibly poor. See [Rendering experiments](rendering-experiments.md). Proposed compromises must be demonstrated in A/B images and timed captures.

## Sound and perspective

The environment should have meaningful **spatial acoustic identity**: distinguish stream sound, distant weather, footsteps, rustling plants, animal calls and occasional natural silences. Use positioned sources and coarse habitat ambience rather than requiring a simulated agent for every insect.

HeroView's spatial-audio listener follows the camera, including bounded detached observation over a hill. HeroSim's animal hearing remains anchored to the actual head/body. A hidden call can therefore be *heard by the player* but not by the animal, which continues natural behavior until its own senses register it. Keep camera transitions/crossfades smooth; physiological feedback may be subtly layered without sounding physically near a distant camera. Do not use the player's audio perspective to trigger HeroSim alarms or supernatural knowledge.

## HeroView framing and camera embodiment

HeroView's orbit/follow camera retains its chosen orientation and lets Smalltrotter cross the composition, tracking her *position* smoothly rather than forcing a behind-the-animal camera. A bounded locally detached camera may rise above a nearby ridge, not fly to another island. Use careful collision/occlusion handling, avoid abrupt snapping at the tether, and let world/audiovisual presentation be independent of her actual sensory knowledge. Controls are body-relative (W always forward from the animal); the camera must not redefine her heading. See [HeroView](hero-view.md).
