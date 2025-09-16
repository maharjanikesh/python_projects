def get_words(paragraph):
    # Converting into lowercase
    paragraph = paragraph.lower()

    # Replacing punctuation
    for p in [",", ".", "!"]:
        paragraph = paragraph.replace(p, "")

    # Splitting words
    words = paragraph.split()

    # Counting the words and inserting in a dict
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # Top Three in dict
    top_three = []
    for _ in range(3):
        if not word_count:
            break
        else:
            max_word = max(word_count, key=word_count.get)
            top_three.append(max_word)
            del word_count[max_word]
    

    return top_three

print(get_words("Coding in Python is fun because coding Python allows for coding in Python easily while coding"))