import unittest
from cyberark import CyberarkAgent
from email_agent import Email, Inbox

class TestCyberArk(unittest.TestCase):
    def setUp(self):
        self.crkl = CyberarkAgent('s_damail_n',
                                  'APPL_PROP_DAMAIL_ikjk',
                                  'APPL_TECHCORE_DAMAIL')

    def tearDown(self):
        print('teardown')

    def test_get_password(self):
        password = self.crkl.get_password()
        self.assertIsInstance(password, str)


class TestInbox(unittest.TestCase):
    def setUp(self):
        self.ob = Inbox('s_damail_n',
                        CyberarkAgent('s_damail_n',
                                      'APPL_PROP_DAMAIL_ikjk',
                                  'APPL_TECHCORE_DAMAIL').get_password(),
                        'C:\\Users\\sshresth\\Documents\\Cyberark_k\\Inbox'
                        )
    def tearDown(self):
        print('Teardown')

    def test_search(self):
        self.ob.search()
        self.assertTrue(len(self.ob.emails))
        