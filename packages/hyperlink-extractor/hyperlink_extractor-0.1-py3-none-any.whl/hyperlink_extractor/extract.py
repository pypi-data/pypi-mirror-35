import six
from hyperlink import URL
from lxml import html

if six.PY2:
    from urlparse import urljoin
elif six.PY3:
    from urllib.parse import urljoin
else:
    raise RuntimeError('Unable to find "urljoin"')


def _a_handler(a_el):
    href = a_el.attrib.get('href')
    if href:
        url = urljoin(a_el.base_url, href)
        if not isinstance(url, six.text_type):
            url = six.u(url)
        return URL.from_text(url)


_HTML_TAG_HANDLERS = {
    'a': _a_handler
}


def extract_from_el(el):
    xpaths = ['descendant-or-self::a']
    els = [el_ for xpath in xpaths for el_ in el.xpath(xpath)
           if el_.tag in _HTML_TAG_HANDLERS]
    links = [_HTML_TAG_HANDLERS[el.tag](el) for el in els]
    return [link for link in links if link]


def extract_from_doc(doc, restrict_xpaths=None):
    """ Returns hyperlink.URL from given lxml.Element. """

    restrict_xpaths = restrict_xpaths or []
    if restrict_xpaths:
        els = [el for xpath in restrict_xpaths for el in doc.xpath(xpath)]
    else:
        els = [doc]

    return [hlink for el in els for hlink in extract_from_el(el)]


def extract(text, restrict_xpaths=None, base_url=None):
    """ Returns hyperlink.URL from given text. """
    if isinstance(text, six.binary_type):
        _io = six.BytesIO(text)
    elif isinstance(text, (six.string_types, six.text_type)):
        _io = six.StringIO(text)
    else:
        raise RuntimeError('Unsupported text type %s' % type(text))

    doc = html.parse(_io, base_url=base_url)
    return extract_from_doc(doc, restrict_xpaths)
