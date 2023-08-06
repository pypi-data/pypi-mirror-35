from tokenizer_tools.evaluator.token.token_level import TokenEvaluator
from tokenizer_tools.tagset.BMES import BMESEncoderDecoder
from tokenizer_tools.evaluator.token.tag_level import TagEvaluator


def evaluate_by_files_at_tag_level(test_file, gold_file):
    with open(test_file) as fd:
        test_line_list = fd.readlines()

    with open(gold_file) as fd:
        gold_line_list = fd.readlines()

    encoder = BMESEncoderDecoder()
    tag_evaluator = TagEvaluator()

    test_content = ' '.join([i.strip() for i in test_line_list])
    gold_content = ' '.join([i.strip() for i in gold_line_list])

    test_word_list = test_content.split()
    gold_word_list = gold_content.split()

    test_tags = encoder.encode_word_list_as_string(test_word_list)
    gold_tags = encoder.encode_word_list_as_string(gold_word_list)

    tag_evaluator.process_one_batch(gold_tags, test_tags)

    metrics = tag_evaluator.get_score()

    return metrics


def evaluate_by_files_at_token_level(test_file, gold_file):
    with open(test_file) as fd:
        test_line_list = fd.readlines()

    with open(gold_file) as fd:
        gold_line_list = fd.readlines()

    token_evaluator = TokenEvaluator()

    test_content = ' '.join([i.strip() for i in test_line_list])
    gold_content = ' '.join([i.strip() for i in gold_line_list])

    test_word_list = test_content.split()
    gold_word_list = gold_content.split()

    token_evaluator.process_one_batch(gold_word_list, test_word_list)

    metrics = token_evaluator.get_score()

    return metrics
