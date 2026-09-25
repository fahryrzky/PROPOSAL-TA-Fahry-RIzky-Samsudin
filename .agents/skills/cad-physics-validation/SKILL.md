---
name: cad-physics-validation
description: Analytical mechanical engineering screening and physics validation for CAD models. Computes bending stress, tip deflection, Euler column buckling, resonance frequency, pressure plate deflection, shaft sizing, and bolted/welded joint capacities. Produces cited PASS/FAIL scorecards with governing failure modes and safety factors before committing CAD geometry.
---

# CAD Physics Validation & Analytical Screening

A deterministic, first-principles analytical screening discipline for mechanical parts and assemblies.
Derived from [clay-good/anvilate](https://github.com/clay-good/anvilate).

> **Core Axiom**: Never hand a "silent green" to an unverified CAD model.
> A part that is strong enough on yield stress can easily fail on deflection or resonance. Stress scales with $t^{-2}$ while deflection scales with $t^{-3}$, so designing on stress alone is designing on the wrong governing limit.

---

## 1. Governing Mechanical Screening Formulations

### A. Beam Bending & Deflection (Cantilever & Supported)

1. **Second Moment of Area**:
   - Rectangular cross-section ($b \times h$): $I = \frac{b h^3}{12}$, section modulus $Z = \frac{b h^2}{6}$.
   - Solid circular shaft (diameter $d$): $I = \frac{\pi d^4}{64}$, polar moment $J = \frac{\pi d^4}{32}$.
   - Hollow circular tube ($D_o, D_i$): $I = \frac{\pi (D_o^4 - D_i^4)}{64}$.
2. **Bending Stress**:
   $$\sigma_b = \frac{M_{\text{max}} \cdot c}{I} = \frac{M_{\text{max}}}{Z}$$
   - Safety factor on yield: $n_{\sigma} = \frac{S_y}{\sigma_b} \ge n_{\text{req}}$ (typically $1.5 - 2.0$).
3. **Deflection Limits**:
   - Cantilever with point load at end: $\delta_{\text{max}} = \frac{F L^3}{3 E I}$.
   - Simply supported with center load: $\delta_{\text{max}} = \frac{F L^3}{48 E I}$.
   - Simply supported with uniform load $q$: $\delta_{\text{max}} = \frac{5 q L^4}{384 E I}$.
   - Allowable deflection criterion: $\delta_{\text{max}} \le \frac{L}{250}$ (structural) or $\delta \le \delta_{\text{clearance}}$ (precision mechanism).

### B. Column Buckling (Euler & Johnson)

1. **Critical Buckling Load (Euler)**:
   $$P_{\text{cr}} = \frac{\pi^2 E I}{(K L)^2}$$
   - Effective length factor $K$:
     - Pin-Pin: $K = 1.0$
     - Fixed-Free (cantilever): $K = 2.0$
     - Fixed-Pin: $K = 0.7$
     - Fixed-Fixed: $K = 0.5$
2. **Transition Slenderness Ratio**:
   $$\lambda = \frac{K L}{r}, \quad r = \sqrt{\frac{I}{A}}, \quad \lambda_c = \sqrt{\frac{2 \pi^2 E}{S_y}}$$
   - If $\lambda \ge \lambda_c$: Use Euler buckling equation.
   - If $\lambda < \lambda_c$: Use Johnson parabolic formula (inelastic buckling).

### C. Pressure-Loaded Plates & Covers

For a flat rectangular plate ($a \times b$, thickness $t$) under uniform pressure $P$:
1. **Governing Scaling**:
   - Maximum stress: $\sigma_{\text{max}} \propto \frac{P b^2}{t^2}$
   - Maximum deflection: $w_{\text{max}} \propto \frac{P b^4}{E t^3}$
2. **Boundary Clamping Effect**:
   - Clamped edges reduce maximum deflection by $>3\times$ compared to simply supported edges.
   - Declaring an edge `CLAMPED` requires verifiable physical bolting stiffness; otherwise assume `SIMPLY_SUPPORTED`.

### D. Rotating Transmission Shafts

A shaft experiences simultaneous torsion $T$ and bending moment $M$:
1. **von Mises Equivalent Stress**:
   $$\sigma' = \sqrt{\sigma_b^2 + 3 \tau^2} = \sqrt{\left(\frac{32 M}{\pi d^3}\right)^2 + 3 \left(\frac{16 T}{\pi d^3}\right)^2} \le \frac{S_y}{n}$$
2. **Torsional Deflection**:
   $$\theta = \frac{T L}{G J} \le \theta_{\text{allow}} \quad (\text{standard: } 1.0^\circ \text{ per 20 shaft diameters})$$

### E. Bolted & Threaded Connections

1. **Bolt Tensile Stress Area**: $A_t = 0.7854 \left(d - \frac{0.9382}{p}\right)^2$.
2. **Thread Engagement Length**:
   - Steel bolt in steel nut: $L_e \ge 1.0 d$.
   - Steel bolt in aluminum / 3D-printed plastic: $L_e \ge 1.8 - 2.5 d$.
3. **Minimum Edge Distance**: $e \ge 1.5 d$ (to prevent hole tear-out).

---

## 2. Standard Material Properties Database

| Material | Yield Strength $S_y$ (MPa) | Ultimate $S_{ut}$ (MPa) | Young's Modulus $E$ (GPa) | Density $\rho$ ($\text{g/cm}^3$) |
|---|---|---|---|---|
| **Al 6061-T6** | 276 | 310 | 68.9 | 2.70 |
| **Al 7075-T6** | 503 | 572 | 71.7 | 2.81 |
| **Structural Steel (A36)** | 250 | 400 | 200.0 | 7.85 |
| **Alloy Steel (4140 Q&T)**| 655 | 850 | 205.0 | 7.85 |
| **Stainless 304** | 205 | 515 | 193.0 | 8.00 |
| **PLA (3D Printed)** | 35–50 | 50–65 | 3.5 | 1.24 |
| **PETG (3D Printed)** | 40–50 | 50–55 | 2.1 | 1.27 |
| **Nylon PA12 (SLS)** | 32–45 | 48 | 1.7 | 1.01 |

---

## 3. Screening Scorecard Generation Pattern (Python)

```python
from dataclasses import dataclass
from typing import List

@dataclass
class CheckResult:
    check_name: str
    actual_value: float
    limit_value: float
    unit: str
    safety_factor: float
    passed: bool
    citation: str

class PhysicalScorecard:
    def __init__(self, part_name: str):
        self.part_name = part_name
        self.checks: List[CheckResult] = []

    def add_check(self, name: str, actual: float, limit: float, unit: str, req_sf: float, citation: str, is_upper_limit: bool = True):
        sf = limit / actual if is_upper_limit else actual / limit
        passed = sf >= req_sf
        self.checks.append(CheckResult(name, actual, limit, unit, sf, passed, citation))

    def evaluate(self) -> str:
        failed = [c for c in self.checks if not c.passed]
        governing = min(self.checks, key=lambda c: c.safety_factor) if self.checks else None
        
        status = "PASS" if not failed else "FAIL"
        report = [f"=== Scorecard for {self.part_name}: {status} ==="]
        for c in self.checks:
            tag = "[PASS]" if c.passed else "[FAIL]"
            report.append(f"{tag} {c.check_name}: {c.actual_value:.3f} vs limit {c.limit_value:.3f} {c.unit} (SF: {c.safety_factor:.2f}) [{c.citation}]")
        if governing:
            report.append(f"Governing mode: {governing.check_name} (SF: {governing.safety_factor:.2f})")
        return "\n".join(report)
```

---

## 4. Integration with CAD Authoring

When receiving a CAD task:
1. Run `cad-physics-validation` **first** to determine minimum thicknesses, beam heights, shaft diameters, and bolt hole counts.
2. Feed validated dimensions directly into the parametric modeling script (`build123d` or `OpenSCAD`).
3. Embed the generated scorecard into the technical documentation or drawing notes.
