# Library Project

This project implements a library management system with books, users, borrowings, and authentication.

---

## Completed Tasks

### 1. Implement CRUD functionality for Books Service
- Initialized the `books` app.
- Added the `Book` model with fields: `title`, `author`, `cover`, `inventory`, `daily_fee`.
- Implemented serializers and views for all CRUD endpoints for books.

### 2. Add permissions to Books Service
- Only admin users can create, update, or delete books.
- All users (including unauthenticated) can list books.
- Used JWT token authentication from the users service.

### 3. Implement CRUD for Users Service
- Initialized the `users` app.
- Added custom user model with email as the `USERNAME_FIELD`.
- Added JWT authentication support with a custom `Authorize` header for better integration with ModHeader Chrome extension.
- Implemented serializers and views for user registration and management.

### 4. Implement Borrowing List & Detail endpoints
- Initialized the `borrowings` app.
- Created `Borrowing` model with constraints on `borrow_date`, `expected_return_date`, and `actual_return_date`.
- Implemented a read serializer including detailed book info.
- Created list and detail endpoints for borrowings.

### 5. Implement Create Borrowing endpoint
- Implemented a serializer for borrowing creation.
- Validated that the book inventory is not zero.
- Decreased book inventory by 1 when borrowing is created.
- Automatically attached the current authenticated user to the borrowing.
- Created the endpoint for borrowing creation.

### 6. Add filtering for Borrowings List endpoint
- Ensured non-admin users can only see their own borrowings.
- Allowed access only to authenticated users.
- Added `is_active` filter to show only active borrowings (not yet returned).
- Added `user_id` filter for admin users to filter borrowings by specific users.

### 7. Implement return Borrowing functionality
- Prevented returning a borrowing more than once.
- Increased book inventory by 1 on returning a borrowing.
- Added a dedicated endpoint for returning a borrowing.

### 8. Implement sending notifications on Borrowing creation
- Set up Telegram bot and chat for notifications (private keys managed securely).
- Created a helper function to send messages via Telegram API.
- Integrated notification sending on new borrowing creation with detailed borrowing info.

---

## Technologies Used
- Django 5.2
- Django REST Framework
- Simple JWT Authentication
- SQLite (default DB)
- Telegram Bot API for notifications

---

## How to Run
1. Clone the repository.
2. Create and activate a virtual environment.
3. Install requirements: `pip install -r requirements.txt`
4. Configure `.env` file with necessary secrets (e.g., Telegram bot token).
5. Run migrations: `python manage.py migrate`
6. Run the server: `python manage.py runserver`

---

## Notes
- JWT Authentication uses the custom header `Authorize` for better frontend compatibility.
- Borrowing creation reduces book inventory and sends a notification.
- Return borrowing endpoint ensures data integrity by disallowing double returns.

