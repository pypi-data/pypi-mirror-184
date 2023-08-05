# bobcatpy

An asyncio based Python library to interact with the Bobcat Helium miner diagnostics API.

`bobcatpy` provides an alternative way to interact with the Bobcat diagnoser interface.


## Installation

`bobcatpy` is available through PyPi.

```
pip install bobcatpy
```

## Usage

```python
from bobcatpy import Bobcat
import asyncio

async def main():
    b = Bobcat("10.10.21.70")
    temps = await b.temps()
    print(temps)
    await b.close_session()

asyncio.run(main())
```

## Legacy Synchronous version
To use Bobcatpy in a synchronous fashion please use a version prior to v2.0.0
