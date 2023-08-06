# -*- coding: utf-8 -*-

import random
import re
import html.parser

import requests
import pmxbot
from pmxbot.core import command
from pmxbot.karma import Karma
import ftfy


@command(aliases='piratemotivate')
def pm(client, event, channel, nick, rest):
    'Arggh matey'
    if rest:
        rest = rest.strip()
        Karma.store.change(rest, 2)
        rcpt = rest
    else:
        rcpt = channel

    if random.random() > 0.95:
        return f"Arrggh ye be doin' great, grand work, {rcpt}!"
    return f"Arrggh ye be doin' good work, {rcpt}!"


@command(aliases='latinmotivate')
def lm(client, event, channel, nick, rest):
    'Rico Suave'
    if rest:
        rest = rest.strip()
        Karma.store.change(rest, 2)
        rcpt = rest
    else:
        rcpt = channel
    return f'¡Estás haciendo un buen trabajo, {rcpt}!'


@command(aliases='frenchmotivate')
def fm(client, event, channel, nick, rest):
    'pmxbot parle français'
    if rest:
        rest = rest.strip()
        Karma.store.change(rest, 2)
        rcpt = rest
    else:
        rcpt = channel
    return f'Vous bossez bien, {rcpt}!'


@command(aliases='japanesemotivate')
def jm(client, event, channel, nick, rest):
    if rest:
        rest = rest.strip()
        Karma.store.change(rest, 2)
        rcpt = rest
    else:
        rcpt = channel

    hon_romaji = ' san'
    hon_ja = ' さん'

    # Use correct honorific.
    bosses = pmxbot.config.get('bosses', set())
    if any(rcpt.lower().startswith(boss_nick) for boss_nick in bosses):
        hon_romaji = ' sensei'
        hon_ja = ' 先生'

    elif rcpt == channel:
        hon_romaji = ''
        hon_ja = ''

    emoji = '(^_−)−☆'

    return (
        f'{rcpt}{hon_ja}, あなたわよくやっています! '
        f'({rcpt}{hon_romaji}, anata wa yoku yatte '
        f'imasu!)  -  {emoji}'
    )


@command(aliases=('kurdishmotivate', 'km'))
def zorsupas(client, event, channel, nick, rest):
    'Zor supas! — !زۆر سوپاس'
    if rest:
        rest = rest.strip()
        Karma.store.change(rest, 1)
        rcpt = rest
    else:
        rcpt = channel
    return (
        f'Zor supas {rcpt}, to zor zor barezi! —'
        ' زۆر سوپاس، تۆ زۆر زۆر به‌ره‌زی'
    )


@command(aliases=('dankeschoen', 'ds'))
def danke(client, event, channel, nick, rest):
    'Danke schön!'
    if rest:
        rest = rest.strip()
        Karma.store.change(rest, 1)
        rcpt = rest
    else:
        rcpt = channel
    return f'Danke schön, {rcpt}! Danke schön!'


@command(aliases=('germanmotivate',), doc='German motivate')
def gm(client, event, channel, nick, rest):
    if rest:
        rest = rest.strip()
        Karma.store.change(rest, 1)
        rcpt = rest
    else:
        rcpt = channel
    return f'Du leistest gute Arbeit, {rcpt}!'


@command('esperantomotivate', aliases=('em',), doc='Esperanto motivate')
def em(client, event, channel, nick, rest):
    if rest:
        rest = rest.strip()
        Karma.store.change(rest, 2)
        rcpt = rest
    else:
        rcpt = channel
    return f'Vi faras bonan laboron, {rcpt}!'


@command(aliases=('рm', 'rm'), doc="Motivate nick на русском")
def russianmotivate(client, event, channel, nick, rest):
    if rest:
        rest = rest.strip()
        Karma.store.change(rest, 1)
        rcpt = rest
    else:
        rcpt = channel
    return f'Вы делаете хорошую работу, {rcpt}!'


@command()
def schneier(client, event, channel, nick, rest):
    'schneier "facts"'
    rcpt = rest.strip() or channel
    if rest.strip():
        Karma.store.change(rcpt, 2)

    url = 'https://www.schneierfacts.com/'
    d = requests.get(url).text
    start_tag = re.escape('<p class="fact">')
    end_tag = re.escape('</p>')
    p = re.compile(
        start_tag + '(.*?)' + end_tag,
        flags=re.DOTALL | re.MULTILINE)
    match = p.search(d)

    if not match:
        return "Sorry, no facts found (check your crypto anyway)."
    phrase = match.group(1).replace('\n', ' ').strip()
    if rcpt != channel:
        phrase = re.sub('(Bruce ?)?Schneier', rcpt, phrase, flags=re.I)
        phrase = re.sub('Bruce', rcpt, phrase, flags=re.I)

    # unescape HTML
    h = html.parser.HTMLParser()
    phrase = h.unescape(phrase)

    # Correct improperly-encoded strings
    phrase = ftfy.fix_encoding(phrase)

    return phrase
