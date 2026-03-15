import pytest


def test_plugin_import():
    from testscope_plugin import TestScopePlugin

    plugin = TestScopePlugin()
    assert plugin.name == "testscope"
