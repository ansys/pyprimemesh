# Copyright (C) 2024 - 2026 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
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

"""Tests for pathlib.Path support on file I/O helpers."""
from pathlib import Path

import ansys.meshing.prime.internals.config as config
import ansys.meshing.prime.internals.defaults as defaults
import ansys.meshing.prime.internals.utils as utils


def test_to_path_str_accepts_str_and_path(tmp_path):
    """Path-like values normalize to filesystem strings."""
    as_str = str(tmp_path / "mesh.pmdat")
    assert utils.to_path_str(as_str) == as_str
    assert utils.to_path_str(Path(as_str)) == as_str


def test_file_read_context_accepts_path(tmp_path):
    """file_read_context yields a string path when given a Path."""
    target = tmp_path / "mesh.pmdat"
    target.write_text("placeholder")
    previous = config.using_container()
    try:
        config.set_using_container(False)
        with utils.file_read_context(None, target) as yielded:
            assert isinstance(yielded, str)
            assert yielded == str(target)
    finally:
        config.set_using_container(previous)


def test_file_write_context_accepts_path(tmp_path):
    """file_write_context yields a string path when given a Path."""
    target = tmp_path / "out.pmdat"
    previous = config.using_container()
    try:
        config.set_using_container(False)
        with utils.file_write_context(None, target) as yielded:
            assert isinstance(yielded, str)
            assert yielded == str(target)
    finally:
        config.set_using_container(previous)


def test_file_read_context_list_accepts_paths(tmp_path):
    """file_read_context_list normalizes every Path in the list."""
    paths = [tmp_path / "a.msh", tmp_path / "b.msh"]
    for path in paths:
        path.write_text("placeholder")
    previous = config.using_container()
    try:
        config.set_using_container(False)
        with utils.file_read_context_list(None, paths) as yielded:
            assert yielded == [str(path) for path in paths]
    finally:
        config.set_using_container(previous)


def test_container_staging_is_isolated_per_reader(tmp_path):
    """Concurrent readers of the same base name do not share a staged copy.

    The doc build runs the gallery in parallel, so two readers of the same file
    used to stage it under one path and delete it from under each other.
    """
    first = tmp_path / "one" / "mixing_elbow.fmd"
    second = tmp_path / "two" / "mixing_elbow.fmd"
    for path in (first, second):
        path.parent.mkdir(parents=True)
        path.write_text(path.parent.name)

    previous = config.using_container()
    try:
        config.set_using_container(True)
        with utils.file_read_context(None, first) as outer:
            with utils.file_read_context(None, second) as inner:
                assert outer != inner
            # the inner reader's cleanup must leave the outer staged copy alone
            staged = Path(defaults.get_examples_path(), Path(outer).parent.name, "mixing_elbow.fmd")
            assert staged.is_file()
            assert staged.read_text() == "one"
        assert not staged.parent.exists()
    finally:
        config.set_using_container(previous)
