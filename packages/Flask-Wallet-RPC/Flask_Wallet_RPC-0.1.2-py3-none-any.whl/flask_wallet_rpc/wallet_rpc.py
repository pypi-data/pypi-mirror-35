from __future__ import absolute_import
from flask import _request_ctx_stack
from werkzeug.local import LocalProxy
from slickrpc import Proxy


def _get_wallet():
    from flask import current_app
    return current_app.wallet_instance

def _wallet_context_processor():
    return dict(current_wallet=_get_wallet())

current_wallet = LocalProxy(lambda: _get_wallet())

wallet = LocalProxy(lambda: _get_wallet().connect)

class Walletrpc(object):
    """Central controller class that can be used to configure how
    Flask-Wallet-RPC behaves.  Each application that wants to use Flask-Wallet-RPC
    has to create, or run :meth:`init_app` on, an instance of this class
    after the configuration was initialized.
    """

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
         """Set up this instance for use with *app*, if no app was passed to
        the constructor.
        """
        self.app = app
        app.wallet_instance = self
        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['wallet'] = self

        app.config.setdefault('WALLET_RPC_URL', '"http://%s:%s@127.0.0.1:8332"%("Rpcuser", "Rpcpassword")')
        self.connect = Proxy(app.config['WALLET_RPC_URL'])

        app.context_processor(_wallet_context_processor)
        app.teardown_appcontext(self.teardown)

     def teardown(self, exception):
        ctx = _request_ctx_stack.top
        if hasattr(ctx, 'extensions'):
            ctx.extensions.close()
