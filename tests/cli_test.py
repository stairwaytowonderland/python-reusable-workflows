"""Tests for sample_app.cli."""
from sample_app.cli import main


def test_main_prints_hello_world(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello, world!\n"
