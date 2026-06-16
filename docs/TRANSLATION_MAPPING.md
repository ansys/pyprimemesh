# PolyData ↔ USD Translation Mapping

## Translation Feasibility

The translation between PyVista PolyData and OpenUSD is **straightforward and clean** because both ultimately represent the same underlying geometry primitives.

## Data Flow Comparison

### Current PolyData Flow
```
Connectivity Results (raw arrays)
  ├─ node_coords: [x0, y0, z0, x1, y1, z1, ...]  (flat)
  ├─ face_list: [count, v0, v1, v2, count, v0, v1, ...]  (VTK format)
  └─ edge_list: [count, v0, v1, count, v0, v1, ...]  (VTK format)
           ↓
       Mesh._get_vertices_and_surf_faces()
           ↓
       vertices: [[x0, y0, z0], [x1, y1, z1], ...]  (N, 3) array
       faces: [count, v0, v1, v2, ...]  (packed list)
           ↓
       pv.PolyData(vertices, faces)
           ↓
       PolyData object (VTK representation)
```

### New USD Flow
```
Connectivity Results (same raw arrays)
  ├─ node_coords: [x0, y0, z0, x1, y1, z1, ...]
  ├─ face_list: [count, v0, v1, v2, ...]
  └─ edge_list: [count, v0, v1, ...]
           ↓
       MeshUSD._extract_face_geometry()
           ↓
       vertices: [[x0, y0, z0], [x1, y1, z1], ...]  (N, 3) array
       face_vertex_counts: [count, count, ...]
       face_vertex_indices: [v0, v1, v2, v0, v1, ...]  (unpacked)
           ↓
       FaceGeometry DTO
           ↓
       face_geometry_to_usd() → UsdGeomMesh prim
           ↓
       USD stage with mesh prims
```

## Element-by-Element Mapping

### Faces

| PyVista | USD | Notes |
|---------|-----|-------|
| `pv.PolyData(vertices, faces)` | `UsdGeomMesh` | Both represent surface mesh |
| `vertices: (N, 3)` | `points attr` | Direct correspondence |
| `faces: [4, v0, v1, v2, v3, 3, ...]` (VTK packed) | `faceVertexCounts: [4, 3, ...]` + `faceVertexIndices: [v0, v1, v2, v3, ...]` | VTK → USD unpacking (easy 1:1) |
| `colors: (N_faces, 3)` array attribute | `displayColor: [(r, g, b), ...]` primvar | Color per-face, must normalize 0-255 → 0.0-1.0 |
| Custom: colors per-face | Custom attributes: `primMeshId`, `primZoneId`, `primPartId` | USD allows user-defined attributes |

### Edges

| PyVista | USD | Notes |
|---------|-----|-------|
| `pv.PolyData(vertices, lines)` | `UsdGeomBasisCurves` | Both represent curves |
| `vertices: (N, 3)` | `points attr` | Direct |
| `lines: [2, v0, v1, 2, v1, v2, ...]` (cell array) | `curveVertexCounts: [2, 2, ...]` + (implicit indices) | Unpacking same pattern |
| Line width (style) | Basis type: `linear` | USD basis curves vs VTK cell data |
| `colors: (N_edges, 3)` | `displayColor` primvar | Same normalization |

### Splines

| PyVista | USD | Notes |
|---------|-----|-------|
| Control points: `pv.PolyData(cp_vertices, faces)` | `UsdGeomPoints` or `UsdGeomMesh` | Points as mesh (quads) or as point cloud |
| Surface: `pv.PolyData(surf_vertices, faces)` | `UsdGeomMesh` | Direct mesh representation |
| `color_matrix` indexed by ID | `displayColor` primvar | Indexed lookup → direct color per prim |

## VTK-to-USD List Format Conversion

The main translation difference is list packing format:

### VTK Packed List (PyVista input)
```
faces = [4, 0, 1, 2, 3,  3, 1, 2, 4,  ...]
        [count, indices..., count, indices..., ...]
```

### USD Unpacked Lists
```
faceVertexCounts = [4, 3, ...]
faceVertexIndices = [0, 1, 2, 3, 1, 2, 4, ...]
```

### Conversion (VTK → USD)
```python
def unpack_vtk_list(packed_list):
    counts = []
    indices = []
    i = 0
    while i < len(packed_list):
        count = int(packed_list[i])
        counts.append(count)
        indices.extend(packed_list[i + 1 : i + 1 + count])
        i += count + 1
    return counts, indices
```

This is exactly what `MeshUSD._extract_face_geometry()` does—a simple, deterministic unpacking.

## Metadata Preservation

| Data | PolyData Path | USD Path | Preservation |
|------|--------------|----------|--------------|
| Face coordinates | vertices array | points attr | ✅ Direct |
| Face topology | faces (packed) | faceVertexCounts + faceVertexIndices | ✅ Unpacking |
| Zone ID | DisplayMeshInfo.zone_id | Custom `primZoneId` attribute | ✅ Custom attr |
| Zone name | DisplayMeshInfo.zone_name | Custom `primZoneName` attribute | ✅ Custom attr |
| Mesh ID | DisplayMeshInfo.id | Custom `primMeshId` attribute | ✅ Custom attr |
| Color | colors array on prim | displayColor primvar | ✅ Normalized |
| has_mesh flag | DisplayMeshInfo.has_mesh | Custom `primHasMesh` attribute | ✅ Custom attr |
| display_mesh_type | DisplayMeshInfo.display_mesh_type | Custom `primDisplayMeshType` attribute | ✅ Custom attr |

## Round-Trip Fidelity

Starting from connectivity → PolyData → USD → (hypothetical reverse) should preserve all data:

```
Connectivity source
    ↓
    ├─ Mesh → PolyData ✅ (existing, proven)
    └─ MeshUSD → FaceGeometry/EdgeGeometry/SplineGeometry → USD ✅ (new)
         ↓
    [hypothetical]
    USD parse → back to Geometry DTOs → PolyData ✅ (feasible, not implemented)
```

The DTO layer makes reverse translation **trivial** if needed—just read prim attributes and arrays, no complex conversions required.

## Complexity Breakdown

| Task | Complexity | Why |
|------|-----------|-----|
| Faces (PolyData → USD) | ✅ **Easy** | VTK list unpacking is straightforward |
| Edges (PolyData → USD) | ✅ **Easy** | Same as faces, BasisCurves is simpler than Mesh |
| Splines (PolyData → USD) | ✅ **Easy** | Points-as-points or mesh; no topology needed |
| Colors | ✅ **Easy** | Scale RGB 0-255 → 0.0-1.0 |
| Metadata | ✅ **Easy** | USD custom attributes are generic |
| PolyData → USD serialization | ✅ **Easy** | `pxr.Usd` has high-level API |
| USD → PolyData (reverse) | 🟡 **Moderate** | Requires parsing USD prims; feasible but not done yet |
| USD-native interactive rendering | 🔴 **Hard** | Requires new viewport/rendering backend; out of scope |

## Conclusion

**Translation between PolyData and USD is fundamentally easy** because:
1. Both represent the same geometric primitives (points, faces, curves, colors)
2. The format differences are superficial (VTK-packed vs USD-unpacked lists)
3. Metadata maps directly to USD custom attributes
4. The geometry DTOs provide a clean intermediary for future backends
5. No complex mathematical transformations needed

The effort is **low integration cost** (~1-2 days for full USD support) vs. **high value** (interchange, long-term flexibility, potential USD-native rendering in future).
