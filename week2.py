import os


# random testing the os.walk() method to learn about it
tree = []
exclude = ['env', '.git']
for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if d not in exclude]
    tree.append(root)
    for f in files:
        tree.append(os.path.join(root, f))

for x in tree:
    print(x)