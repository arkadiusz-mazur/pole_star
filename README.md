# Description

Description of task you can find in pdf file in the same folder.

No authentication is needed to be able to acces API.

# Author

Arkadiusz Mazur

arkadiusz.mazur@hotmail.com

programmer.rails@gmail.com


## Installation

```bash
docker-compose up
```

## Usage
Main link:

http://localhost:8000/

Other example links:

http://127.0.0.1:8000/api/positions/

http://127.0.0.1:8000/api/ships/

JSON format example:

http://127.0.0.1:8000/api/positions.json?imo=9632179

## Data
IMO numbers to use:
9632179, 9247455, 9595321

# Tests
```bash
cd pytests
pytest tests.py
```