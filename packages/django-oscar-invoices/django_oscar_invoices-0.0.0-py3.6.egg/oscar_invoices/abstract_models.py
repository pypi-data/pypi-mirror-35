from django.conf import settings
from django.core.files.base import ContentFile
from django.db import models
from django.template.loader import render_to_string
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField

from oscar.apps.address.abstract_models import AbstractAddress

from . import app_settings


@python_2_unicode_compatible
class AbstractLegalEntity(models.Model):
    """
    Represents LegalEntity - merchant (company or individual) which we issue
    invoice on behalf of.
    """
    shop_name = models.CharField(_('Shop name'), max_length=255, null=True, blank=True)
    business_name = models.CharField(_('Business name'), max_length=255, db_index=True)
    vat_number = models.CharField(_('VAT identification number'), max_length=20)
    logo = models.ImageField(
        _('Logo'), upload_to=settings.OSCAR_IMAGE_FOLDER, max_length=255, null=True, blank=True)
    email = models.EmailField(_('Email'), null=True, blank=True)
    web_site = models.URLField(_('Website'), null=True, blank=True)

    class Meta:
        abstract = True
        app_label = 'oscar_invoices'
        verbose_name = _('Legal Entity')
        verbose_name_plural = _('Legal Entities')

    def __str__(self):
        return self.business_name

    @property
    def has_addresses(self):
        return self.addresses.exists()


@python_2_unicode_compatible
class AbstractLegalEntityAddress(AbstractAddress):
    """
    Represents Address of LegalEntity.

    Used in Invoices.
    """
    legal_entity = models.ForeignKey(
        'oscar_invoices.LegalEntity',
        on_delete=models.CASCADE,
        related_name='addresses',
        verbose_name=_('Legal Entity'))

    phone_number = PhoneNumberField(_('Phone number'), blank=True)
    fax_number = PhoneNumberField(_('Fax number'), blank=True)

    class Meta:
        abstract = True
        app_label = 'oscar_invoices'
        verbose_name = _('Legal Entity Address')
        verbose_name_plural = _('Legal Entity Addresses')


@python_2_unicode_compatible
class AbstractInvoice(models.Model):
    """
    An Invoice.
    """

    legal_entity = models.ForeignKey(
        'oscar_invoices.LegalEntity',
        on_delete=models.CASCADE,
        related_name='invoices',
        verbose_name=_('Legal Entity'))

    number = models.CharField(
        _('Invoice number'), max_length=128)

    order = models.OneToOneField(
        'order.Order', verbose_name=_('Order'), related_name='invoice',
        null=True, blank=True, on_delete=models.SET_NULL)

    notes = models.TextField(_('Notes for invoice'), null=True, blank=False)

    document = models.FileField(
        _('Document'), upload_to=app_settings.OSCAR_INVOICES_UPLOAD_FOLDER,
        blank=True, null=True, max_length=255)

    class Meta:
        abstract = True
        app_label = 'oscar_invoices'
        verbose_name = _('Invoice')
        verbose_name_plural = _('Invoices')

    @classmethod
    def get_last_invoice_number(cls):
        last_invoice = cls.objects.order_by('-id').last()
        return last_invoice.number if last_invoice else 0

    def __str__(self):
        if self.order:
            order_number = self.order.number
            return _(
                'Invoice #%(invoice_number)s for order #%(order_number)s'
            ) % {'invoice_number': self.number, 'order_number': order_number}

        return _(
            'Invoice %(invoice_number)s') % {'number': self.number}

    def get_invoice_filename(self):
        return 'invoice_{}.html'.format(self.order.number)

    def render_document(self):
        """
        Return rendered from html template invoice document.
        """
        template_name = 'invoices/invoice.html'
        template_context = {
            'invoice': self,
            'order': self.order,
            'legal_entity': self.legal_entity,
            'legal_entity_address': self.legal_entity.addresses.first(),
        }
        return render_to_string(template_name, template_context)

    def generate_and_save_document(self):
        """
        Create and save invoice document (as *.html file).
        """
        document_file = ContentFile(self.render_document())
        self.document.save(self.get_invoice_filename(), document_file)
