# Compiler-Interpreter

This is PJP course project, focusing on compiler and interpreter development.
It's based on the [Project's definition](http://behalek.cs.vsb.cz/wiki/index.php/PLC_Project).

- **Pages:** https://martin-minarik.github.io/pjp-compiler-interpreter/

## Basic description

This project utilizes ANTLR for programming language processing. It focuses on parsing specified language, ensuring
syntactic correctness and thorough type checking, and generating executable stack-based instructions.
The project also includes an interpreter that executes these instructions.

---

## Installation

```bash
pip install -r requirements.txt
```

### Dependencies

- [antlr4](https://github.com/antlr/antlr4)
- [black](https://github.com/psf/black)
- [isort](https://github.com/PyCQA/isort)
- [pytest](https://github.com/PyCQA/isort)
- [pytest-cov](https://github.com/PyCQA/isort)
- [pytest-html](https://github.com/PyCQA/isort)
- [PyMarkdown](https://github.com/jackdewinter/pymarkdown)
- [MkDocs](https://github.com/mkdocs/mkdocs)
- [mkdocs-material](https://github.com/squidfunk/mkdocs-material)
- [mkdocs-minify-plugin](https://github.com/squidfunk/mkdocs-material)

## Usage

### compile.py

```shell
python main.py code.txt
```

- **options:**
  - `-o`, `--output_file`
  - `--no_output_file`
  - `-v`, `--verbose`
  - `-i`, `--interpret`
    - automatically runs virtual machine
  - `-h`, `--help`

### virtual_machine.py

```shell
python virtual_machine.py instructions.txt
```

## Chore

- Recompile antlr4 grammar
  - `antlr4 -Dlanguage=Python3 language/Language.g4 -visitor`
