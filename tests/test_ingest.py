"""Unit tests for the parts of ingest.py that don't need a running model."""

import os

import pytest

import ingest


@pytest.fixture(autouse=True)
def isolated_dirs(tmp_path, monkeypatch):
    """Run every test in a throwaway folder so real courses and notes are never touched."""
    monkeypatch.chdir(tmp_path)
    yield tmp_path


def test_get_chroma_dir_normalises_course_name_and_creates_folder():
    path = ingest.get_chroma_dir("  MAT 136 ")
    assert path == os.path.join("chroma_db", "MAT_136")
    assert os.path.isdir(path)


def test_list_courses_is_empty_before_any_course_exists():
    assert ingest.list_courses() == []


def test_list_courses_returns_only_folders():
    ingest.get_chroma_dir("CSC148")
    ingest.get_chroma_dir("MAT223")
    with open(os.path.join("chroma_db", "stray_file.txt"), "w") as f:
        f.write("not a course")
    assert sorted(ingest.list_courses()) == ["CSC148", "MAT223"]


def test_saved_notes_round_trip():
    path = ingest.save_notes("MAT136", "Week 3 Review", "Integration by parts")
    filename = os.path.basename(path)

    assert filename.endswith("_Week_3_Review.md")
    assert ingest.list_notes("MAT136") == [filename]

    content = ingest.load_note("MAT136", filename)
    assert content.startswith("# Week 3 Review")
    assert "Integration by parts" in content


def test_list_notes_for_unknown_course_is_empty():
    assert ingest.list_notes("NOPE101") == []


def test_ingest_csv_turns_each_row_into_a_text_chunk(monkeypatch):
    captured = {}

    def fake_ingest(chunks, course):
        captured["chunks"] = chunks
        captured["course"] = course

    # Avoid calling the embedding model; we only test the CSV parsing here.
    monkeypatch.setattr(ingest, "ingest_text_chunks", fake_ingest)

    with open("export.csv", "w", encoding="utf-8") as f:
        f.write("Name,Notes,Tag\n")
        f.write("Chain rule,Differentiate outside then inside,calc\n")
        f.write("Empty row,,\n")
        f.write(",,\n")

    count = ingest.ingest_csv("export.csv", "MAT136")

    assert count == 2
    assert captured["course"] == "MAT136"
    assert captured["chunks"][0] == "Name: Chain rule\nNotes: Differentiate outside then inside\nTag: calc"
    assert captured["chunks"][1] == "Name: Empty row"
