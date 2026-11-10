# Week 5 - Task 3: Parallel Tool Calling and Memory

## Completed Tasks

- Parallel tool execution using asyncio.gather()
- Order status checking
- Customer information retrieval
- Handling unknown order errors
- Handling invalid arguments
- Handling nonexistent tools
- Saving conversation history in JSON
- Retrieving user information from conversation history

## Parallel Tool Calling

Independent tools run concurrently using asyncio.gather().

## Error Handling

Four test cases are demonstrated:
1. Valid order
2. Unknown order
3. Invalid argument
4. Nonexistent tool

## Conversation Memory

Conversation messages are saved in conversation.json.
The program retrieves the user's name from saved history.