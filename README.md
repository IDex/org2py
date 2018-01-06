# Org2py
```
usage: org2py [-h] [-o OUTPUT] [-i INDENT] [-m] input

Generates Python class/function stumps from an Org file.

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
## Installation
Requires Python 3.6 or later
```
git clone https://github.com/IDex/org2py.git
cd org2py
pip install .
```
## Example usage

Following is an example of the kind of code the script generates

### Org outline
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
```
### Command used
```
[ide@ide-g500 org2py]$ org2py outline.org --main --indent "  " 
```
### Python code
```


class User:

  def __init__(self, user_id):
    self.user_id = user_id

  def get_game(latest):
    pass


class Game:

  def __init__(self, id, content, result, player):
    self.id = id
    self.content = content
    self.result = result
    self.player = player

  def save(output_file):
    pass

  def analyse():
    pass

  def download():
    pass


def process_games(user, total, latest, download_only, skip):
  pass


def main():
  pass


if __name__ == '__main__':
  main()
```
