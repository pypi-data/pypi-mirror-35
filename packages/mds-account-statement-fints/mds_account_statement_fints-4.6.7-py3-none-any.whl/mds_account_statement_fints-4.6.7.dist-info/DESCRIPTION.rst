mds-account-statement-fints
===========================
Tryton module for importing bank statements via Internet 
from your bank using the FinTS-3 protocol.

Install
-------
pip install mds-account-statement-fints

Limitations
-----------
- PIN/TAN authentication only
- read only access

How to setup
============

Configure access to your bank
-----------------------------
Create your Bank
  Open *Banking/Banks* and create your bank. The value for the *FinTS-URL* can 
  be found on the website 'https://www.hbci-zka.de/institute/institut_auswahl.htm', 
  search for your bank and copy the value for *PIN/TAN-URL*.
Create Account
  Open *Banking/Account*. Create an account and enter owner, currency, 
  and the bank you just created. Your company must be the owner of the bank account to 
  allow online access. Create a 'Number'. Enter your IBAN and activate 'enable online 
  access'. In 'FinTS-Login' enter the login name for your online account.
  You can also enter the PIN.  If you leave the field blank, you will be 
  prompted for the PIN each time you access online banking.
Check connection
  Open *Banking/Account*, mark the accounts to be checked. Click the action 
  button and select 'Check bank access'. If the connection works, 
  the dialog will display the list of available SEPA accounts.  

Create journals
---------------
Journal for account transactions
  In *Finance/Configuration/Journals/Journals* create a new entry and enter a name, 
  e.g. 'BankXY bookings', the type is 'statement'. Enter in *Default Debit Account*
  and *Default Credit Account* an account from your chart of accounts. In the german 
  SKR04 for example '1810'. This account will receive all account movements of your 
  bank account. In *sequence* use the existing 'Default Account Journal'.
Statement Journal
  In *Finance/Configuration/Statements/Statement Journals* create a new entry and 
  enter a name, eg 'BankXY statements'. Enter the other values: *Currency:* Euro, 
  *Journal:* the journal created above, *Company:* your company, 
  *Bank Account:* the bank account created above, *Validation Type:* Balance. 
  This journal will contain the bank statements.

Permissions
-----------
*Account Statement FinTS - edit logindata*
  allows the user to change the connection settings and the login data to the bank
*Account Statement FinTS - online access*
  allows the user online access to the bank

The following permissions are required for a user to fetch the account statements:
  - Account Statement FinTS online access
  - Account

In order to allow the automatic generation of bank accounts of the payer/payee 
the user needs the permission 'Bank Adminstration'.


Pick up bank statements
=======================
Open *Finance/Statements/Statements*, click the action button and then 
'Import bank statements online'. The wizard will guide you through the 
import. For new payments, a statement is created in draft mode. 
You can then check and commit the statement.

Invoices that have to be paid are automatically linked with appropriate
lines of the bank statement if: the invoice number appears in the purpose 
and the amount corresponds to the invoice amount.

Requires
========
- Tryton 4.6
- fints (tested with 1.0.1)
- mt-940 (tested with 4.12.2)
- Python 3

Banks tested
============
 - DKB, Postbank, Deutsche Bank, Sparkasse

Changes
=======

4.6.7 - 22.08.2018
- new: bank bccount list contains name of bank
- fix: UI improvements
- fix: exception if starting the import with an empty account list
- dependency changed to mt-940 >= 4.12.2 (removed mt-940 fixing)

4.6.6 - 07/02/2018
 - fix: improved version detection with 'mt-940'

4.6.5 - 06/02/2018
 - fix: add depency to 'pytz'
 - fix: transaction details was not decoded if message not starts with posting text

4.6.4 - 17/01/2018
 - new: Button on import wizard to show new bank statements

4.6.3 - 15/01/2018
 - fix: use alternative date with missing entry_date on statement lines
 - fix: exception handling on import error

4.6.2 - 12/01/2018
 - Importwizard improved, checkboxes for connecting invoices and ignore duplicates

4.6.1 - 11/01/2018
 - Improved recognition of known account statement lines

4.6.0 - 08/01/2018
 - first public version


