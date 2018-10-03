# Start - 14:45
# End   - 15:54 (with book help)
from collections import namedtuple

__all__ = ('get_biggest_subsequence',
           '_compress_same_sign')


CompSeqItem = namedtuple('CompSeqItem', ('subseq', 'val'))


def get_biggest_subsequence(seq_str):
    """assume that seq_str is comma-separated integers without any blank."""
    if not seq_str:
        return ''

    seq = map(int, seq_str.split(','))
    compressed_seq = _compress_same_sign(seq)

    if len(compressed_seq) == 1:
        if compressed_seq[0].val < 0:
            return str(max(seq))
        else:
            return seq_str

    max_sum = 0
    max_subseq = []
    curr_sum = 0
    curr_subseq = []

    for comp_seq_item in compressed_seq:
        _, val = comp_seq_item
        if curr_sum + val < 0:
            if max_sum < curr_sum:
                max_sum = curr_sum
                max_subseq = curr_subseq
                curr_sum = 0
                curr_subseq = []
        else:
            curr_sum += val
            curr_subseq.append(comp_seq_item)

    # Rightmost CompSeqItem's val in max_subseq can be negative.
    # If so, remove it from max_subseq.
    if max_subseq[-1].val < 0:
        max_sum -= max_subseq[-1].val
        max_subseq.pop()

    max_subseq = [elem for comp_seq_item in max_subseq
                  for elem in comp_seq_item.subseq]
    return max_sum, ','.join(map(str, max_subseq))


def _compress_same_sign(seq):
    is_positive_subseq = None
    curr_subseq = []
    compressed_seq = []
    for elem in seq:
        if not curr_subseq:
            # First iteration
            curr_subseq.append(elem)
            is_positive_subseq = (elem >= 0)
        else:
            if is_positive_subseq == (elem >= 0):
                curr_subseq.append(elem)
            else:
                compressed_seq.append(CompSeqItem(curr_subseq, sum(curr_subseq)))
                curr_subseq = [elem]
                is_positive_subseq = (elem >= 0)
    if curr_subseq:
        compressed_seq.append(CompSeqItem(curr_subseq, sum(curr_subseq)))
    return compressed_seq
