def sort_words(sentence):
    """
    Insert your code here
    """
    words = sentence.split()
    n = len(words)
    for i in range(n):
        for j in range(0, n-i-1):
            if len(words[j]) > len(words[j+1]):
                words[j], words[j+1] = words[j+1], words[j]
    return words

if __name__ == "__main__":
    words = 'ala ma kota i chomika'
    print(sort_words(words))
