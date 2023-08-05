import pytest
from testfixtures import compare
import nbrmd
from .utils import list_all_notebooks


@pytest.mark.parametrize('py_file', list_all_notebooks('.py', '../nbrmd') +
                         list_all_notebooks('.py'))
def test_identity_source_write_read(py_file):
    with open(py_file) as fp:
        py = fp.read()

    nb = nbrmd.reads(py, ext='.py')
    py2 = nbrmd.writes(nb, ext='.py')

    compare(py, py2)
