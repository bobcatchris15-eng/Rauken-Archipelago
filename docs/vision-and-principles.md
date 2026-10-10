# Vision and principles

**Status:** Working creative direction. **Project:** The Stalthosian Archipelago.

## Experience

Play a dinosaur living its ordinary life on a fictional Late Cretaceous-inspired archipelago. Hatch as an ordinary member of a chosen species in its existing wild population, experience species-specific childhood, survive, grow, explore, potentially breed and tend young, and eventually die. Another life can hatch in the same persistent world. The player is not a human adventurer wearing a dinosaur skin. The world doesn't issue quests, level-gate islands, or arrange drama in response to the player's camera.

**The player is the animal's intention, not its nervous system.** Direct steering and chosen responses are the strongest voluntary intervention; compatible ingestion, posture, perception and social reactions continue automatically even while moving. Uncommanded animals pursue ordinary life under HeroSim control. When camera input also stops, HeroView may gently frame them as a continuous nature documentary.

A creature can spend its whole life in one valley. Curious players may travel much farther—even across dangerous seas—but the environment owes them neither rewards nor survival.

## Design pillars

1. **Lived landscape.** Sheltered mossy ravines, drowned valleys, mineral outcrops, resilient forests, floodplains and real landmarks. Recognizable places matter more than raw area.
2. **Environmental survival.** Heat, dehydration, hazardous ground, weather, flood pulses, food quality and illness should be more common problems than active predator pursuit.
3. **Believable organisms.** Plants and animals have ecology, physical structures, growth and relationships. Eating changes plants; weather changes habitat; growth changes mobility and risk.
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
- Rigorous life simulation vs. readable, non-nagging feedback.
- Fluid juvenile development vs. coherent world time and the development of neighboring wildlife.
- Continuous ecology vs. tractable CPU/memory budgets.

**Success:** a player can find a home, recognize individual landmarks and plants, become absorbed in ordinary life, and remain curious about the next ridge. Every Hero Beast should be satisfying to simply watch living for an extended period without player commands.

**Named architecture:** SimCore coordinates time; **StalthosState** stores persistent identity/history; **StalthosSim** governs environment; **FloraSim** plants; **FaunaSim** wildlife; **HeroSim** the player; **BeastCore** shared animal rules; **InteractionsCore** ecological exchanges. See [Simulation architecture](simulation-architecture.md).
