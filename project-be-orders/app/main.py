from fake_db import FakeSession
import views
from datetime import date

def main():
    session = FakeSession()

    # 1. Order Viewing Page
    views.order_viewing_page(session, {"date": date(2025, 5, 25), "name": "Ordine", "description": ""})

    # 2. Detailed Order View
    views.detailed_order_view(session, 2)

    # 3. Order Management
    # Creazione
    views.order_management(session, "create", {
        "name": "Ordine D",
        "description": "Descrizione ordine D",
        "date": date(2025, 6, 10)
    })
    # Modifica
    views.order_management(session, "update", {
        "id": 2,
        "name": "Ordine B Modificato",
        "description": "Nuova descrizione",
        "date": date(2025, 5, 25)
    })
    # Cancellazione
    views.order_management(session, "delete", {"id": 1})

if __name__ == "__main__":
    main()
