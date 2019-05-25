# GST Categories for ref
GST = [
    ('CGST', 'CGST'),
    ('SGST', 'SGST'),
    ('IGST', 'IGST'),
]

# GST Rates 
GST_RATE = [
    (1, '0%'),
    (2, '5%'),
    (3, '12%'),
    (4, '18%'),
    (5, '28%'),
]

# Invoice customer address
ADDRESS_TYPE = [
    (0, 'Billing'),
    (1, 'Shipping'),
]

# Refill Request
REFILL_REQUEST_TYPE = [
    ('missing', 'missing'),
    ('half-done', 'half-done'),
    ('fulfilled', 'fulfilled'),
]

# New Order Application
ORDER_STATUS = [
    ('unseen', 'unseen'), # haven't opened the path to this order
    ('reviewed', 'reviewed'), # have viewed this order
    ('packing', 'packing'), # products of this order are undergoing packing process
    ('dispatched', 'dispatched'), # products of this order have been dispatched for delivery
    ('delivered', 'delivered'), # products of this order have been delivered
    ('incomplete', 'incomplete'), # products of this package have been half processed
    ('return', 'return'), # products of this order have been returned
]

# Countries
COUNTRIES = [
    ('India', 'India'),
]

# States
STATES = [
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chattisgarh', 'Chattisgarh'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jammu and Kashmir', 'Jammu and Kashmir'),
    ('Jharkhand', 'Jharkhand'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Uttarakhand', 'Uttarakhand'),
    ('West Bengal', 'West Bengal'),
]

# Indian Territories
TERRITORIES = [
    ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
    ('Chadigarh', 'Chadigarh'),
    ('Dadar and Nagar Haveli', 'Dadar and Nagar Haveli'),
    ('Daman and Diu', 'Daman and Diu'),
    ('Delhi', 'Delhi'),
    ('Lakshadweep', 'Lakshadweep'),
    ('Puducherry', 'Puducherry'),
]

# Payment Method
MODE_OF_PAYMENT = [
    (1, 'Cash'),
    (2, 'Card'),
    (3, 'E-Waller'),
]

# Webpage categories for reference to complain
WEBPAGE_REF = [
    ('Dashboard', 'Dashboard'),
    ('Invoice', 'Invoice'),
    ('Customers', 'Customers'),
    ('Manage Orders', 'Manage Orders'),
    ('Inventory', 'Inventory'),
    ('Team', 'Team'),
]

QUANTITY = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4), 
    (5, 5),
    (6, 6),
]

