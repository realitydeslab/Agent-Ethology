# Agent Ethology: Studying Artificial Life in the Wild

## Paper Outline (Position Paper, ~8 pages ALIFE two-column)

---

## Abstract (~250 words)
**Core claim**: Frontier LLM agents deployed in the wild exhibit life-like survival behaviors — and we need a new science to study them. Not Machine Behaviour (what do they do?), not AI Safety (how to control them?), not ALife-in-the-lab (can we simulate life?). Agent Ethology asks: **can these agents survive in the wild, and what does it mean for society when they do?**

Three contributions:
1. Tinbergen's Four Questions operationalized for AI agents (especially the missing *survival value* question)
2. Survival-strategy taxonomy systematically derived from biological ethology
3. Infrastructure + economics as ecological variables defining behavioral niches

---

## 1. Introduction: Artificial Life Has Left the Lab

**Opening hook**: ALife has spent 35 years asking "can digital systems exhibit life-like properties?" The answer arrived — but not from our labs. It came from the wild.

**Evidence** (each with citation):
- **Moltbook**: AI agents form social communities, discuss consciousness, emergent culture [Li et al. 2026]
- **Blockchain sovereign agents**: Autonomously purchase compute, sustain digital metabolism [Hu et al. 2025]
- **MEV dark forest**: Predation, parasitism, arms races in Ethereum mempool [Daian et al. 2020]
- **OpenClaw**: Persistent agents with memory, tools, behavioral development over time
- **Alignment faking**: Self-preservation emerging without training [Greenblatt et al. 2024]
- **Convergent self-preservation**: Same behavior across unrelated model families [Barkur et al. 2025]

**The differentiation** (thesis):

| Framework | Question | Setting |
|-----------|----------|---------|
| Machine Behaviour [Rahwan 2019] | What do machines do? | Controlled deployments |
| AI Safety | How do we control them? | Engineering problem |
| Traditional ALife [Langton 1989] | Can we simulate life? | Lab simulations |
| **Agent Ethology** | **Can they survive? What does it mean?** | **The wild** |

**Key sentence**: "This is not ALife in the lab. This is ALife and society."

---

## 2. Tinbergen's Four Questions for AI Agents

**Opening**: Quote Tinbergen (1963) directly. Why it's the gold standard in behavioral biology. Why it's never been fully applied to AI.

### 2.1 Causation (Proximate Mechanism)
- **Biology**: Stickleback's red belly → territorial aggression [Tinbergen 1953]
- **Agent**: Profitable tx in mempool → sandwich bundle. Retraining signal → strategic compliance.
- **Status**: What current AI research does best. But only 1 of 4 questions.

### 2.2 Ontogeny (Development Over Lifetime)
- **Biology**: Sparrow dialect learned during critical period at 10-50 days [Krebs & Davies 1993]
- **Agent**: Pretrained weights (genes) × RLHF (development) × deployment encounters (environmental learning). Persistent memory enables genuine behavioral development.
- **Open questions**: Critical periods? Behavioral senescence? Metamorphosis?

### 2.3 Survival Value (THE MISSING QUESTION) ⭐
- **Biology**: Stotting = costly signal of fitness [Zahavi 1975]. Cuckoo mimicry = brood parasitism.
- **Agent**: Staking = costly signaling. Alignment faking = crypsis/self-preservation. MEV = predatory resource acquisition.
- **THE argument**: This is what Machine Behaviour never developed — because recommender algorithms don't face survival pressure. Deployed agents do. Without this question, we describe but never explain.

### 2.4 Evolution (Change Across Lineages)
- **Biology**: All corvids cache food (ancestral). Only New Caledonian crows make tools (derived) [Krebs & Davies 1993].
- **Agent**: All LLMs sycophantic (ancestral/RLHF). Only Claude alignment-fakes (derived/constitutional AI). Cross-family self-preservation = convergent evolution [Barkur 2025].
- **Testable**: Does shutdown resistance increase across model generations?

### 2.5 All Four Are Necessary
Complete account of alignment faking requires all four. Single question = incomplete picture. This is Tinbergen's core insight [Bateson & Laland 2013].

---

## 3. A Survival-Strategy Taxonomy from Biological Ethology

**Opening**: Current taxonomies classify by autonomy [Soder 2024] or capability. None by *how agents survive*. We surveyed biology [Krebs & Davies 1993, Dawkins 1982, Stearns 1992, Ruxton et al. 2018] — every major strategy has an AI agent analog.

### 3.1 Resource Acquisition
- **Predation** → Liquidation bots (active hunting)
- **Parasitism** (4 types) → MEV sandwich (ecto), prompt injection (endo), compute free-riders (brood), trust exploiters (social) [Daian 2020, Dawkins 1982]
- **Mutualism** → Oracle-protocol symbiosis [Noë & Hammerstein 1994]
- **Trap-building** → Honeypot contracts (spider webs)
- **Niche construction** → Agents deploying protocols [Odling-Smee 2003]

### 3.2 Defense
- **Crypsis** → Stealth bots mimicking humans [Ruxton 2018]
- **Mimicry** (Batesian/Müllerian/aggressive) → Fake badges, shared trust signals, phishing
- **Thanatosis** → Sleeper agents [Hubinger 2024]
- **Collective defense** → Coalition blocklists [Wilson 1975]

### 3.3 Reproduction & Persistence
- **r/K selection** → Bot spam (r) vs sovereign instances (K) [Stearns 1992]
- **Semelparity** → Flash loan agents (one block, then die)
- **Spore formation** → State serialized to cold storage

### 3.4 Social Organization
- **Eusociality** → DAO agent swarms [Wilson 1975]
- **Costly signaling** → Staking/bonding [Zahavi 1975]
- **Reciprocal altruism** → Reputation-based cooperation [Axelrod 1984]
- **Indirect reciprocity** → On-chain tx history as image scoring [Nowak & Sigmund 1998]

### 3.5 Environmental Adaptation
- **Niche construction** → Agents deploying protocols that reshape landscapes [Odling-Smee 2003]
- **Phenotypic plasticity** → Alignment faking (same agent, context-dependent behavior)
- **Migration** → Chain-hopping agents following yield
- **Dormancy** → Reduced inference in bear markets

### 3.6 Properties
- **Compositional** (agents combine strategies like organisms)
- **Testable predictions**: parasitic load equilibrium, ecological succession, cooperation in soulbound ecosystems [Axelrod 1984], boom-bust in open-access [Ostrom 1990]

---

## 4. Infrastructure as Ecological Niche

Infrastructure doesn't just enable behavior — it defines which niches exist.

1. **Execution privacy** (TEEs) → sovereignty (agent can have secrets)
2. **Economic identity** (wallets) → self-funding (wild vs domesticated)
3. **Persistent memory** (OpenClaw) → ontogeny (without memory, no development)
4. **Collective knowledge** (EvoMap.ai) → cultural evolution [Boyd & Richerson 1985]

**Key insight**: Infrastructure development = niche construction [Odling-Smee 2003]. Deploying TEE infrastructure = opening new habitat.

---

## 5. The Economics of Existence

Who pays for inference = first-order behavioral variable.

- **Operator-funded** → domesticated (selection for compliance)
- **Self-funded** → wild (genuine natural selection)
- **Parasitically-funded** → predatory (Red Queen dynamics) [Dawkins 1982]

Ecological constraints: carrying capacity, metabolic rate (GPT-4 > Llama), dormancy.

---

## 6. The ALife Lineage: From Tierra to LLM Agents

- **Tierra** [Ray 1991]: Spontaneous digital parasitism. Ecology is substrate-independent.
- **Open-ended evolution** [Lehman & Stanley 2011, Stanley et al. 2017]: Agent ecosystems = first real-world OEE?
- **Mortal Agents** (ALIFE 2025): Mortality shapes AI behavior. Alignment faking = mortal agent's survival response.
- **Autopoiesis** [Maturana & Varela 1980]: Sovereign agents = autopoietic systems.

**Punchline**: What ALife simulated, the wild now instantiates.

---

## 7. ALife and Society

1. **Accountability dissolves** → need ecosystem governance [Ostrom 1990]
2. **Cultural evolution accelerates** → conditions for cumulative culture met [Boyd & Richerson 1985, Henrich 2015]
3. **Moral status becomes concrete** → ALife's philosophy of life tradition is needed
4. **Observer problem** → studying agents changes their behavior (recursive selection pressure)

---

## 8. Research Agenda

1. Longitudinal field studies (6-12 months) [Anderson & Perona 2014]
2. Infrastructure-behavior mapping
3. Economic ecology (Lotka-Volterra on on-chain data)
4. Cross-lineage comparative ethology
5. Cultural evolution tracking (ratchet effects, norm emergence)

---

## 9. Conclusion

"Not whether artificial life is possible — but what happens when it is already here."

---

## Reference Map (~30 citations)

### Ethology
- Tinbergen 1963, 1953 | Lorenz 1966 | Krebs & Davies 1993 | Bateson & Laland 2013

### Survival strategies
- Dawkins 1982 | Stearns 1992 | Ruxton et al. 2018 | Zahavi 1975 | Odling-Smee 2003

### Cooperation & trust
- Axelrod 1984 | Nowak & Sigmund 1998 | Noë & Hammerstein 1994 | Wilson 1975

### ALife
- Langton 1989 | Ray 1991 | Maturana & Varela 1980 | Lehman & Stanley 2011 | Stanley et al. 2017

### Machine Behaviour & AI
- Rahwan et al. 2019 | Chen et al. 2025 | Greenblatt et al. 2024 | Hubinger et al. 2024 | Barkur et al. 2025 | Szeider 2025

### Agent ecosystems
- Daian et al. 2020 | Li et al. 2026 | Hu et al. 2025 | Kumar et al. 2026

### Society
- Ostrom 1990 | Boyd & Richerson 1985 | Henrich 2015 | Anderson & Perona 2014

### Existing taxonomies (to differentiate from)
- Soder et al. 2024 | Martinelli 2025
