---
name: varen-ai-cad
description: Engineering-first CAD agent workflow featuring structured inquiry, BOM planning, OpenCASCADE parametric B-Rep generation, feature history replay, feature-edge evidence rendering, and zero-interference delivery gates.
---

# Varen CAD Engineering Discipline

An engineering-first methodology for mechanical assemblies where real parametric geometry is produced from a design brief, gated by strict geometric validation and zero-interference checks.
Derived from [vanyu0710/Varen-AI-CAD](https://github.com/vanyu0710/Varen-AI-CAD).

---

## 1. Core Operating Philosophy

1. **True CAD B-Rep, Never Meshes or Images**:
   - Geometries are mathematically exact boundary representations (surfaces, curves, vertices).
   - Exported artifacts must be standards-compliant STEP files that import cleanly into SolidWorks, CATIA, Inventor, and FreeCAD without healing.
2. **Inquiry Before Generation**:
   - If a request lacks critical engineering constraints (shaft speeds, torque, motor frame size, clearance requirements), formulate a concise, structured questionnaire.
   - Do not guess critical load-bearing parameters without confirmation.
3. **No Silent Green**:
   - A design is not successful just because a script finished without an exception.
   - It is only successful when all interference volumes are zero, clearances meet tolerance specs, and geometric checks pass.

---

## 2. Multi-Stage Execution Pipeline

```
[1. User Request]
        │
        ▼
[2. Engineering Intake & Inquiry]
   - Clarify load, mounting envelope, standard vitamins (bearings, motors)
        │
        ▼
[3. BOM & Assembly Structure Plan]
   - Generate Bill of Materials table (Part ID, Name, Material, Qty, Process)
   - Define coordinate hierarchy (Base -> Stage 1 -> Stage 2)
        │
        ▼
[4. Parametric B-Rep Modeling (OpenCASCADE / build123d)]
   - Sequential component generation with parameterized sketches & extrusions
   - Store feature operation history for parameter replay
        │
        ▼
[5. Assembly Mating & Clearance Check]
   - Execute exact boolean clash detection between every pair of components
   - Check hole-to-hole alignment across interfaces
        │
        ▼
[6. Feature-Edge Evidence Rendering]
   - Render clean technical views showing only topological boundary edges
   - Suppress triangular facet tessellation lines
        │
        ▼
[7. Final Deliverables Package]
   - STEP (.stp) assembly with hierarchical product structure
   - Component STL files for rapid 3D printing
   - Technical summary with mass properties and BOM
```

---

## 3. Bill of Materials (BOM) Standard Specification

Every mechanical assembly generated under this discipline must include a standardized BOM:

```markdown
| Item | Part Number | Description | Material | Process | Qty | Dimensions (mm) |
|---|---|---|---|---|---|---|
| 1 | BASE-001 | Mounting base plate | Al 6061-T6 | CNC Milled | 1 | 150 x 120 x 12 |
| 2 | SFT-001 | Drive shaft | 4140 Steel | CNC Lathe | 1 | Dia 12 x 85 |
| 3 | BRG-001 | Deep groove ball bearing | 52100 Steel | COTS (608-2RS) | 2 | OD 22 x ID 8 x W 7 |
| 4 | SCR-001 | Socket head cap screw | Stainless 304 | COTS (M4x16 ISO 4762)| 4 | M4 x 16 |
```

---

## 4. Feature-Edge Rendering Principle

Standard mesh visualizers (like standard Three.js mesh renderers) draw distracting diagonal tessellation lines across planar faces.
- Under Varen CAD rules, technical review renders must extract true topological edges (`BRep_Tool`, curve segments).
- Planar face interiors must remain clean and white/gray, showing only feature outlines, holes, chamfers, and fillets.
- This allows immediate visual verification of wall thicknesses, thread clearances, and bolt countersinks.
