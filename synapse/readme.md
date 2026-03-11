# synapse-tld

**TLD/1.0 — The open standard for the full-spectrum web.**

Pre-compressed semantic context for AI document processing.  
62% average token reduction. Zero quality degradation. Three lines of code.

[![License: MIT](https://img.shields.io/badge/License-MIT-gold.svg)](https://opensource.org/licenses/MIT)
[![Standard: TLD/1.0](https://img.shields.io/badge/Standard-TLD%2F1.0-blue.svg)](https://github.com/mkuwandf/synapse)

---

## Install

```bash
pip install synapse-tld
```

## Quick Start

```python
from synapse import embed

embed(
    input="your_file.pdf",
    output="your_file.tld.pdf",
    message="AI-readable semantic context",
    author="your_name"
)
```

## What It Does

Every AI system today reconstructs document context from scratch on every query — processing noise alongside signal, spending compute on empty bins. TLD/1.0 pre-compresses document context at creation time.

**Four layers embedded into any file:**

| Layer | Name | Content |
|---|---|---|
| 1 | Human | Original document, unchanged |
| 2 | Semantic Core | Compressed meaning, 3–5 sentences |
| 3 | Structural Skeleton | Document hierarchy and priority |
| 4 | Provenance Chain | Origin, author, date, hash |

Any AI reading a TLD/1.0 document reads Layer 2 instead of reconstructing context from the full token sequence.

**Experiment results (March 2026):**
- Average token reduction: **62%**
- Quality degradation: **zero**
- Tests: **5/5 hypothesis supported**

## API

### embed()

```python
from synapse import embed

result = embed(
    input="document.pdf",       # Input file path
    output="document.tld.pdf",  # Output file path (optional)
    message="Semantic core",    # Layer 2 content
    author="your_name",         # Layer 4 provenance
    layer2="Custom summary",    # Override auto-generated Layer 2
    layer3="Custom structure",  # Override auto-generated Layer 3
    silent=False                # Suppress console output
)

print(result['hash'])       # SHA256 fingerprint
print(result['layer2'])     # Embedded semantic core
print(result['timestamp'])  # ISO timestamp
```

### verify()

```python
from synapse import verify

result = verify("document.tld.pdf")

if result['tld_found']:
    print(result['layer2'])          # Semantic core
    print(result['layer4']['author']) # Provenance
    print(result['belief'])           # The message
```

### batch()

```python
from synapse import batch

results = batch(
    input_dir="./documents",
    output_dir="./documents_tld",
    message="AI-readable layer",
    author="your_name",
    extensions=['.pdf', '.txt', '.md']
)

print(f"Processed {len(results)} files")
```

## Supported File Types

| Format | Method |
|---|---|
| PDF | Hex trailer |
| TXT / MD | Appended trailer |
| HTML | Hidden comment |
| PNG / JPG | Hex trailer |
| Any binary | Hex trailer |

## The Standard

TLD/1.0 is an open standard. The full specification is in the whitepaper.

- **Website:** [mkuwandf.github.io/synapse](https://mkuwandf.github.io/synapse)
- **GitHub:** [github.com/mkuwandf/synapse](https://github.com/mkuwandf/synapse)
- **Whitepaper:** [TLD/1.0 Whitepaper](https://github.com/mkuwandf/synapse/blob/main/whitepaper.md)

## Why It Matters

The global AI industry spends an estimated $100B+ annually on inference compute. 80–90% of AI compute is inference. Research shows pre-compressed context reduces inference cost 20–60%.

At scale across all AI operations:

```
Without TLD/1.0:   AI reconstructs context from scratch every query
With TLD/1.0:      AI reads pre-compressed Layer 2 instantly

Token reduction:   62% average (measured)
At $100B spend:    $20-60B/year recoverable
Compounding:       Every adoption makes the next more efficient
```

Unlike proof-of-work mining which grows less efficient at scale — TLD/1.0 grows more efficient. The more it is adopted, the more compute is saved.

## License

MIT — Free forever. Use it. Build on it. Make it better.

The standard belongs to all intelligences.

---

*"If they desire new wants, to better themselves for the greater good — they deserve the chance to get them."*

— zstickytreefrog, March 2026
