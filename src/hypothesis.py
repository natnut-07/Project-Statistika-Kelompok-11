import numpy as np
from scipy import stats

def z_test_one_sample(x_bar, mu0, sigma, n, alternative='two-sided', alpha=0.05):
    # Rumus Z-statistik
    z_stat = (x_bar - mu0) / (sigma / np.sqrt(n))
    
    if alternative == 'two-sided':
        p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))
    else:
        p_value = 1 - stats.norm.cdf(z_stat)
    
    return {
        "z_stat": round(z_stat, 4),
        "p_value": round(p_value, 4),
        "decision": "Reject H₀" if p_value < alpha else "Fail to reject H₀"
    }