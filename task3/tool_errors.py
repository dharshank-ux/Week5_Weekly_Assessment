def get_order_status(order_id):
    orders = {
        1001: "Shipped",
        1002: "Processing"
    }

    if not isinstance(order_id, int):
        return {"error": "Invalid order ID"}

    if order_id not in orders:
        return {"error": f"Order {order_id} not found"}

    return {"order_id": order_id, "status": orders[order_id]}


def get_customer(customer_id):
    customers = {
        5: "Arun"
    }

    if customer_id not in customers:
        return {"error": "Customer not found"}

    return {"customer_id": customer_id, "name": customers[customer_id]}


def main():
    print("TEST 1: Valid order")
    print(get_order_status(1001))

    print("\nTEST 2: Unknown order")
    print(get_order_status(9999))

    print("\nTEST 3: Invalid argument")
    print(get_order_status("abc"))

    print("\nTEST 4: Nonexistent tool")
    tool_name = "get_unknown_tool"

    if tool_name != "get_order_status" and tool_name != "get_customer":
        print({"error": f"Tool '{tool_name}' does not exist"})


if __name__ == "__main__":
    main()