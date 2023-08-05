from unittest import TestCase


class Assert:

    @staticmethod
    def assert_true(msg, condition):
        """
        断言condition为真则pass
        :param msg: 
        :param condition: 
        :return: 
        """
        if condition:
            print(msg + "检查通过")
            TestCase().assertTrue(condition, msg)
        else:
            print(msg + "检查不通过")
            TestCase().assertTrue(condition, msg)

    @staticmethod
    def assert_flase(msg, condition):
        """
        断言condition为假则pass
        :param msg:
        :param condition:
        :return:
        """
        if not condition:
            TestCase().assertFalse(condition, msg)
        else:
            print(msg + "检查不通过")
            TestCase().assertFalse(condition, msg)

    @staticmethod
    def assert_int_equal(msg, actual, expected):
        """
         判断int型数据相等则pass
         :param msg:
         :param actual:
         :param expected:
         :return:
         """
        if actual == expected:
            print(msg + ":检查通过,实际值 =" + str(actual))
            TestCase().assertEqual(actual, expected, msg)
        else:
            print(msg + ":检查不通过,预期值为(" + str(expected) + "),实际为(" + str(actual) + ")")
            TestCase().assertEqual(actual, expected, msg)

    @staticmethod
    def assert_float_equal(msg, actual, expected):
        """
        判断float型数据相等则pass
        :param msg: 
        :param actual: 
        :param expected: 
        :return: 
        """
        if actual == expected:
            print(msg + ":检查通过,实际值 =" + str(actual))
            TestCase().assertEqual(actual, expected, msg)
        else:
            print(msg + ":检查不通过,预期值为(" + str(expected) + "),实际为(" + str(actual) + ")")
            TestCase().assertEqual(actual, expected, msg)

    @staticmethod
    def assert_str_equal(msg, actual, expected):
        """
         判断字符串相等则pass
         :param msg: 
         :param actual: 
         :param expected: 
         :return: 
         """
        actual = str(actual)
        if actual.strip() == expected.strip():
            if expected == "":
                print(msg + ":检查通过,实际值 =空")
                TestCase().assertEqual(actual, expected, msg)
            else:
                print(msg + ":检查通过,实际值 =" + actual)
                TestCase().assertEqual(actual, expected, msg)
        else:
            print(msg + ":检查不通过,预期值为(" + expected + "),实际为(" + actual + ")")
            TestCase().assertEqual(actual, expected, msg)

    @staticmethod
    def assert_null(msg, object):
        """
         判断对象是否不为null，如果等于null则pass
        :param msg:
        :param object:
        :return:
        """
        if object is None:
            print(msg + ":检查通过,为空")
            TestCase().assertIsNone(object, msg)
        else:
            print(msg + ":检查不通过,预期值为空,实际不为空")
            TestCase().assertIsNone(object, msg)

    @staticmethod
    def assert_not_null(msg, object):
        """
        判断对象是否不为null，如果不等于null则pass
        :param msg:
        :param object:
        :return:
        """
        if object is not None:
            print(msg + ":检查通过,不为空")
            TestCase().assertIsNotNone(object ,msg)
        else:
            print(msg + ":检查不通过,预期值不为空,实际为空");
            TestCase().assertIsNotNone(object, msg)

    @staticmethod
    def assert_int_not_equal(msg, actual, expected):
        """
        判断actual是否不等于expected，若actual != expected则pass
        :param msg:
        :param actual:
        :param expected:
        :return:
        """
        if actual != expected:
            print(msg + ":检查通过,预期值为不等于(" + str(expected) + "),实际为(" + str(actual) + ")")
            TestCase().assertNotEqual(actual, expected, msg)
        else:
            print(msg + ":检查不通过,实际值 =" + str(actual))
            TestCase().assertNotEqual(actual, expected, msg)

    @staticmethod
    def assert_float_not_equal(msg, actual, expected):
        """
        判断actual是否不等于expected，若actual != expected则pass
        :param msg:
        :param actual: 
        :param expected: 
        :return: 
        """
        if actual != expected:
            print(msg + ":检查通过,预期值为不等于(" + str(expected) + "),实际为(" + str(actual) + ")")
            TestCase().assertNotEqual(actual, expected, msg)
        else:
            print(msg + ":检查不通过,实际值 =" + str(actual))
            TestCase().assertNotEqual(actual, expected, msg)

    @staticmethod
    def assert_str_not_equal(msg, actual, expected):
        """
        判断actual是否不等于expected，若actual != expected则pass
        :param msg:
        :param actual:
        :param expected:
        :return:
        """
        if actual.strip() != (expected.strip()):
            print(msg + ":检查通过,实际值 = " + actual)
            TestCase().assertNotEqual(actual, expected, msg)
        else:
            print(msg + ":检查不通过,预期值不为(" + expected + "),实际为(" + actual + ")")
            TestCase().assertNotEqual(actual, expected, msg)

    @staticmethod
    def assert_in(msg, actual, expected):
        """
        若expected包含actual则pass
        :param msg: 
        :param actual: 
        :param expected: 
        :return: 
        """
        if actual.strip() != "" or expected.strip() != "":
            if expected in actual:
                print(msg + ":检查通过,实际值包含(" + expected + ")")
                TestCase().assertIn(expected, actual, msg)
            else:
                print(msg + ":检查不通过,预期值包含(" + expected + "),实际为(" + actual + ")")
                TestCase().assertIn(expected, actual, msg)
        else:
            print(msg + ":检查不通过,逾期和实际都为空")
            TestCase().assertTrue(1 != 1, msg)

    @staticmethod
    def assert_not_in(msg, actual, expected):
        """
        若expected不包含actual则pass
        :param msg:
        :param expected:
        :param actual:
        :return:
        """
        if actual.strip() != "" or expected.strip() != "":
            if expected not in actual:
                print(msg + ":检查通过,预期值不包含(" + expected + "),实际为(" + actual + ")")
                TestCase().assertNotIn(expected, actual, msg)
            else:
                print(msg + ":检查不通过,预期值(" + expected + "),实际为(" + actual + ")")
                TestCase().assertNotIn(expected, actual, msg)
        else:
            print(msg + ":检查不通过,逾期和实际都为空")
            TestCase().assertTrue(1 != 1, msg)
