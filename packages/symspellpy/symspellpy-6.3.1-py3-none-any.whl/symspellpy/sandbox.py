import re

phrase = "in Subject 083.89 te dhird QARTER ofl'ast jear he hadlearned ofca sekretplan y iran"
aa = re.findall(r"([^\W_]+['’]*[^\W_]*)", phrase)


def try_parse_int64(string):
    try:
        ret = int(string)
    except ValueError:
        return None
    return None if ret < -2 ** 64 or ret >= 2 ** 64 else ret

for a in aa:
    print(re.match(r"[A-Z]{2,}\b", a))
