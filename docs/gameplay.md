# Gameplay specification

**Domain:** Controls, feedback, lifecycle, experience. **Status:** First planning draft.

## Core loop

1. Enter the world as a juvenile recently beyond (or dispersing from) the protection/familiarity of its birth group.
2. Walk, run, look, investigate, approach, avoid, rest and deliberately choose routes.
3. Let instinctive routines exploit appropriate nearby affordances: feeding when hungry and within reach of suitable plants, drinking when thirsty beside accessible freshwater, grooming and posture adjustments during downtime.
4. Experience physiological consequences over credible time, not arcade hunger countdowns.
5. Learn a home range, exploit familiar resources, confront weather and terrain, encounter other animals and grow.
6. Remain free to leave: new valleys and marine crossings are feasible but risky.
7. Mature, possibly breed, age and die; allow another life afterward without supernatural inheritance of learned knowledge.

No mandatory quests, inventories, technology trees, crafting, collectible checklists or map-reveal towers.

## Embodied camera and movement authority

**HeroView** separates **camera placement** from **movement intent**. In body-relative direct mode, W always means forward from Smalltrotter's facing even if the orbit camera is in front of her. The orbit/follow camera holds a chosen orientation and pans/translates when Smalltrotter moves across the frame; it is not compelled to chase her heading.

A locally detached camera can fly **over a nearby hill** while Smalltrotter continues living, but stays within a **soft/hard tether** anchored to her; it cannot travel to another island. In camera-control input mode, ground selection requests a destination and HeroSim decides how to travel there, using only her senses for new hazards. Camera sightings do **not** grant her omniscience.

Intent types: **direct body-relative steering**, **persistent destination**, **uncommanded autonomy**. Normal hunger/thirst cannot hijack WASD and should not discard a destination; severe fear/pain can interrupt more readily in destination travel than direct control. Direct movement normally cancels old destinations. See [HeroView](hero-view.md).

## Control contract

**Explicit player controls:** movement direction and speed, camera/attention, deliberate interactions with other animals, voluntary rest/shelter, investigation and flight, optional social or breeding actions.

**Autonomous routines:** browsing, swallowing and chewing-like animation appropriate to anatomy; drinking; attention shifts; breathing; small balance and grooming movements; posture microadjustments. They must not wrest locomotion away from the player.

Interaction algorithm (conceptual):
- Current internal state establishes possible drives.
- Sensory/environmental query provides physically reachable food/water/rest affordances.
- Species and learned preferences score candidates.
- A low-cost local action begins only if compatible with player action and safety context.
- Movement, danger, deliberate interaction or loss of access interrupts naturally.
- Actual calories/water/biomass are changed by the ecological model; animation only represents the event.

Never eat undrinkable saltwater because it is water; do not vacuum biomass through rock or far outside neck reach.

## Simulation contract

**HeroSim** owns the player's condition and player-intention arbitration using shared **BeastCore** metabolic/sensory models also used by **FaunaSim**. **RaukenSim** provides weather/water, **FloraSim** finite food, **InteractionsCore** transfer results, **RaukenState** persistence and **SimCore** world time. Acute startle/pain and movement remain immediately responsive; thermal, hydration, digestion and developmental processes can be sampled at different slower rates.

## Physiological model

Maintain internal quantities separate from UI semantics:
- Energy balance and metabolic expenditure; gut fill, digestion queue, food fiber/quality and available reserves.
- Hydration, water content in forage, temperature-related loss, salinity and fluid status.
- Body temperature, radiant exposure, shade, wind, size and activity heat budget.
- Fatigue, stress and recovery, sleep/rest opportunity.
- Physical injuries, mobility effects, infections/parasites where tractable.
- Growth state, anatomical proportions, reproductive condition and senescence.

Values and mechanisms must be based on documented ranges or transparent experimental assumptions. Sim time should support long calm periods without constant button presses. Environmental temperatures affect physiology, not simply an 'overheated' damage meter.

Avoid assuming one food offers immediate calorie transfer. A fermenting herbivore can have gut contents with delayed energetic payback. Taste/food preferences need not equal true digestibility.

## UI and animal legibility

Prefer **diegetic-first, optional contextual HUD**:
- Normal state: no persistent barrage of bars.
- Noticeable states: restrained cues for thirst, forage deficit, thermal discomfort, fatigue, injury.
- On-demand condition view: body outline, growth, hydration/nutrition/thermal trends and injuries in plain qualitative terms; optional diagnostic numbers for accessibility/testing.
- Behavioral cues: posture, panting, gait, scanning, willingness to browse or drink, movement speed, vocal or body responses.
- Explain why an available-looking resource is unsuitable (e.g., brackish water), without giving the animal magical knowledge.

Playtest whether players can distinguish *hungry* from *digesting but low stomach fullness*, or *warm* from *heat stressed*. Don't conceal vital state so thoroughly that deaths feel arbitrary.

## Growth and long play

Life stages are overlapping continuous processes, not XP thresholds:
- **Young juvenile:** small reach and reserves, detailed low cover, limited mobility and hazard tolerance.
- **Older juvenile:** changing proportions and preferred forage, improved reach, altered routes.
- **Subadult:** greater biomass demand, open habitat and social opportunity.
- **Adult:** larger, less vulnerable to small predators, higher daily feeding requirements, viable reproduction.
- **Aging:** long-term wear, fertility and physical condition; continue playing as long as alive.

Changes in mass and body proportions affect gait, clearance, climbing, water depth tolerance, heat retention and browser reach. Some spaces accessible to juveniles cease to be usable by adults.

Parental protection is species-dependent and not assumed long for sauropods: begin near a familiar nursery/group if prolonged parental care is not scientifically defensible for a fictional interpretation.

## Navigation and exploration

- Real traversable terrain: cliffs are cliffs, some ravines have one-way-feeling descent, tidal crossings can close, narrow passes and headlands matter.
- No automatic fast-travel island teleport. Swimming and rare rafting or favorable shallows can enable crossings for appropriately capable species.
- Distance is meaningful because the player is small and usually not marching continuously.
- Memory/familiarity: world and creatures persist so recognizable feeding grounds, landmarks, nest sites and individuals remain identifiable. Optional animal-local memory influences preferences but not forced player decisions.
- Camera should serve juvenile body height; third-person and any alternate inspection perspectives should retain scale.

## Hazards

Primary pressure: drought, storms and flash floods, high tides, heat stress, wrong-way slope traversal, deep mud, falls, infection, malnutrition, accidental large-herbivore displacement. Predators have home ranges, limited information, search and hunger; no scripted homing.

Cause/consequence chains matter: a mild leg injury can make reaching food costly; a former crossing can flood; long exposure can induce dehydration. Not every poor choice immediately kills.

## Time, save and death

- Implement persistent time, weather and ecology without simulating every leaf offscreen at full fidelity.
- Favor meaningful days, seasonal shifts and generational lifespan rather than arcade timing.
- **Fluid time:** visible juvenile growth should emerge within a reasonably short play session. SimCore can accelerate world time/rest and shared species developmental curves may compress early growth; exact pacing remains under test.
- Real-time controls and acute sensory reactions cannot slow down just because world/developmental time advances faster. Comparable NPC juveniles must have compatible BeastCore growth rules.
- World and botanical state, wildlife population cohorts and the hero's life remain coherent after death. **Most wildlife is not a durable named individual**; only eligible previously-instantiated mature giant animals may retain identity.
- Consider starting a later life as a descendant only if birth and inheritance systems justify it.

## Initial usability tests

- Can a new player find food/water and remain alive without tooltips?
- Does autonomous browsing feel organic and interruptible?
- Does the animal avoid inappropriate food and saltwater?
- Does an injury change choices without arbitrary death spirals?
- Can a player inhabit one small territory for several simulated days without boredom driven solely by status bars?
- Does maturation materially change traversal and diet?
- Can the simulation produce quiet hours without forced events?

## Out of scope for this domain

Specific plant/species designs belong in [Flora](flora.md) and [Creatures](creatures.md). Persistence and ownership belong in [Simulation architecture](simulation-architecture.md); specifics in [HeroSim](hero-sim.md), [RaukenSim](rauken-sim.md), [FloraSim](flora-sim.md) and [FaunaSim](fauna-sim.md). Appearance belongs in [Visual direction](visual-direction.md); human-facing control/camera design belongs in [HeroView](hero-view.md).
