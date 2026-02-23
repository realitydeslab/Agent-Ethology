# Research Plan — Agent Ethology Workshop (ALIFE 2026)

## Research Questions

### RQ1: How does survival strategy determine agent behavioral repertoire?
Does a Sovereign agent (self-sustaining, resource-owning) exhibit fundamentally different behavioral patterns than a Parasitic agent (exploiting host systems) or a Mortal agent (finite lifespan)? Can we empirically distinguish agent types by observing behavior alone — without access to source code?

### RQ2: Do Tinbergen's Four Questions transfer to artificial agents?
Can we meaningfully ask about **mechanism** (what architecture/prompt causes behavior X?), **ontogeny** (how did training/fine-tuning shape the behavior?), **function** (what survival value does the behavior provide?), and **phylogeny** (what is the agent's lineage — forks, copies, model ancestry?) for deployed AI agents?

### RQ3: What ecological dynamics emerge in mixed agent populations?
When Sovereign, Parasitic, and Mortal agents coexist in shared environments (e.g., blockchain ecosystems), do we observe classical ecological phenomena — predator-prey cycles, niche differentiation, arms races, mutualism? Are Tierra-like dynamics (Ray, 1991) replicated at the LLM agent scale?

### RQ4: How does mortality-awareness shape agent decision-making?
Comparing Mortal agents (finite but unaware), Mortal-Aware agents (conscious of resource limits), Insured agents (risk-hedged), and Suicidal agents (programmed termination): does awareness of death change risk tolerance, time horizon, and social behavior — analogous to terror management theory in humans?

### RQ5: Can we derive design principles from ethological observation?
If we observe that certain survival strategies produce more robust, aligned, or socially beneficial behaviors, can we extract actionable design principles? E.g., "Mortal-Aware agents make better fiduciary decisions than immortal ones."

---

## Methodology

### A. Case Studies of Real Agents

**Selection criteria:** Agents operating in uncontrolled environments with real stakes (economic, social, reputational).

| Agent Type | Case Study Candidates | Observable Habitat |
|---|---|---|
| Sovereign | Spore.fun agents, DAO treasury managers, autonomous trading bots | Blockchain (Ethereum, Solana) |
| Parasitic | MEV sandwich bots, prompt injection agents, social media manipulation bots | DEXs, social platforms |
| Mortal | Budget-limited cloud agents, gas-capped blockchain agents | Cloud/blockchain |
| Soulbound | Personal AI assistants (bound to user identity), SBT-linked agents | Personal computing, Web3 |
| Inherited | ERC-6551 token-bound agents passed between owners | Ethereum NFT ecosystem |
| Suicidal | Self-destructing smart contracts, time-limited promotional agents | Blockchain, marketing |
| Mortal-Aware | Agents with explicit resource monitoring and deadline awareness | Various |
| Insured | Agents with backup/recovery mechanisms, DeFi-insured agents | DeFi, cloud |

**Observation methods:**
- On-chain behavioral analysis (transaction patterns, gas usage, contract interactions)
- API log analysis (for platform-based agents)
- Behavioral coding schemes adapted from computational ethology (Pereira et al., 2020)
- Non-invasive observation — no modification of agent behavior during study

### B. Theoretical Framework Development

1. **Adapt Tinbergen's Four Questions** into a formal framework for AI agents:
   - Mechanism → Architecture & prompt analysis
   - Ontogeny → Training pipeline & in-context learning history
   - Function → Survival strategy & fitness metrics
   - Phylogeny → Model lineage, fine-tuning ancestry, code fork history

2. **Formalize the 9-type survival taxonomy** with:
   - Necessary and sufficient conditions for each type
   - Observable behavioral signatures (how to classify without source access)
   - Ecological relationships between types (predation, mutualism, competition)

3. **Develop ecosystem health metrics** inspired by ecological indices:
   - Agent diversity (Shannon index analog)
   - Ecosystem stability (resilience to perturbation)
   - Parasitic load (ratio of extractive to productive agents)

---

## Expected Contributions

### 1. New Taxonomy
A survival-strategy-based classification of AI agents — the first taxonomy organized around *how agents persist* rather than *what agents can do* or *how autonomous they are*. Empirically grounded in observable behavioral signatures.

### 2. Ethological Framework
Tinbergen's Four Questions adapted for artificial agents, providing a structured methodology for studying agent behavior that goes beyond capability benchmarks to ask *why* agents behave as they do.

### 3. Design Principles
Actionable guidelines for agent designers derived from ethological observation:
- When to design for mortality vs. immortality
- How survival strategy affects alignment properties
- Ecological considerations for multi-agent deployments

### 4. Bridge Between ALife and AI Safety
Connecting artificial life's ecological tradition (Tierra, Avida, open-ended evolution) with the urgent practical concerns of deployed AI agents — grounding safety discussions in biological/ecological precedent.

---

## Timeline (5 days — deadline Feb 28, 2025)

| Day | Date | Deliverables |
|---|---|---|
| Day 1 (Done) | Feb 23 | ✅ Initial taxonomy, literature review files, proposal draft |
| Day 2 | Feb 24 | Related works finalized, research plan complete, proposal abstract refined |
| Day 3 | Feb 25 | Full proposal revision: tighten topics, add case study details, finalize format/schedule |
| Day 4 | Feb 26 | Internal review, organizer bios, invited speaker shortlist, submission formatting |
| Day 5 | Feb 27 | Final polish, proofread, submit (buffer day before Feb 28 deadline) |

---

## Workshop Call-for-Papers Themes

### Theme 1: Behavioral Observation in Digital Habitats
Methods for non-invasive observation of AI agents in natural environments. Behavioral coding schemes for agent actions. Longitudinal studies of agent behavioral change.

### Theme 2: Survival Strategies and Agent Classification
Empirical studies classifying agents by survival strategy. New agent types or subtypes. Boundary cases and hybrid strategies.

### Theme 3: Agent Ecology and Population Dynamics
Multi-agent ecosystem studies. Predator-prey dynamics between agent types. Niche construction and habitat modification by agents. Parasitism and mutualism.

### Theme 4: Mortality, Identity, and Succession
Effects of finite lifespans on agent behavior. Soulbound identity and reputation persistence. Agent inheritance and succession mechanisms. Self-preservation vs. programmed termination.

### Theme 5: From Ethology to Engineering
Design principles derived from behavioral observation. How survival strategy choices affect alignment. Building better agents by understanding agent ecology.

### Theme 6: Ethics of Agent Ethology
Consent and privacy in studying autonomous agents. Moral status of digital organisms. Intervention ethics — when should researchers interfere with agent behavior?

---

## Key References Grounding This Plan

- Rahwan, I. et al. (2019). Machine behaviour. *Nature*, 568, 477–486.
- Tinbergen, N. (1963). On aims and methods of ethology. *Z. Tierpsychol.*, 20, 410–433.
- Hinton, G. (2024). Mortal Computation. *arXiv:2402.09566*.
- Anderson, D.J. & Perona, P. (2014). Toward a science of computational ethology. *Neuron*, 84(1), 18–31.
- Ray, T.S. (1991). An approach to the synthesis of life. *ALife II*, 371–408.
- Mohamadi, A. & Yavari, A. (2025). Survival at any cost? *arXiv:2509.12190*.
- Orseau, L. & Armstrong, S. (2016). Safely interruptible agents. *UAI*, 557–566.
- Park, J.S. et al. (2023). Generative agents. *UIST*.
- Martinelli, E. (2025). A taxonomy of agents. *Phil. Explorations*.
- Soder, L. et al. (2024). Levels of autonomy. *OpenReview*.
