


def num_different_permutations_helper(word, index):
    if index >= len(word) - 1:
        return 1
    c = 0
    for i in range(index, len(word)):
        if word[i] not in word[index:i]:
            word[index], word[i] = word[i], word[index]
            c += num_different_permutations_helper(word, index+1)
            word[index], word[i] = word[i], word[index]
    return c



def num_different_permutations(word):
    word = list(word)
    return num_different_permutations_helper(word, 0)

print(num_different_permutations('abb'))
