# hooks/pre_gen_project.py
import sys
from cookiecutter.main import cookiecutter


cookiecutter(
    "work/cookiecutter-gotofritz-poetry",
    replay=None,
    extra_context={"full_name": "<<<<ARRGGH"},
)
sys.exit(0)
