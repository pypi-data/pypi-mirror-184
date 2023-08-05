# auto-device

Automatically assign devices in-line with pytorch code

### Usage

```python
from autodevice import AutoDevice

x = torch.randn([200, 50]).to(AutoDevice())
```

### Installation

```
pip install auto-device
```