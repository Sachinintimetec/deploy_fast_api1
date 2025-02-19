import random
from faker import Faker

# Initialize Faker instance
fake = Faker()

# Function to generate mock data with confidence levels
def generate_w9_mock_data() -> dict:
    return {
        'name': {'value': fake.name(), 'confidence': round(random.uniform(0.8, 1.0), 2)},
        'business_name': {'value': fake.company(), 'confidence': round(random.uniform(0.8, 1.0), 2)},
        'address': {'value': fake.street_address(), 'confidence': round(random.uniform(0.8, 1.0), 2)},
        'city': {'value': fake.city(), 'confidence': round(random.uniform(0.8, 1.0), 2)},
        'state': {'value': fake.state_abbr(), 'confidence': round(random.uniform(0.8, 1.0), 2)},
        'zip': {'value': fake.zipcode(), 'confidence': round(random.uniform(0.8, 1.0), 2)},
        'ssn': {'value': fake.ssn(), 'confidence': round(random.uniform(0.8, 1.0), 2)},
        'supplier_name': {'value': fake.name(), 'confidence': round(random.uniform(0.8, 1.0), 2)},
        'requested_supplier': {'value': 'Asset Services', 'confidence': round(random.uniform(0.8, 1.0), 2)},
        'service_agreement':  {'value': True, 'confidence': round(random.uniform(0.8, 1.0), 2)},
        'indicate_supplier':  {'value':'Supplier is also a client', 'confidence': round(random.uniform(0.8, 1.0), 2)},
        'ein': {'value': f"{random.randint(10, 99)}-{random.randint(1000000, 9999999)}", 'confidence': round(random.uniform(0.8, 1.0), 2)},
        'signature': {'value': fake.name(), 'confidence': round(random.uniform(0.8, 1.0), 2)},
        'date': {'value': fake.date_this_year().strftime('%m/%d/%Y'), 'confidence': round(random.uniform(0.8, 1.0), 2)},
    }
