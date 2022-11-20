from . import InitTestCase
class TestRoute(InitTestCase):
    def test_list_tasks_before_create(self):
        expect_code, expect_data = 200, {'result':[{'id':1, 'name':'name', 'status':0}]}
        resp = self.client.get('/tasks')
        self.assertEqual(resp.status_code, expect_code, f'response text is {resp.text}')
        self.assertEqual(resp.json, expect_data)
    def test_create_task(self):
        input_task_name = 'task_name'
        expect_code, expect_data = 201, {'result':{'id':1, 'name':input_task_name, 'status':0}}
        resp = self.client.post('/task', json={'name':input_task_name}, )
        self.assertEqual(resp.status_code, expect_code, f'response text is {resp.text}')
        self.assertEqual(resp.json, expect_data)
    def test_update_uncreated_task(self):
        input_task_id = 2
        input_task = {'id': input_task_id, 'name': 'task_name', 'status': 1}
        expect_code = 404
        resp = self.client.put(f'/task/{input_task_id}', json=input_task)
        self.assertEqual(resp.status_code, expect_code, f'response text is {resp.text}')
    def test_delete_uncreated_task(self):
        input_task_id = 2
        input_task = {'id': input_task_id, 'name': 'task_name', 'status': 1}
        expect_code = 404
        resp = self.client.delete(f'/task/{input_task_id}', json=input_task)
        self.assertEqual(resp.status_code, expect_code, f'response text is {resp.text}')