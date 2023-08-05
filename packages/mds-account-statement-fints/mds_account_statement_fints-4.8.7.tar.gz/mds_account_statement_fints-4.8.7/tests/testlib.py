# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.


from trytond.pool import Pool
from trytond.modules.currency.tests.test_currency import create_currency 


def create_party(name, adrname, street, zip, city):
    """ create party with address and category
    """
    pool = Pool()
    Party = pool.get('party.party')
    Address = pool.get('party.address')

    pty1 = Party(name=name, 
            addresses=[
                    Address(name=adrname,
                        street=street,
                        zip=zip,
                        city=city,
                    )
                ],
        )

    pty1.save()
    return pty1
# end create_party


def create_bank(name, blz, url):
    pool = Pool()
    Party = pool.get('party.party')
    Bank = pool.get('bank')
    
    b1 = Bank(
            party = Party(name=name),
            fintsblz = blz, 
            fintsurl = url,
        )
    b1.save()
    return b1
# end create_bank


def create_bankaccount(bank, owner, numbers):
    pool = Pool()
    BankAccount = pool.get('bank.account')
    BankAccNumbr = pool.get('bank.account.number')
    Party = pool.get('party.party')
    
    curr1 = create_currency('EUR')

    ba1 = BankAccount(
            bank = bank,
            owners = [owner],
            currency = curr1,
            numbers=[BankAccNumbr(type='other', number=x) for x in numbers],
            active = True,
        )
    ba1.save()
    return ba1

# end create_bankaccount
