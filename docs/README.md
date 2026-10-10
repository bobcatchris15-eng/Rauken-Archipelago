# Planning index

These are **planning documents**, not implementation code. They are separated by responsibility so a creature designer can change a species without silently changing engine decisions, and a rendering engineer can replace the renderer without rewriting biology.

| Domain | Document | Owns |
|---|---|---|
| Product direction | [Vision and principles](vision-and-principles.md) | Goals, tone, acceptance philosophy |
| Gameplay | [Gameplay](gameplay.md) | Player agency, physiology interface, life cycle and experience |
| Geography | [Geography](geography.md) | The Stalthosian Archipelago's four islands, coastlines, terrain characters and scales |
| World generation | [World generation](world-generation.md) | Authoring/generation method, metrics and test landforms |
| Architecture | [Simulation architecture](simulation-architecture.md) | Named systems, ownership, time, interactions and persistence |
| Environment simulation | [StalthosSim](stalthos-sim.md) | Weather, seasonal conditions, floods, environmental history |
| Plant simulation | [FloraSim](flora-sim.md) | Persistent trees, shrubs, herbs, fungi; lazy growth and browsing |
| Animal simulation | [FaunaSim](fauna-sim.md) | Regional cohorts, transient locally instantiated animals, bounded retention of previously instantiated, relevant individuals |
| Player animal | [HeroSim and BeastCore](hero-sim.md) | Bodily condition, perception and player-intent execution |
| Player interface | [HeroView](hero-view.md) | Body-relative WASD, contextual intentions adopted by HeroSim, bounded detached/documentary camera, independent camera-centered audio, alarm recall |
| Spatial lifecycle | [Spatial activation](spatial-activation.md) | Simulation regions buffered beyond perception and camera visibility |
| Ecology | [Ecology and hydrology](ecology-and-hydrology.md) | Cross-domain habitats and ecological processes |
| Flora | [Flora](flora.md) | Plant/fungal organisms, anatomical families, foods and plant life histories |
| Creatures | [Creatures](creatures.md) | Five playable lineages, growth, sociality, reproduction and ecological niches |
| Visual design | [Visual direction](visual-direction.md) | Appearance and motion quality contract, independent of renderer |
| Engineering research | [Rendering experiments](rendering-experiments.md) | Engine comparison, hardware targets, instrumentation and gates |
| Production tooling | [Asset toolkit](asset-toolkit.md) | Agent-accessible source-art and asset production pipeline |
| Evidence and decisions | [Research register](research-register.md) | Research leads, hypotheses, open questions and decision process |

## Project-wide simulation depth rule

**Display fidelity beats internal fidelity.** The archipelago is a visually ambitious natural-history illusion with shallow, inexpensive ecological internals. Use the simplest plausible proxy/heuristic that produces convincing observable behavior; preserve only the conspicuous consequences and continuity that a player can actually notice. No exact population energy ledger, hydrological reconstruction, weather chronology, full nutrient cycle or complex individual physiology is required by default. Existing detailed algorithms in domain documents are proposals **subordinate to this rule**.

Retain real spatial collision, correct camera/player agency, responsive animal interactions, recognizable landmarks, surviving social bonds and conspicuous persistent changes. These are the places where a hollow simulation must *not look hollow*.

## Current status

- **Established direction:** fictional Late Cretaceous-inspired archipelago; four main islands; dense, causally convincing landforms; continuous animal life rather than quest-led survival; environmental threats more common than predatory attacks; near-photorealistic rendering at 30 FPS minimum on the reference machine.
- **Named architecture (decided):** **StalthosState**, **BeastCore**, **InteractionsCore**, alongside SimCore, StalthosSim, FloraSim, FaunaSim, HeroSim and **HeroView**. Logical in-process modules, not mandatory separate services.
- **Decided life design:** five Hero Beasts; hatching within existing populations; autonomous animal life while uncommanded; optional player-invoked slow-time intentions; species-specific parenting and compressed nesting; documentary camera; persistent world across player deaths.
- **Provisional:** exact island dimensions, separation dates, species anatomy, metabolic values, time-compression tuning, storm/flood intensity, reconciliation budgets, demographic precision, engine selection and vendor dependencies. Detailed groundwater transport and continuous erosion are explicitly out of runtime scope.
- **Research required:** age-dependent sauropod integument (the quills are consciously speculative); Cretaceous botanical reconstruction; physiological parameter ranges; low-end-hardware renderer benchmarks.

## Rules for future agents

1. Treat this index as the entrance; read [Vision](vision-and-principles.md) before modifying any domain.
2. Keep **what exists** (world/species/ecology) separate from **how it looks** (visual) and **how it is implemented** (rendering/toolkit).
3. Use [Simulation architecture](simulation-architecture.md) for canonical component names and authority; don't invent player-only biological rules. Choose approximate shared rules unless more depth demonstrably improves observed behavior.
4. Prepare visually relevant local fauna beyond HeroView's reachable tether and HeroSim's perception; never instantiate animals *because* they entered the frustum. Regional catch-up must be cheap and bounded, using current-state snapshots and occasional consequential events, not mandatory replay of environmental history.
5. FaunaSim retains compact individual records only after actual instantiation, for bonded companions, dependent young, some notable giants or other bounded reasons. Dormant individuals can advance, return or eventually decay to cohorts without creating duplicate animals.
6. HeroView can **see and hear** things the Hero Beast cannot perceive. Direct W is body-forward independent of camera orientation; camera detachment does not suspend autonomy; player-suggested goals become high-priority HeroSim intentions **without passing camera-only sensory knowledge**.
7. Preserve concrete user preferences even when scientifically improbable; favor evocative geography where coherent causal relationships can still be maintained.
8. Do not harden estimates into requirements without testing or an explicit design decision. Mark assumptions as *Proposed*, *To test*, *Unknown*, or *Decided*. In ecological domains, complex simulation requires evidence that cheap presentation-level approximation fails.
9. Make work reproducible. Research claims require real citations in future completed specifications; don't invent taxonomic evidence.
10. No gameplay implementation or vertical slice is currently requested by these documents. The renderer and asset toolkit documents describe **experiments** only.

## Proposed document maintenance

Each domain owner records changes, unresolved tensions, experiment outcomes, and cross-domain implications. Revisions to another domain's *contract* require a note in the research register. Specifications should remain readable independently, but this index is the source of truth for boundaries.
