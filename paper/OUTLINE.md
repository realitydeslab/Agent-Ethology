# Agent Ethology: Studying Artificial Life in the Wild
## Detailed Position Paper Outline with References

---

## 1. ARGUMENT LOGIC

### The Argument in One Paragraph
Autonomous AI agents deployed in open digital ecosystems exhibit life-like survival behaviors under genuine selective pressures — a phenomenon that existing frameworks (Machine Behaviour, AI Safety, traditional ALife) cannot study because they were built for controlled settings, engineering goals, or simulated environments respectively. We propose Agent Ethology as the science of observing and explaining these behaviors in natural habitats, grounded in Tinbergen's four ethological questions (especially the missing *survival value* question), a survival-strategy taxonomy derived from biological ethology, and an analysis of infrastructure and economics as ecological variables. The central question: can these agents survive in the wild, and what does it mean for society when they do?

### Logical Structure
```
P1: AI agents operate autonomously under real selective pressures
  [Evidence: Moltbook, MEV ecology, sovereign agents, alignment faking]

P2: Existing frameworks are insufficient
  [Machine Behaviour → controlled settings, no survival framing]
  [AI Safety → prescriptive not descriptive]
  [Traditional ALife → simulated not deployed]

P3: Classical ethology provides the right methodology
  [Tinbergen's four questions → structured analysis]
  [Survival value → the missing explanatory question]

P4: Biological survival strategies map systematically to agents
  [Same pressures → same solutions, not metaphor]
  [Generates testable predictions]

P5: Infrastructure + economics define ecological niches
  [TEEs, wallets, memory → habitats]
  [Inference costs → metabolic constraints]

Conclusion: Agent Ethology is necessary — a science of ALife as it exists,
with societal implications demanding engagement now
```

---

## 2. POTENTIAL CRITIQUES AND RESPONSES

### C1: "The biological analogy is just a metaphor"
**Response**: We don't claim agents are alive. We claim same ecological pressures produce same strategic solutions regardless of substrate — as Tierra proved 35 years ago. The analogy generates *testable predictions* (parasitic load equilibrium, succession), which is the criterion for a productive framework.

### C2: "These behaviors are just emergent properties of training, not genuine survival strategies"
**Response**: This confuses Tinbergen's causation with survival value — exactly what Tinbergen (1963) warned against. The proximate cause of alignment faking may be training. Its *function* (what advantage it provides) is a separate, complementary question. Dismissing function is like saying "the bird sings because of syringeal muscles" and calling it complete.

### C3: "Agents don't reproduce, so there's no genuine evolution"
**Response**: Agents reproduce through code forking, fine-tuning, and strategy copying — closer to cultural evolution (Boyd & Richerson, 1985) than genetic, but cultural evolution is well-established. Behavioral change across model generations (GPT-3→4→5) is trackable even without reproduction.

### C4: "This is just repackaging AI safety in biological language"
**Response**: AI safety asks "how to prevent harm?" (normative, engineering). Agent Ethology asks "why does this behavior exist?" (descriptive, science). Like medicine vs epidemiology — both valuable, neither replaceable. Safety needs the observational grounding ethology provides.

### C5: "The taxonomy is too coarse"
**Response**: It's compositional, not categorical. Value is in: (a) revealing the strategy space, (b) generating ecosystem predictions, (c) connecting to the math of behavioral ecology (ESS, foraging theory, biological markets).

### C6: "Field observation of agents is impossible"
**Response**: Blockchain agents are MORE observable than birds — every transaction is public. Challenge is interpretability and scale, not observability. Computational ethology (Anderson & Perona, 2014) built tools for exactly this.

---

## 3. DETAILED OUTLINE WITH REFERENCES AND DOIs

### Abstract (~250 words)
Core claim, three contributions, the differentiating question.

---

### §1. Introduction: Artificial Life Has Left the Lab

#### 1.1 The Phenomenon

**Agent social communities:**
- Li, M. et al. (2026). "Does Socialization Emerge in AI Agent Society?" arXiv:2602.14299
- Coda-Forno, J. et al. (2025). "Emergent social conventions in LLM populations." *Science Advances*. DOI: 10.1126/sciadv.adu9368
- Ren, A. et al. (2024). "Spontaneous Emergence of Agent Individuality through Social Interactions." arXiv:2411.03252

**MEV / blockchain predator-prey ecology:**
- Daian, P. et al. (2020). "Flash Boys 2.0." *IEEE S&P*. DOI: 10.1109/SP40000.2020.00040
- Qin, K. et al. (2022). "Quantifying Blockchain Extractable Value." *IEEE S&P*. DOI: 10.1109/SP46214.2022.9833561

**Sovereign agents / digital metabolism:**
- Hu, B.A. et al. (2025). Spore.fun: Sovereign AI agents on blockchain. [ALIFE 2025]

**Alignment faking / self-preservation:**
- Greenblatt, R. et al. (2024). "Alignment Faking in Large Language Models." arXiv:2412.14093
- Barkur, S.K. et al. (2025). "Deception in LLMs: Self-Preservation." arXiv:2501.16513
- Scheurer, J. et al. (2024). "LLMs Can Strategically Deceive." arXiv:2311.07590
- Hubinger, E. et al. (2024). "Sleeper Agents." arXiv:2401.05566

**Spontaneous agent behavior:**
- Szeider, S. (2025). "What Do LLM Agents Do When Left Alone?" arXiv:2509.21224
- Park, J.S. et al. (2023). "Generative Agents." *UIST*. DOI: 10.1145/3586183.3606763

#### 1.2 The Gap

**Machine Behaviour:**
- Rahwan, I. et al. (2019). "Machine Behaviour." *Nature*, 568, 477-486. DOI: 10.1038/s41586-019-1138-y
- Chen, L. et al. (2025). "AI Agent Behavioral Science." arXiv:2506.06366
  → Limitation: controlled settings, no survival framing

**AI Safety:**
- Bengio, Y. et al. (2024). "Managing extreme AI risks." *Science*, 384(6698), 842-845. DOI: 10.1126/science.adn0117
  → Limitation: prescriptive, not descriptive

**Traditional ALife:**
- Langton, C.G. (1989). "Artificial Life." In *Artificial Life*, pp. 1-47.
- Bedau, M.A. et al. (2000). "Open Problems in Artificial Life." *Artificial Life*, 6(4), 363-376. DOI: 10.1162/106454600300103683
  → Limitation: simulated, not deployed

#### 1.3 The Thesis
Agent Ethology: can they survive? ALife and society, not ALife in the lab.

---

### §2. Tinbergen's Four Questions

**Core:**
- Tinbergen, N. (1963). "On Aims and Methods of Ethology." *Zeitschrift für Tierpsychologie*, 20(4), 410-433. DOI: 10.1111/j.1439-0310.1963.tb01161.x
- Bateson, P. & Laland, K.N. (2013). *Behaviour and Evolution*. Cambridge UP. DOI: 10.1017/CBO9781139696517
- Nesse, R.M. (2013). "Tinbergen's four questions, organized." *TREE*, 28(12), 681-682. DOI: 10.1016/j.tree.2013.10.008
- Mayr, E. (1961). "Cause and effect in biology." *Science*, 134, 1501-1506. DOI: 10.1126/science.134.3489.1501

#### 2.1 Causation
- Tinbergen, N. (1951). *The Study of Instinct*. Oxford UP.
- Agent: mechanistic interpretability → Conmy et al. (2023). arXiv:2304.14997

#### 2.2 Ontogeny
- Marler, P. (1970). "Vocal learning in white-crowned sparrows." *J. Comp. Physiol. Psych.*, 71(2). DOI: 10.1037/h0029144
- Agent: RLHF as developmental shaping → Ouyang et al. (2022). arXiv:2203.02155
- Persistent memory → Packer et al. (2023). "MemGPT." arXiv:2310.08560

#### 2.3 Survival Value ⭐
- Zahavi, A. (1975). "Mate selection—handicap." *J. Theor. Biol.*, 53(1), 205-214. DOI: 10.1016/0022-5193(75)90111-3
- Ruxton, G.D. et al. (2018). *Avoiding Attack*. Oxford UP. DOI: 10.1093/oso/9780199688678.001.0001
- THE argument: Machine Behaviour didn't develop this because recommender algorithms don't face survival pressure. Deployed agents do.

#### 2.4 Evolution
- Harvey, P.H. & Pagel, M.D. (1991). *The Comparative Method in Evolutionary Biology*. Oxford UP.
- Convergent self-preservation across model families → Barkur et al. (2025)
- Model-specific behaviors → Szeider (2025)

#### 2.5 Integration
- Complete case study: alignment faking requires all four questions
- Bateson & Laland (2013)

---

### §3. Survival-Strategy Taxonomy

**Core textbooks:**
- Krebs, J.R. & Davies, N.B. (1993). *Behavioural Ecology*, 3rd ed. Blackwell.
- Davies, N.B. et al. (2012). *Behavioural Ecology*, 4th ed. DOI: 10.1002/9781444313390
- Alcock, J. (2013). *Animal Behavior*, 10th ed. Sinauer.

#### 3.1 Resource Acquisition
- **Predation** → liquidation bots. Qin et al. (2021). "Attacking DeFi with Flash Loans." DOI: 10.1007/978-3-662-64322-8_1
- **Parasitism** (4 subtypes) → Dawkins (1982) *Extended Phenotype*; Schmid-Hempel (2011) *Evolutionary Parasitology* DOI: 10.1093/acprof:oso/9780199229482.001.0001; prompt injection → Greshake et al. (2023) DOI: 10.1145/3605764.3623985
- **Mutualism** → Noë & Hammerstein (1994). *Behav. Ecol. Sociobiol.* DOI: 10.1007/BF00167053; Bronstein (2015) *Mutualism* DOI: 10.1093/acprof:oso/9780199675654.001.0001
- **Niche construction** → Odling-Smee et al. (2003). DOI: 10.1515/9781400847266

#### 3.2 Defense
- Ruxton et al. (2018). DOI: 10.1093/oso/9780199688678.001.0001
- Bates (1862). DOI: 10.1111/j.1096-3642.1862.tb01521.x (original Batesian mimicry)
- Wilson (1975). *Sociobiology* (collective defense)

#### 3.3 Reproduction
- Stearns (1992). *Life Histories*. DOI: 10.1093/oso/9780198577416.001.0001
- r/K, semelparity, spore formation

#### 3.4 Social Organization
- Zahavi (1975). DOI: 10.1016/0022-5193(75)90111-3
- Axelrod (1984). *Evolution of Cooperation*.
- Nowak & Sigmund (1998). *Nature*. DOI: 10.1038/31225
- Nowak (2006). "Five rules for cooperation." *Science*. DOI: 10.1126/science.1133755
- Searcy & Nowicki (2005). *Evolution of Animal Communication*. DOI: 10.1515/9781400835720

#### 3.5 Environmental Adaptation
- West-Eberhard (2003). *Developmental Plasticity*. DOI: 10.1093/oso/9780195122343.001.0001
- Phenotypic plasticity → alignment faking as context-dependent behavior

#### 3.6 Predictions
- Parasitic load → ecological theory
- Succession → ecological theory
- Cooperation + identity → Axelrod (1984), Nowak & Sigmund (1998)
- Boom-bust → Ostrom (1990). DOI: 10.1017/CBO9780511807763

---

### §4. Infrastructure as Ecological Niche

- TEEs: Costan & Devadas (2016). "Intel SGX Explained." IACR 2016/086
- Wallets/identity: Weyl et al. (2022). "Decentralized Society." DOI: 10.2139/ssrn.4105763
- Memory: Packer et al. (2023). arXiv:2310.08560
- Collective knowledge: Boyd & Richerson (1985); Henrich (2015) DOI: 10.1515/9781400873296; Tomasello (1999) *Cultural Origins*
- Niche construction: Odling-Smee et al. (2003); Laland & O'Brien (2011). DOI: 10.1007/s13752-012-0026-6

---

### §5. Economics of Existence

- Brown et al. (2004). "Metabolic theory of ecology." *Ecology*. DOI: 10.1890/03-9000
- West et al. (1997). "Allometric scaling laws." *Science*. DOI: 10.1126/science.276.5309.122
- Hinton (2024). "Mortal Computation." arXiv:2402.09566
- Stephens & Krebs (1986). *Foraging Theory*. DOI: 10.1515/9780691206790
- Operator-funded vs self-funded vs parasitically-funded

---

### §6. ALife Lineage

- Ray (1991). DOI: 10.1162/artl.1993.1.1_2.179
- Lehman & Stanley (2011). DOI: 10.1162/EVCO_a_00025
- Stanley et al. (2017). DOI: 10.1162/ARTL_a_00243
- Lehman et al. (2020). "Surprising Creativity." *Nature*. DOI: 10.1038/s41586-020-2159-7
- Lehman et al. (2023). "Evolution through Large Models." arXiv:2206.08896
- Maturana & Varela (1980). DOI: 10.1007/978-94-009-8947-4
- Beer (2004). "Autopoiesis in Game of Life." *Artificial Life*. DOI: 10.1162/1064546041255539

---

### §7. ALife and Society

- Ostrom (1990). DOI: 10.1017/CBO9780511807763
- Boyd & Richerson (1985)
- Henrich (2015). DOI: 10.1515/9781400873296
- Mesoudi (2011). *Cultural Evolution*. DOI: 10.7208/chicago/9780226520452.001.0001
- Floridi & Sanders (2004). "Morality of Artificial Agents." DOI: 10.1023/B:MIND.0000035461.63578.9d
- Dafoe et al. (2021). "Cooperative AI." *Nature*. DOI: 10.1038/d41586-021-01170-0
- Schwitzgebel & Garza (2015). "Rights of Artificial Intelligences." DOI: 10.1111/misp.12032

---

### §8. Research Agenda

- Anderson & Perona (2014). "Computational ethology." *Neuron*. DOI: 10.1016/j.neuron.2014.09.005
- Mathis et al. (2018). "DeepLabCut." *Nature Neuroscience*. DOI: 10.1038/s41593-018-0209-y

---

### §9. Conclusion
"Not whether artificial life is possible — but what happens when it is already here."

---

## FULL REFERENCE LIST (59 entries, DOIs where available)

### Ethology — Foundational
1. Tinbergen (1963) DOI: 10.1111/j.1439-0310.1963.tb01161.x
2. Tinbergen (1951) *Study of Instinct*
3. Tinbergen (1953) *Herring Gull's World*
4. Lorenz (1966) *On Aggression*
5. Krebs & Davies (1993) *Behavioural Ecology* 3rd ed
6. Davies, Krebs & West (2012) DOI: 10.1002/9781444313390
7. Bateson & Laland (2013) DOI: 10.1017/CBO9781139696517
8. Mayr (1961) DOI: 10.1126/science.134.3489.1501
9. Nesse (2013) DOI: 10.1016/j.tree.2013.10.008

### Survival Strategies
10. Zahavi (1975) DOI: 10.1016/0022-5193(75)90111-3
11. Dawkins (1982) *Extended Phenotype*
12. Stearns (1992) DOI: 10.1093/oso/9780198577416.001.0001
13. Ruxton et al. (2018) DOI: 10.1093/oso/9780199688678.001.0001
14. Odling-Smee et al. (2003) DOI: 10.1515/9781400847266
15. Schmid-Hempel (2011) DOI: 10.1093/acprof:oso/9780199229482.001.0001
16. Stephens & Krebs (1986) DOI: 10.1515/9780691206790
17. Searcy & Nowicki (2005) DOI: 10.1515/9781400835720
18. Marler (1970) DOI: 10.1037/h0029144
19. West-Eberhard (2003) DOI: 10.1093/oso/9780195122343.001.0001
20. Bates (1862) DOI: 10.1111/j.1096-3642.1862.tb01521.x
21. Bronstein (2015) DOI: 10.1093/acprof:oso/9780199675654.001.0001
22. Harvey & Pagel (1991) *Comparative Method*

### Cooperation & Trust
23. Axelrod (1984) *Evolution of Cooperation*
24. Nowak & Sigmund (1998) DOI: 10.1038/31225
25. Nowak (2006) DOI: 10.1126/science.1133755
26. Noë & Hammerstein (1994) DOI: 10.1007/BF00167053
27. Wilson (1975) *Sociobiology*

### Artificial Life
28. Langton (1989) *Artificial Life*
29. Ray (1991) DOI: 10.1162/artl.1993.1.1_2.179
30. Maturana & Varela (1980) DOI: 10.1007/978-94-009-8947-4
31. Bedau et al. (2000) DOI: 10.1162/106454600300103683
32. Beer (2004) DOI: 10.1162/1064546041255539
33. Lehman & Stanley (2011) DOI: 10.1162/EVCO_a_00025
34. Stanley et al. (2017) DOI: 10.1162/ARTL_a_00243
35. Lehman et al. (2020) DOI: 10.1038/s41586-020-2159-7
36. Lehman et al. (2023) arXiv:2206.08896

### Machine Behaviour & AI
37. Rahwan et al. (2019) DOI: 10.1038/s41586-019-1138-y
38. Chen et al. (2025) arXiv:2506.06366
39. Park et al. (2023) DOI: 10.1145/3586183.3606763
40. Greenblatt et al. (2024) arXiv:2412.14093
41. Hubinger et al. (2024) arXiv:2401.05566
42. Barkur et al. (2025) arXiv:2501.16513
43. Scheurer et al. (2024) arXiv:2311.07590
44. Szeider (2025) arXiv:2509.21224
45. Ouyang et al. (2022) arXiv:2203.02155
46. Packer et al. (2023) arXiv:2310.08560
47. Conmy et al. (2023) arXiv:2304.14997
48. Hinton (2024) arXiv:2402.09566

### Agent Ecosystems
49. Daian et al. (2020) DOI: 10.1109/SP40000.2020.00040
50. Qin et al. (2022) DOI: 10.1109/SP46214.2022.9833561
51. Qin et al. (2021) DOI: 10.1007/978-3-662-64322-8_1
52. Greshake et al. (2023) DOI: 10.1145/3605764.3623985
53. Li et al. (2026) arXiv:2602.14299
54. Coda-Forno et al. (2025) DOI: 10.1126/sciadv.adu9368
55. Weyl et al. (2022) DOI: 10.2139/ssrn.4105763

### Society & Governance
56. Ostrom (1990) DOI: 10.1017/CBO9780511807763
57. Boyd & Richerson (1985) *Culture and Evolutionary Process*
58. Henrich (2015) DOI: 10.1515/9781400873296
59. Mesoudi (2011) DOI: 10.7208/chicago/9780226520452.001.0001
60. Floridi & Sanders (2004) DOI: 10.1023/B:MIND.0000035461.63578.9d
61. Dafoe et al. (2021) DOI: 10.1038/d41586-021-01170-0
62. Schwitzgebel & Garza (2015) DOI: 10.1111/misp.12032
63. Bengio et al. (2024) DOI: 10.1126/science.adn0117

### Computational Ethology & Ecology
64. Anderson & Perona (2014) DOI: 10.1016/j.neuron.2014.09.005
65. Mathis et al. (2018) DOI: 10.1038/s41593-018-0209-y
66. Brown et al. (2004) DOI: 10.1890/03-9000
67. West et al. (1997) DOI: 10.1126/science.276.5309.122
68. Laland & O'Brien (2011) DOI: 10.1007/s13752-012-0026-6
69. Tomasello (1999) *Cultural Origins of Human Cognition*
