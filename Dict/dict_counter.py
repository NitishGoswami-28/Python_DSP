from collections import Counter

votes = ['A', 'B', 'A', 'C', 'B', 'A']
vote_count = Counter(votes)
winner = vote_count.most_common(1)[0][0]
print(f"The winner is: {winner}")
