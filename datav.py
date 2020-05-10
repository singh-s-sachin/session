import fintech
fintech.register()
from fintech.ebics import EbicsKeyRing, EbicsBank, EbicsUser, EbicsClient

keyring = EbicsKeyRing(keys='~/mykeys', passphrase='mysecret')
bank = EbicsBank(keyring=keyring, hostid='MYBANK', url='https://www.mybank.de/ebics')
user = EbicsUser(keyring=keyring, partnerid='CUSTOMER123', userid='USER1')
# Create new keys for this user
user.create_keys(keyversion='A006', bitlength=2048)

client = EbicsClient(bank, user)
# Send the public electronic signature key to the bank.
client.INI()
# Send the public authentication and encryption keys to the bank.
client.HIA()

# Create an INI-letter which must be printed and sent to the bank.
user.create_ini_letter(bankname='MyBank AG', path='~/ini_letter.pdf')

# After the account has been activated the public bank keys
# must be downloaded and checked for consistency.
print(client.HPB())

# Finally the bank keys must be activated.
bank.activate_keys()

# Download CAMT53 bank account statements
data = client.C53(
    start='2019-02-01',
    end='2019-02-07',
    )
client.confirm_download()








#MguJTis/s2,j