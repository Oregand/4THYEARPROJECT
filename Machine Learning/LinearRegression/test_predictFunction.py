from unittest import TestCase
from LR import LR

__author__ = 'davidoregan'


class TestPredictFunction(TestCase):
    def test_transform(self):
        self.fail()

    def test_predict(self):
        self.fail()

    def test_predictP(self):
        p = LR
        self.assert_(Exception, p.predict)
