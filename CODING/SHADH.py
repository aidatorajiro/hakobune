import hashlib

P = b"\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11"

def add(P, Q):
    if P == b"":
        return Q
    if Q == b"":
        return P
    if len(P) != 32 or len(Q) != 32:
        raise Exception("invalid length")
    if int.from_bytes(P, "big") <= int.from_bytes(Q, "big"):
        return hashlib.sha256(P + Q).digest()
    else:
        return hashlib.sha256(Q + P).digest()

def mul(P, n):
    bs = format(n, 'b')[::-1]
    tmp = P
    result = b""
    for i in bs:
        if i == "1":
            result = add(result, tmp)
        tmp = add(tmp, tmp)
    return result