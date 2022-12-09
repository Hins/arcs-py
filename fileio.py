import jieba

WORD = 0
POS = 1
HEAD = 2
LABEL = 3


def read_conll_deps(file, trainable=True):
    origin_sentences = []
    sentences = []
    sentence = []
    with open(file, 'r') as f:
        for line in f:
            line = line.strip().replace('\n', '')
            if trainable:
                tokens = line.split('\t')
                if len(tokens) < 9:
                    sentence = [tok if tok[HEAD] is not -1 else (tok[WORD], tok[POS], len(sentence), tok[LABEL]) for tok in sentence]
                    sentences.append(sentence)
                    sentence = []
                else:
                    sentence.append((tokens[1].lower(), tokens[3], int(tokens[6]) - 1, tokens[7]))
            else:
                tokens = [token for token in jieba.cut(line)]
                origin_sentences.append(tokens)
                for token in tokens:
                    sentence.append((token[0].lower(), "", 0, "root"))
                sentence = [tok if tok[HEAD] is not -1 else (tok[WORD], tok[POS], len(sentence), tok[LABEL]) for tok in
                            sentence]
                sentences.append(sentence)
                sentence = []
    return origin_sentences, sentences
