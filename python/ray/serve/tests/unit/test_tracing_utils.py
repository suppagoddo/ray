import pytest

import ray.serve._private.tracing_utils as tracing_utils


class TestTracingEnabledFlag:
    def setup_method(self):
        self._original = tracing_utils._tracing_enabled
        tracing_utils._tracing_enabled = False

    def teardown_method(self):
        tracing_utils._tracing_enabled = self._original

    def test_is_tracing_enabled_false_by_default(self):
        assert tracing_utils.is_tracing_enabled() is False

    def test_is_tracing_enabled_true_after_set(self):
        tracing_utils._tracing_enabled = True
        assert tracing_utils.is_tracing_enabled() is True

    def test_is_tracing_enabled_false_after_reset(self):
        tracing_utils._tracing_enabled = True
        assert tracing_utils.is_tracing_enabled() is True
        tracing_utils._tracing_enabled = False
        assert tracing_utils.is_tracing_enabled() is False


if __name__ == "__main__":
    import sys

    sys.exit(pytest.main(["-v", "-s", __file__]))
