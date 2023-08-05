# fraise

A Python module for generating "correct horse battery staple" like random pass phrases.

## Installation

```
pip install fraise
```

## Usage
```
# Import the package
import fraise

# By default, generate will return four lowercase words
passphrase = fraise.generate()

# You can set the number of words to include with word_count
passphrase = fraise.generate(word_count = 8)
```

## Contributing

Please fork the repository and raise a pull request (PR). PRs require one approval in order to be merged into the master branch.

Issue tracking is maintained on a public [Trello board](https://trello.com/b/ZiTGwaif/fraise). Please contact the repo owner if you would like access to the board. Commits should be prefixed with the Trello card ref, for example "FR-100 Did the thing". A link to the PR should be added to the card.

### Initial setup

```
make init
```

### Testing

```
make test
```

### Building

```
make build
```
