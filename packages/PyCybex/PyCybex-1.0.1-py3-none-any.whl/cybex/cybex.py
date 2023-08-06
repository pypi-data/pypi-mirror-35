from . import intercept_bitshares
from bitshares.bitshares import BitShares
from bitshares.account import Account
from bitshares.amount import Amount
from bitshares.storage import configStorage as config
from bitsharesbase import operations
from bitsharesbase.chains import known_chains
from graphenebase.base58 import known_prefixes
from graphenebase.types import Set
from . import asset
from . import cybex_operations
from . import gateway

import bitsharesbase.objects as bsobjects
bsobjects.operations = intercept_bitshares.cybex_operations

def cybex_debug_config(chain_id):
    debug_chain = {
        'chain_id': chain_id,
        'core_symbol': 'CYB',
        'prefix': 'CYB'
    }
    known_chains['CYB'] = debug_chain 

CYBEX_PROD_CHAIN = {
    'chain_id': '90be01e82b981c8f201c9a78a3d31f655743b29ff3274727b1439b093d04aa23',
    'core_symbol': 'CYB',
    'prefix': 'CYB'
}

class Cybex(BitShares):
    def __init__(self, node="", rpcuser="", rpcpassword="", 
                debug=False, **kwargs):

        if 'CYB' not in known_chains: # else we must have set a debug chain id
            known_chains['CYB'] = CYBEX_PROD_CHAIN

        known_prefixes.append('CYB')
        config['prefix'] = 'CYB'
        config.config_defaults["node"] = node

        super(Cybex, self).__init__(node=node, rpcuser=rpcuser,
                 rpcpassword=rpcpassword, debug=debug, **kwargs)

    def transfer(self, to, amount, asset, memo="", account=None, **kwargs):
        """ Transfer an asset to another account.

            :param str to: Recipient
            :param float amount: Amount to transfer
            :param str asset: Asset to transfer
            :param str memo: (optional) Memo, may begin with `#` for encrypted
                messaging
            :param str account: (optional) the source account for the transfer
                if not ``default_account``
        """
        from bitshares.memo import Memo
        if not account:
            if "default_account" in config:
                account = config["default_account"]
        if not account:
            raise ValueError("You need to provide an account")

        account = Account(account, bitshares_instance=self)
        amount = Amount(amount, asset, bitshares_instance=self)
        to = Account(to, bitshares_instance=self)

        memoObj = Memo(
            from_account=account,
            to_account=to,
            bitshares_instance=self
        )

        op = cybex_operations.Transfer(**{
            "fee": {"amount": 0, "asset_id": "1.3.0"},
            "from": account["id"],
            "to": to["id"],
            "amount": {
                "amount": int(amount),
                "asset_id": amount.asset["id"]
            },
            "memo": memoObj.encrypt(memo),
            "extensions": None if 'extensions' not in kwargs else kwargs['extensions'],
            "prefix": self.prefix
        })
        return self.finalizeOp(op, account, "active", **kwargs)

    def withdraw(self, to_addr, amount, asset, account = None, **kwargs):
        """ Withdraw asset to external address.

            :param str to_addr: Recipient address
            :param float amount: Amount to withdraw
            :param str asset: Asset to withdraw
            :param str account: (optional) the source account for the withdraw
                if not ``default_account``
        """
        withdraw_account = "cybex-jadegateway"
        accepted_assets = [
            'JADE.ETH', 'JADE.BTC', 'JADE.LTC', 'JADE.EOS', 'JADE.USDT',
            'JADE.MT',  'JADE.SNT', 'JADE.PAY', 'JADE.GET', 'JADE.MVP',
            'JADE.DPY', 'JADE.MVP', 'JADE.LHT', 'JADE.INK', 'JADE.BAT',
            'JADE.OMG', 'JADE.NAS', 'JADE.KNC', 'JADE.MAD', 'JADE.TCT',
            'JADE.GNT', 'JADE.GNX'
        ]

        if asset not in accepted_assets:
            raise ValueError("Asset {} not supported for withdraw yet".format(asset))

        from bitshares.memo import Memo
        if not account:
            if "default_account" in config:
                account = config["default_account"]
        if not account:
            raise ValueError("You need to provide an account")

        extern_symbol = asset[5:]
        withdraw_info = gateway.get_withdraw_info(extern_symbol)
        assert withdraw_info['asset'] == asset
        if float(amount) < float(withdraw_info['minValue']):
            raise ValueError("Withdraw amount [{}] for {} less than minimum [{}]".format(amount,extern_symbol,float(withdraw_info['minValue'])))

        if not gateway.validate_withdraw_address(extern_symbol, to_addr, account):
            raise ValueError("Invalid withdraw address for asset {}".format(extern_symbol))

        account = Account(account, bitshares_instance = self)
        amount = Amount(amount, asset, bitshares_instance=self)
        to = Account(withdraw_account, bitshares_instance = self)

        if to['id'] != withdraw_info['gatewayAccount']:
            raise ValueError("Invalid gateway account, \
                    please contact author or manually operate on web based wallet")

        memo_str = 'withdraw:CybexGateway:{}:{}'.format(extern_symbol, to_addr)

        from bitshares.memo import Memo
        memoObj = Memo(
            from_account = account,
            to_account = to,
            bitshares_instance = self
        )

        op = cybex_operations.Transfer(**{
            "fee": {"amount": 0, "asset_id": "1.3.0"},
            "from": account["id"],
            "to": to["id"],
            "amount": {
                "amount": int(amount),
                "asset_id": amount.asset["id"]
            },
            "memo": memoObj.encrypt(memo_str),
            "extensions": None,
            "prefix": self.prefix
        })

        return self.finalizeOp(op, account, "active", **kwargs)

    def issue_asset(self, to, amount, asset, memo = "", account = None, **kwargs):
        """ Issue an asset to another account.

            :param str to: Recipient
            :param float amount: Amount to issue
            :param str asset: Asset to issue
            :param str memo: (optional) Memo
            :param str account: (optional) ths source account to issue
        """
        from bitshares.memo import Memo
        if not account:
            if "default_account" in config:
                account = config["default_account"]
        if not account:
            raise ValueError("You need to provide an account")
        account = Account(account, bitshares_instance = self)
        to = Account(to, bitshares_instance = self)
        amount = Amount(amount, asset, bitshares_instance = self)

        memoObj = Memo(
            from_account = account,
            to_account = to,
            bitshares_instance = self
        )

        op = cybex_operations.Asset_issue(**{
            'fee': {"amount": 0, "asset_id": "1.3.0"},
            'issuer': account["id"],
            'issue_to_account': to["id"],
            'asset_to_issue': {
                'amount': int(amount),
                'asset_id': amount.asset["id"],
            },
            'memo': memoObj.encrypt(memo),
            "extensions": None if 'extensions' not in kwargs else kwargs['extensions'],
            "prefix": self.prefix
        })
        return self.finalizeOp(op, account, "active", **kwargs)

    def call_order_update(self, delta_collateral, delta_debt, account=None):
        """ call_order_update 
    
            :param str account: the account to cancel
                to (defaults to default_account)
        """
        if not account:
            if "default_account" in config:
                account = config["default_account"]
        if not account:
            raise ValueError("You need to provide an account")

        account = Account(account)
    
        kwargs = {
            'fee':{"amount": 0, "asset_id": "1.3.0"},
            'funding_account':account["id"],
            'delta_collateral':delta_collateral,
            'delta_debt':delta_debt,
        }
    
        op = operations.Call_order_update(**kwargs)
    
        return self.finalizeOp(op, account, "active")

    def create_asset(self, 
        symbol,
        precision,
        max_supply,
        core_exchange_ratio,
        description = '',
        charge_market_fee = True,
        white_list = True,
        override_authority = True,
        transfer_restricted = True,
        is_prediction_market = False,
        account = None,
        **kwargs):
        """ Create asset.

            :param str symbol: symbol of asset 
            :param int precision: precision of asset
            :param int max_supply: max supply of asset
            :param core_exchange_ratio: dict like {'symbol': 1, 'CYB': 2000}
                    'symbol' and 'CYB' must be in key, value must be int
            :param str description: description of asset
            
            PERMISSION FLAGS FOR ASSET.
            Caution!!! this can not be updated after created.
            :param bool charge_market_fee: set to true if an issuer specific percentage of
                    all market trades in this asset is paid to the issuer
            :param bool white_list: accounts must be white listed to hold this asset
            :param bool override_authority: issuer has permission to transfer from any to any
            :param bool transfer_restricted: issuer should be on part in transfer operation
            END OF PERMISSION FLAGS

            :param bool is_prediction_market
            :param str account: creator of asset
        """

        if (len(core_exchange_ratio) != 2 or 
            symbol not in core_exchange_ratio or
            'CYB' not in core_exchange_ratio):
            raise ValueError("Invalid core exchange ratio")

        if precision < 0 or precision > 12:
            raise ValueError("Invalid precision, not in range [0, 12]")

        if not account:
            if "default_account" in config:
                account = config["default_account"]
        if not account:
            raise ValueError("You need to provide an account")

        account = Account(account, bitshares_instance=self)

        perm = {
            "charge_market_fee": 0x01,
            "white_list": 0x02,
            "override_authority": 0x04,
            "transfer_restricted": 0x08,
            "disable_force_settle": 0x10,
            "global_settle": 0x20,
            "disable_confidential": 0x40,
            "witness_fed_asset": 0x80,
            "committee_fed_asset": 0x100,
        }
        
        permissions = {"charge_market_fee" : charge_market_fee,
                       "white_list" : white_list,
                       "override_authority" : override_authority,
                       "transfer_restricted" : transfer_restricted,
                       "disable_force_settle" : False,
                       "global_settle" : False,
                       "disable_confidential" : True,
                       "witness_fed_asset" : False,
                       "committee_fed_asset" : False,
                       }
        flags       = {"charge_market_fee" : False,
                       "white_list" : False,
                       "override_authority" : False,
                       "transfer_restricted" : False,
                       "disable_force_settle" : False,
                       "global_settle" : False,
                       "disable_confidential" : False,
                       "witness_fed_asset" : False,
                       "committee_fed_asset" : False,
                       }

        permissions_int = sum(
            [perm[p] if v else 0
                for p, v in permissions.items()])

        flags_int = sum(
            [perm[p] if v else 0
                for p, v in flags.items()])
        
        core_asset = asset.Asset('CYB', cybex_instance = self)

        options = {"max_supply" : max_supply * (10 ** precision),
                   "market_fee_percent" : 0,
                   "max_market_fee" : 0,
                   "issuer_permissions" : permissions_int,
                   "flags" : flags_int,
                   "precision" : precision,
                   "core_exchange_rate" : {
                       "base": {
                           "amount": int(core_exchange_ratio['CYB'] * (10 ** core_asset.precision)),
                           "asset_id": core_asset['id']},
                       "quote": {
                           "amount": core_exchange_ratio[symbol] * (10 ** precision),
                           "asset_id": "1.3.1"}},
                   "whitelist_authorities" : [],
                   "blacklist_authorities" : [],
                   "whitelist_markets" : [],
                   "blacklist_markets" : [],
                   "description" : description,
                   "extensions" : [] 
                   }

        if 'common_options' in kwargs:
              common_options=kwargs['common_options']
        else:
              common_options=options
        
        if 'bitasset_options' in kwargs:
              bitasset_options=kwargs['bitasset_options']
        else:
              bitasset_options=None
        
        kwargs = {
                     'fee': {"amount": 0, "asset_id": "1.3.0"},
                     'issuer': account["id"],
                     'symbol': symbol,
                     'precision': precision,
                     'common_options': common_options,
                     'is_prediction_market': is_prediction_market
        }

        if bitasset_options:
             kwargs['bitasset_opts'] = bitasset_options 
        
        op = operations.Asset_create(**kwargs)

        return self.finalizeOp(op, account, "active")

    def balance_claim(self, account, balance_id, balance_owner_key, amount, asset, **kwargs):
        """ Claim balance.

            :param str account: account to deposit the balance
            :param str balance_id: object id of balance object
            :param str balance_owner_key: public key of balance owner
            :param int amount: amount to claim
            :param str asset: asset to claim
        """
        account = Account(account, bitshares_instance = self)
        amount = Amount(amount, asset, bitshares_instance = self)
        op = cybex_operations.Balance_claim(**{
            "fee": {"amount": 0, "asset_id": "1.3.0"},
            "deposit_to_account": account["id"],
            "balance_to_claim": balance_id,
            "balance_owner_key": balance_owner_key,
            "total_claimed": {
                "amount": int(amount),
                "asset_id": amount.asset["id"]
            }
        })
        return self.finalizeOp(op, account, "active", **kwargs)
        
    def cancel_vesting(self, balance_object, sender = None, **kwargs):
        """ cancel vesting balance.

            :param str balance_object_id: balance object id of balance
            :param sender 
        """
        if not sender:
            if "default_account" in config:
                sender = config["default_account"]
        if not sender:
            raise ValueError("You need to provide an account")

        account = Account(sender, bitshares_instance = self)
        op = cybex_operations.Cancel_vesting(**{
            "fee": {"amount": 0, "asset_id": "1.3.0"},
            "payer": account["id"],
            "sender": account["id"],
            "balance_object": balance_object
        })
        return self.finalizeOp(op, account, "active", **kwargs)
