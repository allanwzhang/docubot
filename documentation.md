# API Documentation

## Endpoint: /users
- **GET**: Retrieve a list of users.
 - Parameters:
 - `page` (integer): The page number for pagination.
 - `per_page` (integer): Number of items to return per page.
- **POST**: Create a new user.
 - Parameters:
 - `username` (string): Unique username for the user.
 - `email` (string): User's email address.
 - `password` (string): Password for the user account.
- **PUT**: Update user information.
 - Parameters:
 - `user_id` (integer): Unique ID of the user to update.
 - `updates` (object): An object containing fields to update (e.g., `username`, `email`).

## Endpoint: /products
- **GET**: Fetch a list of products.
 - Parameters:
 - `category` (string): Filter products by category.
 - `price_range` (object): An object with `min` and `max` values to filter by price.
- **POST**: Add a new product.
 - Parameters:
 - `product_name` (string): Name of the product.
 - `description` (string): Description of the product.
 - `price` (float): Price of the product.
 - `categories` (array): Array of category strings.

## Endpoint: /orders
- **GET**: Retrieve all orders.
 - Parameters:
 - `status` (string): Filter orders by status (e.g., "pending", "shipped").
- **POST**: Create a new order.
 - Parameters:
 - `user_id` (integer): ID of the user placing the order.
 - `order_items` (array): Array of objects containing `product_id` and `quantity`.
- **PATCH**: Update order status.
 - Parameters:
 - `order_id` (integer): ID of the order to update.
 - `status` (string): New status for the order.

## Endpoint: /authentication
- **POST**: User login.
 - Parameters:
 - `username_or_email` (string): Username or email address for login.
 - `password` (string): Password for authentication.
- **DELETE**: Logout and revoke access token.
 - Parameters: None.

## Endpoint: /reviews
- **POST**: Submit a product review.
 - Parameters:
 - `product_id` (integer): ID of the product being reviewed.
 - `user_id` (integer): ID of the reviewer.
 - `rating` (integer): Rating given by the user (1-5).
 - `comment` (string): Optional comment from the reviewer.
