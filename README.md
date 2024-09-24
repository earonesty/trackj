# trackj

A simple Python library for determining shipping carriers and generating tracking URLs from tracking numbers. Supports multiple carriers with regex-based detection.

## Installation

```bash
pip install trackj
```

Or using Poetry:

```bash
poetry add trackj
```

## Usage

Import the `trackj` module and use the available functions to match carriers, generate URLs, or get carrier IDs.

```python
import trackj

# Match a tracking number to a carrier and URL
result = trackj.match("1Z999AA10123456784")
print(result)  # {'carrier': 'ups', 'url': 'http://wwwapps.ups.com/...'}

# Get only the tracking URL
url = trackj.url("1Z999AA10123456784")
print(url)  # 'http://wwwapps.ups.com/...'

# Get only the carrier ID
carrier = trackj.carrier("1Z999AA10123456784")
print(carrier)  # 'ups'

# Access the full mapping of carriers, regex patterns, and URLs
print(trackj.MAP)
```

## Supported Carriers

- UPS
- FedEx
- USPS
- DHL
- Canada Post
- Royal Mail
- Australia Post
- China Post
- Japan Post
- Hermes UK
- GLS
- PostNL
- Correos Spain
- Deutsche Post
- Aramex
- SF Express

## License

MIT License
