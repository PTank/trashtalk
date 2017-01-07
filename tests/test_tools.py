from trashtalk.tools import human_readable_from_bytes


def test_human_readable_from_bytes():
    b = human_readable_from_bytes(500)
    k = human_readable_from_bytes(1024)
    m = human_readable_from_bytes(1024**2)
    g = human_readable_from_bytes(1024**3)
    t = human_readable_from_bytes(1024**4)
    p = human_readable_from_bytes(1024**5)
    e = human_readable_from_bytes(1024**6)
    z = human_readable_from_bytes(1024**7)
    y = human_readable_from_bytes(1024**8)

    assert b == '500'
    assert k == "1K"
    assert m == "1M"
    assert g == "1G"
    assert t == "1T"
    assert p == "1P"
    assert e == "1E"
    assert z == "1Z"
    assert y == "1Y"
