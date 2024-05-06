Courier Delivery Service API
Description
The Courier Delivery Service API provides a RESTful interface for managing and tracking parcel deliveries. Users can register, create parcels, assign couriers, track parcel status, and confirm delivery. Built using Django and Django Rest Framework, the API offers secure authentication via JWT with djangorestframework-simplejwt and documentation using Swagger with DRF YASG. PostgreSQL is used for development purposes.


API Documentation:
/api/users/ (GET, POST): User registration and listing.

/api/token/ (POST): Obtain JWT token.
/api/token/refresh/ (POST): Refresh JWT token.

/api/parcels/ (GET, POST): List all parcels and create a new parcel.
/api/parcels/<id>/ (GET, PUT, DELETE): Retrieve, update, and delete parcel details.

/api/courier/ (GET): List parcels assigned to the logged-in courier.

Contact:
For questions, suggestions, or feedback, please contact us at jekokobakidze@gmail.com.
