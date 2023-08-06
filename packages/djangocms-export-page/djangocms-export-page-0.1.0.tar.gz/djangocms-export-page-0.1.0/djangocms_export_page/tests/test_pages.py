from django.test import RequestFactory, TestCase

from cms.api import add_plugin
from cms.models import Placeholder
from meta.views import Meta
from mock import patch

from annefrank.plugins.tests.factories import PageFactory

from ..export.common import Field, PageExport
from ..export.docx import DocxPageExport


class ExportPageTests(TestCase):
    def setUp(self):
        self.placeholder = Placeholder.objects.create(slot='test')
        self.page = PageFactory()
        self.page.placeholders.add(self.placeholder)
        self.language = 'nl'
        self.request = RequestFactory().get('/nl/')

    def test_expost_non_implemented(self):
        with self.assertRaises(NotImplementedError):
            PageExport(self.request, self.page, language=self.language).export()

    def test_base_url(self):
        export = PageExport(self.request, self.page, language=self.language)
        self.assertEqual(export.base_url, 'http://example.com')

    def test_page_url(self):
        export = PageExport(self.request, self.page, language=self.language)
        self.assertEqual(export.page_url, 'http://example.com/nl/')

    @patch('djangocms_export_page.export.common.get_page_meta')
    def test_meta_extra_custom_props(self, mock):
        mock.return_value = Meta(extra_custom_props=[
            ('propz', 'some', 'val'),
        ])
        export = PageExport(self.request, self.page, language=self.language)
        section = export.get_data()[0]
        self.assertIn(Field('some (propz)', 'val'), section.components[0].fields)

    def test_blank_page_export(self):
        export = DocxPageExport(self.request, self.page, language=self.language)
        export_file = export.export()
        self.assertEqual(type(export_file), bytes)

    def test_page_with_body_text(self):
        add_plugin(self.placeholder, 'BodyTextPlugin', 'nl', body='Some text')
        export = DocxPageExport(self.request, self.page, language=self.language)
        self.assertEqual(export.get_data()[0].components[0].fields[0].value, 'Some text')

    def test_page_with_control_char_in_text(self):
        add_plugin(self.placeholder, 'BodyTextPlugin', 'nl', body='Some text \f')
        export = DocxPageExport(self.request, self.page, language=self.language)
        self.assertEqual(export.get_data()[0].components[0].fields[0].value, 'Some text')
