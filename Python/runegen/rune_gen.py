import random, sys

SYLLABLES = ["al","ar","el","or","eth","in","ra","lun","sol","mir","ka","thar","vis"]
# Contributors: add more syllables

RUNES = [
    "ᚠ","ᚢ","ᚦ","ᚨ","ᚱ","ᚲ","ᚷ","ᚹ","ᚺ","ᚾ","ᛁ","ᛃ","ᛇ"
]
# small unicode runic set for style

def make_name(parts=2):
    return ''.join(random.choice(SYLLABLES).capitalize() if i==0 else random.choice(SYLLABLES) for i in range(parts))

def make_sigil(seed=None, length=8):
    if seed:
        random.seed(seed)
    return ''.join(random.choice(RUNES) for _ in range(length))

def ascii_sigil(sig):
    # simple box
    return "+-{}-+\n| {} |\n+-{}-+".format('-'*len(sig), sig, '-'*len(sig))

if __name__ == "__main__":
    if len(sys.argv)>1 and sys.argv[1]=="name":
        print(make_name(parts=int(sys.argv[2]) if len(sys.argv)>2 else 2))
    elif len(sys.argv)>1 and sys.argv[1]=="sigil":
        print(ascii_sigil(make_sigil()))
    else:
        print("RuneGen CLI\nUsage: rune_gen.py name [parts]\n       rune_gen.py sigil")
