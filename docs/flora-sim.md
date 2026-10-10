# FloraSim — persistent botanical life

**Domain:** Individual and population plant/fungal ecology; **status:** conceptual subsystem plan.

## Authority

FloraSim owns living trees, shrubs, ferns, herbaceous populations, moss-like colonies, fungal systems, botanical growth, fruiting, competition, damage and death. It does **not** own rendered plant instances, atmospheric weather, animal decisions or frame-by-frame updates.

A plant may be ecologically elaborate while rendered with one simple distant mesh. A thousand dense grass blades may be one population-patch record.

## Representation

**Individuals:** prominent/long-lived trees, significant shrubs, large ferns/cycads and plants with distinctive browsing scars. Stable organism ID, species, seed, location, age, size, resources, health, growth/reproduction state, structural branch IDs/damage and last-evaluated time.

**Population/colony patches:** grasses, reeds, horsetails, small herbs, mosses and fungi where organism-level tracking would be wasteful. Stable patch ID, species mix, coverage, density, age/size distribution, available edible biomass, health, cohort change and last-evaluated time.

All organisms/patches use environmental baseline fields from world generation and time-window summaries from RaukenSim. Their persistent records and relevant event cursors live in RaukenState.

## Lazy advancement

- On a bulk spatial snapshot request, retrieve elapsed world-time and accumulated climate/disturbance history.
- Advance growth, reproduction, leaf turnover, resources and mortality by appropriate analytic/coarse-step rules, with relevant discrete events applied in timestamp order.
- Do not tick every plant every frame or re-query every plant on render updates.
- On browsing/branchfall/burning/flooding, update the affected organisms promptly via validated InteractionsCore event/transaction.
- A visibly changing plant sends specific state deltas to the renderer; ordinary tiny biomass changes may accumulate until they matter visually.
- Unloading/changing LOD discards graphics only, not botanical state.

Plants must not re-randomize shape during a chunk reload: stable seeds and saved structural changes preserve identity. In particular, a tree with a broken branch keeps the missing branch as it grows around that loss.

## Food and interaction model

Each edible part has anatomical location/reach, current biomass, water, fiber/chemical defenses and nutritional properties. BeastCore provides consumer physiology via HeroSim/FaunaSim, FloraSim validates resource quantity, InteractionsCore commits transfer once and returns true intake to animal owners. Feeding removes visible tissue where appropriate.

Animal populations offscreen may have bulk browsing budgets applied to cohorts and selected persistent individuals. Their ecological use persists through lazy advancement.

## Death, fungi and detritus

When a tree dies, FloraSim ends the living plant record and emits a structural/detrital transition. RaukenState persists deadwood or other remains. FloraSim may continue modeling fungal colonization, wood decay and nutrient/soil organic effects at coarse interval; FaunaSim detritivores/scavengers consume shared resources via InteractionsCore. Avoid per-microbe simulation or double-counting live and dead biomass.

## Rendering contract

For requested chunks, return stable botanical snapshots/variant seeds, geometry-growth parameters, damage masks, leaf/frond density, fruit state and interaction anchors. Renderer performs *visual* wind bending, animation and GPU instancing independent of ecological ticking.

## Test cases

A tree growing over multiple seasons returns as the same individual; a browsed shrub loses finite edible biomass; a rain event outside render view changes future growth; a fern colony can update 6 months of history quickly; two animals cannot consume the same leaf biomass twice.

Biology definitions live in [Flora](flora.md); architecture in [Simulation architecture](simulation-architecture.md).
