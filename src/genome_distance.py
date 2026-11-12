def jaccard_distance_kmers(seq1: str, seq2: str, k: int) -> float:
  set1 = set(seq1[i : i + k] for i in range(max(0, len(seq1) - k + 1)))
  set2 = set(seq2[i : i + k] for i in range(max(0, len(seq2) - k + 1)))

  kmers1 = {seq1[i : i + k] for i in range(len(seq1) - k + 1)}
  kmers2 = {seq2[i : i + k] for i in range(len(seq2) - k + 1)}

  intersection = len(kmers1.intersection(kmers2))
  union = len(kmers1.union(kmers2))

  if union == 0:
    return 1.0

  similarity = intersection / union
  return 1.0 - similarity


if __name__ == "__main__":
  s1 = "ATCGATCGATCGATCG"
  s2 = "ATCGATCGATCGATCC"
  dist = jaccard_distance_kmers(s1, s2, k=4)
  print(f"Distance de Jaccard entre s1 et s2 : {dist:.4f}")