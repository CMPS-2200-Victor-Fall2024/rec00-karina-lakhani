    #Recitation0


'''In this recitation, you will complete the Knuth-Morris-Pratt string matching algorithm.
I wrote the function compute_table, which tells you how much to shift the gene when a mismatch is found.
You must complete the algorithm by completing the function, kmp.
'''
def compute_table(gene):
    '''Compute the KMP table (also known as the partial match or failure function) for the given gene (pattern).'''
    m = len(gene)
    table = [0] * m
    j = 0  

    for i in range(1, m):
        while j > 0 and gene[i] != gene[j]:
            j = table[j - 1]
        if gene[i] == gene[j]:
            j += 1
        table[i] = j

    return table

def kmp(gene, genome):
    '''KMP string matching algorithm.'''
    if not gene:
        return True  
    
    n = len(genome)
    m = len(gene)
    
    table = compute_table(gene)
    j = 0  
    
    for i in range(n):  
        while j > 0 and genome[i] != gene[j]:
            j = table[j - 1]
        if genome[i] == gene[j]:
            j += 1
        if j == m:
            return True
    
    return False

def test_compute_table():
    gene = "abcabcacab"
    ideal_answer = [0, 0, 1, 2, 3, 4, 5, 6, 7, 8]
    result = compute_table(gene)
    assert result == ideal_answer, f"Expected {ideal_answer}, got {result}"
    print("compute_table test passed")

def test_kmp():
    '''
    Do not modify this code. Make sure that this test passes before pushing your code to github.
    '''
    genes = ["", "a", "t", "att", "cat", "catacatttcat", "ggggaa", "atatatatat", "aaaat", "aaaa"]
    genomes = ["", "a", "catacattaccattacgaccag", "atgcacattatatatatatgcatat", "gggggggaaaaaaaa", "aaa", "taaa"]

    for gene in genes:
        for genome in genomes:
            assert kmp(gene, genome) == (gene in genome), f"Failed for gene: '{gene}' and genome: '{genome}'"
    print("kmp test passed")

# Run the tests
test_compute_table()
test_kmp()
