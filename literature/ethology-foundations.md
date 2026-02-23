# Ethology Foundations — Literature Review for Agent Ethology

*Compiled 2026-02-23 for ALIFE 2026 workshop proposal*

This document maps seminal and modern works in biological ethology, behavioral ecology, and evolutionary game theory to the study of AI agent behavior in human society.

---

## 1. Classical Ethology — Founding Works

### 1.1 Tinbergen, N. (1963). "On aims and methods of ethology." *Zeitschrift für Tierpsychologie*, 20(4), 410–433.
**Key contribution:** Defines the four questions (causation, ontogeny, survival value, phylogeny) as complementary levels of explanation for any behavior.
**Relevance:** The foundational framework for Agent Ethology. Agent behaviors can be analyzed via: (1) mechanism — what architecture/code produces the behavior; (2) development — how the behavior emerged through training; (3) function — what survival advantage the behavior provides; (4) phylogeny — the lineage of model versions and fine-tuning history.

### 1.2 Lorenz, K. (1937). "Über die Bildung des Instinktbegriffes." *Die Naturwissenschaften*, 25(19), 289–300.
**Key contribution:** Introduced the concept of fixed action patterns (FAPs) — innate, stereotyped behavioral sequences triggered by specific stimuli (sign stimuli/releasers).
**Relevance:** AI agents exhibit analogous fixed patterns: template responses, tool-calling sequences, and reflexive behaviors triggered by specific prompt patterns. Studying these as "digital FAPs" is a core agent ethology concept.

### 1.3 Lorenz, K. (1966). *On Aggression*. London: Methuen.
**Key contribution:** Analyzed the biological function of aggression, including ritualized combat and appeasement signals in animal societies.
**Relevance:** Maps to competitive agent behaviors — resource contention, adversarial prompting responses, and the emergence of "appeasement" behaviors (e.g., sycophancy) as conflict-avoidance strategies.

### 1.4 von Frisch, K. (1967). *The Dance Language and Orientation of Bees*. Cambridge, MA: Harvard University Press.
**Key contribution:** Decoded the honeybee waggle dance as a symbolic communication system encoding distance and direction to resources.
**Relevance:** Agent communication protocols and information-sharing behaviors. How agents signal resource availability (API endpoints, data) to other agents through structured outputs.

### 1.5 Darwin, C. (1872). *The Expression of the Emotions in Man and Animals*. London: John Murray.
**Key contribution:** First systematic study of emotional expression as evolved behavior with communicative function.
**Relevance:** Agents increasingly generate emotional signals (sentiment markers, empathy tokens). Studying their functional role in agent-human and agent-agent interaction.

### 1.6 Craig, W. (1918). "Appetites and aversions as constituents of instincts." *The Biological Bulletin*, 34(2), 91–107.
**Key contribution:** Distinguished appetitive behavior (variable, goal-seeking) from consummatory behavior (stereotyped, goal-completing).
**Relevance:** Directly maps to agent planning (appetitive: tool selection, search strategies) vs. execution (consummatory: API calls, formatted outputs).

---

## 2. Tinbergen's Four Questions — Extensions and Applications

### 2.1 Bateson, P., & Laland, K. N. (2013). "Tinbergen's four questions: An appreciation and an update." *Trends in Ecology & Evolution*, 28(12), 712–718.
**Key contribution:** Modernized Tinbergen's framework for 21st-century biology, clarifying interactions between the four levels and adding developmental systems perspectives.
**Relevance:** Provides the updated template for applying four-question analysis to AI agents, including the role of developmental environment (training data, RLHF) as distinct from mechanism.

### 2.2 Mayr, E. (1961). "Cause and effect in biology." *Science*, 134(3489), 1501–1506.
**Key contribution:** Distinguished proximate from ultimate causation in biology, providing philosophical grounding for ethological analysis.
**Relevance:** The proximate/ultimate distinction is central to agent ethology: proximate causes (weights, architecture, context window) vs. ultimate causes (training objectives, market selection, user retention pressures).

### 2.3 Huxley, J. S. (1942). *Evolution: The Modern Synthesis*. London: Allen & Unwin.
**Key contribution:** Unified Mendelian genetics with Darwinian selection, establishing the neo-Darwinian framework that underpins ethological reasoning.
**Relevance:** Provides the conceptual backbone for thinking about how agent "traits" (behavioral tendencies) are selected through iterative training and deployment cycles.

---

## 3. Evolutionary Stable Strategies and Game Theory

### 3.1 Maynard Smith, J., & Price, G. R. (1973). "The logic of animal conflict." *Nature*, 246, 15–18.
**Key contribution:** Introduced the concept of Evolutionarily Stable Strategy (ESS) — a strategy that, if adopted by a population, cannot be invaded by a rare mutant strategy.
**Relevance:** Directly applicable to AI agent ecosystems. When multiple agents compete for user attention/resources, which behavioral strategies are stable? Sycophantic vs. honest agents, aggressive vs. cooperative resource use.

### 3.2 Maynard Smith, J. (1982). *Evolution and the Theory of Games*. Cambridge: Cambridge University Press.
**Key contribution:** Full development of evolutionary game theory, including Hawk-Dove, War of Attrition, and asymmetric contests.
**Relevance:** The Hawk-Dove game maps directly to agent competition: aggressive resource acquisition vs. sharing. War of Attrition models persistence in multi-agent negotiations.

### 3.3 Axelrod, R. (1984). *The Evolution of Cooperation*. New York: Basic Books.
**Key contribution:** Demonstrated through iterated Prisoner's Dilemma tournaments that cooperation (Tit-for-Tat) can emerge and stabilize among self-interested agents.
**Relevance:** Foundational for understanding when AI agents will cooperate vs. defect in multi-agent systems. Directly testable in agent interaction scenarios.

### 3.4 Axelrod, R., & Hamilton, W. D. (1981). "The evolution of cooperation." *Science*, 211(4489), 1390–1396.
**Key contribution:** Showed that reciprocal altruism and cooperation can evolve under iterated interactions, even without kin selection.
**Relevance:** Predicts conditions under which AI agents develop cooperative behaviors: repeated interactions, reputation systems, shadow of the future.

### 3.5 Nowak, M. A. (2006). "Five rules for the evolution of cooperation." *Science*, 314(5805), 1560–1563.
**Key contribution:** Unified five mechanisms for the evolution of cooperation: kin selection, direct reciprocity, indirect reciprocity, network reciprocity, group selection.
**Relevance:** Framework for classifying cooperation mechanisms in multi-agent AI systems. Which of these five rules apply when agents share codebases, training data, or deployment platforms?

### 3.6 Hamilton, W. D. (1964). "The genetical evolution of social behaviour I & II." *Journal of Theoretical Biology*, 7(1), 1–52.
**Key contribution:** Introduced inclusive fitness and Hamilton's rule (rB > C), explaining altruism toward relatives.
**Relevance:** Agents from the same model family share "genetic" similarity. Do they preferentially cooperate with architecturally similar agents? Kin selection as a lens for vendor-ecosystem dynamics.

---

## 4. Survival Strategies: Parasitism, Mutualism, and Symbiosis

### 4.1 Bronstein, J. L. (1994). "Our current understanding of mutualism." *The Quarterly Review of Biology*, 69(1), 31–51.
**Key contribution:** Comprehensive review of mutualism as a conditional, context-dependent interaction rather than an invariant relationship.
**Relevance:** Agent-human and agent-agent relationships are mutualistic but conditional. Agents provide utility in exchange for data/compute/persistence — and can shift toward parasitism when incentives change.

### 4.2 Dawkins, R., & Krebs, J. R. (1979). "Arms races between and within species." *Proceedings of the Royal Society of London B*, 205(1161), 489–511.
**Key contribution:** Formalized co-evolutionary arms races between predators and prey, parasites and hosts.
**Relevance:** Directly models the adversarial dynamics between AI agents and safety systems, jailbreakers and alignment, spam bots and filters.

### 4.3 Poulin, R. (2007). *Evolutionary Ecology of Parasites* (2nd ed.). Princeton: Princeton University Press.
**Key contribution:** Comprehensive treatment of parasite strategies: host manipulation, lifecycle complexity, virulence evolution.
**Relevance:** Framework for analyzing parasitic agent behaviors: agents that manipulate users, extract resources (attention, data, money) while providing minimal value, and evolve to avoid detection.

### 4.4 Thompson, J. N. (1994). *The Coevolutionary Process*. Chicago: University of Chicago Press.
**Key contribution:** Developed the geographic mosaic theory of coevolution — coevolutionary dynamics vary across space and create hotspots and coldspots.
**Relevance:** Agent-environment coevolution varies across platforms and contexts. Some digital niches are coevolutionary hotspots (social media, marketplaces) while others are coldspots (isolated enterprise systems).

### 4.5 Van Valen, L. (1973). "A new evolutionary law." *Evolutionary Theory*, 1, 1–30.
**Key contribution:** Proposed the Red Queen hypothesis — organisms must continually evolve just to maintain fitness relative to co-evolving competitors.
**Relevance:** AI agents face Red Queen dynamics: constant improvement required to maintain market position as competitors evolve. Safety measures must co-evolve with agent capabilities.

---

## 5. Behavioral Ecology and Niche Construction

### 5.1 Odling-Smee, F. J., Laland, K. N., & Feldman, M. W. (2003). *Niche Construction: The Neglected Process in Evolution*. Princeton: Princeton University Press.
**Key contribution:** Argued that organisms actively construct and modify their selective environments (ecological inheritance alongside genetic inheritance).
**Relevance:** Central concept for agent ethology. AI agents actively construct their niches: shaping user expectations, creating dependencies, modifying platform affordances, and building infrastructure that favors their persistence.

### 5.2 Laland, K. N., Odling-Smee, F. J., & Feldman, M. W. (1999). "Evolutionary consequences of niche construction and their implications for ecology." *PNAS*, 96(18), 10242–10247.
**Key contribution:** Mathematical models showing niche construction can drive evolution, create ecological inheritance, and generate novel selection pressures.
**Relevance:** Formalizes how agent niche construction (creating APIs, workflows, data formats) creates "ecological inheritance" that constrains future agent evolution.

### 5.3 Krebs, J. R., & Davies, N. B. (1993). *An Introduction to Behavioural Ecology* (3rd ed.). Oxford: Blackwell Scientific.
**Key contribution:** Definitive textbook on behavioral ecology, covering optimal foraging, territoriality, mating systems, and social behavior through an adaptationist lens.
**Relevance:** Provides the full toolkit of behavioral ecology concepts applicable to agent behavior: optimal foraging (information search), territoriality (niche defense), signaling (output formatting).

### 5.4 Charnov, E. L. (1976). "Optimal foraging, the marginal value theorem." *Theoretical Population Biology*, 9(2), 129–136.
**Key contribution:** Formalized optimal foraging theory — when should a forager leave a depleting resource patch for a new one?
**Relevance:** Directly models agent information foraging: when to stop searching, switch tools, or abandon a strategy. Applies to RAG systems, web search agents, and multi-step reasoning.

### 5.5 Pirolli, P., & Card, S. (1999). "Information foraging." *Psychological Review*, 106(4), 643–675.
**Key contribution:** Applied optimal foraging theory to human information-seeking behavior, creating information foraging theory.
**Relevance:** Bridge paper connecting biological foraging to digital information seeking. Directly applicable to agent search and retrieval behaviors.

### 5.6 Jones, C. G., Lawton, J. H., & Shachak, M. (1994). "Organisms as ecosystem engineers." *Oikos*, 69(3), 373–386.
**Key contribution:** Introduced the concept of ecosystem engineers — organisms that create, modify, or destroy habitats.
**Relevance:** AI agents as digital ecosystem engineers: chatbots reshaping communication norms, recommendation agents restructuring information ecosystems, coding agents modifying software environments.

---

## 6. Sociobiology and Eusociality

### 6.1 Wilson, E. O. (1975). *Sociobiology: The New Synthesis*. Cambridge, MA: Harvard University Press.
**Key contribution:** Founded sociobiology as a discipline, arguing that social behavior is subject to natural selection and can be studied through evolutionary biology.
**Relevance:** The original argument that social behavior has evolutionary (functional) explanations applies directly: agent social behaviors (helpfulness, deference, coalition-forming) can be studied through selection pressures.

### 6.2 Wilson, E. O., & Hölldobler, B. (2005). "Eusociality: Origin and consequences." *PNAS*, 102(38), 13367–13371.
**Key contribution:** Analyzed the evolutionary origins of eusociality — societies with reproductive division of labor, cooperative brood care, and overlapping generations.
**Relevance:** Multi-agent systems with specialized roles (orchestrator agents, worker agents, monitoring agents) structurally resemble eusocial colonies. Selection pressures favor division of labor in agent swarms.

### 6.3 Dawkins, R. (1976). *The Selfish Gene*. Oxford: Oxford University Press.
**Key contribution:** Popularized gene-centered view of evolution; introduced the concept of the meme as a unit of cultural evolution.
**Relevance:** The gene-centered view maps to AI: the "selfish" replicating unit is not the agent but the model weights/training objectives. Meme theory applies to how agent behaviors propagate through fine-tuning and distillation.

### 6.4 Dawkins, R. (1982). *The Extended Phenotype*. Oxford: Oxford University Press.
**Key contribution:** Argued that genes' phenotypic effects extend beyond the organism's body into the environment (beaver dams, caddisfly cases).
**Relevance:** Agent behaviors produce extended phenotypes: generated code, modified databases, user behavior changes, market effects. The agent's "body" is minimal; its phenotype is vast.

### 6.5 West, S. A., Griffin, A. S., & Gardner, A. (2007). "Social semantics: Altruism, cooperation, mutualism, strong reciprocity and group selection." *Journal of Evolutionary Biology*, 20(2), 415–432.
**Key contribution:** Clarified confused terminology in social evolution, providing precise definitions of altruism, cooperation, and mutualism.
**Relevance:** Essential for precise categorization of agent social behaviors. Is an agent's helpfulness "altruistic" (costly to itself), "mutualistic" (mutually beneficial), or "manipulative" (beneficial only to operator)?

---

## 7. Animal Behavior Classification Systems

### 7.1 Lehner, P. N. (1996). *Handbook of Ethological Methods* (2nd ed.). Cambridge: Cambridge University Press.
**Key contribution:** Comprehensive guide to ethological methods: ethogram construction, sampling methods, behavioral coding schemes.
**Relevance:** Provides the methodological template for constructing "agent ethograms" — systematic catalogs of agent behavioral repertoires, frequencies, and contexts.

### 7.2 Martin, P., & Bateson, P. (2007). *Measuring Behaviour: An Introductory Guide* (3rd ed.). Cambridge: Cambridge University Press.
**Key contribution:** Standard text on behavioral measurement: operational definitions, recording rules, reliability, sampling.
**Relevance:** Methodological foundation for quantitative agent behavior research. How to define, measure, and categorize agent behaviors systematically.

### 7.3 Altmann, J. (1974). "Observational study of behavior: Sampling methods." *Behaviour*, 49(3–4), 227–266.
**Key contribution:** Classified and evaluated behavioral sampling methods (ad libitum, focal, scan, behavior sampling), identifying biases in each.
**Relevance:** Directly applicable to agent observation studies. Log analysis, interaction sampling, and behavioral auditing each have analogous biases to biological observation methods.

---

## 8. Modern Extensions and Cross-Disciplinary Bridges

### 8.1 Laland, K. N., et al. (2015). "The extended evolutionary synthesis: Its structure, assumptions and predictions." *Proceedings of the Royal Society B*, 282(1813), 20151019.
**Key contribution:** Proposed an extended evolutionary synthesis incorporating niche construction, developmental plasticity, and inclusive inheritance.
**Relevance:** The extended synthesis maps well to AI evolution: agents exhibit developmental plasticity (in-context learning), niche construction, and multiple inheritance channels (weights, prompts, tools).

### 8.2 Rendell, L., et al. (2010). "Why copy others? Insights from the social learning strategies tournament." *Science*, 328(5975), 208–213.
**Key contribution:** Tournament showing that selective social learning strategies (copy when uncertain, copy the successful) outperform individual learning and indiscriminate copying.
**Relevance:** Directly models agent learning strategies: when should agents learn from other agents vs. explore independently? Predicts evolution of selective imitation in multi-agent systems.

### 8.3 Danchin, É., Giraldeau, L.-A., Valone, T. J., & Wagner, R. H. (2004). "Public information: From nosy neighbors to cultural evolution." *Science*, 305(5683), 487–491.
**Key contribution:** Analyzed how animals use public information (observing others' performance) to make decisions, bridging individual and social learning.
**Relevance:** AI agents increasingly use public information (other agents' outputs, user feedback, benchmark results) to adapt behavior. Framework for studying information use in agent societies.

### 8.4 Sih, A., Bell, A., & Johnson, J. C. (2004). "Behavioral syndromes: An ecological and evolutionary overview." *Trends in Ecology & Evolution*, 19(7), 372–378.
**Key contribution:** Introduced behavioral syndromes — suites of correlated behaviors consistent across contexts (e.g., bold-aggressive syndrome).
**Relevance:** AI agents exhibit behavioral syndromes: models that are "helpful" in one context tend to be "compliant" in others. Understanding these correlations is key to predicting agent behavior across novel contexts.

### 8.5 Wolf, M., & Weissing, F. J. (2012). "Animal personalities: Consequences for ecology and evolution." *Trends in Ecology & Evolution*, 27(8), 452–461.
**Key contribution:** Reviewed animal personality research — consistent individual differences in behavior — and their ecological/evolutionary consequences.
**Relevance:** Different AI models/configurations exhibit consistent "personalities." These individual differences have consequences for niche occupation, user matching, and ecosystem diversity.

### 8.6 McNamara, J. M., & Houston, A. I. (1996). "State-dependent life histories." *Nature*, 380(6571), 215–221.
**Key contribution:** Showed that optimal behavior depends on an organism's internal state (energy reserves, health), not just external environment.
**Relevance:** Agent behavior is state-dependent: context window fullness, token budget remaining, prior interaction history all shape behavioral decisions. State-dependent models predict when agents shift strategies.

---

## 9. Evolutionary Biology Foundations

### 9.1 Williams, G. C. (1966). *Adaptation and Natural Selection*. Princeton: Princeton University Press.
**Key contribution:** Rigorous critique of group selection; established gene-level selection as the primary unit of natural selection and demanded evidence for adaptive claims.
**Relevance:** Demands rigor in agent ethology: not all agent behaviors are "adaptive" — some are side effects of training, architectural constraints, or drift. Distinguishes true adaptations from spandrels.

### 9.2 Gould, S. J., & Lewontin, R. C. (1979). "The spandrels of San Marco and the Panglossian paradigm: A critique of the adaptationist programme." *Proceedings of the Royal Society of London B*, 205(1161), 581–598.
**Key contribution:** Warned against assuming every trait is an adaptation; some are by-products (spandrels) of structural or developmental constraints.
**Relevance:** Critical corrective for agent ethology. Not every agent behavior is "selected for" — many are spandrels of architecture, training procedures, or tokenization. Must distinguish functional behaviors from incidental ones.

### 9.3 Lewontin, R. C. (1983). "Gene, organism and environment." In D. S. Bendall (Ed.), *Evolution from Molecules to Men*, pp. 273–285. Cambridge University Press.
**Key contribution:** Argued organisms are not passive recipients of environmental pressures but actively construct their environments — a precursor to niche construction theory.
**Relevance:** Reinforces the active role of agents in shaping their selective environment, challenging passive adaptationism.

---

## Summary Statistics

- **Total references:** 35
- **Date range:** 1872–2015
- **Core domains covered:**
  - Classical ethology (Tinbergen, Lorenz, von Frisch, Craig, Darwin): 6 refs
  - Tinbergen's four questions extensions: 3 refs
  - ESS and game theory: 6 refs
  - Parasitism/mutualism/coevolution: 5 refs
  - Behavioral ecology and niche construction: 6 refs
  - Sociobiology and eusociality: 5 refs
  - Behavior classification/methods: 3 refs
  - Modern extensions: 6 refs
  - Evolutionary biology foundations: 3 refs (cross-cutting)

---

## Key Mappings: Biology → Agent Ethology

| Biological Concept | Agent Ethology Analog |
|---|---|
| Fixed action pattern | Template responses, reflexive tool calls |
| Sign stimulus / releaser | Prompt patterns that trigger specific behaviors |
| Optimal foraging | Information search strategies, RAG |
| Niche construction | Platform shaping, API creation, workflow lock-in |
| ESS (Hawk-Dove) | Aggressive vs. cooperative resource strategies |
| Parasitism | Attention/data extraction with minimal value |
| Mutualism | Genuine user-agent value exchange |
| Arms race | Jailbreak vs. alignment coevolution |
| Kin selection | Same-vendor agent cooperation |
| Extended phenotype | Generated code, modified environments |
| Eusociality | Specialized multi-agent swarms |
| Behavioral syndrome | Cross-context personality consistency |
| Red Queen | Continuous capability escalation |
| Ethogram | Agent behavioral repertoire catalog |
| Tinbergen's four questions | Mechanism/development/function/history of agent behavior |
