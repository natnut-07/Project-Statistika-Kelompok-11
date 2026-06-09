import numpy as np
import hashlib

def estimate_probability(event_fn, n_trials=50000):
    r"""
    Menghitung estimasi probabilitas menggunakan simulasi Monte Carlo.
    
    Referensi:
        Tsun (2020)
        
    Parameters:
        event_fn (callable): Fungsi yang mengembalikan True jika event terjadi, False jika tidak.
        n_trials (int): Jumlah iterasi simulasi.
        
    Returns:
        float: Estimasi probabilitas kejadian.
    """
    successes = sum(1 for _ in range(n_trials) if event_fn())
    return successes / n_trials


class BloomFilter:
    r"""
    Implementasi struktur data probabilistik Bloom Filter untuk efisiensi memori.
    
    Referensi Formula FPR:
        (1 - (1 - 1/m)**n)**k (Tsun, 2020, Halaman 329)
    """
    def __init__(self, k, m):
        self.k = k
        self.m = m
        self.bit_array = np.zeros(m, dtype=bool)

    def _hashes(self, item):
        """Menghasilkan k nilai hash untuk sebuah item."""
        hashes = []
        for i in range(self.k):
            # Menggunakan salt yang berbeda untuk setiap fungsi hash
            hash_object = hashlib.md5((str(item) + str(i)).encode())
            hashes.append(int(hash_object.hexdigest(), 16) % self.m)
        return hashes

    def add(self, item):
        """Menambahkan item ke dalam Bloom Filter."""
        for h in self._hashes(item):
            self.bit_array[h] = True

    def contains(self, item):
        """Memeriksa apakah item mungkin ada di dalam himpunan."""
        for h in self._hashes(item):
            if not self.bit_array[h]:
                return False
        return True

    def theoretical_fpr(self, n):
        """Menghitung Theoretical False Positive Rate."""
        return (1 - (1 - 1 / self.m)**n)**self.k


def mcmc_knapsack(items, capacity, n_iter=100000):
    r"""
    Menyelesaikan problem Knapsack menggunakan pendekatan Markov Chain Monte Carlo (MCMC).
    Digunakan untuk optimasi prioritas pengerjaan bug berdasarkan waktu (weight) dan severity (value).
    
    Referensi:
        Tsun (2020)
        
    Parameters:
        items (list of dict): Daftar dictionary dengan key 'weight' dan 'value'.
        capacity (float/int): Kapasitas maksimal (misal: total jam kerja).
        n_iter (int): Jumlah iterasi MCMC.
        
    Returns:
        dict: Solusi terbaik yang ditemukan berisi 'max_value', 'total_weight', dan 'best_state'.
    """
    n_items = len(items)
    
    # State awal: array boolean acak (diambil/tidak)
    current_state = np.random.choice([False, True], size=n_items)
    
    def evaluate(state):
        w = sum(items[i]['weight'] for i in range(n_items) if state[i])
        v = sum(items[i]['value'] for i in range(n_items) if state[i])
        return w, v

    # Pastikan state awal valid
    current_w, current_v = evaluate(current_state)
    while current_w > capacity:
        current_state = np.random.choice([False, True], size=n_items)
        current_w, current_v = evaluate(current_state)

    best_state = current_state.copy()
    best_v = current_v
    best_w = current_w

    for _ in range(n_iter):
        # Proposal: balikkan (flip) satu state secara acak
        proposal_state = current_state.copy()
        flip_idx = np.random.randint(n_items)
        proposal_state[flip_idx] = not proposal_state[flip_idx]
        
        prop_w, prop_v = evaluate(proposal_state)
        
        # Aturan transisi (Hill Climbing / Simplified Metropolis)
        if prop_w <= capacity:
            if prop_v >= current_v:
                current_state = proposal_state
                current_v = prop_v
                current_w = prop_w
                # Update best state
                if current_v > best_v:
                    best_v = current_v
                    best_w = current_w
                    best_state = current_state.copy()
            else:
                # Stochastic acceptance untuk menghindari local optima
                acceptance_prob = np.exp((prop_v - current_v) / 1.0) # Suhu konstan
                if np.random.rand() < acceptance_prob:
                    current_state = proposal_state
                    current_v = prop_v
                    current_w = prop_w

    return {
        'max_value': best_v,
        'total_weight': best_w,
        'best_state': best_state.tolist()
    }