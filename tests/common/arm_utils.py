import os
import sys


def is_running_in_arm():
    return 'ARM_RUN' in os.environ


def get_input_files_location():
    input_path = os.environ.get('INPUT_FILES', None)
    if input_path is None:
        if sys.platform.startswith('win32'):
            parts_dir = os.environ.get(
                'PARTS_DIR', r'\\smb.cdcislcore.ansys.com\ARM\ARM_v222\Parts'
            )
        else:
            parts_dir = os.environ.get('PARTS_DIR', r'/nfs/cdcisldev/ARM/SHARE/')
        input_path = os.path.join(parts_dir, 'FluentMeshing')
    if os.path.exists(input_path):
        os.environ['INPUT_FILES'] = input_path
        return input_path
    else:
        raise FileNotFoundError(f'INPUT_FILES path "{input_path}" does not exist.')
