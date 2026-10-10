# FaunaSim — convincing local wildlife

**Domain:** Habitat populations, locally instantiated animals and ecological interactions. **Status:** Working design, detailed memory/biography simulation deliberately excluded.

## Intent

**FaunaSim exists to populate The Stalthosian Archipelago with convincing animals using cheap staged populations, not to reconstruct their complete lives or balance a closed food web.** Wildlife should mostly be living ordinary lives: resting, browsing, basking, yawning, wandering a little, observing without reacting dramatically. Predators should often be sated, cautious or simply uninterested. Comfortable animals are allowed to remain inactive for long periods.

Example: a well-fed adult megalosaurid reclines in shade on a hill. It notices Smalltrotter crossing the valley, lifts its head to watch, then lies back down. Hunting is not compelled by an AI update. An animal is not a player-centered event dispenser.

## Three representations and bounded individual retention

| State | Meaning | Persistence |
|---|---|---|
| **Regional population** | Species abundance, habitat suitability, broad age mix and occupancy hints | Cheap **approximate aggregate**, no individual identity |
| **Active instantiated animal** | Locally relevant animal with body, sensory state, behavior and nearby contacts | Selected from regional availability; active only while needed |
| **Dormant retained individual** | A **previously instantiated** animal whose identity still matters | Compact identity, age/appearance, broad location and essential ties; coarsely advanced |

Ordinary wild animals retire to approximate regional availability when no longer locally relevant. **Selected previously instantiated notable giants are not the only retention case**: Reedcrest's bonded peers, dependent Longstride young or an active caregiving parent (including a wild parent of a playable hatchling), and similarly justified animals may retain compact identity. This is bounded and must not become a global list of personal histories.

A retained individual is **not** continuously simulated in full detail. It advances coarsely from its last evaluated world-time timestamp: aging, plausible movement between regions, condition, mortality and essential social/dependence changes. Reinstantiation is possible only where this continuation places a *survivor*. It may die, lose its identifying relationship, disperse or **decay to cohort state** when retaining its identity no longer matters. Following a player across terrain or sea is neither a teleport nor a guarantee of success.

Each new player hatchling arises as an ordinary species member in a suitable **existing** population. Death of a Hero Beast must not delete unrelated retained animals, reroll the archipelago, or keep former acquaintances permanently alive.

No daily route logs, detailed lifelong memory graphs, pre-generated giant registries, exact parentage records or full offscreen animal biographies.

## Population accounting

**Regions contain approximate wildlife availability, not an exact balanced headcount.** A region/species can use habitat suitability, coarse density, broad age mix, season and short occupancy hints. When locally activated, select plausible animals and let them begin lightweight responsive behavior *before* the player or detached camera sees them.

**Promotion safety matters more than cohort arithmetic:** a currently active or retained creature must not also be sampled as a new animal. Track a small active/retained-ID exclusion and locality cooldown. On retirement, ordinary nonretained animals can disappear into approximate region density; known deaths and other conspicuous changes should influence immediate revisits.

There is no requirement for a global conservation law covering every regional birth, death, crossing, migration or predator meal. Coarse populations must look plausible, resist repeated camera-turn repopulation and respect retained individual identities.
## Durable population ledger — not individual biographies

**Durable background state** is mostly species density/abundance by region, habitat suitability and recent occupancy/disturbance. Retain an individual identity only after instantiation and only for established social, dependent or notable cases.

For locally active/retained wildlife, a simple exclusion check prevents visible duplication and resurrection. An already retained companion cannot exist in two places at once; a documented death stays dead. Distant populations may change through coarse seasonal probabilities. Do not require the sum of abstract + active + retained entities to reconcile exactly across the archipelago, precise migratory debit/credit bookkeeping, per-cohort calorie models or historical event journals.

### Approximate forage and predation pressure

Active animals use plausible food interactions with visible outcomes. Distant animals can exert a simple seasonal forage/depletion bias on regional plant cover and a broad predation/mortality tendency on species density. Resource scarcity can make local animals sparser or prompt plausible relocation; it need not balance exact calories, biomass and birth/death rates.

**Acceptance:** repeated visits and chunk boundary crossings never duplicate a known animal, revive a confirmed death, spawn a herd at a camera turn or erase visible recent depletion. Mathematical population balance beyond that observable result is not a goal.
## Short-lived attention, local ranging and limited memory

Active wildlife uses the same **small, expiring working-memory principle** as HeroSim: keep current sensory focus, immediate goals and a bounded amount of recent context (such as a predator briefly passing behind cover), without building learned landmark maps, lifelong routes or generalized experience histories. Short-lived habituation can prevent repeated Brackenback false alarms but naturally fades. Ordinary individuals need no long-term geographic memory records when returned to cohorts.

Comfortable, adequately supplied animals primarily live within ecologically plausible local ranges: feeding, resting, drinking, socializing and making short trips. Range size and movement frequency depend on species and habitat; there is **no universal idle leash**, nor an intrinsic sightseeing/exploration objective. Actual scarcity, dispersal, pursuit, threats, weather or reproductive movement may carry an animal much farther. An animal displaced by events or player direction simply resumes suitable local behavior where it finds itself; there is no default long-range homing quest.

Persistent regional distributions, habitat suitability, cohort movement and explicitly retained relationship/identity facts are **world/population state**, not a private learned map in every animal. Previously instantiated Reedcrest bonds and Longstride caregiver/dependent ties stay eligible for bounded persistence as already specified, without adding autobiographical memory.

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
- **FloraSim/InteractionsCore:** local feeding/contact outcomes and visible plant changes, not exact hidden resource balancing.
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
5. Known individuals and visible occupancy remain coherent across visits; background densities need only be plausible.
6. Startle and acute pain affect active animals promptly without long-term psychological history tracking.
7. FaunaSim and HeroSim use compatible **simple** BeastCore rules, but FaunaSim chooses lower fidelity when adequate.
8. Wildlife instantiation remains independent from the player camera's instantaneous orientation.

Related: [Spatial activation](spatial-activation.md), [HeroView](hero-view.md), [HeroSim](hero-sim.md), [Simulation architecture](simulation-architecture.md).
