# Copyright (C) 2026 ANSYS, Inc. and/or its affiliates.
# Copyright (C) 2026 Synopsys, Inc. and ANSYS, Inc. All rights reserved.
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

"""Internal translation-log HTML renderer.

Renders the translation-log document (``jsonSummaryDoc`` from the internal
``GetImportLog`` / ``GetExportLog`` FileIO RPCs) to a self-contained, collapsible
HTML tree report written next to the input/export file. Internal utility used
only by :mod:`fileio`; **not** part of the public PyPrime API.
"""

import html
import json
import os
from pathlib import Path
from typing import Iterator, List, Optional, Tuple, Union

__all__ = ["write_abaqus_import_html_log", "write_cdb_export_html_log"]

_CSS_FILE = os.path.join(os.path.dirname(__file__), "assets", "fe2ansys_translation_log.css")


def _load_css() -> str:
    with open(_CSS_FILE, encoding="utf-8") as fh:
        return fh.read()


_JS_FILE = os.path.join(os.path.dirname(__file__), "assets", "fe2ansys_translation_log.js")


def _load_js() -> str:
    with open(_JS_FILE, encoding="utf-8") as fh:
        return fh.read()


def write_abaqus_import_html_log(
    fileio, inp_file_name: str, *, crash_error: Optional[str] = None
) -> None:
    """Write the Abaqus import translation-log HTML report next to the input file.

    Parameters
    ----------
    fileio : FileIO
        FileIO object the import ran on; used to fetch the import log.
    inp_file_name : str
        Imported Abaqus .inp file path. The report is written next to it.
    crash_error : str, optional
        Set when the import RPC hard-crashed; a crash-only report is written
        and no log is fetched.

    Notes
    -----
    **Internal API**. Best-effort and never raises; failures are logged through
    ``fileio._model.python_logger`` so the import result is unaffected. Called
    by :mod:`fileio` when ``ImportAbaqusParams.write_html_log`` is set.
    """
    logger = getattr(getattr(fileio, "_model", None), "python_logger", None)
    try:
        if crash_error is not None:
            _render_abaqus_import_html_log(
                None,
                inp_file_name + ".html",
                inp_file_name=inp_file_name,
                crash_error=crash_error,
            )
            return
        log_doc = _fetch_log_doc(fileio, "PrimeMesh::FileIO/GetImportLog")
        if log_doc is None:
            return
        _render_abaqus_import_html_log(
            log_doc,
            inp_file_name + ".html",
            inp_file_name=inp_file_name,
        )
    except Exception as e:
        if logger is not None:
            logger.warning("Failed to render import translation log to HTML: %s", e)


def write_cdb_export_html_log(
    fileio, cdb_file_name: str, *, crash_error: Optional[str] = None
) -> None:
    """Write the MAPDL CDB export translation-log HTML report next to the .cdb.

    Parameters
    ----------
    fileio : FileIO
        FileIO object the export ran on; used to fetch the export (and any
        preceding import) log.
    cdb_file_name : str
        Exported .cdb file path. The report is written next to it and its bytes
        are read for export source snippets.
    crash_error : str, optional
        Set when the export RPC hard-crashed; a crash-only report is written
        and no log is fetched.

    Notes
    -----
    **Internal API**. Best-effort and never raises; failures are logged through
    ``fileio._model.python_logger`` so the export result is unaffected. When the
    model originated from an Abaqus INP, import-time warnings/errors and the
    import summary are surfaced alongside the export ones. Called by
    :mod:`fileio` when ``ExportMapdlCdbParams.write_html_log`` is not False.
    """
    logger = getattr(getattr(fileio, "_model", None), "python_logger", None)
    try:
        if crash_error is not None:
            _render_cdb_export_html_log(
                None,
                cdb_file_name + ".html",
                export_file_name=cdb_file_name,
                import_log_doc=None,
                crash_error=crash_error,
            )
            return
        export_doc = _fetch_log_doc(fileio, "PrimeMesh::FileIO/GetExportLog")
        if export_doc is None:
            return
        import_doc = _fetch_log_doc(fileio, "PrimeMesh::FileIO/GetImportLog")
        _render_cdb_export_html_log(
            export_doc,
            cdb_file_name + ".html",
            export_file_name=cdb_file_name,
            import_log_doc=import_doc,
        )
    except Exception as e:
        if logger is not None:
            logger.warning("Failed to render export translation log to HTML: %s", e)


def write_dyna_export_html_log(
    fileio, k_file_name: str, *, crash_error: Optional[str] = None
) -> None:
    """Write the LS-DYNA (K) export translation-log HTML report next to the .k file.

    Parameters
    ----------
    fileio : FileIO
        FileIO object the export ran on; used to fetch the export (and any
        preceding import) log.
    k_file_name : str
        Exported .k file path. The report is written next to it.
    crash_error : str, optional
        Set when the export RPC hard-crashed; a crash-only report is written
        and no log is fetched.

    Notes
    -----
    **Internal API**, not yet wired into :mod:`fileio` (the LS-DYNA export path
    has no ``writeHtmlLog`` parameter yet) and not exported from ``__all__``.
    The Dyna-specific render (:func:`_render_dyna_export_html_log`) is currently
    a placeholder that raises ``NotImplementedError``; the warnings/errors path
    is already format-agnostic and will work once the render body is filled in.
    Best-effort and never raises.
    """
    logger = getattr(getattr(fileio, "_model", None), "python_logger", None)
    try:
        if crash_error is not None:
            _render_dyna_export_html_log(
                None,
                k_file_name + ".html",
                export_file_name=k_file_name,
                import_log_doc=None,
                crash_error=crash_error,
            )
            return
        export_doc = _fetch_log_doc(fileio, "PrimeMesh::FileIO/GetExportLog")
        if export_doc is None:
            return
        import_doc = _fetch_log_doc(fileio, "PrimeMesh::FileIO/GetImportLog")
        _render_dyna_export_html_log(
            export_doc,
            k_file_name + ".html",
            export_file_name=k_file_name,
            import_log_doc=import_doc,
        )
    except Exception as e:
        if logger is not None:
            logger.warning("Failed to render export translation log to HTML: %s", e)


def _fetch_log_doc(fileio, rpc_name: str) -> Optional[dict]:
    """Fetch and parse a translation-log JSON doc via an internal FileIO RPC.

    Returns the parsed dict, or ``None`` when the server returned nothing or a
    non-object. Reaches into ``fileio``'s private comm/model/object id.
    """
    log_str = fileio._comm.serve(fileio._model, rpc_name, fileio._object_id)
    if not log_str or not log_str.strip():
        return None
    parsed = json.loads(log_str)
    return parsed if isinstance(parsed, dict) else None


def _render_abaqus_import_html_log(
    log_doc: Optional[dict],
    out_file_name: str,
    *,
    inp_file_name: Optional[str] = None,
    crash_error: Optional[str] = None,
) -> None:
    """Render an Abaqus import translation log to a self-contained HTML file.

    ``log_doc`` is the fetched import log (a top-level ``Crash`` key, if present,
    is shown as a banner), or ``None`` on a hard crash where ``crash_error``
    carries the RPC exception and no C++ log is available.
    """
    header = _file_link_field("Import Source:", inp_file_name)
    if log_doc is None:
        heading = (
            "Import did not complete \u2014 the PRIME server process likely "
            "crashed during this operation."
        )
        note = (
            "No C++ translation log is available: the server terminated "
            "before the log could be retrieved."
        )
        body = (
            _crash_banner(heading, crash_error or "")
            + f'<p class="empty-note">{html.escape(note)}</p>'
        )
        _render("Abaqus Import Translation Report", body, out_file_name, header)
        return
    crash = _crash_text(log_doc, crash_error)
    banner = _crash_banner("Import ended with a crash.", crash) if crash else ""
    body = (
        banner
        + _warnings_errors_section(
            log_doc, label="Warnings &amp; Errors", snippet_file_path=inp_file_name, is_export=False
        )
        + _abaqus_import_summary_section(log_doc, snippet_file_path=inp_file_name)
    )
    _render("Abaqus Import Translation Report", body, out_file_name, header)


def _render_cdb_export_html_log(
    log_doc: Optional[dict],
    out_file_name: str,
    *,
    export_file_name: Optional[str] = None,
    import_log_doc: Optional[dict] = None,
    crash_error: Optional[str] = None,
) -> None:
    """Render a MAPDL CDB export translation log to a self-contained HTML file.

    ``export_file_name`` is the exported .cdb (read for export source snippets).
    When ``import_log_doc`` is provided (model originated from an Abaqus INP),
    page order is: Import Warnings & Errors, Export Warnings & Errors, Import
    Summary, Export Summary. Import source snippets come from the import log
    doc's ``Map.Files[].Filepath`` (stored as a full path by the C++ importer).
    On a hard crash ``log_doc`` is ``None`` and ``crash_error`` carries the RPC
    exception.
    """
    if log_doc is None:
        heading = (
            "Export did not complete \u2014 the PRIME server process likely "
            "crashed during this operation."
        )
        note = (
            "No C++ translation log is available: the server terminated "
            "before the log could be retrieved."
        )
        header = _file_link_field("Exported CDB:", export_file_name)
        body = (
            _crash_banner(heading, crash_error or "")
            + f'<p class="empty-note">{html.escape(note)}</p>'
        )
        _render("MAPDL CDB Export Translation Report", body, out_file_name, header)
        return
    import_inp_path = _first_inp_filepath(import_log_doc)
    crash = _crash_text(log_doc, crash_error)
    banner = _crash_banner("Export ended with a crash.", crash) if crash else ""
    body = banner
    if import_log_doc:
        body += _warnings_errors_section(
            import_log_doc,
            label="Import Warnings &amp; Errors",
            snippet_file_path=import_inp_path,
            is_export=False,
        )
    body += _warnings_errors_section(
        log_doc,
        label="Export Warnings &amp; Errors",
        snippet_file_path=export_file_name,
        is_export=True,
    )
    if import_log_doc:
        body += _abaqus_import_summary_section(import_log_doc, snippet_file_path=import_inp_path)
    body += _cdb_export_summary_section(log_doc)
    header = _file_link_field("Import Source:", import_inp_path) + _file_link_field(
        "Exported CDB:", export_file_name
    )
    _render("MAPDL CDB Export Translation Report", body, out_file_name, header)


def _render_dyna_export_html_log(
    log_doc: Optional[dict],
    out_file_name: str,
    *,
    export_file_name: Optional[str] = None,
    import_log_doc: Optional[dict] = None,
    crash_error: Optional[str] = None,
) -> None:
    """Render an LS-DYNA (K) export translation log to HTML.

    Placeholder: the Dyna summary (``Counts.translated/skipped``, ``Ids.*.max``,
    ``Settings``) and LS-DYNA title/labels are not yet implemented. Raises
    ``NotImplementedError`` so a premature call surfaces via the write wrapper's
    logged exception instead of writing a wrong CDB-shaped report. The
    warnings/errors path is already format-agnostic.
    """
    raise NotImplementedError("LS-DYNA export HTML log is not yet implemented")


def _render(title: str, body: str, out_file_name: str, header_extras: str) -> None:
    page = _page(title, body, header_extras)
    with open(out_file_name, "w", encoding="utf-8") as fh:
        fh.write(page)


def _page(title: str, body: str, header_extras: str) -> str:
    return (
        "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n"
        "<meta charset=\"UTF-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
        + f"<title>{html.escape(title)}</title>\n<style>{_load_css()}</style>\n"
        + "</head>\n<body>\n<div class=\"container\">\n"
        + '<div class="header">\n'
        + f"<h1>{html.escape(title)}</h1>\n{header_extras}\n"
        # Filter bar (behavior in fe2ansys_translation_log.js, styles in the .css).
        + '<div class="search-bar"><input id="tl-search" type="search"'
        ' placeholder="Filter report… (press /)" autocomplete="off"'
        ' spellcheck="false"><span id="tl-clear" class="tl-clear"'
        ' title="clear (Esc)">×</span><span id="tl-count"></span></div>\n'
        + "</div>\n<div class=\"content\">\n"
        + body
        # Inline the filter JS so the report stays self-contained (opens offline).
        + "\n</div>\n</div>\n" + f"<script>{_load_js()}</script>\n" + "</body>\n</html>\n"
    )


def _warnings_errors_section(
    log_doc: dict, *, label: str, snippet_file_path: Optional[str] = None, is_export: bool = False
) -> str:
    """Build a Warnings & Errors section with Errors and Warnings tabs."""
    logs = _logs(log_doc)
    warnings: List[str] = logs.get("warnings", []) or []
    errors: List[str] = logs.get("errors", []) or []
    body = _severity_tree(
        "Errors",
        errors,
        log_doc,
        severity="errors",
        snippet_file_path=snippet_file_path,
        is_export=is_export,
        css="err",
    ) + _severity_tree(
        "Warnings",
        warnings,
        log_doc,
        severity="warnings",
        snippet_file_path=snippet_file_path,
        is_export=is_export,
        css="warn",
    )
    return f'<div class="section"><h2>{label}</h2>{body}</div>'


def _abaqus_import_summary_section(
    log_doc: dict, *, snippet_file_path: Optional[str] = None
) -> str:
    """Import summary mirroring AbaqusUtils::GetSummaryLoggerString.

    Two collapsible subsections: **Keywords** (Processed / Skipped / Unrecognized
    buckets, occurrence totals with distinct-keyword secondaries; skipped
    entries expand to their Map.Skipped occurrences) and **Imported Mesh**
    (Nodes, Elements Found → Processed [By Classification, By Abaqus Type] /
    Skipped [By Abaqus Type], Nsets, Elsets). All counts are occurrence units
    and every breakdown sums to its parent total.
    """
    s = log_doc.get("Summary", {}) if isinstance(log_doc, dict) else {}
    if not isinstance(s, dict):
        s = {}
    kw = s.get("Keywords", {}) if isinstance(s, dict) else {}
    if not isinstance(kw, dict):
        kw = {}
    kw_counts = kw.get("Counts", {}) if isinstance(kw, dict) else {}
    if not isinstance(kw_counts, dict):
        kw_counts = {}
    counts = s.get("Counts", {}) if isinstance(s, dict) else {}
    if not isinstance(counts, dict):
        counts = {}

    # --- Keywords subsection ---
    # Keyword counts are occurrence (keyword-block) units; len(<bucket>) is the
    # distinct-keyword count shown as each dropdown's secondary.
    kw_found = _int(kw_counts, "total_keywords_found")
    proc_kw = _count_items(kw.get("processed_keywords"))
    sk_kw = _count_items(kw.get("skipped_keywords"))
    unp_kw = _count_items(kw.get("unprocessed_keywords"))
    distinct_keywords = len(proc_kw) + len(sk_kw) + len(unp_kw)
    if kw_found or distinct_keywords:
        kw_root = _root_summary(
            "Keywords",
            kw_found,
            _plural(distinct_keywords, "distinct keyword", "distinct keywords"),
        )
    else:
        kw_root = "Keywords"
    kw_lists = (
        _count_dict_dropdown("Processed Keywords", kw.get("processed_keywords"))
        + _skipped_keywords_dropdown(
            kw.get("skipped_keywords"),
            _skipped_occurrences_by_keyword(log_doc),
            snippet_file_path,
            _map_files(log_doc),
        )
        + _count_dict_dropdown("Unrecognized Keywords", kw.get("unprocessed_keywords"))
    )
    keywords_sub = _tree(kw_root, kw_lists, classes="subsection", open_attr=True)

    # --- Imported Mesh subsection ---
    # Order: Nodes, Elements Found dropdown, then Nsets + Elsets.
    nodes_node = _count_stub("Nodes", _int(counts, "node"))
    # Nsets / Elsets: name-list dropdowns from Map.Keywords (no snippets/links).
    nsets_drop = _names_dropdown(
        "Nsets", _map_keyword_names(log_doc, "NSET"), _int(counts, "nsets"), empty_note="(no nsets)"
    )
    elsets_drop = _names_dropdown(
        "Elsets",
        _map_keyword_names(log_doc, "ELSET"),
        _int(counts, "elsets"),
        empty_note="(no elsets)",
    )
    mesh_stats_tail = nsets_drop + elsets_drop
    # found = processed + skipped; each processed element falls into exactly one
    # classification (incl. MASS/ROTARYI), so breakdowns sum to `element`.
    class_items: List[Tuple[str, int]] = []
    for k, label in (
        ("beam", "Beam"),
        ("shell", "Shell"),
        ("solid", "Solid"),
        ("connector", "Connector"),
    ):
        n = _int(counts, k)
        if n:
            class_items.append((label, n))
    pbt = counts.get("physical_by_type")
    if isinstance(pbt, dict):
        for k, label in (("MASS", "Mass"), ("ROTARYI", "Rotary Inertia")):
            n = _int(pbt, k)
            if n:
                class_items.append((label, n))
    class_items.sort(key=lambda it: (-it[1], it[0]))
    type_items = _count_items(counts.get("element_by_type"))
    skipped_type_items = _count_items(counts.get("skipped_element_by_type"))
    processed_total = _int(counts, "element")
    skipped_total = _int(counts, "skipped_element")
    found_total = _int(counts, "total_elements_found")

    # Aggregate breakdown children under roots with descriptive secondaries.
    processed_children: List[str] = []
    class_branch = _breakdown_branch(
        "By Classification", class_items, "classification", "classifications"
    )
    type_branch = _breakdown_branch(
        "By Abaqus Type", type_items, "distinct abaqus type", "distinct abaqus types"
    )
    if class_branch:
        processed_children.append(class_branch)
    if type_branch:
        processed_children.append(type_branch)
    processed_node = _tree(
        _root_summary("Elements Processed", processed_total),
        (
            "".join(processed_children)
            if processed_total and processed_children
            else (
                '<div class="empty-note">(no breakdown available)</div>'
                if processed_total
                else '<div class="empty-note">(no processed elements)</div>'
            )
        ),
        classes="branch",
    )
    sk_children: List[str] = []
    sk_type_branch = _breakdown_branch(
        "By Abaqus Type", skipped_type_items, "distinct abaqus type", "distinct abaqus types"
    )
    if sk_type_branch:
        sk_children.append(sk_type_branch)
    # Always render Elements Skipped (even at 0) — absence reads as "unknown".
    skipped_node = _tree(
        _root_summary("Elements Skipped", skipped_total, "by abaqus type"),
        (
            "".join(sk_children)
            if skipped_total and sk_children
            else (
                '<div class="empty-note">(no breakdown available)</div>'
                if skipped_total
                else '<div class="empty-note">(no skipped elements)</div>'
            )
        ),
        classes="branch",
    )
    found_children = [processed_node, skipped_node]
    mesh_lists = _tree(
        _root_summary("Elements Found", found_total, "processed + skipped"), "".join(found_children)
    )
    mesh_sub = _tree(
        "Imported Mesh",
        nodes_node + mesh_lists + mesh_stats_tail,
        classes="subsection",
        open_attr=True,
    )

    return f'<div class="section"><h2>Import Summary</h2>{keywords_sub}{mesh_sub}</div>'


def _cdb_export_summary_section(log_doc: dict) -> str:
    """CDB/MAPDL export summary from Summary.Counts.

    A single **Exported Mesh** subsection: Nodes, Elements (→ By ANSYS Type when
    ``element_by_type`` is present), NBLOCKs, EBLOCKs, and Components (CMBLOCKs →
    Node/Element Components). The type breakdown is grouped by actual ANSYS
    output element type from EBLOCK write data.
    """
    s = log_doc.get("Summary", {}) if isinstance(log_doc, dict) else {}
    if not isinstance(s, dict):
        s = {}
    counts = s.get("Counts", {}) if isinstance(s, dict) else {}
    if not isinstance(counts, dict):
        counts = {}

    nodes_node = _count_stub("Nodes", _int(counts, "node"))
    output_type_items = _labeled_count_items(counts.get("element_by_type"))
    if output_type_items:
        elements_node = _tree(
            _root_summary("Elements", _int(counts, "element")),
            _breakdown_branch(
                "By ANSYS Type",
                output_type_items,
                "distinct ansys element type",
                "distinct ansys element types",
            ),
        )
    else:
        elements_node = _count_stub("Elements", _int(counts, "element"))
    nblocks_node = _count_stub("NBLOCKs", _int(counts, "nblock_count"))
    eblocks_node = _count_stub("EBLOCKs", _int(counts, "eblock_count"))

    generated_node_components = _count_stub(
        "Generated Node Components",
        _int(counts, "generated_node_components"),
        classes="branch",
    )
    node_components = _tree(
        _root_summary("Node Components", _int(counts, "node_components")),
        generated_node_components,
        classes="branch",
    )
    element_components = _count_stub(
        "Element Components",
        _int(counts, "element_components"),
        classes="branch",
    )
    components_total = _int(counts, "node_components") + _int(counts, "element_components")
    components_node = _tree(
        _root_summary("Components (CMBLOCKs)", components_total),
        node_components + element_components,
    )

    mesh_body = nodes_node + elements_node + nblocks_node + eblocks_node + components_node
    mesh_sub = _tree("Exported Mesh", mesh_body, classes="subsection", open_attr=True)

    return f'<div class="section"><h2>Export Summary</h2>{mesh_sub}</div>'


def _severity_tree(
    label: str,
    all_msgs: List[str],
    log_doc: dict,
    *,
    severity: str,
    snippet_file_path: Optional[str],
    is_export: bool,
    css: str,
) -> str:
    """Build a Warnings/Errors tab with all messages and source locations."""
    glyph, msg_prefix = _severity_glyphs(severity)
    children = _leaf(
        _root_summary(f"All {label}", len(all_msgs)), all_msgs, classes="all", prefix=msg_prefix
    )
    branch = _by_source_branch(
        log_doc, severity=severity, snippet_file_path=snippet_file_path, is_export=is_export
    )
    if not branch:
        branch = '<div class="empty-note">(none located)</div>'
    return _tree(_root_summary(f"{glyph} {label}", len(all_msgs)), children + branch, classes=css)


def _by_source_branch(
    log_doc: dict, *, severity: str, snippet_file_path: Optional[str], is_export: bool
) -> str:
    """Build a source-location branch with one leaf per occurrence span."""
    files = _map_files(log_doc)
    offsets = log_doc.get("Map", {}).get("Offsets", {}) if is_export else {}
    if not isinstance(offsets, dict):
        offsets = {}
    leaves: List[str] = []
    for entity, keyword, sp in _iter_spans(log_doc):
        msgs = _span_msgs(sp, severity)
        if not msgs:
            continue
        size = sp.get("Size", 0) or 0
        if is_export:
            stream = sp.get("Stream")
            base = offsets.get(stream, 0) if isinstance(stream, str) else 0
            offset = (base or 0) + (sp.get("Offset", 0) or 0)
            fpath, flabel = snippet_file_path, (
                os.path.basename(snippet_file_path) if snippet_file_path else (stream or "?")
            )
        else:
            offset = sp.get("Offset", 0) or 0
            fpath, flabel = _resolve_inp_file(sp.get("FileIndex"), files, snippet_file_path)
        snippet = _read_snippet(fpath, offset, size)
        leaves.append(
            _located_leaf(entity, keyword, msgs, severity, fpath, flabel, offset, size, snippet)
        )
    if not leaves:
        return ""
    return _tree(
        _root_summary("By Source Location", len(leaves)), "".join(leaves), classes="branch"
    )


def _located_leaf(
    entity: str,
    keyword: str,
    msgs: List[str],
    severity: str,
    fpath: Optional[str],
    flabel: str,
    offset: int,
    size: int,
    snippet: Optional[Tuple[str, bool]],
) -> str:
    _, msg_prefix = _severity_glyphs(severity)
    children = _pre(msgs, prefix=msg_prefix)
    # Skip the source-location line when there's no real byte range (Size=0).
    if size and size > 0:
        if fpath:
            uri = _file_uri(fpath)
            loc = (
                f'<a href="{html.escape(uri)}" title="{html.escape(fpath)}">'
                f'{html.escape(flabel)}</a> @ {offset:,} ({size:,} B)'
            )
        else:
            loc = f"{html.escape(flabel)} @ {offset:,} ({size:,} B)"
        children = f'<div class="loc-meta">{loc}</div>' + children
    if snippet:
        text, truncated = snippet
        disp = html.escape(text)
        if truncated:
            disp += "\n\u2026 (truncated)"
        children += (
            f'<details class="tree snip"><summary>source ({size:,} B)</summary>'
            f'<div class="tree-children"><pre class="snippet">{disp}</pre></div></details>'
        )
    return _tree(_root_summary(f"{entity} \u203a {keyword}", len(msgs)), children, classes="loc")


def _span_msgs(span: dict, severity: str) -> List[str]:
    key = "Warnings" if severity == "warnings" else "Errors"
    return _as_str_list(span.get(key))


def _iter_spans(log_doc: dict) -> Iterator[Tuple[str, str, dict]]:
    """Yield each occurrence span from Map.Translated and Map.Skipped.

    Include both IDs and identifiers.
    """
    m = log_doc.get("Map") if isinstance(log_doc, dict) else None
    if not isinstance(m, dict):
        return
    for section in ("Translated", "Skipped"):
        sec = m.get(section)
        if not isinstance(sec, dict):
            continue
        for bucket_name, prefix in (("Identifiers", None), ("Ids", "Id ")):
            b = sec.get(bucket_name)
            if not isinstance(b, dict):
                continue
            for entity, occs in b.items():
                label = (prefix + str(entity)) if prefix else str(entity)
                if not isinstance(occs, list):
                    continue
                for occ in occs:
                    if not isinstance(occ, dict):
                        continue
                    for keyword, spans in occ.items():
                        if not isinstance(spans, list):
                            continue
                        for sp in spans:
                            if isinstance(sp, dict):
                                yield label, str(keyword), sp


def _map_files(log_doc: dict) -> List[dict]:
    m = log_doc.get("Map") if isinstance(log_doc, dict) else None
    if not isinstance(m, dict):
        return []
    files = m.get("Files")
    return files if isinstance(files, list) else []


def _resolve_inp_file(
    file_index, files: List[dict], inp_file_path: Optional[str]
) -> Tuple[Optional[str], str]:
    """Resolve a readable path for an import span's FileIndex.

    Map.Files[].Filepath is the full path stored by the importer; a relative
    path is resolved against the imported .inp file's directory. Returns
    (readable_path_or_None, label).
    """
    fp = ""
    if (
        isinstance(file_index, int)
        and 0 <= file_index < len(files)
        and isinstance(files[file_index], dict)
    ):
        fp = files[file_index].get("Filepath", "") or ""
    label = os.path.basename(fp) if fp else "?"
    if not fp:
        return None, label
    if os.path.isabs(fp):
        return fp, label
    if inp_file_path:
        base = os.path.dirname(inp_file_path)
        return (os.path.join(base, fp) if base else fp), label
    return fp, label  # best-effort (relative to CWD)


def _read_snippet(
    path: Optional[str], offset: int, size: int, cap: int = 800
) -> Optional[Tuple[str, bool]]:
    """Read up to `cap` bytes and return the text and truncation state.

    Return None when there is no real range.
    """
    if not path or not size or size <= 0 or offset is None or offset < 0:
        return None
    try:
        with open(path, "rb") as fh:
            fh.seek(offset)
            data = fh.read(min(size, cap))
    except (OSError, ValueError):
        return None
    if not data:
        return None
    text = data.decode("utf-8", errors="replace")
    return text, size > cap


def _skipped_keywords_dropdown(
    skipped_counts, occ_by_kw: dict, snippet_file_path: Optional[str], files: List[dict]
) -> str:
    """Render a Skipped Keywords dropdown with occurrence leaves and snippets."""
    items = _count_items(skipped_counts)
    if not items:
        # Always render the Skipped Keywords dropdown (even at 0) — absence reads as "unknown".
        return _tree(
            _root_summary(
                "Skipped Keywords", 0, _plural(0, "distinct keyword", "distinct keywords")
            ),
            '<div class="empty-note">(no skipped keywords)</div>',
        )
    total = sum(n for _, n in items)
    nodes = []
    for keyword, count in items:
        occs = occ_by_kw.get(keyword, [])
        if occs:
            body = "".join(
                _skipped_keyword_occ_leaf(ent, keyword, sp, files, snippet_file_path)
                for ent, sp in occs
            )
        else:
            body = '<div class="empty-note">(no located occurrences)</div>'
        nodes.append(_tree(_root_summary(keyword, count), body))
    return _tree(
        _root_summary(
            "Skipped Keywords", total, _plural(len(items), "distinct keyword", "distinct keywords")
        ),
        "".join(nodes),
    )


def _skipped_keyword_occ_leaf(
    entity: str, keyword: str, span: dict, files: List[dict], snippet_file_path: Optional[str]
) -> str:
    """One Map.Skipped occurrence as a located leaf with a source snippet."""
    msgs = _as_str_list(span.get("Warnings")) or ["Skipped keyword block (no message recorded)"]
    offset = span.get("Offset", 0) or 0
    size = span.get("Size", 0) or 0
    fpath, flabel = _resolve_inp_file(span.get("FileIndex"), files, snippet_file_path)
    snippet = _read_snippet(fpath, offset, size)
    return _located_leaf(entity, keyword, msgs, "warnings", fpath, flabel, offset, size, snippet)


def _skipped_occurrences_by_keyword(log_doc: dict) -> dict:
    """Map.Skipped walked as {keyword: [(entity_label, span), ...]}."""
    m = log_doc.get("Map") if isinstance(log_doc, dict) else None
    if not isinstance(m, dict):
        return {}
    skipped = m.get("Skipped")
    if not isinstance(skipped, dict):
        return {}
    result: dict = {}
    for bucket_name, prefix in (("Identifiers", None), ("Ids", "Id ")):
        b = skipped.get(bucket_name)
        if not isinstance(b, dict):
            continue
        for entity, occs in b.items():
            label = (prefix + str(entity)) if prefix else str(entity)
            if not isinstance(occs, list):
                continue
            for occ in occs:
                if not isinstance(occ, dict):
                    continue
                for keyword, spans in occ.items():
                    if not isinstance(spans, list):
                        continue
                    for sp in spans:
                        if isinstance(sp, dict):
                            result.setdefault(str(keyword), []).append((label, sp))
    return result


def _names_dropdown(title: str, names: List[str], total: int, *, empty_note: str) -> str:
    """Render a collapsible list of names.

    The root badge is ``total`` and the secondary label is the distinct-name count.
    """
    if names:
        body = _pre([html.escape(n) for n in names])
    else:
        body = f'<div class="empty-note">{html.escape(empty_note)}</div>'
    summary = _root_summary(title, total, _plural(len(names), "distinct name", "distinct names"))
    return _tree(summary, body)


def _map_keyword_names(log_doc: dict, keyword: str) -> List[str]:
    """Return sorted identifier names under Map.Keywords[``keyword``].

    The result may be empty.
    """
    m = log_doc.get("Map") if isinstance(log_doc, dict) else None
    if not isinstance(m, dict):
        return []
    kw = m.get("Keywords")
    if not isinstance(kw, dict):
        return []
    bucket = kw.get(keyword)
    if not isinstance(bucket, dict):
        return []
    return sorted(str(k) for k in bucket.keys())


def _count_dict_dropdown(
    title: str,
    mapping,
    *,
    css: str = "",
    singular: str = "distinct keyword",
    plural: str = "distinct keywords",
) -> str:
    """Collapsible 'count: key' lines for a {key: count} dict; root badge is the total."""
    items = _count_items(mapping)
    if not items:
        return ""  # omit empty dropdowns (no node, no triangle)
    total = sum(n for _, n in items)
    summary = _root_summary(title, total, _plural(len(items), singular, plural))
    return _tree(summary, _count_lines(items), classes=css)


def _breakdown_branch(
    title: str, items: List[Tuple[str, int]], singular: str, plural: str = ""
) -> str:
    """Build a nested ``tree.branch`` and omit it when empty.

    The root shows the total of its leaves and a muted secondary label.
    """
    if not items:
        return ""
    total = sum(n for _, n in items)
    summary = _root_summary(title, total, _plural(len(items), singular, plural))
    return _tree(summary, _count_lines(items), classes="branch")


def _count_lines(items: List[Tuple[str, int]]) -> str:
    rows = []
    for label, n in items:
        marker = label if label.endswith(":") else label + ":"
        rows.append(
            f'<div class="count-row"><span class="count-marker">{html.escape(marker)}</span>'
            f'<span class="count-number">{n:,}</span></div>'
        )
    return f'<div class="count-table">{"".join(rows)}</div>'


def _count_items(mapping) -> List[Tuple[str, int]]:
    """Sorted (key, count) pairs from a {key: count} dict, by count desc then key."""
    if not isinstance(mapping, dict):
        return []
    items: List[Tuple[str, int]] = []
    for k, v in mapping.items():
        try:
            n = int(v)
        except (TypeError, ValueError):
            continue
        items.append((str(k), n))
    items.sort(key=lambda it: (-it[1], it[0]))
    return items


def _labeled_count_items(
    mapping, *, count_key: str = "Count", label_key: str = "Label"
) -> List[Tuple[str, int]]:
    """Return sorted label and count pairs from supported mappings.

    Supported mappings are ``{label: count}`` and ``{code: {Label, Count}}``.
    """
    if not isinstance(mapping, dict):
        return []
    items: List[Tuple[str, int]] = []
    for k, v in mapping.items():
        if isinstance(v, dict):
            label = v.get(label_key)
            if isinstance(label, str) and str(label).strip():
                label_text = str(label).strip()
            else:
                label_text = str(k)
            if count_key not in v:
                continue
            n = _int(v, count_key)
            items.append((label_text, n))
            continue
        try:
            n = int(v)
        except (TypeError, ValueError):
            continue
        items.append((str(k), n))
    items.sort(key=lambda it: (-it[1], it[0]))
    return items


def _stat_rows(rows: List[Tuple[str, Union[int, str]]]) -> str:
    def _fmt(v: Union[int, str]) -> str:
        return v if isinstance(v, str) else f"{int(v):,}"

    parts = [
        f'<div class="stat"><span class="stat-label">{html.escape(label)}</span>'
        f'<span class="stat-val">{_fmt(value)}</span></div>'
        for label, value in rows
    ]
    return f'<div class="stat-grid">{"".join(parts)}</div>'


def _root_summary(title: str, total: int, branch_text: str = "") -> str:
    """Build a dropdown summary line ending in the total badge.

    Optionally precede the badge with a muted ``branch_text`` secondary.
    """
    tail = []
    if branch_text:
        tail.append(f'<span class="sub-count">{html.escape(branch_text)}</span>')
    tail.append(_badge(total))
    return (
        f'<span class="summary-title">{html.escape(title)}</span>'
        f'<span class="summary-tail">{"".join(tail)}</span>'
    )


def _tree_stub(summary: str, *, classes: str = "") -> str:
    cls = f"tree stub {classes}".strip()
    return f'<details class="{cls}"><summary>{summary}</summary></details>'


def _count_stub(title: str, total: int, *, classes: str = "") -> str:
    return _tree_stub(_root_summary(title, total), classes=classes)


def _plural(n: int, singular: str, plural: str = "") -> str:
    """``'1 type'`` / ``'12 types'`` — picks the singular form for n == 1."""
    return f"{n} {singular if n == 1 else (plural or singular + 's')}"


def _int(d: dict, key: str, default: int = 0) -> int:
    if not isinstance(d, dict):
        return default
    v = d.get(key)
    try:
        return int(v) if v is not None else default
    except (TypeError, ValueError):
        return default


def _tree(summary: str, body: str, *, classes: str = "", open_attr: bool = False) -> str:
    o = " open" if open_attr else ""
    cls = f"tree {classes}".strip()
    return (
        f'<details class="{cls}"{o}><summary>{summary}</summary>'
        f'<div class="tree-children">{body}</div></details>'
    )


def _leaf(summary: str, msgs: List[str], *, classes: str = "", prefix: str = "") -> str:
    return _tree(summary, _pre(msgs, prefix=prefix), classes=classes)


def _badge(n: int) -> str:
    cls = "log-count zero" if n == 0 else "log-count"
    return f'<span class="{cls}">{n:,}</span>'


def _pre(msgs: List[str], *, prefix: str = "") -> str:
    if not msgs:
        return '<pre class="log-area empty">(no messages)</pre>'
    body = "\n".join(prefix + html.escape(m) for m in msgs)
    return f'<pre class="log-area">{body}</pre>'


def _severity_glyphs(severity: str) -> Tuple[str, str]:
    """(root-tab glyph, per-message prefix) for a severity."""
    if severity == "warnings":
        return "\u26a0", "\u26a0 "
    return "\u2717", "\u2717 "


def _crash_banner(heading: str, detail: str = "") -> str:
    """Build a prominent red banner for crash reports."""
    detail_html = f'<pre>{html.escape(detail)}</pre>' if detail else ""
    return (
        '<div class="crash-banner"><span class="crash-glyph">\u2717</span>'
        f'<div class="crash-body"><div class="crash-heading">{html.escape(heading)}</div>'
        f'{detail_html}</div></div>'
    )


def _crash_text(log_doc: Optional[dict], crash_error: Optional[str]) -> str:
    """Return the crash message from the document or RPC exception."""
    if isinstance(log_doc, dict):
        c = log_doc.get("Crash")
        if isinstance(c, str) and c.strip():
            return c.strip()
    if crash_error:
        return str(crash_error).strip()
    return ""


def _file_link_field(label: str, path: Optional[str]) -> str:
    """Build a labeled field with containing-folder and file links.

    The file link uses the basename as its label and the full path as its href and tooltip.
    """
    if not path:
        return ""
    name = Path(path).name or path
    uri = _file_uri(path)
    folder = _folder_link(path)
    sep = " " if folder else ""
    return (
        f'<div class="file-link"><span class="field-label">{html.escape(label)}</span> '
        f'{folder}{sep}<a href="{html.escape(uri)}" title="{html.escape(path)}">'
        f'{html.escape(name)}</a></div>'
    )


def _folder_link(path: Optional[str]) -> str:
    """Build a hyperlink to the containing folder."""
    if not path:
        return ""
    parent = os.path.dirname(path)
    if not parent:
        return ""
    name = os.path.basename(parent) or parent
    uri = _file_uri(parent)
    if not uri.endswith("/"):
        uri += "/"
    return (
        f'<a class="folder-link" href="{html.escape(uri)}" title="{html.escape(parent)}">'
        f'\U0001f4c1 {html.escape(name)}</a>'
    )


def _file_uri(path: str) -> str:
    try:
        return Path(path).as_uri()
    except (ValueError, OSError):
        return path


def _first_inp_filepath(log_doc) -> Optional[str]:
    """First Map.Files[].Filepath from a log doc, if any."""
    if not isinstance(log_doc, dict):
        return None
    m = log_doc.get("Map")
    if not isinstance(m, dict):
        return None
    files = m.get("Files")
    if not isinstance(files, list) or not files:
        return None
    f0 = files[0]
    if isinstance(f0, dict):
        p = f0.get("Filepath")
        if isinstance(p, str) and p:
            return p
    return None


def _as_str_list(v) -> List[str]:
    if isinstance(v, list):
        return [str(x) for x in v]
    if isinstance(v, str) and v:
        return [v]
    return []


def _logs(log_doc: dict) -> dict:
    logs = log_doc.get("Logs", {}) if isinstance(log_doc, dict) else {}
    return logs if isinstance(logs, dict) else {}
