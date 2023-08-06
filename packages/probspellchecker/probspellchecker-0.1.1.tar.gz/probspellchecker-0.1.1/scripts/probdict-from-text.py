#!/usr/bin/python3
# -*- coding: utf-8 -*-

import click
from collections import Counter
import json
import re


def get_words(text):
    return re.findall(r"\w+", text.lower())


@click.command()
@click.option("--input-file", help="file to import")
@click.option("--dict-file", help="file to write dict to")
def main(input_file, dict_file):
    doc_count = 0
    words = Counter()
    with open(input_file, "r", encoding="utf-8") as inp:
        for line in inp:
            if line.startswith("<title>"):
                line = line[7:-8]
                if line.startswith("Wikipedia:"):
                    line = line[10:]
            elif line.startswith("<abstract>"):
                line = line[10:-11]
            else:
                continue
            words.update(get_words(line))
            doc_count += 1
    click.echo("got {} words from {} docs".format(len(words), doc_count))
    with open(dict_file, "w") as output:
        output.write(json.dumps(dict(words)))


if __name__ == "__main__":
    main()
