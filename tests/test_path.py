import io
import zipfile


def test_malformed_paths():
    """
    Path should handle malformed paths.
    """
    data = io.BytesIO()
    zf = zipfile.ZipFile(data, "w")
    zf.writestr("/one-slash.txt", b"content")
    zf.writestr("//two-slash.txt", b"content")
    zf.writestr("../parent.txt", b"content")
    zf.filename = ''
    root = zipfile.Path(zf)
    assert list(map(str, root.iterdir())) == [
        'one-slash.txt',
        'two-slash.txt',
        'parent.txt',
    ]
