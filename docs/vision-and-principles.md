# Vision and principles

**Status:** Working creative direction. **Project:** The Stalthosian Archipelago.

## Experience

Play a dinosaur living its ordinary life on a fictional Late Cretaceous-inspired archipelago. Hatch as an ordinary member of a chosen species in its existing wild population, experience species-specific childhood, survive, grow, explore, potentially breed and tend young, and eventually die. Another life can hatch in the same persistent world. The player is not a human adventurer wearing a dinosaur skin. The world doesn't issue quests, level-gate islands, or arrange drama in response to the player's camera.

**The player is the animal's intention, not its nervous system.** Direct steering and chosen responses are the strongest voluntary intervention; compatible ingestion, posture, perception and social reactions continue automatically even while moving. Uncommanded animals pursue ordinary life under HeroSim control. When camera input also stops, HeroView may gently frame them as a continuous nature documentary.

A creature can spend its whole life in one valley. Curious players may travel much farther—even across dangerous seas—but the environment owes them neither rewards nor survival.

## Fidelity mandate — theatrical ecology

**Build a beautiful Potemkin village of the Cretaceous.** The experience should *look and behave* like an intricate living world without requiring intricate internal machinery. The visual result, animal animation/interaction and immediate sensory credibility have the highest fidelity priority. Observable local effects and recognizable revisits must remain coherent. Unseen ecological processes are deliberately shallow, statistical, deterministic-where-useful or staged.

**Spend simulation budget only when the player can observe its benefit.** Prefer a simple seasonal moisture factor to weather-history replay; a population density and occasional movement to an exact demographic ecology; a lightweight animal condition model to rigorous metabolic accounting; and a visually changed shrub patch to per-leaf nutrient conservation. Preserve special persistent relationships and conspicuous damaged landmarks, but do not extend those exceptions to every organism.

The world should not visibly contradict itself: creatures must not pop into existence when a camera turns, dead companions cannot reappear, browsed bushes should visibly respond, and familiar fallen trees must stay fallen. Those are **presentation/continuity requirements**, not proof that the invisible ecological model must be physically complete.

If a complex mechanism adds no measurable visual, behavioral or gameplay improvement against a cheap approximation, **do not build it**. Scientific and ecological research is guidance for appearance and plausible behavior, not a requirement for numerical biological fidelity.

## Runtime cost doctrine — every frame is for the facade

**Performance is an aesthetic enabling constraint.** Minimize per-frame CPU/GPU work that does not directly improve the image, sound, interaction or responsiveness the player currently experiences. In particular, no per-object ecology polling, full-scene collision sweeps, hidden-individual behavior trees, world-wide animation, climate integration or routine save/database traffic on the render path. Ordinary background state advances on events, coarse timers, camera-region preparation or elapsed-time reconstruction.

Reserve immediate work for the Hero Beast, responsive nearby physical contacts, current camera/audio presentation and visible local wildlife. Stage animals beyond the possible camera reveal before they're seen, but do **not** run them all at full behavior/animation/physics fidelity. Distant regions use static graphics, approximate abundance and saved conspicuous exceptions.

Spend *offline* computation freely where it improves reusable asset quality: mesh/material generation, baking, LOD/impostor creation, terrain composition, reference-driven variation and diagnostics. On the GPU, measure and optimize the actual visual costs—foliage overdraw, shadows, lighting, draw submission, skinning, streaming—rather than compromising near-view appearance by assumption. Prefer batching, instancing, cache reuse, cheap distant substitutes and update-on-change. Never equate "no per-frame simulation" with "no rendered motion": visually essential animation still runs, using its most economical representation.

The GTX 1080 / first-gen Ryzen 1080p, 30 FPS floor remains a **measured full-scene objective**. Each proposed recurring workload must justify its observed benefit and be profiled alongside dense botanical scenery, weather, hero locomotion and nearby wildlife. Do not buy hidden ecological fidelity with frame time.

## Biodiversity is an authored spectacle, not an ecology budget

Prefer **fifty convincingly different non-hero wildlife actors** over sixteen deeply and quantitatively simulated animal species. Prefer **around two hundred recognizably different plant silhouettes, branching systems and leaf/frond designs** over a handful of highly detailed botanical simulators. These are **expandable creative starting ambitions, not caps, mandatory completion gates or a reason to reject an animal or plant the user specifically wants**.

The fauna's distinguishing value is its appearance, characteristic behavior, voices and credible natural placement; the flora's is shape, variety, layering, surface detail and rootedness in a believable habitat. The food web supplies an **approximate, stage-setting explanation for encounters** and a few observable local consequences, not an equilibrium model whose mathematical requirements restrict the cast. Reuse body-plan animation families and habitat/season display templates rather than writing a deep individual simulation for every actor.

A forest can display dozens of botanical forms whose hidden 'biology' uses a few common growth/condition/cover rules. An animal can be compelling while basking or foraging without having a simulated lifelong biography. **Never trade away the convincing appearance of abundance merely to make the invisible ecology more rigorous.** See [Fauna actor catalog](fauna-actor-catalog.md) and [Plant visual catalog](plant-visual-catalog.md).

## Confirmed display-and-continuity decisions — 2026-10-10

**Vegetation contact is a visual priority.** Shrubs, tall ferns and small branches should visibly bend/part when an animal presses through, rather than simply clipping through its body. Start by targeting that effect using lightweight local deformation, simple collision proxies or shader-driven bending—not per-leaf rigid-body physics. If full-scene benchmarks later show it too expensive, it may be scaled back with explicit visual/performance evidence. Do not preemptively eliminate it.

**Animal interaction is part of its performance.** Brackenback protecting a distressed smaller animal, posturing, inspecting a threat, displaying at another creature or responding to the player should look coherent and convincing. That does not create a requirement for private psychology, emergent social simulation, lifelong experience or deep plans. Animate and stage believable observable responses using shared behavior families and brief perceptual state.

**Geography is composed, not historically solved.** Offline landscape generators can use drainage/geology as reference but are primarily tools for credible, beautiful and dramatic locations. No numerical reenactment of geological eras is required.

**Memory of scenery is local and selective.** Going over a nearby hill and returning should reveal the same tree positions and local actors, not a freshly shuffled scene. Recently instantiated regions need a grace/continuity window. After a long dormant interval, unimportant scenery may be procedurally regenerated or rearranged, while prominent landmarks, saved damage and important individuals remain consistent. Test continuity by a player's likely revisits, not a requirement for permanent identity of every tree.

**Reference images:** the desired overall photographic/artistically realistic look is not locked until the user selects suitable visual references.

## Design pillars

1. **Lived landscape.** Sheltered mossy ravines, drowned valleys, mineral outcrops, resilient forests, floodplains and real landmarks. Recognizable places matter more than raw area.
2. **Environmental survival.** Heat, dehydration, hazardous ground, weather, flood pulses, food quality and illness should be more common problems than active predator pursuit.
3. **Believable organisms on screen.** Plants and animals have convincing structure, movement, growth and relationships. Eating visibly changes nearby plants; weather looks and feels consequential; growth changes movement and reach. Hidden ecology may be approximate.
4. **Biological credibility with fictional freedom.** Derive anatomy/ecology from Late Cretaceous groups and extant comparators without pretending invention is fossil evidence.
5. **Density over cartographic purity.** Compress distance and emphasize unusual landforms while retaining coherent geology, drainage and ecological causes.
6. **No player magnet.** Avoid guaranteed encounters, scripted fauna spawning, predator omniscience and escalating threats tied to player progress.
7. **Coherence over brute visual cost.** Convincing contact, scale, light, wind, movement and vegetation structure outweigh maximal polygons or novelty effects.

## Scope and boundaries

- World: **The Stalthosian Archipelago**, four major irregular islands (Main Island, Rainridge, Stone Island, Outer Reach) plus numerous smaller fragments. Each major island has two or three notable landscape assemblages and many local habitats.
- **Five planned playable lineages:** Smalltrotter, dwarf titanosaur visual flagship; Brackenback, true ankylosaurid with generalized protection of small distressed animals; Thistletail, flightless feathered omnivore; Longstride, mobile medium predator and long-term parent; Reedcrest, basal hadrosauroid with a persistent bonded peer group.
- Reproduction is a playable life event: courtship, nesting, incubation and hatching accelerated through the shared world timeline, targeting a focused episode of about thirty minutes or less. Species-specific offspring care may continue through ordinary play much longer.
- No genetic optimization, breeding-stat progression, mandatory reproduction or inheritance-based player advantage.
- Visual goal: **near-photorealistic outdoor nature** that runs at a **30 FPS floor**, preferably higher, on **GeForce GTX 1080 8 GB and first-generation Ryzen**.
- Runtime engine: **Flax or Wicked Engine are leading preferences**. Do not lock either before controlled trials.
- Platform: Windows-first desktop. Resolution baseline for comparisons: 1920×1080 until actual display information changes it.
- Asset production: automated and agent-friendly; use reference research, Blender/procedural systems, offline mesh/material baking, measurable exports and visual checks.

## Intentional non-goals

No combat/progression treadmill, crafting survival UI, survival bars that drain unrealistically fast, compulsory island tourism, evenly spaced points of interest, permanent player-centered danger bubble, or total-environment fluid/structural simulation.

No expectation of exact Paleogene/Maastrichtian reconstruction: this is an invented archipelago and invented descendant lineages. Cite research when claiming something was actually known.

## Tensions to evaluate in-engine

- Geographical density vs. meaningful ordinary stretches and plausible watersheds.
- Understory richness vs. fill rate, shadows and visible repetition.
- Small animal-scale detail vs. overall world size and streaming.
- Full animal autonomy and documentary observation vs. the immediate priority of direct player steering.
- Lightweight biological approximations vs. convincing observable consequences and readable, non-nagging feedback.
- Fluid juvenile development vs. coherent world time and the development of neighboring wildlife.
- Continuous ecology vs. tractable CPU/memory budgets.

**Success:** a player can find a home, recognize individual landmarks and plants, become absorbed in ordinary life, and remain curious about the next ridge. Every Hero Beast should be satisfying to simply watch living for an extended period without player commands.

**Named architecture:** SimCore coordinates time; **StalthosState** stores persistent identity/history; **StalthosSim** governs environment; **FloraSim** plants; **FaunaSim** wildlife; **HeroSim** the player; **BeastCore** shared animal rules; **InteractionsCore** ecological exchanges. See [Simulation architecture](simulation-architecture.md).
