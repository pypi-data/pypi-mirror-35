===============================
 The ZCML Documentation Module
===============================

.. currentmodule:: zope.app.apidoc.zcmlmodule

This documentation module provides you with a complete reference of all
directives available on your Zope 3 installation.


:class:`ZCMLModule`
===================

The ZCML module class manages all available ZCML namespaces. Once we
initialize the module

  >>> from zope.app.apidoc.zcmlmodule import ZCMLModule
  >>> module = ZCMLModule()

it evaluates all meta directives and creates the namspace list:

  >>> module.get('http://namespaces.zope.org/browser').getFullName()
  'http://namespaces.zope.org/browser'

You can also access the namespace via its encoded form:

  >>> module.get(
  ...     'http_co__sl__sl_namespaces.zope.org_sl_browser').getFullName()
  'http://namespaces.zope.org/browser'

and via its short form:

  >>> module.get('browser').getFullName()
  'http://namespaces.zope.org/browser'

If the module does not exist, the usual :const:`None` is returned:

  >>> module.get('foo') is None
  True

You can also list all namespaces:

  >>> names = [n for n, ns in module.items()]
  >>> 'ALL' in names
  True
  >>> 'http_co__sl__sl_namespaces.zope.org_sl_browser' in names
  True
  >>> 'http_co__sl__sl_namespaces.zope.org_sl_meta' in names
  True


:class:`Namespace`
==================

Simple namespace object for the ZCML Documentation Module.

The namespace manages a particular ZCML namespace. The object always
expects the parent to be a :class:`ZCMLModule` instance. So let's
create a namespace:

  >>> module = ZCMLModule()
  >>> from zope.app.apidoc.zcmlmodule import Namespace, _clear
  >>> _clear()
  >>> ns = Namespace(ZCMLModule(), 'http://namespaces.zope.org/browser')

We can now get its short name, which is the name without the URL prefix:

  >>> ns.getShortName()
  'browser'

and its full name in unquoted form:

  >>> ns.getFullName()
  'http://namespaces.zope.org/browser'

or even quoted:

  >>> ns.getQuotedName()
  'http_co__sl__sl_namespaces.zope.org_sl_browser'

One can get a directive using the common mapping interface:

  >>> ns.get('pages').__name__
  'pages'

  >>> ns.get('foo') is None
  True

  >>> print('\n'.join([name for name, dir in ns.items()][:3]))
  addMenuItem
  addform
  containerViews

:func:`quoteNS`
===============

Quotes a namespace to make it URL-secure.

  >>> from zope.app.apidoc.zcmlmodule import quoteNS
  >>> quoteNS('http://namespaces.zope.org/browser')
  'http_co__sl__sl_namespaces.zope.org_sl_browser'


:func:`unquoteNS`
=================

Un-quotes a namespace from a URL-secure version.

  >>> from zope.app.apidoc.zcmlmodule import unquoteNS
  >>> unquoteNS('http_co__sl__sl_namespaces.zope.org_sl_browser')
  'http://namespaces.zope.org/browser'
