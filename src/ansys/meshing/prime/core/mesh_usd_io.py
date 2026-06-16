# Copyright (C) 2024 - 2026 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""USD I/O utilities for mesh geometry serialization."""

from pathlib import Path
from typing import Dict, Optional

import numpy as np


def normalize_color(color_rgb_0_255):
    """Convert 0-255 RGB to 0.0-1.0 USD displayColor format.

    Parameters
    ----------
    color_rgb_0_255 : list
        RGB color in [0, 255] range.

    Returns
    -------
    tuple
        Normalized RGB color in (0.0, 1.0) range.
    """
    return tuple(c / 255.0 for c in color_rgb_0_255)


def face_geometry_to_usd(face_geom, stage, part_path: str, face_index: int):
    """Convert FaceGeometry DTO to USD mesh prim.

    Parameters
    ----------
    face_geom : FaceGeometry
        Face geometry DTO.
    stage : pxr.Usd.Stage
        USD stage to write to.
    part_path : str
        Base path for part prims (e.g., "/parts/1").
    face_index : int
        Index of this face geometry within the part.

    Returns
    -------
    pxr.UsdGeomMesh or None
        The created mesh prim, or None if no points.
    """
    try:
        from pxr import Sdf, UsdGeom
    except ImportError:
        raise ImportError(
            "OpenUSD is required for USD export. Install it with: pip install usd-core"
        )

    if len(face_geom.points) == 0:
        return None

    prim_path = f"{part_path}/faces/face_{face_index}"
    mesh_prim = UsdGeom.Mesh.Define(stage, prim_path)

    # Set points
    mesh_prim.GetPointsAttr().Set(face_geom.points)

    # Set face topology (faceVertexCounts and faceVertexIndices)
    mesh_prim.GetFaceVertexCountsAttr().Set(face_geom.face_vertex_counts)
    mesh_prim.GetFaceVertexIndicesAttr().Set(face_geom.face_vertex_indices)

    # Add display color primvar
    norm_color = normalize_color(face_geom.color)
    color_attr = mesh_prim.CreateDisplayColorAttr()
    color_attr.Set([norm_color])

    # Add custom attributes for metadata
    prim = mesh_prim.GetPrim()
    prim.CreateAttribute("primMeshId", Sdf.ValueTypeNames.Int).Set(int(face_geom.mesh_id))
    prim.CreateAttribute("primZoneId", Sdf.ValueTypeNames.Int).Set(int(face_geom.zone_id))
    if face_geom.zone_name:
        prim.CreateAttribute("primZoneName", Sdf.ValueTypeNames.String).Set(
            str(face_geom.zone_name)
        )
    prim.CreateAttribute("primPartId", Sdf.ValueTypeNames.Int).Set(int(face_geom.part_id))
    prim.CreateAttribute("primHasMesh", Sdf.ValueTypeNames.Bool).Set(bool(face_geom.has_mesh))
    prim.CreateAttribute("primDisplayMeshType", Sdf.ValueTypeNames.Int).Set(
        int(face_geom.display_mesh_type)
    )

    return mesh_prim


def edge_geometry_to_usd(edge_geom, stage, part_path: str, edge_index: int):
    """Convert EdgeGeometry DTO to USD basis curves prim.

    Parameters
    ----------
    edge_geom : EdgeGeometry
        Edge geometry DTO.
    stage : pxr.Usd.Stage
        USD stage to write to.
    part_path : str
        Base path for part prims (e.g., "/parts/1").
    edge_index : int
        Index of this edge geometry within the part.

    Returns
    -------
    pxr.UsdGeomBasisCurves or None
        The created curves prim, or None if no points.
    """
    try:
        from pxr import Sdf, UsdGeom
    except ImportError:
        raise ImportError(
            "OpenUSD is required for USD export. Install it with: pip install usd-core"
        )

    if len(edge_geom.points) == 0:
        return None

    prim_path = f"{part_path}/edges/edge_{edge_index}"
    curves_prim = UsdGeom.BasisCurves.Define(stage, prim_path)

    # Set points
    curves_prim.GetPointsAttr().Set(edge_geom.points)

    # Set curve topology (curveVertexCounts)
    curves_prim.GetCurveVertexCountsAttr().Set(edge_geom.edge_vertex_counts)

    # Set curve basis and wrap
    curves_prim.GetBasisAttr().Set(UsdGeom.Tokens.linear)
    curves_prim.GetTypeAttr().Set(UsdGeom.Tokens.linear)

    # Add display color primvar
    norm_color = normalize_color(edge_geom.color)
    color_attr = curves_prim.CreateDisplayColorAttr()
    color_attr.Set([norm_color])

    # Add custom attributes for metadata
    prim = curves_prim.GetPrim()
    prim.CreateAttribute("primMeshId", Sdf.ValueTypeNames.Int).Set(int(edge_geom.mesh_id))
    prim.CreateAttribute("primPartId", Sdf.ValueTypeNames.Int).Set(int(edge_geom.part_id))
    prim.CreateAttribute("primDisplayMeshType", Sdf.ValueTypeNames.Int).Set(
        int(edge_geom.display_mesh_type)
    )

    return curves_prim


def spline_geometry_to_usd(spline_geom, stage, part_path: str, spline_index: int):
    """Convert SplineGeometry DTO to USD points or mesh prim.

    Parameters
    ----------
    spline_geom : SplineGeometry
        Spline geometry DTO.
    stage : pxr.Usd.Stage
        USD stage to write to.
    part_path : str
        Base path for part prims (e.g., "/parts/1").
    spline_index : int
        Index of this spline within the part.

    Returns
    -------
    pxr.UsdGeomPoints or pxr.UsdGeomMesh or None
        The created prim, or None if no points.
    """
    try:
        from pxr import Sdf, UsdGeom
    except ImportError:
        raise ImportError(
            "OpenUSD is required for USD export. Install it with: pip install usd-core"
        )

    if len(spline_geom.points) == 0:
        return None

    from ansys.meshing.prime.core.mesh import DisplayMeshType

    if spline_geom.geom_type == DisplayMeshType.SPLINECONTROLPOINTS:
        prim_path = f"{part_path}/splines/ctrlpts_{spline_index}"
        points_prim = UsdGeom.Points.Define(stage, prim_path)
        points_prim.GetPointsAttr().Set(spline_geom.points)

        norm_color = normalize_color(spline_geom.color)
        color_attr = points_prim.CreateDisplayColorAttr()
        color_attr.Set([norm_color])

        prim = points_prim.GetPrim()
        prim.CreateAttribute("primSplineId", Sdf.ValueTypeNames.Int).Set(int(spline_geom.spline_id))
        prim.CreateAttribute("primPartId", Sdf.ValueTypeNames.Int).Set(int(spline_geom.part_id))

        return points_prim
    else:  # SPLINESURFACE
        prim_path = f"{part_path}/splines/surf_{spline_index}"
        mesh_prim = UsdGeom.Mesh.Define(stage, prim_path)
        mesh_prim.GetPointsAttr().Set(spline_geom.points)

        # For spline surface, create a simple grid topology (assumes quad layout from points)
        # This is a placeholder; actual implementation depends on spline data structure
        norm_color = normalize_color(spline_geom.color)
        color_attr = mesh_prim.CreateDisplayColorAttr()
        color_attr.Set([norm_color])

        prim = mesh_prim.GetPrim()
        prim.CreateAttribute("primSplineId", Sdf.ValueTypeNames.Int).Set(int(spline_geom.spline_id))
        prim.CreateAttribute("primPartId", Sdf.ValueTypeNames.Int).Set(int(spline_geom.part_id))

        return mesh_prim


def build_stage_from_usd_geom(
    usd_geom_dict: Dict[int, Dict[str, list]], stage=None
) -> Optional[object]:
    """Build a USD stage from geometry DTOs.

    Parameters
    ----------
    usd_geom_dict : dict
        Dictionary mapping part_id -> {"faces": [...], "edges": [...],
        "ctrlpts": [...], "splinesurf": [...]} as returned by MeshUSD.as_usd().
    stage : pxr.Usd.Stage, optional
        Existing stage to add prims to. If None, a new in-memory stage is created.

    Returns
    -------
    pxr.Usd.Stage
        The populated USD stage.
    """
    try:
        from pxr import Usd, UsdGeom
    except ImportError:
        raise ImportError(
            "OpenUSD is required for USD export. Install it with: pip install usd-core"
        )

    if stage is None:
        stage = Usd.Stage.CreateInMemory()

    # Build an explicit hierarchy so mesh prims are always authored before edge prims.
    parts_root = UsdGeom.Xform.Define(stage, "/parts")
    stage.SetDefaultPrim(parts_root.GetPrim())

    for part_id, geoms in usd_geom_dict.items():
        part_path = f"/parts/part_{part_id}"
        UsdGeom.Xform.Define(stage, part_path)
        UsdGeom.Xform.Define(stage, f"{part_path}/faces")
        UsdGeom.Xform.Define(stage, f"{part_path}/edges")
        UsdGeom.Xform.Define(stage, f"{part_path}/splines")

        # Add faces
        for i, face_geom in enumerate(geoms.get("faces", [])):
            face_geometry_to_usd(face_geom, stage, part_path, i)

        # Add edges
        for i, edge_geom in enumerate(geoms.get("edges", [])):
            edge_geometry_to_usd(edge_geom, stage, part_path, i)

        # Add control points
        for i, spline_geom in enumerate(geoms.get("ctrlpts", [])):
            spline_geometry_to_usd(spline_geom, stage, part_path, i)

        # Add spline surfaces
        for i, spline_geom in enumerate(geoms.get("splinesurf", [])):
            spline_geometry_to_usd(spline_geom, stage, part_path, i)

    return stage


def export_to_usd(usd_geom_dict: Dict[int, Dict[str, list]], filepath: str) -> None:
    """Export geometry DTOs to a USD file.

    Parameters
    ----------
    usd_geom_dict : dict
        Dictionary mapping part_id -> {"faces": [...], "edges": [...], ...}
        as returned by MeshUSD.as_usd().
    filepath : str
        Path to write the USD file (.usd or .usda).
    """
    stage = build_stage_from_usd_geom(usd_geom_dict)
    stage.Export(filepath)


def export_usd_viewer_html(
    usd_geom_dict: Dict[int, Dict[str, list]],
    usd_path: "str | Path",
    html_path: "str | Path",
    line_color: str = "#ffffff",
    line_opacity: float = 0.9,
) -> Path:
    """Export a USD file and a web viewer HTML with mesh lines already enabled.

    Combines :func:`export_to_usd`, ``ansys.tools.usdviewer.web.html_export.export_viewer_html``,
    and :func:`enable_mesh_lines_in_viewer_html` into a single call so that mesh
    line overlays are injected automatically.

    Parameters
    ----------
    usd_geom_dict : dict
        Dictionary mapping part_id -> {"faces": [...], "edges": [...], ...}
        as returned by ``model.as_usd()``.
    usd_path : str | Path
        Destination path for the USD file (.usd or .usda).
    html_path : str | Path
        Destination path for the viewer HTML file.
    line_color : str, default: "#ffffff"
        CSS hex colour for the mesh edge overlay.
    line_opacity : float, default: 0.9
        Opacity of the mesh edge overlay (0.0 – 1.0).

    Returns
    -------
    pathlib.Path
        Resolved path to the written HTML file.
    """
    from ansys.tools.usdviewer.web.html_export import export_viewer_html as _export_html

    usd_path = Path(usd_path).expanduser().resolve()
    export_to_usd(usd_geom_dict, str(usd_path))
    result_html = _export_html(usd_path, html_path)
    return enable_mesh_lines_in_viewer_html(
        result_html,
        line_color=line_color,
        line_opacity=line_opacity,
        usd_geom_dict=usd_geom_dict,
    )


def enable_mesh_lines_in_viewer_html(
    html_path: str | Path,
    line_color: str = "#ffffff",
    line_opacity: float = 0.9,
    usd_geom_dict: Optional[Dict[int, Dict[str, list]]] = None,
) -> Path:
    """Enable mesh line overlays in a USD web viewer HTML export.

    Post-processes the HTML generated by
    ``ansys.tools.usdviewer.web.html_export.export_viewer_html`` and injects
    mesh element edges derived from the original polygon topology stored in
    ``usd_geom_dict``.  Each polygon edge is drawn exactly once, matching
    the element-edge display of PyVista / PrimePlotter with no tessellation
    diagonals and no angle-based filtering.

    Parameters
    ----------
    html_path : str | Path
        Path to the generated viewer HTML file.
    line_color : str, default: "#ffffff"
        Hex color for the mesh lines.
    line_opacity : float, default: 0.9
        Opacity for the mesh lines in the range [0.0, 1.0].
    usd_geom_dict : Dict[int, Dict[str, list]], optional
        USD geometry dictionary returned by ``model.as_usd()``.  When
        provided, element edges are derived from face polygon connectivity.
        When ``None``, a simple Three.js ``EdgesGeometry`` fallback is used.

    Returns
    -------
    Path
        Absolute path to the updated HTML file.
    """
    viewer_path = Path(html_path).expanduser().resolve()
    if not viewer_path.exists():
        raise FileNotFoundError(f"Viewer HTML file not found: {viewer_path}")

    if not (0.0 <= line_opacity <= 1.0):
        raise ValueError("line_opacity must be between 0.0 and 1.0.")

    html_text = viewer_path.read_text(encoding="utf-8")

    if "pyprimeEdgesInjected" in html_text:
        return viewer_path

    config_anchor = "const binary = atob(glbBase64);"
    if config_anchor not in html_text:
        raise RuntimeError("Unsupported viewer HTML format: config anchor not found.")

    scene_anchor = "scene.add(gltf.scene);"
    if scene_anchor not in html_text:
        raise RuntimeError("Unsupported viewer HTML format: scene anchor not found.")

    if usd_geom_dict is not None:
        # ------------------------------------------------------------------
        # Derive element edges from face polygon topology.
        # face_vertex_counts preserves original polygon sizes (3 = tri, 4 = quad …).
        # This produces exactly the same edges PyVista draws: one line per
        # polygon boundary edge, no tessellation diagonals.
        # ------------------------------------------------------------------
        segments: list[float] = []
        for geoms in usd_geom_dict.values():
            for face_geom in geoms.get("faces", []):
                pts = np.asarray(face_geom.points, dtype=np.float32)
                if len(pts) == 0:
                    continue
                counts = np.asarray(face_geom.face_vertex_counts, dtype=np.int32)
                indices = np.asarray(face_geom.face_vertex_indices, dtype=np.int32)

                seen: set[tuple[int, int]] = set()
                cursor = 0
                for n in counts:
                    face_verts = indices[cursor : cursor + n]
                    for i in range(n):
                        a = int(face_verts[i])
                        b = int(face_verts[(i + 1) % n])
                        key = (a, b) if a < b else (b, a)
                        if key not in seen:
                            seen.add(key)
                            segments.extend(map(float, pts[a]))
                            segments.extend(map(float, pts[b]))
                    cursor += n

        # Embed segment positions as a compact JSON array of flat floats.
        import json as _json

        segs_json = _json.dumps([round(v, 6) for v in segments], separators=(",", ":"))

        config_block = (
            f"      const pyprimeSegs = new Float32Array({segs_json});\n"
            f'      const pyprimeMeshLineColor = new THREE.Color("{line_color}");\n'
            f"      const pyprimeMeshLineOpacity = {line_opacity};\n"
            "      // pyprimeEdgesInjected\n\n"
            "      "
        )
        html_text = html_text.replace(config_anchor, config_block + config_anchor, 1)

        edge_js = """scene.add(gltf.scene);
        if (pyprimeSegs.length >= 6) {
          const geo = new THREE.BufferGeometry();
          geo.setAttribute("position", new THREE.BufferAttribute(pyprimeSegs, 3));
          const mat = new THREE.LineBasicMaterial({
            color: pyprimeMeshLineColor,
            transparent: pyprimeMeshLineOpacity < 1.0,
            opacity: pyprimeMeshLineOpacity,
          });
          const lines = new THREE.LineSegments(geo, mat);
          lines.name = "PyPrimeMeshEdges";
          lines.frustumCulled = false;
          lines.renderOrder = 1;
          scene.add(lines);
        }"""
    else:
        # Fallback: use Three.js EdgesGeometry (works for any GLB).
        config_block = (
            f'      const pyprimeMeshLineColor = new THREE.Color("{line_color}");\n'
            f"      const pyprimeMeshLineOpacity = {line_opacity};\n"
            "      // pyprimeEdgesInjected\n\n"
            "      "
        )
        html_text = html_text.replace(config_anchor, config_block + config_anchor, 1)

        edge_js = """scene.add(gltf.scene);
        gltf.scene.traverse((obj) => {
          if (!obj.isMesh || !obj.geometry || obj.userData.pyprimeEdgesAdded) return;
          const edgeGeo = new THREE.EdgesGeometry(obj.geometry, 15);
          const edgeMat = new THREE.LineBasicMaterial({
            color: pyprimeMeshLineColor,
            transparent: pyprimeMeshLineOpacity < 1.0,
            opacity: pyprimeMeshLineOpacity,
          });
          const lines = new THREE.LineSegments(edgeGeo, edgeMat);
          lines.frustumCulled = false;
          lines.renderOrder = 1;
          lines.userData.pyprimeEdgesAdded = true;
          obj.add(lines);
        });"""

    html_text = html_text.replace(scene_anchor, edge_js, 1)
    viewer_path.write_text(html_text, encoding="utf-8")
    return viewer_path
