# FaunaSim — convincing local wildlife

**Domain:** Habitat populations, locally instantiated animals and ecological interactions. **Status:** Working design, detailed memory/biography simulation deliberately excluded.

## Intent

**FaunaSim exists to populate The Stalthosian Archipelago with convincing animals, not to reconstruct their complete lives.** Wildlife should mostly be living ordinary lives: resting, browsing, basking, yawning, wandering a little, observing without reacting dramatically. Predators should often be sated, cautious or simply uninterested. Comfortable animals are allowed to remain inactive for long periods.

Example: a well-fed adult megalosaurid reclines in shade on a hill. It notices Smalltrotter crossing the valley, lifts its head to watch, then lies back down. Hunting is not compelled by an AI update. An animal is not a player-centered event dispenser.

## Three representations and bounded individual retention

| State | Meaning | Persistence |
|---|---|---|
| **Regional population** | Species/age cohorts, habitat suitability and approximate ecological pressure | Persistent **aggregate**, no individual identity |
| **Active instantiated animal** | Locally relevant animal with body, sensory state, behavior and nearby contacts | Reserved from a cohort, active only while needed |
| **Dormant retained individual** | A **previously instantiated** animal whose specific identity still matters | Compact identity, age, appearance, condition, broad location and essential ties; coarsely advanced |

Ordinary wild animals retire to the cohort ledger when no longer locally relevant. **Selected previously instantiated notable giants are not the only retention case**: Reedcrest's bonded peers, dependent Longstride young or an active caregiving parent (including a wild parent of a playable hatchling), and similarly justified animals may retain compact identity. This is bounded and must not become a global list of personal histories.

A retained individual is **not** continuously simulated in full detail. It advances coarsely from its last evaluated world-time timestamp: aging, plausible movement between regions, condition, mortality and essential social/dependence changes. Reinstantiation is possible only where this continuation places a *survivor*. It may die, lose its identifying relationship, disperse or **decay to cohort state** when retaining its identity no longer matters. Following a player across terrain or sea is neither a teleport nor a guarantee of success.

Each new player hatchling arises as an ordinary species member in a suitable **existing** population. Death of a Hero Beast must not delete unrelated retained animals, reroll the archipelago, or keep former acquaintances permanently alive.

No daily route logs, detailed lifelong memory graphs, pre-generated giant registries, exact parentage records or full offscreen animal biographies.

## Population accounting

Regions define species/age-cohort occupancy and suitability using geology, climate, flora productivity, water and general habitat. They need not instantiate anyone until a local simulation region is activated.

- On activation, budget/reserve actual local animals from population distributions.
- Active individuals interact with local flora and fauna through InteractionsCore; they may consume food or sustain injuries.
- On retirement, release an individual's demographic slot back to its population (or mark its birth/death/exit) so it cannot be counted twice.
- A retained individual is **still accounted for** against its population. It does not appear in addition to a sampled animal of the same cohort.
- Short-lived disturbance/occupancy/cooldown of a locality may prevent immediate replacement when a Hero Beast turns away.
- Avoid minute-by-minute virtual population biographies offscreen; a coarse ecological accounting is sufficient for changing numbers, energy pressure and seasonal habitats.

## Durable population ledger — not individual biographies

**The region/species/age cohort is the durable demographic unit.** Distinguish:
- **Abstract available** cohort count or statistical density.
- **Active reserved** local instantiated animals, counted as members of the same cohort.
- **Retained reserved** eligible **previously instantiated** individuals (bonded peers, dependent young, selected notable mature animals), still drawn from—not added on top of—the cohort.

For discrete animals, an accounting invariant is **total = abstract + active + retained** within a region/species/cohort, accounting for any transfers in flight. Only births, deaths, immigration and emigration change a region's total; age transitions move members between cohorts. A moved animal debits one region and credits another once. Large populations of tiny creatures may instead use density/expected abundance with explicit rounding/sampling rules.

Use stable operation IDs or region version checks on activation/retirement so overlapping prewarm/release operations cannot double-reserve. **Repeated crossings of a chunk boundary must not repeatedly generate new animals.** Keep short activation grace time, active-set hysteresis and coarse local occupancy/disturbance/cooldown, not lifelong individual memory.

An individual can disappear forever as a named object while **its demographic and ecological contributions remain**. Preserve cohort totals/age structure, approximate reproductive and mortality outcomes, and regional foraging/occupancy pressure. Precision of rates is a tunable ecological approximation; exact headcounts are not required for insects.

### Aggregate resource consequences

For each habitat/cohort interval, derive bounded **forage demand by plant resource class**, water requirements and coarse browsing pressure. InteractionsCore applies batched, finite debits to FloraSim patch/organism resources, with actual granted amount returned to FaunaSim. No invisible herd may consume unavailable biomass twice, and consumption must affect what a Hero Beast later encounters.

A cohort's feeding and energy state can use approximate budgets; we do **not** reconstruct specific remote bites, routes, gut histories, matter cycles or every death. Mass removed from vegetation is not equal to body mass gained. If a region lacks enough forage, model a coarse consequence (e.g. poorer condition, dispersal pressure, lower reproduction or mortality risk), not magical replacement food.

Test demographic/resource invariants after repeated enter/leave, offscreen season advancement and retained-individual reactivation.

## What an active animal needs

- Species and current age/stage; geometry/appearance seed.
- Position, speed, body orientation and physically plausible movement.
- Simple relevant BeastCore drives: satiety, fatigue, thermal comfort, alertness, acute pain, fear/stress and relevant social disposition.
- Active behavioral activity and continuity: resting, feeding, drinking, watching, grooming, locomoting, investigating, pursuing or fleeing.
- Brief local attention/sensory state, not a durable memory graph.
- Local interaction/resource access and explicit response to relevant events.

An idle animal should **not** randomly reroll behaviors every evaluation. Use state persistence and hysteresis so comfort means remaining comfortable until something changes. Interest in prey is condition-dependent: a sated predator may watch instead of attack. Close intrusion or injury can still trigger defensive reactions.

## Update cadence and sensory reactions

Nearby animal movement, collision, immediate pain/startle and urgent sensory stimuli are actively handled. Thermal comfort, ongoing stress and attention run at moderate rates; satiety, hydration, fatigue and growth can advance less often or by elapsed time. No universal 60 Hz biography tick.

Perception uses local line-of-sight/occlusion, sound and simplified wind/odor where relevant. FaunaSim isn't granted omniscience about the Hero Beast or invisible prey. HeroSim's high fidelity does not force every NPC to the same computational cost; both share BeastCore species and physiology rules.

## Regional activation beyond view

**Simulation chunks prewarm and extend beyond both the Hero Beast's current senses and HeroView's bounded local camera envelope.** The world on the other side of a nearby ridge must already have its animals behaving before the camera sees them.

FaunaSim instantiation is separate from renderer visibility. Active animals may be offscreen, obscured or farther from the hero than her perceptual range. A camera pan cannot directly create/despawn the predator it reveals.

In contrast, no requirement exists to instantiate every animal on Outer Reach while the hero is on Main Island. Distant regions remain demographic populations, not remote wildlife soap operas.

## Interactions and outputs

- **StalthosSim:** weather, local temperature/wind/water and extreme conditions.
- **FloraSim/InteractionsCore:** finite vegetation and water/resource outcomes, plant damage and other organism interactions.
- **HeroSim:** receives only relevant sensed or contacted stimuli; the player animal is another organism, not an NPC omniscience target.
- **StalthosState:** maintains population/cohort records, local occupancy/cooldowns and a bounded set of **previously instantiated** retained individuals with active social, dependent or notable reasons.
- **Renderer/HeroView:** receive body pose, movement, behavioral intent and appearance, not private future plans or complete internal biographies.

## Shared wildlife behavior and species relationships

- Wild adult **Brackenbacks** may defend any distressed animal perceived as small and vulnerable, including an unrelated adult Thistletail, and may occasionally posture at an ambiguous bush or rock. Perception uncertainty, physical risk and habituation govern response; no scripted universal rescue.
- **Reedcrest** youngsters from neighboring near-synchronous nests may form small, distinctive mutual bonds; they can initiate movement, separate, search, reunite and cross water only under real navigational constraints. No fixed player-follower leash or magically restored squad slots.
- **Longstride** care is asymmetric: young follow their parent, accept food/protection, learn increasing independence and eventually disperse. The reverse starting circumstance—a hatched playable Longstride with a wild parent—must use compatible biology. Maintain identity only while the relationship still warrants it.
- Local insects, small prey and detritivores can have resource/cohort representation with a few opportunistically instantiated individuals; Thistletail needn't force a million individually ticking insects.
- Social instincts are species-defined. A reusable bounded identity-link representation is sufficient; no general biography or genetic optimization simulator.

## Acceptance scenarios

9. A later player life can encounter a surviving prior companion or offspring correctly aged and moved; no duplicate or resurrected dead individual.
10. Reedcrest companions and Longstride young crossing separate paths or straits use real individual movement and cohort debits/credits.
11. A wild Brackenback alarms at a surprising bush, or blocks a predator approaching a distressed small stranger, without a player-driven script.


1. A sated megalosaurid can watch Smalltrotter amble through its valley without pursuing her; its idle behavior stays coherent for minutes.
2. Nearby grazing animals continue activity while occluded or outside the camera frustum.
3. Small/juvenile animals can disappear from long-term individual tracking after deactivation without causing visible popping or mass duplication.
4. Eligible previously instantiated bonded peers, dependent offspring and notable mature animals can reappear with recognizable shape/condition after coarse catch-up; **never-instantiated** animals have no identity record.
5. Fauna regional populations and active/retained counts reconcile across visits.
6. Startle and acute pain affect active animals promptly without long-term psychological history tracking.
7. FaunaSim and HeroSim use compatible BeastCore rules, but FaunaSim chooses lower fidelity when adequate.
8. Wildlife instantiation remains independent from the player camera's instantaneous orientation.

Related: [Spatial activation](spatial-activation.md), [HeroView](hero-view.md), [HeroSim](hero-sim.md), [Simulation architecture](simulation-architecture.md).
