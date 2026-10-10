# FloraSim — persistent botanical life

**Domain:** Individual and population plant/fungal ecology; **status:** conceptual subsystem plan.

## Authority

FloraSim owns living trees, shrubs, ferns, herbaceous populations, moss-like colonies, fungal systems, botanical growth, lightweight establishment/suitability, damage and death. It does **not** own rendered plant instances, atmospheric weather, animal decisions or frame-by-frame updates.

A plant may be ecologically elaborate while rendered with one simple distant mesh. A thousand dense grass blades may be one population-patch record.

## Representation

**Individuals:** prominent/long-lived trees, significant shrubs, large ferns/cycads and plants with distinctive browsing scars. Each substantial tree has a stable *logical identity* (region/placement ID or durable ID), species, location, deterministic branching seed, establishment/growth information and any meaningful structural overrides. **Identity does not imply a separate heavyweight persisted row or per-tree update loop:** unchanged baseline trees can be reconstructed from world/region seeds; only meaningful mutable differences need compact records. New trees established later receive durable identities.

**Population/colony patches:** grasses, reeds, horsetails, small herbs, mosses and fungi where organism-level tracking would be wasteful. Stable patch ID, species mix, coverage, density, age/size distribution, available edible biomass, health, cohort change and last-evaluated time.

All organisms/patches use environmental baseline fields from world generation and time-window summaries from StalthosSim. **Where state differs from its deterministic baseline**, compact records and relevant event/checkpoint information live in StalthosState. Do not store generated meshes or an endless replay log for every tree.

## Biological region activation ahead of rendering

When **SimCore** activates a simulation chunk around Smalltrotter (including buffer beyond HeroView's bounded detached camera), FloraSim resolves the locally appropriate full botanical community from habitat distributions, stable seeds, StalthosState records and elapsed environmental history.

This means all visually required plant instances/colonies have a biologically coherent source **before** the renderer requests the camera-visible chunk; it does **not** require independent ticking of every rendered stem. Trees and other durable specimens preserve identities/damage; low cover can be dense geometry derived from one ecological population patch.

The renderer may ask for batches of the already-derived state without making individual plants poll the climate or grow merely because the frustum touched them. See [Spatial activation](spatial-activation.md).

## Lazy advancement

- On a bulk spatial snapshot request, retrieve elapsed world-time and accumulated climate/disturbance history.
- Advance growth, reproduction, leaf turnover, resources and mortality by appropriate analytic/coarse-step rules, with relevant discrete events applied in timestamp order.
- Do not tick every plant every frame or re-query every plant on render updates.
- On browsing/branchfall/burning/flooding, update the affected organisms promptly via validated InteractionsCore event/transaction.
- A visibly changing plant sends specific state deltas to the renderer; ordinary tiny biomass changes may accumulate until they matter visually.
- Unloading/changing LOD discards graphics only, not botanical state.

Plants must not re-randomize shape during a chunk reload: stable seeds and saved structural changes preserve identity. In particular, a tree with a broken branch keeps the missing branch as it grows around that loss.

## Stable anatomical addressing for significant plants

**Persistent organism ID is not enough** when a particular branch is bitten or broken. For durable trees, conspicuous shrubs and other structurally important plants, use **stable anatomical addresses**: organism ID + immutable segment/branch ID + tissue/resource category. Branch IDs must be generated deterministically or assigned durably; never use mutable array positions, which shift as growth adds branches.

FloraSim owns the structural graph/compact generative parameterization and amounts of accessible tissue. StalthosState persists stable seed, last-evaluated time, current structure, scars/pruning/tombstones and material state as needed. The **asset generator** reconstructs the same physical segment at the same location/pose from that biological record.

An interaction is a typed, idempotent command (target/address, tissue type, requested quantity, actor and operation ID). InteractionsCore validates location/reach and available tissue with the appropriate owners, commits the **actual granted** biomass/injury exactly once and returns the outcome to animal digestion/behavior. FloraSim retains the **resulting structural state** and segment/resource version, not an ever-growing diary of bites; future regrowth may replace foliage but must not mysteriously restore a severed limb.

Do **not** give every leaf, fern frond or grass blade a persistent ID. Dense cover may use patch IDs, coarse browsing masks and aggregate resource budgets. Tree topology resolution is species/visual-significance dependent, not universally maximal.

## Provisional forest disturbance and lightweight recovery — scope ceiling

**Provisionally accepted because it changes the visible forest, not because the project needs a full forest ecology simulator.** The first implementation should use the existing FloraSim tree identity/branching-seed model, patch state, lazy catch-up and StalthosSim weather events; **do not introduce another runtime simulation domain**.

- **Occasional consequential changes:** storms, branchfall, individual tree death/uprooting and localized canopy openings. Record which established trees are lost/damaged and preserve recognizable standing deadwood, fallen trunks and persistent gaps where relevant. A deterministic seed must **not resurrect** a tree suppressed by a saved death/fall override.
- **Coarse patch response:** affected understory/ground cover may become denser, sparser or compositionally different as shade/exposure changes. Approximate the canopy gap using existing patch/environment summaries, **not** per-leaf lighting, soil or full competition solves.
- **Simple replacement:** when a patch has available space and broadly suitable conditions, permit occasional new saplings/trees to establish with stable identities and deterministic meshes. No explicit seed-by-seed dispersal, individual seedling survival simulation or ranked competition among thousands of saplings.
- **Lazy/checkpointed history:** update patches and important trees when needed; periodically persist resulting canopy/cover state plus exceptional individual overrides so old disturbances need not be replayed from the beginning of the world. Keep regeneration and reappearance physically credible on return, but avoid detailed ecological chronologies.

**Deferred unless a real in-engine visual/gameplay deficiency justifies them:** comprehensive succession-stage models, detailed plant competition or seed banks, mechanistic wildfire ignition/spread/recovery, full forestry dynamics and terrain erosion. A rare burned/damaged patch may eventually be represented as a coarse disturbance *if justified*, but wildfire propagation is **not** an approved system here. Keep geological terrain, rivercourses and ordinary topography stable.

**Acceptance:** revisiting a familiar woodland years later reveals persistent fallen trees, a changed canopy opening, more cover or occasional young trees, without rebuilding the forest from scratch, resetting damage, maintaining every seedling as an entity or causing activation/save-size spikes. Evaluate whether this modest layer adds enough visual value **before** adding further depth.

## Ordered growth and bounded catch-up

FloraSim consumes StalthosSim's **chronologically ordered regional intervals** and exceptional events, integrating drought/flood/heat effects in sequence rather than using seasonal means alone. Each individual or patch maintains a last-evaluated timestamp and state version to support deterministic resumable advancement.

For an old inactive chunk, calculate inexpensive patch-level summaries first, then advance significant plant individuals in **budgeted batches** ahead of camera observation. No renderer movement may force unbounded synchronous replay. Catch-up jobs can be subdivided with a cursor; late results are discarded or reconciled if the plant version advanced due to a newer bite or storm. High-detail geometry only builds after the state it represents is valid at the requested time.

A lower-detail presentation is acceptable if detail isn't ready; a **factually contradictory** stale representation is not. Preserve committed visible damage/depletion via structural deltas or temporarily omit unreconciled high-detail detail rather than resurrecting destroyed vegetation. Test the visual result under rapid ridge-overlook camera movement and years of deferred growth.

## Food and interaction model

Each edible part has anatomical location/reach, current biomass, water, fiber/chemical defenses and nutritional properties. BeastCore provides consumer physiology via HeroSim/FaunaSim, FloraSim validates resource quantity, InteractionsCore commits transfer once and returns true intake to animal owners. Feeding removes visible tissue where appropriate.

Animal populations offscreen may have bulk browsing budgets applied to cohorts and selected persistent individuals. Their ecological use persists through lazy advancement.

## Death, fungi and detritus

When a tree dies, FloraSim ends the living plant record and emits a structural/detrital transition. StalthosState persists deadwood or other remains. FloraSim may continue modeling fungal colonization, wood decay and nutrient/soil organic effects at coarse interval; FaunaSim detritivores/scavengers consume shared resources via InteractionsCore. Avoid per-microbe simulation or double-counting live and dead biomass.

## Rendering contract

For requested chunks, return stable botanical snapshots/variant seeds, geometry-growth parameters, damage masks, leaf/frond density, fruit state and interaction anchors. Renderer performs *visual* wind bending, animation and GPU instancing independent of ecological ticking.

## Test cases

A tree growing over multiple seasons returns as the same individual; a browsed shrub loses finite edible biomass; a rain event outside render view changes future growth; a fern colony can update 6 months of history quickly; two animals cannot consume the same leaf biomass twice. A fallen seed-generated tree does not return undamaged after chunk cycling; a localized gap can develop different coarse cover and a few new durable trees over time without simulating individual seedlings or rebuilding all neighboring tree meshes.

Biology definitions live in [Flora](flora.md); architecture in [Simulation architecture](simulation-architecture.md).
