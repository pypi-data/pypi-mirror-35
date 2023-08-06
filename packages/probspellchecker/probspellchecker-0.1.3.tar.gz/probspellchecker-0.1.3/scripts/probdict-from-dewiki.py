#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# grep '<page>' /storage/tmp/DE_Wikipedia/dewiki-20180220-pages-articles.xml | wc -l
# 4205618

import click
import codecs
from collections import Counter
import json
import re
import time
import xml.dom.minidom as minidom


def get_docs(input_stream):
    while input_stream:
        for line in input_stream:
            if "<page>" in line:
                break
        if "<page>" not in line:
            break
        page = u"<page>\n"
        for line in input_stream:
            if "</page>" in line:
                break
            page += line
        if "</page>" not in line:
            break
        page += u"</page>\n"
        dom = minidom.parseString(page.encode("utf-8"))
        title = " ".join(
            node.data
            for elt in dom.getElementsByTagName("title")
            for node in elt.childNodes
            if node.nodeType == node.TEXT_NODE
        )
        page = " ".join(
            node.data
            for elt in dom.getElementsByTagName("text")
            for node in elt.childNodes
            if node.nodeType == node.TEXT_NODE
        )
        yield get_words(title), get_words(page)


def get_words(text):
    return re.findall(r'\w+', text.lower(), flags=re.UNICODE)


@click.command()
@click.option("--input")
@click.option("--output", help="dictionary to write")
@click.option("--titles", help="write titles here", default="titles.txt")
@click.option("--n-docs", default=100000)
def make_dictionary(input, output, titles, n_docs):
    t_start = time.time()
    total_count, doc_count = 0, 0
    words = Counter()
    with codecs.open(input, "r", encoding="utf-8") as inp, open(titles, "wb") as titles:
        for title, text in get_docs(inp):
            total_count += 1
            if total_count % 1000 == 0:
                click.echo("{} doc {}, {} words... {}".format(time.ctime(), total_count, len(words), " ".join(title).encode("utf-8")))
            if ("liste" in title) \
            or ("datei" in title) \
            or ("wikipedia" in title) \
            or ("kategorie" in title) \
            or (len("".join(title)) < 4) \
            or (len(title) == 1 and title[0].isdigit()) \
            or (len(title) == 3 and title[0].isdigit() and title[1] == "v" and title[2] == "chr"):
                #click.echo("skipping {}".format(" ".join(title)))
                continue
            #click.echo("indexing {}...".format(" ".join(title)))
            titles.write("{}\n".format(" ".join(title).encode("utf-8")))
            words.update([w for w in title if not w.isdigit() and len(w) > 1 and "_" not in w])
            words.update([w for w in title if not w.isdigit() and len(w) > 1 and "_" not in w])  # title twice
            words.update([w for w in text if not w.isdigit() and len(w) > 1 and "_" not in w])
            doc_count += 1
            if total_count >= n_docs:
                click.echo("let's leave it at that")
                break
    click.echo("got {} words from {} docs ({:.1f} docs/s)".format(
        len(words), doc_count, doc_count/(time.time()-t_start),
    ))
    with open(output, "w") as out:
        out.write(json.dumps(dict(words)))


if __name__ == "__main__":
    make_dictionary()
