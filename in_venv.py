import sys
import os

def get_environment_type():
    """Check if the current Python environment is a virtual environment or a Conda environment."""
    # Check for standard Python venv
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        return "venv"
    # Check for Conda environment
    if 'CONDA_PREFIX' in os.environ:
        return "conda"
    return "global"

env_type = get_environment_type()

if env_type == "venv":
    print('Inside a Python virtual environment')
    venv_path = os.environ.get('VIRTUAL_ENV')
    if venv_path:
        print(f"Current VENV path: {venv_path}")
elif env_type == "conda":
    print('Inside a Conda environment')
    conda_path = os.environ.get('CONDA_PREFIX')
    if conda_path:
        print(f"Current Conda path: {conda_path}")
else:
    print('Not in an isolated environment (using global Python)')