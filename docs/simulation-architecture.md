# Simulation architecture — state, activation, perception and presentation

**Status:** Agreed logical boundaries; algorithms, distances and implementation framework remain provisional. These are **modules**, not independent network services.

## Named components

| Component | Owns | Does not own |
|---|---|---|
| **SimCore** | Shared timeline, variable time scale, scheduling, ordering, spatial **simulation chunk activation** | Weather, animal biology, camera |
| **StalthosState** | Persisted world/region/plant records, regional fauna cohorts, bounded eligible retained identities, saves and event history | A complete persistent biography for every animal; simulation itself |
| **StalthosSim** | Weather, day/night, seasons, local wetness, temporary storm/flood conditions and environment history | Runtime erosion/geology, organisms |
| **FloraSim** | All relevant botanical/fungal individuals and patches; growth, health, resources, death, lazy catch-up | Per-frame renderer polling |
| **FaunaSim** | Local active wildlife drawn from population cohorts, behavior, physiology at suitable fidelity; *optional bounded retention of previously instantiated relevant individuals* | Individual identities for never-instantiated wildlife, lifelong memories for ordinary animals |
| **HeroSim** | Current Hero Beast biology, autonomous behavior, player-intent arbitration, senses and involuntary responses | Camera knowledge or camera movement |
| **BeastCore** | Shared animal physiology, sensation, growth and behavior primitives used by HeroSim and FaunaSim | Its own ticking population |
| **InteractionsCore** | Validated cross-domain resource/damage/state transfers and outcome events | A master AI decision layer |
| **HeroView** | Player input/focus, direct movement/destinations, invoked contextual slow-time responses, documentary/alarm camera and human-facing experience | Biological truth, unrestricted spectator flight, injecting camera sight into HeroSim |
| **Renderer/physics/audio** | Scene rendering, local physical contact/animation and audio implementation | Persistence/biological authority, weather decisions |

**Ownership invariant:** one domain owns each mutable ecological fact. StalthosState stores agreed persistent representations without becoming a per-frame database bottleneck; InteractionsCore coordinates only significant cross-domain operations. Direct local reads and high-rate interactions should remain inexpensive.

## Conceptual data flow

```text
  Human  ->  HeroView (input focus, camera, destination picking)
                      | player intention
                      v
                   HeroSim <---- BeastCore shared with FaunaSim
                body + perception
                 ^     ^      ^
          StalthosSim FloraSim FaunaSim <--- SimCore simulation activation
              \        |      /
                   InteractionsCore
                         |
                    StalthosState

  World snapshots: StalthosState + domain sims -> scene streamer -> renderer
  Subjective/body signals: HeroSim ---------------------------> HeroView
  Visual/audio scene + body presentation ---------------------> human
```

This is **not** a fixed synchronous API chain. HeroSim senses a world through the Hero Beast's own body, not through the camera. The renderer ingests world renderables from the streamer/domain snapshots without routing whole scene graphs through HeroSim.

## Spatial lifecycle: three independent extents

1. **Active simulation:** SimCore prewarms and activates chunks around the Hero Beast, including a buffer beyond the **entire reachable envelope** of HeroView's nearby detached camera. FaunaSim begins local behaviors before the ridge is rendered; FloraSim bulk reconstructs the right plants/patches.
2. **Hero perception:** BeastCore/HeroSim evaluate what the Hero Beast could perceive from her body (eyes/ears/smell/contact, occlusion, attention); no omniscient camera data.
3. **Rendered scene:** HeroView's camera frustum and LOD choose what's drawn, including distant static scenery. The camera can show something she does not notice.

**A simulation chunk is not the same as a render chunk.** A renderer chunk unloading cannot kill a local animal. Camera flight over a nearby hill shouldn't cause a new herd to spring into existence only because it is now visible. Camera tether and simulation-buffer distances are open tuning parameters; avoid whole-island active simulation when the hero is far away.

[Spatial activation](spatial-activation.md) describes the activation/retirement lifecycle.

## What becomes instantiated

**Flora:** On simulation activation, FloraSim resolves plant individuals and colonies from static suitability, deterministic seeds and persisted events, lazily advancing growth to current world time. Trees retain recognizable age, shape and damage across reloads. Low ground cover can be population patches with fully rendered blades but not separate biology objects.

**Fauna:** Before local activation, regions have habitat-based **population/age cohorts**, not individually simulated or named animals. On activation FaunaSim reserves cohort counts and instantiates appropriate local animals (including ones outside camera view); these live, rest, browse, observe and react. On retirement most return to aggregate populations. Only **previously instantiated** animals still relevant as bonded companions, dependent young, participating caregivers or selected notable mature giants may keep compact dormant records. A hypothetical large constrictor never encountered is still only a cohort member, not a pre-existing personal record.

Individual retention and simulation fidelity are different axes: an active small transient creature can have responsive behavior; a retained social or notable individual can sleep as a tiny saved record. Cohort accounting prevents duplicate animals on reactivation. A short locality disturbance/cooldown may discourage conspicuous instant replacement without keeping per-animal biographies.

## HeroSim, HeroView and successive lives

**Direct body-relative steering** is the strongest voluntary human intervention. Ordinary hunger, curiosity and social impulses must not redirect player locomotion. Genuine physical incapacity or exceptional short reflexes can affect action. **Player-invoked** contextual response choices and persistent TravelTo destinations are higher-level intentions HeroSim must enact or fail under physical/sensory conditions, not guaranteed animations, strikes, mating outcomes or navigation.

**Direct locomotor correction policy:** BeastCore supplies camera-independent motor competence (foot placement, balance, small avoidance); HeroSim accepts movement intents from HeroView and rejects self-chosen route deviations exceeding a **central-third-wide screen-space corridor around the intended projected course**. If no valid local route exists, the Hero Beast stops and may inspect the obstacle until direct input changes or is released. Release restores ordinary full autonomy; destination mode remains free to plan wide routes. This corridor limits *automatic lateral deviation*, not deliberate side-on travel across a moving camera's entire screen. HeroView supplies projection/framing only, never extra animal sensory knowledge.

Compatible local behavior continues during direct locomotion: a Smalltrotter can pluck shrubs while walking, Reedcrest exchange calls, Thistletail snap up nearby morsels and Brackenback glance at questionable scenery without prompts. With no player locomotion or maintained deliberate intent, **full HeroSim autonomy** travels, feeds, rests, socializes, courts, parents, responds to danger and can die. No mandatory idle radius or protective documentary-only variant.

HeroView normally presents an animal-centered third-person orbit/follow camera, independent of the Hero Beast's heading. A bounded locally detached camera remains available; it never supplies the animal with omniscience. After camera inactivity, HeroView may gently transition to continuous documentary framing, following the Hero Beast's actual life without cinematic teleports or staged events. Significant *sensed* alarms may coordinate animal and camera attention on the same approximate world point and recall a detached camera smoothly toward the animal. Player camera input can immediately interrupt any automatic composition.

A newly selected Hero Beast **hatches as an ordinary population member** within appropriate species habitat, with its natural parental and juvenile circumstances. Breeding/nesting are playable: a short, accelerated, world-consistent nesting-to-hatching episode targets roughly thirty minutes or less, whereas dependent care may continue through ordinary play much longer. No genetic-optimization or inherited character-progression system.

Death terminates the current animal, **not the persistent world**. A new hatchling enters an existing population with no prior Hero Beast relationships or powers. Previously instantiated individuals remain under the same bounded FaunaSim identity-retention/decay policy, coarsely advancing while inactive, even between player lives. No life-change purge, teleporting companions or demographically duplicated wildlife.

## Resolution is not a single distance-based level

Apply three **independent design considerations** to each domain process:
- **Causal retention:** which effects must remain true, even when no individual is instantiated? Examples: population/cohort totals, forage depletion, an old tree's lost limb, persistent flood damage.
- **Temporal evaluation:** when does that process next have to be reconciled, or how much time may be aggregated? Regional browsing may integrate by week; local collisions must resolve immediately.
- **Representation:** what geometric, behavioral or physical detail is currently needed? A distant herd can be only a cohort ledger; a nearby transient animal can be richly animated.

Proximity influences **deadlines and visual detail**, not whether significant resource accounting exists. Do **not** implement a general-purpose causal-importance predictor or three-axis runtime LOD manager. Define domain-specific invariants and work queues: immediate contact, population/resource settlements, environmental interval integration, chunk prewarm, and graphics creation. Most scheduling can use a small number of priority/deadline classes.

## Four cross-domain contracts before implementation

1. **Counts and resources:** FaunaSim's demographic cohorts, active reservations and retained individuals balance. FaunaSim's aggregate browsing causes finite FloraSim resource debits through InteractionsCore; aggregate input/output need not conserve exact biological energy.
2. **Chronological environment:** StalthosSim provides time-ordered environmental intervals plus discrete damaging events. Averages alone are insufficient. Records may be compacted once all dependent state has safely passed them.
3. **Bounded catch-up:** Every region and durable organism/patch tracks evaluation time and version. SimCore amortizes reconciliation ahead of both Smalltrotter and the full HeroView tether; render work cannot trigger an unbounded biological replay.
4. **Stable structural edits:** Significant tree/shrub segment IDs survive growth and asset regeneration. InteractionsCore commits a precisely addressed finite change; FloraSim stores the resulting structural state, not every historic bite.

These are **contracts across existing modules, not new standalone subsystems**. See [FaunaSim](fauna-sim.md), [StalthosSim](stalthos-sim.md), [FloraSim](flora-sim.md) and [Spatial activation](spatial-activation.md).

## Time and update rates

SimCore owns global world-time progression (which may be accelerated through uneventful/rest periods). StalthosSim derives sun, seasons and weather from that timeline. Species-specific developmental pacing can make juvenile growth meaningfully noticeable without forcing animation/reflex speed to match accelerated years; HeroSim and FaunaSim use the same underlying BeastCore developmental laws. **Four meanings of time:** realtime physical controls/contacts; shared SimCore world/calendar time; physiology integrated over world intervals plus actual activity/event costs; and species life-history development derived from world time and condition. Physiology and development aren't independent hidden clocks.

- Direct physical response, collision, pain/startle: prompt real-time/event-driven.
- Local animal orientation and movement: active high-rate as needed.
- Thermal discomfort, attention and continuing pain: medium-rate.
- Hunger, thirst, gut, fatigue, health: slower or event-integrated.
- Growth, reproduction, botanical senescence: coarse/lazy.
- Inactive environment: compact time-window weather summaries retained for FloraSim and cohort catch-up.

Exact frequencies are unknown; don't demand one timer per internal variable.

## Environment and cross-domain changes

The map generator establishes mostly fixed streams, springs, terrain, soil, drainage and plant moisture suitability. StalthosSim handles day/night, weather and temporary storm-driven water level changes with **no routine erosion or detailed groundwater transport**.

FloraSim catches up plant health/age from stable suitability, environmental interval summaries and discrete browsing/storm events. InteractionsCore validates finite transfers (food into stomach, biomass removed; rain/damage effects; carcasses/deadwood), preventing double consumption and duplicated live/dead resources.

The renderer can animate foliage wind and wetness each frame while biological state advances only on appropriate events/requests.

## Invariants / quality checks

1. Adult trees maintain stable shape and accumulated damage after arbitrary chunk cycling.
2. An active animal is already resting/browsing before Smalltrotter or the bounded camera sees it; the renderer's visibility does not generate it.
3. No remote island-wide individual wildlife registry. Long-term retained individuals are eligible **only after actual instantiation**, for bounded social, dependent and notable reasons.
4. Retiring and reinstantiating cohorts preserves demographic accounting (abstract + active reservations + retained), resource debits and age-class transitions; statistical expectations may be approximate, but bookkeeping must not fabricate animals.
5. HeroView may observe unseen predators; **HeroSim does not learn of them** until Smalltrotter's own senses detect them.
6. From a front-facing orbit camera, W moves Smalltrotter toward camera; moving sideways across the view leads to camera translation, not forced heading recenter.
7. A locally detached camera can inspect a nearby hill but is physically bounded from remote-island flight.
8. Ordinary thirst/hunger do not hijack direct steering or an active destination. Strong fear/pain can interrupt, especially during autonomous travel.
9. A comfortable, recently fed large predator may simply watch a juvenile sauropod and return to resting.
10. A flood affects movement/plant conditions/rendering consistently, then recedes with familiar terrain intact.
11. Changes to time scale keep developmental/physiological accounting consistent across HeroSim and FaunaSim.
12. Test modules headlessly with fixed seeds, region cycling and interaction logs, including rain/drought ordering, bounded reconciliation cost, stable tree segment IDs, equivalent player/NPC developmental curves, social follower strait travel and multi-life individual persistence.

## Related specifications

[HeroView](hero-view.md) · [Spatial activation](spatial-activation.md) · [HeroSim](hero-sim.md) · [FaunaSim](fauna-sim.md) · [FloraSim](flora-sim.md) · [StalthosSim](stalthos-sim.md) · [Gameplay](gameplay.md)
