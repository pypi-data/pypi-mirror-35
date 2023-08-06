Run OpenAI Gym environments on an external process or remote machine using gRPC.

## Installation

[Install Gym] and run:

```sh
pip install gymx
```

It is recommended to use a [virtual environment].

## Usage

### Server

To start the server run:

```sh
python -m gymx
```

To use a different port run:

```sh
python -m gymx --port=54321
```

### Client

Inside your application use:

```py
from gymx import Env

env = Env('CartPole-v0')
```

To specify the server address use:

```py
env = Env('CartPole-v0', address='localhost:54321')
```

## License

[MIT][license]

[license]: /LICENSE
[virtual environment]: https://docs.python.org/3/library/venv.html
[install gym]: https://github.com/openai/gym#installation
