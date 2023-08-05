#!/usr/bin/python3
import copy

from bitstring import BitArray


class SHA2:
    """
    Family of SHA2 hash functions
    """
    Constants_256 = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
                     0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
                     0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
                     0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
                     0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
                     0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
                     0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
                     0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]

    Constants_512 = [0x428a2f98d728ae22, 0x7137449123ef65cd, 0xb5c0fbcfec4d3b2f, 0xe9b5dba58189dbbc,
                     0x3956c25bf348b538, 0x59f111f1b605d019, 0x923f82a4af194f9b, 0xab1c5ed5da6d8118,
                     0xd807aa98a3030242, 0x12835b0145706fbe, 0x243185be4ee4b28c, 0x550c7dc3d5ffb4e2,
                     0x72be5d74f27b896f, 0x80deb1fe3b1696b1, 0x9bdc06a725c71235, 0xc19bf174cf692694,
                     0xe49b69c19ef14ad2, 0xefbe4786384f25e3, 0x0fc19dc68b8cd5b5, 0x240ca1cc77ac9c65,
                     0x2de92c6f592b0275, 0x4a7484aa6ea6e483, 0x5cb0a9dcbd41fbd4, 0x76f988da831153b5,
                     0x983e5152ee66dfab, 0xa831c66d2db43210, 0xb00327c898fb213f, 0xbf597fc7beef0ee4,
                     0xc6e00bf33da88fc2, 0xd5a79147930aa725, 0x06ca6351e003826f, 0x142929670a0e6e70,
                     0x27b70a8546d22ffc, 0x2e1b21385c26c926, 0x4d2c6dfc5ac42aed, 0x53380d139d95b3df,
                     0x650a73548baf63de, 0x766a0abb3c77b2a8, 0x81c2c92e47edaee6, 0x92722c851482353b,
                     0xa2bfe8a14cf10364, 0xa81a664bbc423001, 0xc24b8b70d0f89791, 0xc76c51a30654be30,
                     0xd192e819d6ef5218, 0xd69906245565a910, 0xf40e35855771202a, 0x106aa07032bbd1b8,
                     0x19a4c116b8d2d0c8, 0x1e376c085141ab53, 0x2748774cdf8eeb99, 0x34b0bcb5e19b48a8,
                     0x391c0cb3c5c95a63, 0x4ed8aa4ae3418acb, 0x5b9cca4f7763e373, 0x682e6ff3d6b2b8a3,
                     0x748f82ee5defb2fc, 0x78a5636f43172f60, 0x84c87814a1f0ab72, 0x8cc702081a6439ec,
                     0x90befffa23631e28, 0xa4506cebde82bde9, 0xbef9a3f7b2c67915, 0xc67178f2e372532b,
                     0xca273eceea26619c, 0xd186b8c721c0c207, 0xeada7dd6cde0eb1e, 0xf57d4f7fee6ed178,
                     0x06f067aa72176fba, 0x0a637dc5a2c898a6, 0x113f9804bef90dae, 0x1b710b35131c471b,
                     0x28db77f523047d84, 0x32caab7b40c72493, 0x3c9ebe0a15c9bebc, 0x431d67c49c100d4c,
                     0x4cc5d4becb3e42b6, 0x597f299cfc657e2a, 0x5fcb6fab3ad6faec, 0x6c44198c4a475817]

    @staticmethod
    def hash_sha224(msg):
        h0 = BitArray(uint=0xC1059ED8, length=32)
        h1 = BitArray(uint=0x367cd507, length=32)
        h2 = BitArray(uint=0x3070dd17, length=32)
        h3 = BitArray(uint=0xf70e5939, length=32)
        h4 = BitArray(uint=0xffc00b31, length=32)
        h5 = BitArray(uint=0x68581511, length=32)
        h6 = BitArray(uint=0x64f98fa7, length=32)
        h7 = BitArray(uint=0xbefa4fa4, length=32)

        bit_msg = BitArray(msg)
        len_msg = len(bit_msg)
        bit_msg += BitArray(bin='1')
        k = (448 - (len_msg + 1)) % 512
        bit_msg += BitArray(bin='0' * k)
        bit_msg += BitArray(int=len_msg, length=64)
        num_chunks = len(bit_msg) // 512
        assert len(bit_msg) % 512 == 0

        bit_msg_chunks = list(bit_msg[512 * num_chunk:
                                      512 * (num_chunk + 1)]
                              for num_chunk in range(num_chunks))
        for bit_msg_chunk in bit_msg_chunks:
            msg_sub_chunks = list(bit_msg_chunk[32 * num_chunk:
                                                32 * (num_chunk + 1)]
                                  for num_chunk in range(16))
            for i in range(16, 64):
                chunk_i_15 = msg_sub_chunks[i - 15]
                temp0 = copy.deepcopy(chunk_i_15)
                temp0.ror(7)
                temp1 = copy.deepcopy(chunk_i_15)
                temp1.ror(18)
                temp2 = copy.deepcopy(chunk_i_15)
                temp2 = temp2 >> 3
                s0 = temp0 ^ temp1 ^ temp2

                chunk_i_2 = msg_sub_chunks[i - 2]
                temp0 = copy.deepcopy(chunk_i_2)
                temp0.ror(17)
                temp1 = copy.deepcopy(chunk_i_2)
                temp1.ror(19)
                temp2 = copy.deepcopy(chunk_i_2)
                temp2 = temp2 >> 10
                s1 = temp0 ^ temp1 ^ temp2

                msg_sub_chunks.append(BitArray(
                    uint=(msg_sub_chunks[i - 16].uint + s0.uint + msg_sub_chunks[i - 7].uint + s1.uint) % (2 ** 32),
                    length=32))

            a = copy.deepcopy(h0)
            b = copy.deepcopy(h1)
            c = copy.deepcopy(h2)
            d = copy.deepcopy(h3)
            e = copy.deepcopy(h4)
            f = copy.deepcopy(h5)
            g = copy.deepcopy(h6)
            h = copy.deepcopy(h7)

            for i in range(0, 64):
                temp0 = copy.deepcopy(a)
                temp0.ror(2)
                temp1 = copy.deepcopy(a)
                temp1.ror(13)
                temp2 = copy.deepcopy(a)
                temp2.ror(22)
                Sum0 = temp0 ^ temp1 ^ temp2

                Ma = (a & b) ^ (a & c) ^ (b & c)

                t2 = BitArray(uint=(Sum0.uint + Ma.uint) % (2 ** 32),
                              length=32)

                temp0 = copy.deepcopy(e)
                temp0.ror(6)
                temp1 = copy.deepcopy(e)
                temp1.ror(11)
                temp2 = copy.deepcopy(e)
                temp2.ror(25)
                Sum1 = temp0 ^ temp1 ^ temp2

                temp0 = e & f
                temp1 = ~e
                temp2 = copy.deepcopy(g)
                Ch = temp0 ^ (temp1 & temp2)

                t1 = BitArray(
                    uint=(h.uint + Sum1.uint + Ch.uint + SHA2.Constants_256[i] + msg_sub_chunks[i].uint) % (2 ** 32),
                    length=32)

                h = copy.deepcopy(g)
                g = copy.deepcopy(f)
                f = copy.deepcopy(e)
                e = BitArray(uint=(d.uint + t1.uint) % (2 ** 32),
                             length=32)
                d = copy.deepcopy(c)
                c = copy.deepcopy(b)
                b = copy.deepcopy(a)
                a = BitArray(uint=(t1.uint + t2.uint) % (2 ** 32),
                             length=32)

            h0 = BitArray(uint=(h0.uint + a.uint) % (2 ** 32),
                          length=32)
            h1 = BitArray(uint=(h1.uint + b.uint) % (2 ** 32),
                          length=32)
            h2 = BitArray(uint=(h2.uint + c.uint) % (2 ** 32),
                          length=32)
            h3 = BitArray(uint=(h3.uint + d.uint) % (2 ** 32),
                          length=32)
            h4 = BitArray(uint=(h4.uint + e.uint) % (2 ** 32),
                          length=32)
            h5 = BitArray(uint=(h5.uint + f.uint) % (2 ** 32),
                          length=32)
            h6 = BitArray(uint=(h6.uint + g.uint) % (2 ** 32),
                          length=32)
            h7 = BitArray(uint=(h7.uint + h.uint) % (2 ** 32),
                          length=32)

        hash = h0 + h1 + h2 + h3 + h4 + h5 + h6
        return hash.tobytes()

    @staticmethod
    def hash_sha256(msg):



        h0 = BitArray(uint=0x6a09e667, length=32)
        h1 = BitArray(uint=0xbb67ae85, length=32)
        h2 = BitArray(uint=0x3c6ef372, length=32)
        h3 = BitArray(uint=0xa54ff53a, length=32)
        h4 = BitArray(uint=0x510e527f, length=32)
        h5 = BitArray(uint=0x9b05688c, length=32)
        h6 = BitArray(uint=0x1f83d9ab, length=32)
        h7 = BitArray(uint=0x5be0cd19, length=32)

        bit_msg = BitArray(msg)
        len_msg = len(bit_msg)
        bit_msg += BitArray(bin='1')
        k = (448 - (len_msg + 1)) % 512
        bit_msg += BitArray(bin='0'*k)
        bit_msg += BitArray(int=len_msg, length=64)
        num_chunks = len(bit_msg) // 512
        assert len(bit_msg) % 512 == 0

        bit_msg_chunks = list(bit_msg[512 * num_chunk:
                                      512 * (num_chunk + 1)]
                              for num_chunk in range(num_chunks))
        for bit_msg_chunk in bit_msg_chunks:
            msg_sub_chunks = list(bit_msg_chunk[32 * num_chunk:
                                                32 * (num_chunk + 1)]
                                  for num_chunk in range(16))
            for i in range(16, 64):
                chunk_i_15 = msg_sub_chunks[i-15]
                temp0 = copy.deepcopy(chunk_i_15)
                temp0.ror(7)
                temp1 = copy.deepcopy(chunk_i_15)
                temp1.ror(18)
                temp2 = copy.deepcopy(chunk_i_15)
                temp2 = temp2 >> 3
                s0 = temp0 ^ temp1 ^ temp2

                chunk_i_2 = msg_sub_chunks[i-2]
                temp0 = copy.deepcopy(chunk_i_2)
                temp0.ror(17)
                temp1 = copy.deepcopy(chunk_i_2)
                temp1.ror(19)
                temp2 = copy.deepcopy(chunk_i_2)
                temp2 = temp2 >> 10
                s1 = temp0 ^ temp1 ^ temp2

                msg_sub_chunks.append(BitArray(uint=(msg_sub_chunks[i-16].uint + s0.uint + msg_sub_chunks[i-7].uint + s1.uint) % (2 ** 32),
                                       length=32))

            a = copy.deepcopy(h0)
            b = copy.deepcopy(h1)
            c = copy.deepcopy(h2)
            d = copy.deepcopy(h3)
            e = copy.deepcopy(h4)
            f = copy.deepcopy(h5)
            g = copy.deepcopy(h6)
            h = copy.deepcopy(h7)

            for i in range(0, 64):
                temp0 = copy.deepcopy(a)
                temp0.ror(2)
                temp1 = copy.deepcopy(a)
                temp1.ror(13)
                temp2 = copy.deepcopy(a)
                temp2.ror(22)
                Sum0 = temp0 ^ temp1 ^ temp2

                Ma = (a & b) ^ (a & c) ^ (b & c)

                t2 = BitArray(uint=(Sum0.uint + Ma.uint) % (2 ** 32),
                              length=32)

                temp0 = copy.deepcopy(e)
                temp0.ror(6)
                temp1 = copy.deepcopy(e)
                temp1.ror(11)
                temp2 = copy.deepcopy(e)
                temp2.ror(25)
                Sum1 = temp0 ^ temp1 ^ temp2

                temp0 = e & f
                temp1 = ~e
                temp2 = copy.deepcopy(g)
                Ch = temp0 ^ (temp1 & temp2)

                t1 = BitArray(uint=(h.uint + Sum1.uint + Ch.uint + SHA2.Constants_256[i] + msg_sub_chunks[i].uint) % (2 ** 32),
                              length=32)

                h = copy.deepcopy(g)
                g = copy.deepcopy(f)
                f = copy.deepcopy(e)
                e = BitArray(uint=(d.uint + t1.uint) % (2 ** 32),
                             length=32)
                d = copy.deepcopy(c)
                c = copy.deepcopy(b)
                b = copy.deepcopy(a)
                a = BitArray(uint=(t1.uint + t2.uint) % (2 ** 32),
                             length=32)

            h0 = BitArray(uint=(h0.uint + a.uint) % (2 ** 32),
                          length=32)
            h1 = BitArray(uint=(h1.uint + b.uint) % (2 ** 32),
                          length=32)
            h2 = BitArray(uint=(h2.uint + c.uint) % (2 ** 32),
                          length=32)
            h3 = BitArray(uint=(h3.uint + d.uint) % (2 ** 32),
                          length=32)
            h4 = BitArray(uint=(h4.uint + e.uint) % (2 ** 32),
                          length=32)
            h5 = BitArray(uint=(h5.uint + f.uint) % (2 ** 32),
                          length=32)
            h6 = BitArray(uint=(h6.uint + g.uint) % (2 ** 32),
                          length=32)
            h7 = BitArray(uint=(h7.uint + h.uint) % (2 ** 32),
                          length=32)

        hash = h0 + h1 + h2 + h3 + h4 + h5 + h6 + h7
        return hash.tobytes()

    @staticmethod
    def hash_sha384(msg):
        h0 = BitArray(uint=0xcbbb9d5dc1059ed8, length=64)
        h1 = BitArray(uint=0x629a292a367cd507, length=64)
        h2 = BitArray(uint=0x9159015a3070dd17, length=64)
        h3 = BitArray(uint=0x152fecd8f70e5939, length=64)
        h4 = BitArray(uint=0x67332667ffc00b31, length=64)
        h5 = BitArray(uint=0x8eb44a8768581511, length=64)
        h6 = BitArray(uint=0xdb0c2e0d64f98fa7, length=64)
        h7 = BitArray(uint=0x47b5481dbefa4fa4, length=64)

        bit_msg = BitArray(msg)
        len_msg = len(bit_msg)
        bit_msg += BitArray(bin='1')
        k = (896 - (len_msg + 1)) % 1024
        bit_msg += BitArray(bin='0'*k)
        bit_msg += BitArray(int=len_msg, length=128)
        num_chunks = len(bit_msg) // 1024
        assert len(bit_msg) % 1024 == 0

        bit_msg_chunks = list(bit_msg[1024 * num_chunk:
                                      1024 * (num_chunk + 1)]
                              for num_chunk in range(num_chunks))
        for bit_msg_chunk in bit_msg_chunks:
            msg_sub_chunks = list(bit_msg_chunk[64 * num_chunk:
                                                64 * (num_chunk + 1)]
                                  for num_chunk in range(16))
            for i in range(16, 80):
                chunk_i_15 = msg_sub_chunks[i-15]
                temp0 = copy.deepcopy(chunk_i_15)
                temp0.ror(1)
                temp1 = copy.deepcopy(chunk_i_15)
                temp1.ror(8)
                temp2 = copy.deepcopy(chunk_i_15)
                temp2 = temp2 >> 7
                s0 = temp0 ^ temp1 ^ temp2

                chunk_i_2 = msg_sub_chunks[i-2]
                temp0 = copy.deepcopy(chunk_i_2)
                temp0.ror(19)
                temp1 = copy.deepcopy(chunk_i_2)
                temp1.ror(61)
                temp2 = copy.deepcopy(chunk_i_2)
                temp2 = temp2 >> 6
                s1 = temp0 ^ temp1 ^ temp2

                msg_sub_chunks.append(BitArray(uint=(msg_sub_chunks[i-16].uint + s0.uint + msg_sub_chunks[i-7].uint + s1.uint) % (2 ** 64),
                                               length=64))

            a = copy.deepcopy(h0)
            b = copy.deepcopy(h1)
            c = copy.deepcopy(h2)
            d = copy.deepcopy(h3)
            e = copy.deepcopy(h4)
            f = copy.deepcopy(h5)
            g = copy.deepcopy(h6)
            h = copy.deepcopy(h7)

            for i in range(0, 80):
                temp0 = copy.deepcopy(a)
                temp0.ror(28)
                temp1 = copy.deepcopy(a)
                temp1.ror(34)
                temp2 = copy.deepcopy(a)
                temp2.ror(39)
                Sum0 = temp0 ^ temp1 ^ temp2

                Ma = (a & b) ^ (a & c) ^ (b & c)

                t2 = BitArray(uint=(Sum0.uint + Ma.uint) % (2 ** 64),
                              length=64)

                temp0 = copy.deepcopy(e)
                temp0.ror(14)
                temp1 = copy.deepcopy(e)
                temp1.ror(18)
                temp2 = copy.deepcopy(e)
                temp2.ror(41)
                Sum1 = temp0 ^ temp1 ^ temp2

                temp0 = e & f
                temp1 = ~e
                temp2 = copy.deepcopy(g)
                Ch = temp0 ^ (temp1 & temp2)

                t1 = BitArray(uint=(h.uint + Sum1.uint + Ch.uint + SHA2.Constants_512[i] + msg_sub_chunks[i].uint) % (2 ** 64),
                              length=64)

                h = copy.deepcopy(g)
                g = copy.deepcopy(f)
                f = copy.deepcopy(e)
                e = BitArray(uint=(d.uint + t1.uint) % (2 ** 64),
                             length=64)
                d = copy.deepcopy(c)
                c = copy.deepcopy(b)
                b = copy.deepcopy(a)
                a = BitArray(uint=(t1.uint + t2.uint) % (2 ** 64),
                             length=64)

            h0 = BitArray(uint=(h0.uint + a.uint) % (2 ** 64),
                          length=64)
            h1 = BitArray(uint=(h1.uint + b.uint) % (2 ** 64),
                          length=64)
            h2 = BitArray(uint=(h2.uint + c.uint) % (2 ** 64),
                          length=64)
            h3 = BitArray(uint=(h3.uint + d.uint) % (2 ** 64),
                          length=64)
            h4 = BitArray(uint=(h4.uint + e.uint) % (2 ** 64),
                          length=64)
            h5 = BitArray(uint=(h5.uint + f.uint) % (2 ** 64),
                          length=64)
            h6 = BitArray(uint=(h6.uint + g.uint) % (2 ** 64),
                          length=64)
            h7 = BitArray(uint=(h7.uint + h.uint) % (2 ** 64),
                          length=64)

        hash = h0 + h1 + h2 + h3 + h4 + h5
        return hash.tobytes()

    @staticmethod
    def hash_sha512_224(msg):
        h0 = BitArray(uint=0x8c3d37c819544da2, length=64)
        h1 = BitArray(uint=0x73e1996689dcd4d6, length=64)
        h2 = BitArray(uint=0x1dfab7ae32ff9c82, length=64)
        h3 = BitArray(uint=0x679dd514582f9fcf, length=64)
        h4 = BitArray(uint=0x0f6d2b697bd44da8, length=64)
        h5 = BitArray(uint=0x77e36f7304c48942, length=64)
        h6 = BitArray(uint=0x3f9d85a86a1d36c8, length=64)
        h7 = BitArray(uint=0x1112e6ad91d692a1, length=64)

        bit_msg = BitArray(msg)
        len_msg = len(bit_msg)
        bit_msg += BitArray(bin='1')
        k = (896 - (len_msg + 1)) % 1024
        bit_msg += BitArray(bin='0' * k)
        bit_msg += BitArray(int=len_msg, length=128)
        num_chunks = len(bit_msg) // 1024
        assert len(bit_msg) % 1024 == 0

        bit_msg_chunks = list(bit_msg[1024 * num_chunk:
                                      1024 * (num_chunk + 1)]
                              for num_chunk in range(num_chunks))
        for bit_msg_chunk in bit_msg_chunks:
            msg_sub_chunks = list(bit_msg_chunk[64 * num_chunk:
                                                64 * (num_chunk + 1)]
                                  for num_chunk in range(16))
            for i in range(16, 80):
                chunk_i_15 = msg_sub_chunks[i - 15]
                temp0 = copy.deepcopy(chunk_i_15)
                temp0.ror(1)
                temp1 = copy.deepcopy(chunk_i_15)
                temp1.ror(8)
                temp2 = copy.deepcopy(chunk_i_15)
                temp2 = temp2 >> 7
                s0 = temp0 ^ temp1 ^ temp2

                chunk_i_2 = msg_sub_chunks[i - 2]
                temp0 = copy.deepcopy(chunk_i_2)
                temp0.ror(19)
                temp1 = copy.deepcopy(chunk_i_2)
                temp1.ror(61)
                temp2 = copy.deepcopy(chunk_i_2)
                temp2 = temp2 >> 6
                s1 = temp0 ^ temp1 ^ temp2

                msg_sub_chunks.append(BitArray(
                    uint=(msg_sub_chunks[i - 16].uint + s0.uint + msg_sub_chunks[i - 7].uint + s1.uint) % (2 ** 64),
                    length=64))

            a = copy.deepcopy(h0)
            b = copy.deepcopy(h1)
            c = copy.deepcopy(h2)
            d = copy.deepcopy(h3)
            e = copy.deepcopy(h4)
            f = copy.deepcopy(h5)
            g = copy.deepcopy(h6)
            h = copy.deepcopy(h7)

            for i in range(0, 80):
                temp0 = copy.deepcopy(a)
                temp0.ror(28)
                temp1 = copy.deepcopy(a)
                temp1.ror(34)
                temp2 = copy.deepcopy(a)
                temp2.ror(39)
                Sum0 = temp0 ^ temp1 ^ temp2

                Ma = (a & b) ^ (a & c) ^ (b & c)

                t2 = BitArray(uint=(Sum0.uint + Ma.uint) % (2 ** 64),
                              length=64)

                temp0 = copy.deepcopy(e)
                temp0.ror(14)
                temp1 = copy.deepcopy(e)
                temp1.ror(18)
                temp2 = copy.deepcopy(e)
                temp2.ror(41)
                Sum1 = temp0 ^ temp1 ^ temp2

                temp0 = e & f
                temp1 = ~e
                temp2 = copy.deepcopy(g)
                Ch = temp0 ^ (temp1 & temp2)

                t1 = BitArray(
                    uint=(h.uint + Sum1.uint + Ch.uint + SHA2.Constants_512[i] + msg_sub_chunks[i].uint) % (2 ** 64),
                    length=64)

                h = copy.deepcopy(g)
                g = copy.deepcopy(f)
                f = copy.deepcopy(e)
                e = BitArray(uint=(d.uint + t1.uint) % (2 ** 64),
                             length=64)
                d = copy.deepcopy(c)
                c = copy.deepcopy(b)
                b = copy.deepcopy(a)
                a = BitArray(uint=(t1.uint + t2.uint) % (2 ** 64),
                             length=64)

            h0 = BitArray(uint=(h0.uint + a.uint) % (2 ** 64),
                          length=64)
            h1 = BitArray(uint=(h1.uint + b.uint) % (2 ** 64),
                          length=64)
            h2 = BitArray(uint=(h2.uint + c.uint) % (2 ** 64),
                          length=64)
            h3 = BitArray(uint=(h3.uint + d.uint) % (2 ** 64),
                          length=64)
            h4 = BitArray(uint=(h4.uint + e.uint) % (2 ** 64),
                          length=64)
            h5 = BitArray(uint=(h5.uint + f.uint) % (2 ** 64),
                          length=64)
            h6 = BitArray(uint=(h6.uint + g.uint) % (2 ** 64),
                          length=64)
            h7 = BitArray(uint=(h7.uint + h.uint) % (2 ** 64),
                          length=64)

        hash = h0 + h1 + h2 + h3
        return hash[:224].tobytes()

    @staticmethod
    def hash_sha512_256(msg):
        h0 = BitArray(uint=0x22312194fc2bf72c, length=64)
        h1 = BitArray(uint=0x9f555fa3c84c64c2, length=64)
        h2 = BitArray(uint=0x2393b86b6f53b151, length=64)
        h3 = BitArray(uint=0x963877195940eabd, length=64)
        h4 = BitArray(uint=0x96283ee2a88effe3, length=64)
        h5 = BitArray(uint=0xbe5e1e2553863992, length=64)
        h6 = BitArray(uint=0x2b0199fc2c85b8aa, length=64)
        h7 = BitArray(uint=0x0eb72ddc81c52ca2, length=64)

        bit_msg = BitArray(msg)
        len_msg = len(bit_msg)
        bit_msg += BitArray(bin='1')
        k = (896 - (len_msg + 1)) % 1024
        bit_msg += BitArray(bin='0'*k)
        bit_msg += BitArray(int=len_msg, length=128)
        num_chunks = len(bit_msg) // 1024
        assert len(bit_msg) % 1024 == 0

        bit_msg_chunks = list(bit_msg[1024 * num_chunk:
                                      1024 * (num_chunk + 1)]
                              for num_chunk in range(num_chunks))
        for bit_msg_chunk in bit_msg_chunks:
            msg_sub_chunks = list(bit_msg_chunk[64 * num_chunk:
                                                64 * (num_chunk + 1)]
                                  for num_chunk in range(16))
            for i in range(16, 80):
                chunk_i_15 = msg_sub_chunks[i-15]
                temp0 = copy.deepcopy(chunk_i_15)
                temp0.ror(1)
                temp1 = copy.deepcopy(chunk_i_15)
                temp1.ror(8)
                temp2 = copy.deepcopy(chunk_i_15)
                temp2 = temp2 >> 7
                s0 = temp0 ^ temp1 ^ temp2

                chunk_i_2 = msg_sub_chunks[i-2]
                temp0 = copy.deepcopy(chunk_i_2)
                temp0.ror(19)
                temp1 = copy.deepcopy(chunk_i_2)
                temp1.ror(61)
                temp2 = copy.deepcopy(chunk_i_2)
                temp2 = temp2 >> 6
                s1 = temp0 ^ temp1 ^ temp2

                msg_sub_chunks.append(BitArray(uint=(msg_sub_chunks[i-16].uint + s0.uint + msg_sub_chunks[i-7].uint + s1.uint) % (2 ** 64),
                                               length=64))

            a = copy.deepcopy(h0)
            b = copy.deepcopy(h1)
            c = copy.deepcopy(h2)
            d = copy.deepcopy(h3)
            e = copy.deepcopy(h4)
            f = copy.deepcopy(h5)
            g = copy.deepcopy(h6)
            h = copy.deepcopy(h7)

            for i in range(0, 80):
                temp0 = copy.deepcopy(a)
                temp0.ror(28)
                temp1 = copy.deepcopy(a)
                temp1.ror(34)
                temp2 = copy.deepcopy(a)
                temp2.ror(39)
                Sum0 = temp0 ^ temp1 ^ temp2

                Ma = (a & b) ^ (a & c) ^ (b & c)

                t2 = BitArray(uint=(Sum0.uint + Ma.uint) % (2 ** 64),
                              length=64)

                temp0 = copy.deepcopy(e)
                temp0.ror(14)
                temp1 = copy.deepcopy(e)
                temp1.ror(18)
                temp2 = copy.deepcopy(e)
                temp2.ror(41)
                Sum1 = temp0 ^ temp1 ^ temp2

                temp0 = e & f
                temp1 = ~e
                temp2 = copy.deepcopy(g)
                Ch = temp0 ^ (temp1 & temp2)

                t1 = BitArray(uint=(h.uint + Sum1.uint + Ch.uint + SHA2.Constants_512[i] + msg_sub_chunks[i].uint) % (2 ** 64),
                              length=64)

                h = copy.deepcopy(g)
                g = copy.deepcopy(f)
                f = copy.deepcopy(e)
                e = BitArray(uint=(d.uint + t1.uint) % (2 ** 64),
                             length=64)
                d = copy.deepcopy(c)
                c = copy.deepcopy(b)
                b = copy.deepcopy(a)
                a = BitArray(uint=(t1.uint + t2.uint) % (2 ** 64),
                             length=64)

            h0 = BitArray(uint=(h0.uint + a.uint) % (2 ** 64),
                          length=64)
            h1 = BitArray(uint=(h1.uint + b.uint) % (2 ** 64),
                          length=64)
            h2 = BitArray(uint=(h2.uint + c.uint) % (2 ** 64),
                          length=64)
            h3 = BitArray(uint=(h3.uint + d.uint) % (2 ** 64),
                          length=64)
            h4 = BitArray(uint=(h4.uint + e.uint) % (2 ** 64),
                          length=64)
            h5 = BitArray(uint=(h5.uint + f.uint) % (2 ** 64),
                          length=64)
            h6 = BitArray(uint=(h6.uint + g.uint) % (2 ** 64),
                          length=64)
            h7 = BitArray(uint=(h7.uint + h.uint) % (2 ** 64),
                          length=64)

        hash = h0 + h1 + h2 + h3
        return hash.tobytes()

    @staticmethod
    def hash_sha512(msg):
        h0 = BitArray(uint=0x6a09e667f3bcc908, length=64)
        h1 = BitArray(uint=0xbb67ae8584caa73b, length=64)
        h2 = BitArray(uint=0x3c6ef372fe94f82b, length=64)
        h3 = BitArray(uint=0xa54ff53a5f1d36f1, length=64)
        h4 = BitArray(uint=0x510e527fade682d1, length=64)
        h5 = BitArray(uint=0x9b05688c2b3e6c1f, length=64)
        h6 = BitArray(uint=0x1f83d9abfb41bd6b, length=64)
        h7 = BitArray(uint=0x5be0cd19137e2179, length=64)

        bit_msg = BitArray(msg)
        len_msg = len(bit_msg)
        bit_msg += BitArray(bin='1')
        k = (896 - (len_msg + 1)) % 1024
        bit_msg += BitArray(bin='0'*k)
        bit_msg += BitArray(int=len_msg, length=128)
        num_chunks = len(bit_msg) // 1024
        assert len(bit_msg) % 1024 == 0

        bit_msg_chunks = list(bit_msg[1024 * num_chunk:
                                      1024 * (num_chunk + 1)]
                              for num_chunk in range(num_chunks))
        for bit_msg_chunk in bit_msg_chunks:
            msg_sub_chunks = list(bit_msg_chunk[64 * num_chunk:
                                                64 * (num_chunk + 1)]
                                  for num_chunk in range(16))
            for i in range(16, 80):
                chunk_i_15 = msg_sub_chunks[i-15]
                temp0 = copy.deepcopy(chunk_i_15)
                temp0.ror(1)
                temp1 = copy.deepcopy(chunk_i_15)
                temp1.ror(8)
                temp2 = copy.deepcopy(chunk_i_15)
                temp2 = temp2 >> 7
                s0 = temp0 ^ temp1 ^ temp2

                chunk_i_2 = msg_sub_chunks[i-2]
                temp0 = copy.deepcopy(chunk_i_2)
                temp0.ror(19)
                temp1 = copy.deepcopy(chunk_i_2)
                temp1.ror(61)
                temp2 = copy.deepcopy(chunk_i_2)
                temp2 = temp2 >> 6
                s1 = temp0 ^ temp1 ^ temp2

                msg_sub_chunks.append(BitArray(uint=(msg_sub_chunks[i-16].uint + s0.uint + msg_sub_chunks[i-7].uint + s1.uint) % (2 ** 64),
                                               length=64))

            a = copy.deepcopy(h0)
            b = copy.deepcopy(h1)
            c = copy.deepcopy(h2)
            d = copy.deepcopy(h3)
            e = copy.deepcopy(h4)
            f = copy.deepcopy(h5)
            g = copy.deepcopy(h6)
            h = copy.deepcopy(h7)

            for i in range(0, 80):
                temp0 = copy.deepcopy(a)
                temp0.ror(28)
                temp1 = copy.deepcopy(a)
                temp1.ror(34)
                temp2 = copy.deepcopy(a)
                temp2.ror(39)
                Sum0 = temp0 ^ temp1 ^ temp2

                Ma = (a & b) ^ (a & c) ^ (b & c)

                t2 = BitArray(uint=(Sum0.uint + Ma.uint) % (2 ** 64),
                              length=64)

                temp0 = copy.deepcopy(e)
                temp0.ror(14)
                temp1 = copy.deepcopy(e)
                temp1.ror(18)
                temp2 = copy.deepcopy(e)
                temp2.ror(41)
                Sum1 = temp0 ^ temp1 ^ temp2

                temp0 = e & f
                temp1 = ~e
                temp2 = copy.deepcopy(g)
                Ch = temp0 ^ (temp1 & temp2)

                t1 = BitArray(uint=(h.uint + Sum1.uint + Ch.uint + SHA2.Constants_512[i] + msg_sub_chunks[i].uint) % (2 ** 64),
                              length=64)

                h = copy.deepcopy(g)
                g = copy.deepcopy(f)
                f = copy.deepcopy(e)
                e = BitArray(uint=(d.uint + t1.uint) % (2 ** 64),
                             length=64)
                d = copy.deepcopy(c)
                c = copy.deepcopy(b)
                b = copy.deepcopy(a)
                a = BitArray(uint=(t1.uint + t2.uint) % (2 ** 64),
                             length=64)

            h0 = BitArray(uint=(h0.uint + a.uint) % (2 ** 64),
                          length=64)
            h1 = BitArray(uint=(h1.uint + b.uint) % (2 ** 64),
                          length=64)
            h2 = BitArray(uint=(h2.uint + c.uint) % (2 ** 64),
                          length=64)
            h3 = BitArray(uint=(h3.uint + d.uint) % (2 ** 64),
                          length=64)
            h4 = BitArray(uint=(h4.uint + e.uint) % (2 ** 64),
                          length=64)
            h5 = BitArray(uint=(h5.uint + f.uint) % (2 ** 64),
                          length=64)
            h6 = BitArray(uint=(h6.uint + g.uint) % (2 ** 64),
                          length=64)
            h7 = BitArray(uint=(h7.uint + h.uint) % (2 ** 64),
                          length=64)

        hash = h0 + h1 + h2 + h3 + h4 + h5 + h6 + h7
        return hash.tobytes()
