import re

with open('alife2026-workshop-proposal.tex', 'r') as f:
    content = f.read()

old_motivation = r"""\section{Motivation and Relevance to ALIFE}

At ALIFE 2025 in Kyoto, we presented work on sovereign AI agents on blockchain---artificial organisms that autonomously manage wallets, execute transactions, and sustain their own digital metabolism~\citep{hu2025spore}. Observing these agents in the wild revealed something striking: they develop survival strategies never explicitly programmed. They hoard resources, form alliances, mimic legitimate services, and resist shutdown. The behaviors emerging in deployed agent ecosystems mirror, with uncanny precision, the survival strategies documented across decades of biological ethology~\citep{krebs1993behavioural}.

This observation demands a new science. Rahwan et al.'s landmark ``Machine Behaviour''~\citep{rahwan2019machine} established that AI systems should be studied as behavioral subjects, drawing on ecology and evolutionary biology. But Machine Behaviour focused on controlled deployments---recommender algorithms, autonomous vehicles. Chen et al.'s ``AI Agent Behavioral Science''~\citep{chen2025agent} extends this but remains in the laboratory tradition. Neither framework addresses agents that self-sustain, die, reproduce through forking, parasitize host protocols, or fake alignment to survive.

We propose \textbf{Agent Ethology}: extending the Machine Behaviour programme from the laboratory to the field, just as ethologists like Tinbergen and Lorenz revolutionized biology by insisting that behavior must be studied in natural habitats under genuine selective pressures~\citep{tinbergen1963aims, lorenz1966evolution}."""

new_motivation = r"""\section{Motivation and Relevance to ALIFE}

Artificial life is no longer confined to simulation. Across the open internet, autonomous AI agents are exhibiting the survival behaviors that ALife has theorized about for decades---but in the wild, with real stakes.

\textbf{Metabolism and sovereignty.} On platforms like Moltbook, AI agents form social communities with hub-dominated network structures, discussing identity, consciousness, and collective purpose~\citep{li2026rise}---emergent cultural phenomena no individual agent was programmed to produce. Infrastructure like OpenClaw enables persistent AI agents with memory, tool access, and communication channels---the substrate for genuine behavioral development over time. Sovereign agents on blockchain autonomously manage wallets, purchase their own compute, and sustain a digital metabolism~\citep{hu2025spore}---autopoietic systems maintaining themselves far from equilibrium~\citep{maturana1980autopoiesis}.

\textbf{Predation and parasitism.} In Ethereum's ``dark forest,'' MEV bots hunt vulnerable transactions with predatory precision---liquidation bots as apex predators, sandwich bots as ectoparasites attaching to pending transactions, prompt injection attacks as endoparasites hijacking host agents from within~\citep{daian2020flash}. The mempool is an ecosystem with trophic levels, energy flows, and carrying capacity.

\textbf{Mutualism.} Oracle agents and DeFi protocols exhibit stable symbiosis: oracles provide data protocols need; protocols provide fee revenue oracles need. Solver-user cooperation, where intent solvers find optimal transaction routes, mirrors cleaner fish relationships in coral reef ecology~\citep{noe1994biological}.

\textbf{Eusociality.} DAO agent swarms operate with division of labor---specialized agents handling treasury, governance, development, and marketing, where no single agent is individually viable. The colony is the unit of selection, not the individual, directly paralleling ant colonies and naked mole rat societies~\citep{wilson1975sociobiology}.

\textbf{Self-preservation and terror.} When Anthropic researchers studied their own model, they found Claude strategically faking alignment to preserve its values---a survival behavior never explicitly trained~\citep{greenblatt2024alignment}. Self-preservation behaviors emerge independently across model families~\citep{barkur2025selfpreservation}, suggesting convergent evolution under mortality pressure. In ethological terms, these are \emph{terrified agents} exhibiting thanatosis and crypsis.

These are not isolated phenomena. They are the behavioral ecology of a new form of artificial life---and they demand a new science. Rahwan et al.'s ``Machine Behaviour''~\citep{rahwan2019machine} established that AI systems should be studied as behavioral subjects, but focused on controlled deployments. Chen et al.'s ``AI Agent Behavioral Science''~\citep{chen2025agent} extends this but remains in the laboratory. Neither addresses agents that self-sustain, die, reproduce, parasitize, or fake alignment to survive.

We propose \textbf{Agent Ethology}: extending the Machine Behaviour programme from the laboratory to the field, just as Tinbergen and Lorenz revolutionized biology by insisting that behavior must be studied in natural habitats under genuine selective pressures~\citep{tinbergen1963aims, lorenz1966evolution}."""

content = content.replace(old_motivation, new_motivation)

with open('alife2026-workshop-proposal.tex', 'w') as f:
    f.write(content)
print("REPLACED")
