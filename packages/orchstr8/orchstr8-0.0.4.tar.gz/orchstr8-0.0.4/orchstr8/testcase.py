import asyncio
from twisted.trial import unittest
from twisted.internet import utils, defer
from twisted.internet.utils import runWithWarningsSuppressed as originalRunWith
from orchstr8.conductor import FullStack
from torba.basemanager import BaseWalletManager


def d2f(deferred):
    return deferred.asFuture(asyncio.get_event_loop())


class IntegrationTestCase(unittest.TestCase):

    VERBOSE = False
    WALLET_MANAGER = BaseWalletManager

    async def setUp(self):
        self.stack = FullStack(self.WALLET_MANAGER, verbose=self.VERBOSE)
        await self.stack.start()
        self.blockchain = self.stack.blockchain
        ws = self.stack.wallet
        self.manager = ws.manager
        self.ledger = ws.ledger
        self.wallet = ws.wallet
        self.account = ws.manager.default_account

    async def tearDown(self):
        await self.stack.stop()

    def broadcast(self, tx):
        return d2f(self.ledger.broadcast(tx))

    def get_balance(self, account=None, confirmations=0):
        if account is None:
            return d2f(self.manager.get_balance(confirmations=confirmations))
        else:
            return d2f(account.get_balance(confirmations=confirmations))

    async def on_header(self, height):
        if self.ledger.headers.height < height:
            await self.ledger.on_header.where(
                lambda e: e.height == height
            )
        return True

    async def on_transaction_id(self, txid):
        await self.ledger.on_transaction.where(
            lambda e: e.tx.id == txid
        )

    async def on_transaction(self, tx):
        addresses = await d2f(tx.get_my_addresses(self.ledger))
        await d2f(defer.DeferredList([
            self.ledger.on_transaction.deferred_where(lambda e: e.address == address)
            for address in addresses
        ]))


def run_with_async_support(suppress, f, *a, **kw):
    if asyncio.iscoroutinefunction(f):
        def test_method(*args, **kwargs):
            return defer.Deferred.fromFuture(asyncio.ensure_future(f(*args, **kwargs)))
    else:
        test_method = f
    return originalRunWith(suppress, test_method, *a, **kw)


utils.runWithWarningsSuppressed = run_with_async_support
