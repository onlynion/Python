dt = {"a": "A", "b": "B", "c": "C", "d": "D"}
print(dt)

dt[(1, 2, 3)] = "tuple"
print(dt)

# number, string, tuple dictionary তে key হিসেবে ব্যাবহার করযা যাবে কারণ এগুলা imutable অর্থাৎ এদেরকে পরিভর্তন করা যায় কিন্তু list, set এগুলা কে Key হিসেবে ব্যাবহার করা যাবে না কারণ এগুলা mutable অর্থাৎ এগুলা পরিবর্তন করা যায় 