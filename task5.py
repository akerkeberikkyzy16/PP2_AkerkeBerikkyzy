import re

#Functions
txt = "The rain in Spain stays mainly in the plain"
print("== search ==");  print(re.search(r"\bS\w+", txt).group(), re.search(r"\bS\w+", txt).span())
print("== match ==");   print(re.match(r"The", txt) is not None, re.match(r"rain", txt) is not None)
print("== findall =="); print(re.findall(r"ai", txt))
print("== split ==");   print(re.split(r"\s", txt), re.split(r"\s", txt, 1))
print("== sub ==");     print(re.sub(r"\s", "_", txt), re.sub(r"\s", "9", txt, 2))
print("== finditer =="); print([m.start() for m in re.finditer(r"ain", txt)])

#Metacharacters
print("\n== Metacharacters ==")
print("[] set        :", re.findall(r"[a-m]", "the rain"))
print("\\ escape      :", re.findall(r"\d", "that will be 59 dollars"))
print(".  any char   :", re.findall(r"he..o", "hello world"))
print("^  starts     :", bool(re.findall(r"^hello", "hello world")))
print("$  ends       :", bool(re.findall(r"world$", "hello world")))
print("*  0 or more  :", re.findall(r"he.*o", "hello world"))
print("+  1 or more  :", re.findall(r"he.+o", "hello world"))
print("?  0 or 1     :", re.findall(r"he.?o", "hello world"))
print("{} exactly    :", re.findall(r"he.{2}o", "hello world"))
print("|  either     :", re.findall(r"falls|stays", txt))
print("() group      :", re.search(r"(\d+)-(\d+)", "tel 123-4567").groups())

#Special sequences
print("\n== Special sequences ==")
s = "Python 3 is fun_2024!"
print(r"\A start    :", bool(re.findall(r"\APython", s)))
print(r"\b boundary :", re.findall(r"\bis\b", s))
print(r"\B not bound:", re.findall(r"\Bun\b", s))
print(r"\d digits   :", re.findall(r"\d", s))
print(r"\D non-dig  :", "".join(re.findall(r"\D", s)))
print(r"\s space    :", re.findall(r"\s", s))
print(r"\S non-space:", re.findall(r"\S+", s))
print(r"\w word     :", re.findall(r"\w+", s))
print(r"\W non-word :", re.findall(r"\W", s))
print(r"\Z end      :", bool(re.findall(r"fun_2024!\Z", s)))

#Sets
print("\n== Sets ==")
t = "Hello, World 123 rain"
print("[arn]    :", re.findall(r"[arn]", t))
print("[a-n]    :", re.findall(r"[a-n]", t))
print("[^arn]   :", "".join(re.findall(r"[^arn]", t)))
print("[0123]   :", re.findall(r"[0123]", t))
print("[0-9]    :", re.findall(r"[0-9]", t))
print("[0-5][0-9]:", re.findall(r"[0-5][0-9]", "a 59 b 61 c 07"))
print("[a-zA-Z] :", re.findall(r"[a-zA-Z]+", t))
print("[+]      :", re.findall(r"[+]", "1+2+3"))

#Quantifiers
print("\n== Quantifiers ==")
q = "aaa abab aab"
print("a{2}   :", re.findall(r"a{2}", q))
print("a{2,}  :", re.findall(r"a{2,}", q))
print("a{1,2} :", re.findall(r"a{1,2}", q))
print("greedy vs lazy:", re.findall(r"<.+>", "<a><b>"), re.findall(r"<.+?>", "<a><b>"))

#Flags
print("\n== Flags ==")
m = "First line\nsecond line\nThird LINE"
print("IGNORECASE :", re.findall(r"line", m, re.IGNORECASE))
print("MULTILINE  :", re.findall(r"^\w+", m, re.MULTILINE))
print("DOTALL     :", re.findall(r"First.*LINE", m, re.DOTALL))
print("VERBOSE    :", re.findall(r"""\d{3}   # area
                                     -        # dash
                                     \d{4}    # number""", "call 555-1234", re.VERBOSE))
print("ASCII      :", re.findall(r"\w+", "café", re.ASCII))

#Match object & named groups
print("\n== Match object ==")
mo = re.search(r"(?P<y>\d{4})-(?P<m>\d{2})-(?P<d>\d{2})", "Date: 2019-04-18")
print(mo.group(), mo.groupdict(), mo.span(), mo.string)