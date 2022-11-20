from flask_testing import TestCase
import server
class InitTestCase(TestCase):
    def create_app(self):
        server.app.config['TESTING'] = True
        return server.app
    def setUp(self):
        server.init_task_list()