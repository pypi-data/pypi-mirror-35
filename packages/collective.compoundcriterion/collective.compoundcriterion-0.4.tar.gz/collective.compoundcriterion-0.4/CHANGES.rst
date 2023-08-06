Changelog
=========


0.4 (2018-08-31)
----------------

- When getting the adapter, if context is not the Collection, try to get real context
  following various cases.  This is the case when using Collection
  from plone.app.contenttypes.
  [gbastien]
- Do not use a SelectionWidget to render the querystring widget as it does not
  exist anymore for plone.app.contenttypes Collection.
  Use the MultipleSelectionWidget.  This way finally we may select several
  filters to build the query.
  [gbastien]
- When using 'not' in queries for ZCatalog 3, 'query' level must be replaced by 'not' in query dictionary.
  [sgeulette]

0.3 (2016-12-08)
----------------

- Return clear message when a query format is not plone.app.querystring compliant.
  [gbastien]


0.2 (2015-09-04)
----------------

- Raise a KeyError if the format of the query returned by the named adapter
  is not compliant with what is returned by
  plone.app.querystring.queryparser.parseFormquery, this way it behaves
  correctly with collective.eeafaceted.collectionwidget.
  [gbastien]


0.1 (2015-06-02)
----------------

- Initial release.
  [IMIO]
