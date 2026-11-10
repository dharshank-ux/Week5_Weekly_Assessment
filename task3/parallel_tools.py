import asyncio

orders = {
    1001: {"status": "Shipped", "item": "Laptop"},
    1002: {"status": "Processing", "item": "Mobile"}
}

customers = {
    5: {"name": "Arun", "city": "Chennai"}
}

async def get_order_status(order_id: int):
    await asyncio.sleep(1)
    return orders.get(order_id, "Order not found")

async def get_customer(customer_id: int):
    await asyncio.sleep(1)
    return customers.get(customer_id, "Customer not found")

async def main():
    print("Checking orders 1001 and 1002 and customer 5...")

    results = await asyncio.gather(
        get_order_status(1001),
        get_order_status(1002),
        get_customer(5)
    )

    print("Order 1001:", results[0])
    print("Order 1002:", results[1])
    print("Customer 5:", results[2])

asyncio.run(main())