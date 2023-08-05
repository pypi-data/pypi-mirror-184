import numpy as np

# assume dones[5] is terminated and resulted in the terminated observation of obs5
rewards = np.array([1, 0.1, 0.01, 0.001, 0.0001, 2, 0.1, 0.01,]).reshape(-1, 1)
dones = np.array([0, 0, 0, 0, 0, 1, 0, 0]).reshape(-1, 1)
gamma = 1.0
num_steps = 8
next_done = 0
next_value = 0.0005 # value of obs8
returns = np.zeros_like(rewards)
for t in reversed(range(num_steps)): 
    if t == num_steps - 1: 
        nextnonterminal = 1.0 - next_done 
        next_return = next_value 
    else: 
        nextnonterminal = 1.0 - dones[t + 1] 
        next_return = returns[t + 1] 
    returns[t] = rewards[t] + gamma * nextnonterminal * next_return
print(list(returns))


# assume dones[5] is truncated and resulted in the truncated observation of obs5
rewards = np.array([1, 0.1, 0.01, 0.001, 0.0001, 2, 0.1, 0.01,]).reshape(-1, 1)
dones = np.array([0, 0, 0, 0, 0, 1, 0, 0]).reshape(-1, 1)
v_obs_5 = 0.0008
rewards[4] += v_obs_5
next_done = 0
next_value = 0.0005 # value of obs8
returns = np.zeros_like(rewards)
for t in reversed(range(num_steps)): 
    if t == num_steps - 1: 
        nextnonterminal = 1.0 - next_done 
        next_return = next_value 
    else: 
        nextnonterminal = 1.0 - dones[t + 1] 
        next_return = returns[t + 1] 
    returns[t] = rewards[t] + gamma * nextnonterminal * next_return

print(list(returns))


