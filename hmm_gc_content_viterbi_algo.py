"""
Hidden Markov Model (HMM) for DNA Sequence Analysis

Uses the Viterbi algorithm to classify DNA sequence positions
into High-GC (H) or Low-GC (L) regions.

Applications:
- CpG island detection
- Gene region identification
- Genome segmentation
"""

import math


# Emission probabilities
# H → High GC content
# L → Low GC content
H = {'A': 0.2, 'T': 0.2, 'G': 0.3, 'C': 0.3}
L = {'A': 0.3, 'T': 0.3, 'G': 0.2, 'C': 0.2}

# Convert emissions to log2 space
for base in H:
    H[base] = math.log(H[base], 2)
for base in L:
    L[base] = math.log(L[base], 2)


# Initial state probabilities
log_start_H = math.log(0.5, 2)
log_start_L = math.log(0.5, 2)


# Transition probabilities
pHH = math.log(0.5, 2)
pHL = math.log(0.5, 2)
pLH = math.log(0.4, 2)
pLL = math.log(0.6, 2)


# DNA sequence
sequence = "GGATGC"


# Viterbi DP tables
high = []
low = []


# INITIALIZATION (THIS WAS MISSING)
first_base = sequence[0]
high.append(log_start_H + H[first_base])
low.append(log_start_L + L[first_base])


# RECURSION
for i in range(1, len(sequence)):
    base = sequence[i]

    high_score = H[base] + max(
        pHH + high[i - 1],
        pLH + low[i - 1]
    )

    low_score = L[base] + max(
        pLL + low[i - 1],
        pHL + high[i - 1]
    )

    high.append(round(high_score, 3))
    low.append(round(low_score, 3))


# STATE DECODING
state_path = []
for i in range(len(sequence)):
    if high[i] > low[i]:
        state_path.append("H")
    else:
        state_path.append("L")


# OUTPUT
print("DNA Sequence:     ", sequence)
print("High-GC Scores:   ", high)
print("Low-GC Scores:    ", low)
print("Predicted States:", ''.join(state_path))

print("\nInterpretation:")
print("H → High GC content region")
print("L → Low GC content region")
