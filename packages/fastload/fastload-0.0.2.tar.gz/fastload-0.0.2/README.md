# fastload

FastLoad downloads files faster using the same technology as IDM aiming to utilize the maximum available bandwidth for faster downloading.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install fastload.

```bash
pip install fastload
```

## Usage

```python
from fastload import FastLoad

def main():
    # e.g: https://www.cdn.xyz.mp4
    url = '<absolute_url_of_the file>'

    # Initialize the downloader
    fastload = FastLoad(url=url)

    # Start downloading
    fastload.download()

if __name__=='__main__':
    main()
```

## History

### 0.0.2

- Added a README.md file.
- Minor changes.

### 0.0.1

- First release on PyPI.
