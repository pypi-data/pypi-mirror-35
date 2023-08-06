# coding=utf-8
import datetime
import itertools

from aioxmpp import JID


def _agent_in_msg(agent, msg):
    return msg.to == agent or msg.sender == agent


class TraceStore(object):
    def __init__(self, size):
        self.size = size
        self.store = []

    def reset(self):
        self.store = []

    def append(self, event, category=None):
        date = datetime.datetime.now()
        self.store.insert(0, (date, event, category))
        if len(self.store) > self.size:
            del self.store[-1]

    def len(self):
        return len(self.store)

    def all(self, limit=None):
        return self.store[:limit][::-1]

    def received(self, limit=None):
        return list(itertools.islice((itertools.filterfalse(lambda x: x[1].sent, self.store)), limit))[::-1]

    def filter(self, limit=None, to=None, category=None):
        if category and not to:
            msg_slice = itertools.islice((x for x in self.store if x[2] == category), limit)
        elif to and not category:
            to = JID.fromstr(to)
            msg_slice = itertools.islice((x for x in self.store if _agent_in_msg(to, x[1])), limit)
        elif to and category:
            to = JID.fromstr(to)
            msg_slice = itertools.islice((x for x in self.store if _agent_in_msg(to, x[1]) and x[2] == category), limit)
        else:
            msg_slice = self.all(limit=limit)
            return msg_slice

        return list(msg_slice)[::-1]
