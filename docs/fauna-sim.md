# FaunaSim — convincing local wildlife

**Domain:** Habitat populations, locally instantiated animals and ecological interactions. **Status:** Working design, detailed memory/biography simulation deliberately excluded.

## Intent

**FaunaSim exists to populate The Rauken with convincing animals, not to reconstruct their complete lives.** Wildlife should mostly be living ordinary lives: resting, browsing, basking, yawning, wandering a little, observing without reacting dramatically. Predators should often be sated, cautious or simply uninterested. Comfortable animals are allowed to remain inactive for long periods.

Example: a well-fed adult megalosaurid reclines in shade on a hill. It notices Smalltrotter crossing the valley, lifts its head to watch, then lies back down. Hunting is not compelled by an AI update. An animal is not a player-centered event dispenser.

## The three representations

| State | Meaning | Persistence |
|---|---|---|
| **Regional population** | Species abundance/age cohorts, habitat distribution and approximate seasonal activity | Persistent **aggregate**, no individual identity |
| **Active instantiated animal** | Locally relevant animal with position, variant, state, attention and animations; can exist beyond sight of player/camera | Temporary by default; counts reserved from its cohort |
| **Eligible retained giant** | Already-instantiated **mature** member of a **designated largest species** | Optional compact individual record after deactivation; no ongoing detailed simulation |

**Do not pre-instantiate mature megafauna across the islands.** Merely being an adult of a big species does not entitle an animal to persistent identity. A Dolores-like adult constrictor need not exist individually anywhere on Rainridge if Smalltrotter never approaches an area where one is instantiated.

The retention policy is intentionally narrow and bounded. Individuals of ordinary size, immature members of large species and most short-lived animals are reclaimed to population state when no longer active. Their turnover can be explained as dispersal, mortality, maturation or replacement **without simulating the journey**. Juvenile dispersal is species-dependent, not a universal biological law.

Do not maintain elaborate persistent home ranges, route networks, social graphs or lifelong memories for every animal. Even retained giants need only distinguishing appearance, general location/eligibility, life stage and coarse condition sufficient for a plausible re-encounter.

## Population accounting

Regions define species/age-cohort occupancy and suitability using geology, climate, flora productivity, water and general habitat. They need not instantiate anyone until a local simulation region is activated.

- On activation, budget/reserve actual local animals from population distributions.
- Active individuals interact with local flora and fauna through InteractionsCore; they may consume food or sustain injuries.
- On retirement, release an individual's demographic slot back to its population (or mark its birth/death/exit) so it cannot be counted twice.
- A retained adult is **still accounted for** against the population. It does not appear in addition to a newly sampled adult count.
- Short-lived disturbance/occupancy/cooldown of a locality may prevent immediate replacement when Smalltrotter turns away.
- Avoid minute-by-minute virtual population biographies offscreen; a coarse ecological accounting is sufficient for changing numbers, energy pressure and seasonal habitats.

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

Perception uses local line-of-sight/occlusion, sound and simplified wind/odor where relevant. FaunaSim isn't granted omniscience about Smalltrotter or invisible prey. HeroSim's high fidelity does not force every NPC to the same computational cost; both share BeastCore species and physiology rules.

## Regional activation beyond view

**Simulation chunks prewarm and extend beyond both Smalltrotter's current senses and HeroView's bounded local camera envelope.** The world on the other side of a nearby ridge must already have its animals behaving before the camera sees them.

FaunaSim instantiation is separate from renderer visibility. Active animals may be offscreen, obscured or farther from the hero than her perceptual range. A camera pan cannot directly create/despawn the predator it reveals.

In contrast, no requirement exists to instantiate every animal on Outer Reach while the hero is on Main Island. Distant regions remain demographic populations, not remote wildlife soap operas.

## Interactions and outputs

- **RaukenSim:** weather, local temperature/wind/water and extreme conditions.
- **FloraSim/InteractionsCore:** finite vegetation and water/resource outcomes, plant damage and other organism interactions.
- **HeroSim:** receives only relevant sensed or contacted stimuli; the player animal is another organism, not an NPC omniscience target.
- **RaukenState:** maintains population/cohort records, local occupancy/cooldowns and a small bounded set of **previously instantiated** retained adults.
- **Renderer/HeroView:** receive body pose, movement, behavioral intent and appearance, not private future plans or complete internal biographies.

## Acceptance scenarios

1. A sated megalosaurid can watch Smalltrotter amble through its valley without pursuing her; its idle behavior stays coherent for minutes.
2. Nearby grazing animals continue activity while occluded or outside the camera frustum.
3. Small/juvenile animals can disappear from long-term individual tracking after deactivation without causing visible popping or mass duplication.
4. Previously instantiated mature giants can reappear with recognizable shape/condition; **uninstantiated** giants have no individual records anywhere.
5. Fauna regional populations and active/retained counts reconcile across visits.
6. Startle and acute pain affect active animals promptly without long-term psychological history tracking.
7. FaunaSim and HeroSim use compatible BeastCore rules, but FaunaSim chooses lower fidelity when adequate.
8. Wildlife instantiation remains independent from the player camera's instantaneous orientation.

Related: [Spatial activation](spatial-activation.md), [HeroView](hero-view.md), [HeroSim](hero-sim.md), [Simulation architecture](simulation-architecture.md).
