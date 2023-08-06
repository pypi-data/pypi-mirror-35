#!/usr/bin/env python
import argparse
import sys
from lxml import etree

import requests
from gtts import gTTS
from html2text import HTML2Text
from requests.exceptions import RequestException


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--lang', default='en-US')
    parser.add_argument('-o', '--output', default='output.mp3')
    parser.add_argument('-p', '--path', default='//article')
    parser.add_argument('url')

    known_args, _ = parser.parse_known_args(sys.argv[1:])

    response = requests.get(known_args.url)

    try:
        response.raise_for_status()
    except RequestException as err:
        resp = err.response
        sys.stderr.write(
            '{} - {}\n'.format(
                resp.status_code,
                resp.content.decode('utf-8'),
            )
        )
        sys.exit(1)

    document = etree.HTML(response.content.decode('utf-8'))

    article = document.xpath(known_args.path)[0]

    h2txt = HTML2Text()
    h2txt.ignore_links = True

    text = '\n'.join([
        h2txt.handle(etree.tostring(p).decode('utf-8'))
        for p in article.xpath('//p')
        if p.text
    ])

    gTTS(
        lang=known_args.lang,
        slow=False,
        text=text
    ).save(known_args.output)


if __name__ == "__main__":
    main()
