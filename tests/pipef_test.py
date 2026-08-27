from operator import itemgetter

import pytest

import pipef


def test_exposes_a_version():
    assert isinstance(pipef.__version__, str)
    assert pipef.__version__


def _add_2(x):
    return x + 2


def _multiply_by_3(x):
    return x * 3


# Function factory (lazy)


def test_factory_builds_a_reusable_fn():
    fn = pipef.pipef | _add_2 | _multiply_by_3
    assert fn(1) == 9


def test_only_the_bare_class_opens_a_lazy_chain():
    fn = pipef.pipef | _add_2 | _multiply_by_3
    (result,) = pipef.pipef(1) | _add_2 | _multiply_by_3
    assert fn(1) == result


def test_factory_passes_through_all_call_args():
    fn = pipef.pipef | (lambda a, b, c=0: a + b + c) | _multiply_by_3
    assert fn(1, 2, c=3) == 18


def test_factory_forks_without_mutating_the_original():
    fn_1 = pipef.pipef | _add_2 | _multiply_by_3
    fn_2 = fn_1 | _add_2
    fn_3 = fn_1 | (lambda x: x - 3)
    assert fn_2(2) == 14
    assert fn_3(2) == 9
    assert fn_1(2) == 12


def test_factory_composes_with_another_lazy_pipef():
    add_2_mult_3 = pipef.pipef | _add_2 | _multiply_by_3
    mult_3_add_2 = pipef.pipef | _multiply_by_3 | _add_2
    fn = add_2_mult_3 | mult_3_add_2
    assert fn(1) == (1 + 2) * 3 * 3 + 2


def test_factory_forks_on_shared_lookups():
    get_bar = pipef.pipef | itemgetter("foo") | itemgetter("bar")
    a_dict = {"foo": {"bar": {"egg": 123}}}
    b_dict = {"foo": {"bar": {"spam": 456}}}
    assert (get_bar | itemgetter("egg"))(a_dict) == 123
    assert (get_bar | itemgetter("spam"))(b_dict) == 456


# Eager pipe


def test_eager_pipes_a_value_through_the_chain():
    (result,) = pipef.pipef(1) | _add_2
    assert result == 3


def test_eager_chains_multiple_steps():
    (result,) = pipef.pipef(1) | _add_2 | _multiply_by_3
    assert result == 9


def test_eager_with_no_pipe_yields_the_original_value():
    (result,) = pipef.pipef(1)
    assert result == 1


def test_eager_with_no_pipe_keeps_only_the_first_arg():
    (result,) = pipef.pipef(1, 2)
    assert result == 1


def test_eager_with_no_args_yields_none():
    (result,) = pipef.pipef()
    assert result is None


def test_eager_kwargs_only_raises_instead_of_losing_the_value():
    with pytest.raises(TypeError):
        pipef.pipef(x=1)()


def test_eager_is_not_hashable():
    with pytest.raises(TypeError):
        hash(pipef.pipef(2))


def test_eager_with_no_args_reprs_as_none():
    assert repr(pipef.pipef()) == "None"


def test_eager_first_step_receives_all_args_and_kwargs_spread():
    (result,) = pipef.pipef(1, 2, c=3) | (lambda a, b, c: a + b + c) | _add_2
    assert result == 8


def test_eager_with_no_args_still_calls_the_first_step():
    (result,) = pipef.pipef() | (lambda: 1) | _add_2
    assert result == 3


def test_eager_call_with_no_args_returns_the_same_value_as_unpacking():
    result_fn = pipef.pipef(1) | _add_2 | _multiply_by_3
    (result,) = result_fn
    assert result_fn() == result


def test_eager_forks_without_mutating_the_original():
    start = pipef.pipef(2)
    add_2 = start | _add_2
    multiply_by_3 = start | _multiply_by_3
    (add_2_result,) = add_2
    (multiply_by_3_result,) = multiply_by_3
    assert add_2_result == 4
    assert multiply_by_3_result == 6


def test_eager_result_forks_into_further_pipes():
    result_fn = pipef.pipef(2) | _add_2 | _multiply_by_3
    (result_1,) = result_fn | (lambda x: x + 5)
    (result_2,) = result_fn | (lambda x: x - 3)
    (result_0,) = result_fn
    assert result_1 == result_2 + 8
    assert result_0 == (2 + 2) * 3
