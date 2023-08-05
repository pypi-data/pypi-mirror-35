================
Flask-Wallet-RPC
================

Flask-Wallet-RPC is a Crypto Wallet RPC client extension for `Flask`_, based on the
Python module `slick-bitcoinrpc`_.
Connects to the RPC server of your wallet.


Installation
------------

Install the extension with one of the following commands::

    $ easy_install Flask-Walet-RPC

or alternatively if you have pip installed::

    $ pip install Flask-Wallet-RPC


Example 1
=========
.. code:: python

    from flask import Flask
    from flask_wallet_rpc import Walletrpc, wallet

    app = Flask(__name__)
    app.config.from_pyfile('mysettings.cfg')
    w = Walletrpc(app)

    @app.route('/')
    def main():
        return wallet.getwalletinfo()

Example 2
=========
.. code:: python

    from flask import Flask
    from flask_wallet_rpc import Walletrpc, wallet

    rpc = Walletrpc()

    def create_app('the-config.cfg'):
        rpc.init_app(app)

Then in your blueprint.

.. code:: python

    from yourapp import wallet
    bp = Blueprint('name_of_bp', __name__)

    @bp.route('/')
    def index():
        return wallet.getwalletinfo()


Configuration
=============
In your flask app config add::

  WALLET_RPC_URL = "http://%s:%s@127.0.0.1:8332"%("Rpcuser", "Rpcpassword")

Replace Rpcuser and Rpcpassword with your wallets RPC info.


.. _Flask: http://flask.pocoo.org/
.. _slick-bitcoinrpc: https://pypi.python.org/pypi/slick-bitcoinrpc
