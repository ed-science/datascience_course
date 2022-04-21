results = []
for x in data:
    y = delayed(double)(x) if is_even(x) else delayed(inc)(x)
    results.append(y)

total = delayed(sum)(results)