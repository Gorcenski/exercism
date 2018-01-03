def to_rna(dna_strand):

    def compliment(protein):
        transcription = {'C': 'G', 'G': 'C',
                         'T': 'A', 'A': 'U'}
        if protein in transcription:
            return transcription[protein]
        else:
            raise ValueError('Unspecified protein {} found'.format(protein))

    return ''.join([compliment(p) for p in dna_strand])
