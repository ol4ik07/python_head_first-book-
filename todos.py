todos=open('todos.txt','a')
print('put out the trash', file=todos)
print('fee the cat', file=todos)
print('prepare tax return', file=todos)
todos.close()
tasks=open('todos.txt')
for chore in tasks:
    print(chore)

tasks.close()