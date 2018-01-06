def rotate(text, key):
    def mod(char):
        if ord(char) in range(ord('a'), ord('z') + 1):
            return chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        elif ord(char) in range(ord('A'), ord('Z') + 1):
            return chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        else:
            return char

    return ''.join([mod(c) for c in text])
