# The Stalthosian Archipelago - Project Task List

This task list serves as a high-level roadmap for implementing the project based on the planning documents and specifications provided in the `docs/` folder.

## 1. Engine & Technical Foundation
- [ ] **Engine Selection & Evaluation**: Set up an evaluation environment for the leading engine candidates: **Flax Engine** and **Wicked Engine**. Produce rendering and benchmark experiments.
- [ ] **Asset Pipeline Validation**: Build the six reference plants from `docs/flora.md` and the sauropod anatomical proxy from `docs/creatures.md`. Run generation, bake, import, turntables, LOD, and benchmark. Ensure tools run unattended from a Windows PowerShell entrypoint.
- [ ] **Core Simulation Architecture setup**: Define and skeletonize the named system modules:
  - `SimCore` (shared time/scheduling)
  - `StalthosState` (persistence layer for explicit exceptions/events)
  - `StalthosSim` (environmental/weather state)
  - `FloraSim` (plant/fungi state)
  - `FaunaSim` (wildlife population/instantiation)
  - `HeroSim` (player state/intents)
  - `BeastCore` (shared animal biology/locomotion rules)
  - `InteractionsCore` (cross-domain exchanges)
  - `HeroView` (camera and embodiment controls)
- [ ] **Spatial Activation System**: Implement a chunk/region activation system governed by `SimCore`. Ensure it manages 3 presentation levels: Observed/contacting (full simulation), Nearby but hidden (pre-warmed), and Remote/forgotten (regional profiles only).

## 2. World Generation & Environment (StalthosSim)
- [ ] **Terrain Generation Pipeline**: Create offline world-generation outputs for the four major islands (Main Island, Rainridge, Stone Island, Outer Reach) considering height, slope/aspect, bedrock/substrate, soil type/drainage, and drainage network. Apply geographic compression.
- [ ] **Environmental State System (`StalthosSim`)**: Implement coarse weather states (sunny, raining, etc.), wind, approximate temperature, and dampness. Do NOT simulate atmospheric fluid dynamics or detailed hydrology.
- [ ] **Water & Flooding**: Implement simple seasonal level adjustments and predefined floodable areas.

## 3. Flora & Vegetation (FloraSim)
- [ ] **Vegetation Generation & Placement**: Create botanical form generators based on true structural families (branch-bearing trees, ferns, horsetails, etc.).
- [ ] **Flora Representation**: Use procedural seeds and current season to produce most flora. Implement patch-level cover for grasses and small herbs.
- [ ] **Interaction & Disturbance**: Implement visible browse removal with lazy recovery. Implement lightweight local deformation/bending for vegetation contact.
- [ ] **Flora Persistence (`StalthosState`)**: Implement compact exception saving for prominent long-lived trees or conspicuous events (e.g., fallen trees, stripped shrubs) so observed changes remain believable.

## 4. Fauna & Wildlife (FaunaSim & BeastCore)
- [ ] **BeastCore Shared Biology**: Implement camera-independent motor competence (foot placement, balance) and shared behavior families (resting, foraging, reacting to danger).
- [ ] **Wildlife Instantiation & Persistence**: Implement regional catch-up where local animals are prepared *before* they are camera-visible. Implement retention of compact individual records *only* for bonded companions, dependent young, or notable encounters.
- [ ] **Food Web Infrastructure**: Implement simple food-web relationships (what an actor eats/is eaten by) as presentation guidance, not a quantitative ecosystem model.

## 5. Hero Beasts (Playable Characters)
- [ ] **HeroSim Foundation**: Implement player condition tracking (food/water/comfort/fatigue/injury) using `BeastCore` rules.
- [ ] **Smalltrotter (Dwarf Titanosaur)**: Implement juvenile vs. mature models (pebbled scales, bristles vs. thick joints, osteoderms). Define unique foraging animations.
- [ ] **Brackenback (Ankylosaurid)**: Implement low, tough foraging. Implement generalized protection behavior (reacting to distressed small animals).
- [ ] **Thistletail (Paravian)**: Implement active, birdlike movement, opportunistic snap-feeding on insects/small resources, and brief intensive parenting.
- [ ] **Longstride (Medium Theropod)**: Implement stalking/pursuit mechanics, episodic hunting, and extended offspring dependency/following behaviors.
- [ ] **Reedcrest (Basal Hadrosauroid)**: Implement variable foraging stances and the persistent peer-bond "Kindergarten" system where 2-4 companions follow and associate.
- [ ] **Reproduction / Life Cycle**: Implement the accelerated playable life events: courtship, nesting, incubation, and hatching (targeting a ~30 min focused episode).

## 6. Player Control & Camera (HeroView)
- [ ] **Direct Steering**: Implement body-relative WASD movement. Implement the "central-third-wide screen-space corridor" path constraint for player intents.
- [ ] **Autonomy System**: Implement `HeroSim` fallback to full autonomy (travel, feed, rest, socialize) when no commands are given.
- [ ] **Contextual Slow-Time Menu**: Implement a contextual intention menu invoked manually by the player.
- [ ] **Camera Systems (`HeroView`)**:
  - Animal-centered third-person orbit/follow camera.
  - Passive documentary camera (activates during inactivity).
  - Locally detached observation camera with a strict spatial tether.
  - Alarm-driven shared attention (camera orienting towards sensed threats).
- [ ] **Independent Audio Listener**: Tie the primary spatial audio listener to the active player camera, keeping player ears independent from `HeroSim`'s biological senses.
