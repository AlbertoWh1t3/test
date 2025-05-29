import repository

def search_orders(session, filters):
    return repository.get_orders(
        session,
        date_filter=filters.get("date"),
        name_filter=filters.get("name"),
        description_filter=filters.get("description")
    )

def get_order_details(session, order_id):
    return repository.get_order_by_id(session, order_id)

def manage_order(session, action, data):
    if action == "create":
        return repository.create_order(session, data)
    elif action == "update":
        return repository.update_order(session, data["id"], data)
    elif action == "delete":
        return repository.delete_order(session, data["id"])
    else:
        raise ValueError("Azione non supportata")
