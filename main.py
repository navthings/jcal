import jax
import jax.numpy as jnp

print("simple calculator using jnp arrays. Type 'q' to quit.")
print("type 'clear' to clear the screen.")
print("enter expressions in the format: a op b (e.g., 2 + 3)")

while True:
    expression = input("> ")

    if expression == "q":
        break
    
    if expression == "clear":
        print("\033c", end="")
        continue

    a, op, b = expression.split()

    a = jnp.array(float(a))
    b = jnp.array(float(b))

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        result = a / b
    else:
        print("unknown operator")
        continue

    print(result)