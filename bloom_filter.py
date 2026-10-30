from numpy import zeros
from random import randint

K = 8
BLOOM_FILTER_CAPACITY = 64
NUMBER_OF_HASH_FUNCTIONS = 4
NUMBER_OF_KMERS_IN_COLLECTION = 8

#Hash XOR >> shift function
def kmer_hash(encoded_kmer:int, shift:int):
    shifted_kmer = encoded_kmer >> shift
    hashed_kmer = encoded_kmer^shifted_kmer
    return hashed_kmer

#Bloom Filter class
class BloomFilter:
    def __init__(self, m:int, k:int):
        self.k = k #number of hash functions
        self.m = m #capacity
        self.bit_array = zeros(m)

    def populate_bloom_filter(self, kmer:int):
        for i in range(self.k):
            hashed_kmer = kmer_hash(kmer, i)
            self.bit_array[hashed_kmer%self.m] = 1

    def match_kmer(self, kmer:int):
        is_a_match = True
        i=1
        while is_a_match and i<self.k:
            hashed_kmer=kmer_hash(kmer,i)
            is_a_match &= self.bit_array[hashed_kmer%self.m] == 1
            i+=1
        return is_a_match

#Randomly generated kmer list to populate bloom filter
def generate_kmer_list(kmer_number:int, k=K):
    kmer_list = []
    for i in range(kmer_number):
        kmer_list.append(randint(0, 2**(k-1)))
    return kmer_list




generated_kmer_collection = generate_kmer_list(NUMBER_OF_KMERS_IN_COLLECTION, K)
print(f'Randomly generated list of K-mers: {generated_kmer_collection}')

bloom_filter = BloomFilter(BLOOM_FILTER_CAPACITY,NUMBER_OF_HASH_FUNCTIONS)

for kmer in generated_kmer_collection :
    BloomFilter.populate_bloom_filter(bloom_filter, kmer)

print(f'Bloom filter populated with collection : {bloom_filter.bit_array}')

new_kmer = generated_kmer_collection[2]
print(f'Testing match with K-mer : {new_kmer}')

is_a_match = BloomFilter.match_kmer(bloom_filter, new_kmer)

if is_a_match:
    print('New K-mer is likely to be in the collection.')
else :
    print('New K-mer is not in the collection.')
