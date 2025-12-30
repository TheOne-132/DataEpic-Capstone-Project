# Smart Inventory Management System 🛒

## Capstone Project Overview

This project demonstrates core Object-Oriented Programming (OOP) principles in Python through a **Smart Inventory Management System** for an online store that sells both **physical** and **digital** products.

### Key OOP Concepts Demonstrated
- **Inheritance** – `PhysicalProduct` and `DigitalProduct` inherit from abstract base `Product`
- **Polymorphism** – `get_total_price(quantity)` behaves differently based on product type
- **Abstraction** – Abstract base class `Product` enforces a contract via `@abstractmethod`
- **Encapsulation** – Protected attributes `_name` and `_price`
- **Composition** – `Order` class contains a list of products
- **Modularization** – Clean package structure with separate modules

### Product Types
- **Physical Goods** (e.g., laptops): Include shipping cost (₦200 per kg) and weight tracking
- **Digital Goods** (e.g., e-books): No shipping cost, infinite stock, include download link

## Project Structure
smart_inventory_project/
├── main.py                  # Entry point – Interactive store simulator
├── README.md                # This file
└── store/
    ├── init.py          # Makes 'store' a Python package
    ├── models.py            # Product, PhysicalProduct, DigitalProduct classes
    └── operations.py        # Order class with cart and checkout logic


## Features 

This implementation goes **beyond** the basic requirements with:

- Fully **interactive console interface**
- Add any number of products dynamically
- Input validation (prices, quantities, weights, links)
- **Grouped receipt** separating Physical and Digital products
- Shipping cost clearly shown for physical items
- **Download links displayed** for digital products after purchase
- Clean, professional receipt formatting

## How to Run

1. Make sure you have **Python 3.1+** installed
2. Open the project folder in VS Code (or any editor)
3. Open a terminal in the project root (where `main.py` is located)
4. Run the program:
    (```bash
           python main.py)
6. Follow the prompts:
- Type yes to add a product
- Enter name, price, quantity, type (p for physical, d for digital)
- For physical: enter weight (kg)
- For digital: enter download link
- Type done when finished shopping
6. View your formatted receipt with grouped items and totals!


## Author - Adewale Victor
## DataEpic Cohort 4 Capstone Project
