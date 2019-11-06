def make_trie(words):
    end = '__end__'
    root = {}
    for word in words:
        cur_dict = root
        for letter in word:
            cur_dict = cur_dict.setdefault(letter, {})
        cur_dict[end] = end
    return root


def in_trie(trie, word):
    end = '__end__'
    cur_dict = trie
    for letter in word:
        if letter in cur_dict:
            cur_dict = cur_dict[letter]
        else:
            return False
    if end in cur_dict:
        return True
    else:
        return False

def predict(trie, prefix):
    end = '__end__'
    cur_dict = trie
    for letter in prefix:
        if letter in cur_dict:
            cur_dict = cur_dict[letter]
        else:
            return []
    
    predictions = []
    def helper(trie, prefix):
        for k,v in trie.items():
            if v != '__end__':
                helper(v, prefix+k)
            else:
                predictions.append(prefix)
    helper(cur_dict, prefix)
    return predictions

words = ['foo', 'bar', 'baz', 'barz']
root = make_trie(words)
print(root)
print(in_trie(root, 'foo'))
print(in_trie(root, 'fooz'))
print(predict(root, 'ba'))
