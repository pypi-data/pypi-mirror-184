# Copyright Contributors to the Packit project.
# SPDX-License-Identifier: MIT

import copy

import pytest

from specfile.sections import Section, Sections


def test_find():
    sections = Sections(
        [
            Section("package"),
            Section("prep"),
            Section("changelog"),
            Section("pAckage foo"),
        ]
    )
    assert sections.find("prep") == 1
    assert sections.find("package foo") == 3
    with pytest.raises(ValueError):
        sections.find("install")


def test_get():
    sections = Sections([Section("package"), Section("package bar")])
    assert sections.get("package") == []
    assert sections.get("package bar") == []
    with pytest.raises(ValueError):
        sections.get("package foo")


def test_parse():
    sections = Sections.parse(
        [
            "0",
            "",
            "",
            "%prep",
            "0",
            "1",
            "2",
            "",
            "%package x",
            "%files y",
            "0",
            "%changelog",
        ]
    )
    assert sections[0][0] == "0"
    assert sections[1].id == "prep"
    assert sections.prep == ["0", "1", "2", ""]
    assert sections[2].id == "package x"
    assert not sections[2]
    assert sections[-1].id == "changelog"


def test_parse_case_insensitive():
    sections = Sections.parse(
        ["0", "", "%Prep", "0", "1", "2", "", "%pAckage x", "Requires: bar"]
    )
    assert sections[0][0] == "0"
    assert sections[1].id == "Prep"
    assert sections.prep == ["0", "1", "2", ""]
    assert sections[2].id == "pAckage x"
    assert sections[2] == ["Requires: bar"]


def test_parse_invalid_name():
    sections = Sections.parse(
        [
            "%description",
            "This is a description.",
            "",
            "%description(fr)",
            "Ceci est une description.",
            "",
        ]
    )
    assert len(sections) == 2  # including empty preamble
    assert sections[1].id == "description"
    assert sections.description[2] == "%description(fr)"


def test_copy_sections():
    sections = Sections([Section("package", ["Name: test", "Version: 0.1"])])
    shallow_copy = copy.copy(sections)
    assert shallow_copy == sections
    assert shallow_copy is not sections
    assert shallow_copy[0] is sections[0]
    deep_copy = copy.deepcopy(sections)
    assert deep_copy == sections
    assert deep_copy is not sections
    assert deep_copy[0] is not sections[0]


@pytest.mark.parametrize(
    "section, is_script",
    [
        ("package", False),
        ("install", True),
        ("PostUn", True),
        ("SourceList", False),
    ],
)
def test_is_script(section, is_script):
    assert Section(section).is_script == is_script
