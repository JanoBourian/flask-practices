from unittest import TestCase
from models.StoreModel import StoreModel
from db import db
from app import app 
import json

class BaseTest(TestCase):
    def setUp(self):
        # Make sure database exists
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        with app.app_context():
            db.init_app(app)
            db.create_all()
        # Get a test client
        self.app = app.test_client() 
        self.app_context = app.app_context
    
    def tearDown(self):
        # Database is blank
        with app.app_context():
            db.session.remove()
            db.drop_all()   

class TestStore(BaseTest):
    def test_crud_store(self):
        name = 'test'
        description = 'description test'
        with self.app_context():
            store = StoreModel(name, description)
            self.assertIsNone(StoreModel.find_by_name(name))
            store.add_to_database()
            self.assertIsNotNone(StoreModel.find_by_name(name))
            store.delete_to_database(name)
            self.assertIsNone(StoreModel.find_by_name(name))
        
    # def setUp(self):
    #     self.name = "Test"
    #     self.message_creation = {'message': f"Store {self.name} added to database"}
        
    # def test_post_store(self):
    #     with self.app_context() as c:
    #         req = c.post(f'/store/{self.name}')
    #         self.assertEqual(req.status_code, 201)
    #         self.assertEqual(json.loads(req.get_data()),self.message_creation)
    
    # def test_get_store(self):
    #     with app.test_client() as c: 
    #         req = c.get(f"/store/{self.name}")
    #         self.assertEqual(req.status_code, 200)
    #         self.assertEqual(json.loads(req.get_data()), self)
