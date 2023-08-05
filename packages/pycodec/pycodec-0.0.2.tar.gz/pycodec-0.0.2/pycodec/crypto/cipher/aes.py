#!/usr/bin/python3

import copy
from gf256 import GF256


class AES:
    """
    AES standard cryptography cipher
    """
    Sbox = [
        [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76],
        [0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0],
        [0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15],
        [0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75],
        [0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84],
        [0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf],
        [0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8],
        [0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2],
        [0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73],
        [0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb],
        [0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79],
        [0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08],
        [0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a],
        [0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e],
        [0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf],
        [0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16],
    ]

    InvSbox = [
        [0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb],
        [0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb],
        [0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e],
        [0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25],
        [0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92],
        [0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84],
        [0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06],
        [0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b],
        [0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73],
        [0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e],
        [0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b],
        [0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4],
        [0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f],
        [0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef],
        [0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61],
        [0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d],
    ]

    Rcon = [
        [0x00, 0x00, 0x00, 0x00],
        [0x01, 0x00, 0x00, 0x00],
        [0x02, 0x00, 0x00, 0x00],
        [0x04, 0x00, 0x00, 0x00],
        [0x08, 0x00, 0x00, 0x00],
        [0x10, 0x00, 0x00, 0x00],
        [0x20, 0x00, 0x00, 0x00],
        [0x40, 0x00, 0x00, 0x00],
        [0x80, 0x00, 0x00, 0x00],
        [0x1b, 0x00, 0x00, 0x00],
        [0x36, 0x00, 0x00, 0x00],
    ]

    class _State:
        """
        Class state is used internally for AES algorithm
        """
        def __init__(self):
            self.bytes = [
                [None, None, None, None],
                [None, None, None, None],
                [None, None, None, None],
                [None, None, None, None]
            ]

        def __getitem__(self, index):
            return self.bytes[index]

        def __setitem__(self, key, value):
            self.bytes[key] = value

        def get_bytes(self):
            result = bytes()
            num = 0
            col_num = 0
            while True:
                result += bytes([self.bytes[num][col_num]])
                num += 1
                if num >= len(self.bytes):
                    num = 0
                    col_num += 1
                if col_num >= len(self.bytes[0]):
                    break
            return result

        def __str__(self):
            result = ''
            for lst in self.bytes:
                for ch in lst:
                    result += chr(ch)
            return result

    def _is_valid_key_len(self, key_len):
        return key_len == 16 or key_len == 24 or key_len == 32

    def __init__(self, key, iv=None):
        if not self._is_valid_key_len(len(key)):
            raise ValueError(f'Key [{len(key)}] is not valid key length')
        self.Nb = 4
        self.Nk = len(key) // self.Nb
        self._calculate_round_num()
        self._exp_key = self._expand_key(key)
        if iv is not None:
            if type(iv) == bytes:
                self._iv = iv
            else:
                self._iv = bytes(iv)
        else:
            with open("/dev/urandom", "rb") as urandom_gen:
                self._iv = urandom_gen.read(16)

    def _calculate_round_num(self):
        if self.Nk == 4:
            self.Nr = 10
        elif self.Nk == 6:
            self.Nr = 12
        elif self.Nk == 8:
            self.Nr = 14

    def _expand_key(self, key):
        """
        This function is used for key expansion
        :param key: Key to be expanded
        :return: Expanded key
        """
        exp_key = []
        i = 0
        while i < self.Nk:
            exp_key.append([key[self.Nb*i], key[self.Nb*i+1], key[self.Nb*i+2], key[self.Nb*i+3]])
            i += 1
        i = self.Nk
        while i < (self.Nb * (self.Nr + 1)):
            temp = exp_key[i-1]
            if (i % self.Nk) == 0:
                sub_word = self._sub_word(self._rot_word(temp))
                rcon = AES.Rcon[i // self.Nk]
                temp = self._xor_lists(sub_word, rcon)
            elif self.Nk > 6 and (i % self.Nk) == 4:
                temp = self._sub_word(temp)
            exp_key.append(self._xor_lists(exp_key[i - self.Nk], temp))
            i += 1
        return exp_key

    def _sub_word(self, word):
        sub_word = []
        for ch in word:
            x = ch // 16
            y = ch % 16
            sub_word.append(AES.Sbox[x][y])
        return sub_word

    def _rot_word(self, word):
        return [word[1], word[2], word[3], word[0]]

    def _xor_lists(self, list0, list1):
        return [x ^ y for x, y in zip(list0, list1)]

    def _increment_none(self):
        is_overflow = False
        new_none = []
        is_first = True
        for ch in reversed(self._iv):
            if is_first:
                ch += 1
                is_first = False
            if is_overflow:
                ch += 1
                is_overflow = False
            new_ch = ch % 256
            if ch // 256 > 0:
                is_overflow = True
            new_none.insert(0, new_ch)
        self._iv = bytes(new_none)

    def _create_state(self, msg):
        """
        Create state from msg
        :param msg: Msg from which created _State
        :return: _State class
        """
        state = AES._State()
        row_num = 0
        col_num = 0
        for ch in msg:
            if row_num >= self.Nb:
                row_num = 0
                col_num += 1
            if row_num < self.Nb:
                state.bytes[row_num][col_num] = ch
                row_num += 1
        return state

    def _encrypt_ECB(self, msg):
        state = self._create_state(msg)
        state = self._add_round_key(state, self._exp_key[0:self.Nb])
        for round in range(1, self.Nr):
            state = self._sub_bytes(state)
            state = self._shift_rows(state)
            state = self._mix_columns(state)
            state = self._add_round_key(state, self._exp_key[(round * self.Nb):((round + 1) * self.Nb)])
        state = self._sub_bytes(state)
        state = self._shift_rows(state)
        state = self._add_round_key(state, self._exp_key[(self.Nr * self.Nb):((self.Nr + 1) * self.Nb)])
        return state.get_bytes()

    def _encrypt_CBC(self, msg):
        enc_msg = []
        index = 0
        xor_list = self._iv
        num_chunks = len(msg) // 16
        while index < num_chunks:
            msg_to_enc = msg[16*index:16*index+16]
            msg_to_enc = self._xor_lists(xor_list, msg_to_enc)
            xor_list = self._encrypt_ECB(msg_to_enc)
            enc_msg.append(xor_list)
            index += 1
        return b"".join(enc_msg)

    def _encrypt_CTR(self, msg):
        enc_msg = []
        index = 0
        num_chunks = len(msg) // 16
        if len(msg) % 16 > 0:
            num_chunks += 1
        while index < num_chunks:
            dec_nonce = self._encrypt_ECB(self._iv)
            self._increment_none()
            msg_to_enc = msg[16*index:16*index+16]
            enc_msg.append(self._xor_lists(dec_nonce, msg_to_enc))
            index += 1
        bytess = [bytes(chunk) for chunk in enc_msg]
        return b"".join(bytess)

    def encrypt(self, msg, mode='ECB'):
        """
        Encrypt message
        :param msg: Msg for encryption
        :return: Bytes list
        """
        if mode is None or mode == 'ECB':
            return self._encrypt_ECB(msg)
        elif mode == 'CBC':
            return self._encrypt_CBC(msg)
        elif mode == 'CTR':
            return self._encrypt_CTR(msg)
        else:
            raise NotImplementedError(f'mode [{mode}] is not implemented !!')

    def _decrypt_ECB(self, msg):
        state = self._create_state(msg)
        state = self._add_round_key(state, self._exp_key[(self.Nr * self.Nb):((self.Nr + 1) * self.Nb)])
        for round in reversed(range(1, self.Nr)):
            state = self._inv_shift_rows(state)
            state = self._inv_sub_bytes(state)
            state = self._add_round_key(state, self._exp_key[(round * self.Nb):((round + 1) * self.Nb)])
            state = self._inv_mix_columns(state)
        state = self._inv_shift_rows(state)
        state = self._inv_sub_bytes(state)
        state = self._add_round_key(state, self._exp_key[0:self.Nb])
        return state.get_bytes()

    def _decrypt_CBC(self, cmsg):
        dec_msg = []
        index = 0
        xor_list = self._iv
        num_chunks = len(cmsg) // 16
        while index < num_chunks:
            cmsg_chunk = cmsg[16*index:16*index+16]
            dec_msg_chunk = self._xor_lists(xor_list, self._decrypt_ECB(cmsg_chunk))
            dec_msg.append(dec_msg_chunk)
            xor_list = cmsg_chunk
            index += 1
        bytess = [bytes(chunk) for chunk in dec_msg]
        return b"".join(bytess)

    def _decrypt_CTR(self, cmsg):
        dec_msg = []
        index = 0
        num_chunks = len(cmsg) // 16
        if len(cmsg) % 16 > 0:
            num_chunks += 1
        while index < num_chunks:
            dec_nonce = self._encrypt_ECB(self._iv)
            self._increment_none()
            cmsg_to_dec = cmsg[16*index:16*index+16]
            dec_msg.append(self._xor_lists(dec_nonce, cmsg_to_dec))
            index += 1
        bytess = [bytes(chunk) for chunk in dec_msg]
        return b"".join(bytess)

    def decrypt(self, msg, mode='ECB'):
        """
        Decrypt message
        :param msg: Msg for decryption
        :return: Bytes list
        """
        if mode is None or mode == 'ECB':
            return self._decrypt_ECB(msg)
        elif mode == 'CBC':
            return self._decrypt_CBC(msg)
        elif mode == 'CTR':
            return self._decrypt_CTR(msg)
        else:
            raise NotImplementedError(f'mode [{mode}] is not implemented !!')

    def _add_round_key(self, state, round_key):
        new_state = copy.deepcopy(state)
        row_num = 0
        for row in state.bytes:
            column_num = 0
            for column in row:
                new_state[row_num][column_num] ^= round_key[column_num][row_num]
                column_num += 1
            row_num += 1
        return new_state

    def _sub_bytes(self, state):
        new_state = copy.deepcopy(state)
        row_num = 0
        for row in state.bytes:
            column_num = 0
            for column in row:
                state_value = state[row_num][column_num]
                x = state_value // 16
                y = state_value % 16
                new_state[row_num][column_num] = AES.Sbox[x][y]
                column_num += 1
            row_num += 1
        return new_state

    def _inv_sub_bytes(self, state):
        inv_state = copy.deepcopy(state)
        row_num = 0
        for row in state.bytes:
            column_num = 0
            for column in row:
                state_value = state[row_num][column_num]
                x = state_value // 16
                y = state_value % 16
                inv_state[row_num][column_num] = AES.InvSbox[x][y]
                column_num += 1
            row_num += 1
        return inv_state

    def _shift_rows(self, state):
        new_state = copy.deepcopy(state)
        row_num = 0
        for row in state.bytes:
            new_state[row_num] = state[row_num][row_num:] + state[row_num][:row_num]
            row_num += 1
        return new_state

    def _inv_shift_rows(self, state):
        inv_state = copy.deepcopy(state)
        row_num = 0
        for row in state.bytes:
            before = state[row_num][len(state.bytes)-row_num:]
            after = state[row_num][:len(state.bytes)-row_num]
            inv_state[row_num] = before + after
            row_num += 1
        return inv_state

    def _mix_columns(self, state):
        new_state = copy.deepcopy(state)
        row_num = 0
        for row in state.bytes:
            column_num = 0
            for column in row:
                new_state[0][column_num] = int(GF256(2) * GF256(state[0][column_num])) ^ \
                                           int(GF256(3) * GF256(state[1][column_num])) ^ \
                                           state[2][column_num] ^ \
                                           state[3][column_num]
                new_state[1][column_num] = state[0][column_num] ^ \
                                           int(GF256(2) * GF256(state[1][column_num])) ^ \
                                           int(GF256(3) * GF256(state[2][column_num])) ^ \
                                           state[3][column_num]
                new_state[2][column_num] = state[0][column_num] ^ \
                                           state[1][column_num] ^ \
                                           int(GF256(2) * GF256(state[2][column_num])) ^ \
                                           int(GF256(3) * GF256(state[3][column_num]))
                new_state[3][column_num] = int(GF256(3) * GF256(state[0][column_num])) ^ \
                                           state[1][column_num] ^ \
                                           state[2][column_num] ^ \
                                           int(GF256(2) * GF256(state[3][column_num]))
                column_num += 1
            row_num += 1
        return new_state

    def _inv_mix_columns(self, state):
        inv_state = copy.deepcopy(state)
        row_num = 0
        for row in state.bytes:
            column_num = 0
            for column in row:
                inv_state[0][column_num] = int(GF256(0x0e) * GF256(state[0][column_num])) ^ \
                                           int(GF256(0x0b) * GF256(state[1][column_num])) ^ \
                                           int(GF256(0x0d) * GF256(state[2][column_num])) ^ \
                                           int(GF256(0x09) * GF256(state[3][column_num]))
                inv_state[1][column_num] = int(GF256(0x09) * GF256(state[0][column_num])) ^ \
                                           int(GF256(0x0e) * GF256(state[1][column_num])) ^ \
                                           int(GF256(0x0b) * GF256(state[2][column_num])) ^ \
                                           int(GF256(0x0d) * GF256(state[3][column_num]))
                inv_state[2][column_num] = int(GF256(0x0d) * GF256(state[0][column_num])) ^ \
                                           int(GF256(0x09) * GF256(state[1][column_num])) ^ \
                                           int(GF256(0x0e) * GF256(state[2][column_num])) ^ \
                                           int(GF256(0x0b) * GF256(state[3][column_num]))
                inv_state[3][column_num] = int(GF256(0x0b) * GF256(state[0][column_num])) ^ \
                                           int(GF256(0x0d) * GF256(state[1][column_num])) ^ \
                                           int(GF256(0x09) * GF256(state[2][column_num])) ^ \
                                           int(GF256(0x0e) * GF256(state[3][column_num]))
                column_num += 1
            row_num += 1
        return inv_state


def main():
    '''
    Cryptography, Part 1 (Coursera)
    Week2: Examples
    '''
    aes = AES(bytes.fromhex('140b41b22a29beb4061bda66b6747e14'),
              [0x4c, 0xa0, 0x0f, 0xf4, 0xc8, 0x98, 0xd6, 0x1e, 0x1e, 0xdb, 0xf1, 0x80, 0x06, 0x18, 0xfb, 0x28])
    dec_msg = aes.decrypt(bytes.fromhex('28a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81'), mode='CBC')
    print(f'example_msg_0 is {dec_msg}')

    aes = AES(bytes.fromhex('140b41b22a29beb4061bda66b6747e14'),
              [0x5b, 0x68, 0x62, 0x9f, 0xeb, 0x86, 0x06, 0xf9, 0xa6, 0x66, 0x76, 0x70, 0xb7, 0x5b, 0x38, 0xa5])
    dec_msg = aes.decrypt(bytes.fromhex('b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253'), mode='CBC')
    print(f'example_msg_1 is {dec_msg}')

    aes = AES(bytes.fromhex('36f18357be4dbd77f050515c73fcf9f2'),
              [0x69, 0xdd, 0xa8, 0x45, 0x5c, 0x7d, 0xd4, 0x25, 0x4b, 0xf3, 0x53, 0xb7, 0x73, 0x30, 0x4e, 0xec])
    dec_msg = aes.decrypt(bytes.fromhex('0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329'), mode='CTR')
    print(f'example_msg_2 is {dec_msg}')

    aes = AES(bytes.fromhex('36f18357be4dbd77f050515c73fcf9f2'),
              [0x77, 0x0b, 0x80, 0x25, 0x9e, 0xc3, 0x3b, 0xeb, 0x25, 0x61, 0x35, 0x8a, 0x9f, 0x2d, 0xc6, 0x17])
    dec_msg = aes.decrypt(bytes.fromhex('e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451'), mode='CTR')
    print(f'example_msg_3 is {dec_msg}')


if __name__ == '__main__':
    main()
