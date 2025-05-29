import services

def order_viewing_page(session, filters):
    orders = services.search_orders(session, filters)
    print("\n--- Order Viewing Page ---")
    for o in orders:
        print(f"ID: {o.id}, Nome: {o.name}, Data: {o.date}, Descrizione: {o.description}")

def detailed_order_view(session, order_id):
    order = services.get_order_details(session, order_id)
    if order:
        print(f"\n--- Dettaglio Ordine #{order.id} ---")
        print(f"Nome: {order.name}")
        print(f"Descrizione: {order.description}")
        print(f"Data: {order.date}")
        print("Prodotti:")
        for p in order.products:
            print(f" - {p.name}")
    else:
        print("Ordine non trovato.")

def order_management(session, action, data):
    result = services.manage_order(session, action, data)
    print(f"\n--- Order Management ({action}) ---")
    if result:
        print("Operazione riuscita:", result)
    else:
        print("Operazione fallita.")
