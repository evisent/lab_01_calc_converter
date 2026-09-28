# Toolkit

Консольная утилита на Python: **калькулятор** арифметических выражений и **конвертер** единиц измерения

## Возможности

- Калькулятор: вычисление арифметичесиких выражений: `+`, `-`, `*`, `/`. Выполняется приоритет операций (сначала `*`, `/`, потом `+` и `-`). Поддерживаются скобки
- Конвертер длины: `m`, `mm`, `cm`, `km`
- Конвертер массы: `g`, `kg`
- Конвертер температуры: `c`, `f`, `k`

## Установка

```bash
pip install -e .
```

## Использование

### Калькулятор 

```bash
python -m toolkit calc "2+9"
# 11
```

### Конвертер

```bash
python -m toolkit convert 1 --from km --to m
# 1000.0
```

## Структура
```
lab_01/
  pyproject.toml
  README.md
  .gitignore
  src/toolkit/
    __init__.py
    __main__.py
    calculator.py
    converter.py
    errors.py
  tests/
    calculator_tests.py
    converter_tests.py
    cli_tests.py

```

## Тесты и линтер
```bash
python -m pytest
ruff check .
```
