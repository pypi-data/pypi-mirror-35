# SPDX-License-Identifier: LGPL-2.1+

import pytest
import rustcfg

asdf_data = [
    # None means expression is unparsable
    ('cfg(ok)', True),
    ('cfg(not_ok)', False),
    ('cfg( ok )', True),
    ('cfg(foo-bar-bar)', None),
    ('cfg(foo_bar_bar)', True),
    (' foo-bar-bar ', False),
    (' cfg(not(foo))', False),
    (' cfg(not(foo foo))', None),
    ('cfg(any(asdf, asdf))', True),
    ('cfg(all(asdf, asdf))', True),
    ('cfg(any())', None),
    ('cfg(all())', None),
    ('cfg(all(not(asdf)))', False),
    ('cfg(all(not(any(all(asdf)))))', False),
    ('cfg(foo="bar")', True),
    ('cfg(foo = "bar")', True),
    ('cfg(foo = " bar ")', True),
    ('cfg(foo = "not bar")', False),
    ('cfg(foo=bar)', None),
    ('cfg(foo foo = = " bar ")', None),
    ('cfg(foo = foo = " bar ")', None)]

@pytest.fixture
def asdf_evaluator():
    options = ('ok',
               'foo_bar_bar',
               'foo',
               'asdf',
               ('foo', 'bar'),
               ('foo', ' bar '))
    return rustcfg.Evaluator(options=options)

@pytest.mark.parametrize("expression,result", asdf_data)
def test_parsing(expression, result, asdf_evaluator):
    g = rustcfg.cfg_grammar()
    try:
        t = g.parseString(expression)
    except Exception:
        good = False
    else:
        good = True
    assert good == (result is not None)

    if result is not None:
        res = asdf_evaluator.eval_tree(t)
        assert res == result

linux_data = [
    ('cfg(unix)', True),
    ('cfg(windows)', False),

    ('cfg(all(unix, not(target_os = "fuchsia"), not(target_os = "emscripten"), not(target_os = "macos"), not(target_os = "ios")))', True),
    ("cfg(all(unix, not(target_os = \"fuchsia\"), not(target_os = \"emscripten\"), not(target_os = \"macos\"), not(target_os = \"ios\")))", True),

    ("cfg(all(unix, not(target_os = \"macos\")))", True),
    ('cfg(not(any(target_os = "windows", target_os = "macos")))', True),
    ('cfg(not(target_os = "redox"))', True),
    ('cfg(not(target_os = "windows"))', True),
    ("cfg(not(target_os = \"windows\"))", True),
    ('cfg(target_env = "msvc")', False)]

@pytest.fixture
def linux_evaluator():
    return rustcfg.Evaluator.platform()

@pytest.mark.parametrize("expression,result", linux_data)
def test_linux(expression, result, linux_evaluator):
    res = linux_evaluator.parse_and_eval(expression)
    assert res == result
