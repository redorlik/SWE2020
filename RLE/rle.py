#RLE encoder / decoder

def decode(st):
    res = []
    st = list(st)
    while st:
        res.append(int(st.pop(0))*st.pop(0))
    return ''.join(res)

def rle(st):
    j = 0
    res = []
    while j < len(st):
        i = 0
        ch = st[j]
        while j < len(st) and st[j] == ch:
            i += 1
            j += 1
        res.append(f'{i}{ch}')
    return ''.join(res)
