# Python3 - SubPS

Wrapper script for subprocess usage.

It only uses builtin modules.

## Install

```bash
python3 -m pip install subps
```

See: [PyPI](https://pypi.org/project/subps/)

## Usage

```python3
from subps import process, process_out_err, process_out, process_err, process_rc

process(cmd='ls -l')
# dict('stdout': 'stdout...', 'stderr': 'stderr...', 'rc': 0)

process_out_err(cmd='ls -l')
# tuple('stdout...', 'stderr...')

process_out(cmd='ls -l')
# 'stdout...'

process_err(cmd='ls -l')
# 'stderr...'

process_rc(cmd='ls -l')
# 0
```
