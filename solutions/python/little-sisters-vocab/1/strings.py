"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    return "un" + word


def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    words_with_prefix = [prefix + word for word in vocab_words[1:]]
    result_words = [prefix] + words_with_prefix
    return " :: ".join(result_words)


def remove_suffix_ness(word):
    root_word = word[:-4]
    if root_word.endswith('i'):
        return root_word[:-1] + 'y'
    else:
        return root_word


def adjective_to_verb(sentence, index):
    words = sentence.strip().rstrip('.,!?;').split()
    adjective = words[index]
    adjective = adjective.rstrip('.,!?;')
    return adjective + 'en'
