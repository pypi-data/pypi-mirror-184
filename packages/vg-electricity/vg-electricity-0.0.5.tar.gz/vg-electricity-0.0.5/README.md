# vg-electricity-py



## Getting started

```python
from vgelectricity import VGElectricity
import asyncio

async def main():
    vg = VGElectricity()
    print(await vg.sensor_data())
    await vg.close_session()

asyncio.run(main())
```
