
from "./job.py" import Moyenne

def test_moyenne():
    assert Moyenne(10, 2) == 6
    assert Moyenne(-1, 1) == 0

