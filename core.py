from typing import Dict
import configparser

import requests

from etymologydatabase import EtymologyDatabase


def build_page_word(word: str) -> str:
    word = word.lower()
    word = word.strip()
    urls = get_urls_for_word(word)
    record_word_and_urls_to_database(word, urls)
    html = create_word_page(word, urls)
    return html


def record_word_and_urls_to_database(word: str, urls: Dict) -> None:
    config = configparser.ConfigParser()
    config.read('config.ini')
    filename = config['DATABASE']['path']
    db = EtymologyDatabase(filename)
    db.add_word_and_links(word, urls)
    return


def build_api_result_word(word: str, urls: Dict) -> Dict:
    results = {'word': word}
    results.update(urls)
    return results


def create_word_page(word: str, urls: Dict) -> str:
    links = ''
    for name, url in urls.items():
        section = f'<a href="{url}">{name}</a><br><br>'
        links += section
    html = f'<html><h1>{word}</h1>{links}</html>'
    return html


def get_urls_for_word(word: str) -> Dict[str, str]:
    urls = {'wiktionary': f'https://en.wiktionary.org/wiki/{word}#Etymology',
            'etymology_online': f'https://www.etymonline.com/word/{word}',
            'dictionary': f'https://www.dictionary.com/browse/{word}'}
    return {name: url for name, url in urls.items() if check_url_ok(url)}


def get_status_of_url(url: str) -> int:
    response = requests.head(url)
    return response.status_code


def check_url_ok(url: str) -> bool:
    return get_status_of_url(url) == 200
