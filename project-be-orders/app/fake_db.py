from datetime import date
from models import Order, Product

class FakeSession:
    def __init__(self):
        # Popoliamo i dati in memoria
        self.orders = [
            Order(
                id=1, name="Ordine A", description="Descrizione ordine A", date=date(2025, 5, 20),
                products=[
                    Product(id=1, name="Prodotto 1", order_id=1),
                    Product(id=2, name="Prodotto 2", order_id=1)
                ]
            ),
            Order(
                id=2, name="Ordine B", description="Descrizione ordine B", date=date(2025, 5, 25),
                products=[
                    Product(id=3, name="Prodotto 3", order_id=2)
                ]
            ),
            Order(
                id=3, name="Ordine C", description="Descrizione ordine C", date=date(2025, 6, 1),
                products=[]
            )
        ]

    def query_orders(self):
        # Simula session.query(Order)
        return self.orders

    def add_order(self, order):
        self.orders.append(order)

    def commit(self):
        pass  # Non fa nulla, simulazione

    def delete_order(self, order):
        self.orders.remove(order)
