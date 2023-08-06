import os
import json
from plone import api
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.interface import directlyProvides
from zope.interface import provider
from plone.i18n.normalizer.interfaces import IIDNormalizer
from zope.component import getUtility
from plone.app.vocabularies.catalog import KeywordsVocabulary

from collective.vocabularies import DATABASE_DIR


@provider(IVocabularyFactory)
def country_factory(context):
    countries_db = os.path.join(DATABASE_DIR, 'countries.json')
    with open(countries_db, 'r') as dp:
        data = json.load(dp)

    lang = api.portal.get_current_language()
    normalizer = getUtility(IIDNormalizer)
    items = []
    for item in data:
        country_name = api.portal.translate(
            item['country'],
            lang=lang
        )
        items.append((country_name, country_name))
    items.sort(key=lambda it: normalizer.normalize(it[1], locale=lang))
    items = [
        SimpleTerm(value=it[0], title=it[1])
        for it in items
    ]
    return SimpleVocabulary(items)