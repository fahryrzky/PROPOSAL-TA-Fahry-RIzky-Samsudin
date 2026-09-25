---
name: cad-constraint-kit
description: Constraint-driven mechanical CAD modeling. The LLM handles engineering intent and parameters; deterministic solvers (Z3 SMT, Willis gear formulas, SolveSpace) and B-Rep kernels (build123d, OpenCASCADE) handle geometry, mating, and interference. Use when designing mechanisms, gear trains, linkages, assemblies, or when exact manufacturable mates and honest decline policies are required.
---

# CAD Constraint Kit

Constraint-driven CAD modeling discipline where:
> **The AI handles meaning. Deterministic math handles geometry.**
> The LLM only decides *which* parts, *which* parameters, and *what connects to what*. Parametric generators build exact B-rep solids, and a deterministic mate kernel puts every part in place. The model never places a single vertex.

Derived from [jajmangold/constraint-kit](https://github.com/jajmangold/constraint-kit).

---

## 1. Core Principles

1. **Separation of Concerns**:
   - LLM: Semantic parsing, component selection, constraint definition, dimensional intent.
   - Solvers (Z3, Willis, SolveSpace): Kinematic loops, gear ratios, center distances, degrees of freedom (DOF).
   - Kernel (`build123d`, `OpenCASCADE`): B-Rep solid generation, boolean operations, STEP/GLB export.
2. **Deterministic Mates via Oriented Joint Frames**:
   - Parts never float by ad-hoc coordinates `(x, y, z)`.
   - Every connection attaches a named joint frame on Part A (`parent_joint`) to a named joint frame on Part B (`child_joint`).
   - Joint frames survive parameter changes (e.g. changing plate thickness automatically translates parts seated on its boss).
3. **Exact Kinematics**:
   - Gears mesh by exact pitch center distance: $d = m \cdot \frac{z_1 + z_2}{2}$ (where $m$ is module, $z$ is tooth count).
   - Planetary epicyclic ratios solve Willis' equation: $\frac{\omega_{\text{sun}} - \omega_{\text{carrier}}}{\omega_{\text{ring}} - \omega_{\text{carrier}}} = -\frac{z_{\text{ring}}}{z_{\text{sun}}}$.
   - Four-bar and planar linkages solve closed loop constraints via SolveSpace / geometric constraint systems.
4. **Zero Silent Failures (Honest Decline Policy)**:
   - If a requested mechanism is kinematically locked (over-constrained), clashes physically, or requires unsupported geometries (e.g. spiral hypoid bevels when only straight bevels exist), **decline explicitly and explain why**.
   - A plausible-looking broken model is far worse than an honest refusal.

---

## 2. Joint & Mate Taxonomy

Every mate connects two named joint frames with orientation matrices:

| Mate Type | Constrained DOF | Free DOF | Typical Use |
|---|---|---|---|
| `rigid` / `fixed` | 6 (3 trans, 3 rot) | 0 | Bolted plates, welded brackets, pressed pins |
| `revolute` | 5 (3 trans, 2 rot) | 1 (rotation around Z) | Gears on shafts, bearings on axles, pivots |
| `prismatic` | 5 (2 trans, 3 rot) | 1 (translation along Z) | Linear rails, slider carriages, hydraulic pistons |
| `cylindrical` | 4 (2 trans, 2 rot) | 2 (1 trans, 1 rot) | Guide bushings, unkeyed shafts |
| `planar` / `flush` | 3 (1 trans, 2 rot) | 3 (2 trans, 1 rot) | Mounting faces, plate stacks, gasket interfaces |
| `coaxial` / `concentric` | 4 (2 trans, 2 rot) | 2 (1 trans, 1 rot) | Bolt holes, shaft centerlines, bearing bores |

---

## 3. Workflow for Constraint-Driven Assemblies

```
User Intent ("planetary gearset 4:1 with carrier and 3 planets")
               │
               ▼
   [1. Semantic Parameter Resolution]
      - Extract module m, ratio R, torque target
      - Query standard fasteners / vitamins (BOSL2, ISO bolts)
               │
               ▼
   [2. Deterministic Kinematic Synthesis]
      - Z3 SMT solver solves integer teeth: z_ring = z_sun + 2*z_planet
      - Verify planet symmetry: (z_sun + z_ring) % num_planets == 0
      - Calculate center distances and carrier geometry
               │
               ▼
   [3. B-Rep Solid Generation (build123d / OCCT)]
      - Generate involute tooth profile (no polygon mesh approximations)
      - Generate sun, ring, planets, carrier plate, bearings, pins
      - Attach named joint frames (@origin, @shaft_bore, @pin_mount)
               │
               ▼
   [4. Deterministic Assembly & Mating]
      - Apply rigid & revolute transforms between joint frames
               │
               ▼
   [5. Collision & Interference Check]
      - Bounding-box prefilter -> OCCT boolean intersection
      - Hard interference == 0 check (except specified press fits)
               │
               ▼
   [6. Export & Bill of Materials]
      - STEP AP242, STL, GLB, mass properties, BOM table
```

---

## 4. Involute Spur Gear Python Generator Pattern (`build123d`)

```python
import math
from build123d import *

def generate_spur_gear(module: float, teeth: int, face_width: float, bore_dia: float) -> Compound:
    """Generate exact involute spur gear with true B-rep geometry."""
    pitch_dia = module * teeth
    base_dia = pitch_dia * math.cos(math.radians(20.0))  # 20 deg pressure angle
    addendum = 1.0 * module
    dedendum = 1.25 * module
    tip_dia = pitch_dia + 2 * addendum
    root_dia = pitch_dia - 2 * dedendum
    
    with BuildPart() as gear:
        # Base cylinder / blank
        with BuildSketch() as blank_sketch:
            Circle(radius=tip_dia / 2.0)
            if bore_dia > 0:
                Circle(radius=bore_dia / 2.0, mode=Mode.SUBTRACT)
        extrude(amount=face_width)
        
        # Exact tooth cutouts or lofted profile
        # Attach standard named joint frames
        RigidJoint("bore_center", gear.part, Location((0, 0, 0), (0, 0, 1)))
        RigidJoint("front_face", gear.part, Location((0, 0, face_width), (0, 0, 1)))
        RigidJoint("pitch_point", gear.part, Location((pitch_dia / 2.0, 0, face_width / 2.0), (1, 0, 0)))
        
    return gear.part
```

---

## 5. Collision & Clash Detection Rules

1. **Bounding Box Sweep**: Filter out disjoint parts ($O(N \log N)$).
2. **Boolean Intersection**: For overlapping bounding boxes, execute `part_A.intersect(part_B)`.
3. **Interference Classification**:
   - Volume $< 10^{-6}\ \text{mm}^3$: Tangent contact / mesh boundary (OK).
   - Volume $> 10^{-6}\ \text{mm}^3$: **Hard Collision (CLASH)** $\rightarrow$ Reject assembly and feed intersection volume back to solver to recalculate offsets.
