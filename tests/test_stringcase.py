"""Unit test for stringcase"""

import pytest

from src.stringcase import (
    alphanumcase,
    backslashcase,
    camelcase,
    capitalcase,
    constcase,
    dotcase,
    kebabcase,
    lowercase,
    pascalcase,
    pathcase,
    sentencecase,
    snakecase,
    spinalcase,
    titlecase,
    trimcase,
    uppercase,
)


@pytest.mark.parametrize(
    "expected, text_input",
    (
        ("fooBar", "foo_bar"),
        ("fooBar", "FooBar"),
        ("fooBar", "foo-bar"),
        ("fooBar", "foo.bar"),
        ("barBaz", "_bar_baz"),
        ("barBaz", ".bar_baz"),
        ("", ""),
        ("none", None),
    ),
)
def test_camelcase(expected, text_input):
    assert expected == camelcase(text_input)


@pytest.mark.parametrize(
    "expected, text_input",
    (
        ("FooBar", "fooBar"),
        ("", ""),
    ),
)
def test_capitalcase(expected, text_input):
    assert expected == capitalcase(text_input)


@pytest.mark.parametrize(
    "expected, text_input",
    (
        ("FOO_BAR", "fooBar"),
        ("FOO_BAR", "foo_bar"),
        ("FOO_BAR", "foo-bar"),
        ("FOO_BAR", "foo.bar"),
        ("_BAR_BAZ", "_bar_baz"),
        ("_BAR_BAZ", ".bar_baz"),
        ("", ""),
        ("NONE", None),
    ),
)
def test_constcase(expected, text_input):
    assert expected == constcase(text_input)


@pytest.mark.parametrize(
    "expected, text_input",
    (
        ("none", None),
        ("", ""),
        ("foo", "Foo"),
    ),
)
def test_lowercase(expected, text_input):
    assert expected == lowercase(text_input)


@pytest.mark.parametrize(
    "expected, text_input",
    (
        ("FooBar", "foo_bar"),
        ("FooBar", "foo-bar"),
        ("FooBar", "foo.bar"),
        ("BarBaz", "_bar_baz"),
        ("BarBaz", ".bar_baz"),
        ("", ""),
        ("None", None),
    ),
)
def test_pascalcase(expected, text_input):
    assert expected == pascalcase(text_input)


@pytest.mark.parametrize(
    "expected, text_input",
    (
        ("foo/bar", "fooBar"),
        ("foo/bar", "foo_bar"),
        ("foo/bar", "foo-bar"),
        ("foo/bar", "foo.bar"),
        ("/bar/baz", "_bar_baz"),
        ("/bar/baz", ".bar_baz"),
        ("", ""),
        ("none", None),
    ),
)
def test_pathcase(expected, text_input):
    assert expected == pathcase(text_input)


@pytest.mark.parametrize(
    "expected, text_input",
    (
        ("foo\\bar", "fooBar"),
        ("foo\\bar", "foo_bar"),
        ("foo\\bar", "foo-bar"),
        ("foo\\bar", "foo.bar"),
        ("\\bar\\baz", "_bar_baz"),
        ("\\bar\\baz", ".bar_baz"),
        ("", ""),
        ("none", None),
    ),
)
def test_backslashcase(expected, text_input):
    assert expected == backslashcase(text_input)


@pytest.mark.parametrize(
    "expected, text_input",
    (
        ("foo.bar", "fooBar"),
        ("foo.bar", "foo_bar"),
        ("foo.bar", "foo-bar"),
        ("foo.bar", "foo.bar"),
        (".bar.baz", "_bar_baz"),
        (".bar.baz", ".bar_baz"),
        ("", ""),
        ("none", None),
    ),
)
def test_dotcase(expected, text_input):
    assert expected == dotcase(text_input)


@pytest.mark.parametrize(
    "expected, text_input",
    (
        ("Foo bar", "fooBar"),
        ("Foo bar", "foo_bar"),
        ("Foo bar", "foo-bar"),
        ("Foo bar", "foo.bar"),
        ("Bar baz", "_bar_baz"),
        ("Bar baz", ".bar_baz"),
        ("", ""),
        ("None", None),
    ),
)
def test_sentencecase(expected, text_input):
    assert expected == sentencecase(text_input)


@pytest.mark.parametrize(
    "expected, text_input",
    (
        ("NONE", None),
        ("", ""),
        ("FOO", "foo"),
    ),
)
def test_uppercase(expected, text_input):
    assert expected == uppercase(text_input)


@pytest.mark.parametrize(
    "expected, text_input",
    (
        ("foo_bar", "fooBar"),
        ("foo_bar", "foo_bar"),
        ("foo_bar", "foo-bar"),
        ("foo_bar", "foo.bar"),
        ("_bar_baz", "_bar_baz"),
        ("_bar_baz", ".bar_baz"),
        ("", ""),
        ("none", None),
    ),
)
def test_snakecase(expected, text_input):
    assert expected == snakecase(text_input)


@pytest.mark.parametrize(
    "expected, text_input",
    (
        ("foo-bar", "fooBar"),
        ("foo-bar", "foo_bar"),
        ("foo-bar", "foo-bar"),
        ("foo-bar", "foo.bar"),
        ("-bar-baz", "_bar_baz"),
        ("-bar-baz", ".bar_baz"),
        ("", ""),
        ("none", None),
    ),
)
def test_spinalcase(expected, text_input):
    assert expected == spinalcase(text_input)
    assert expected == kebabcase(text_input)


@pytest.mark.parametrize(
    "expected, text_input",
    (
        ("Foo Bar", "fooBar"),
        ("Foo Bar", "foo_bar"),
        ("Foo Bar", "foo-bar"),
        ("Foo Bar", "foo.bar"),
        (" Bar Baz", "_bar_baz"),
        (" Bar Baz", ".bar_baz"),
        ("", ""),
        ("None", None),
    ),
)
def test_titlecase(expected, text_input):
    assert expected == titlecase(text_input)


@pytest.mark.parametrize(
    "expected, text_input",
    (
        ("foo bar baz", " foo bar baz "),
        ("", ""),
    ),
)
def test_trimcase(expected, text_input):
    assert expected == trimcase(text_input)


@pytest.mark.parametrize(
    "expected, text_input",
    (
        ("FooBar", "_Foo., Bar"),
        ("Foo123Bar", "Foo_123 Bar!"),
        ("", ""),
        ("None", None),
    ),
)
def test_alphanumcase(expected, text_input):
    assert expected == alphanumcase(text_input)
