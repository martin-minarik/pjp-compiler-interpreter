# SSP Final Project

This repository is a fork of the PJP class project, focusing on compiler and interpreter development.
It's based on the [Project's definition](http://behalek.cs.vsb.cz/wiki/index.php/PLC_Project).

## Basic description

This project utilizes ANTLR for programming language processing. It focuses on parsing specified language, ensuring
syntactic correctness and thorough type checking, and generating executable stack-based instructions.
The project also includes an interpreter that executes these instructions.

## Installation

```bash
pip install -r requirements.txt
```

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

## Hodnotící kritéria (CZ)

Požadavky na kvalitu práce:

* [x] GIT repozitář na Gitlabu.
    * [x] Repozitář má README.md (K čemu projekt slouží, jak se používá, jak se instaluje, jaké jsou prerekvizity,
      apod.)
* [x] Použití vlastního projektu (ideální kandidát má kombinaci jazyků - např. Python a BASH, Markdown a JS, apod.)
* [x] Vytvořená CI v repozitáři.
* [x] CI má minimálně tři úlohy:
    * [x] Test kvality Markdown stránek. (Kvalita dokumentace je důležitá. Minimálně README.md by mělo být v repozitáři
      dostupné.)
    * [x] Kontrola syntaxe každého jazyka.
    * [x] Použití "lint" nástroje pro každý jazyk.
* [ ] (Volitelné/doporučené) Nástroj na kontrolu dostupnosti aktualizací/security updates pro moduly jazyka (pokud
  existuje).
* [ ] (Volitelné/doporučené) Nástroj na kontrolu testů/code coverage (pokud existuje).
* [ ] (Volitelné/doporučené) Pokud některé nástroje umí generovat HTML reporty - umistěte je na Gitlab pages.
* [ ] (Volitelné/doporučené) Repozitář obsahuje šablonu ticketu.


