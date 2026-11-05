# Phylogeny and genomics

This repository contains computational approaches to genomic sequence analysis.

## Bloom filter 
**bloom_filter.py**

The goal of this code is to check if a K-mer exists in a collection by using a Bloom Filter.
- Define hash functions
- Create an empty Bloom Filter
- Populate the Bloom Filter with a randomly generated list of K-mers
- Generate a new K-mer
- Check if the K-mer can be the collection or not

Guide :

* _kmer_hash function_ : hash function using the XOR>>shift principle. Different hash functions are provided to the Bloom filter by using different shift values

* _BloomFilter class_ : 
  * attributes : capacity, number of hash functions, bit array
  * methods : populate bloom filter using list of K-mers, check if new K-mer matches the collection

* _generate_kmer_list function_ : randomly generates a list of K-mers, each K-mer being represented by an integer
