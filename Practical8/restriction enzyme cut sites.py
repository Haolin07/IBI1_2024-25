def restriction_enzyme_cut(sequence,recognised_sequence):
    """
    find the enzyme recongnise sequence
    parameters: 
        sequence:the DNA sequence to be cut
        recognised_sequence: the enzyme recognise sequence
    return:
        point: the location of the first nucleotide
    error:
        return error if the sequence not only contains ACGT 
    """
    #find if there is a error
    if not set(sequence).issubset({'A', 'C', 'G', 'T'}):
        raise ValueError("The DNA sequence contains non-standard nucleotide")
    if not set(recognised_sequence).issubset({'A', 'C', 'G', 'T'}):
        raise ValueError("The recognised DNA sequence contains non-standard nucleotide")
    #find the cut point
    global point
    point=[]
    location=sequence.find(recognised_sequence)
    if location != -1:
        point.append(location)
    else:
        print("no recognised sequence")
    return point
##example
seq="ATCGATCGTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGC"
restriction_enzyme_cut(seq,"GCTAGC")
print(point)