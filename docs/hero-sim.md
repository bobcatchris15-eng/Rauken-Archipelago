# HeroSim — the player's animal

**Domain:** High-fidelity player-animal physiology, intention, sensory feedback and lifecycle. **Status:** Conceptual plan.

## Authority

HeroSim owns the player animal's immediate biological state and player-facing behavior. Its biological rules come from **BeastCore**, the same shared physiology/perception/anatomy library used by FaunaSim. It does not own weather, flora resources, or a separate world clock.

## Body-relative direct control and destination goals

**HeroView** maps keyboard/controller/camera inputs to intentions; **HeroSim** makes Smalltrotter enact them in accordance with her body and BeastCore. W always requests forward relative to **her heading**, never camera-forward. A/D request anatomically plausible turning; the camera may orbit independently and follow position without rotating behind her.

A player can instead fly HeroView's **locally detached, hard-tethered** camera around nearby terrain and pick a destination. That yields a persistent `TravelTo` goal: HeroSim navigates, assesses terrain and local stimuli, and may pause/replan/resume or fail if unreachable. It does **not** inherit knowledge of unseen animals from camera flight. Direct movement normally cancels the destination. No command leaves room for ordinary browsing/resting/curiosity.

**Control authority is mode-sensitive:** routine hunger/thirst should almost never take over direct WASD or erase a destination. Pain/startle/fear can briefly override direct motion only when significant; destination mode yields more to pauses, avoidance or withdrawal. Temperature/fatigue usually adjust physical performance rather than replace voluntary aims. See [HeroView](hero-view.md).

## Player intention versus involuntary physiology

Player expresses travel, gaze/attention, inspection, resting and deliberate interaction. The animal performs routine actions autonomously when allowed by physiology, perception, safety, reach and the player's current intent.

Examples: approachable edible plant while hungry → orient/lower neck and browse; accessible freshwater while thirsty → drink; relaxed idle → grooming/weight adjustment. Interrupt when the player walks away, an obstacle blocks reach, or a sensory event demands immediate attention. Avoid hijacking the controls with unrequested long auto-navigation.

## BeastCore — shared internal model

BeastCore is a **library of reusable animal biology and sensory mechanisms**, not a fifth autonomous organism simulator:
- Metabolism, energy reserves, gut fill, delayed digestion, water intake and loss.
- Body temperature/thermal discomfort, exertion, activity fatigue.
- Injury, acute nociception/startle and slower persistent pain/healing.
- Growth and anatomical proportions from species life-history curves, nourishment and developmental state.
- Sensory capability models (sight, hearing, smell, body contact), limited perception and habituation.
- Drives (hunger, thirst, rest, shelter, alertness) derived separately from objective internal quantities.

HeroSim and FaunaSim must use the same underlying formulas and species definitions, but HeroSim evaluates urgent values more frequently and provides richer presentation output. BeastCore should be headlessly testable against reference environmental traces.

## Timing and fluid progression

- Inputs, collisions, balance and acute reactions retain realtime responsiveness.
- Thermoregulation, ongoing pain and arousal use relatively frequent scheduled integration.
- Digestion, hydration, injury healing and fatigue use slower physiological stepping; events such as a drink or injury still affect state immediately.
- Growth is **nonlinear and condition dependent**. Young juveniles should noticeably grow during an approachable play session, not require hours for the first visible changes.
- SimCore owns world-time acceleration and time-skipping. Species developmental pacing may be compressed, but must remain consistent for wild juveniles and the player's animal; do not give HeroSim secret biological rules or multiply immediate reflex rate.
- Rest/sleep may accelerate world time while updating hazards and offscreen ecology, with bounded interrupt checks.

A key tuning question remains: how much growth compression comes from global clock acceleration versus a shared species developmental curve? Record options with test results rather than selecting durations prematurely.

## Environment and interaction contracts

- RaukenSim: sample current local conditions relevant to heat, rain, wind, water safety, shelter and flooding.
- FloraSim: query reachable resources, finite plant biomass and ecological quality through validated feeding events.
- FaunaSim: shared encounters, sensing, signals and physical contact; not privileged to reveal all unseen animals.
- InteractionsCore: commit cross-domain transfers, injury effects and resource transitions.
- RaukenState: preserve this animal's identity and lifecycle so saves/reloads and deaths remain coherent.
- HeroView/renderer/physics: HeroView owns human input focus and bounded camera, receives HeroSim bodily/sensory presentation; streamer supplies renderable world separately; none owns animal biology.

## Visual/body development

Juvenile dwarf titanosaur: prominent irregular nape/upper-back bristles, small osteoderm bumps and pebbled skin. As it ages, different body regions change proportions, scale patterns, skin folds, osteoderms and residual bristle density. Growth alters eye/camera height, foot contact, feeding reach and access through crevices.

## Behavioral quality tests

Two animals of same species and circumstances grow similarly even if one is player-controlled; player can interrupt feeding; pain instantly affects posture while healing remains slow; animal does not seek unperceived water through a ridge; head/neck browsing reaches actual available leaves; time acceleration doesn't turn reflexes into slow motion or deplete animals impossibly fast.

Related [HeroView](hero-view.md), [Spatial activation](spatial-activation.md), [Gameplay](gameplay.md), [Creatures](creatures.md), [Simulation architecture](simulation-architecture.md).
