# hooks/pre_gen_project.py
import sys
from cookiecutter.main import cookiecutter


cookiecutter(
    "cookiecutter-gotofritz-poetry/",
    extra_context={"project_folder": "<<<<AHGA AHAHA"},
)
sys.exit(0)
