def detect_anagrams(word, candidates):
    def is_anagram(word, candidate):
        return (({l: list(word).count(l) for l in set(word)} ==
                 {l: list(candidate).count(l) for l in set(candidate)}) and
                (word != candidate))

    return list(filter(lambda c: is_anagram(word.lower(), c.lower()),
                       candidates))
