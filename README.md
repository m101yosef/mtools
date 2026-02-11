# m101tools
A lightweight toolkit for ML projects with setup verification and GPU diagnostics.

## Installation
```bash
pip install git+https://github.com/m101yosef/m101tools.git
```

For development:
```bash
git clone https://github.com/m101yosef/m101tools.git
pip install -e ./m101tools[dev]
```

## Quick Start
```python
from mtools import SetupChecker

checker = SetupChecker(
    dependencies=["fastapi", "uvicorn", "torch"]
)
checker.run_all()
```

## Features

- Python and PyTorch version detection
- GPU memory monitoring via NVML
- Environment variable validation
- Dependency checking
- Programmatic access to all results

<br>
<br>

To be continue...
