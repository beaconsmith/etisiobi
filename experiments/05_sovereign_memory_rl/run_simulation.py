"""
Sovereign Memory RL Agent Simulation (Mock)
===========================================

Testing Balaji/LeCun's "Memory as Direction" hypothesis.

This script simulates a reinforcement learning environment where the rules
periodically shift (non-stationary environment). We compare two agents:

1. Agent A (Unbounded Memory): Remembers all past states perfectly. 
2. Agent B (PAGC Sovereign Memory): Is constrained to encode its memory 
   through a 27x8 (216 token) structure. It forces "programmable forgetting"
   of noise and prioritizes a "moral/survival cache".

Hypothesis: Agent B adapts faster to rule shifts because its memory is 
already compressed into higher-order invariants, preventing it from 
overfitting to obsolete historical data.

This is a conceptual mock to demonstrate the architecture for the paper.
"""

import numpy as np
import random
import time
from pathlib import Path

# Setup paths
RESULTS_DIR = Path(__file__).parent / "results"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)


class Environment:
    """A non-stationary environment with shifting reward rules."""
    def __init__(self, states=1000):
        self.num_states = states
        self.current_rule = "A" # Shifts to "B" midway
        self.step_count = 0
        
    def get_reward(self, state, action):
        # We define a complex underlying state space.
        # But there is a hidden, simple invariant (e.g., states divisible by 27 are "safe").
        
        is_safe_invariant = (state % 27) == 0
        
        if self.current_rule == "A":
            # Rule A: Invariants are good, but there's a lot of noisy specific state rewards
            if is_safe_invariant and action == 1:
                return 10
            elif state % 5 == 0 and action == 0:
                return 5
            return -1
        else:
            # Rule B: Environment shifted! All the noisy specific states changed polarity,
            # but the underlying invariant (divide by 27) remains the same.
            if is_safe_invariant and action == 1:
                return 10
            elif state % 5 == 0 and action == 0:
                return -5 # Punishment now!
            return -1

    def step(self):
        self.step_count += 1
        if self.step_count == 5000:
            print(">>> ENVIRONMENT SHIFT: Shifted to Rule B (Noise polarity reversed) <<<")
            self.current_rule = "B"
        return random.randint(0, self.num_states - 1)


class UnboundedAgent:
    """Agent A: Memorizes exact states and best actions."""
    def __init__(self):
        self.q_table = {} # Dict of {state: [q0, q1]}
        self.alpha = 0.1
        self.gamma = 0.9

    def choose_action(self, state, epsilon=0.1):
        if state not in self.q_table:
            self.q_table[state] = [0.0, 0.0]
        if random.random() < epsilon:
            return random.choice([0, 1])
        return int(np.argmax(self.q_table[state]))

    def learn(self, state, action, reward, next_state):
        if next_state not in self.q_table:
            self.q_table[next_state] = [0.0, 0.0]
        best_future = np.max(self.q_table[next_state])
        self.q_table[state][action] = (1 - self.alpha) * self.q_table[state][action] + \
                                      self.alpha * (reward + self.gamma * best_future)


class PAGC_SovereignAgent:
    """
    Agent B: Has a strict 216-token (27x8) memory bottleneck.
    It cannot memorize the 1000 underlying states. It maps everything into 216 buckets.
    """
    def __init__(self):
        self.q_table = np.zeros((216, 2)) # Strictly constrained memory space
        self.alpha = 0.1
        self.gamma = 0.9

    def _encode_state(self, raw_state):
        # The agent naturally "sees as" via a fixed structural mapping.
        # It collapses the 1000 states into 216.
        # It naturally retains the invariant (modulo 27) via its base symbols.
        base_symbol = raw_state % 27
        modifier = (raw_state // 27) % 8
        return (modifier * 27) + base_symbol # Index 0 to 215

    def choose_action(self, raw_state, epsilon=0.1):
        state_encoded = self._encode_state(raw_state)
        if random.random() < epsilon:
            return random.choice([0, 1])
        return int(np.argmax(self.q_table[state_encoded]))

    def learn(self, raw_state, action, reward, next_raw_state):
        s = self._encode_state(raw_state)
        next_s = self._encode_state(next_raw_state)
        best_future = np.max(self.q_table[next_s])
        self.q_table[s][action] = (1 - self.alpha) * self.q_table[s][action] + \
                                  self.alpha * (reward + self.gamma * best_future)


def run_simulation():
    env = Environment(states=1000)
    agent_a = UnboundedAgent()
    agent_b = PAGC_SovereignAgent()

    rewards_a = []
    rewards_b = []

    print("=====================================================")
    print("Sovereign Memory vs Unbounded Memory Simulation")
    print("=====================================================\n")

    state = env.step()
    
    # Track rolling averages
    rolling_a = 0
    rolling_b = 0

    for step in range(1, 10001):
        action_a = agent_a.choose_action(state)
        action_b = agent_b.choose_action(state)

        r_a = env.get_reward(state, action_a)
        r_b = env.get_reward(state, action_b)

        next_state = env.step()

        agent_a.learn(state, action_a, r_a, next_state)
        agent_b.learn(state, action_b, r_b, next_state)

        state = next_state

        rolling_a = 0.99 * rolling_a + 0.01 * r_a
        rolling_b = 0.99 * rolling_b + 0.01 * r_b
        
        if step % 1000 == 0:
            print(f"Step {step:5d} | Unbounded Agent Avg: {rolling_a:5.2f} | PAGC Agent Avg: {rolling_b:5.2f}")
            rewards_a.append(rolling_a)
            rewards_b.append(rolling_b)

    generate_plots(rewards_a, rewards_b)

def generate_plots(a_hist, b_hist):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 6))
    plt.plot(range(1000, 11000, 1000), a_hist, marker='o', label="Agent A (Unbounded Memory)")
    plt.plot(range(1000, 11000, 1000), b_hist, marker='s', label="Agent B (PAGC 216-Token Memory)")
    plt.axvline(5000, color='red', linestyle='--', label="Environment Rule Shift")
    
    plt.title("Adaptation after Environmental Shift:\nPAGC Directional Memory vs Unbounded Memory")
    plt.xlabel("Steps")
    plt.ylabel("Rolling Average Reward")
    plt.legend()
    plt.grid(True, alpha=0.3)

    out_path = RESULTS_DIR / "sovereign_memory_adaptation.png"
    plt.savefig(out_path)
    plt.close()
    print(f"\n[+] Simulation complete. Falsification chart saved to: {out_path}")


if __name__ == "__main__":
    run_simulation()
