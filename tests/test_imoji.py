from imoji.entry import stringify, get_unicode
import unittest


class TestImoji(unittest.TestCase):

    @staticmethod
    def get_text():
        text = "Sendo o emoji de palhaço since 1986 🤡 #NewProfilePic https://t.co/hm2jrLlhrz"
        return text

    def testStringify_whenTextHasOneUnicode_ShouldReturnTextInBytes(self):
        text = self.get_text()
        to_encode = stringify(value=text)
        self.assertEqual(to_encode, b'Sendo o emoji de palha\\xe7o since 1986 \\U0001f921 #NewProfilePic https://t.co/hm2jrLlhrz')

    def testGetUnicode_whenTextHasBytes_ShouldReturnUnicodeWithOutPrefixInList(self):
        text = self.get_text().encode("unicode_escape")
        unicode = get_unicode(value=text)
        self.assertEqual(unicode, ['1f921'])


