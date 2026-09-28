import pytest

from toolkit.__main__ import main

# Positive tests calculation

def test_cli_calc1(capsys):
    main(["calc", "2 + 2"])
    out = capsys.readouterr().out
    assert out.strip() == "4.0"

def test_cli_calc2(capsys):
    main(["calc", "2 + 2 * 3"])
    out = capsys.readouterr().out
    assert out.strip() == "8.0"

def test_cli_calc3(capsys):
    main(["calc", "-2 * (3 + 4) / (5 - 2)"])
    out = capsys.readouterr().out
    assert float(out.strip()) == pytest.approx(-14 / 3)


# Postive tests convertation

def test_cli_convert1(capsys):
    main(["convert", "1", "--from", "m", "--to", "cm"])
    out = capsys.readouterr().out
    assert out.strip() == "100.0 cm"

def test_cli_convert2(capsys):
    main(["convert", "100", "--from", "c", "--to", "f"])
    out = capsys.readouterr().out
    assert out.strip() == "212.0 f"

def test_cli_convert3(capsys):
    main(["convert", "1", "--from", "kg", "--to", "g"])
    out = capsys.readouterr().out
    assert out.strip() == "1000.0 g"


# Negative tests

def test_cli_no_args(capsys):
    with pytest.raises(SystemExit) as exc:
        main([])
    assert exc.value.code != 0

def test_cli_unknown_command(capsys):
    with pytest.raises(SystemExit):
        main(["wtf"])

def test_cli_missing_expression(capsys):
    with pytest.raises(SystemExit):
        main(["calc"])

def test_cli_missing_from(capsys):
    with pytest.raises(SystemExit):
        main(["convert", "100", "--to", "cm"])

def test_cli_missing_to(capsys):
    with pytest.raises(SystemExit):
        main(["convert", "100", "--from", "m"])

def test_cli_wrong_value(capsys):
    with pytest.raises(SystemExit):
        main(["convert", "abc", "--from", "m", "--to", "cm"])

def test_cli_different_units(capsys):
    with pytest.raises((SystemExit, Exception)):
        main(["convert", "1", "--from", "m", "--to", "kg"])