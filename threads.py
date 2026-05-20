import threading as t
"""
#Singlr level Thread
def ebook(n):
    print("Book Name:",n)
ebook("learn java")
t1=t.Thread(target=ebook,args=("Learn python",))
t1.start()

#multi level thread
def ebook(n):
    print("Book Name:",n)
def author(n):
    print("author Name:",n)

t1=t.Thread(target=ebook,args=("Learn python",))
t2=t.Thread(target=author,args=("praveen",))
t1.start()
t1.join()
t2.start()
t2.join()
"""
#Doemon thread
def ebook(n):
    print("Book Name:",n)
t1=t.Thread(target=ebook,args=("Learn python",))
t1.setDaemon(True)
print(t1.isDaemon)
t1.start()
t1.join

