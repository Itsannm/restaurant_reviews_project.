# Yelp-Style Restaurant Review System

This project is a simple implementation of a Yelp-style restaurant review system in Python. It consists of three main classes: `Customer`, `Restaurant`, and `Review`. These classes allow you to manage customers, restaurants, and their associated reviews.

## Table of Contents

- [Getting Started](#getting-started)
- [Usage](#usage)
- [Classes](#classes)
- [Sample Usage](#sample-usage)
- [Contributing](#contributing)


## Getting Started

To get started with this project, you'll need Python installed on your system. You can clone this repository to your local machine and run the Python script.

```bash
git clone https://github.com/yourusername/restaurant-review.git
cd restaurant-review
python restaurant_review.py
```

## Usage

The project provides three main classes:

1. `Customer`: Represents a customer who can write reviews.
2. `Restaurant`: Represents a restaurant that can be reviewed.
3. `Review`: Represents a review written by a customer for a restaurant.

Each class has specific methods to interact with and manage data related to customers, restaurants, and reviews.

## Classes

### `Customer`

- `__init__(self, given_name, family_name)`: Initializes a customer instance with a given name and family name.
- `full_name(self)`: Returns the full name of the customer.
- `num_reviews(self)`: Returns the number of reviews authored by the customer.
- `restaurants(self)`: Returns a list of restaurant names the customer has reviewed.
- `add_review(self, restaurant, rating)`: Adds a review associated with this customer.

### `Restaurant`

- `__init__(self, name)`: Initializes a restaurant instance with a name.
- `average_star_rating(self)`: Calculates and returns the average star rating for the restaurant.
- `customers(self)`: Returns a list of customers who have reviewed the restaurant.

### `Review`

- `__init__(self, customer, restaurant, rating)`: Initializes a review instance with a customer, restaurant, and rating.

## Sample Usage

```python
# Create customer and restaurant instances
customer1 = Customer("John", "Doe")
customer2 = Customer("Lisa", "Achieng")

restaurant1 = Restaurant("Tasty Burger")
restaurant2 = Restaurant("Pizza Palace")

# Add reviews
customer1.add_review(restaurant1, 4)
customer2.add_review(restaurant1, 5)
customer2.add_review(restaurant2, 3)

# Print some results
print(customer1.full_name())
print(customer2.num_reviews())
print(restaurant1.average_star_rating())
```

## Contributing

Contributions are welcome! If you have ideas for improvements or find any issues, please open an issue or create a pull request.

