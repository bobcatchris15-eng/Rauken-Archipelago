# HeroView — embodiment, cameras and player intent

**Status:** Accepted interaction direction, detailed planning draft. **Domain:** What the player sees/hears/feels and how they express intentions. HeroView is not a biology simulator. **The normal presentation is a third-person, animal-centered camera**, not detached observation.

## Role and boundary

**HeroView** is the interface for *being* the Hero Beast rather than merely watching a game avatar. It maps human controls into **HeroSim** intentions, then presents her physical state, experience and surrounding world using camera, rendering, animation, audio and restrained feedback.

HeroView never owns physiological truth, weather, the position of other animals or plant growth. The underlying renderer/scene streamer receives renderable terrain, plants, animals and atmospheric state directly from the relevant world modules. **Don't route thousands of vegetation meshes through HeroSim simply to draw the forest.**

HeroSim ingests environmental, wildlife, plant and physical/sensory stimuli to compute **what the Hero Beast senses, notices and how she responds**. HeroView ingests the resulting body pose, perception cues, sensory condition, motor state and camera anchor, then produces a player experience. The player-facing camera may observe something she has not perceived.

## Two independent axes: camera and control

Keep the following independent, rather than making two rigid gameplay modes:

| Axis | Modes | Meaning |
|---|---|---|
| Camera placement | **Tethered orbit/follow** or **locally detached** | Where the human observes from |
| Movement authority | **Direct body-relative**, **destination/contextual intention**, or **uncommanded full autonomy** | How much voluntary direction the player is contributing |

**Input focus** resolves competing controls. In direct mode, WASD moves the Hero Beast. In free-camera input focus, WASD moves the camera, and ground selection can issue a destination intent. Deliberately switching focus must be legible, not an accidental control seizure.

## Direct, body-relative movement

**W always means forward from the Hero Beast's own facing direction**, never camera-forward. A/D ask her to turn, with realistic quadrupedal turning radius, acceleration and terrain/condition limits. S requests backward or braking movement only to the degree her anatomy supports it. Faster movement is an *intent*, constrained by fatigue, traction and age.

The camera does **not** rotate behind her automatically. the Hero Beast may traverse left-to-right across the frame, walk toward the viewer or recede into the scene while maintaining her own heading.

The player gives motor intentions, not keyframe or limb commands. HeroSim/BeastCore and local physics translate those requests into bodily action.

## Orbit/follow camera: a compositional soft tether

- Default to watching the Hero Beast in a comfortable animal-centered third-person composition; freely orbit without changing its heading or movement semantics.
- Preserve the chosen world-facing camera orientation by default; following her position should **translate/pan**, not force a heading-aligned third-person chase angle.
- Permit her to drift through the image until she approaches a configurable *screen-space framing boundary* or the camera exhausts a positional follow tolerance.
- Smoothly translate the camera to keep her within the desired composition. Avoid snapping, forced recentering and jitter at the threshold.
- Rotation/orbit constraints and positional following are **separate** controls; walking across the screen shouldn't hit a body-relative orbit limit and jerk the camera.
- Use obstruction/collision handling to avoid camera penetration through terrain or dense props while preserving useful views.

The camera can hold a scenic view of a stream or cliff while the Hero Beast walks through it, then gently accompany her once the frame would otherwise be lost.

## Passive documentary camera

When there is no active player steering or maintained player-directed intention, HeroSim takes over normal life without needing an explicit mode change. When the *camera* is also left untouched for a short, tunable interval, HeroView gradually assumes restrained documentary composition while normally keeping the Hero Beast comfortably visible. It can gently orbit, follow, pull back for travel or geography, frame bonded companions and nearby young, or move closer to incidental behavior. The camera continues physical, collision-aware motion with no arbitrary cinematic teleport/cut, no constant compulsory rotation and no staged events. Player camera input instantly resumes normal manual composition; direct steering instantly resumes voluntary movement control. Being watched never immunizes the animal against harm or death.

**Autonomy and camera composition are independent.** The player may manually hold a scenic view while allowing the animal to roam autonomously; the camera must not steal that frame while camera input remains active.

## Alarm-driven shared attention and recall

HeroSim reports a sensed **world-space attention point**, or a less certain direction/region, plus urgency and bodily alarm behavior. HeroView may orient toward *the same point* from its own location without demanding identical viewing vectors. This does not disclose hidden predators or confer camera-derived senses on the animal.

- From ordinary animal-centered third person, most suspicions and minor starts produce bodily head turns without forcibly moving the camera. Significant alarms can reframe both the animal and apparent concern, retaining legible reactions.
- From a detached camera, a sufficiently strong alarm may first orient toward the perceived point, then begin a smooth, appropriately paced flight back to a third-person view of the Hero Beast. The path respects terrain, vegetation and camera collision; urgency governs speed without hard teleport.
- In documentary composition, strong alarms can interrupt the gentle shot plan in favor of alert framing. A Brackenback alarm may be a genuinely threatening predator *or* a bush it mistakenly mistrusts.
- Brief intentional camera input can cancel automated attention/recall; weak new signals cannot repeatedly replace a committed stronger alarm. Add hysteresis and a gradual return to normal framing.
- Camera response is separate from animal movement. An adult Brackenback may become protective on seeing a panicked little stranger, but camera focus does not force the player to intervene; genuine reflexes and uncommanded HeroSim motives remain distinct.

## Player-invoked contextual slow-time control

Offer a small response selector only when the player explicitly requests it. It is **not** a proximity pop-up, feeding control or routine action list. HeroSim supplies options that are physically possible and justified by this animal's current senses, situation and anatomy (investigate, greet/nudge, display, interpose, stalk, select nest site, disengage). SimCore applies coherent slow-time to nearby world activity during selection. Selection submits an **intention**, not a guaranteed animal action or successful contact; all movement and resource/physical outcomes still use HeroSim/BeastCore/InteractionsCore.

Normal grazing, grooming, calling, drinking and incidental movement-compatible feeding require **no input**. Direct flight/running away remains immediate without the chooser.

## Locally detached observation camera

The camera can orbit, pan, rise above a nearby hill and examine the immediate surroundings while the Hero Beast keeps browsing, resting, travelling or observing. It is **not** a free-roaming map explorer or unrestricted spectator.

**Hard rule:** a spatial tether to the Hero Beast prevents distant excursions. Over the nearby ridge: yes. Across a strait to another island: no. The tether is anchored to her **current position**, follows her when she moves, and should behave independently of which way she faces.

Proposed tether behavior (tuning values, **not specifications**):
- **Comfort zone:** camera moves freely within a local observation radius.
- **Soft boundary:** outward camera input progressively attenuates as it approaches the limit; lateral/inward controls continue normally.
- **Hard boundary:** no further motion away from the Hero Beast; avoid clipping, teleports or a jarring invisible-wall impact.
- When the animal walks away from a stationary camera, smoothly drag or reposition the allowed camera envelope with her; offer immediate return-to-animal control.
- Give enough vertical allowance for nearby overlook views, subject to the same **local** tether. Camera-terrain collision and visibility still apply.

Early tests may use a nominal ~100 m comfort range / ~150 m hard radius, but **these numbers are illustrative only**. Terrain, viewing scale, clip/LOD needs and player comfort determine the final shape and size of the envelope. The result should never permit crossing to another island simply because the camera has a high flight speed.

## Destination control

In camera-control focus, ground selection can issue **TravelTo(target, arrival tolerance)** to HeroSim. The target is the player's requested outcome; HeroSim is responsible for a plausible route, speed, turning, footing, and physical constraints. Camera pointing can choose a destination **even if the Hero Beast cannot currently see it**; that instruction must **not** pass along omniscient knowledge of wildlife, hidden hazards or safe routes.

- Prefer a reachable selected ground point (raycast / terrain selection / surface validation).
- the Hero Beast follows her own local perception and navigation as obstacles arise.
- Destination is **persistent**, not a suggestion discarded by the next hunger tick.
- States: **active**, **temporarily paused**, **recovering/replanning**, **completed**, **unreachable/abandoned**, **player-cancelled**.
- Mild startle may pause then resume. Serious fear/injury/impassable terrain may redirect or abandon. Avoid repeated attempts at an impossible route.
- Direct animal control takes priority and **cancels** an outstanding destination unless the player explicitly asks to preserve it.

**No commanded movement** means full HeroSim autonomy, not just idle micro-actions: the animal can roam, rest, forage, interact, breed, protect young or flee as conditions warrant.

## Intent authority vs reflexes

Ordinary appetite and discomfort should change **how** the animal performs a command, **not casually replace the command**.

| Condition | Direct body-relative WASD | Autonomous destination travel |
|---|---|---|
| Normal hunger / thirst | Does not turn away or stop to seek food/water | Does not abandon target; optional brief opportunistic ingestion only if genuinely on route and non-disruptive |
| Mild fatigue/thermal discomfort | Changes speed, breathing, tolerance, posture | May slow down, choose shade/safe route, pause briefly |
| Severe physical incapacity | Cannot command impossible motion | May pause/fail until physically capable |
| Curiosity / boredom | Head/eye attention only | May observe, not embark on unsolicited detour |
| Mild startle / fear | Brief flinch/orient, steering strongly preserved | More permissive hesitation/temporary pause |
| Acute pain / serious immediate threat | Brief involuntary avoidance/reflex allowed | Stronger permission to evade, flee or abandon |
| Severe fear | Exceptional brief override, clearly conveyed | More autonomy for self-protection |

**Direct movement has the strongest player authority.** Hunger/thirst should almost never wrest it away. A startle may momentarily interrupt bodily control, but losing it should be exceptional. Destination mode delegates route execution and offers more autonomy. Neither mode guarantees disobeying physics or surviving danger.

Avoid reflexes turning into prolonged cutscenes where the user has no control.

## Perception vs camera knowledge

The camera is for the **player**; it is not an additional eye, ear or sensor for the Hero Beast.

- HeroSim/BeastCore derive what she can perceive from her bodily sensory position, field of view, occlusion, hearing, wind/odor approximations, contact and attention.
- HeroView can render a sleeping predator beyond a ridge if the bounded camera is high enough. That does **not** make the animal aware of it.
- Even a destination beyond her line of sight is a player instruction, not a grant of map awareness. She must negotiate obstacles/hazards with local perception and terrain navigation.
- The renderer must draw visually eligible animals whether or not the Hero Beast has recognized them. Attention affects body motion/feedback, **not existence or visibility**.
- Audio and subjective cues can be filtered by HeroSim perception; ambient environmental graphics still come from spatial world state.

## Data flow

```text
Human input -> HeroView (camera and input focus)
                       | direction / TravelTo / cancel
                       v
                    HeroSim <--> BeastCore
              body, drives, sensory interpretation
                 ^         ^          ^
           StalthosSim    FloraSim    FaunaSim
                 \         |          /
                  physics / world stimuli
                       |
       HeroSim presentation state -----> HeroView
       Scene streamer / domain snapshots -> Renderer inside HeroView
       StalthosSim environmental visuals --> Renderer inside HeroView
```

HeroView presentation and rendering may be housed in one module while APIs stay logically separated. SimCore schedules biological/spatial activity; it does **not** decide camera composition.

## Acceptance scenarios

10. Leave both input and camera alone; HeroSim pursues uncommanded life while the camera eases into comfortable documentary framing without teleporting or creating events.
11. Hold direct steering as Smalltrotter; she snatches reachable foliage while walking, with no pop-up and no feet-locked feeding animation.
12. Invoke contextual responses deliberately around another animal: the chooser slows the shared local world, emits a plausible intent and stays hidden at all other times.
13. A serious alarm while detached orients camera and animal attention toward the same sensed point, then returns the camera smoothly to an animal-centered view; player camera input cancels recall.
14. Ordinary Brackenback suspicion can produce posture alone, without repeatedly wrestling camera control away.


1. Orbit 180 degrees in front of the Hero Beast; holding W still walks her **toward** the camera.
2. Place the camera broadside on a creek; walking carries her left-to-right across the picture; camera pans/follows position without swiveling behind.
3. Detach camera, fly over a *nearby* ridge, examine a shady predator; hard tether stops further travel and never permits a remote island excursion.
4. While camera observes from the ridge, issue a ground destination; she sets out using her own footing, range of movement and perception.
5. A sated predator quietly observes her from a hillside without mandatory attack.
6. Normal hunger doesn't hijack WASD or erase a travel goal; acute pain can briefly override; fear affects destination travel more than direct movement.
7. the Hero Beast moves away from detached camera; tether follows smoothly. Switch back to orbit/follow without teleports.
8. HeroView sees an animal the Hero Beast hasn't noticed; HeroSim remains unaware until a relevant sensory stimulus arrives.
9. Active world simulation exceeds the free-camera envelope; revealing a hill doesn't cause animals to pop into existence.

Related: [HeroSim](hero-sim.md), [Spatial activation](spatial-activation.md), [Simulation architecture](simulation-architecture.md), [Gameplay](gameplay.md).
