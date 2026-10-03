#1 Match a string that has an 'a' followed by zero or more 'b's.
import re

pattern = r"ab*"
for s in ["ac", "abc", "abbbc", "bbb", "a"]:
    print(f"{s!r:8} ->", "Match" if re.search(pattern, s) else "No match")

#2 Match a string that has an 'a' followed by two to three 'b's.
import re

pattern = r"ab{2,3}"
for s in ["ab", "abb", "abbb", "abbbb", "aabbc"]:
    print(f"{s!r:8} ->", "Match" if re.search(pattern, s) else "No match")

#3 Find sequences of lowercase letters joined with an underscore.
import re

text = "hello_world, my_var_name, Not_Match, another_one, nounderscore"
print(re.findall(r"\b[a-z]+_[a-z]+\b", text))
# For full snake_case words with several underscores
print(re.findall(r"\b[a-z]+(?:_[a-z]+)+\b", text))

#4 Find sequences of one upper case letter followed by lower case letters.
import re

text = "Hello World from Python, aBc DEF Xyz"
print(re.findall(r"[A-Z][a-z]+", text))

#5 Match a string that has an 'a' followed by anything, ending in 'b'.
import re

pattern = r"^a.*b$"
for s in ["ab", "acb", "a123b", "acbc", "bab", "a"]:
    print(f"{s!r:8} ->", "Match" if re.search(pattern, s) else "No match")

#6 Replace all occurrences of space, comma, or dot with a colon.
import re

text = "Python Exercises, Practice. Solution"
print(re.sub(r"[ ,.]", ":", text))

#7 Convert snake case string to camel case string.
import re

def snake_to_camel(s: str) -> str:
    #Upper-case the letter after each underscore and remove the underscore
    return re.sub(r"_([a-zA-Z0-9])", lambda m: m.group(1).upper(), s.lower())

for s in ["hello_world", "snake_case_to_camel_case", "alreadycamel"]:
    print(s, "->", snake_to_camel(s))

#8 Split a string at uppercase letters.
import re

def split_upper(s: str) -> list[str]:
    # (?=[A-Z]) is a zero-width lookahead: split *before* each capital letter
    return [p for p in re.split(r"(?=[A-Z])", s) if p]

print(split_upper("SplitAtUpperCaseLetters"))
print(split_upper("helloWorldFromPython"))

#9 Insert spaces between words starting with capital letters.
import re

def add_spaces(s: str) -> str:
    return re.sub(r"(\w)([A-Z])", r"\1 \2", s)

print(add_spaces("InsertSpacesBetweenWords"))
print(add_spaces("HelloWorld"))

#10 Convert a given camel case string to snake case.
import re

def camel_to_snake(s: str) -> str:
    # Insert '_' before every capital that is not at the start, then lower-case
    return re.sub(r"(?<!^)(?=[A-Z])", "_", s).lower()

for s in ["camelCaseString", "CamelCaseString", "helloWorld"]:
    print(s, "->", camel_to_snake(s))