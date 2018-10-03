from main import get_biggest_subsequence, _compress_same_sign


def test_compress_same_sign():
    seq = [2, 3, -8, -1, 2, 4, -2, 3]
    compressed_seq = _compress_same_sign(seq)
    expected = '5,-9,6,-2,3'
    assert expected == ','.join(map(str, [val for _, val in compressed_seq]))


def test_one():
    seq = '2,-8,3,-2,4,-10'
    sum, subseq = get_biggest_subsequence(seq)
    assert sum == 5
    assert subseq == '3,-2,4'
