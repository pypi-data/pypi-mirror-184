# radiocc

> Provide a tool to compute radio occulations for planetary missions.

---

[Requirements](#requirements) |
[Installation](#installation) |
[Usage](#usage) |
[Configuration](#configuration) |
[Roadmap](#roadmap) |
[License](#license)

---

## Requirements

### Ubuntu 21.10

```sh
sudo apt install -y python3-gi libgirepository1.0-dev libcairo2-dev
gobject-introspection gir1.2-gtk-3.0
```

### Fedora 35

```sh
sudo dnf install gcc cairo-devel pkg-config python3-devel
gobject-introspection-devel cairo-gobject-devel gtk3
```

## Installation

```sh
# Create directory.
mkdir radiocc && cd radiocc

# Create virtual environnement to install package and activate it.
# Please read: https://docs.python.org/3/library/venv.html
python -m venv .env
source .env/bin/activate

# Install radiocc
pip install radiocc
```

## Usage

If you use **radiocc** as a command-line, you should read the
[command line guide][command-line-guide file].

If you decide to use it from Python, you should read the
[library guide][library-guide file].

## Configuration

**radiocc**
+ runs a list of input folders gathered in a "to_process" folder
+ writes the ouputs and saves figures in a "results" folder

To understand the config file, you should read the
[config file guide][config-file-guide file].

## Roadmap

+ improve old code for lisibility, portability and testing
+ optimise code speed
+ improve CLI interface, library API and config file for parameter tuning
+ provide GUI interface for parameter tuning and application of corrections

## License

Licensed under the [Apache 2.0 license][license file].

[repo url]: https://gitlab-as.oma.be/radiocc/radiocc
[pypi url]: https://pypi.org/project/radiocc
[command-line-guide file]: ./command-line-guide.md
[library-guide file]: ./doc/usage/library-guide.md
[config-file-guide file]: ./doc/usage/config-file-guide.md
[license file]: ./doc/usage/LICENSE
