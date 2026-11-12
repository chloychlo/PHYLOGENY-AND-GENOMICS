# Genomic Alignment-Free & K-mer Analysis Toolset

## Project Overview
This project explores **alignment-free sequence analysis** and probabilistic data structures for genomics and phylogenetics. Traditional sequence alignment can be computationally expensive for massive genomic datasets; this repository implements alternative, high-performance approaches using $k$-mer decomposition, Jaccard distance metrics, and Bloom filters for efficient sequence membership and comparison.

---

## Repos Structure

```text
genomics-kmer-phylogeny/
├── src/                     # Core source code modules
│   ├── __init__.py
│   ├── bloom_filter.py      # Probabilistic data structure for k-mer membership
│   ├── kmer_analysis.py     # Extraction and manipulation of k-mers from DNA sequences
│   └── genome_distance.py   # Alignment-free distance metrics (e.g., Jaccard distance)
├── requirements.txt         # Project Python dependencies
└── README.md                # Project documentation
```

## Core Modules (src/)
* **kmer_analysis.py**: Sliding-window k-mer extraction from biological DNA strings and numerical encoding representations.
* **genome_distance.py**: Genome comparison tool calculating Jaccard distances derived from k-mer set intersections and unions.
* **bloom_filter.py**: Implements a Bloom filter tailored for testing $k$-mer presence in large sequence collections without storing full datasets in memory.
