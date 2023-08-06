import functools

import responses

from motivation import commands


def test_jm():
	res = commands.jm(None, None, "#inane", None, "")
	assert isinstance(res, str)


def test_schneier():
	res = commands.schneier(None, None, "#inane", None, "foo")
	assert 'foo' in res


add_fact = functools.partial(
	responses.add,
	responses.GET,
	'https://www.schneierfacts.com/',
)


@responses.activate
def test_schneier_all_caps():
	"At least one schneier fact features BRUCE SCHNEIER"
	add_fact('<p class="fact">How awesome is BRUCE SCHNEIER!</p>')
	res = commands.schneier(None, None, "#inane", None, "darwin")
	assert res == "How awesome is darwin!"


@responses.activate
def test_schneier_multi():
	"At least one schneier fact features the phrase twice"
	add_fact(
		'<p class="fact">How awesome is Bruce '
		'Schneier? Bruce Schneier!</p>',
	)
	res = commands.schneier(None, None, "#inane", None, "darwin")
	assert res == "How awesome is darwin? darwin!"


@responses.activate
def test_schneier_no_space():
	"At least one fact contains BRUCESCHNEIER"
	add_fact('<p class="fact">How awesome is BruceSchneier!</p>')
	res = commands.schneier(None, None, "#inane", None, "darwin")
	assert res == "How awesome is darwin!"


@responses.activate
def test_schneier_no_bruce():
	"At least one fact contains only 'schneier'"
	add_fact('<p class="fact">How awesome is Schneier!</p>')
	res = commands.schneier(None, None, "#inane", None, "darwin")
	assert res == "How awesome is darwin!"


@responses.activate
def test_schneier_no_schneier():
	"At least one fact contains only 'bruce'"
	add_fact('<p class="fact">How awesome is Bruce!</p>')
	res = commands.schneier(None, None, "#inane", None, "darwin")
	assert res == "How awesome is darwin!"
