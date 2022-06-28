from dbx.api.context import LocalContextManager
from dbx.models.context import ContextInfo


def test_local_context_serde():
    ctx = ContextInfo(context_id="000aaa")
    LocalContextManager.set_context(ctx)
    result = LocalContextManager.get_context()
    assert ctx == result


def test_local_context_non_existent():
    LocalContextManager.context_file_path.unlink(missing_ok=True)
    result = LocalContextManager.get_context()
    assert result is None
