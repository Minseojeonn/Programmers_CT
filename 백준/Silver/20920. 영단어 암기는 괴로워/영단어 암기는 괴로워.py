num_vocab, len_limit = map(int, input().split(" "))

vocab_dict = {}    

for i in range(num_vocab):
    vocab = input()
    if len(vocab) >= len_limit:
        if vocab not in vocab_dict:
            vocab_dict[vocab] = 1
        else:
            vocab_dict[vocab] += 1

word_sorter = []
for vocab in vocab_dict:
    num = vocab_dict[vocab]
    word_sorter.append((num, vocab))
    
word_sorter.sort(key=lambda x : (-x[0], -len(x[1]), x[1]))
for num, vocab in word_sorter:
    print(vocab)