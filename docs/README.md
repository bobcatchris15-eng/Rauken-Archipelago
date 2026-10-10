# Planning index

These are **planning documents**, not implementation code. They are separated by responsibility so a creature designer can change a species without silently changing engine decisions, and a rendering engineer can replace the renderer without rewriting biology.

| Domain | Document | Owns |
|---|---|---|
| Product direction | [Vision and principles](vision-and-principles.md) | Goals, tone, acceptance philosophy |
| Gameplay | [Gameplay](gameplay.md) | Player agency, physiology interface, life cycle and experience |
| Geography | [Geography](geography.md) | The Rauken's four islands, coastlines, terrain characters and scales |
| World generation | [World generation](world-generation.md) | Authoring/generation method, metrics and test landforms |
| Architecture | [Simulation architecture](simulation-architecture.md) | Named systems, ownership, time, interactions and persistence |
| Environment simulation | [RaukenSim](rauken-sim.md) | Weather, seasonal conditions, floods, environmental history |
| Plant simulation | [FloraSim](flora-sim.md) | Persistent trees, shrubs, herbs, fungi; lazy growth and browsing |
| Animal simulation | [FaunaSim](fauna-sim.md) | Wild animals, multirate physiology, offscreen populations |
| Player animal | [HeroSim and BeastCore](hero-sim.md) | Intent and shared animal biology at high fidelity |
| Ecology | [Ecology and hydrology](ecology-and-hydrology.md) | Cross-domain habitats and ecological processes |
| Flora | [Flora](flora.md) | Plant/fungal organisms, anatomical families, foods and plant life histories |
| Creatures | [Creatures](creatures.md) | Animal anatomy, growth, behavior and ecological niches |
| Visual design | [Visual direction](visual-direction.md) | Appearance and motion quality contract, independent of renderer |
| Engineering research | [Rendering experiments](rendering-experiments.md) | Engine comparison, hardware targets, instrumentation and gates |
| Production tooling | [Asset toolkit](asset-toolkit.md) | Agent-accessible source-art and asset production pipeline |
| Evidence and decisions | [Research register](research-register.md) | Research leads, hypotheses, open questions and decision process |

## Current status

- **Established direction:** fictional Late Cretaceous-inspired archipelago; four main islands; dense, causally convincing landforms; continuous animal life rather than quest-led survival; environmental threats more common than predatory attacks; near-photorealistic rendering at 30 FPS minimum on the reference machine.
- **Named architecture (decided):** **RaukenState**, **BeastCore**, **InteractionsCore**, alongside SimCore, RaukenSim, FloraSim, FaunaSim and HeroSim. Logical in-process modules, not mandatory separate services.
- **Provisional:** exact island dimensions, separation dates, species anatomy, metabolic values, time-compression tuning, storm/flood intensity, engine selection and vendor dependencies. Detailed groundwater transport and continuous erosion are explicitly out of runtime scope.
- **Research required:** age-dependent sauropod integument (the quills are consciously speculative); Cretaceous botanical reconstruction; physiological parameter ranges; low-end-hardware renderer benchmarks.

## Rules for future agents

1. Treat this index as the entrance; read [Vision](vision-and-principles.md) before modifying any domain.
2. Keep **what exists** (world/species/ecology) separate from **how it looks** (visual) and **how it is implemented** (rendering/toolkit).
3. Use [Simulation architecture](simulation-architecture.md) for canonical component names and authority; don't invent player-only biological rules.
4. Keep render chunk visibility separate from biological activity and never tick plants just because they are rendered.
5. Preserve concrete user preferences even when scientifically improbable; favor evocative geography where coherent causal relationships can still be maintained.
6. Do not harden estimates into requirements without testing or an explicit design decision. Mark assumptions as *Proposed*, *To test*, *Unknown*, or *Decided*.
7. Make work reproducible. Research claims require real citations in future completed specifications; don't invent taxonomic evidence.
8. No gameplay implementation or vertical slice is currently requested by these documents. The renderer and asset toolkit documents describe **experiments** only.

## Proposed document maintenance

Each domain owner records changes, unresolved tensions, experiment outcomes, and cross-domain implications. Revisions to another domain's *contract* require a note in the research register. Specifications should remain readable independently, but this index is the source of truth for boundaries.
