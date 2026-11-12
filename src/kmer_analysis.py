def extract_kmers(sequence: str, k: int) -> list[str]:
  kmers = []
  if len(sequence) < k:
    return kmers
  for i in range(len(sequence) - k + 1):
    kmers.append(sequence[i : i + k])
  return kmers


def kmer_to_int(kmer: str) -> int:
  mapping = {"A": 0, "C": 1, "G": 2, "T": 3}
  val = 0
  for char in kmer.upper():
    val = (val << 2) | mapping.get(char, 0)
  return val


if __name__ == "__main__":
  dna_seq = "AGCTTCGATCGATCGTACG"
  k = 5
  kmers = extract_kmers(dna_seq, k)
  print(f"Séquence : {dna_seq}")
  print(f"K-mers (k={k}) : {kmers} (total: {len(kmers)})")