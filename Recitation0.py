    #Recitation0


'''In this recitation, you will complete the Knuth-Morris-Pratt string matching algorithm.
I wrote the function compute_table, which tells you how much to shift the gene when a mismatch is found.
You must complete the algorithm by completing the function, kmp.
'''
def compute_table(gene):
    
    table = [0] * len(gene)
    j = 0
    for i in range(1, len(gene)):
        while j > 0 and gene[i] != gene[j]:
            j = table[j - 1]
        if gene[i] == gene[j]:
            j += 1
        table[i] = j
    return table

def kmp(gene, genome):
   
    if not gene:
        return True  
    
    n = len(genome)
    m = len(gene)
    
    table = compute_table(gene)
    j = 0  # index for gene
    
    for i in range(n):  # index for genome
        while j > 0 and genome[i] != gene[j]:
            j = table[j - 1]
        if genome[i] == gene[j]:
            j += 1
        if j == m:
            return True
    
    return False

def test_compute_table():
    gene = "abcabcacab"
    print(compute_table(gene))
    ideal_answer = [j - i + 1 for j, i in enumerate([0, 1, 1, 0, 1, 1, 0, 5, 0, 1])]
    assert compute_table(gene) == ideal_answer

def test_kmp():
    '''
    Do not modify this code. Make sure that this test passes before pushing your code to github.
    '''
    genes = ["", "a", "t", "att", "cat", "catacatttcat", "ggggaa", "atatatatat", "aaaat", "aaaa"]
    genomes = ["", "a", "catacattaccattacgaccag", "atgcacattatatatatatgcatat", "gggggggaaaaaaaa", "aaa", "taaa"]

    for gene in genes:
        for genome in genomes: # tests every pair of gene and genome.
            assert kmp(gene, genome) == (gene in genome)  # asserts that the kmp function returns the same value as the builtin 'in' function.

# Run the tests
test_compute_table()
test_kmp()
