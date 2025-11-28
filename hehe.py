# perform decryption with given constants
blob = "Sd9CG5TC4Xrz6ISW830mryN0qzBXwV/lyRt+cA2ifxAxXJPRAbLYR65qQWzv1HrKAJb1CBEwt+F8tvNnYfsBdAoQifQnjNi/GLHB"
ALPHABET="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789{}_"
STD="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
CST="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/"
SM=7; OFF=23
import base64

# reverse stage3: map custom to standard
trans = str.maketrans({c:STD[i] for i,c in enumerate(CST)})
std = blob.translate(trans)
# pad
std += "="*((-len(std))%4)
data_bytes = base64.b64decode(std)
# decode latin-1 to string
s2 = data_bytes.decode('latin-1')
# reverse stage2
s1 = ''.join(chr(ord(c) ^ ((i*SM + OFF) % 256)) for i,c in enumerate(s2))
# reverse stage1
plain_chars = []
for ch in s1:
    if ch in ALPHABET:
        idx = ALPHABET.index(ch)
        plain_chars.append(ALPHABET[(idx - OFF) % len(ALPHABET)])
    else:
        plain_chars.append(ch)
plain = ''.join(plain_chars)
print (plain)
