from concurrent.futures import ThreadPoolExecutor as Pool
from flask_testing import LiveServerTestCase
import server, requests
class TestMultithread(LiveServerTestCase):
    def create_app(self):
        server.app.config['TESTING'] = True
        server.app.config['LIVESERVER_PORT'] = 8080
        return server.app
    def setUp(self):
        server.init_task_list()
    def test_create_100_tasks_concurrency(self):
        input_task_name = 'task_name'
        thread_counts = 100
        url = self.get_server_url()
        client = requests

        def return_status_code(task_seq):
            resp = client.post(f'{url}/task', json={'name': f'{input_task_name}-{task_seq}'})
            return resp.status_code

        expect_status_code_dict = {201: thread_counts}
        resp_status_code_dict  = {}
        with Pool(max_workers=thread_counts) as pool:
            result = pool.map(return_status_code, [i for i in range(1,thread_counts+1)])
        for resp_status_code in result:
            if resp_status_code in resp_status_code_dict:
                resp_status_code_dict[resp_status_code] += 1
            else:
                resp_status_code_dict[resp_status_code] = 1
        self.assertEqual(resp_status_code_dict, expect_status_code_dict)

        resp = client.get(f'{url}/tasks')
        resp_task_list = resp.json()['result']
        resp_task_id_set = set(t['id'] for t in resp_task_list)
        expect_task_id_set = set(i for i in range(1, thread_counts+1))
        self.assertEqual(len(resp_task_list), thread_counts)
        self.assertEqual(resp_task_id_set, expect_task_id_set)
