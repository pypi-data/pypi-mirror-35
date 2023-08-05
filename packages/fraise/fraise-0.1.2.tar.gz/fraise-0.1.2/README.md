# fraise

A Python module for generating "correct horse battery staple" like random pass phrases.

## Installation

```
pip install fraise
```

## Usage
```
from fraise import fraise

password = fraise.generate()
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
