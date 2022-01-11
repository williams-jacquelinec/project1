# DNA -> RNA Transcription


def transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA by generating
    the complement sequence with T -> U replacement
    """
    seq_list = list(seq)
    for i in range(len(seq_list)):
        if seq_list[i] == 'A':
            seq_list[i] = 'U'
        elif seq_list[i] == 'T':
            seq_list[i] = 'A'
        elif seq_list[i] == 'C':
            seq_list[i] = 'G'
        else:
            seq_list[i] = 'C'

    transcribe_str = ''.join(seq_list)
    return transcribe_str


def reverse_transcribe(seq: str) -> str:
    """
    transcribes DNA to RNA then reverses
    the strand
    """
    rev_transcribe_str = transcribe(seq)
    rev_list = list(rev_transcribe_str)
    for i in range(len(rev_list)):
        if rev_list[i] == 'A':
            rev_list[i] = 'U'
        elif rev_list[i] == 'U':
            rev_list[i] = 'A'
        elif rev_list[i] == 'C':
            rev_list[i] = 'G'
        else:
            rev_list[i] = 'C'
    
    final_str = ''.join(rev_list)
    return final_str
