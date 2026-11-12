# Genomic Alignment-Free & K-mer Analysis Toolset

## Project Overview
This project explores sequence analysis and probabilistic data structures for genomics. Traditional sequence alignment can be computationally expensive for massive genomic datasets; this repository implements high-performance approaches using k-mer decomposition, Jaccard distance metrics, and Bloom filtersn.

## Core Modules (src/)
* **kmer_analysis.py**: Sliding-window k-mer extraction from biological DNA strings and numerical encoding representations.
* **genome_distance.py**: Genome comparison tool calculating Jaccard distances derived from k-mer set intersections and unions.
* **bloom_filter.py**: Implements a Bloom filter tailored for testing $k$-mer presence in large sequence collections without storing full datasets in memory.

_Note: The project is currently in progress._
