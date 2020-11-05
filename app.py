import configparser

from flask import Flask, render_template, redirect, url_for, request, jsonify

from etymologydatabase import EtymologyDatabase
import core

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('lookup_page.html')


@app.route('/lookup', methods=['GET'])
def lookup():
    word = request.args.get('word')
    if not word:
        return redirect(url_for('index'))

    word = word.lower()
    word = word.strip()
    urls = core.get_urls_for_word(word)
    core.record_word_and_urls_to_database(word, urls)
    return render_template('results_page.html', word=word, urls=urls)


@app.route('/all')
def all_temp():
    config = configparser.ConfigParser()
    config.read('config.ini')
    filename = config['DATABASE']['path']
    db = EtymologyDatabase(filename)
    data = db.get_word_all()
    return jsonify(data)
