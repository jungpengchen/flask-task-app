from . import InitTestCase
class TestScenario(InitTestCase):
    def test_list_tasks_after_create(self):
        input_task_name = 'task_name'
        resp = self.client.post('/task', json={'name':input_task_name}, )
        
        expect_code, expect_data = 200, {'result':[{'id':1, 'name':input_task_name, 'status':0}]}
        resp = self.client.get('/tasks')
        self.assertEqual(resp.status_code, expect_code, f'response text is {resp.text}')
        self.assertEqual(resp.json, expect_data)
    def test_update_created_task_status(self):
        input_task_name = 'task_name'
        resp = self.client.post('/task', json={'name':input_task_name}, )
        
        input_task_id = 1
        input_task = {'id': input_task_id, 'name': input_task_name, 'status': 1}
        expect_code, expect_data = 200, {'result': input_task}
        resp = self.client.put(f'/task/{input_task_id}', json=input_task)
        self.assertEqual(resp.status_code, expect_code, f'response text is {resp.text}')
    def test_update_created_task_id(self):
        input_task_name = 'task_name'
        resp = self.client.post('/task', json={'name':input_task_name}, )
        
        input_task_id = 1
        input_new_task_id = 2
        input_task = {'id': input_new_task_id, 'name': input_task_name, 'status': 1}
        expect_code, expect_data = 200, {'result': input_task}
        resp = self.client.put(f'/task/{input_task_id}', json=input_task)
        self.assertEqual(resp.status_code, expect_code, f'response text is {resp.text}')
    def test_list_tasks_after_update(self):
        input_task_name = 'task_name'
        resp = self.client.post('/task', json={'name':input_task_name}, )
        input_task_id = 1
        input_task = {'id': input_task_id, 'name': input_task_name, 'status': 1}
        resp = self.client.put(f'/task/{input_task_id}', json=input_task)

        expect_code, expect_data = 200, {'result':[{'id':1, 'name':input_task_name, 'status':1}]}
        resp = self.client.get('/tasks')
        self.assertEqual(resp.status_code, expect_code, f'response text is {resp.text}')
        self.assertEqual(resp.json, expect_data)
    def test_delete_created_task(self):
        input_task_name = 'task_name'
        resp = self.client.post('/task', json={'name':input_task_name}, )

        input_task_id = 1
        expect_code = 200
        resp = self.client.delete(f'/task/{input_task_id}')
        self.assertEqual(resp.status_code, expect_code, f'response text is {resp.text}')
    def test_list_tasks_after_delete(self):
        input_task_name = 'task_name'
        resp = self.client.post('/task', json={'name':input_task_name}, )
        input_task_id = 1
        resp = self.client.delete(f'/task/{input_task_id}')

        expect_code, expect_data = 200, {'result':[{'id':1, 'name':'name', 'status':0}]}
        resp = self.client.get('/tasks')
        self.assertEqual(resp.status_code, expect_code, f'response text is {resp.text}')
        self.assertEqual(resp.json, expect_data)
    def test_create_after_delete_latest_task(self):
        input_task_name = 'task_name'
        resp = self.client.post('/task', json={'name':input_task_name})
        input_task_id = 1
        resp = self.client.delete(f'/task/{input_task_id}')

        expect_code, expect_data = 201, {'result': {'id': input_task_id, 'name': input_task_name, 'status': 0}}
        resp = self.client.post('/task', json={'name':input_task_name})
        self.assertEqual(resp.status_code, expect_code, f'response text is {resp.text}')