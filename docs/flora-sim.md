# FloraSim — persistent botanical life

**Domain:** Individual and population plant/fungal ecology; **status:** conceptual subsystem plan.

## Authority

FloraSim owns living trees, shrubs, ferns, herbaceous populations, moss-like colonies, fungal systems, botanical growth, lightweight establishment/suitability, damage and death. It does **not** own rendered plant instances, atmospheric weather, animal decisions or frame-by-frame updates.

A plant may be ecologically elaborate while rendered with one simple distant mesh. A thousand dense grass blades may be one population-patch record.

## Representation

**Individuals:** prominent/long-lived trees, significant shrubs, large ferns/cycads and plants with distinctive browsing scars. Each substantial tree has a stable *logical identity* (region/placement ID or durable ID), species, location, deterministic branching seed, establishment/growth information and any meaningful structural overrides. **Identity does not imply a separate heavyweight persisted row or per-tree update loop:** unchanged baseline trees can be reconstructed from world/region seeds; only meaningful mutable differences need compact records. New trees established later receive durable identities.

**Population/colony patches:** grasses, reeds, horsetails, small herbs, mosses and fungi where organism-level tracking would be wasteful. Stable patch ID, species mix, coverage, density, age/size distribution, available edible biomass, health, cohort change and last-evaluated time.

Organisms/patches use environmental baseline fields from world generation and **coarse current season/condition signals** from StalthosSim. **Where state differs from its deterministic baseline**, compact records and relevant event/checkpoint information live in StalthosState. Do not store generated meshes or an endless replay log for every tree.

## Biological region activation ahead of rendering

When **SimCore** activates a simulation chunk around Smalltrotter (including buffer beyond HeroView's bounded detached camera), FloraSim builds plausible local botanical appearance from habitat distributions, stable seeds, coarse seasonal condition and any player-visible saved exceptions.

This means all visually required plant instances/colonies have a biologically coherent source **before** the renderer requests the camera-visible chunk; it does **not** require independent ticking of every rendered stem. Trees and other durable specimens preserve identities/damage; low cover can be dense geometry derived from one ecological population patch.

The renderer may ask for batches of the already-derived state without making individual plants poll the climate or grow merely because the frustum touched them. See [Spatial activation](spatial-activation.md).

## Lazy advancement

Normal flora advancement is **cheap scene reconstruction**, not replaying complete plant biology.

- Rebuild most plant appearance from habitat, fixed identity/seed, current season and elapsed-time growth/recovery approximations.
- Use a small cover/food-availability value for browsed patches. A recently eaten shrub can show missing shoots or lower foliage density; it recovers gradually enough to look credible.
- Save specific exceptions for conspicuous dead/uprooted trees, broken landmark branches or visibly altered plants; seed generation must honor these exceptions.
- Updated close vegetation can trigger a **localized graphical change**. Do not rebuild the entire forest actor for each bite or give every branch a growth timer.
- Unloaded chunks can simply advance by a bounded approximate function of elapsed time; old climate history is not required.

Fidelity improves only when a cheaper representation demonstrably fails under observation.
## Stable anatomical addressing for significant plants

**Default to visual patches, not per-branch biological ledgers.** Most browsing can reduce foliage density, change a small localized mask or swap a pruned variant. Exact eaten-leaf identity, individual nutrient units and durable anatomical addresses are unnecessary.

For a **conspicuous, persistent structural change**—a familiar tree's broken limb, a distinct shrub repeatedly stripped in the player's view—optionally assign stable branch/segment identifiers or a compact procedural damage mask. An organism ID + seed + coarse damage data often suffices; use per-segment addressing only if an explicit close-view test proves necessary. New growth must not resurrect a saved broken landmark limb, but ordinary leaves may be regenerated cheaply.

InteractionsCore prevents an immediate visible interaction from being applied twice, checks approximate physical reach and reduces the relevant local visible resource amount. A complex typed transaction journal and full mass/chemical accounting are not default requirements. No persistent IDs for leaves, blades, fronds or ordinary branches.
## Provisional forest disturbance and lightweight recovery — scope ceiling

**Provisionally accepted because it changes the visible forest, not because the project needs a full forest ecology simulator.** The first implementation should use the existing FloraSim tree identity/branching-seed model, patch state, lazy catch-up and StalthosSim weather events; **do not introduce another runtime simulation domain**.

- **Occasional consequential changes:** storms, branchfall, individual tree death/uprooting and localized canopy openings. Record which established trees are lost/damaged and preserve recognizable standing deadwood, fallen trunks and persistent gaps where relevant. A deterministic seed must **not resurrect** a tree suppressed by a saved death/fall override.
- **Coarse patch response:** affected understory/ground cover may become denser, sparser or compositionally different as shade/exposure changes. Approximate the canopy gap using existing patch/environment summaries, **not** per-leaf lighting, soil or full competition solves.
- **Simple replacement:** when a patch has available space and broadly suitable conditions, permit occasional new saplings/trees to establish with stable identities and deterministic meshes. No explicit seed-by-seed dispersal, individual seedling survival simulation or ranked competition among thousands of saplings.
- **Cheap reconstruction:** use current season, coarse elapsed-time recovery and persisted significant tree/canopy overrides. No mandatory replay or checkpointing of fine-grained ecological history.

**Deferred unless a real in-engine visual/gameplay deficiency justifies them:** comprehensive succession-stage models, detailed plant competition or seed banks, mechanistic wildfire ignition/spread/recovery, full forestry dynamics and terrain erosion. A rare burned/damaged patch may eventually be represented as a coarse disturbance *if justified*, but wildfire propagation is **not** an approved system here. Keep geological terrain, rivercourses and ordinary topography stable.

**Acceptance:** revisiting a familiar woodland years later reveals persistent fallen trees, a changed canopy opening, more cover or occasional young trees, without rebuilding the forest from scratch, resetting damage, maintaining every seedling as an entity or causing activation/save-size spikes. Evaluate whether this modest layer adds enough visual value **before** adding further depth.

## Ordered growth and bounded catch-up

**Do not replay chronological drought/heat/rain histories.** On revisiting an inactive region, advance patches and notable plants via elapsed time, seasonal profile, simple condition modifiers and saved lasting exceptions. If a tree fell in an observed storm, store the resulting fallen/dead state; no tree-by-tree weather-integral replay is needed.

Keep generation and plant-state preparation ahead of a potential camera reveal. Budget geometry builds and preserve version safety for **concurrently edited noticeable plants**, but do not require every patch to maintain a journal cursor and historical reconciliation pipeline. When detail is unready, use a cheaper consistent visual representation that still respects visible damage, rather than showing a restored destroyed tree.
## Food and interaction model

The player or a nearby visible animal may reach actual foliage, nip a shrub and visibly reduce its amount. FloraSim needs simple edible suitability/quality tags, approximate accessible resource amount or patch density, and local reach/interaction anchors. BeastCore receives a plausible feeding result; no exact food chemistry, digestion yield or species-specific energy-conservation transfer is mandated.

Remote animals may exert **coarse pressure** on an entire forage patch or regional cover value, sampled only when needed. Do not generate an unseen log of specific bites or settle exact hidden biomass transactions.
## Death, fungi and detritus

When a prominent tree dies, persist its standing-dead/fallen state and place convincing deadwood/litter visuals. A few timed stages can vary fungi, wood decay and ground cover; optional detritivore activity may be staged from habitat cues. No nutrient/soil recycling conservation, microbial model or remote detritus ledger is required.

## Rendering contract

For requested chunks, return stable botanical snapshots/variant seeds, geometry-growth parameters, damage masks, leaf/frond density, fruit state and interaction anchors. Renderer performs *visual* wind bending, animation and GPU instancing independent of ecological ticking.

## Test cases

A tree growing over multiple seasons returns as the same individual; a browsed shrub loses finite edible biomass; a rain event outside render view changes future growth; a fern colony can update 6 months of history quickly; two animals cannot consume the same leaf biomass twice. A fallen seed-generated tree does not return undamaged after chunk cycling; a localized gap can develop different coarse cover and a few new durable trees over time without simulating individual seedlings or rebuilding all neighboring tree meshes.

Biology definitions live in [Flora](flora.md); architecture in [Simulation architecture](simulation-architecture.md).
