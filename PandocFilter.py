from panflute import *
import sys

headers = []

def changeHeader(elem, _):
    if isinstance(elem, Header) and elem.level > 2:
        return Header(Str(stringify(elem).upper()), level=elem.level)

def changeOnBold(file, _):
    file.replace_keyword("BOLD", Strong(Str("BOLD")))

def headerAlreadyExists(element, _):
    if isinstance(element, Header):
        text = stringify(element)
        if text in headers:
            print("Warning: duplicate header: " + text, file = stderr)
        else:
            headers.append(text)

if __name__ == "__main__":
    run_filters([headerAlreadyExists, changeHeader], prepare=changeOnBold)