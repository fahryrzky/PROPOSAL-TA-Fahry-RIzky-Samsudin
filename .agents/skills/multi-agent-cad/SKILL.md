---
name: multi-agent-cad
description: Decoupled multi-agent architecture for text-to-CAD generation. Employs specialized Planner, Generator, Repairer, and Judge roles with test-time compute to generate valid parametric parts and multi-part assemblies with visual verification.
---

# Multi-Agent CAD (MAC) Architecture

A decoupled multi-agent engineering workflow for converting complex design briefs into validated, manufacturable CAD parts and assemblies.
Derived from [Pan-Chera/Multi-Agent-CAD](https://github.com/Pan-Chera/Multi-Agent-CAD).

---

## 1. Agent Roles & Separation of Responsibilities

```
                      [User Design Brief]
                               │
                               ▼
                        [Planner Agent]
               (Decomposes into BOM, part hierarchy,
                mating frames & dimension envelopes)
                               │
               ┌───────────────┴───────────────┐
               ▼                               ▼
       [Part 1 Generator]             [Part N Generator]
      (build123d / OCCT)              (build123d / OCCT)
               │                               │
               ▼                               ▼
        [Repairer Agent]                [Repairer Agent]
       (Fixes geometry /               (Fixes geometry /
        boolean errors)                 boolean errors)
               │                               │
               └───────────────┬───────────────┘
                               │
                               ▼
                      [Assembly Engine]
             (Solves mates & joint transformations)
                               │
                               ▼
                         [Judge Agent]
             (Multi-view orthogonal visual critique,
              interference & dimensional verification)
                               │
               ┌───────────────┴───────────────┐
            [PASS]                          [FAIL]
               │                               │
               ▼                               ▼
      [Export Artifacts]              [Repair Feedback Loop]
    (STEP, STL, GLB, URDF)           (Back to Planner/Generator)
```

---

## 2. Detailed Agent Specifications

### A. Planner Agent
- **Goal**: Convert ambiguous natural language into an unambiguous assembly tree and Bill of Materials (BOM).
- **Outputs**:
  - `components`: List of parts with bounding envelopes ($L \times W \times H$), materials, and fabrication processes (CNC, FDM, Sheet metal).
  - `mates`: Graph of kinematic connections (rigid, revolute, prismatic) between named joint frames.
  - `critical_dimensions`: Interface holes, shaft diameters, gear centerlines that must align.

### B. Generator Agent
- **Goal**: Write executable, idiomatic `build123d` or `cadquery` code for a single component.
- **Rules**:
  - Always use named parameters at the top of the file.
  - Anchor geometry to logical origins (e.g. mounting surface or primary bore center).
  - Expose named Joint objects (`RigidJoint`, `RevoluteJoint`) on mating surfaces.
  - Avoid fragile magic numbers; calculate derived features from root parameters.

### C. Repairer Agent
- **Goal**: Automatically intercept and resolve runtime kernel errors without user intervention.
- **Common Failure Modes & Fixes**:
  1. *Co-planar face boolean failure*:
     - Symptom: Cutout or hole fails with `Standard_ConstructionError` or leaves paper-thin ghost membranes.
     - Fix: Add a tiny overshoot offset ($\epsilon = 0.01 - 0.1\ \text{mm}$) to cutting solids.
  2. *Fillet radius too large*:
     - Symptom: `BRepBlend_StatusError` when fillet radius exceeds edge length.
     - Fix: Clamp maximum fillet radius to $r \le 0.4 \times \min(\text{adjacent edge lengths})$.
  3. *Zero-thickness wall / Non-manifold vertex*:
     - Symptom: Tangent circles or solids touching at an exact infinitesimal point.
     - Fix: Ensure overlap of at least $\epsilon = 0.05\ \text{mm}$ before boolean union.

### D. Judge / Verifier Agent
- **Goal**: Act as an adversarial quality gate. The Judge never wrote the code; its only job is inspection.
- **Verification Checklist**:
  1. *Geometric Validity*: Is `part.is_valid()` true? Is volume $> 0$? Are there non-manifold edges?
  2. *Interference*: Is boolean clash volume between any two distinct parts zero?
  3. *Visual Inspection*: Render 4 orthogonal views (Top, Front, Side, Isometric). Do holes go through? Are features aligned?
  4. *Brief Fidelity*: Does the model satisfy all specific dimensional requirements in the original prompt?

---

## 3. Test-Time Compute Strategy

When generating high-complexity mechanisms:
1. Generate $k = 3$ candidate implementations for the critical driving component.
2. Filter out scripts that fail compilation or produce invalid B-Reps.
3. Score remaining candidates based on DFM rules, feature cleanliness, and structural compactness.
4. Pass the winning candidate to the assembly integrator.
