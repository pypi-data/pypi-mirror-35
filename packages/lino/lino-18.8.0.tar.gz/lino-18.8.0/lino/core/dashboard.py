# -*- coding: UTF-8 -*-
# Copyright 2016-2018 Rumma & Ko Ltd
# License: BSD, see LICENSE for more details.
"""Defines the :class:`DashboardItem` class.

"""
from __future__ import unicode_literals
from builtins import str

from lino.api import _
from lino.core.permissions import Permittable
from etgen.html import E, tostring

class DashboardItem(Permittable):
    """Base class for all dashboard items.

    .. attribute:: name

        The name used to reference this item in
        :attr:`Widget.item_name`.

    .. attribute:: width

        The width in percent of total available width.

    """

    width = None
    header_level = None
    
    def __init__(self, name):
        self.name = name
        
    def render(self, ar):
        """Return a HTML string """

    def render_request(self, ar, sar):
        """
        Render the given table action
        request. `ar` is the incoming request (the one which displays
        the dashboard), `sar` is the table we want to show (a child of
        `ar`).

        This is a helper function for shared use by :class:`ActorItem`
        and :class:`RequestItem`.
        """
        T = sar.actor
        if not sar.get_total_count():
            # print("20180212 render no rows in ", sar)
            return ''
        if self.header_level is None:
            s = ''
        else:
            s = tostring(E.h2(
                str(sar.actor.get_title_base(sar)),
                ' ', ar.window_action_button(
                    T.default_action,
                    # label="🗗",
                    # label="☌",  # conjunction
                    # label="◱", # 25F1
                    # label="◳", # 25F3
                    # label="⏍", # 23CD
                    label="⏏", # 23CF
                    # label="⍐", # 2350
                    # style="text-decoration:none; font-size:80%;",
                    style="text-decoration:none;",
                    title=_("Show this table in own window"))))

        s += tostring(ar.show(sar))
        return s
            
class ActorItem(DashboardItem):
    """A dashboard item which simply renders a given actor.
    The actor should be a table, other usage is untested.

    Usage examples:
    - :mod:`lino_xl.lib.blogs` 
    - :mod:`lino_book.projects.events` 

    .. attribute:: header_level

        The header level.

    """
    def __init__(self, actor, header_level=2):
        self.actor = actor
        self.header_level = header_level
        super(ActorItem, self).__init__(str(actor))
        
    def get_view_permission(self, user_type):
        return self.actor.default_action.get_view_permission(user_type)

    def render(self, ar):
        """Render this table to the dashboard.

        - Do nothing if there is no data.

        - If :attr:`header_level` is not None, add a header

        - Render the table itself by calling
          :meth:`lino.core.requests.BaseRequest.show`

        """
        T = self.actor
        sar = ar.spawn(T, limit=T.preview_limit)
        return self.render_request(ar, sar)
    
class RequestItem(DashboardItem):
    """
    Experimentally used in `lino_book.projects.events`.
    """
    def __init__(self, sar, header_level=2):
        self.sar = sar
        self.header_level = header_level
        super(RequestItem, self).__init__(None)
        
    def get_view_permission(self, user_type):
        return self.sar.get_permission()
    
    def render(self, ar):
        return self.render_request(ar, self.sar)
        

class CustomItem(DashboardItem):
    """Won't work. Not used and not tested."""
    def __init__(self, name, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs
        super(CustomItem, self).__init__(name)
        
    def render(self, ar):
        return self.func(ar, *self.args, **self.kwargs)
                          
