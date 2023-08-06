# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import pytest

from tokenizer_tools.tagset.BMES import BMESEncoderDecoder


word_coding_pairs = (
    ('我', 'S'),
    ('我们', 'BE'),
    ('飞机票', 'BME'),
    ('东南西北', 'BMME'),

)


@pytest.mark.parametrize("input_word, output_tags", word_coding_pairs)
def test_encode_word(input_word, output_tags):
    bmes_encoder_decoder = BMESEncoderDecoder()

    tags = bmes_encoder_decoder.encode_word(input_word)

    pytest.helpers.assert_sequence_equals(tags, output_tags)


@pytest.mark.parametrize(
    "word_list, gold_tags_list",
    (list(zip(*word_coding_pairs)),)
)
def test_encode_word_list(word_list, gold_tags_list):
    bmes_encoder_decoder = BMESEncoderDecoder()

    test_tags_list = bmes_encoder_decoder.encode_word_list(word_list)

    pytest.helpers.assert_sequence_equals(test_tags_list, gold_tags_list)


test_encode_word_list_as_string_parametrize = (
    (
        list(zip(*word_coding_pairs))[0],
        ''.join(list(zip(*word_coding_pairs))[1])
    ),
)


@pytest.mark.parametrize(
    "word_list, gold_str",
    test_encode_word_list_as_string_parametrize
)
def test_encode_word_list_as_string(word_list, gold_str):
    bmes_encoder_decoder = BMESEncoderDecoder()

    test_str = bmes_encoder_decoder.encode_word_list_as_string(word_list)

    pytest.helpers.assert_sequence_equals(test_str, gold_str)


test_decode_char_tag_pair_parametrize = (
    (list(zip(*[''.join(i) for i in zip(*word_coding_pairs)])), [i[0] for i in word_coding_pairs]),
)


@pytest.mark.parametrize("char_tag_pair, gold_word_list", test_decode_char_tag_pair_parametrize)
def test_decode_char_tag_pair(char_tag_pair, gold_word_list):
    bmes_encoder_decoder = BMESEncoderDecoder()

    test_word_list = bmes_encoder_decoder.decode_char_tag_pair(char_tag_pair)

    pytest.helpers.assert_sequence_equals(test_word_list, gold_word_list)
