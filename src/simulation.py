import numpy as np
import hashlib

def estimate_probability(event_fn, n_trials=50000):
    # (Kode lama Anda biarkan di sini)
    successes = sum((1 for _ in range(n_trials) if event_fn()))
    return successes / n_trials

class BloomFilter:
    def __init__(self, k, m):
        self.k = k  # Jumlah fungsi hash
        self.m = m  # Ukuran bit array
        self.bit_array = np.zeros(self.m, dtype=bool)

    def add(self, item):
        for i in range(self.k):
            # Menggunakan hashlib untuk fungsi hash deterministik
            digest = hashlib.md5(f"{item}_{i}".encode()).hexdigest()
            idx = int(digest, 16) % self.m
            self.bit_array[idx] = True

    def contains(self, item):
        for i in range(self.k):
            digest = hashlib.md5(f"{item}_{i}".encode()).hexdigest()
            idx = int(digest, 16) % self.m
            if not self.bit_array[idx]:
                return False
        return True

    def theoretical_fpr(self, n):
        """
        Rumus FPR sesuai Tsun (2020) halaman 329.
        n = jumlah elemen yang dimasukkan.
        """
        return (1 - (1 - 1/self.m)**n)**self.k

def mcmc_knapsack(items, capacity, n_iter=100000):
    """
    Optimasi pemilihan issue menggunakan Markov Chain Monte Carlo (Metropolis-Hastings).
    items: list of dicts [{'weight': w, 'value': v, 'id': id}, ...]
    """
    n_items = len(items)
    weights = np.array([item['weight'] for item in items])
    values = np.array([item['value'] for item in items])
    
    current_state = np.zeros(n_items, dtype=int)
    current_value, current_weight = 0, 0
    
    best_state = current_state.copy()
    best_value = 0
    
    beta = 1.5 # Parameter pengarah eksploitasi nilai tinggi
    
    for _ in range(n_iter):
        idx = np.random.randint(n_items)
        new_state = current_state.copy()
        new_state[idx] = 1 - new_state[idx] # Flip bit
        
        new_weight = np.sum(new_state * weights)
        new_value = np.sum(new_state * values)
        
        # Tolak absolut jika melebihi kapasitas
        if new_weight > capacity:
            continue
            
        # Metropolis acceptance rule
        delta_v = new_value - current_value
        if delta_v >= 0:
            accept_prob = 1.0
        else:
            accept_prob = np.exp(beta * delta_v)
            
        if np.random.rand() < accept_prob:
            current_state = new_state
            current_weight = new_weight
            current_value = new_value
            
            if current_value > best_value:
                best_value = current_value
                best_state = current_state.copy()
                
    return {
        'best_value': best_value,
        'best_weight': np.sum(best_state * weights),
        'best_items_idx': np.where(best_state == 1)[0].tolist()
    }