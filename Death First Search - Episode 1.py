def bBW(si, gw):
    global rels
    for g in gw:
        if g in rels[si]:
            return [si, g]  # returning the path shared by both the gw and the si if there is one
    for g in gw:
        if len(rels[g]) > 0:
            return [g, rels[g][0]]  # returning a link anywhere if si and gw don't share a path
    return [0, 0]  # returning the first node itself


def rem(c1, c2):
    global rels
    rels[c1].remove(c2)  # removing c2 from c1
    rels[c2].remove(c1)  # removing c1 from c2


n, l, e = [int(i) for i in input().split()]

rels = {}
for i in range(l):
    n1, n2 = [int(j) for j in input().split()]
    rels.setdefault(n1, []).append(n2)
    rels.setdefault(n2, []).append(n1)

gw = []
for i in range(e):
    ei = int(input())
    gw.append(ei)

while True:
    si = int(input())
    c1, c2 = bBW(si, gw)  # finding the best way to block
    rem(c1, c2)  # removing the bridge
    print(f"{c1} {c2}")
