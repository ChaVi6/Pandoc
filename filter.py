import sys
import panflute

headers = []


def headerFilter(elem, doc):
    if isinstance(elem, panflute.Header):
        text = panflute.stringify(elem)
        if text in headers:
            sys.stderr.write("Attention! Header '" + text + "' already exists in document.\n")
        else:
            headers.append(text)


def levelFilter(elem, doc):
    if isinstance(elem, panflute.Header):
        if elem.level > 2:
            return panflute.Header(panflute.Str(panflute.stringify(elem).upper()), level=elem.level)


def bold(doc):
    doc.replace_keyword('BOLD', panflute.Strong(panflute.Str('BOLD')))


if __name__ == '__main__':
    panflute.run_filters([headerFilter, levelFilter], finalize=bold)
