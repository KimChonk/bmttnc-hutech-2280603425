print("Enter text (type 'done' to finish):")
line = []
while True:
    text = input()
    if text == 'done':
        break
    line.append(text.upper())
print("Output:")
for i in line:
    print(i.upper())
