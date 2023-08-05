"""
    Slixmpp: The Slick XMPP Library
    Copyright (C) 2012 Nathanael C. Fritz, Lance J.T. Stout
    This file is part of Slixmpp.

    See the file LICENSE for copying permission.
"""

import logging

from slixmpp import Iq, Message
from slixmpp.plugins import BasePlugin
from slixmpp.xmlstream import register_stanza_plugin
from slixmpp.plugins.xep_0258 import stanza, SecurityLabel, Catalog


log = logging.getLogger(__name__)


class XEP_0258(BasePlugin):

    name = 'xep_0258'
    description = 'XEP-0258: Security Labels in XMPP'
    dependencies = {'xep_0030'}
    stanza = stanza

    def plugin_init(self):
        register_stanza_plugin(Message, SecurityLabel)
        register_stanza_plugin(Iq, Catalog)

    def plugin_end(self):
        self.xmpp['xep_0030'].del_feature(feature=SecurityLabel.namespace)

    def session_bind(self, jid):
        self.xmpp['xep_0030'].add_feature(SecurityLabel.namespace)

    def get_catalog(self, jid, ifrom=None,
                          callback=None, timeout=None):
        iq = self.xmpp.Iq()
        iq['to'] = jid
        iq['from'] = ifrom
        iq['type'] = 'get'
        iq.enable('security_label_catalog')
        return iq.send(callback=callback, timeout=timeout)
