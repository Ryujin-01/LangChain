from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

saved_history = [
    HumanMessage(content="Hi, I placed an order three days ago and it still says 'Processing'. My order number is #88492."),
    AIMessage(content="Hello! I apologize for the wait. Let me check on Order #88492 for you. It looks like the mechanical keyboard you ordered was briefly out of stock, but the shipment just arrived at our warehouse."),
    HumanMessage(content="Oh, okay. Will it still arrive before my brother's birthday on Friday?"),
    AIMessage(content="Yes! Because of the delay, I have upgraded your shipping to Overnight Express at no extra charge. It will be delivered on Thursday afternoon."),
    HumanMessage(content="That is amazing, thank you so much! What carrier will be delivering it?")
]