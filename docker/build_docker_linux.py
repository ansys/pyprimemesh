# Copyright (C) 2024 ANSYS, Inc. and/or its affiliates.
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

"""Script to build linux based docker image for the pyprimemesh project."""
import json
import logging
import os
import re
import shutil
import subprocess
import sys

# -------------------------------------------------------------------------------
# Check input
if len(sys.argv) < 2:
    print("Please specify Ansys installation folder.")
    print("Example: {} /ansys_inc/v251".format(os.path.basename(__file__)))
    sys.exit(1)

AWP_ROOT = sys.argv[1]
if not os.path.exists(AWP_ROOT):
    print("Could not find Ansys installation folder '{}'. Please try again.".format(AWP_ROOT))
    sys.exit(1)

# -------------------------------------------------------------------------------
# Globals
MANIFEST_SYMLINKS = os.path.join(AWP_ROOT, "meshing", "Prime", "Manifest_PyPrimeSymlinks.json")
MANIFEST_FOUND_IN_UNIFIED = os.path.join(
    AWP_ROOT, "meshing", "Prime", "Manifest_AnsysInstallation.json"
)
ASSEMBLED_PACKAGE_ROOT = "PyPrimeMeshPackage"
LOG_FILE = "AssemblePyPrimeMeshServerPackage.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.DEBUG,
    filemode="w",
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M:%S",
)
# logging.getLogger().addHandler(logging.StreamHandler(sys.stderr))


def load_manifest():
    """Load Ansys unified installation match manifest."""
    with open(MANIFEST_FOUND_IN_UNIFIED, 'r', encoding='utf-8') as file:
        unifiedPathDict = json.load(file)

    # Load symlink manifest
    with open(MANIFEST_SYMLINKS, 'r', encoding='utf-8') as file:
        allSymlinkDict = json.load(file)

    return unifiedPathDict, allSymlinkDict


def create_symlink(link, target):
    """Create symlinks as specified in PyPrimeMesh package manifest."""
    cmd = ['ln', '-s', target, link]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (stdoutdata, stderrdata) = p.communicate()


def assemble_full_package(unifiedPathDict, allFileDict, dest_package_path):
    """Assemble standalone PyPrimeMesh package using Ansys installation as source."""
    if os.path.exists(dest_package_path):
        shutil.rmtree(dest_package_path, ignore_errors=True)

    # copy entire CPython directory
    shutil.copytree(
        os.path.join(AWP_ROOT, "commonfiles", "CPython"),
        os.path.join(dest_package_path, "commonfiles", "CPython"),
        symlinks=True,
    )

    # copy parasolid schema
    shutil.copytree(
        os.path.join(
            AWP_ROOT, "commonfiles", "CAD", "Siemens", "Parasolid36.1.212", "linx64", "schema"
        ),
        os.path.join(
            dest_package_path,
            "commonfiles",
            "CAD",
            "Siemens",
            "Parasolid36.1.212",
            "linx64",
            "schema",
        ),
    )

    # copy JTOpen dependency
    shutil.copytree(
        os.path.join(AWP_ROOT, "commonfiles", "CAD", "Siemens", "JTOpen", "linx64"),
        os.path.join(dest_package_path, "commonfiles", "CAD", "Siemens", "JTOpen", "linx64"),
    )

    if not os.path.exists(os.path.join(dest_package_path, "aisol", "bin", "linx64")):
        os.makedirs(os.path.join(dest_package_path, "aisol", "bin", "linx64"))
    # copy FMTransmogrifier
    shutil.copy(
        os.path.join(AWP_ROOT, "aisol", "bin", "linx64", "FMTransmogrifier_JT"),
        os.path.join(dest_package_path, "aisol", "bin", "linx64", "FMTransmogrifier_JT"),
    )
    shutil.copy(
        os.path.join(AWP_ROOT, "aisol", "bin", "linx64", "FMTransmogrifier_WB"),
        os.path.join(dest_package_path, "aisol", "bin", "linx64", "FMTransmogrifier_WB"),
    )
    shutil.copy(
        os.path.join(AWP_ROOT, "aisol", "bin", "linx64", "FMTransmogrifier_XC"),
        os.path.join(dest_package_path, "aisol", "bin", "linx64", "FMTransmogrifier_XC"),
    )

    # Copy regular files
    for key, value in unifiedPathDict.items():
        val_list = value if isinstance(value, list) else [value]
        for val in val_list:
            source = os.path.join(AWP_ROOT, val["path"], key)
            target = os.path.join(dest_package_path, val["path"])
            if not os.path.exists(target):
                os.makedirs(target)

            logging.info("\tcopying source {} --> target {}".format(source, target))
            shutil.copy(source, target)

    # copy libFM so files
    for file in os.listdir(os.path.join(AWP_ROOT, "aisol", "lib", "linx64")):
        if "libFM" in file:
            shutil.copy(
                os.path.join(AWP_ROOT, "aisol", "lib", "linx64", file),
                os.path.join(dest_package_path, "meshing", "Prime", "lib"),
            )

    # Copy symlinks
    for key, value in allSymlinkDict.items():
        dest_folder = re.sub(r'.*meshing/Prime', 'meshing/Prime', value["path"])
        symlink_folder = os.path.join(dest_package_path, dest_folder)
        try:
            os.chdir(symlink_folder)
            cur_dir = os.getcwd()

            if os.path.exists(value["target"]):
                logging.info(
                    "\tcreating symlink {}/{} --> target {}".format(
                        cur_dir, value["link"], value["target"]
                    )
                )
                create_symlink(value["link"], value["target"])
            else:
                logging.warning(
                    "\tcould not create symlink {}/{} --> target {}. Target does not exist.".format(
                        symlink_folder, value["link"], value["target"]
                    )
                )
        except:
            pass


def create_docker_image(dest_package_path):
    """Create docker image from the archived package."""
    # Check if Docker is installed on the system
    print(">>> Checking if Docker is installed")
    if shutil.which("docker") is None:
        print("XXXXXXX Docker is not installed.. exiting process. XXXXXXX")
        exit(1)

    # Build the docker image
    print(">>> Building docker image. This might take some time...")
    out = subprocess.run(
        ["docker", "build", "-f", "linux/Dockerfile", "-t", "ghcr.io/ansys/prime:latest", "."],
        cwd=os.path.dirname(os.path.abspath(__file__)),
        capture_output=True,
    )


# -------------------------------------------------------------------------------
#
# stand-alone use
#

if __name__ == "__main__":

    try:

        # change into the directory where the script resides
        root = os.path.dirname(os.path.abspath(__file__))
        dest_package_path = os.path.join(root, ASSEMBLED_PACKAGE_ROOT)
        os.chdir(root)

        unifiedPathDict, allSymlinkDict = load_manifest()

        logging.info("Assembling Ansys PyPrimeMesh server package...")
        print("Assembling Ansys PyPrimeMesh server package...")
        assemble_full_package(unifiedPathDict, allSymlinkDict, dest_package_path)

        logging.info(
            "Processing complete. PyPrimeMesh server package assembled in {}.".format(
                dest_package_path
            )
        )
        print(
            "Processing complete. \nPyPrimeMesh server package assembled in {}. "
            "\nDetails in log file {}.".format(dest_package_path, LOG_FILE)
        )

        create_docker_image(dest_package_path)

        shutil.rmtree(dest_package_path)

    except SystemExit:
        raise
    except Exception as msg:
        logging.info(
            """ %s\n
        An internal error occurred."""
            % msg
        )
        sys.exit(1)
