from tokenizer_tools.tagset.BMES import BMESEncoderDecoder
from tokenizer_tools.evaluator.token.tag_level import TagEvaluator


def evaluate_by_files(test_file, gold_file, corpus_aligned=False):
    with open(test_file) as fd:
        test_line_list = fd.readlines()

    with open(gold_file) as fd:
        gold_line_list = fd.readlines()

    if corpus_aligned:
        assert len(test_line_list) == len(gold_line_list)

    encoder = BMESEncoderDecoder()
    tag_evaluator = TagEvaluator()

    if corpus_aligned:
        for i in range(len(gold_line_list)):
            test_line = test_line_list[i]
            gold_line = gold_line_list[i]

            test_word_list = test_line.strip().split()
            gold_word_list = gold_line.strip().split()

            test_tags = encoder.encode_word_list_as_string(test_word_list)
            gold_tags = encoder.encode_word_list_as_string(gold_word_list)

            tag_evaluator.process_one_paragraph(gold_tags, test_tags)
    else:
        test_content = ' '.join([i.strip() for i in test_line_list])
        gold_content = ' '.join([i.strip() for i in gold_line_list])

        test_word_list = test_content.split()
        gold_word_list = gold_content.split()

        test_tags = encoder.encode_word_list_as_string(test_word_list)
        gold_tags = encoder.encode_word_list_as_string(gold_word_list)

        tag_evaluator.process_one_paragraph(gold_tags, test_tags)

    precision, recall, f1 = tag_evaluator.get_score()

    return precision, recall, f1
