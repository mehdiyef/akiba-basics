print("================================Text Statistics and Word Analyzer =========================")

def count_words(para):
    return len(para.split())

def count_char(para):
    counter=0
    for i in para:
        if  i!=" ":
            counter+=1
    return counter

def count_vowel_consonant(para):
    vowel=0
    consonant=0

    # print(para.lower())

    for i in para.lower():
        # print(i)
        if i == " ": continue

        else:
            if i in "aeiou":
                vowel+=1
            else:
                consonant+=1
    return vowel, consonant

def longest_word(para):
    splited_para=para.split()

    longest=splited_para[0]

    for i in splited_para[1:]:
        if len(i)>len(longest):
            longest=i

    return longest


def repeated_words(para):
    repeated_words=[]
    splited_para=para.split()

    for i in range(len(splited_para)):
        repeated = splited_para[i]
        if repeated in splited_para[i+1:]:
            repeated_words.append(repeated)
    return repeated_words


def main():
    para="Python is useful and Python  is powerful"
    print("Words: ", count_words(para))
    print("longest word: ", longest_word(para))
    print("repeated word: ",repeated_words(para))


if __name__ == "__main__":
    main()