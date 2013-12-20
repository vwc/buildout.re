from five import grok
from plone.directives import dexterity, form
from zope import schema
from plone.indexer import indexer

from plone.namedfile.interfaces import IImageScaleTraversable

from plone.app.textfield import RichText
from plone.namedfile.field import NamedBlobImage

from erben.blog import MessageFactory as _


class IBlogEntry(form.Schema, IImageScaleTraversable):
    """
    A single blogentry that can contain images
    """
    text = RichText(
        title=_(u"Blog Entry"),
        description=_(u"Please enter main body text for this blog entry"),
        required=False,
    )
    form.fieldset(
        'details',
        label=_(u"Details"),
        fields=['image', 'pressitem']
    )
    image = NamedBlobImage(
        title=_(u"Preview Image"),
        description=_(u"Upload optional preview image displayed in listings"),
        required=False,
    )
    pressitem = schema.Bool(
        title=_(u"Mark this entry as pressrelease?"),
        default=False,
    )


@indexer(IBlogEntry)
def pressitemIndexer(obj):
    return obj.pressitem
grok.global_adapter(pressitemIndexer, name="pressitem")


class BlogEntry(dexterity.Container):
    grok.implements(IBlogEntry)


class View(grok.View):
    grok.context(IBlogEntry)
    grok.require('zope2.View')
    grok.name('view')
