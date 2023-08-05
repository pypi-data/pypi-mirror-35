# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.tests.test_tryton import ModuleTestCase, with_transaction
from trytond.pool import Pool
from trytond.transaction import Transaction
from trytond.exceptions import UserError
from trytond.modules.account_statement_fints.tests.testlib import create_bank,\
    create_bankaccount, create_party


class BankTestCase(ModuleTestCase):
    'Test bank module'
    module = 'account_statement_fints'

    @with_transaction()
    def test_bank_create_item(self):
        """ test: create valid bank item
        """
        bank1 = create_bank(name = 'Bank 1', blz = '10010010', url='https://fints.bank.foo')
        
        self.assertTrue(bank1)
        self.assertEqual(bank1.rec_name, 'Bank 1')
        self.assertEqual(bank1.fintsblz, '10010010')
        self.assertEqual(bank1.fintsurl, 'https://fints.bank.foo')

    @with_transaction()
    def test_bankaccount_fints(self):
        """ test: check fints-fields
        """
        bank1 = create_bank(name='Bank 1', blz='10010010', url='https://fints.bank.foo')
        pty1 = create_party(name='Frida', adrname='Kahlo', street='Painter 1', zip='12345', city='Berlin')
        ba1 = create_bankaccount(bank=bank1, owner=pty1, numbers=['1234567890'])
        
        self.assertTrue(ba1)
        self.assertEqual(ba1.bank.rec_name, 'Bank 1')
        self.assertEqual(len(ba1.numbers), 1)
        self.assertEqual(ba1.numbers[0].rec_name, '1234567890 (Bank 1)')
        
        # owners
        self.assertEqual(len(ba1.numbers[0].fints_company), 1)
        self.assertEqual(ba1.numbers[0].fints_company[0].rec_name, 'Frida')

        # enable online access
        nmbr = ba1.numbers[0]
        nmbr.fints_ena = True
        nmbr.fints_name ='1'
        nmbr.fints_login = '1'
        nmbr.save()
        
        self.assertEqual(ba1.numbers[0].fints_ena, True)
        self.assertEqual(ba1.numbers[0].fints_name, '1')
        self.assertEqual(ba1.numbers[0].fints_login, '1')

    @with_transaction()
    def test_bankaccount_owners_text(self):
        """ test: generate owners text
        """
        bank1 = create_bank(name='Bank 1', blz='10010010', url='https://fints.bank.foo')
        pty1 = create_party(name='Frida', adrname='Kahlo', street='Painter 1', zip='12345', city='Berlin')
        ba1 = create_bankaccount(bank=bank1, owner=pty1, numbers=['1234567890'])
        
        # single owner
        self.assertTrue(ba1)
        self.assertEqual(ba1.bank.rec_name, 'Bank 1')
        self.assertEqual(len(ba1.owners), 1)
        self.assertEqual(ba1.owners[0].rec_name, 'Frida')
        self.assertEqual(len(ba1.numbers), 1)
        self.assertEqual(ba1.numbers[0].rec_name, '1234567890 (Bank 1)')
        
        self.assertEqual(ba1.owners_text, 'Frida')
        
        # two owners
        pty2 = create_party(name='Diego', adrname='Riviera', street='Painter 1', zip='12345', city='Berlin')
        l1 = list(ba1.owners)
        l1.append(pty2)
        ba1.owners = l1
        ba1.save()
        self.assertEqual(len(ba1.owners), 2)

        self.assertEqual(ba1.owners_text, '%s, ...' % ba1.owners[0].rec_name)

# end BankTestCase
