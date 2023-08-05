# copyright 2003-2010 LOGILAB S.A. (Paris, FRANCE), all rights reserved.
# contact https://www.logilab.fr/ -- mailto:contact@logilab.fr
#
# This file is part of CubicWeb.
#
# CubicWeb is free software: you can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 2.1 of the License, or (at your option)
# any later version.
#
# CubicWeb is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License along
# with CubicWeb.  If not, see <https://www.gnu.org/licenses/>.
"""mime type transformation engine for cubicweb, based on mtconverter"""


from logilab import mtconverter
from logilab.mtconverter import (
    register_base_transforms,
    register_pil_transforms,
    register_pygments_transforms,
)
from logilab.mtconverter.engine import TransformEngine
from logilab.mtconverter.transform import Transform

from cubicweb.ext.markdown import markdown_publish
from cubicweb.uilib import rest_publish, html_publish
from cubicweb import schema


HTML_MIMETYPES = ("text/html", "text/xhtml", "application/xhtml+xml")

# CubicWeb specific transformations


class rest_to_html(Transform):
    inputs = ("text/rest", "text/x-rst")
    output = "text/html"

    def _convert(self, trdata):
        return rest_publish(trdata.appobject, trdata.decode())


class markdown_to_html(Transform):
    inputs = ("text/markdown", "text/x-markdown")
    output = "text/html"

    def _convert(self, trdata):
        return markdown_publish(trdata.appobject, trdata.decode())


class html_to_html(Transform):
    inputs = HTML_MIMETYPES
    output = "text/html"

    def _convert(self, trdata):
        return html_publish(trdata.appobject, trdata.data)


# Instantiate and configure the transformation engine

mtconverter.UNICODE_POLICY = "replace"

ENGINE = TransformEngine()
ENGINE.add_transform(rest_to_html())
ENGINE.add_transform(markdown_to_html())
ENGINE.add_transform(html_to_html())

schema.NEED_PERM_FORMATS.remove("text/cubicweb-page-template")


if register_pil_transforms(ENGINE, verb=False):
    HAS_PIL_TRANSFORMS = True
else:
    HAS_PIL_TRANSFORMS = False

try:
    from logilab.mtconverter.transforms import pygmentstransforms

    for mt in ("text/plain",) + HTML_MIMETYPES:
        try:
            pygmentstransforms.mimetypes.remove(mt)
        except ValueError:
            continue
    register_pygments_transforms(ENGINE, verb=False)

    def patch_convert(cls):
        def _convert(self, trdata, origconvert=cls._convert):
            add_css = getattr(trdata.appobject._cw, "add_css", None)
            if add_css is not None:
                # session has no add_css, only http request
                add_css("pygments.css")
            return origconvert(self, trdata)

        cls._convert = _convert

    patch_convert(pygmentstransforms.PygmentsHTMLTransform)

    HAS_PYGMENTS_TRANSFORMS = True
except ImportError:
    HAS_PYGMENTS_TRANSFORMS = False

register_base_transforms(ENGINE, verb=False)
