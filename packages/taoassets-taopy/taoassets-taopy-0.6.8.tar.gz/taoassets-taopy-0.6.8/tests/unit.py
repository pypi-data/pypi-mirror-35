# Copyright (C) 2017 chainside srl
# Copyright (C) 2018 Bryce Weiner
#
# This file is part of the taopy package.
#
# It is subject to the license terms in the LICENSE.md file found in the top-level
# directory of this distribution.
#
# No part of taopy, including this file, may be copied, modified,
# propagated, or distributed except according to the terms contained in the
# LICENSE.md file.


import unittest
from random import random
from unittest.mock import patch

from taopy.constants import (
    BitcoinMainnet,
    BitcoinTestnet,
    PeercoinMainnet,
    PeercoinTestnet,
    TaoMainnet,
)
from taopy.structs.crypto import PublicKey, PrivateKey
from taopy.structs.transaction import *
from taopy.structs.script import *
from taopy.structs.block import *
from taopy.structs.sig import *
from taopy.structs.address import Address, SegWitAddress, P2shAddress, ClassicAddress
from taopy.lib.codecs import CouldNotDecode
from taopy.structs.hd import *
from taopy.lib.base58 import (
    b58decode,
    b58decode_check,
    b58encode,
    b58encode_check,
)
from taopy.lib.parsing import IncompleteParsingException


def get_data(filename):
    import os
    import json
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open('{}/data/{}.json'.format(dir_path, filename)) as infile:
        return json.load(infile)


locktime_dates = get_data('locktime_dates')
locktime_ordering = get_data('locktime_ordering')
sequence_ordering = get_data('sequence_ordering')
transactions = get_data('rawtxs')
json_txs = get_data('tx_json')
scripts = get_data('scripts')
unknownscripts = get_data('unknownscripts')
keys = get_data('xkeys')
segwit_valid_addresses = get_data('segwit_addr_valid')
segwit_invalid_addresses = get_data('segwit_addr_invalid')
valid_blocks = get_data('valid_blocks')
invalid_blocks = get_data('invalid_blocks')
short_blocks = get_data('short_blocks')
hd_keys = get_data('hd')
addresses = get_data('addr')
malleated_txs = get_data('malleated')
privk = get_data('priv_addr_path')
segsig = get_data('segwitsig')
p2sh = get_data('p2sh')
priv_pub_hash_addr_p2pkh_segwit = get_data('priv_pub_hash_addr_p2pkh_segwit')
b58 = get_data('base58')
b58chk = get_data('base58_check')
segwit_hashes = get_data('segwit_hashes')
wif = get_data('wif')
p2wpkh_over_p2sh = get_data("p2wpkh_over_p2sh")
p2wsh_over_p2sh = get_data("p2wsh_over_p2sh")
serialization_data = get_data('stack_data/serialization')
sequence_numbers = get_data('sequence')
sequence_times = get_data('sequence_time')


class TestB58(unittest.TestCase):

    def test_b58encode(self):
        for hexa, encoded in b58:
            self.assertEqual(b58encode(unhexlify(hexa)), encoded)

    def test_b58encode_check(self):
        for hexa, encoded in b58chk:
            self.assertEqual(b58encode_check(unhexlify(hexa)), encoded)

    def test_b58decode(self):
        for hexa, encoded in b58:
            self.assertEqual(hexlify(b58decode(encoded)).decode(), hexa)

    def test_b58decode_check(self):
        for hexa, encoded in b58chk:
            self.assertEqual(hexlify(b58decode_check(encoded)).decode(), hexa)


class TestSegwitHashes(unittest.TestCase):

    def test_hashes(self):
        for tx in segwit_hashes:
            parsed = TransactionFactory.unhexlify(tx['tx'])
            self.assertEqual(parsed.txid, tx['txid'])
            self.assertEqual(parsed.hash(), tx['hash'])


class TestUnknownScript(unittest.TestCase):

    def test(self):
        for script in unknownscripts:
            result = ScriptBuilder.identify(unhexlify(script['hex']))
            self.assertTrue(isinstance(result, UnknownScript))
            self.assertEqual(result.hexlify(), script['hex'])
            self.assertEqual(str(result), script['asm'])


class TestPrivPubHashAddrP2pkhSegwit(unittest.TestCase):

    def test(self):
        for data in priv_pub_hash_addr_p2pkh_segwit:
            try:
                net = BitcoinMainnet
                priv = PrivateKey.from_wif(net, data['privkey'])
            except ValueError:
                net = BitcoinTestnet
                priv = PrivateKey.from_wif(net, data['privkey'])

            pub = PublicKey.unhexlify(data['pubkey'])
            pubhash = bytearray(unhexlify(data['pubkeyhash']))
            address = Address.from_string(net, data['address'])
            p2pkhhex = data['scriptpubkey']
            segwit_addr = data['segwit']

            self.assertEqual(priv.pub(), pub)
            self.assertEqual(pub.hash(), pubhash)
            self.assertEqual(address.hash, pubhash)
            self.assertEqual(P2pkhScript(pub).hexlify(), p2pkhhex)
            self.assertEqual(P2pkhScript(address).hexlify(), p2pkhhex)
            self.assertEqual(P2pkhScript(pubhash).hexlify(), p2pkhhex)
            self.assertEqual(str(P2shScript(P2wpkhV0Script(pub)).address(net)), segwit_addr)
            self.assertEqual(str(P2shScript(P2wpkhV0Script(pubhash)).address(net)), segwit_addr)
            self.assertEqual(P2shScript(P2wpkhV0Script(pub)).scripthash, Address.from_string(net, segwit_addr).hash)
            self.assertEqual(P2shScript(P2wpkhV0Script(pubhash)).scripthash, Address.from_string(net, segwit_addr).hash)


class TestNormalizedId(unittest.TestCase):

    def test(self):
        for tx1, tx2 in malleated_txs:
            tx1 = TransactionFactory.unhexlify(tx1)
            tx2 = TransactionFactory.unhexlify(tx2)
            self.assertNotEqual(tx1.txid, tx2.txid)
            self.assertEqual(tx1.normalized_id, tx2.normalized_id)


class TestHD(unittest.TestCase):

    def test_hd(self):
        masterpriv = None
        for data in hd_keys:
            priv = ExtendedKey.decode(BitcoinMainnet, data['prv'])
            pub = ExtendedKey.decode(BitcoinMainnet, data['pub'])
            if data['path'] == 'm':
                masterpriv = priv
            self.assertEqual(priv.pub().encode(BitcoinMainnet), pub.encode(BitcoinMainnet))
            self.assertEqual(priv.encode(BitcoinMainnet), data['prv'])
            self.assertEqual(pub.encode(BitcoinMainnet), data['pub'])
            derived = masterpriv.derive(data['path'])
            self.assertEqual(derived.encode(BitcoinMainnet), data['prv'])
            self.assertEqual(derived.pub().encode(BitcoinMainnet), data['pub'])

    def test_priv_pub(self):
        masterpub = ExtendedPublicKey.decode(BitcoinMainnet, hd_keys[0]['pub'])
        masterpriv = ExtendedPublicKey.decode(BitcoinMainnet, hd_keys[0]['prv'])
        pubs = [masterpub]
        privs = [masterpriv]
        paths = ['m/0/1/2147483646/2',
                 './2147483646/0',
                 './0/2147483647/1/2147483646/2',
                 './156131385/44645489/4865448/4896853']
        for path in paths:
            newpubs = []
            newprivs = []
            for pub, priv in zip(pubs, privs):
                newpubs.append(pub.derive(path))
                newprivs.append(priv.derive(path))
                self.assertEqual(newpubs[-1], newprivs[-1].pub())
            pubs += newpubs
            privs += newprivs


class TestBlock(unittest.TestCase):
    def test_block_deserialize_serialize(self):
        for i in range(len(valid_blocks)):
            unhex_block = Block.unhexlify(valid_blocks[i]['raw'])
            serial_block = unhex_block.serialize()
            self.assertEqual(valid_blocks[i]['raw'], hexlify(serial_block).decode())

    def test_block_hash(self):
        for i in range(len(valid_blocks)):
            unhex_block = Block.unhexlify(valid_blocks[i]['raw'])
            self.assertEqual(valid_blocks[i]['hash'], unhex_block.hash())

    def test_block_header(self):
        for i in range(len(valid_blocks)):
            unhex_block = Block.unhexlify(valid_blocks[i]['raw'])
            unhex_header = BlockHeader.unhexlify(valid_blocks[i]['raw'])
            self.assertEqual(hexlify(unhex_block.header.serialize()), hexlify(unhex_header.serialize()))

    def test_fail_block_deserialize_serialize(self):
        for i in range(len(valid_blocks)):
            unhex_block = Block.unhexlify(invalid_blocks[i]['raw'])
            serial_block = unhex_block.serialize()
            self.assertNotEqual(valid_blocks[i]['raw'], hexlify(serial_block).decode())

    def test_fail_block_hash(self):
        for i in range(len(valid_blocks)):
            unhex_block = Block.unhexlify(invalid_blocks[i]['raw'])
            self.assertNotEqual(valid_blocks[i]['hash'], unhex_block.hash())

    def test_fail_block_header(self):
        for i in range(len(valid_blocks)):
            unhex_block = Block.unhexlify(valid_blocks[i]['raw'])
            unhex_header = BlockHeader.unhexlify(invalid_blocks[i]['raw'])
            self.assertNotEqual(hexlify(unhex_block.header.serialize()), hexlify(unhex_header.serialize()))

    def test_stop_iteration(self):
        for i in range(len(short_blocks)):
            with self.assertRaises(StopIteration):
                Block.unhexlify(short_blocks[i]['raw'])
            with self.assertRaises(StopIteration):
                Block.unhexlify(short_blocks[i]['raw']).serialize()

    def test_empty_deserialized_string(self):
        for i in range(len(valid_blocks)):
            parser = BlockParser(bytearray(unhexlify(valid_blocks[i]['raw'])), TransactionParser, BitcoinMainnet)
            parser.get_block_header()
            parser.get_txns()
            with self.assertRaises(StopIteration):
                parser >> 1

    def test_incomplete_parsing_exception(self):
        for i in range(len(valid_blocks)):
            aug_raw = valid_blocks[i]['raw'] + "ff"
            with self.assertRaises(IncompleteParsingException):
                Block.unhexlify(aug_raw)


class TestTransaction(unittest.TestCase):

    def test_serialization(self):
        for data in transactions:
            tx = TransactionFactory.unhexlify(data['raw'])
            computed = tx.hexlify()
            original = data['raw']
            self.assertEqual(computed, original)

    def test_jsonization(self):
        for data in transactions:
            tx = TransactionFactory.unhexlify(data['raw'])
            self.assertEqual(TransactionFactory.from_json(tx.to_json()).to_json(), tx.to_json())

        for tx in json_txs:
            self.assertEqual(TransactionFactory.from_json(tx), TransactionFactory.unhexlify(tx['hex']))
            self.assertEqual(TransactionFactory.unhexlify(tx['hex']).to_json(), tx)

    def test_txid(self):
        for data in transactions:
            self.assertEqual(TransactionFactory.unhexlify(data['raw']).txid, data['txid'])

    def test_script(self):
        for key, value in scripts.items():
            self.assertEqual(eval(value['code']).hexlify(), value['hex'])
            self.assertEqual(str(eval(value['code'])), value['asm'])
            parsed_script = Script.unhexlify(value['hex'])
            self.assertEqual(parsed_script.hexlify(), value['hex'])
            self.assertEqual(str(parsed_script), value['asm'])
            parsed_script = ScriptBuilder.identify(value['hex'])
            self.assertEqual(parsed_script.hexlify(), value['hex'])
            self.assertEqual(str(parsed_script), value['asm'])
            self.assertEqual(parsed_script.type, value['type'])

    # Fails on the last transaction for some reason :\
    def test_json(self):
        for data in transactions:
            tx = Transaction.unhexlify(data["raw"])
            tx_json = tx.to_json()
            tx_from_json = Transaction.from_json(tx_json)
            self.assertEqual(tx, tx_from_json)


class TestSegWitAddress(unittest.TestCase):

    def test_valid(self):
        for data in segwit_valid_addresses:
            try:
                net = BitcoinMainnet
                address = SegWitAddress.from_string(net, data['address'])
            except CouldNotDecode:
                net = BitcoinTestnet
                address = SegWitAddress.from_string(net, data['address'])

            script = ScriptBuilder.identify(data['script'])
            self.assertEqual(address.hash, script.address(net).hash)
            if len(data['script']) == 44:
                self.assertEqual(P2wpkhV0Script(address), script)
            elif len(data['script']) == 68:
                self.assertEqual(P2wshV0Script(address), script)

    def test_invalid(self):
        for address in segwit_invalid_addresses:
            with self.assertRaises(CouldNotDecode):
                print(SegWitAddress.decode(address, strict=False))


class TestSegwitOverP2sh(unittest.TestCase):

    def test_p2wpkh_over_p2sh(self):
        for spend in p2wpkh_over_p2sh:
            pubkey = PublicKey.unhexlify(spend['pubkey'])
            self.assertEqual(str(P2shAddress.from_script(BitcoinMainnet, P2wpkhScript.get(spend['witness_version'])(pubkey),)), spend['address'])
            self.assertEqual(P2wpkhScript.get(spend['witness_version'])(pubkey).hexlify(), spend['redeem_script'])
            self.assertEqual(str(P2shScript(P2wpkhScript.get(spend['witness_version'])(pubkey))), spend['script_pubkey'])

    def test_p2wsh_over_p2sh(self):
        for spend in p2wsh_over_p2sh:
            wit_script = ScriptBuilder.identify(spend['witness_script'])
            self.assertEqual(str(P2shScript(P2wshScript.get(spend['witness_version'])(wit_script))), spend['script_pubkey'])
            self.assertEqual(P2wshScript.get(spend['witness_version'])(wit_script).hexlify(), spend['redeem_script'])
            self.assertEqual(str(P2shAddress.from_script(BitcoinMainnet, P2wshScript.get(spend['witness_version'])(wit_script))), spend['address'])


class TestReplace(unittest.TestCase):

    def test_success(self):
        from random import randint
        for transaction in transactions:
            tx = TransactionFactory.unhexlify(transaction['raw'], mutable=True)
            self.assertEqual(tx.is_replaceable(), transaction['replaceable'])
            if len(tx.ins) > 2 and not transaction['replaceable']:
                tx.ins[1].sequence = Sequence(randint(0, 0xfffffffe))
                self.assertTrue(tx.ins[1].is_replaceable())
                self.assertFalse(tx.ins[2].is_replaceable())
                self.assertTrue(tx.is_replaceable())


class TestStackData(unittest.TestCase):

    @staticmethod
    def get_test_data():
        from os import walk
        files = next(walk('./stack_data/data/rand_data'))[2]
        for file in files:
            with open('stack_data/data/rand_data/'+file, 'rb') as infile:
                yield bytearray(infile.read())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fail_sizes = [2**32 + 1]

    def test_success(self):
        stored_data = TestStackData.get_test_data()
        for data in stored_data:
            stack = StackData.from_bytes(data)
            push_op = stack.to_push_op()
            if len(data) == 1 and 0 <= data[0] <= 16:
                self.assertTrue(len(push_op) == len(data))
            elif 1 <= len(data) <= 75:
                self.assertTrue(len(push_op) == len(data) + 1)
                self.assertTrue(push_op[0] == len(data))
            elif 76 <= len(data) <= 255:
                self.assertTrue(len(push_op) == len(data) + 2)
                self.assertTrue(push_op[0] == 76)
                self.assertTrue(push_op[1] == len(data))
            elif 256 <= len(data) <= 2**16 - 1:
                self.assertTrue(len(push_op) == len(data) + 3)
                self.assertTrue(push_op[0] == 77)
                self.assertTrue(int.from_bytes(push_op[1:3], 'little') == len(data))
            elif 65536 <= len(data) <= 2**32 - 1:
                self.assertTrue(len(push_op) == len(data) + 5)
                self.assertTrue(push_op[0] == 78)
                self.assertTrue(int.from_bytes(push_op[1:5], 'little') == len(data))

    def test_basic(self):
        for item in serialization_data:
            if 'int' in item:
                data = StackData.from_int(item['int'])
            else:
                push_op, data = item['data']
                data = StackData(push_op, unhexlify(data))
            self.assertEqual(Witness([data]).hexlify(), item['hex'])

    def test_failure(self):
        for size in self.fail_sizes:
            with patch('taopy.structs.script.len', return_value=size, create=True):
                with self.assertRaises(WrongPushDataOp):
                    StackData(bytearray([0]))

    def test_int_conversion(self):
        import os
        path = os.path.realpath(__file__).rsplit('/', 1)[0]
        with open('{}/data/stack_data/rand_ints'.format(path)) as infile:
            ints = [int(x) for x in infile.read().split()]
        ints = list(range(1001)) + ints
        for x in ints:
            self.assertTrue(int(StackData.from_int(x)) == x)


class TestKeys(unittest.TestCase):

    def test_priv_to_pubhash(self):
        for priv, addr, _ in privk['derivations']:     
            self.assertEqual(str(PrivateKey.from_wif(BitcoinTestnet, priv).pub().to_address(BitcoinTestnet)), addr)
            self.assertEqual(PrivateKey.from_wif(BitcoinTestnet, priv).pub().hash(),
                             Address.from_string(BitcoinTestnet, addr).hash)

    def test_derivation(self):
        m = ExtendedPrivateKey.decode(BitcoinTestnet, privk['master'])
        for priv, _, path in privk['derivations']:
            self.assertEqual(m.derive(path).key, PrivateKey.from_wif(BitcoinTestnet, priv))

    def test_to_wif(self):
        for w in wif:
            try:
                net = BitcoinMainnet
                self.assertEqual(PrivateKey.from_wif(net, w['wif']).hexlify(), w['hex'])
            except:
                net = BitcoinTestnet
                self.assertEqual(PrivateKey.from_wif(net, w['wif']).hexlify(), w['hex'])

            priv = PrivateKey.unhexlify(w['hex'])
            if not w['compressed']:
                priv.public_compressed = False
            self.assertEqual(priv.to_wif(net), w['wif'])


class TestPubkey(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.compressed = '03fe43d0c2c3daab30f9472beb5b767be020b81c7cc940ed7a7e910f0c1d9feef1'
        self.uncompressed = ('04fe43d0c2c3daab30f9472beb5b767be020b81c7cc940ed7a7e910f0c1d9feef10fe85eb3ce193405c2dd845'
                             '3b7aeb6c1752361efdbf4f52ea8bf8f304aab37ab')
        self.address = '1KKKK6N21XKo48zWKuQKXdvSsCf95ibHFa'

    def test_compression(self):
        pubk = PublicKey.unhexlify(self.uncompressed)
        self.assertTrue(hexlify(pubk.compressed).decode() == self.compressed)

    def test_uncompression(self):
        pubk = PublicKey.unhexlify(self.compressed)
        self.assertTrue(hexlify(pubk.uncompressed).decode() == self.uncompressed)

    def test_address_generation(self):
        pubk = PublicKey.unhexlify(self.uncompressed)
        self.assertTrue(str(pubk.to_address(BitcoinMainnet)) == self.address)


class TestPrivKey(unittest.TestCase):

    def setUp(self):
        from ecdsa import SigningKey, SECP256k1

        self.mainnet_privs = []
        self.testnet_privs = []
        self.mainnet_vers = []
        self.testne_vers = []

        for k in keys:
            try:
                self.mainnet_privs.append(ExtendedPrivateKey.decode(BitcoinMainnet, k[1]).key)
            except ValueError:
                self.testnet_privs.append(ExtendedPrivateKey.decode(BitcoinTestnet, k[1]).key)

        self.mainnet_vers = [SigningKey.from_string(p.key, curve=SECP256k1).get_verifying_key() for p in self.mainnet_privs]

        self.testnet_vers = [SigningKey.from_string(p.key, curve=SECP256k1).get_verifying_key() for p in self.testnet_privs]

    def test_raw_sig_success(self):
        from os import urandom
        for _ in range(10):

            for ver, priv in zip(self.mainnet_vers, self.mainnet_privs):
                digest = bytearray(urandom(32))
                r, s, order = priv.raw_sign(digest)
                self.assertTrue(s in range(1, PrivateKey.highest_s))
                self.assertTrue(ver.verify_digest((r, s), digest, sigdecode=lambda sig, _: (sig[0], sig[1])))

            for ver, priv in zip(self.testnet_vers, self.testnet_privs):
                digest = bytearray(urandom(32))
                r, s, order = priv.raw_sign(digest)
                self.assertTrue(s in range(1, PrivateKey.highest_s))
                self.assertTrue(ver.verify_digest((r, s), digest, sigdecode=lambda sig, _: (sig[0], sig[1])))

    def test_der_sig_success(self):
        from os import urandom
        import struct

        for _ in range(10):

            for priv in self.mainnet_privs:
                digest = bytearray(urandom(32))
                sig = priv.sign(digest)
                length_r = sig[3]
                length_s = sig[5 + length_r]
                s = int.from_bytes(bytearray(struct.unpack(str(length_s) + 'B', sig[6 + length_r:6 + length_r + length_s])), 'big')
                self.assertTrue(s in range(1, PrivateKey.highest_s))

            for priv in self.testnet_privs:
                digest = bytearray(urandom(32))
                sig = priv.sign(digest)
                length_r = sig[3]
                length_s = sig[5 + length_r]
                s = int.from_bytes(bytearray(struct.unpack(str(length_s) + 'B', sig[6 + length_r:6 + length_r + length_s])), 'big')
                self.assertTrue(s in range(1, PrivateKey.highest_s))


    def test_derivation_success(self):
        for pub, priv in keys:
            try:
                net = BitcoinMainnet
                pu = ExtendedPublicKey.decode(net, pub).key
            except ValueError:
                net = BitcoinTestnet
                pu = ExtendedPublicKey.decode(net, pub).key

            pr = ExtendedPrivateKey.decode(net, priv).key
            self.assertTrue(pr.pub() == pu)
            self.assertTrue(pr.pub().hexlify() == pu.hexlify())


class TestP2pk(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pubk = '0384478d41e71dc6c3f9edde0f928a47d1b724c05984ebfb4e7d0422e80abe95ff'

    def test_success(self):
        script = P2pkScript(PublicKey.unhexlify(self.pubk))
        self.assertTrue(script.decompile() == '{} OP_CHECKSIG'.format(self.pubk))
        self.assertTrue(script.hexlify() == '21{}ac'.format(self.pubk))

    def test_matching_fail_leftover(self):
        with self.assertRaises(WrongScriptTypeException):
            P2pkScript.unhexlify('21{}acac'.format(self.pubk))

    def test_matching_fail_long_push(self):
        with self.assertRaises(WrongScriptTypeException):
            P2pkScript.unhexlify('22{}11ac'.format(self.pubk))

    def test_matching_fail_short_push(self):
        with self.assertRaises(WrongScriptTypeException):
            P2pkScript.unhexlify('20{}ac'.format(self.pubk[:-2]))

    def test_matching_fail_wrong_op(self):
        with self.assertRaises(WrongScriptTypeException):
            P2pkScript.unhexlify('21{}ad'.format(self.pubk))


class TestP2pkh(unittest.TestCase):

    def setUp(self):
        self.pubk = PublicKey.unhexlify('0384478d41e71dc6c3f9edde0f928a47d1b724c05984ebfb4e7d0422e80abe95ff')
        self.pubkh = self.pubk.hash()
        self.address = Address.from_string(BitcoinTestnet, 'mquvJWnJJwTDUcdneQkUbrfN2wm9uiXd1p')

    def test_success_pubk(self):
        script = P2pkhScript(self.pubk)
        self.assertTrue(script.decompile() ==
                        'OP_DUP OP_HASH160 {} OP_EQUALVERIFY OP_CHECKSIG'.format(hexlify(self.pubkh).decode()))
        self.assertTrue(script.hexlify() == '76a914{}88ac'.format(hexlify(self.pubkh).decode()))

    def test_success_hash(self):
        script = P2pkhScript(self.pubkh)
        self.assertTrue(script.decompile() ==
                        'OP_DUP OP_HASH160 {} OP_EQUALVERIFY OP_CHECKSIG'.format(hexlify(self.pubkh).decode()))
        self.assertTrue(script.hexlify() == '76a914{}88ac'.format(hexlify(self.pubkh).decode()))

    def test_success_address(self):
        script = P2pkhScript(self.address)
        self.assertTrue(script.decompile() ==
                        'OP_DUP OP_HASH160 {} OP_EQUALVERIFY OP_CHECKSIG'.format(hexlify(self.pubkh).decode()))
        self.assertTrue(script.hexlify() == '76a914{}88ac'.format(hexlify(self.pubkh).decode()))

    def test_matching_fail_leftover(self):
        with self.assertRaises(WrongScriptTypeException):
            P2pkScript.unhexlify('76a914{}88acac'.format(hexlify(self.pubkh).decode()))

    def test_matching_fail_long_push(self):
        with self.assertRaises(WrongScriptTypeException):
            P2pkScript.unhexlify('79a915{}1188ac'.format(hexlify(self.pubkh).decode()))

    def test_matching_fail_short_push(self):
        with self.assertRaises(WrongScriptTypeException):
            P2pkScript.unhexlify('79a913{}88ac'.format(hexlify(self.pubkh[:-1]).decode()))

    def test_matching_fail_wrong_op(self):
        with self.assertRaises(WrongScriptTypeException):
            P2pkScript.unhexlify('79a914{}88ad'.format(hexlify(self.pubkh).decode()))


class TestPwpkhScript(unittest.TestCase):

    def setUp(self):
        self.pubk = PublicKey.unhexlify('0384478d41e71dc6c3f9edde0f928a47d1b724c05984ebfb4e7d0422e80abe95ff')
        self.pubkh = self.pubk.hash()

    def test_success_pubk(self):
        script = P2wpkhV0Script(self.pubk)
        self.assertTrue(script.decompile() ==
                        'OP_0 {}'.format(hexlify(self.pubkh).decode()))
        self.assertTrue(script.hexlify() == '0014{}'.format(hexlify(self.pubkh).decode()))

    def test_success_hash(self):
        script = P2wpkhV0Script(self.pubkh)
        self.assertTrue(script.decompile() ==
                        'OP_0 {}'.format(hexlify(self.pubkh).decode()))
        self.assertTrue(script.hexlify() == '0014{}'.format(hexlify(self.pubkh).decode()))

    def test_matching_fail_leftover(self):
        with self.assertRaises(WrongScriptTypeException):
            P2wpkhV0Script.unhexlify('0014{}aa'.format(hexlify(self.pubkh).decode()))

    def test_matching_fail_long_push(self):
        with self.assertRaises(WrongScriptTypeException):
            P2wpkhV0Script.unhexlify('0015{}aa'.format(hexlify(self.pubkh).decode()))

    def test_matching_fail_short_push(self):
        with self.assertRaises(WrongScriptTypeException):
            P2wpkhV0Script.unhexlify('0013{}'.format(hexlify(self.pubkh[:-1]).decode()))

    def test_matching_fail_wrong_op(self):
        with self.assertRaises(WrongScriptTypeException):
            P2wpkhV0Script.unhexlify('0114{}'.format(hexlify(self.pubkh).decode()))


class TestP2sh(unittest.TestCase):

    def setUp(self):
        self.redeem_script = P2pkhScript(PublicKey.unhexlify('0384478d41e71dc6c3f9edde0f928a47d1b724c'
                                                             '05984ebfb4e7d0422e80abe95ff'))
        self.as_data = StackData.from_bytes(self.redeem_script.p2sh_hash())
        self.address = P2shAddress.from_script(BitcoinMainnet, self.redeem_script)

    def test_success_hash(self):
        script = P2shScript(self.redeem_script.p2sh_hash())
        self.assertTrue(script.decompile() ==
                        'OP_HASH160 {} OP_EQUAL'.format(self.as_data))
        self.assertTrue(script.hexlify() == 'a9{:02x}{}87'.format(len(self.as_data), self.as_data))

    def test_success_redeem(self):
        script = P2shScript(self.redeem_script)
        self.assertTrue(script.decompile() ==
                        'OP_HASH160 {} OP_EQUAL'.format(self.as_data))
        self.assertTrue(script.hexlify() == 'a9{:02x}{}87'.format(len(self.as_data), self.as_data))

    def test_success_addresses(self):

        for script_hex, address in p2sh.items():
            script = ScriptBuilder.identify(bytearray(unhexlify(script_hex)))
            try:
                net = BitcoinMainnet
                from_addr = P2shScript(Address.from_string(net, address))
            except CouldNotDecode:
                net = BitcoinTestnet
                from_addr = P2shScript(Address.from_string(net, address))

            from_script = P2shScript(script)
            self.assertTrue(str(from_addr.address(net)) == address)
            self.assertTrue(str(P2shAddress.from_script(net, script)) == address)
            self.assertTrue(str(from_script.address(net)) == address)

        script = P2shScript(self.address)
        self.assertTrue(script.decompile() ==
                        'OP_HASH160 {} OP_EQUAL'.format(self.as_data))
        self.assertTrue(script.hexlify() == 'a9{:02x}{}87'.format(len(self.as_data), self.as_data))

    def test_matching_fail_leftover(self):
        with self.assertRaises(WrongScriptTypeException):
            P2shScript(Script('a9{:02x}{}87ac'.format(len(self.as_data), self.as_data)))

    def test_matching_fail_long_push(self):
        with self.assertRaises(WrongScriptTypeException):
            P2shScript.unhexlify('a9{:02x}{}aa87'.format(len(self.as_data)+1, self.as_data))

    def test_matching_fail_short_push(self):
        with self.assertRaises(WrongScriptTypeException):
            P2shScript.unhexlify('a9{:02x}{}87'.format(len(self.as_data)-1, str(self.as_data)[:-2]))

    def test_matching_fail_wrong_op(self):
        with self.assertRaises(WrongScriptTypeException):
            P2shScript.unhexlify('a9{:02x}{}88'.format(len(self.as_data), self.as_data))


class TestP2wsh(unittest.TestCase):

    def setUp(self):
        self.redeem_script = P2pkhScript(PublicKey.unhexlify('0384478d41e71dc6c3f9edde0f928a47d1b724c'
                                                             '05984ebfb4e7d0422e80abe95ff'))
        self.as_data = StackData.from_bytes(self.redeem_script.p2wsh_hash())

    def test_success_hash(self):
        script = P2wshV0Script(self.redeem_script.p2wsh_hash())
        self.assertTrue(script.decompile() ==
                        'OP_0 {}'.format(self.as_data))
        self.assertTrue(script.hexlify() == '00{:02x}{}'.format(len(self.as_data), self.as_data))

    def test_success_redeem(self):
        script = P2wshV0Script(self.redeem_script)
        self.assertTrue(script.decompile() ==
                        'OP_0 {}'.format(self.as_data))
        self.assertTrue(script.hexlify() == '00{:02x}{}'.format(len(self.as_data), self.as_data))

    def test_matching_fail_leftover(self):
        with self.assertRaises(WrongScriptTypeException):
            P2wshV0Script.unhexlify('00{:02x}{}aa'.format(len(self.as_data), self.as_data))

    def test_matching_fail_long_push(self):
        with self.assertRaises(WrongScriptTypeException):
            P2wshV0Script.unhexlify('00{:02x}{}aa'.format(len(self.as_data) + 1, self.as_data))

    def test_matching_fail_short_push(self):
        with self.assertRaises(WrongScriptTypeException):
            P2wshV0Script.unhexlify('00{:02x}{}'.format(len(self.as_data) - 1, str(self.as_data)[:-2]))

    def test_matching_fail_wrong_op(self):
        with self.assertRaises(WrongScriptTypeException):
            P2wshV0Script.unhexlify('01{:02x}{}'.format(len(self.as_data), self.as_data))


class TestNulldata(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = StackData.unhexlify('c97232cda052b9e9c312af692c310e4061dcf937910a335bdb96865a0fb9469b0622c6fa')

    def test_success(self):
        script = NulldataScript(self.data)
        self.assertTrue(script.decompile() ==
                        'OP_RETURN {}'.format(self.data))
        self.assertTrue(script.hexlify() == '6a{:02x}{}'.format(len(self.data), self.data))

    def test_matching_fail_leftover(self):
        with self.assertRaises(WrongScriptTypeException):
            P2shScript.unhexlify('a9{:02x}{}aa'.format(len(self.data), self.data))

    def test_matching_fail_long_push(self):
        with self.assertRaises(WrongScriptTypeException):
            P2shScript.unhexlify('a9{:02x}{}aa'.format(len(self.data)+1, self.data))

    def test_matching_fail_short_push(self):
        with self.assertRaises(WrongScriptTypeException):
            P2shScript.unhexlify('a9{:02x}{}'.format(len(self.data)-1, str(self.data)[:-2]))

    def test_matching_fail_wrong_op(self):
        with self.assertRaises(WrongScriptTypeException):
            P2shScript.unhexlify('a8{:02x}{}'.format(len(self.data), self.data))


class TestMultisig(unittest.TestCase):

    def setUp(self):
        self.m = 2
        self.pubkeys = [PublicKey.unhexlify("02c08786d63f78bd0a6777ffe9c978cf5899756cfc32bfad09a89e211aeb926242"),
                        PublicKey.unhexlify("033e81519ecf373ea3a5c7e1c051b71a898fb3438c9550e274d980f147eb4d069d"),
                        PublicKey.unhexlify("036d568125a969dc78b963b494fa7ed5f20ee9c2f2fc2c57f86c5df63089f2ed3a")]
        self.n = 3
        self.hex_template = '{:02x}{}{:02x}ae'.format(self.m + 80,
                                                      ''.join('{:02x}{}'.format(len(pk), pk) for pk in self.pubkeys),
                                                      self.n + 80)

    def test_success(self):
        script = MultisigScript(self.m, *(self.pubkeys + [self.n]))
        expected = 'OP_{} {} OP_{} OP_CHECKMULTISIG'.format(self.m, ' '.join(str(pk) for pk in self.pubkeys), self.n)
        self.assertTrue(script.decompile() == expected)
        self.assertTrue(script.hexlify() == self.hex_template)

    def test_matching_fail_leftover(self):
        with self.assertRaises(WrongScriptTypeException):
            MultisigScript.unhexlify(self.hex_template+'aa')

    def test_matching_fail_wrong_op(self):
        with self.assertRaises(WrongScriptTypeException):
            MultisigScript.unhexlify(self.hex_template[:-2]+'aa')


class TestIf(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.inner_script = MultisigScript(2,
                                           PublicKey.unhexlify("02c08786d63f78bd0a6777ffe9c978cf5899756cfc32bfad09a89e2"
                                                               "11aeb926242"),
                                           PublicKey.unhexlify("033e81519ecf373ea3a5c7e1c051b71a898fb3438c9550e274d980f"
                                                               "147eb4d069d"),
                                           PublicKey.unhexlify("036d568125a969dc78b963b494fa7ed5f20ee9c2f2fc2c57f86c5df"
                                                               "63089f2ed3a"),
                                           3)


class TestIfElse(unittest.TestCase):

    def setUp(self):
        self.if_script = MultisigScript(2,
                                        PublicKey.unhexlify("02c08786d63f78bd0a6777ffe9c978cf5899756cfc32bfad09a89e2"
                                                            "11aeb926242"),
                                        PublicKey.unhexlify("033e81519ecf373ea3a5c7e1c051b71a898fb3438c9550e274d980f"
                                                            "147eb4d069d"),
                                        PublicKey.unhexlify("036d568125a969dc78b963b494fa7ed5f20ee9c2f2fc2c57f86c5df"
                                                            "63089f2ed3a"),
                                        3)
        self.else_script = P2shScript(P2pkhScript(PublicKey.unhexlify("02c08786d63f78bd0a6777ffe9c978cf5899756cfc32bf"
                                                                      "ad09a89e211aeb926242")))

    def test_success(self):
        script = IfElseScript(self.if_script, self.else_script)
        self.assertTrue(script.decompile() ==
                        'OP_IF {} OP_ELSE {} OP_ENDIF'.format(self.if_script.decompile(), self.else_script.decompile()))
        self.assertTrue(script.hexlify() == '63{}67{}68'.format(self.if_script.hexlify(), self.else_script.hexlify()))

    def test_matching_fail_leftover(self):
        with self.assertRaises(WrongScriptTypeException):
            IfElseScript.unhexlify('63{}67{}68aa'.format(self.if_script.hexlify(), self.else_script.hexlify()))

    def test_matching_fail_wrong_op(self):
        with self.assertRaises(WrongScriptTypeException):
            IfElseScript.unhexlify('63{}aa{}68'.format(self.if_script.hexlify(), self.else_script.hexlify()))


class TestTimelock(unittest.TestCase):

    def setUp(self):
        self.locktime = 500000
        self.locked_script = P2shScript(P2pkhScript(PublicKey.unhexlify("02c08786d63f78bd0a6777ffe9c978cf5899756cfc32bf"
                                                                        "ad09a89e211aeb926242")))

    def test_success(self):
        script = AbsoluteTimelockScript(Locktime(self.locktime), self.locked_script)
        self.assertTrue(script.decompile() ==
                        '{} OP_CHECKLOCKTIMEVERIFY OP_DROP {}'.format(Locktime(self.locktime).for_script(),
                                                                      self.locked_script.decompile()))
        self.assertTrue(script.hexlify() == '{}b175{}'.format(Locktime(self.locktime).for_script().hexlify(),
                                                              self.locked_script.hexlify()))

    def test_matching_fail_wrong_op(self):
        with self.assertRaises(WrongScriptTypeException):
            AbsoluteTimelockScript.unhexlify('{}b1aa{}'.format(Locktime(self.locktime).for_script().hexlify(),
                                                       self.locked_script.hexlify()))


class TestSequence(unittest.TestCase):

    @staticmethod
    def td_compare(td1, td2):
        """in our case two timedeltas are equal if they differ by no more than 512*2 seconds"""
        return int(td1.total_seconds()) in range(max(int(td2.total_seconds()) - 512, 0),
                                                 int(td2.total_seconds()) + 512 + 1)

    def test_baseclass(self):
        for data in sequence_numbers:
            created = Sequence.create(**data['params'])
            self.assertEqual(created.seq, data['sequence'])
            self.assertEqual(created.n, data['params']['seq'])
            self.assertEqual(not created.is_active(), data['params']['disable'])
            self.assertEqual(created.is_blocks(), data['params']['blocks'])
            self.assertEqual(not created.is_time(), data['params']['blocks'])

    def test_timebased(self):
        for data in sequence_numbers:
            if data['params']['blocks'] or data['params']['disable']:
                with self.assertRaises(ValueError):
                    TimeBasedSequence(data['sequence'])
            else:
                created = TimeBasedSequence.create(data['params']['seq'])
                self.assertTrue(created.is_time())
                self.assertFalse(created.is_blocks())
                self.assertTrue(created.is_active())

    def test_timedeltas(self):
        from datetime import timedelta
        for data in sequence_times:
            td = timedelta(**data['date'])
            seq = TimeBasedSequence.from_timedelta(td)
            self.assertTrue(self.td_compare(seq.to_timedelta(), td))

    def test_heightbased(self):
        for data in sequence_numbers:
            if (not data['params']['blocks']) or data['params']['disable']:
                with self.assertRaises(ValueError):
                    HeightBasedSequence(data['sequence'])
            else:
                created = HeightBasedSequence.create(data['params']['seq'])
                self.assertFalse(created.is_time())
                self.assertTrue(created.is_blocks())
                self.assertTrue(created.is_active())

    def test_lt(self):
        for data in sequence_ordering:
            if data['outcome'] == 'error':
                with self.assertRaisesRegex(ValueError, data['error_regex']):
                    max([Sequence(x) for x in data['data']])
            else:
                self.assertEqual(max([Sequence(x) for x in data['data']]), Sequence(data['outcome']))


class TestLocktime(unittest.TestCase):

    def test_lt(self):
        for data in locktime_ordering:
            if data['outcome'] == 'error':
                with self.assertRaises(ValueError):
                    max([Locktime(x) for x in data['data']])
            else:
                self.assertEqual(max([Locktime(x) for x in data['data']]), Locktime(data['outcome']))

    def test_dates(self):
        from datetime import datetime, timezone
        for data in locktime_dates:
            if data['timestamp'] == 'error':
                with self.assertRaises(ValueError):
                    Locktime.from_datetime(datetime(tzinfo=timezone.utc, **data['data']))
            else:
                self.assertEqual(Locktime.from_datetime(datetime(tzinfo=timezone.utc,
                                                                 **data['data'])).n,
                                 data['timestamp'])


class TestRelativeTimelock(unittest.TestCase):

    def setUp(self):
        self.sequence = 500000
        self.locked_script = P2shScript(P2pkhScript(PublicKey.unhexlify("02c08786d63f78bd0a6777ffe9c978cf5899756cfc32bf"
                                                                        "ad09a89e211aeb926242")))

    def test_success(self):
        script = RelativeTimelockScript(Sequence(self.sequence), self.locked_script, strict=True)
        self.assertTrue(script.decompile() ==
                        '{} OP_CHECKSEQUENCEVERIFY OP_DROP {}'.format(Sequence(self.sequence).for_script(),
                                                                      self.locked_script.decompile()))
        self.assertTrue(script.hexlify() == '{}b275{}'.format(Sequence(self.sequence).for_script().hexlify(),
                                                              self.locked_script.hexlify()))

    def test_matching_fail_wrong_op(self):
        with self.assertRaises(WrongScriptTypeException):
            RelativeTimelockScript.unhexlify('{}b2aa{}'.format(Sequence(self.sequence).for_script().hexlify(),
                                                               self.locked_script.hexlify()))


class TestHashlock(unittest.TestCase):

    def setUp(self):
        self.hash = PublicKey.unhexlify("02c08786d63f78bd0a6777ffe9c978cf5899756cfc32bfad09a89e211aeb926242").hash()
        self.locked_script = P2shScript(P2pkhScript(PublicKey.unhexlify("02c08786d63f78bd0a6777ffe9c978cf5899756cfc32bf"
                                                                        "ad09a89e211aeb926242")))

    def test_success(self):
        script = Hashlock256Script(StackData.from_bytes(self.hash), self.locked_script)
        self.assertTrue(script.decompile() ==
                        'OP_HASH256 {} OP_EQUALVERIFY {}'.format(hexlify(self.hash).decode(),
                                                                 self.locked_script.decompile()))
        self.assertTrue(script.hexlify() == 'aa{:02x}{}88{}'.format(len(self.hash),
                                                                    hexlify(self.hash).decode(),
                                                                    self.locked_script.hexlify()))

    def test_matching_fail_wrong_op(self):
        with self.assertRaises(WrongScriptTypeException):
            Hashlock256Script.unhexlify('{:02x}{}a8aa{}'.format(len(self.hash),
                                                                hexlify(self.hash).decode(),
                                                                self.locked_script.hexlify()))


class TestBitcoinAddress(unittest.TestCase):

    def setUp(self):
        self.good_addresses = {('BitcoinMainnet', P2pkhAddress, '1KKKK6N21XKo48zWKuQKXdvSsCf95ibHFa',
                                b'\xc8\xe9\t\x96\xc7\xc6\x08\x0e\xe0b\x84`\x0chN\xd9\x04\xd1L\\'),
                               ('BitcoinTestnet', P2pkhAddress, 'mtH6FLMQNu2fFQ4mrb7UjEUjTAhUNCMFoi',
                                b'\x8b\xfas]\x98\xabb\x1e\xdbOw\xd7\xb7\xfe\nK\x1f\xfc\xc0$'),
                               ('BitcoinTestnet', P2pkhAddress, 'n3wEvhujG7SDcgeKCXZMrty5QqhQZ7f6jW',
                                b'\xf5\xea\xa2K\x82\xc8\x1f4L\x9a\x16\xa8\xfb\x84t\xe1\x10\xfd\xb1\xc3'),
                               ('BitcoinMainnet', P2shAddress, '3P14159f73E4gFr7JterCCQh9QjiTjiZrG',
                                b'\xe9\xc3\xdd\x0c\x07\xaa\xc7ay\xeb\xc7jlx\xd4\xd6|l\x16\n'),
                               ('BitcoinTestnet', P2shAddress, '2N6JFaB5rMtPwutovP6cirwBVxHuAVaHvMG',
                                b'\x8f,4\xa2<F\xe9\x80\xb7\x9e\x10\x9b\x11\xa2\xc8-9\x92\xeb\x95')}
        self.bad_addresses = {'vioqwV3F4YzpgnfyUukGVMB3Hv83ujehKCiGWyrYyx2Z7hiKQy7SWUV9KgfMdV9J',
                              'bc1a',
                              '3rE3tz',
                              '1KKKK6N21XKo48zWKuuKXdvSsCf95ibHFa'}

    def test_success(self):
        for net, addr_type, address, hashed_data in self.good_addresses:
            if net == 'BitcoinMainnet':
                net = BitcoinMainnet
            else:
                net = BitcoinTestnet

            from_string = Address.from_string(net, address)
            self.assertTrue(address == str(from_string))
            self.assertTrue(from_string.__class__ == addr_type)
            self.assertTrue(from_string.network == net)
            self.assertTrue(from_string.hash == hashed_data)

    def test_fail(self):
        for address in self.bad_addresses:
            with self.assertRaises(ValueError):
                ClassicAddress.decode(address, strict=False)

    def test_conversions(self):
        for address, pkh in addresses:
            self.assertEqual(hexlify(Address.from_string(BitcoinMainnet, address).hash).decode(), pkh)
            self.assertEqual(str(P2pkhScript(bytearray(unhexlify(pkh))).address(BitcoinMainnet)), address)
            self.assertEqual(P2pkhScript(Address.from_string(BitcoinMainnet, address)).pubkeyhash,
                             bytearray(unhexlify(pkh)))
            self.assertEqual(P2pkhAddress(BitcoinMainnet, bytearray(unhexlify(pkh))).hash, bytearray(unhexlify(pkh)))


class TestPeercoinAddress(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.good_addresses = {
            ('PeercoinMainnet', P2pkhAddress, 'PAdonateFczhZuKLkKHozrcyMJW7Y6TKvw',),
            ('PeercoinTestnet', P2pkhAddress, 'mj46gUeZgeD9ufU7Fvz2dWqaX6Nswtbpba',),
            ('PeercoinTestnet', P2pkhAddress, 'n12h8P5LrVXozfhEQEqg8SFUmVKtphBetj',),
            ('PeercoinMainnet', P2shAddress, 'p92W3t7YkKfQEPDb7cG9jQ6iMh7cpKLvwK',),
        }
        self.bad_addresses = {
            'vioqwV3F4YzpgnfyUukGVMB3Hv83ujehKCiGWyrYyx2Z7hiKQy7SWUV9KgfMdV9J',
            'bc1a',
            '3rE3tz',
            '1KKKK6N21XKo48zWKuQKXdvSsCf95ibHFa',
        }

    def test_success(self):
        for net, addr_type, address in self.good_addresses:
            if net == 'PeercoinMainnet':
                net = PeercoinMainnet
            else:
                net = PeercoinTestnet

            from_string = Address.from_string(net, address)
            self.assertTrue(address == str(from_string))
            self.assertTrue(from_string.__class__ == addr_type)
            self.assertTrue(from_string.network == net)

    def test_fail(self):
        for address in self.bad_addresses:
            with self.assertRaises(ValueError):
                Address.from_string(PeercoinMainnet, address)

class TestTaoAddress(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.good_addresses = {
            ('TaoMainnet', P2pkhAddress, 'TxYzV4kL11M2ioAK3wG4dTesqepamWZA5R',),
            ('TaoMainnet', P2shAddress, '2USHRW8UcSAAnHxWnPe4yX2BV5K3dbWss9',),
        }
        self.bad_addresses = {
            'vioqwV3F4YzpgnfyUukGVMB3Hv83ujehKCiGWyrYyx2Z7hiKQy7SWUV9KgfMdV9J',
            'bc1a',
            '3rE3tz',
            '1KKKK6N21XKo48zWKuQKXdvSsCf95ibHFa',
        }

    def test_success(self):
        for net, addr_type, address in self.good_addresses:
            if net == 'TaoMainnet':
                net = TaoMainnet
            #else:
            #    net = TaoTestnet

            from_string = Address.from_string(net, address)
            self.assertTrue(address == str(from_string))
            self.assertTrue(from_string.__class__ == addr_type)
            self.assertTrue(from_string.network == net)

    def test_fail(self):
        for address in self.bad_addresses:
            with self.assertRaises(ValueError):
                Address.from_string(TaoMainnet, address)


class TestPeercoinTx(unittest.TestCase):

    def test_unhexilify(self):
        """Check that we can parse a PeercoinTx from hex encoded bytes. Data from:

        In [1]: import pytaoassets as pa

        In [2]: provider = pa.Explorer(network='tppc')

        In [3]: raw = provider.getrawtransaction('c418f3bded92ebc035cfefc93f54dc8a501702e6ad4e6a26a07aab87f4cfb653')
        """
        raw = '01000000f7ae3b5b01b3a00d828f5a9a8e908fb59353b4a87132a75a6d939c6e9338e3727631a65028010000006c493046022100e3a72a3a9f53eab66186da5354a58a6fb4b4fc96c5836445bce0b3755840653f022100f7013eb0c3bbd901a8e9c4935edefa9765fa5dd2f1f3a276634d248a4e17c59801210207c75090d56b94a9f638b8b9abaa346c053db265f4aa752170b86c32cdec7efbffffffff0260d3e815000000001976a914c8ec65800888c2c4f831826ba7e10603b3692db188ac00e1f505000000001976a914ba96e0c304ad07afb115d7019b9e54db96668f9988ac00000000'
        PeercoinTx.unhexlify(raw, network=PeercoinTestnet)

    def test_to_script(self):
        data = {}
        for addr, pkh in addresses:
            data[addr] = P2pkhScript(bytearray(unhexlify(pkh)))
        for script, addr in p2sh.items():
            data[addr] = P2shScript(ScriptBuilder.identify(script))
        for dic in segwit_valid_addresses:
            data[dic['address']] = ScriptBuilder.identify(dic['script'])

        for addr, script in data.items():
            self.assertTrue(Address.from_string(addr, strict=False).to_script().hexlify(),
                            script.hexlify())

class TestTaoTx(unittest.TestCase):

    def test_unhexilify(self):
        """Check that we can parse a TaoTx from hex encoded bytes. Data from:

        In [1]: import pytaoassets as pa

        In [2]: provider = pa.Explorer(network='xto')

        In [3]: raw = provider.getrawtransaction('c97c6c9d86c88dca65cab42d9718d9e91216f4add3c48777d15b2919ce49c0f7')
        """
        raw = '007400004836c65706036386fede2c6844e5afca7c74952abf710c89c89d5af892e2ec184d403f5b60000000006a4730440220138be8bf8a62a734b63d93a870077974c1d5fea009d7406c873f0c2742858a020220085b337bd83df023638cc31068dd1324d63ab89861a4ac1f496710f23ae5f8370121023fa6ffb62e36a69099fa68ffb844e56d316bade2562cf71b99106f3d8cf6c765ffffffff0e5ab3110d5394ebff3cc563540bbec3293ddce72b77c8c4c71aa96823fcafd8000000006a473044022030bc39e5152b9d8b9b3ace95ea3b366565d7f9ac230c8f9c67dec6ed47de38e002202906562260c1250a6beaaa611867551d92a355e0352b41da2723ffff4925b2f4012102714442af94e019fc100f8ebf5ea2dbc43d4a5a498887de7953171b0fa0d6539cffffffff300045e6b70ec1f24387af29969ff7f1f961001a2b4c8d1e4f824e564302053b000000006a4730440220050393d977088e9f3d82cb0c0adae8ea693fb2c805deae03c257d320558cfb3902202acd81a6f09f00c43c1cac52068826be2cfe048237635b186e8a34c9c778fe650121026b6abfb9616534161823107d454241154265408e302710cadef4bbf9b3ebd565ffffffffc19da9cd8caad94872882f5cc1a632232dcf24d54e8b6338f6d3a7dfba8eeae0000000006a47304402200f0bad8fd3225565ca6a354fb3cf45a459f2a7a6673b20d7aeeffb1bf4d2ba0e022023051b084b6385eb3d805fba662e43fb71dc52593df9c2c26b5b571f17b331e8012102a56c6759511ea3eff552790310a34b34ddffb4c59cb1ed890e55dd306f3d2d19ffffffffd06bbf5acef25f5c406a5d3f32b70d238c4fcd43b95cbc1e962dc74a1be1db9d000000006a473044022026b122e551e69ab1ec138f6850350b08dcb59b0e4def7b6ae29538130b1ef0ce022000b951c0a0978b34baaf1788d0b692147beef79a03cf20bb37014589e3e1a112012103ce7f32cf28e78ed5e61b8f5d28d54e42055a89e16a2ba12e90c889b370417cf1ffffffffdba04624c1f22c9bf00a456d9902f0d6a15fed8fd03041723f8ab1f10c36ceb8000000006b483045022100c5b15696c5a44ea6782f084d63271d1b2728bf2d9b495d914f1e213ae1f0f804022016dc4e3977299368a510e12f147454a8e891589372a8617aa6a02b584c537a9e012103bf4a19831bcde19d556dff2331ff368a189baff970e040332726da12f9284504ffffffff0200b0686d8e18000000000000000000001976a914eaf2a16fa9509c76a3458746559ea63d0e30f3c188ac0050630e11960000832c46bdcd04fbef17a914a92acca80015eebb8d59993ac7efd1d6ebb2be51870000000000'
        TaoTx.unhexlify(raw, network=TaoMainnet)

    def test_to_script(self):
        data = {}
        for addr, pkh in addresses:
            data[addr] = P2pkhScript(bytearray(unhexlify(pkh)))
        for script, addr in p2sh.items():
            data[addr] = P2shScript(ScriptBuilder.identify(script))
        for dic in segwit_valid_addresses:
            data[dic['address']] = ScriptBuilder.identify(dic['script'])

        for addr, script in data.items():
            self.assertTrue(Address.from_string(addr, strict=False).to_script().hexlify(),
                            script.hexlify())


class TestStandardness(unittest.TestCase):

    def test_script_pubkey_success(self):
        # standard types
        self.assertTrue(eval(scripts['p2sh']['code']).is_standard())
        self.assertTrue(eval(scripts['p2pkh']['code']).is_standard())
        self.assertTrue(eval(scripts['p2pk']['code']).is_standard())
        self.assertTrue(eval(scripts['multisig']['code']).is_standard())
        self.assertTrue(eval(scripts['nulldata']['code']).is_standard())
        self.assertTrue(eval(scripts['p2wpkh']['code']).is_standard())
        self.assertTrue(eval(scripts['p2wsh']['code']).is_standard())

    def test_script_pubkey_fail(self):
        # nonstandard types
        self.assertFalse(eval(scripts['if_else_timelock']['code']).is_standard())
        self.assertFalse(eval(scripts['relativetimelock']['code']).is_standard())
        # n > 3
        self.assertFalse(
            MultisigScript(
                2,
                PublicKey.unhexlify("02c08786d63f78bd0a6777ffe9c978cf5899756cfc32bfad09a89e211aeb926242"),
                PublicKey.unhexlify("033e81519ecf373ea3a5c7e1c051b71a898fb3438c9550e274d980f147eb4d069d"),
                PublicKey.unhexlify("036d568125a969dc78b963b494fa7ed5f20ee9c2f2fc2c57f86c5df63089f2ed3a"),
                PublicKey.unhexlify("036d568125a969dc78b963b494fa7ed5f20ee9c2f2fc2c57f86c5df63089f2ed3a"),
                4
            ).is_standard()
        )
        # m > n
        self.assertFalse(
            MultisigScript(
                4,
                PublicKey.unhexlify("02c08786d63f78bd0a6777ffe9c978cf5899756cfc32bfad09a89e211aeb926242"),
                PublicKey.unhexlify("033e81519ecf373ea3a5c7e1c051b71a898fb3438c9550e274d980f147eb4d069d"),
                PublicKey.unhexlify("036d568125a969dc78b963b494fa7ed5f20ee9c2f2fc2c57f86c5df63089f2ed3a"),
                3,
                strict=False).is_standard()
        )
        # >80-byte data
        self.assertFalse(NulldataScript(StackData.unhexlify(
            '444f4350524f4f463832bd18ceb0a7861f2a8198013047a3fb861261523c0fc4164abc044e517702444f4350524f4f463832bd18ce'
            'b0a7861f2a8198013047a3fb861261523c0fc4164abc044e51770211')).is_standard())

    def test_txin_success(self):
        # coinbase txin
        txin = TransactionFactory.unhexlify('01000000010000000000000000000000000000000000000000000000000000000000000000'
                                            'ffffffff3d039920071c2f706f6f6c2e626974636f696e2e636f6d2f4249503130302f4238'
                                            '2f0a092f4542312f4144362f109c52640027ed852ba74c0741c3eb0100ffffffff01505266'
                                            '53000000001976a9143fa71ed2e38d431960f314e7e7aad476a5496b4c88ac00000000').ins[0]
        self.assertTrue(txin.is_standard())
        txin = TransactionFactory.unhexlify('0100000001e4da173fbefe5e60ff63dfd38566ade407532294db655463b77a783f379ce6050000000'
                                            '06b483045022100af246c27890c2bc07a0b7450d3d82509702a44a4defdff766355240b114ee2ac02'
                                            '207bb67b468452fa1b325dd5583879f5c1412e0bb4dae1c2c96c7a408796ab76f1012102ab9e85755'
                                            '36a1e99604a158fc60fe2ebd1cb1839e919b4ca42b8d050cfad71b2ffffffff0100c2eb0b00000000'
                                            '1976a914df76c017354ac39bde796abe4294d31de8b5788a88ac00000000').ins[0]
        self.assertTrue(txin.is_standard())

        # actual redeem script (15 sigops: 14 OP_CHECKMULTISIGVERIFY + OP_CHECKSIG)
        script_sig = ScriptSig(bytearray(b'F0C\x02\x1f\x19\xeewU\xa5w\xd8G\x03\x8f;2K\x8b\xfb\xc4 \x006"\xe73\xa9'
                                         b'\x953\x88:,!\xc2\x16\x02 \x1asWN\x01\xb6fw\xc7\r\x93\x0c|\x19\x182W\x04'
                                         b'\xb0\xe6\xd0.\x92\xe6\xb0\xcdk\xc2\xf0n\r\x8e\x01(\x00c^\xafh!\x02\xae'
                                         b'p6\xec\xd9\xda\xc4\xef)\xff\x0b1\x03\xc1\xa8\xfb[\xa0\xbe=\xed\xf65\xd6'
                                         b'\xfa\xa6\x1f\x06K\xef\x07\xff\xac'))
        prev_script = P2shScript(bytearray(b'\xa9\x14\x00H\xee[\x92\xbc\xc9kx\xa0W\x1e\xdch\x14`\xe8B`\xa5\x87'))
        txin = TxIn('4a0884b0aa0c3d34a81ea747aca1368effd9359d573f79873d2d6b4045e49205',
                    9,
                    script_sig,
                    Sequence(0xffffffff))
        self.assertTrue(txin.is_standard(prev_script))

        # 14 sigops redeem script
        script_sig = ScriptSig(bytearray(b'F0C\x02\x1f\x19\xeewU\xa5w\xd8G\x03\x8f;2K\x8b\xfb\xc4 \x006"\xe73\xa9'
                                         b'\x953\x88:,!\xc2\x16\x02 \x1asWN\x01\xb6fw\xc7\r\x93\x0c|\x19\x182W\x04'
                                         b'\xb0\xe6\xd0.\x92\xe6\xb0\xcdk\xc2\xf0n\r\x8e\x01(\x00c^\xafh!\x02\xae'
                                         b'p6\xec\xd9\xda\xc4\xef)\xff\x0b1\x03\xc1\xa8\xfb[\xa0\xbe=\xed\xf65\xd6'
                                         b'\xfa\xa6\x1f\x06K\xef\x07\xff\xac'))
        prev_script = P2shScript(bytearray(b'\xa9\x14\x00H\xee[\x92\xbc\xc9kx\xa0W\x1e\xdch\x14`\xe8B`\xa5\x87'))
        txin = TxIn('4a0884b0aa0c3d34a81ea747aca1368effd9359d573f79873d2d6b4045e49205',
                    9,
                    script_sig,
                    Sequence(0xffffffff))
        self.assertTrue(txin.is_standard(prev_script))

    def test_txin_fail(self):
        # redeem script with 16 sigops (same as above + b'\xac')
        script_sig = ScriptSig(bytearray(b'F0C\x02\x1f\x19\xeewU\xa5w\xd8G\x03\x8f;2K\x8b\xfb\xc4 \x006"\xe73\xa9'
                                         b'\x953\x88:,!\xc2\x16\x02 \x1asWN\x01\xb6fw\xc7\r\x93\x0c|\x19\x182W\x04'
                                         b'\xb0\xe6\xd0.\x92\xe6\xb0\xcdk\xc2\xf0n\r\x8e\x01(\x00c^\xafh!\x02\xae'
                                         b'p6\xec\xd9\xda\xc4\xef)\xff\x0b1\x03\xc1\xa8\xfb[\xa0\xbe=\xed\xf65\xd6'
                                         b'\xfa\xa6\x1f\x06K\xef\x07\xff\xac' + b'\xac'))
        prev_script = P2shScript(bytearray(b'\xa9\x14\x00H\xee[\x92\xbc\xc9kx\xa0W\x1e\xdch\x14`\xe8B`\xa5\x87'))
        txin = TxIn('4a0884b0aa0c3d34a81ea747aca1368effd9359d573f79873d2d6b4045e49205',
                    9,
                    script_sig,
                    Sequence(0xffffffff))
        self.assertFalse(txin.is_standard(prev_script))

        # nonstandard prev_script
        script_sig = ScriptSig(bytearray(b'F0C\x02\x1f\x19\xeewU\xa5w\xd8G\x03\x8f;2K\x8b\xfb\xc4 \x006"\xe73\xa9'
                                         b'\x953\x88:,!\xc2\x16\x02 \x1asWN\x01\xb6fw\xc7\r\x93\x0c|\x19\x182W\x04'
                                         b'\xb0\xe6\xd0.\x92\xe6\xb0\xcdk\xc2\xf0n\r\x8e\x01(\x00c^\xafh!\x02\xae'
                                         b'p6\xec\xd9\xda\xc4\xef)\xff\x0b1\x03\xc1\xa8\xfb[\xa0\xbe=\xed\xf65\xd6'
                                         b'\xfa\xa6\x1f\x06K\xef\x07\xff\xac'))
        prev_script = UnknownScript('\xac')
        txin = TxIn('4a0884b0aa0c3d34a81ea747aca1368effd9359d573f79873d2d6b4045e49205',
                    9,
                    script_sig,
                    Sequence(0xffffffff))
        self.assertFalse(txin.is_standard(prev_script))

    def test_tx_success(self):
        pass

    def test_tx_fail(self):
        pass

    def test_witness_success(self):
        pass

    def test_witness_fail(self):
        pass


class TestSegwitSigs(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = segsig

    def test_hash_prevouts(self):
        for tx in self.data:
            unsigned = Transaction.unhexlify(tx['unsigned_tx'])
            unsigned = SegWitTransaction(unsigned.version, unsigned.ins, unsigned.outs, unsigned.locktime)
            self.assertEqual(unsigned._hash_prevouts(), bytearray(unhexlify(tx['hash_prevouts'])))

    def test_hash_sequence(self):
        for tx in self.data:
            unsigned = Transaction.unhexlify(tx['unsigned_tx'])
            unsigned = SegWitTransaction(unsigned.version, unsigned.ins, unsigned.outs, unsigned.locktime)
            self.assertEqual(unsigned._hash_sequence(), bytearray(unhexlify(tx['hash_sequence'])))

    def test_hash_outputs(self):
        for tx in self.data:
            unsigned = Transaction.unhexlify(tx['unsigned_tx'])
            unsigned = SegWitTransaction(unsigned.version, unsigned.ins, unsigned.outs, unsigned.locktime)
            self.assertEqual(unsigned._hash_outputs(), bytearray(unhexlify(tx['hash_outputs'])))

    def test_digest_preimage(self):
        for tx in self.data:
            unsigned = Transaction.unhexlify(tx['unsigned_tx'])
            unsigned = SegWitTransaction(unsigned.version, unsigned.ins, unsigned.outs, unsigned.locktime)
            for j, txin in enumerate(tx['txins']):
                if 'digest_preimage' in txin:
                    self.assertEqual(unsigned._get_segwit_digest_preimage(j,
                                                                          ScriptBuilder.identify(txin['prev_script']),
                                                                          txin['prev_amount']).hexlify(),
                                     txin['digest_preimage'])

    def test_digest(self):
        for tx in self.data:
            unsigned = Transaction.unhexlify(tx['unsigned_tx'])
            unsigned = SegWitTransaction(unsigned.version, unsigned.ins, unsigned.outs, unsigned.locktime)
            for j, txin in enumerate(tx['txins']):
                if 'digest' in txin:
                    self.assertEqual(hexlify(unsigned.get_segwit_digest(j,
                                                                        ScriptBuilder.identify(txin['prev_script']),
                                                                        txin['prev_amount'])).decode(),
                                     txin['digest'])

    def test_sig(self):
        for tx in self.data:
            if 'signature' in tx:
                for txin in tx['txins']:
                    if 'privk' in txin and 'digest' in txin:
                        self.assertEqual(hexlify(PrivateKey.unhexlify(txin['privk']).sign(bytearray(unhexlify(txin['digest'])),
                                                                                          deterministic=True)).decode(),
                                         tx['signature'])


class TestStrictMode(unittest.TestCase):

    def test_multisig_parsing_non_strict(self):
        # 1 of 2 with one valid and one invalid public key
        script_hex = ('5121037953dbf08030f67352134992643d033417eaa6fcfb770c038f364ff40d7615882100e8f87dd9d24c3a2f1'
                      '02a5a8276c4a8f58176c961dada423b61063a312b7c270e52ae')
        script = ScriptBuilder.identify(script_hex)
        self.assertTrue(isinstance(script, MultisigScript))
        self.assertEqual(script.type, 'multisig')
        self.assertTrue(isinstance(script.pubkeys[0], PublicKey))
        self.assertTrue(isinstance(script.pubkeys[1], StackData))

        # 1 of 2 with two invalid public keys
        script_hex = ('512100e8f87dd9d24c3a2f102a5a8276c4a8f58176c961dada423b61063a312b7c270e2100e8f87dd9d24c3a2f1'
                      '02a5a8276c4a8f58176c961dada423b61063a312b7c270e52ae')
        script = ScriptBuilder.identify(script_hex, strict=False)
        self.assertTrue(isinstance(script, MultisigScript))
        self.assertEqual(script.type, 'multisig')
        self.assertTrue(isinstance(script.pubkeys[0], StackData))
        self.assertTrue(isinstance(script.pubkeys[1], StackData))

        # 2 of 2 with one valid and one invalid public key
        script_hex = ('5221037953dbf08030f67352134992643d033417eaa6fcfb770c038f364ff40d7615882100e8f87dd9d24c3a2f1'
                      '02a5a8276c4a8f58176c961dada423b61063a312b7c270e52ae')
        script = ScriptBuilder.identify(script_hex, strict=False)
        self.assertTrue(isinstance(script, MultisigScript))
        self.assertEqual(script.type, 'multisig')
        self.assertTrue(isinstance(script.pubkeys[0], PublicKey))
        self.assertTrue(isinstance(script.pubkeys[1], StackData))

    def test_multisig_parsing_strict(self):
        # 1 of 2 with one valid and one invalid public key
        script_hex = ('5121037953dbf08030f67352134992643d033417eaa6fcfb770c038f364ff40d7615882100e8f87dd9d24c3a2f1'
                      '02a5a8276c4a8f58176c961dada423b61063a312b7c270e52ae')
        script = ScriptBuilder.identify(script_hex)
        self.assertTrue(isinstance(script, MultisigScript))
        self.assertEqual(script.type, 'multisig')
        self.assertTrue(isinstance(script.pubkeys[0], PublicKey))
        self.assertTrue(isinstance(script.pubkeys[1], StackData))

        # 1 of 2 with two invalid public keys
        script_hex = ('512100e8f87dd9d24c3a2f102a5a8276c4a8f58176c961dada423b61063a312b7c270e2100e8f87dd9d24c3a2f1'
                      '02a5a8276c4a8f58176c961dada423b61063a312b7c270e52ae')
        script = Script.unhexlify(script_hex)
        with self.assertRaises(WrongPubKeyFormat):
            MultisigScript(script)

        # 2 of 2 with one valid and one invalid public key
        script_hex = ('5221037953dbf08030f67352134992643d033417eaa6fcfb770c038f364ff40d7615882100e8f87dd9d24c3a2f1'
                      '02a5a8276c4a8f58176c961dada423b61063a312b7c270e52ae')
        script = Script.unhexlify(script_hex)
        with self.assertRaises(WrongPubKeyFormat):
            MultisigScript(script)

    def test_multisig_creation_strict(self):
        with self.assertRaises(WrongPubKeyFormat):
            MultisigScript(1, StackData.unhexlify('00'*33), StackData.unhexlify('00'*33), 2)

        script = MultisigScript(1,
                                StackData.unhexlify('00'*33),
                                PublicKey.unhexlify('0384478d41e71dc6c3f9edde0f928a47d1b724c05984ebfb4e7d0422e80abe95ff'),
                                2)
        self.assertTrue(isinstance(script, MultisigScript))
        self.assertEqual(script.type, 'multisig')
        self.assertTrue(isinstance(script.pubkeys[0], StackData))
        self.assertTrue(isinstance(script.pubkeys[1], PublicKey))

    def test_multisig_creation_non_strict(self):
        script = MultisigScript(
            1,
            StackData.unhexlify('00'*33),
            StackData.unhexlify('00'*33),
            2,
            strict=False,
        )
        self.assertTrue(isinstance(script, MultisigScript))
        self.assertEqual(script.type, 'multisig')
        self.assertTrue(isinstance(script.pubkeys[0], StackData))
        self.assertTrue(isinstance(script.pubkeys[1], StackData))

        script = MultisigScript(
            1,
            StackData.unhexlify('00'*33),
            PublicKey.unhexlify('0384478d41e71dc6c3f9edde0f928a47d1b724c05984ebfb4e7d0422e80abe95ff'),
            2,
            strict=False,
        )
        self.assertTrue(isinstance(script, MultisigScript))
        self.assertEqual(script.type, 'multisig')
        self.assertTrue(isinstance(script.pubkeys[0], StackData))
        self.assertTrue(isinstance(script.pubkeys[1], PublicKey))

        with self.assertRaises(WrongScriptTypeException):
            MultisigScript(
                1,
                StackData.unhexlify('00'*2),
                StackData.unhexlify('00'*33),
                2,
                strict=False,
            )

    def test_p2pk_parsing_non_strict(self):
        script_hex = '2100e8f87dd9d24c3a2f102a5a8276c4a8f58176c961dada423b61063a312b7c270eac'
        script = ScriptBuilder.identify(script_hex, strict=False)
        self.assertTrue(isinstance(script, P2pkScript))
        self.assertEqual(script.type, 'p2pk')
        self.assertTrue(isinstance(script.pubkey, StackData))

    def test_p2pk_parsing_strict(self):
        script_hex = '2100e8f87dd9d24c3a2f102a5a8276c4a8f58176c961dada423b61063a312b7c270eac'
        script = Script.unhexlify(script_hex)
        with self.assertRaises(WrongPubKeyFormat):
            P2pkScript(script)

    def test_p2pk_creation_strict(self):
        with self.assertRaises(TypeError):
            P2pkScript(StackData.unhexlify('00'*33))

    def test_p2pk_creation_non_strict(self):
        script = P2pkScript(StackData.unhexlify('00'*33), strict=False)
        self.assertTrue(isinstance(script, P2pkScript))
        self.assertEqual(script.type, 'p2pk')
        self.assertTrue(isinstance(script.pubkey, StackData))

        with self.assertRaises(WrongScriptTypeException):
            P2pkScript(StackData.unhexlify('00'*30))


class TestSolvers(unittest.TestCase):

    def test_nested_locktimes(self):
        pubk = PublicKey.unhexlify('021c703de670b3b0df446e948f76acecd6e539a6a395b408bbcd711e2744b74a7b')
        privk = PrivateKey.unhexlify('e2cf56175f5cd5f19e9d1599b99463d769c6e16f1753dfa18aab64cbabeb7b7d')
        script = IfElseScript(
            AbsoluteTimelockScript(
                Locktime(2000),
                RelativeTimelockScript(
                    Sequence(5),
                    P2pkScript(pubk)
                )
            ),
            P2pkScript(pubk)
        )
        p2wsh = P2wshV0Script(script)
        p2sh = P2shScript(p2wsh)
        solver = P2shSolver(
            p2wsh,
            P2wshV0Solver(
                script,
                IfElseSolver(
                    Branch.IF,
                    AbsoluteTimelockSolver(
                        Locktime(2000),
                        RelativeTimelockSolver(
                            Sequence(5),
                            P2pkSolver(privk)
                        )
                    )
                )
            )
        )
        self.assertTrue(solver.solves_absolute_locktime())
        self.assertTrue(solver.solves_relative_locktime())
        self.assertEqual(solver.get_absolute_locktime(), Locktime(2000))
        self.assertEqual(solver.get_relative_locktime(), Sequence(5))

        preimage = Stream(bytearray([0]*30))
        hash160 = preimage.hash160()
        hash256 = preimage.hash256()
        script = IfElseScript(
            AbsoluteTimelockScript(
                Locktime(2000),
                Hashlock160Script(
                    hash160,
                    RelativeTimelockScript(
                        Sequence(5),
                        Hashlock256Script(
                            hash256,
                            AbsoluteTimelockScript(
                                Locktime(3000),
                                RelativeTimelockScript(
                                    Sequence(10),
                                    P2pkScript(pubk)
                                )
                            )
                        )
                    )
                )
            ),
            P2pkScript(pubk)
        )
        p2wsh = P2wshV0Script(script)
        p2sh = P2shScript(p2wsh)
        solver = P2shSolver(
            p2wsh,
            P2wshV0Solver(
                script,
                IfElseSolver(
                    Branch.IF,
                    AbsoluteTimelockSolver(
                        Locktime(2000),
                        HashlockSolver(
                            preimage.serialize(),
                            RelativeTimelockSolver(
                                Sequence(5),
                                HashlockSolver(
                                    preimage.serialize(),
                                    AbsoluteTimelockSolver(
                                        Locktime(3000),
                                        RelativeTimelockSolver(
                                            Sequence(10),
                                            P2pkSolver(privk)
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
        )

        self.assertTrue(solver.solves_absolute_locktime())
        self.assertTrue(solver.solves_relative_locktime())
        self.assertEqual(solver.get_absolute_locktime(), Locktime(3000))
        self.assertEqual(solver.get_relative_locktime(), Sequence(10))

        tx = MutableTransaction(
            2,
            [
                MutableTxIn(
                    '0'*32,
                    0,
                    ScriptSig.empty(),
                    Sequence.max(),
                    witness=Witness([])
                )
            ],
            [
                TxOut(
                    10,
                    0,
                    P2pkScript(pubk)
                )
            ],
            Locktime(0)
        ).spend([TxOut(11, 0, p2sh)], [solver])

        self.assertTrue(isinstance(tx, SegWitTransaction))
        self.assertEqual(tx.locktime, Locktime(3000))
        self.assertEqual(tx.ins[0].sequence, Sequence(10))


if __name__ == '__main__':
    unittest.main()
