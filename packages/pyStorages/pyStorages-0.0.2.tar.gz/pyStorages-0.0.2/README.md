# pyStorages

Simple data storages written in Python

### Currently supported storage types:
- JSON
- Pickle
- Redis

## Installation

```bash
pip install git+https://github.com/Cub11k/pyStorages.git
```

## Usage

```python
from storages import StorageType
from storages.sync_storages import load_storage

storage = load_storage(StorageType.JSON)

storage.set_data(
    test="test",
    test_int=5,
    test_list=[1, "2"],
    test_dict={"key1": 1, "key2": 2}
)
```

```python
import asyncio
from storages import StorageType
from storages.async_storages import load_storage


async def main():
    storage = await load_storage(StorageType.JSON)

    await storage.set_data(
        test="test",
        test_int=5,
        test_list=[1, "2"],
        test_dict={"key1": 1, "key2": 2}
    )

asyncio.run(main())
```