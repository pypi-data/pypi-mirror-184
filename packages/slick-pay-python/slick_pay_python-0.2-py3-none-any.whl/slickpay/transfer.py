import requests


class Transfer:
    def __init__(self, public_key, sandbox):
        self.public_key = public_key
        self.sandbox = sandbox

    def calculateCommission(self, amount):
        if self.sandbox:
            url = 'http://slickpay-v2.azimutbscenter.com/transfers/commission'
        else:
            url = 'http://slickpay-v2.azimutbscenter.com/transfers/commission'

        headers = {"Authorization": f'{str(self.public_key)}', "Accept": "application/json"}
        data = {
            'amount': amount
        }
        res = requests.post(url, headers=headers, data=data)
        return res.content

    def createPayment(self, data):
        if self.sandbox:
            url = 'http://slickpay-v2.azimutbscenter.com/transfers'
        else:
            url = 'http://slickpay-v2.azimutbscenter.com/transfers'
        headers = {"Authorization": f'{str(self.public_key)}', "Accept": "application/json"}
        res = requests.post(url, headers=headers, data=data)
        body = res.json()
        return body

    def paymentStatus(self, transfer_id):
        if self.sandbox:
            url = f'https://dev.transfer.slick-pay.com/api/user/transfer/{int(transfer_id)}'
        else:
            url = f'https://transfer.slick-pay.com/api/user/transfer/{int(transfer_id)}'
        headers = {"Authorization": 'Bearer 5|6itxL9D8tf1Fw2vnfcxyTdvmayD9er3mFZv3LzHF', "Accept": "application/json"}

        res = requests.get(url, headers=headers)

        return res.content

    def paymentHistory(self, offset):
        if self.sandbox:
            url = f'https://dev.transfer.slick-pay.com/api/user/transfer?offset={int(offset)}'
        else:
            url = f'https://transfer.slick-pay.com/api/user/transfer?offset={int(offset)}'
        headers = {"Authorization": f'{str(self.public_key)}', "Accept": "application/json"}
        res = requests.get(url, headers=headers)

        return res.content

    def paymentDetail(self, uid):
        if self.sandbox:
            url = f'http://slickpay-v2.azimutbscenter.com/transfers/{int(uid)}'
        else:
            url = f'http://slickpay-v2.azimutbscenter.com/transfers/{int(uid)}'
        headers = {"Authorization": f'{str(self.public_key)}', "Accept": "application/json"}
        res = requests.get(url, headers=headers)

        return res.content

    def listTransfer(self, offset, page):
        if self.sandbox:
            url = f'http://slickpay-v2.azimutbscenter.com/transfers?offset={int(offset)}&page={int(page)}'
        else:
            url = f'http://slickpay-v2.azimutbscenter.com/transfers?offset={int(offset)}&page={int(page)}'
        headers = {"Authorization": f'{str(self.public_key)}', "Accept": "application/json"}
        res = requests.get(url, headers=headers)

        return res.content

    def updateTransfer(self, data, uid):
        if self.sandbox:
            url = f'http://slickpay-v2.azimutbscenter.com/transfers/{int(uid)}'
        else:
            url = f'http://slickpay-v2.azimutbscenter.com/transfers/{int(uid)}'
        headers = {"Authorization": f'{str(self.public_key)}', "Accept": "application/json"}
        res = requests.put(url, headers=headers, data=data)

        return res.content

    def deleteTransfer(self, uid):
        if self.sandbox:
            url = f'http://slickpay-v2.azimutbscenter.com/transfers/{int(uid)}'
        else:
            url = f'http://slickpay-v2.azimutbscenter.com/transfers/{int(uid)}'
        headers = {"Authorization": f'{str(self.public_key)}', "Accept": "application/json"}
        res = requests.delete(url, headers=headers)

        return res.content


class BankAccount:
    def __init__(self, public_key, sandbox):
        self.public_key = public_key
        self.sandbox = sandbox

    def create(self, data):
        if self.sandbox:
            url = 'http://slickpay-v2.azimutbscenter.com/accounts'
        else:
            url = 'http://slickpay-v2.azimutbscenter.com/accounts'
        headers = {"Authorization": f'{str(self.public_key)}', "Accept": "application/json"}
        res = requests.post(url, headers=headers, data=data)
        body = res.json()
        return body

    def update(self, uuid, data):
        if self.sandbox:
            url = f'http://slickpay-v2.azimutbscenter.com/accounts/{str(uuid)}'
        else:
            url = f'http://slickpay-v2.azimutbscenter.com/accounts/{str(uuid)}'
        headers = {"Authorization": 'Bearer 5|6itxL9D8tf1Fw2vnfcxyTdvmayD9er3mFZv3LzHF', "Accept": "application/json"}

        res = requests.put(url, headers=headers, data=data)

        return res.content

    def list(self, offset):
        if self.sandbox:
            url = f'http://slickpay-v2.azimutbscenter.com/accounts?offset={int(offset)}'
        else:
            url = f'http://slickpay-v2.azimutbscenter.com/accounts?offset={int(offset)}'
        headers = {"Authorization": f'{str(self.public_key)}', "Accept": "application/json"}
        res = requests.get(url, headers=headers)

        return res.content

    def accountDetails(self, offset):
        if self.sandbox:
            url = f'http://slickpay-v2.azimutbscenter.com/accounts/{int(offset)}'
        else:
            url = f'http://slickpay-v2.azimutbscenter.com/accounts/{int(offset)}'
        headers = {"Authorization": f'Bearer {str(self.public_key)}', "Accept": "application/json"}
        res = requests.get(url, headers=headers)

        return res.content

    def deleteAccount(self, uid):
        if self.sandbox:
            url = f'http://slickpay-v2.azimutbscenter.com/accounts/{int(uid)}'
        else:
            url = f'http://slickpay-v2.azimutbscenter.com/accounts/{int(uid)}'
        headers = {"Authorization": f'{str(self.public_key)}', "Accept": "application/json"}
        res = requests.delete(url, headers=headers)

        return res.content


class Receiver:
    def __init__(self, public_key, sandbox):
        self.public_key = public_key
        self. sandbox = sandbox

    def create(self, data):
        if self.sandbox:
            url = 'https://dev.transfer.slick-pay.com/api/user/receiver'
        else:
            url = 'https://transfer.slick-pay.com/api/user/receiver'
        headers = {"Authorization": f'{str(self.public_key)}', "Accept": "application/json"}
        res = requests.post(url, headers=headers, data=data)
        body = res.json()
        return body

    def update(self, uuid, data):
        if self.sandbox:
            url = f'https://dev.transfer.slick-pay.com/api/user/receiver/{str(uuid)}'
        else:
            url = f'https://transfer.slick-pay.com/api/user/receiver/{str(uuid)}'
        headers = {"Authorization": 'Bearer 5|6itxL9D8tf1Fw2vnfcxyTdvmayD9er3mFZv3LzHF', "Accept": "application/json"}

        res = requests.post(url, headers=headers, data=data)

        return res.content

    def list(self, offset):
        if self.sandbox:
            url = f'https://dev.transfer.slick-pay.com/api/user/receiver?offset={int(offset)}'
        else:
            url = f'https://transfer.slick-pay.com/api/user/receiver?offset={int(offset)}'
        headers = {"Authorization": f'{str(self.public_key)}', "Accept": "application/json"}
        res = requests.get(url, headers=headers)

        return res.content


class Contact:
    def __init__(self, public_key, sandbox):
        self.public_key = public_key
        self.sandbox = sandbox

    def createContact(self, data):
        if self.sandbox:
            url = 'http://slickpay-v2.azimutbscenter.com/contacts'
        else:
            url = 'http://slickpay-v2.azimutbscenter.com/contacts'
        headers = {"Authorization": f'{str(self.public_key)}', "Accept": "application/json"}
        res = requests.post(url, headers=headers, data=data)
        body = res.json()
        return body

    def contactDetail(self, uid):
        if self.sandbox:
            url = f'http://slickpay-v2.azimutbscenter.com/contacts/{int(uid)}'
        else:
            url = f'http://slickpay-v2.azimutbscenter.com/contacts/{int(uid)}'
        headers = {"Authorization": f'{str(self.public_key)}', "Accept": "application/json"}
        res = requests.get(url, headers=headers)

        return res.content

    def listContact(self, offset, page):
        if self.sandbox:
            url = f'http://slickpay-v2.azimutbscenter.com/contacts?offset={int(offset)}&page={int(page)}'
        else:
            url = f'http://slickpay-v2.azimutbscenter.com/contacts?offset={int(offset)}&page={int(page)}'
        headers = {"Authorization": f'{str(self.public_key)}', "Accept": "application/json"}
        res = requests.get(url, headers=headers)

        return res.content

    def updateContact(self, data, uid):
        if self.sandbox:
            url = f'http://slickpay-v2.azimutbscenter.com/contacts/{int(uid)}'
        else:
            url = f'http://slickpay-v2.azimutbscenter.com/contacts/{int(uid)}'
        headers = {"Authorization": f'{str(self.public_key)}', "Accept": "application/json"}
        res = requests.put(url, headers=headers, data=data)

        return res.content

    def deleteContact(self, uid):
        if self.sandbox:
            url = f'http://slickpay-v2.azimutbscenter.com/contacts/{int(uid)}'
        else:
            url = f'http://slickpay-v2.azimutbscenter.com/contacts/{int(uid)}'
        headers = {"Authorization": f'{str(self.public_key)}', "Accept": "application/json"}
        res = requests.delete(url, headers=headers)

        return res.content
