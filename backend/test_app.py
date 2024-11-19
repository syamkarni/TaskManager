import unittest
import warnings
from main import app, db, Task

class TaskManagerTestCase(unittest.TestCase):
    def setUp(self):
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        warnings.filterwarnings("ignore", message=".*datetime.datetime.utcnow.*")
        warnings.filterwarnings("ignore", message=".*Query.get.*")

        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.drop_all()

    def test_create_task(self):
        response = self.client.post(
            '/tasks',
            json={
                "title": "Test Task",
                "description": "This is a test task.",
                "due_date": "2024-12-31"
            },
            headers={"Authorization": "Bearer mysecrettoken"}
        )
        self.assertEqual(response.status_code, 201)

    def test_get_tasks(self):
        self.client.post(
            '/tasks',
            json={
                "title": "Test Task",
                "description": "This is a test task.",
                "due_date": "2024-12-31"
            },
            headers={"Authorization": "Bearer mysecrettoken"}
        )
        response = self.client.get('/tasks', headers={"Authorization": "Bearer mysecrettoken"})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json) > 0)

    def test_mark_complete(self):
        response = self.client.post(
            '/tasks',
            json={
                "title": "Test Task",
                "description": "This is a test task.",
                "due_date": "2024-12-31"
            },
            headers={"Authorization": "Bearer mysecrettoken"}
        )
        task_id = response.json["task_id"]
        response = self.client.patch(
            f'/tasks/{task_id}/complete', headers={"Authorization": "Bearer mysecrettoken"}
        )
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TaskManagerTestCase)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
