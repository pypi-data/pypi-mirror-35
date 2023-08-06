class BMESEncoderDecoder:
    def __int__(self):
        pass

    def encode_word(self, word):
        # type: (str) -> str

        len_of_word = len(word)

        if len_of_word == 1:
            return 'S'

        if len_of_word >= 2:
            number_of_middle = len_of_word - 2
            return 'B' + 'M' * number_of_middle + 'E'

    def encode_word_list(self, word_list):
        # type: (List[str]) -> List(str)

        return [self.encode_word(i) for i in word_list]

    def encode_word_list_as_string(self, word_list):
        # type: (List[str]) -> str

        return "".join(self.encode_word_list(word_list))

    def decode_tag(self, tag_list):
        # type: (List[str]) -> List[List(int, int)]

        def _decoding_exception(tag_list, i):
            return ValueError(
                "Decoding error near end of {}".format(tag_list[:i + 1]))

        def _process_word(word_list_slice, previous_tags, i):
            word_list_slice.append((i - len(previous_tags) + 1, i + 1))
            previous_tags[:] = []

        word_list_slice = []

        previous_tags = []
        for i, tag in enumerate(tag_list):
            if not previous_tags:  # start a new token
                if tag not in ('B', 'S'):
                    raise _decoding_exception(tag_list, i)

                previous_tags.append(tag)

                if tag == 'S':
                    _process_word(word_list_slice, previous_tags, i)
            else:
                if tag not in ('M', 'E'):
                    raise _decoding_exception(tag_list, i)

                previous_tags.append(tag)

                if tag == 'E':
                    _process_word(word_list_slice, previous_tags, i)

        return word_list_slice

    def decode_char_tag_pair(self, char_tag_pair):
        # type: (List[List[str, str]]) -> List[str]

        tag_list = [i[1] for i in char_tag_pair]

        word_list_slice = self.decode_tag(tag_list)

        word_tag_list = [char_tag_pair[i: j] for i, j in word_list_slice]
        word_list = [''.join([j[0] for j in i]) for i in word_tag_list]

        return word_list
