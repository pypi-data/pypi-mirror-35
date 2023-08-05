"""
    Slixmpp: The Slick XMPP Library
    Copyright (C) 2011 Nathanael C. Fritz, Lance J.T. Stout
    This file is part of Slixmpp.

    See the file LICENSE for copying permission.
"""

import logging

from slixmpp import asyncio
from slixmpp.xmlstream import register_stanza_plugin
from slixmpp.plugins.base import BasePlugin, register_plugin


log = logging.getLogger(__name__)


class XEP_0163(BasePlugin):

    """
    XEP-0163: Personal Eventing Protocol (PEP)
    """

    name = 'xep_0163'
    description = 'XEP-0163: Personal Eventing Protocol (PEP)'
    dependencies = {'xep_0030', 'xep_0060', 'xep_0115'}

    def register_pep(self, name, stanza):
        """
        Setup and configure events and stanza registration for
        the given PEP stanza:

            - Add disco feature for the PEP content.
            - Register disco interest in the PEP content.
            - Map events from the PEP content's namespace to the given name.

        :param str name: The event name prefix to use for PEP events.
        :param stanza: The stanza class for the PEP content.
        """
        pubsub_stanza = self.xmpp['xep_0060'].stanza
        register_stanza_plugin(pubsub_stanza.EventItem, stanza)

        self.add_interest(stanza.namespace)
        self.xmpp['xep_0030'].add_feature(stanza.namespace)
        self.xmpp['xep_0060'].map_node_event(stanza.namespace, name)

    def add_interest(self, namespace, jid=None):
        """
        Mark an interest in a PEP subscription by including a disco
        feature with the '+notify' extension.

        Arguments:
            namespace -- The base namespace to register as an interest, such
                         as 'http://jabber.org/protocol/tune'. This may also
                         be a list of such namespaces.
            jid       -- Optionally specify the JID.
        """
        if not isinstance(namespace, set) and not isinstance(namespace, list):
            namespace = [namespace]

        for ns in namespace:
            self.xmpp['xep_0030'].add_feature('%s+notify' % ns,
                                              jid=jid)
        asyncio.ensure_future(self.xmpp['xep_0115'].update_caps(jid))

    def remove_interest(self, namespace, jid=None):
        """
        Mark an interest in a PEP subscription by including a disco
        feature with the '+notify' extension.

        Arguments:
            namespace -- The base namespace to remove as an interest, such
                         as 'http://jabber.org/protocol/tune'. This may also
                         be a list of such namespaces.
            jid       -- Optionally specify the JID.
        """
        if not isinstance(namespace, (set, list)):
            namespace = [namespace]

        for ns in namespace:
            self.xmpp['xep_0030'].del_feature(jid=jid,
                                              feature='%s+notify' % namespace)
        asyncio.ensure_future(self.xmpp['xep_0115'].update_caps(jid))

    def publish(self, stanza, node=None, id=None, options=None, ifrom=None,
                timeout_callback=None, callback=None, timeout=None):
        """
        Publish a PEP update.

        This is just a (very) thin wrapper around the XEP-0060 publish()
        method to set the defaults expected by PEP.

        Arguments:
            stanza   -- The PEP update stanza to publish.
            node     -- The node to publish the item to. If not specified,
                        the stanza's namespace will be used.
            id       -- Optionally specify the ID of the item.
            options  -- A form of publish options.
            ifrom    -- Specify the sender's JID.
            timeout  -- The length of time (in seconds) to wait for a response
                        before exiting the send call if blocking is used.
                        Defaults to slixmpp.xmlstream.RESPONSE_TIMEOUT
            callback -- Optional reference to a stream handler function. Will
                        be executed when a reply stanza is received.
        """
        if node is None:
            node = stanza.namespace
        if id is None:
            id = 'current'

        return self.xmpp['xep_0060'].publish(ifrom, node, id=id,
                                             payload=stanza.xml,
                                             options=options, ifrom=ifrom,
                                             callback=callback,
                                             timeout=timeout,
                                             timeout_callback=timeout_callback)


register_plugin(XEP_0163)
