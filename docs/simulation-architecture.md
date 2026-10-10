# Simulation architecture — state, activation, perception and presentation

**Status:** Agreed logical boundaries; algorithms, distances and implementation framework remain provisional. These are **modules**, not independent network services.

## Named components

| Component | Owns | Does not own |
|---|---|---|
| **SimCore** | Shared timeline, variable time scale, scheduling, ordering, spatial **simulation chunk activation** | Weather, animal biology, camera |
| **RaukenState** | Persisted world/region/plant records, regional fauna cohorts, rare retained large adults, saves and event history | A complete persistent biography for every animal; simulation itself |
| **RaukenSim** | Weather, day/night, seasons, local wetness, temporary storm/flood conditions and environment history | Runtime erosion/geology, organisms |
| **FloraSim** | All relevant botanical/fungal individuals and patches; growth, health, resources, death, lazy catch-up | Per-frame renderer polling |
| **FaunaSim** | Local active wildlife drawn from population cohorts, behavior, physiology at suitable fidelity; *optional retention of already-instantiated mature giants* | Individual identities for never-instantiated wildlife, lifelong memories for ordinary animals |
| **HeroSim** | Smalltrotter's bodily biology, sensory interpretation, player-intent execution, involuntary responses | Camera knowledge or camera movement |
| **BeastCore** | Shared animal physiology, sensation, growth and behavior primitives used by HeroSim and FaunaSim | Its own ticking population |
| **InteractionsCore** | Validated cross-domain resource/damage/state transfers and outcome events | A master AI decision layer |
| **HeroView** | Player controls/focus, body-relative direct steering requests, destination picking, bounded camera, human-facing audiovisual embodiment | Biological truth, unrestricted spectator flight, injecting camera sight into HeroSim |
| **Renderer/physics/audio** | Scene rendering, local physical contact/animation and audio implementation | Persistence/biological authority, weather decisions |

**Ownership invariant:** one domain owns each mutable ecological fact. RaukenState stores agreed persistent representations without becoming a per-frame database bottleneck; InteractionsCore coordinates only significant cross-domain operations. Direct local reads and high-rate interactions should remain inexpensive.

## Conceptual data flow

```text
  Human  ->  HeroView (input focus, camera, destination picking)
                      | player intention
                      v
                   HeroSim <---- BeastCore shared with FaunaSim
                body + perception
                 ^     ^      ^
          RaukenSim FloraSim FaunaSim <--- SimCore simulation activation
              \        |      /
                   InteractionsCore
                         |
                    RaukenState

  World snapshots: RaukenState + domain sims -> scene streamer -> renderer
  Subjective/body signals: HeroSim ---------------------------> HeroView
  Visual/audio scene + body presentation ---------------------> human
```

This is **not** a fixed synchronous API chain. HeroSim senses a world through Smalltrotter's own body, not through the camera. The renderer ingests world renderables from the streamer/domain snapshots without routing whole scene graphs through HeroSim.

## Spatial lifecycle: three independent extents

1. **Active simulation:** SimCore prewarms and activates chunks around Smalltrotter, including a buffer beyond the **entire reachable envelope** of HeroView's nearby detached camera. FaunaSim begins local behaviors before the ridge is rendered; FloraSim bulk reconstructs the right plants/patches.
2. **Hero perception:** BeastCore/HeroSim evaluate what Smalltrotter could perceive from her body (eyes/ears/smell/contact, occlusion, attention); no omniscient camera data.
3. **Rendered scene:** HeroView's camera frustum and LOD choose what's drawn, including distant static scenery. The camera can show something she does not notice.

**A simulation chunk is not the same as a render chunk.** A renderer chunk unloading cannot kill a local animal. Camera flight over a nearby hill shouldn't cause a new herd to spring into existence only because it is now visible. Camera tether and simulation-buffer distances are open tuning parameters; avoid whole-island active simulation when the hero is far away.

[Spatial activation](spatial-activation.md) describes the activation/retirement lifecycle.

## What becomes instantiated

**Flora:** On simulation activation, FloraSim resolves plant individuals and colonies from static suitability, deterministic seeds and persisted events, lazily advancing growth to current world time. Trees retain recognizable age, shape and damage across reloads. Low ground cover can be population patches with fully rendered blades but not separate biology objects.

**Fauna:** Before local activation, regions have habitat-based **population/age cohorts**, not individually simulated or named animals. On activation FaunaSim reserves cohort counts and instantiates appropriate local animals (including ones outside camera view); these live, rest, browse, observe and react. On retirement most return to aggregate populations. Only *previously instantiated* mature members of designated largest species **may** retain a compact persistent identity. No Dolores individual exists on Rainridge merely because a constrictor population exists there.

Individual retention and simulation fidelity are different axes: an active small transient creature can have responsive behavior; a retained large adult can sleep as a tiny saved record. Cohort accounting prevents duplicate animals on reactivation. A short locality disturbance/cooldown may discourage conspicuous instant replacement without keeping per-animal biographies.

## HeroView: camera and authority

**Camera placement and movement authority are separate axes.**

- **Tethered orbit/follow:** orientation stays chosen, not compulsorily behind Smalltrotter. She can walk across the camera frame; only when compositional space is exhausted does the camera smoothly pan/translate to follow.
- **Locally detached observation:** free local pan/orbit/flight within a **soft then hard tether around Smalltrotter**. Up over a nearby hill: yes. Across to another island: no. When she moves away, the allowed envelope follows smoothly; no teleport or abrupt forced rotation.
- **Direct body-relative steering:** W is forward **from Smalltrotter's facing**, independent of camera orientation. A/D request anatomical turning; S asks for braking/backing as physically possible.
- **Destination intent:** in camera-focused mode, pick nearby ground; HeroView sends a target to HeroSim. The animal finds her own route with local sensing and physical limits, not magical information about predators or paths observed only by the camera.
- **No movement command:** Smalltrotter can browse, rest, investigate, watch or drink naturally.

**Player authority:** while holding WASD, routine hunger/thirst/curiosity do not redirect her. Severe pain/startle/imminent danger may cause brief involuntary behavior; forceful control loss is rare. A destination is a **persistent goal** not deleted by routine needs, but permits more hesitation/replanning/avoidance and can be abandoned under strong fear, injury or inability to traverse. Direct steering normally cancels an outstanding destination.

[HeroView](hero-view.md) contains the control/camera detail and acceptance cases.

## Resolution is not a single distance-based level

Apply three **independent design considerations** to each domain process:
- **Causal retention:** which effects must remain true, even when no individual is instantiated? Examples: population/cohort totals, forage depletion, an old tree's lost limb, persistent flood damage.
- **Temporal evaluation:** when does that process next have to be reconciled, or how much time may be aggregated? Regional browsing may integrate by week; local collisions must resolve immediately.
- **Representation:** what geometric, behavioral or physical detail is currently needed? A distant herd can be only a cohort ledger; a nearby transient animal can be richly animated.

Proximity influences **deadlines and visual detail**, not whether significant resource accounting exists. Do **not** implement a general-purpose causal-importance predictor or three-axis runtime LOD manager. Define domain-specific invariants and work queues: immediate contact, population/resource settlements, environmental interval integration, chunk prewarm, and graphics creation. Most scheduling can use a small number of priority/deadline classes.

## Four cross-domain contracts before implementation

1. **Counts and resources:** FaunaSim's demographic cohorts, active reservations and retained individuals balance. FaunaSim's aggregate browsing causes finite FloraSim resource debits through InteractionsCore; aggregate input/output need not conserve exact biological energy.
2. **Chronological environment:** RaukenSim provides time-ordered environmental intervals plus discrete damaging events. Averages alone are insufficient. Records may be compacted once all dependent state has safely passed them.
3. **Bounded catch-up:** Every region and durable organism/patch tracks evaluation time and version. SimCore amortizes reconciliation ahead of both Smalltrotter and the full HeroView tether; render work cannot trigger an unbounded biological replay.
4. **Stable structural edits:** Significant tree/shrub segment IDs survive growth and asset regeneration. InteractionsCore commits a precisely addressed finite change; FloraSim stores the resulting structural state, not every historic bite.

These are **contracts across existing modules, not new standalone subsystems**. See [FaunaSim](fauna-sim.md), [RaukenSim](rauken-sim.md), [FloraSim](flora-sim.md) and [Spatial activation](spatial-activation.md).

## Time and update rates

SimCore owns global world-time progression (which may be accelerated through uneventful/rest periods). RaukenSim derives sun, seasons and weather from that timeline. Species-specific developmental pacing can make juvenile growth meaningfully noticeable without forcing animation/reflex speed to match accelerated years; HeroSim and FaunaSim use the same underlying BeastCore developmental laws. **Four meanings of time:** realtime physical controls/contacts; shared SimCore world/calendar time; physiology integrated over world intervals plus actual activity/event costs; and species life-history development derived from world time and condition. Physiology and development aren't independent hidden clocks.

- Direct physical response, collision, pain/startle: prompt real-time/event-driven.
- Local animal orientation and movement: active high-rate as needed.
- Thermal discomfort, attention and continuing pain: medium-rate.
- Hunger, thirst, gut, fatigue, health: slower or event-integrated.
- Growth, reproduction, botanical senescence: coarse/lazy.
- Inactive environment: compact time-window weather summaries retained for FloraSim and cohort catch-up.

Exact frequencies are unknown; don't demand one timer per internal variable.

## Environment and cross-domain changes

The map generator establishes mostly fixed streams, springs, terrain, soil, drainage and plant moisture suitability. RaukenSim handles day/night, weather and temporary storm-driven water level changes with **no routine erosion or detailed groundwater transport**.

FloraSim catches up plant health/age from stable suitability, environmental interval summaries and discrete browsing/storm events. InteractionsCore validates finite transfers (food into stomach, biomass removed; rain/damage effects; carcasses/deadwood), preventing double consumption and duplicated live/dead resources.

The renderer can animate foliage wind and wetness each frame while biological state advances only on appropriate events/requests.

## Invariants / quality checks

1. Adult trees maintain stable shape and accumulated damage after arbitrary chunk cycling.
2. An active animal is already resting/browsing before Smalltrotter or the bounded camera sees it; the renderer's visibility does not generate it.
3. No remote island-wide individual wildlife registry. Long-term retained adults are eligible **only after actual local instantiation**.
4. Retiring and reinstantiating cohorts preserves demographic accounting (abstract + active reservations + retained), resource debits and age-class transitions; statistical expectations may be approximate, but bookkeeping must not fabricate animals.
5. HeroView may observe unseen predators; **HeroSim does not learn of them** until Smalltrotter's own senses detect them.
6. From a front-facing orbit camera, W moves Smalltrotter toward camera; moving sideways across the view leads to camera translation, not forced heading recenter.
7. A locally detached camera can inspect a nearby hill but is physically bounded from remote-island flight.
8. Ordinary thirst/hunger do not hijack direct steering or an active destination. Strong fear/pain can interrupt, especially during autonomous travel.
9. A comfortable, recently fed large predator may simply watch a juvenile sauropod and return to resting.
10. A flood affects movement/plant conditions/rendering consistently, then recedes with familiar terrain intact.
11. Changes to time scale keep developmental/physiological accounting consistent across HeroSim and FaunaSim.
12. Test modules headlessly with fixed seeds, region cycling and interaction logs, including rain/drought ordering, bounded reconciliation cost, stable tree segment IDs and equivalent player/NPC developmental curves.

## Related specifications

[HeroView](hero-view.md) · [Spatial activation](spatial-activation.md) · [HeroSim](hero-sim.md) · [FaunaSim](fauna-sim.md) · [FloraSim](flora-sim.md) · [RaukenSim](rauken-sim.md) · [Gameplay](gameplay.md)
