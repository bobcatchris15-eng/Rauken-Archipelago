# HeroSim — the player's animal

**Domain:** High-fidelity observable player-animal behavior, lightweight condition cues, intention, sensory feedback and lifecycle. **Status:** Conceptual plan.

## Authority

HeroSim owns the player animal's immediate simplified condition state and player-facing behavior. Its biological rules come from **BeastCore**, the same shared physiology/perception/anatomy library used by FaunaSim. It does not own weather, flora resources, or a separate world clock.

## Hero Beast authority, autonomy and contextual intentions

HeroSim is **species-neutral**: Smalltrotter is the visual flagship, not a universal four-legged locomotor or control assumption. The chosen species provides anatomy, senses, mobility, developmental stage, food/social affordances and parental strategy through BeastCore.

**Voluntary authority from strongest to least:**
1. **Direct body-relative steering.** W requests the animal's own forward, regardless of camera; turning/backing, acceleration and sprinting obey its anatomy. Direct steering takes priority over and normally cancels autonomous destinations.
2. **Player-invoked contextual intentions** (e.g. inspect a specific object, greet a companion, interpose, threaten, stalk, select a nesting site) and persistent destination goals. HeroSim executes a plausible attempt with actual geometry, sensory evidence, contact, hazards and changing animal state; outcomes are never guaranteed.
3. **Uncommanded full autonomy.** Without controlling input or outstanding player-directed goals, the animal may actually travel, forage, court, breed, care for young, rest, socialize, flee or die. This is ordinary local animal life, **not an intrinsic drive to explore distant country**: a comfortable, adequately supplied animal has little reason to leave its current habitat. There is no artificial idle-radius leash, and genuine ecological pressures can shift its range. Direct steering can immediately interrupt voluntary autonomous actions.

**Autonomy remains active during direct steering.** Compatible browsing, chewing, attention, postural correction, scent investigation and vocal/social responses proceed without prompts. Normal hunger, thirst or curiosity do not wrest control of the feet from the player. Genuine severe pain, loss of balance or immediate danger can cause short involuntary reflexes; never turn these into prolonged cutscenes.

HeroView alone owns the **strictly player-invoked** slow-time contextual response chooser. It offers a small set of perceived/species-appropriate intentions only when called; it never appears just because a shrub or animal is in range. SimCore coordinates world-consistent time dilation while choosing.

**TravelTo** remains a persistent player destination chosen through the bounded detached camera if desired. HeroSim routes using the Hero Beast's actual perceptual limitations, not hidden hazards or predators exposed to the player's camera. It may pause/replan/abandon under real constraints; routine physiological needs do not erase the goal.

## One voluntary intention pipeline — not camera-operated AI

HeroSim owns **one** voluntary intention/execution system. An intention may arise from the animal's needs, perception, social situation and ordinary autonomous behavior, or be **suggested by the human via HeroView** (e.g. go to a ground point, inspect, greet, defend or investigate). Once accepted, it becomes **the Hero Beast's current intention**: there is no second movement AI, scripted puppet behavior or conspicuous change of gait/attention because the player originated the suggestion.

Retain minimal **provenance and authority metadata** (source, priority, optionally cancellation/status) to preserve player agency. A player-suggested goal ordinarily persists through hunger, thirst, curiosity and minor interruptions; strong pain/fear, blocked passage and genuine limitations can pause, replan or abandon it. When the goal finishes/fails or the player cancels it, the animal resumes full autonomous goal selection. Direct body-relative steering remains strongest voluntary input and normally cancels outstanding selected destinations. A *detached camera* alone is not a command and never pauses the Hero Beast's life.

**Information boundary:** the player may inject a desired location the animal has never seen (the Malkovich premise), but **not** a mental map of optimal terrain, an unseen predator position, or an audio/visual observation available only to the detached camera. The animal discovers hazards and responds through its own senses and physics during execution.

## Short-lived working memory and home-range behavior

**Decision: cap ordinary animal memory to bounded, short-term working state.** HeroSim does **not** accumulate a learned geographical map, a lifelong catalog of places or routes, a generalized experience/skill history, or a persistent homing target. Do not add a general learning system to make autonomy work.

- **Immediate observations:** currently reachable food, an obstacle being negotiated, a nearby call, visible threat or social cue can inform the present action.
- **Recent context:** a temporarily occluded predator, a recently visited drinkable pool or the course interrupted by a startle can remain relevant briefly; remembered observations decay/expire instead of persisting indefinitely. A threat must not vanish from the animal's mind the instant it leaves sight.
- **Bounded implementation:** a small, capped collection of observation/action records with timestamps or short expiry is sufficient. Details, capacity and duration are implementation-tuning parameters. Recent-event habituation (such as Brackenback settling after repeated harmless rustling) also fades; it is not permanent conditioning.
- **Not general memory:** physiological condition, current intentional action, pregnancy/dependence and explicitly retained social attachments are distinct state, not license to store an expanding autobiographical or spatial history. Reedcrest peer bonds and Longstride dependent-young/caregiver ties may persist through the established bounded FaunaSim/StalthosState identity rules; they do **not** imply lifelong place memory.

**Home range is ecological, not a memorized territory.** An uncommanded animal usually remains around usable local food, water, shelter, compatible company and species-appropriate activity. It may range across a valley or farther when those circumstances warrant, without a magic invisible fence, but should not generate long expeditions just to find new scenery. Species differ in normal ranging scale; Longstride can roam more widely than Smalltrotter without learning a permanent trail atlas.

**Player travel does not install a return-home obligation.** If the player leads Smalltrotter several valleys away and releases control, she resumes ordinary local life where she is, based on what she can currently sense and briefly remember. She does **not** plan a trip back to her former home range or require simulated geographic relearning. Resource shortage, danger, seasonal change, social needs or displacement can still cause natural movement. The *player's intention* supplies most exceptional exploration; HeroSim provides ordinary animal competence while doing it.

Save/load and activation need only preserve the existing persistent biological, relationship and ecological truths plus whatever minimal current activity continuity is warranted, **not** long-term personal maps. NPCs use the same bounded-attention principle under FaunaSim; dormant cohorts do not learn offscreen routes.

### Dual hearing of shared sound events

FaunaSim, StalthosSim and world ambience provide spatial acoustic events. BeastCore/HeroSim evaluates them from **the Hero Beast's anatomical hearing position and species hearing model** to generate sensory perception, attention or alarm. HeroView/audio independently renders a listener at the **player camera** (especially in detached mode). A sound audible to the player may be completely inaudible to the animal; neither animal response nor HeroView's *animal-sensed alarm recall* is triggered by player-only camera audio.

Only HeroSim can mark a sound as **sensed by the animal**. It may also supply restrained body/physiology presentation cues to HeroView, whose sound mix must preserve distance rather than treating the camera as physically inside the animal when detached. See [HeroView](hero-view.md).

## Direct steering — bounded motor competence and obstruction

**The player commands intended direction/pace, not steps or a route.** Species-specific BeastCore locomotion supplies gait selection, foot placement, balance, braking, wading/swimming transitions and small obstacle avoidance; physical contact determines what movement actually succeeds. HeroSim arbitrates voluntary intent and reflexes. The camera does not become a sense or navigation database for the animal.

While direct body-relative steering is actively held, the locomotion system may **propose local adjustments**, not independently choose a new destination or lengthy detour. HeroView supplies a **screen-space lateral correction allowance**: the central third of the active camera composition is the practical width budget for automatic detouring. Evaluate candidate short-horizon routes against the *projected commanded course*, not as an absolute rule that the body must stay at the middle of the screen. This distinction preserves the already-agreed broadside camera composition in which the player deliberately walks the Hero Beast from left to right. Camera follow must not artificially increase the budget mid-decision.

If a competent local solution would require leaving that narrow on-screen steering corridor, **reject the automatic route**. If no admissible path remains, stop translational movement at the physical obstacle and let the Hero Beast **inspect it**: look, orient head, sniff or probe where anatomically sensible, shift balance and remain responsive. Don't loop pathfinding, slide sideways through collisions, force a major detour or invent a permanent refusal state.

The obstruction persists only while the same direct steering intention continues. **Changing the steering direction** immediately retries locomotion; **releasing direct steering** yields ordinary full HeroSim autonomy, which can investigate, turn away, choose a different route or remain nearby for its own reasons. Compatible head/mouth/social actions may continue throughout. Real pain/balance/startle reflexes may still momentarily affect control.

**Division of labor:** BeastCore produces camera-agnostic feasible local motion candidates; HeroSim applies the current intent and the small screen-space deviation constraint received from HeroView; local physics commits the actual motion. Destination TravelTo is **not** subject to the central-third detour constraint and may select wide, physically valid routes.

**Do not hardcode a world-meter sidestep limit as a substitute for this player-facing rule.** The screen-width criterion is a camera-space steering budget, and the projection/reference-path details need implementation playtesting.

## Concurrent body-region activities and behavioral individuality

Do not serialize all actions into one exclusive activity state. Feet/body can continue under player-directed walking while head/neck/mouth and attention perform reachable low-cost behavior: Smalltrotter plucks shrubs while clumping along; Reedcrest calls to companions; Thistletail opportunistically takes a small morsel; Brackenback scans or snorts at suspicious scenery. Animations respect reach, gait, balance and body-part compatibility. Real feeding/damage transfers pass through InteractionsCore; visual chewing does not conjure calories.

Social and alarm behavior derives from senses, present circumstance and species predisposition rather than a new generalized relationship-history simulator. Brackenback protects small distressed animals of any species (and sometimes defensively postures at innocuous rocks or bushes); Reedcrest maintains strong reciprocal peer attachments; Longstride attends its dependent young asymmetrically. All apply to wild animals as well as the player.

## BeastCore — shared internal model

BeastCore is a **small library of shared species behavior and condition cues**, not a full animal physiology engine:

- Approximate hunger/food condition, hydration comfort, fatigue/rest, stress and short-term alarm.
- Simple injury severity and recovery effects when visible.
- Species-defined age/growth-stage morphology, reproductive readiness and aging.
- Basic sensory and contact capabilities: field of view, hearing/odor cues, physical reach, limited transient memory.
- Drives and preferences sufficient for ordinary local animal life, species-specific social instincts and intended action execution.

These are **display/gameplay values**. Avoid gut chemistry, exact energy budgets, thermal-mass models, full parasite/disease ecology and metabolic conservation unless an inexpensive proxy demonstrably fails. HeroSim and FaunaSim share compatible rules while updating at different rates. Headless tests should validate behavior/continuity, not scientific accuracy.
## Timing and fluid progression

- Input, collisions, locomotion, visible feeding and acute alarm/injury remain immediately responsive.
- A few needs, current behavioral activity and simple condition/recovery advance at affordable slower or event-driven rates.
- Reproduction, growth stage and offscreen condition advance from elapsed **SimCore world time** and species-defined curves.
- Rest/nesting can advance the shared clock faster, with bounded checks for meaningful danger and persistent changes.
- Player and active NPC conspecifics have comparable **visible** stage progression. Remote cohorts use coarse stage/abundance updates.

No independent physiology clock or per-organ scheduler. Set lifespan/development rates to create satisfying experiences, not to reconstruct real dinosaur metabolism.
## Time semantics shared with FaunaSim

SimCore owns **one world/calendar clock**. Realtime input and physical contact remain responsive during accelerated world time. BeastCore uses coarse elapsed-time changes for condition and age plus immediate event effects for eating, injury and movement; this is not a continuous mass-balance integrator.

The same species parameters yield **roughly comparable visible** growth, stamina and aging for HeroSim and active FaunaSim. Distant fauna may age statistically. Avoid charging the same movement/action twice during accelerated time, but do **not** require exact metabolic or heat balance between player and NPCs. Rest/time skips sample significant hazards and surviving relationships at bounded intervals. Tuning follows what is observable and enjoyable.
## Environment and interaction contracts

- StalthosSim: sample current local conditions relevant to heat, rain, wind, water safety, shelter and flooding.
- FloraSim: query reachable resources, finite plant biomass and ecological quality through validated feeding events.
- FaunaSim: shared encounters, sensing, signals and physical contact; not privileged to reveal all unseen animals.
- InteractionsCore: commit cross-domain transfers, injury effects and resource transitions.
- StalthosState: preserve this animal's identity and lifecycle so saves/reloads and deaths remain coherent.
- HeroView/renderer/physics: HeroView owns human input focus and bounded camera, receives HeroSim bodily/sensory presentation; streamer supplies renderable world separately; none owns animal biology.

## Hatching, breeding and death continuity

A new Hero Beast hatches as a generic wild individual reserved from the chosen species' existing local population. Species-specific hatchling movement, adult attendance, early care, nesting location and maturation are real HeroSim/BeastCore behaviors, not scripted tutorial exceptions. An adult may court, mate, tend a nest, hatch young, and interact with them as the species warrants. The targeted nesting/hatching episode occupies about thirty minutes or less of focused player time via shared SimCore acceleration; dependent offspring (particularly Longstride) can persist and grow for much longer in ordinary play. No genetics or breeding-stat progression.

Hero Beast death is an ordinary biological death and persists as an ecological outcome. A next playable hatchling begins in the same world, with no inherited special lineage or player knowledge. Previously instantiated companions, dependent young and other eligible individuals retain only justified compact identities under FaunaSim/StalthosState; when inactive they advance coarsely and may later die or decay back into regional cohorts. No death-triggered world reset.

## Visual/body development

Juvenile dwarf titanosaur: prominent irregular nape/upper-back bristles, small osteoderm bumps and pebbled skin. As it ages, different body regions change proportions, scale patterns, skin folds, osteoderms and residual bristle density. Growth alters eye/camera height, foot contact, feeding reach and access through crevices.

## Behavioral quality tests

Two animals of same species and circumstances grow similarly even if one is player-controlled; a wild parent and player parent display compatible species care; uncommanded HeroSim sustains natural life rather than idle animation; simultaneous walking and browsing works without menu prompts; player can interrupt feeding; pain instantly affects posture while healing remains slow; animal does not seek unperceived water through a ridge; head/neck browsing reaches actual available leaves; time acceleration doesn't turn reflexes into slow motion or deplete animals impossibly fast.

Related [HeroView](hero-view.md), [Spatial activation](spatial-activation.md), [Gameplay](gameplay.md), [Creatures](creatures.md), [Simulation architecture](simulation-architecture.md).
