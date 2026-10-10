# FaunaSim — nonplayer animal ecology

**Domain:** Wild animal individuals, behaviors and population processes. **Status:** Conceptual planning, no rates fixed.

## Ownership

FaunaSim owns nonplayer animals: alive/dead, locations and trajectories, behaviors, condition, feeding and reproductive states, social association, remembered places, and coarse population histories.

**BeastCore** supplies the shared anatomical/physiological/sensory rules also used by HeroSim. FaunaSim does not reimplement thirst, thermoregulation or growth to make wild animals follow different laws. Fidelity and update intervals differ; biology should not.

## Multirate, event-responsive animals

- **Immediate:** collisions, injury responses, startle and new sensory stimuli.
- **High-rate local:** motion, orientation, avoidance, foot placement/collision as needed by actual nearby simulation and physics.
- **Medium-rate:** thermal discomfort, alertness, continuing pain, local decision reevaluation.
- **Slow-rate:** hydration, digestion, energy expenditure/recovery, reproductive condition and development.
- **Very slow:** aging, background mortality, herd dynamics and population-level change.

The frequencies are chosen through profiles and measured load rather than fixed constants or a separate timer per statistic. HeroSim receives priority for accurate immediate responses, but FaunaSim remains active for relevant nearby wildlife even when hidden behind foliage.

## Perception and behavior

No omniscient nearest-player checks. Sight requires visibility and occlusion, hearing may be obstructed/attenuated by terrain and weather, smell depends on wind and distance in a deliberately approximate model. Attention, habituation, arousal, hunger and prior experience influence action selection. Predators seek food for their own reasons; their encounters aren't spawned to entertain the player.

Animal drives do not force physical movement independently of physical feasibility. Choose paths and targets from known/perceived opportunities.

## Spatial fidelity

1. **Close:** actual individuals, locomotion/avoidance and physiological responses.
2. **Nearby but not visible:** individuals and interactions at reduced fidelity.
3. **Regional distant:** home-range movement, group aggregates, deaths/births, biomass demands and foraging pressure.
4. **Dormant/checkpointed:** coarse history-to-time reconciliation.

Promoting an aggregate to individual creatures cannot multiply animals or invent unlimited biomass. Significant established animals retain identity, memory and injuries across fidelity changes.

## Cross-domain use

- RaukenSim provides current exposure, water, wind and hazardous storm/flood conditions.
- FloraSim supplies finite edible plant matter and affected plant states; transfer through InteractionsCore.
- HeroSim is another animal in shared physical space, not a magical universal target.
- RaukenState persists identities, regions, histories and long-term resources.
- Renderer requests locally relevant representations; it doesn't direct animal births/biological updates.

## Tests

Player leaves and returns to find persistent fauna; offscreen herbivores consume flora resources; no duplicated animals when crossing LOD boundaries; pain/startle reactions remain immediate when nearby; a distant herd doesn't require 60 Hz animation/sensing; weather can alter movement/thermal behavior without arbitrary scripted encounters.

See [Creatures](creatures.md), [BeastCore and HeroSim contracts](hero-sim.md), [Architecture](simulation-architecture.md).
