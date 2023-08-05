# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

import trytond.tests.test_tryton
import unittest

try:
    from trytond.modules.account_statement_fints.tests.test_bank import BankTestCase
except ImportError:
    from .test_bank import BankTestCase

__all__ = ['suite']


class AccountStatementFintsTestCase(\
            BankTestCase):
    'Test account-statement-fints module'
    module = 'account_statement_fints'

#end AccountStatementFintsTestCase


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(AccountStatementFintsTestCase))
    return suite
