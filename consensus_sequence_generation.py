"""
Consensus Sequence Generation

Description:
Generates a consensus DNA sequence from multiple aligned sequences.
If no nucleotide has majority support at a position, '*' is used.

Applications:
- Multiple sequence alignment
- Motif detection
- Comparative genomics
"""

# Input DNA sequences (must be same length)
sequences = [
    "ATCGA",
    "AACGT",
    "TTGGT",
    "CACCA"
]

# Length check 
seq_length = len(sequences[0])
assert all(len(seq) == seq_length for seq in sequences), "Sequences must be of equal length"
consensus = []

# Iterate column-wise (position by position)
for i in range(seq_length):
    column = [seq[i] for seq in sequences]

    # Count nucleotides
    if column.count('A') > len(column) // 2:
        consensus.append('A')
    elif column.count('T') > len(column) // 2:
        consensus.append('T')
    elif column.count('G') > len(column) // 2:
        consensus.append('G')
    elif column.count('C') > len(column) // 2:
        consensus.append('C')
    else:
        # No majority → ambiguous position
        consensus.append('*')
        
        
print("Consensus Sequence:", ''.join(consensus))

# Print conserved positions (non-ambiguous)
print("\nConserved Positions:")
for index, base in enumerate(consensus):
    if base != '*':
        print(f"Position {index}: {base}")
        