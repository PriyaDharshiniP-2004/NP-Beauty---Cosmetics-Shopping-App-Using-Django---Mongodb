# NP Beauty - Cosmetics Shopping App

NP Beauty is an online cosmetics shopping application developed using **Django** for the frontend and backend and **MongoDB** for the database. The platform allows users to browse various cosmetic products, add them to their wishlist and cart, and place orders seamlessly.

## Features

- **User Authentication**: Sign up and log in functionality.
- **Product Listing**: Browse a variety of cosmetic products.
- **Wishlist**: Save favorite products for later.
- **Shopping Cart**: Add products to the cart before checkout.
- **Order Placement**: Users can place an order after adding products to the cart.

## Technologies Used

- **Backend**: Django (Python)
- **Database**: MongoDB
- **Frontend**: Django Templates, HTML, CSS, JavaScript
- **Authentication**: Django Authentication System

## Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/np-beauty.git
   cd np-beauty
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure MongoDB connection in `settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'djongo',
           'NAME': 'np_beauty_db',
           'CLIENT': {
               'host': 'your_mongodb_connection_string',
           }
       }
   }
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Start the Django development server:
   ```bash
   python manage.py runserver
   ```

7. Open the browser and visit:
   ```
   http://127.0.0.1:8000/
   ```

## Usage

1. **Sign Up / Login**: Create an account and log in.
2. **Browse Products**: View different cosmetics available.
3. **Add to Wishlist**: Save items to wishlist.
4. **Add to Cart**: Move items from wishlist to cart or add directly.
5. **Place Order**: Checkout and confirm your order.


## Contact

For any queries, feel free to reach out:
- Email: priyad109615@gmail.com
- GitHub: https://github.com/PriyaDharshiniP-2004

