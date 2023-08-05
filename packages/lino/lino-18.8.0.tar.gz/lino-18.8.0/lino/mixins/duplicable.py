# -*- coding: UTF-8 -*-
# Copyright 2012-2017 Luc Saffre
# License: BSD (see file COPYING for details)

"""Defines the model mixin :class:`Duplicable`.  "duplicable"
[du'plikəblə] means "able to produce a duplicate
['duplikət], ['du:plikeit]".

"""

from __future__ import unicode_literals, print_function
from builtins import object

import logging
logger = logging.getLogger(__name__)

from django.utils.translation import ugettext_lazy as _

from lino import AFTER17
from lino.core import actions
from lino.core import model
from lino.core.diff import ChangeWatcher


class Duplicate(actions.Action):
    """Duplicate the selected row. 

    This will call :meth:`lino.core.model.Model.on_duplicate` on the
    new object and on related objects.

    """
    label = "\u2687"  # ⚇ "white circle with two dots"
    # label = _("Duplicate")
    # icon_name = 'arrow_divide'
    sort_index = 11
    show_in_workflow = False
    readonly = False  # like ShowInsert. See docs/blog/2012/0726

    def is_callable_from(self, caller):
        if isinstance(caller, actions.ShowInsert):
            return False
        return True

    def unused_get_action_permission(self, ar, obj, state):
        if ar.get_user().user_type.readonly:
            return False
        return super(Duplicate, self).get_action_permission(ar, obj, state)

    def run_from_code(self, ar, **known_values):
        obj = ar.selected_rows[0]
        related = []
        for m, fk in obj._lino_ddh.fklist:
            # print(fk.name, m.allow_cascaded_delete, m.allow_cascaded_copy, obj)
            if fk.name in m.allow_cascaded_delete or fk.name in m.allow_cascaded_copy:
                related.append((fk, m.objects.filter(**{fk.name: obj})))

        if AFTER17:
            fields_list = obj._meta.concrete_fields
        else:
            fields_list = obj._meta.fields
        if True:
            for f in fields_list:
                if not f.primary_key:
                    if f.name not in known_values:
                        known_values[f.name] = getattr(obj, f.name)
            new = obj.__class__(**known_values)
            # 20120704 create_instances causes fill_from_person() on a
            # CBSS request.
        else:
            # doesn't seem to want to work
            new = obj
            for f in fields_list:
                if f.primary_key:
                    # causes Django to consider this an unsaved instance
                    setattr(new, f.name, None)

        new.on_duplicate(ar, None)
        new.save(force_insert=True)
        cw = ChangeWatcher(new)

        for fk, qs in related:
            for relobj in qs:
                relobj.pk = None  # causes Django to save a copy
                setattr(relobj, fk.name, new)
                relobj.on_duplicate(ar, new)
                relobj.save(force_insert=True)

        new.after_duplicate(ar, obj)

        if cw.is_dirty():
            new.full_clean()
            new.save()
            
        return new

    def run_from_ui(self, ar, **kw):
        """This actually runs the action."""
        def ok(ar2):
            new = self.run_from_code(ar)
            kw = dict()
            # kw.update(refresh=True)
            kw.update(message=_("Duplicated %(old)s to %(new)s.") %
                      dict(old=obj, new=new))
            #~ kw.update(new_status=dict(record_id=new.pk))
            ar2.success(**kw)
            if ar.actor.detail_action is None or ar.actor.stay_in_grid:
                ar2.set_response(refresh_all=True)
            else:
                ar2.goto_instance(new)
        obj = ar.selected_rows[0]
        ar.confirm(
            ok, _("This will create a copy of {}").format(obj),
            _("Are you sure?"))


class Duplicable(model.Model):

    """Adds a row action "Duplicate" which duplicates (creates a clone
    of) the object it was called on.
    
    Subclasses may override :meth:`lino.core.model.Model.on_duplicate`
    to customize the default behaviour, which is to copy all fields
    except the primary key and all related objects that are
    duplicable.

    """
    class Meta(object):
        abstract = True

    duplicate = Duplicate()
