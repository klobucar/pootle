#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2009 Zuza Software Foundation
#
# This file is part of Pootle.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.

from django import forms
from djblets.siteconfig.forms import SiteSettingsForm
from django.utils.translation import ugettext_lazy as _


class GeneralSettingsForm(SiteSettingsForm):
    TITLE = forms.CharField(
        label=_("Title"),
        help_text=_("The name for this Pootle server"),
        max_length=50,
        required=True,
    )
    DESCRIPTION = forms.CharField(
        label=_("Description"),
        help_text=_("The description and instructions shown on the front page and about page. Be sure to use valid HTML."),
        max_length=8192,
        required=True,
        widget=forms.Textarea,
    )

    class Meta:
        title = "General Settings"
