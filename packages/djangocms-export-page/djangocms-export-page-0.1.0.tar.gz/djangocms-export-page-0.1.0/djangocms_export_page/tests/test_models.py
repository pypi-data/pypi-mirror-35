from django.test import RequestFactory, TestCase, override_settings

from annefrank.blog.tests.factories import BlogFactory

from ..export.common import PageExport
from ..export.docx import DocxPageExport


@override_settings(ROOT_URLCONF='annefrank.blog.tests.urls_tests')
class ExportModelTests(TestCase):
    def setUp(self):
        self.object = BlogFactory()
        self.language = 'nl'
        self.request = RequestFactory().get(self.object.get_absolute_url())

    def test_model_export(self):
        export = DocxPageExport(self.request, self.object, language=self.language)
        export_file = export.export()
        self.assertEqual(type(export_file), bytes)

    def test_page_url(self):
        export = PageExport(self.request, self.object, language=self.language)
        self.assertEqual(export.page_url, 'http://example.com' + self.object.get_absolute_url())
