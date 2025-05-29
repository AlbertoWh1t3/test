from models import Order

def get_orders(session, date_filter=None, name_filter=None, description_filter=None):
    results = session.query_orders()
    if date_filter:
        results = [o for o in results if o.date == date_filter]
    if name_filter:
        results = [o for o in results if name_filter.lower() in o.name.lower()]
    if description_filter:
        results = [o for o in results if description_filter.lower() in o.description.lower()]
    return results

def get_order_by_id(session, order_id):
    for order in session.query_orders():
        if order.id == order_id:
            return order
    return None

def create_order(session, order_data):
    new_id = max([o.id for o in session.query_orders()] + [0]) + 1
    new_order = Order(
        id=new_id,
        name=order_data["name"],
        description=order_data["description"],
        date=order_data["date"],
        products=[]
    )
    session.add_order(new_order)
    session.commit()
    return new_order

def update_order(session, order_id, updated_data):
    order = get_order_by_id(session, order_id)
    if not order:
        return None
    for key, value in updated_data.items():
        setattr(order, key, value)
    session.commit()
    return order

def delete_order(session, order_id):
    order = get_order_by_id(session, order_id)
    if order:
        session.delete_order(order)
        session.commit()
        return order
    return None
