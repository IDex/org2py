# Org2py
```
usage: org2py [-h] [-o OUTPUT] [-i INDENT] [-m] input

Generates Python class/function stubs from an Org file.

positional arguments:
  input                 Org file to parse.

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output file for the generated code, by default STDOUT.
  -i INDENT, --indent INDENT
                        Indentation for generated code (e.g. " "), by default 4 spaces.
  -m, --main            Add "if __name__" boilerplate to the end, by default off.
```
## Format interpretation
* The lines starting with a star are either classes, methods, or functions.

    * If the first letter is capitalized the line is interpreted as a class.

    * If a function is under a class it's a method.

* Lines without a star are interpreted as a comma-separated list of parameters for above class/function.
## Installation
Requires Python 3.6 or later (Uses f-strings).
```
git clone https://github.com/IDex/org2py.git
cd org2py
pip install .
```
## Example usage

Following is an example of the kind of code the script generates.

### Org file
```
* User
  user_id
** get_game
   latest
* Game
  id, content, result, player
** save
   output_file
** analyse
** download
* process_games
  user,  total,latest,download_only,skip
** inner_function
* another_function
argument
```
### Command used
```
org2py outline.org --main --indent "  "
```
### Resulting Python code
```


class User:

  def __init__(self, user_id):
    self.user_id = user_id

  def get_game(self, latest):
    pass


class Game:

  def __init__(self, id, content, result, player):
    self.id = id
    self.content = content
    self.result = result
    self.player = player

  def save(self, output_file):
    pass

  def analyse(self):
    pass

  def download(self):
    pass


def process_games(user, total, latest, download_only, skip):
  pass

  def inner_function():
    pass


def another_function(argument):
  pass


def main():
  pass


if __name__ == '__main__':
  main()
```
