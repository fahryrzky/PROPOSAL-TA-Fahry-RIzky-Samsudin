---
name: cad-drawing-intelligence
description: Drawing intelligence and safe entity manipulation for 2D CAD (DXF, vector PDF, DWG) using ezdxf. Performs automated drawing health audits, layer protection, compliance verification, quantity takeoff (QTO), and structured entity edits.
---

# CAD Drawing Intelligence (DXF / 2D CAD)

An automated drawing intelligence and safe manipulation discipline for 2D CAD drawings, architectural floor plans, and mechanical fabrication cut sheets.
Derived from [jeremylongshore/cad-ai-agent](https://github.com/jeremylongshore/cad-ai-agent).

---

## 1. Core Operating Principles

1. **Safe Edits (Never Corrupt Raw CAD)**:
   - Modifications are performed via structured programmatic calls (`ezdxf`), never by raw text/regex hacking on DXF files.
   - Always adhere to the "Save-As" workflow: original source drawings are strictly preserved and versioned.
2. **Protected Layers Enforcement**:
   - Critical legal and metadata layers (`TITLE`, `TITLEBLOCK`, `BORDER`, `SEAL`, `STAMP`, `REVISION`) are permanently protected.
   - Any agent tool or script attempting to mutate or delete entities on protected layers must be intercepted and rejected.
3. **Drawing Health Quality Gate**:
   - Before handing off a DXF for laser cutting, waterjet, or architectural review, run a deterministic health audit:
     - Detect zero-length lines and degenerate arcs.
     - Identify duplicate overlapping line segments (double-cutting hazard).
     - Check for unclosed polyline boundaries intended for hatching or CNC profiling.
     - Detect unreferenced blocks and empty layers.

---

## 2. Common Drawing Intelligence Tasks

| Task | Methodology | Python Tooling |
|---|---|---|
| **Health Audit** | Scan entity table, calculate lengths, hash geometry for duplicates | `ezdxf`, `shapely` |
| **Quantity Takeoff (QTO)** | Filter entities by layer/block name; sum lengths, compute polygon areas | `ezdxf.path`, `shapely.geometry` |
| **Zone / Room Detection** | Extract closed polyline loops on boundary layers; calculate area & perimeter | `ezdxf.path.to_polygons` |
| **CNC Profile Validation** | Verify outer contour is a single continuous closed polyline with CW/CCW orientation | `ezdxf`, geometric loop tracer |
| **Layer Hygiene** | Purge unused layers, standardize color/lineweight by layer standard (AIA / ISO 128) | `doc.layers` manager |

---

## 3. Python `ezdxf` Health Audit & Cleaning Pattern

```python
import ezdxf
from collections import defaultdict

def audit_dxf_health(filepath: str) -> dict:
    doc = ezdxf.readfile(filepath)
    msp = doc.modelspace()
    
    report = {
        "total_entities": len(msp),
        "zero_length_lines": 0,
        "duplicate_lines": 0,
        "unclosed_polylines": 0,
        "layer_counts": defaultdict(int),
        "protected_layer_violations": []
    }
    
    seen_lines = set()
    protected_layers = {"TITLE", "TITLEBLOCK", "SEAL", "REVISION", "BORDER"}
    
    for entity in msp:
        report["layer_counts"][entity.dxf.layer] += 1
        
        if entity.dxftype() == 'LINE':
            start = (round(entity.dxf.start.x, 3), round(entity.dxf.start.y, 3))
            end = (round(entity.dxf.end.x, 3), round(entity.dxf.end.y, 3))
            
            # Zero length check
            if start == end:
                report["zero_length_lines"] += 1
                
            # Duplicate line check (order-independent)
            line_key = tuple(sorted([start, end]))
            if line_key in seen_lines:
                report["duplicate_lines"] += 1
            else:
                seen_lines.add(line_key)
                
        elif entity.dxftype() in ('LWPOLYLINE', 'POLYLINE'):
            if not entity.is_closed:
                report["unclosed_polylines"] += 1
                
    return report
```

---

## 4. Quantity Takeoff (QTO) Example

```python
def extract_quantity_takeoff(filepath: str, target_layers: list) -> dict:
    doc = ezdxf.readfile(filepath)
    msp = doc.modelspace()
    
    summary = {layer: {"total_length_m": 0.0, "count": 0} for layer in target_layers}
    
    for entity in msp:
        layer = entity.dxf.layer
        if layer in summary:
            summary[layer]["count"] += 1
            if entity.dxftype() == 'LINE':
                summary[layer]["total_length_m"] += entity.dxf.start.distance(entity.dxf.end) / 1000.0
            elif entity.dxftype() == 'LWPOLYLINE':
                # Sum segment lengths
                pts = entity.get_points(format='xy')
                for i in range(len(pts) - 1):
                    p1, p2 = pts[i], pts[i+1]
                    dist = ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5
                    summary[layer]["total_length_m"] += dist / 1000.0
                    
    return summary
```
