# -*- coding: utf-8 -*-

# $Id:$

from __future__ import print_function
from __future__ import unicode_literals
from future.utils import PY3

import unittest
if PY3:
    from unittest import mock
else:
    import mock

from django.utils.datastructures import MultiValueDict

from .. import validators as V
from ..schema import Bool
from ..schema import Float
from ..schema import Int
from ..schema import List
from ..schema import Schema
from ..schema import String
from ..schema import _Type
from ..schema import _UNDEFINED


class _BaseTestCase(unittest.TestCase):

    def assertConversion(self, value, expected, type_=None):
        if type_ is None:
            type_ = self.type_
        self.assertEqual(type_.to_python(value), expected)

    def assertValidationFails(self, value, regex=None, type_=None):
        if regex is None:
            manager = self.assertRaises(V.SchemaError)
        else:
            manager = self.assertRaisesRegexp(V.SchemaError, regex)
        if type_ is None:
            type_ = self.type_
        with manager:
            type_.to_python(value)


class Test_Type(_BaseTestCase):

    def mock_python_type(self, type_, **kwargs):
        return mock.patch.object(type_, "python_type", **kwargs)

    # to_python

    ## managing undefined values

    def test_to_python_UNDEFINED_with_no_default_raises_SchemaError(self):
        type_ = _Type()
        with self.assertRaisesRegexp(V.SchemaError, r"missing required value"):
            type_.to_python(_UNDEFINED)

    def test_to_python_UNDEFINED_performs_convertion_on_default(self):
        type_ = _Type(default=42)
        with self.mock_python_type(type_) as python_type:
            type_.to_python(_UNDEFINED)
            python_type.assert_called_once_with(42)

    def test_to_python_UNDEFINED_runs_validators_on_default(self):
        type_ = _Type(default=42, validators=[mock.Mock()])
        with mock.patch.object(type_, "_apply_validators") as apply_validators:
            with self.mock_python_type(type_, return_value=314):
                type_.to_python(_UNDEFINED)
                apply_validators.assert_called_once_with(314)

    ## initial type conversion

    def test_to_python_calls_self_dot_python_type(self):
        type_ = _Type()
        with self.mock_python_type(type_, return_value=314) as pt:
            self.assertEqual(type_.to_python(42), 314)
            pt.assert_called_once_with(42)

    def test_to_python_converts_TypeError_to_SchemaError(self):
        type_ = _Type()
        with self.mock_python_type(type_, side_effect=TypeError("foo")):
            with self.assertRaisesRegexp(V.SchemaError, r"foo"):
                type_.to_python(42)

    def test_to_python_converts_ValueError_to_SchemaError(self):
        type_ = _Type()
        with self.mock_python_type(type_, side_effect=ValueError("foo")):
            with self.assertRaisesRegexp(V.SchemaError, r"foo"):
                type_.to_python(42)

    def test_to_python_ignores_other_exceptions(self):
        type_ = _Type()
        with self.mock_python_type(type_, side_effect=ZeroDivisionError("foo")):
            with self.assertRaisesRegexp(ZeroDivisionError, r"foo"):
                type_.to_python(42)

    ## extra validators

    def test_to_python_chains_python_type_with__apply_validators(self):
        type_ = _Type()
        with mock.patch.object(type_, "_apply_validators", return_value=12345) as av:
            with self.mock_python_type(type_, return_value=314) as pt:
                self.assertEqual(type_.to_python(42), 12345)
                pt.assert_called_once_with(42)
                av.assert_called_once_with(314)

    # _apply_validators

    def test_apply_validators_chains_results(self):
        validators = [
            mock.Mock(return_value=23),
            mock.Mock(return_value=42),
        ]
        type_ = _Type(validators=validators)
        type_._apply_validators("asdf")
        validators[0].assert_called_once_with("asdf")
        validators[1].assert_called_once_with(23)

    def test_apply_validators_returns_last_result(self):
        validators = [
            mock.Mock(return_value=23),
            mock.Mock(return_value=42),
        ]
        type_ = _Type(validators=validators)
        self.assertEqual(type_._apply_validators("asdf"), 42)

    def test_validators_chain_stops_on_first_error(self):
        validators = [
            mock.Mock(return_value=23),
            mock.Mock(side_effect=V.SchemaError),
            mock.Mock(return_value=42),
        ]
        type_ = _Type(validators=validators)
        with self.assertRaises(V.SchemaError):
            type_._apply_validators("asdf")
        self.assertEqual(validators[0].call_count, 1)
        self.assertEqual(validators[1].call_count, 1)
        self.assertEqual(validators[2].call_count, 0)


class TestBool(_BaseTestCase):

    def setUp(self):
        self.type_ = Bool()

    def test_initial_conversion(self):
        self.assertConversion("true", True)
        self.assertConversion(True, True)
        self.assertConversion("false", False)
        self.assertConversion(False, False)
        self.assertValidationFails("True", "not boolean.*")
        self.assertValidationFails("False", "not boolean.*")
        self.assertValidationFails("0", "not boolean.*")
        self.assertValidationFails("1", "not boolean.*")
        self.assertValidationFails("a", "not boolean.*")


class TestInt(_BaseTestCase):

    def setUp(self):
        self.type_ = Int()

    def test_initial_conversion(self):
        self.assertConversion("0", 0)
        self.assertConversion("42", 42)
        self.assertConversion("-314", -314)
        self.assertValidationFails("a")
        self.assertValidationFails("3.14")


class TestFloat(_BaseTestCase):

    def setUp(self):
        self.type_ = Float()

    def test_initial_conversion(self):
        self.assertConversion("0", 0)
        self.assertConversion("42", 42)
        self.assertConversion("-314", -314)
        self.assertConversion("3.14", 3.14)
        self.assertValidationFails("a")


class TestList(_BaseTestCase):

    def test_initial_conversion(self):
        self.assertConversion(["1", "3"], [1, 3], type_=List(Int()))

    def test_undefined_list_without_default_raise_SchemaError(self):
        type_ = List(Int())
        with self.assertRaisesRegexp(V.SchemaError, r"missing required value"):
            type_.to_python(_UNDEFINED)

    def test_undefined_list_with_default_returns_default(self):
        type_ = List(Int(), default=[42, 314])
        self.assertEqual(type_.to_python(_UNDEFINED), [42, 314])

    def test_calls_item_type_dot_to_python_for_each_item(self):
        to_python = mock.Mock(wraps=lambda x: int(x) * 2)
        item_type = _Type()
        item_type.to_python = to_python
        type_ = List(item_type)

        # just to be sure that mocking hasn't broken anything
        self.assertConversion(["1", "-3", "42"], [2, -6, 84], type_=type_)

        self.assertEqual(to_python.call_count, 3)
        self.assertEqual(
            to_python.call_args_list,
            [(("1", ), ), (("-3", ), ), (("42", ), )]
        )

    def test_applies_validators_to_the_resulting_list(self):
        v = mock.Mock(return_value="whatever")
        type_ = List(Int(), validators=[v])
        self.assertEqual(type_.to_python(["1", "3"]), "whatever")
        v.assert_called_once_with([1, 3])


class TestSchema(_BaseTestCase):

    def setUp(self):
        self.type_ = Schema(
            schema=dict(
                name=String(),
                value=Int(),
                items=List(String(), default=[])
            )
        )
        self.type_with_default = Schema(
            schema=dict(
                name=String(),
                value=Int(),
                items=List(String(), default=["foo", "bar"])
            ),
            default=dict(name="Bob", value=42),
        )

    def mk_dict(self, **kwargs):
        res = MultiValueDict()
        for k, v in kwargs.items():
            if isinstance(v, list):
                res.setlist(k, v)
            else:
                res[k] = v
        return res

    # __init__

    def test_init_converts_default_to_MultiValueDict(self):
        self.assertIsInstance(self.type_with_default.default, MultiValueDict)

    def test_MultiValueDict_conversion(self):
        d = {"the answer": 42, "hello": "world", "a_list": ["of", "things"]}
        res = Schema._make_multidict(d)
        self.assertIsInstance(res, MultiValueDict)
        self.assertEqual(res.get("the answer"), 42)
        self.assertEqual(res.get("hello"), "world")
        self.assertEqual(res.get("a_list"), "things")
        self.assertEqual(res.getlist("a_list"), ["of", "things"])

    # to_python

    def test_undefined_dict_without_default_raises_SchemaError(self):
        with self.assertRaisesRegexp(V.SchemaError, r"missing required value"):
            self.type_.to_python(_UNDEFINED)

    def test_undefined_dict_with_default_returns_default_augmented(self):
        self.assertNotIn("default", self.type_with_default.default)
        self.assertEqual(
            self.type_with_default.to_python(_UNDEFINED),
            {"name": "Bob", "value": 42, "items": ["foo", "bar"]}
        )

    def test_raises_SchemaError_if_value_contains_unknown_fields(self):
        value = self.mk_dict(
            name="Bob", value="3", unexpected="not in the schema"
        )
        with self.assertRaisesRegexp(V.SchemaError, r"Unknown field.*"):
            self.type_.to_python(value)

    def test_initial_conversion(self):
        value = self.mk_dict(name="Bob", value="3")
        self.assertConversion(
            value,
            {"name": "Bob", "value": 3, "items": []},
        )

    def test_validates_individual_keys(self):
        value = self.mk_dict(name="Bob", value="x")
        self.assertValidationFails(value, r"value: invalid literal.*")

    def test_applies_validators_to_the_resulting_dict(self):
        value = self.mk_dict(name="Bob", value="3")
        v = mock.Mock(return_value="whatever")
        self.type_._validators = [v]
        self.assertEqual(self.type_.to_python(value), "whatever")
        v.assert_called_once_with({"name": "Bob", "value": 3, "items": []})
