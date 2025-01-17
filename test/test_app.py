import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app, db, Bank, Branch

class FlaskAppTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up the test environment before running tests."""
        cls.client = app.test_client()
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Saikrishna2005@localhost:5432/bankdb'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        with app.app_context():
            db.create_all()

            test_bank = Bank(name="Test Bank")
            db.session.add(test_bank)
            db.session.commit()

            test_branch = Branch(
                branch="Main Branch", 
                address="Test Address", 
                city="Test City", 
                district="Test District", 
                state="Test State", 
                bank_id=test_bank.id, 
                ifsc="SBIN0001"
            )
            db.session.add(test_branch)
            db.session.commit()

    @classmethod
    def tearDownClass(cls):
        """Clean up after all tests have run."""
        with app.app_context():
            db.drop_all()

    def test_home(self):
        """Test the home route."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("message", data)
        self.assertEqual(data["message"], "Welcome to the Bank API!")

    def test_get_branch_details(self):
        """Test the /api/branches/branch route with parameters."""
        response = self.client.get('/api/branches/branch', query_string={'ifsc': 'SBIN0001'})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('branch', data)

    def test_branch_not_found(self):
        """Test the case when a branch is not found."""
        response = self.client.get('/api/branches/branch', query_string={'ifsc': 'INVALID123'})
        self.assertEqual(response.status_code, 404)
        data = response.get_json()
        self.assertEqual(data['error'], 'Branch not found')

if __name__ == '__main__':
    unittest.main()
