# Base–Modifier–Cache Grammar (BMCG) v1.0
**A Formal Architecture for Constrained Symbolic Generation**

> **Status:** Formal Specification (v1.0)  
> **Date:** 2026-04-24  
> **Seed Object:** Nwagu Aneke Script (Umuleri, SE Nigeria)  
> **Architectural Goal:** Portable symbolic compression for governance, AI, and narrative systems.

---

## 0. Abstract
BMCG is a formal design pattern for generating large expressive vocabularies from a small set of primitives. It abstracts the structural logic observed in the Nwagu Aneke script—a 26-row by 8-column syllabic matrix supplemented by logographs—into a portable grammar. The architecture is defined by the interaction between a **Compositional Layer** (Base × Modifier) and a **Cache Layer** (Logographs), constrained by sequencing rules and interpreted through context.

---

## 1. Formal Definitions

Let the BMCG system be defined as a 5-tuple: $\mathcal{S} = \langle B, M, L, \Phi, \Gamma \rangle$

### 1.1 Base Set ($B$)
A finite set of $n$ irreducible primitives representing the ontological categories of a domain.
$$B = \{b_1, b_2, \dots, b_n\}$$
*Example (Governance):* $B = \{\text{Proposal}, \text{Member}, \text{Treasury}, \text{Record}\}$

### 1.2 Modifier Set ($M$)
A finite set of $k$ operators that transform or qualify the state of a base element.
$$M = \{m_1, m_2, \dots, m_k\}$$
*Example (State):* $M = \{\text{Created}, \text{Active}, \text{Verified}, \text{Closed}\}$

### 1.3 Cache Set ($L$)
A set of logographic symbols representing high-salience concepts that bypass composition.
$$L = \{l_1, l_2, \dots, l_p\}$$
*Example (Communal):* $L = \{\text{Isusu}, \text{Burial}, \text{Levy}, \text{Omu}\}$

### 1.4 Composition Function ($\Phi$)
A mapping that generates the set of atomic tokens $T$ through the Cartesian product of $B$ and $M$.
$$\Phi: B \times M \to T$$
$$T = \{ (b, m) \mid b \in B, m \in M \}$$
The resulting token set $T$ has a maximum cardinality of $|B| \times |M|$.

### 1.5 Sequencing Grammar ($\Gamma$)
A formal grammar defining valid strings over the alphabet $\Sigma = T \cup L$.
$$\Gamma \subseteq \Sigma^*$$
A valid string $s \in \Gamma$ represents a "Path" or "Narrative" within the system.

---

## 2. Symbolic Grammar Rules

### 2.1 Recursive Composition
Tokens in $T$ can be recursively modified if the domain allows for nested states.
$$T_{n} = \Phi(T_{n-1}, M)$$
*Example:* `((Proposal, Created), Verified)`

### 2.2 Transition Constraints ($\Delta$)
Transitions between tokens are governed by a state-transition function.
$$\Delta: T \times T \to \{0, 1\}$$
If $\Delta(t_i, t_j) = 0$, the sequence $t_i \to t_j$ is invalid (e.g., a "Closed" proposal cannot transition to "Paid" without a "Verified" step).

---

## 3. Domain Mappings (V1.0)

| Domain | Base ($B$) | Modifier ($M$) | Cache ($L$) |
| :--- | :--- | :--- | :--- |
| **Governance** | Institution, Actor | Action, Permission | Levy, Burial, Road |
| **AI Research** | Source, Claim, Data | Search, Critique, Test | LitReview, Audit |
| **Narrative** | Social Role, Place | Moral State, Event | Shrine, Taboo, Oath |
| **PAGC Matrix** | Consonant (26) | Vowel (8) | Logograph (100+) |

---

## 4. Implementation Specification

### 4.1 JSON Schema Path Validator
A BMCG path is valid if and only if:
1. Every element $e \in s$ belongs to $T \cup L$.
2. For every token $(b, m) \in T$, $b \in B$ and $m \in M$.
3. All transitions $e_i \to e_{i+1}$ satisfy $\Delta$.

### 4.2 Encoding
Tokens are encoded as `base_id:modifier_id` or `logograph_id`.
*Example Governance Path:* `PROP:01 -> PROP:03 -> TREA:04 -> REC:02`

---

## 5. Research Invitation
This specification is an invitation for cross-disciplinary critique. We seek to test whether the BMCG architecture provides a more robust foundation for digital sovereignty and institutional memory than traditional unconstrained text systems.

**Contact:** *[Beaconsmith Collective / etisiobi research studio]*

**Contact:** *[Beaconsmith Collective / etisiobi research studio]*
