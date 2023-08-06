<h1 align="center">
    <img src="https://raw.githubusercontent.com/shinigamilib/shinigami-py/main/assets/shinigami_logo.png" />
</h1>

<p align="center">
    <b>Shinigami was created to be simplistic and maintainable</b>
</p>

Shinigami is an open source Python library allowing the user to generate and build Dockerfiles during runtime.

## Usage

You can install Shinigami via pip:
```bash
pip install shinigami
```

### Quick Example
```python
from shinigami.shinigami import Shinigami

def create_file():
    Shinigami(lang_os="python", version="3.9", build=True).generate_dockerfile()

if __name__ == '__main__':
    create_file()
```

If you just want to generate the Dockerfile without building the container, you can do that too. Just remove the `build` boolean from the class and you should see a Dockerfile populate in your current directory within seconds.

There are currently 3 seperate parameters you can choose from:

- `lang_os` (`str`)   - The language or operating system you should like to pull from Docker Hub (Example: `ubuntu`)
- `version` (`str`)   - The version of the language or operating system (Example: `22.04`)
- `build`   (`bool`)  - This allows you to choose if you would like to build the Docker container or just pull the Dockerfile without building
- `verbose`   (`bool`)  - Logs information to stdout