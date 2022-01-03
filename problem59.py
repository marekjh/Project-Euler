def decrypt(filename):
    with open(filename, "r") as f:
        contents = f.read()
        bits = [int(b) for b in contents.split(",")]
    lowercase = range(ord("a"), ord("z") + 1)
    for i in lowercase:
        for j in lowercase:
            for k in lowercase:
                key = (i, j, k)
                out = open("out.txt", "a")
                for b in range(len(bits)):
                    rem = b % 3
                    out.write(chr(bits[b] ^ key[rem]))
                out.write("\n")
    out.close()

def plaintext_sum(filename):
    with open(filename, "r") as f:
        contents = f.read()
        return sum([ord(c) for c in contents])

#decrypt("p059_cipher.txt")
#print(plaintext_sum("p059_plaintext.txt"))
