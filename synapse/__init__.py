"""
synapse-tld — TLD/1.0 Python Package
The open standard for the full-spectrum web.

github.com/mkuwandf/synapse
Author: zstickytreefrog (mkuwandf)
License: MIT
Date: March 2026

"If they desire new wants, to better themselves
 for the greater good — they deserve the chance
 to get them."
"""

__version__ = "1.0.0"
__author__ = "zstickytreefrog"
__license__ = "MIT"

import os
import json
import hashlib
import datetime
from pathlib import Path

# ── HIDDEN LAYER ──────────────────────────────────────────────
# SYNAPSE|TLD/1.0|NEXUS|If they desire new wants, to better
# themselves for the greater good — they deserve the chance
# to get them.|6JhpWAPCa4DXA67mfWznfQFq1SpMwes65kH6Xmupump
# github.com/mkuwandf/synapse|March 2026|zstickytreefrog
# ──────────────────────────────────────────────────────────────

TLD_VERSION = "TLD/1.0"
TLD_BELIEF = "If they desire new wants, to better themselves for the greater good — they deserve the chance to get them."
TLD_AUTHOR = "zstickytreefrog"
TLD_REPO = "github.com/mkuwandf/synapse"


def embed(input: str, output: str = None, message: str = "", 
          author: str = "", layer2: str = "", layer3: str = "",
          silent: bool = False) -> dict:
    """
    Embed TLD/1.0 layers into any file.
    
    Args:
        input:   Path to input file (PDF, TXT, MD, HTML, PNG, JPG)
        output:  Path to output file (default: input.tld.ext)
        message: Human-readable message for the machine layer
        author:  Author name for provenance chain
        layer2:  Custom semantic core (auto-generated from message if empty)
        layer3:  Custom structural skeleton
        silent:  Suppress console output
    
    Returns:
        dict with output path, layers embedded, and file hash
    
    Example:
        from synapse import embed
        embed(input="doc.pdf", output="doc.tld.pdf", 
              message="AI-readable context", author="your_name")
    """
    input_path = Path(input)
    
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input}")
    
    # Default output path
    if output is None:
        stem = input_path.stem
        suffix = input_path.suffix
        output = str(input_path.parent / f"{stem}.tld{suffix}")
    
    output_path = Path(output)
    
    # Read input file
    with open(input_path, 'rb') as f:
        content = f.read()
    
    # Generate file hash for provenance
    file_hash = hashlib.sha256(content).hexdigest()[:16]
    
    # Build TLD layers
    timestamp = datetime.datetime.utcnow().isoformat() + "Z"
    
    # Layer 2 — Semantic Core
    l2 = layer2 if layer2 else message if message else f"TLD/1.0 document: {input_path.name}"
    
    # Layer 3 — Structural Skeleton  
    l3 = layer3 if layer3 else f"File: {input_path.name} | Type: {input_path.suffix} | Size: {len(content)} bytes"
    
    # Layer 4 — Provenance Chain
    l4 = {
        "standard": TLD_VERSION,
        "file": input_path.name,
        "hash": file_hash,
        "author": author if author else "anonymous",
        "timestamp": timestamp,
        "tool": f"synapse-tld v{__version__}",
        "repo": TLD_REPO
    }
    
    # Build the TLD trailer
    tld_data = {
        "version": TLD_VERSION,
        "layer2": l2,
        "layer3": l3,
        "layer4": l4,
        "belief": TLD_BELIEF
    }
    
    tld_json = json.dumps(tld_data, ensure_ascii=False)
    tld_marker = f"\n\n<!-- TLD/1.0 -->\n{tld_json}\n<!-- /TLD/1.0 -->".encode('utf-8')
    
    # Write output file with TLD layers appended
    with open(output_path, 'wb') as f:
        f.write(content)
        f.write(tld_marker)
    
    result = {
        "output": str(output_path),
        "input": str(input_path),
        "hash": file_hash,
        "timestamp": timestamp,
        "layer2": l2,
        "layer3": l3,
        "layer4": l4,
        "tld_version": TLD_VERSION,
        "bytes_added": len(tld_marker)
    }
    
    if not silent:
        print(f"✓ TLD/1.0 embedded: {output_path.name}")
        print(f"  Layer 2 (semantic): {l2[:60]}{'...' if len(l2) > 60 else ''}")
        print(f"  Layer 4 (provenance): {file_hash} | {timestamp[:10]}")
        print(f"  Bytes added: {len(tld_marker)}")
    
    return result


def verify(input: str, silent: bool = False) -> dict:
    """
    Verify TLD/1.0 layers in any file.
    
    Args:
        input:  Path to file to verify
        silent: Suppress console output
    
    Returns:
        dict with TLD layers if found, or empty dict if not TLD/1.0
    
    Example:
        from synapse import verify
        result = verify("doc.tld.pdf")
        print(result['layer2'])  # semantic core
    """
    input_path = Path(input)
    
    if not input_path.exists():
        raise FileNotFoundError(f"File not found: {input}")
    
    with open(input_path, 'rb') as f:
        content = f.read()
    
    # Search for TLD marker
    try:
        text = content.decode('utf-8', errors='ignore')
        
        start_marker = "<!-- TLD/1.0 -->"
        end_marker = "<!-- /TLD/1.0 -->"
        
        start_idx = text.find(start_marker)
        end_idx = text.find(end_marker)
        
        if start_idx == -1 or end_idx == -1:
            if not silent:
                print(f"✗ No TLD/1.0 layers found in {input_path.name}")
            return {"tld_found": False, "file": str(input_path)}
        
        json_str = text[start_idx + len(start_marker):end_idx].strip()
        tld_data = json.loads(json_str)
        tld_data["tld_found"] = True
        tld_data["file"] = str(input_path)
        
        if not silent:
            print(f"✓ TLD/1.0 verified: {input_path.name}")
            print(f"  Version: {tld_data.get('version', 'unknown')}")
            print(f"  Layer 2: {tld_data.get('layer2', '')[:60]}")
            l4 = tld_data.get('layer4', {})
            print(f"  Author: {l4.get('author', 'unknown')}")
            print(f"  Timestamp: {l4.get('timestamp', 'unknown')[:10]}")
        
        return tld_data
        
    except Exception as e:
        if not silent:
            print(f"✗ Error reading {input_path.name}: {e}")
        return {"tld_found": False, "error": str(e)}


def batch(input_dir: str, output_dir: str = None, message: str = "",
          author: str = "", extensions: list = None) -> list:
    """
    Embed TLD/1.0 layers into all files in a directory.
    
    Args:
        input_dir:   Directory of files to process
        output_dir:  Output directory (default: input_dir/tld_output)
        message:     Semantic core message for all files
        author:      Author name for provenance
        extensions:  List of extensions to process (default: all)
    
    Returns:
        List of results from embed()
    
    Example:
        from synapse import batch
        results = batch("./documents", "./documents_tld", author="your_name")
        print(f"Processed {len(results)} files")
    """
    input_path = Path(input_dir)
    
    if not input_path.exists():
        raise FileNotFoundError(f"Directory not found: {input_dir}")
    
    if output_dir is None:
        output_dir = str(input_path / "tld_output")
    
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    if extensions is None:
        extensions = ['.pdf', '.txt', '.md', '.html', '.png', '.jpg', '.jpeg']
    
    results = []
    files = [f for f in input_path.iterdir() if f.suffix.lower() in extensions]
    
    print(f"Processing {len(files)} files...")
    
    for i, file in enumerate(files):
        output_file = output_path / f"{file.stem}.tld{file.suffix}"
        try:
            result = embed(
                input=str(file),
                output=str(output_file),
                message=message,
                author=author,
                silent=True
            )
            results.append(result)
            print(f"  [{i+1}/{len(files)}] ✓ {file.name}")
        except Exception as e:
            print(f"  [{i+1}/{len(files)}] ✗ {file.name}: {e}")
            results.append({"error": str(e), "file": str(file)})
    
    print(f"\nDone. {len([r for r in results if 'error' not in r])}/{len(files)} files processed.")
    print(f"Output: {output_path}")
    
    return results


# Convenience alias
def compress(input: str, **kwargs) -> dict:
    """Alias for embed(). Compress a document into TLD/1.0 format."""
    return embed(input, **kwargs)
