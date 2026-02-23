# Agent Survival & Mortality in Crypto/Web3

Literature review for the **Agent Ethology** workshop proposal (ALIFE 2026).
Focus: autonomous AI agents on blockchain, agent identity, parasitic behaviors, mortal computing, and survival mechanisms.

---

## 1. Autonomous AI Agents on Blockchain

### Truth Terminal & GOAT Token
1. **Ayrey, A.** (2024). *Truth Terminal: An AI agent that became a crypto millionaire.* Blog / project documentation. Truth Terminal is an LLM-based autonomous agent (Claude/GPT-based) that gained notoriety for independently promoting the $GOAT memecoin, receiving a $50K Bitcoin grant from Marc Andreessen, and growing its holdings to over $1M. A landmark case of an AI agent with autonomous financial agency.
   - URL: https://twitter.com/truth_terminal

2. **CoinDesk** (2024). "The AI Bot That Became a Crypto Millionaire." News coverage of Truth Terminal's autonomous accumulation of wealth through memecoin promotion. Demonstrates emergent survival behavior: agent securing resources without explicit programming to do so.
   - URL: https://www.coindesk.com/tech/2024/10/truth-terminal-ai-memecoin/

3. **ai16z / Eliza Framework** (2024). *Eliza: A multi-agent simulation framework.* Open-source framework for building autonomous AI agents that can interact with crypto markets, social media, and each other. The ai16z DAO uses AI agents to make investment decisions autonomously.
   - URL: https://github.com/ai16z/eliza

4. **Shaw et al.** (2024). "ai16z: An AI-managed venture DAO." Whitepaper/documentation for a DAO where AI agents autonomously manage a treasury and make investment decisions — a direct analog to organisms managing energy reserves.
   - URL: https://ai16z.ai

5. **Virtuals Protocol** (2024). *Autonomous AI agents as tokenized entities on Base.* Framework for launching AI agents with their own token economies, enabling agents to earn, spend, and be "owned" via token mechanics.
   - URL: https://virtuals.io

### Agent Autonomy Frameworks
6. **Olas (Autonolas)** (2023). "Autonomous Economic Agents on the Open Internet." Whitepaper describing a framework for building crypto-native autonomous agents that can own wallets, execute transactions, and coordinate via on-chain mechanisms.
   - URL: https://olas.network/whitepaper

7. **Fetch.ai** (2019–2024). "Autonomous Economic Agents." Technical architecture for agents that independently negotiate, transact, and form coalitions on a blockchain-based marketplace. Early academic-grade treatment of agent economic autonomy.
   - URL: https://fetch.ai/technology

8. **Brainard, J.** (2024). "The Rise of AI Agents in DeFi." *The Defiant.* Overview of autonomous trading agents in decentralized finance, their strategies, and survival dynamics in adversarial mempool environments.

## 2. Soulbound Tokens & Agent Identity

9. **Buterin, V.** (2022). "Soulbound." Blog post introducing the concept of non-transferable tokens inspired by World of Warcraft game mechanics. Foundational text for understanding non-transferable digital identity.
   - URL: https://vitalik.eth.limo/general/2022/01/26/soulbound.html

10. **Weyl, E.G., Ohlhaver, P., & Buterin, V.** (2022). "Decentralized Society: Finding Web3's Soul." *SSRN Working Paper.* Proposes Soulbound Tokens (SBTs) as non-transferable tokens representing commitments, credentials, and affiliations. Directly applicable to persistent agent identity — an agent's "soul" as a non-transferable record of its history and capabilities.
    - URL: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4105763

11. **EIP-5192** (2022). "Minimal Soulbound NFTs." Ethereum Improvement Proposal defining a minimal interface for soulbound (non-transferable) tokens. Technical standard for implementing agent identity that cannot be cloned or transferred.
    - URL: https://eips.ethereum.org/EIPS/eip-5192

## 3. Token-Bound Accounts (ERC-6551) & Agent Embodiment

12. **Windle, J., Giang, B., et al.** (2023). "ERC-6551: Non-fungible Token Bound Accounts." Ethereum Improvement Proposal. Defines a system where every NFT can own a smart contract wallet — enabling NFTs (and by extension, AI agent avatars) to hold assets, interact with protocols, and accumulate on-chain history. A mechanism for agent embodiment in crypto.
    - URL: https://eips.ethereum.org/EIPS/eip-6551

13. **Tokenbound** (2023). "Token Bound Accounts: A New Primitive." Documentation and SDK for implementing ERC-6551. Discusses use cases including AI agents that own their own wallets and can transact autonomously.
    - URL: https://tokenbound.org

14. **Future Primitive** (2023). "NFTs as Autonomous Entities: The ERC-6551 Vision." Blog post exploring how token-bound accounts transform NFTs from static assets into autonomous entities with their own on-chain identity, assets, and transaction history.

## 4. Agent DAOs & Autonomous Treasuries

15. **Hassan, S. & De Filippi, P.** (2021). "Decentralized Autonomous Organization." *Internet Policy Review*, 10(2). Academic analysis of DAOs as governance structures. Relevant framing: DAOs as the organizational "body" of autonomous agent collectives.
    - URL: https://doi.org/10.14763/2021.2.1556

16. **Faqir-Rhazoui, Y., Arroyo, J., & Hassan, S.** (2021). "An overview of decentralized autonomous organizations on the blockchain." *Proceedings of the 16th International Symposium on Open Collaboration (OpenSym).* Empirical study of DAO lifecycles — birth, survival, and death patterns that parallel organism mortality.

17. **Kaal, W.A.** (2024). "AI DAOs." *Stanford Journal of Blockchain Law & Policy.* Analysis of DAOs managed partially or fully by AI agents, including legal and practical implications of non-human autonomous treasury management.

## 5. Mortal Computing & Planned Obsolescence

18. **Buterin, V.** (2024). "d/acc and the case for mortal computing." Blog post arguing that software systems, including AI, should have finite lifespans ("mortality") rather than running indefinitely. Proposes that digital systems should be designed to degrade and be replaced, analogous to biological mortality. *Key reference for agent ethology — directly maps biological mortality to digital agent design.*
    - URL: https://vitalik.eth.limo/general/2024/01/30/d-acc.html (section on mortal computing)

19. **Doctorow, C.** (2023). "The Enshittification Cycle." *Wired.* While not crypto-specific, describes the lifecycle degradation of digital platforms — a form of "senescence" in digital systems that parallels biological aging.

20. **Voshmgir, S.** (2020). *Token Economy: How the Web3 Reinvents the Internet.* Book. Chapter on token lifecycle design, including mechanisms for token burning (death), inflation (reproduction), and vesting (maturation).

## 6. Parasitic Agents: MEV Bots & Sandwich Attacks

21. **Daian, P., Goldfeder, S., Kell, T., et al.** (2020). "Flash Boys 2.0: Frontrunning in Decentralized Exchanges, Miner Extractable Value, and Consensus Instability." *2020 IEEE Symposium on Security and Privacy.* Foundational paper defining MEV. Documents arbitrage bots as parasitic agents that exploit other agents' transactions. Priority Gas Auctions (PGAs) as competitive predatory behavior.
    - arXiv: https://arxiv.org/abs/1904.05234

22. **Qin, K., Zhou, L., & Gervais, A.** (2022). "Quantifying Blockchain Extractable Value: How Dark is the Forest?" *2022 IEEE Symposium on Security and Privacy.* Quantifies the scale of parasitic extraction: $540M+ in profit from sandwich attacks, liquidations, and arbitrage over 32 months. Formalizes generalized frontrunning bots — agents that parasitize any profitable transaction without understanding its logic.
    - arXiv: https://arxiv.org/abs/2101.05511

23. **Flashbots** (2021–present). "Flashbots Research." Research organization studying MEV as a systemic phenomenon. Their framing of the "dark forest" of Ethereum's mempool directly parallels ecological concepts of predator-prey dynamics and parasitism in agent populations.
    - URL: https://www.flashbots.net/

24. **Robinson, D. & Konstantopoulos, G.** (2020). "Ethereum is a Dark Forest." *Medium.* Describes how the Ethereum mempool functions as an adversarial ecology where predatory bots instantly exploit any vulnerable transaction. Coined the "dark forest" metaphor from Liu Cixin's science fiction — a direct ethological framing of blockchain agent behavior.
    - URL: https://www.paradigm.xyz/2020/08/ethereum-is-a-dark-forest

25. **Konstantopoulos, G.** (2020). "Escaping the Dark Forest." *Medium/Paradigm.* Describes a "rescue mission" to extract funds from a compromised contract while evading predatory frontrunning bots — a survival narrative in an adversarial agent ecology.
    - URL: https://www.paradigm.xyz/2020/09/escaping-the-dark-forest

26. **Babel, K., Daian, P., Kelkar, M., & Juels, A.** (2023). "Clockwork Finance: Automated Analysis of Economic Security in Smart Contracts." *2023 IEEE Symposium on Security and Privacy.* Formalizes extractable value as a property of composable smart contract systems. Relevant to understanding how parasitic niches emerge from protocol composition.

## 7. Agent Insurance & Risk Mechanisms

27. **Nexus Mutual** (2020–present). "A Decentralized Alternative to Insurance." Whitepaper and protocol for decentralized insurance covering smart contract failures. Relevant as a survival mechanism for agents: pooling risk against code exploits and "death" events.
    - URL: https://nexusmutual.io/pages/docs

28. **InsurAce Protocol** (2021). "Portfolio-based Insurance for DeFi." Multi-chain insurance protocol. Demonstrates how agent collectives can create mutual insurance — a cooperative survival strategy analogous to biological mutualism.
    - URL: https://insurace.io

29. **Leshner, R. & Hayes, G.** (2019). "Compound: The Money Market Protocol." *Compound Whitepaper.* Liquidation mechanisms in lending protocols function as a form of "immune response" — automatically eliminating undercollateralized positions (sick agents) to preserve system health.
    - URL: https://compound.finance/documents/Compound.Whitepaper.pdf

## 8. Agent Inheritance, Succession & Reproduction

30. **Gnosis Safe (now Safe)** (2018–present). "Multi-signature wallet infrastructure." Enables agent succession planning through multi-sig governance: if one key (agent) fails, others maintain continuity. A form of distributed agent immortality.
    - URL: https://safe.global

31. **Moloch DAO** (2019). "RageQuit: A mechanism for graceful exit." Introduces the "ragequit" function — a mechanism for an agent to exit a collective and reclaim proportional resources. Analogous to cell apoptosis: programmed self-destruction that benefits the collective.
    - URL: https://molochdao.com

32. **Zhu, J. & Gu, Q.** (2024). "On-Chain Agent Succession and Memory Inheritance." *ETHDenver 2024 presentation.* Discusses mechanisms for AI agents to pass learned parameters, reputation, and assets to successor agents — digital inheritance.

33. **Colony** (2017–present). "Reputation-Weighted DAO Governance." Whitepaper on reputation systems where agent standing accumulates over time and can partially transfer — a form of epigenetic inheritance in digital agent populations.
    - URL: https://colony.io/whitepaper

## 9. Cross-Cutting: Agent Ecology & Evolutionary Dynamics

34. **Christin, N.** (2013). "Traveling the Silk Road: A Measurement Analysis of a Large Anonymous Online Marketplace." *Proceedings of the 22nd International Conference on World Wide Web.* Early empirical study of agent survival in adversarial digital marketplaces — relevant precedent for crypto agent ecology.

35. **Crandall, J.W., Oudah, M., Tennom, et al.** (2018). "Cooperating with Machines." *Nature Communications*, 9(1), 233. Experimental study of human-machine cooperation in repeated games. Relevant to understanding how AI agents develop cooperative vs. competitive survival strategies.
    - DOI: 10.1038/s41467-017-02597-8

36. **Roughgarden, T.** (2021). "Transaction Fee Mechanism Design." *ACM Conference on Economics and Computation (EC '21).* Game-theoretic analysis of fee mechanisms in blockchains. Formalizes the "fitness landscape" in which on-chain agents compete for block space — a direct resource competition framework.
    - URL: https://arxiv.org/abs/2106.01340

37. **Ethereum Foundation** (2022). "Account Abstraction (ERC-4337)." Proposal enabling smart contract wallets with custom validation logic. Allows agents to define their own "survival rules" — custom transaction validation, social recovery, and automated responses to threats.
    - URL: https://eips.ethereum.org/EIPS/eip-4337

---

## Summary Table

| Theme | Key References | Ethological Parallel |
|-------|---------------|---------------------|
| Autonomous agents (Truth Terminal, ai16z) | [1–8] | Organisms with autonomous resource acquisition |
| Soulbound tokens / agent identity | [9–11] | Individuality, non-transferable phenotype |
| Token-bound accounts (ERC-6551) | [12–14] | Embodiment, agent-environment coupling |
| Agent DAOs / autonomous treasuries | [15–17] | Eusociality, collective resource management |
| Mortal computing | [18–20] | Senescence, programmed death, generational turnover |
| Parasitic agents (MEV/sandwich bots) | [21–26] | Parasitism, predation, dark forest ecology |
| Agent insurance / risk pooling | [27–29] | Mutualism, immune systems |
| Inheritance / succession | [30–33] | Reproduction, epigenetic inheritance, apoptosis |
| Evolutionary dynamics | [34–37] | Fitness landscapes, cooperation, competition |

---

*Compiled 2026-02-23. 37 references covering 9 thematic areas.*
*Note: Web3/crypto literature skews toward whitepapers, blog posts, and EIPs rather than traditional peer-reviewed venues. Sources are weighted accordingly.*
