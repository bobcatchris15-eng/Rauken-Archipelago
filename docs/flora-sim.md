# FloraSim — persistent botanical life

**Domain:** Individual and population plant/fungal ecology; **status:** conceptual subsystem plan.

## Authority

FloraSim owns living trees, shrubs, ferns, herbaceous populations, moss-like colonies, fungal systems, botanical growth, fruiting, competition, damage and death. It does **not** own rendered plant instances, atmospheric weather, animal decisions or frame-by-frame updates.

A plant may be ecologically elaborate while rendered with one simple distant mesh. A thousand dense grass blades may be one population-patch record.

## Representation

**Individuals:** prominent/long-lived trees, significant shrubs, large ferns/cycads and plants with distinctive browsing scars. Stable organism ID, species, seed, location, age, size, resources, health, growth/reproduction state, structural branch IDs/damage and last-evaluated time.

**Population/colony patches:** grasses, reeds, horsetails, small herbs, mosses and fungi where organism-level tracking would be wasteful. Stable patch ID, species mix, coverage, density, age/size distribution, available edible biomass, health, cohort change and last-evaluated time.

All organisms/patches use environmental baseline fields from world generation and time-window summaries from StalthosSim. Their persistent records and relevant event cursors live in StalthosState.

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

A tree growing over multiple seasons returns as the same individual; a browsed shrub loses finite edible biomass; a rain event outside render view changes future growth; a fern colony can update 6 months of history quickly; two animals cannot consume the same leaf biomass twice.

Biology definitions live in [Flora](flora.md); architecture in [Simulation architecture](simulation-architecture.md).
