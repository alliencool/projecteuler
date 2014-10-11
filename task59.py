import sys

top100 = ["the", "of", "and", "a", "to","in","is","you","that","it","he","was",
          "for", "on", "are", "as", "with", "his", "they", "I", "at", "be","this",
          "have", "from", "or", "one", "had", "by", "word", "but", "not", "what",
          "all", "were", "we", "when", "your", "can", "said", "there", "use",
          "an", "each", "which", "she", "do", "how", "their", "if", "will", "up",
          "other", "about", "out", "many", "then", "them", "these", "so", "some",
          "her", "would", "make", "like", "him", "into", "time", "has", "look",
          "two", "more", "write", "go", "see", "number", "no", "way", "could",
          "people", "my", "than", "first", "water", "been", "call", "who",
          "oil", "its", "now", "find", "long", "down", "day", "did", "get", "come",
          "made", "may", "part"]

def task59(filename):
    with open(filename) as fd:
        text = [int(x) for x in fd.read().split(",")]
        text_l = len(text)
        left_bound = ord('a')
        right_bound = ord('z') + 1
        for a in xrange(left_bound, right_bound):
            for b in xrange(left_bound, right_bound):
                for c in xrange(left_bound, right_bound):
                    result = ""
                    key_l = [a, b, c]
                    ind = 0
                    for i in xrange(text_l):
                        result += chr(text[i] ^ key_l[ind])
                        ind = (ind + 1) % 3

                    cnt = 0
                    for word in top100:
                        cnt += result.count(word)

                    if cnt > 200:
                        print "This might be a good result:\n", result, "\nHere is sum of characters: ", sum([ord(c) for c in result])

if __name__ == "__main__":
    task59(sys.argv[1])
