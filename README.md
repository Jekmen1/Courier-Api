Courier Delivery Service API
Description
The Courier Delivery Service API provides a RESTful interface for managing and tracking parcel deliveries. Users can register, create parcels, assign couriers, track parcel status, and confirm delivery. Built using Django and Django Rest Framework, the API offers secure authentication via JWT with djangorestframework-simplejwt and documentation using Swagger with DRF YASG. PostgreSQL is used for development purposes.

Installation
To set up the Courier Delivery Service API, follow these steps:

Install Django and Dependencies:

bash
Copy code
pip install Django djangorestframework django-filter django-templated-mail djangorestframework-simplejwt drf-yasg
Initialize Django Project:

bash
Copy code
django-admin startproject courier_api
Configure Database:
Update the DATABASES settings in courier_api/settings.py to use PostgreSQL or your preferred database.

Usage
To utilize the Courier Delivery Service API, follow these instructions:

Register a User:

Create a new user account by sending a POST request to /api/users/ with the required fields: username, email, password, and role (Customer, Courier, or Admin).
Obtain JWT Token:

After registering or logging in, obtain a JWT token by sending a POST request to /api/token/ with the user's credentials (username and password) in the request body.
Refresh JWT Token (Optional):

If the JWT token expires, refresh it by sending a POST request to /api/token/refresh/ with the expired token in the request body.
Parcel Management:

Create a new parcel: Send a POST request to /api/parcels/ with parcel details including title, description, receiver_name, and receiver_address.
Retrieve parcel details: Send a GET request to /api/parcels/<id>/ to get details of a specific parcel by its ID.
Update parcel details: Send a PUT request to /api/parcels/<id>/ with updated parcel details to modify an existing parcel.
Delete a parcel: Send a DELETE request to /api/parcels/<id>/ to remove a parcel from the system.
Courier Parcel Assignment:

List parcels assigned to the logged-in courier: Send a GET request to /api/courier/ to view parcels assigned to the logged-in courier.
Parcel Status Update & Delivery Proof:

Update parcel status: Send a PUT request to /api/parcels/<id>/ with updated status to change the status of a parcel (e.g., from "Pending" to "In Transit" or "Delivered").
Upload delivery proof: Send a POST request to /api/parcels/<id>/delivery_proof/ with the parcel ID and delivery proof image to provide confirmation of parcel delivery.

API Documentation:
/api/users/ (GET, POST): User registration and listing.
/api/token/ (POST): Obtain JWT token.
/api/token/refresh/ (POST): Refresh JWT token.
/api/parcels/ (GET, POST): List all parcels and create a new parcel.
/api/parcels/<id>/ (GET, PUT, DELETE): Retrieve, update, and delete parcel details.
/api/parcels/<id>/delivery_proof/ (POST): Upload image proof of delivery.
/api/courier/ (GET): List parcels assigned to the logged-in courier.

Contact:
For questions, suggestions, or feedback, please contact us at jekokobakidze@gmail.com.
