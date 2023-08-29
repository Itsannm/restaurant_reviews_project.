# Define the Customer class
class Customer:
    # Class-level list to store all customer instances
    customers = []

    # Constructor to initialize a Customer instance with given_name and family_name
    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.reviews = []  # List to store reviews associated with this customer
        Customer.customers.append(self)  # Add the customer to the class-level list

    # Method to return the full name of the customer
    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    # Method to return the number of reviews authored by the customer
    def num_reviews(self):
        return len(self.reviews)

    # Method to return a list of restaurant names the customer has reviewed
    def restaurants(self):
        reviewed_restaurants = set()
        for review in self.reviews:
            reviewed_restaurants.add(review.restaurant.name)  # Modify to return restaurant names
        return list(reviewed_restaurants)

    # Method to add a review associated with this customer
    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        self.reviews.append(review)


# Define the Restaurant class
class Restaurant:
    # Class-level list to store all restaurant instances
    restaurants = []

    # Constructor to initialize a Restaurant instance with a name
    def __init__(self, name):
        self.name = name
        self.reviews = []  # List to store reviews associated with this restaurant
        Restaurant.restaurants.append(self)  # Add the restaurant to the class-level list

    # Method to calculate and return the average star rating for the restaurant
    def average_star_rating(self):
        if not self.reviews:
            return 0
        total_rating = sum(review.rating for review in self.reviews)
        return total_rating / len(self.reviews)

    # Method to return a list of customers who have reviewed the restaurant
    def customers(self):
        reviewing_customers = set()
        for review in self.reviews:
            reviewing_customers.add(review.customer)
        return list(reviewing_customers)


# Define the Review class
class Review:
    # Class-level list to store all review instances
    reviews = []

    # Constructor to initialize a Review instance with a customer, restaurant, and rating
    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.reviews.append(self)  # Add the review to the class-level list

# Test sample data
customer1 = Customer("John", "Doe")
customer2 = Customer("Lisa", "Achieng")

restaurant1 = Restaurant("Tasty Burger")
restaurant2 = Restaurant("Pizza Palace")

customer1.add_review(restaurant1, 4)
customer2.add_review(restaurant1, 5)
customer2.add_review(restaurant2, 3)


print(customer1.full_name())
print(customer2.num_reviews())
print(restaurant1.average_star_rating())
print([customer.full_name() for customer in Customer.customers])
print([restaurant.name for restaurant in Restaurant.restaurants])
print([review.rating for review in Review.reviews])
