from unittest import TestCase
from models.StoreModel import StoreModel
from models.ItemModel import ItemModel
from models.UserModel import UserModel
from db import db
from app import app 
import json

class BaseTest(TestCase):
    @classmethod
    def setUpClass(cls):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        with app.app_context():
            db.init_app(app)        
    
    def setUp(self):
        # Make sure database exists
        with app.app_context():
            db.create_all()
        # Get a test client
        self.app = app.test_client
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
    
    def test_crud_item(self):
        store_name = "Store Test"
        description = "Test Lorem Ipsum"
        item_sku ="9895956996"
        item_name = "Test Item"
        item_price = 9.99
        with self.app_context():
            store = StoreModel(store_name, description)
            store.add_to_database()
            item = ItemModel(item_sku, item_name, item_price, store.id)
            self.assertIsNone(ItemModel.find_by_name(item.name))
            item.add_to_database()
            self.assertIsNotNone(ItemModel.find_by_name(item.name))
            item.delete_to_database(item.name)
            self.assertIsNone(ItemModel.find_by_name(item.name))
            store.delete_to_database(store.name)
            self.assertIsNone(StoreModel.find_by_name(store.name))
    
    def test_relationships(self):
        store_name = "Store Test"
        description = "Test Lorem Ipsum"
        item_sku ="9895956996"
        item_name = "Test Item"
        item_price = 9.99
        with self.app_context():
            store = StoreModel(store_name, description)
            store.add_to_database()
            item = ItemModel(item_sku, item_name, item_price, store.id)
            item.add_to_database()
            self.assertEqual(item.store.name, store.name)
            self.assertEqual(item.store_id, store.id)
            self.assertListEqual(store.items.all(), [item])
            self.assertEqual(store.items.count(), 1)
            self.assertEqual(store.items.first().name, item.name)
    
    def test_create_store(self):
        name = 'test'
        description = 'description test'
        with self.app_context():
            store = StoreModel(name, description)
            self.assertListEqual(store.items.all(), [])
    
    def test_only_create_user(self):
        name = 'username'
        password = 'password'
        user = UserModel(username=name, password=password)
        self.assertEqual(user.username, name, "In UserModel username is incorrect")
        self.assertEqual(user.password, password, "In UserModel password is incorrect")
    
    def test_crud_user(self):
        name = 'user_test'
        password = 'password'
        with self.app_context():
            user = UserModel(username=name, password=password)
            # validate user is not in db 
            self.assertIsNone(UserModel.find_by_username(user.username))
            # add user user in db
            user.add_to_database()
            # validate user is in db
            self.assertIsNotNone(UserModel.find_by_username(user.username))
            # delete user in db
            user.delete_to_database(user.username)
            # validate user is not in db
            self.assertIsNone(UserModel.find_by_username(user.username))
        
    def test_register_user(self):
        username = 'test9090'
        password = '123456'
        with self.app() as client:
            with self.app_context():
                response = client.post('/register', data ={'username':username, 'password':password})
                self.assertEqual(response.status_code, 201)
                self.assertIsNotNone(UserModel.find_by_username(username))
                self.assertDictEqual({'message': f"{username} added to database"}, json.loads(response.data))
                
    
    def test_register_and_login(self):
        username = 'test9090'
        password = '123456'
        with self.app() as client:
            with self.app_context():
                client.post('/register', data ={'username':username, 'password':password})
                auth_response = client.post('/auth', 
                                           data =json.dumps({'username':username, 'password':password}),
                                           headers = {'Content-Type': 'application/json'})
                self.assertIn('access_token', json.loads(auth_response.data).keys())
    
    def test_register_duplicate_user(self):
        username = 'test9090'
        password = '123456'
        with self.app() as client:
            with self.app_context():
                client.post('/register', data ={'username':username, 'password':password})
                response = client.post('/register', data ={'username':username, 'password':password})
                self.assertEqual(response.status_code, 404)
                self.assertEqual({"error": f"{username} already exists"}, json.loads(response.data))
        
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
