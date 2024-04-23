# SSP Final Project

This repository is a fork of the PJP class project, focusing on compiler development.
It's based on the [Project's definition](http://behalek.cs.vsb.cz/wiki/index.php/PLC_Project).

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Example

```bash
python main.py code.txt # Compile code
python virtual_machine.py # Run compiled instructions
```
## Chore

- Recompile antlr4 grammar
    - `antlr4 -Dlanguage=Python3 language/Language.g4 -visitor`

## Hodnotící kritéria (CZ)

Požadavky na kvalitu práce:

* [x] GIT repozitář na Gitlabu.
  * [x] Repozitář má README.md (K čemu projekt slouží, jak se používá, jak se instaluje, jaké jsou prerekvizity, apod.)
* [x] Použití vlastního projektu (ideální kandidát má kombinaci jazyků - např. Python a BASH, Markdown a JS, apod.)
* [x] Vytvořená CI v repozitáři.
* [x] CI má minimálně tři úlohy:
  * [x] Test kvality Markdown stránek. (Kvalita dokumentace je důležitá. Minimálně README.md by mělo být v repozitáři dostupné.)
  * [x] Kontrola syntaxe každého jazyka.
  * [x] Použití "lint" nástroje pro každý jazyk.
* [ ] (Volitelné/doporučené) Nástroj na kontrolu dostupnosti aktualizací/security updates pro moduly jazyka (pokud existuje).
* [ ] (Volitelné/doporučené) Nástroj na kontrolu testů/code coverage (pokud existuje).
* [ ] (Volitelné/doporučené) Pokud některé nástroje umí generovat HTML reporty - umistěte je na Gitlab pages.
* [ ] (Volitelné/doporučené) Repozitář obsahuje šablonu ticketu.


