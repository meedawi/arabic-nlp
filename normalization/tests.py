import unittest

from normalization.orthographic_normalization import tatweel_removal, \
    diacritic_removal, letter_normalization


class TestOrthographicNormalization(unittest.TestCase):
    def test_tatweel_removal(self):
        # Empty String
        self.assertEqual(tatweel_removal(''), '')
        # None object
        self.assertIsNone(tatweel_removal(None))

        # String without tatweel
        without_tatweel = 'جميل'
        self.assertEqual(
            tatweel_removal(without_tatweel), without_tatweel)

        # First tatweel
        first_tatweel = 'ـجميل'
        self.assertEqual(
            tatweel_removal(first_tatweel), without_tatweel)
        # mid tatweel
        mid_tatweel = 'جـمـيـل'
        self.assertEqual(tatweel_removal(mid_tatweel), without_tatweel)
        # Last tatweel
        last_tatweel = 'جميلـ'
        self.assertEqual(tatweel_removal(last_tatweel), without_tatweel)
        # All tatweel
        all_tatweel = 'ــــ'
        self.assertEqual(tatweel_removal(all_tatweel), '')

    def test_diacritic_removal(self):
        # Empty String
        self.assertEqual(diacritic_removal(''), '')
        # None object
        self.assertIsNone(diacritic_removal(None))

        # String without diacritics
        without_diacritics = 'جميل'
        self.assertEqual(
            diacritic_removal(without_diacritics), without_diacritics)

        # First tatweel
        first_diacritic = 'جُميل'
        self.assertEqual(
            diacritic_removal(first_diacritic), without_diacritics)
        # mid diacritic
        mid_diacritic = 'جَمِيْلٌ'
        self.assertEqual(
            diacritic_removal(mid_diacritic), without_diacritics)
        # Last diacritic
        last_diacritic = 'جميلٌ'
        self.assertEqual(
            diacritic_removal(last_diacritic), without_diacritics)
        # All diacritic
        all_diacritic = 'جَمِيْلٌ'
        self.assertEqual(diacritic_removal(all_diacritic), without_diacritics)

    def test_letter_normalization(self):
        # Testing without egyption
        self.assertEqual(
            letter_normalization('مستشفى'), 'مستشفى')
        self.assertEqual(
            letter_normalization('أحمد إبراهيم'), 'احمد ابراهيم')
        self.assertEqual(
            letter_normalization('جميلة'), 'جميله')
        self.assertEqual(
            letter_normalization('لؤلؤ'), 'لءلء')
        self.assertEqual(
            letter_normalization('أرجئ'), 'ارجء')

        # Testing with egyption
        self.assertEqual(
            letter_normalization('مستشفى', egyptian=True), 'مستشفي')
        self.assertEqual(
            letter_normalization('أحمد إبراهيم', egyptian=True),
            'احمد ابراهيم')
        self.assertEqual(
            letter_normalization('جميلة', egyptian=True), 'جميله')
        self.assertEqual(
            letter_normalization('لؤلؤ', egyptian=True), 'لءلء')
        self.assertEqual(
            letter_normalization('أرجئ', egyptian=True), 'ارجء')
