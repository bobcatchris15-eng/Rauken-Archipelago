# Gameplay specification

**Domain:** Controls, feedback, lifecycle, experience. **Status:** First planning draft.

## Core loop

1. Hatch as an otherwise ordinary individual of the selected Hero Beast species, inside an established wild population and its species-specific nesting/social circumstances.
2. Directly steer or select deliberate intentions when desired; otherwise watch HeroSim live the animal's normal life.
3. Let instinctive routines exploit appropriate nearby affordances: feeding when hungry and within reach of suitable plants, drinking when thirsty beside accessible freshwater, grooming and posture adjustments during downtime.
4. Experience believable visible physical consequences at comfortable timescales, not precise hidden metabolism or arcade hunger countdowns.
5. Live an ordinary local animal life around usable food, water, shelter and companions; confront weather and terrain, encounter other animals and grow. Larger adventures mainly arise from player intention or genuine ecological pressure, not an autonomous exploration drive.
6. Remain free to leave: new valleys and marine crossings are feasible but risky.
7. Mature, optionally court/mate/nest/tend young, age and die; hatch a new animal in the same continuing world with no inherited player progress.

No mandatory quests, inventories, technology trees, crafting, collectible checklists or map-reveal towers.

## Embodied camera and movement authority

**HeroView** separates **camera placement** from **movement intent**. In body-relative direct mode, W always means forward from Smalltrotter's facing even if the orbit camera is in front of her. The orbit/follow camera holds a chosen orientation and pans/translates when Smalltrotter moves across the frame; it is not compelled to chase her heading.

A locally detached camera can fly **over a nearby hill** while Smalltrotter continues living, but stays within a **soft/hard tether** anchored to her; it cannot travel to another island. In camera-control input mode, ground selection requests a destination and HeroSim decides how to travel there, using only her senses for new hazards. Camera sightings do **not** grant her omniscience.

Intent types: **direct body-relative steering**, **persistent destination**, **occasional player-invoked contextual response**, **uncommanded full autonomy**. Normal hunger/thirst cannot hijack WASD and should not discard a destination; severe fear/pain can interrupt more readily in destination travel than direct control. Direct movement normally cancels old destinations. See [HeroView](hero-view.md).

## Direct-control obstacle behavior

Direct input says **"try to go this way"**, not "navigate around everything until you can." The animal automatically handles foot placement, stability and modest local sidesteps. But an automatic route whose **lateral deviation leaves the camera's central-third-width steering corridor** is disallowed; this is a screen-space constraint on *self-chosen detours relative to the commanded course*, not a rule pinning a deliberately side-on moving animal to the middle of the picture.

If a rock/log/cliff leaves no admissible local correction, stop advancing and let the animal **inspect the obstruction** while direct intention remains active. The player can steer differently or release control; release restores full HeroSim autonomy, including deciding to take a completely different route. Destination TravelTo is unrestricted by this direct-steering detour corridor, though still physically constrained. The motor controller does **not** override the player's chosen travel direction by plotting a major detour.

The rule must work for all playable anatomies, not only quadrupedal Smalltrotter. See [HeroSim](hero-sim.md) and [HeroView](hero-view.md).

## Control contract

**Explicit player controls:** movement direction and speed, camera/attention, optional destinations and deliberately invoked contextual intentions for investigation, social contact, threat, predation, nesting or withdrawal. The contextual response interface does **not** appear automatically around ordinary resources.

**Autonomous routines:** opportunistic browsing **while walking**, chewing, drinking, gaze and attention shifts, breathing, small prey-snatching, social calls/contact, sniffing, grooming, balance and posture adjustments. Compatible body regions may act concurrently with locomotion. With no commands, HeroSim initiates ordinary travel, foraging, social responses, rest, flight and risk assessment. Direct steering overrides voluntary navigation, not feasible reflexes or anatomy.

Interaction algorithm (conceptual):
- Current internal state establishes possible drives.
- Sensory/environmental query provides physically reachable food/water/rest affordances.
- Species and learned preferences score candidates.
- A low-cost local action begins only if compatible with player action and safety context, potentially while feet/body continue moving under player steering.
- Movement, danger, deliberate interaction or loss of access interrupts naturally.
- Actual calories/water/biomass are changed by the ecological model; animation only represents the event.

Never eat undrinkable saltwater because it is water; do not vacuum biomass through rock or far outside neck reach.

## Simulation contract

**HeroSim** owns the player's condition and player-intention arbitration using shared **BeastCore** metabolic/sensory models also used by **FaunaSim**. **StalthosSim** provides weather/water, **FloraSim** finite food, **InteractionsCore** transfer results, **StalthosState** persistence and **SimCore** world time. Acute startle/pain and movement remain immediately responsive; thermal, hydration, digestion and developmental processes can be sampled at different slower rates.

## Contextual intentions and documentary observation

Routine eating, drinking, looking about, calling and locomotion-compatible behavior **never need an interaction prompt**. The player may optionally open a small slow-time response chooser to express a specific intention that is not already emerging organically: inspect *that* unusual object, greet *this* companion, interpose against *that* predator, select *this* nest site, or commit to stalking prey. Offered options derive from actual senses, species anatomy and situation; the chooser never pops up by itself. Its selection produces a **HeroSim intent**, not a guaranteed animation, attack, social outcome or magically reachable target. SimCore owns the slowdown of the immediate world and resumes shared time without desynchronizing wildlife.

With neither active steering nor a maintained player intent, **HeroSim governs the entire animal**. It may forage, travel among nearby resources, react socially, avoid hazards, reproduce or die. It behaves like an ordinary creature within a practical ecological home range, not an adventurer seeking the next valley. There is no arbitrary idle-radius leash: shortage, danger, dispersal or other real pressures may shift its whereabouts. Direct steering immediately recovers control, subject to real physical limits and brief genuine involuntary responses.

When the player also leaves the camera alone, **HeroView gradually enters documentary composition**: gentle body-centered orbit/follow, coherent continuous physical camera motion and well-framed portrait, social or environmental shots. It need not spin constantly or cut to unrelated action; direct camera input immediately interrupts. Alarms can briefly focus attention without inventing sensed information. Documentary observation is the real simulation, not a risk-free spectator variant. A useful acceptance target is thirty minutes of engaging animal behavior with no player commands.

## Detached observation, shared intentions and dual audio

Camera detachment is **an observation choice, not a switch to puppet or idle mode**. The Hero Beast continues its own life and may move, forage, socialize or react independently. A point/destination/contextual action selected by the player becomes **the animal's own prioritized intention**; all subsequent locomotion and incidental behavior comes from the same HeroSim/BeastCore mechanisms as if it had wanted to do that naturally. The player can steer directly to override, and when the suggested goal completes/fails the animal resumes autonomous goal selection. The only privileged knowledge supplied is the requested destination/target itself, **not** how to avoid hidden dangers.

**Audio follows the player's camera when detached.** The player may hear a herd or predator from over a ridge while the animal remains oblivious because its ears are elsewhere. When the call finally reaches the animal, HeroSim may react. Spatial sources are shared, but **player listening and animal hearing are separate**; alarm camera recall derives only from the animal's own sensory experience. Restrained body feedback remains possible without loud close-miked breathing across a valley.

## Reproduction, early care and successive lives

- Reproduction is part of the game, not a peripheral optional statistic menu. Species-appropriate courtship, mating, nest preparation, laying, care/incubation and hatching are interactive or observable.
- Target **thirty minutes or less for a focused nesting-to-hatching episode**, using accelerated or interruptible rest through the **single SimCore world time** and credible regional consequences. Not thirty minutes for every offspring to grow up: post-hatch dependence can last through substantial normal play.
- Parenting is **species-specific**: Smalltrotter young are largely on their own; Brackenback youngsters loosely congregate amid protective unrelated adults; Reedcrest peers form a synchronized nesting-ground kindergarten; Thistletail cares briefly then disperses; Longstride has the longest parental dependence, with youngsters following and learning from a parent.
- No breeding-stat minigame, genetic optimization, required clutch success, compulsory offspring care or lineage-based advancement.
- Death is an ordinary animal death. A new session in the **same persistent world** hatches a generic new member of a chosen local species population. Surviving nests, companions, dependent young, corpses and previously instantiated retained wildlife obey ordinary persistence/cohort rules and biological advancement. The new Hero Beast inherits none of the prior animal's relationships or special knowledge.

## Physiological model

The player should see **convincing bodily needs and consequences**, not the machinery of a detailed biological simulation. BeastCore may use a few inexpensive species-tuned quantities:

- **Food condition:** rough hunger/satiety and forage suitability, without detailed gut chemistry or calorie conservation.
- **Water and thermal comfort:** simple thirst/heat/cold/exposure cues; actual fresh versus saline water matters.
- **Rest/stamina:** plausible exertion, slowdown and resting.
- **Injury/stress:** immediate responses with an affordable lingering severity/recovery timer when noticeable.
- **Age/reproduction:** simple species growth-stage curves, maturity and late-life decline.

These variables can be combined or split only if that improves **visible** behavior. Do not begin with a metabolic organ model, digestion queue, precise body heat budget, infection ecology or exact nutrition equation. Feedback stays legible and restrained; ordinary comfortable animals should spend long periods doing very little.
## UI and animal legibility

Prefer **diegetic-first, optional contextual HUD**:
- Normal state: no persistent barrage of bars.
- Noticeable states: restrained cues for thirst, forage deficit, thermal discomfort, fatigue, injury.
- On-demand condition view: body outline, growth, hydration/nutrition/thermal trends and injuries in plain qualitative terms; optional diagnostic numbers for accessibility/testing.
- Behavioral cues: posture, panting, gait, scanning, willingness to browse or drink, movement speed, vocal or body responses.
- Explain why an available-looking resource is unsuitable (e.g., brackish water), without giving the animal magical knowledge.

Playtest whether players can distinguish *hungry* from *digesting but low stomach fullness*, or *warm* from *heat stressed*. Don't conceal vital state so thoroughly that deaths feel arbitrary.

## Development and time compression — deliberate tradeoff

**One SimCore world/calendar clock**, with a pleasant accelerated day/night cycle and faster advancement during rest or nesting. Realtime controls, movement, collisions and acute danger remain responsive. Species have simple staged life histories—hatchling, juvenile, subadult, adult, aging—with sufficiently continuous visual/movement transitions. Exact lifespans, reproduction windows and time multipliers are **playtest tunables**.

Adequate food permits growth; prolonged shortage may slow it. No exact kilograms gained or metabolic integration required. Player and active wild conspecifics should **appear to age comparably**, while remote cohorts use coarse stage probabilities. Time-skips check meaningful threats and save important outcomes instead of simulating every unseen day.

Judge pacing by the *experience*: juvenile growth is noticeable, adulthood lasts, seasonal changes register and parenting stays interesting. Biological precision is not a goal.
## Growth and long play

Life stages are overlapping continuous processes, not XP thresholds:
- **Young juvenile:** small reach and reserves, detailed low cover, limited mobility and hazard tolerance.
- **Older juvenile:** changing proportions and preferred forage, improved reach, altered routes.
- **Subadult:** greater biomass demand, open habitat and social opportunity.
- **Adult:** larger, less vulnerable to small predators, higher daily feeding requirements, viable reproduction.
- **Aging:** long-term wear, fertility and physical condition; continue playing as long as alive.

Changes in mass and body proportions affect gait, clearance, climbing, water depth tolerance, heat retention and browser reach. Some spaces accessible to juveniles cease to be usable by adults.

Early life begins at hatching; parental protection and developmental acceleration differ by species. A Longstride begins under a caring parent, Brackenback among communal young, Reedcrest among neighboring synchronized nests, Thistletail with a brief attendant parent and Smalltrotter near largely independent hatchlings.

## Navigation and exploration

- Real traversable terrain: cliffs are cliffs, some ravines have one-way-feeling descent, tidal crossings can close, narrow passes and headlands matter.
- No automatic fast-travel island teleport. Swimming and rare rafting or favorable shallows can enable crossings for appropriately capable species.
- Distance is meaningful because the player is small and usually not marching continuously.
- **Animal memory is short-term only:** keep a small expiring working set of recently sensed objects, hazards and immediate action context (so an occluded predator is not forgotten instantly). Do not accumulate a learned map, stored routes, lifelong familiarity scores or a remembered home-location objective. The *player* may recognize persistent landmarks and places, but the animal need not learn them.
- **Relocation:** after the player takes an animal to an unfamiliar valley and releases control, it lives locally from its current senses and needs instead of automatically attempting to return home. Durable social/dependence ties remain narrow biological exceptions, not general geographic memory.
- Camera should serve juvenile body height; third-person and any alternate inspection perspectives should retain scale.

## Hazards

Primary pressure: drought, storms and flash floods, high tides, heat stress, wrong-way slope traversal, deep mud, falls, infection, malnutrition, accidental large-herbivore displacement. Predators have home ranges, limited information, search and hunger; no scripted homing.

Cause/consequence chains matter: a mild leg injury can make reaching food costly; a former crossing can flood; long exposure can induce dehydration. Not every poor choice immediately kills.

## Time, save and death

- Implement persistent time, weather and ecology without simulating every leaf offscreen at full fidelity.
- Favor meaningful days, seasonal shifts and generational lifespan rather than arcade timing.
- **Fluid time:** visible juvenile growth should emerge within a reasonably short play session using a simple species life-stage curve on SimCore's shared clock; exact pacing remains under test.
- Real-time controls and acute sensory reactions cannot slow down just because world/developmental time advances faster. Comparable NPC juveniles must have compatible BeastCore growth rules.
- World and botanical state, nests, corpses, cohorts and eligible previously instantiated wildlife continue across player deaths. Most wildlife is not a durable individual, but relevant bonded peers, dependent offspring and selected notable giants may retain compact identity that advances coarsely or later expires.
- New player lives are **ordinary hatchlings from existing species populations**, not designated descendants, reincarnations or recipients of inherited traits.

## Initial usability tests

- Can Smalltrotter pluck reachable foliage while the player keeps moving without invoking UI or stopping her feet?
- Does a fully autonomous Hero Beast continue believable travel, feeding and relationships under passive documentary observation?
- Does a deliberately opened response wheel produce an intent, not a scripted guaranteed outcome, and otherwise stay entirely out of the way?
- Can a player hatch, experience appropriate parental behavior, tend a nest within a short accelerated episode and remain with dependent young afterward?
- Does another player life find a continuing world without resurrecting, duplicating or protecting earlier individuals?


- Can a new player find food/water and remain alive without tooltips?
- Does autonomous browsing feel organic and interruptible?
- Does the animal avoid inappropriate food and saltwater?
- Does an injury change choices without arbitrary death spirals?
- Can a player inhabit one small territory for several simulated days without boredom driven solely by status bars?
- Does maturation materially change traversal and diet?
- Can the simulation produce quiet hours without forced events?

## Out of scope for this domain

Specific plant/species designs belong in [Flora](flora.md) and [Creatures](creatures.md). Persistence and ownership belong in [Simulation architecture](simulation-architecture.md); specifics in [HeroSim](hero-sim.md), [StalthosSim](stalthos-sim.md), [FloraSim](flora-sim.md) and [FaunaSim](fauna-sim.md). Appearance belongs in [Visual direction](visual-direction.md); human-facing control/camera design belongs in [HeroView](hero-view.md).
