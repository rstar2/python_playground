import threading
import time

print('Start of program.')


def takeANap():
    time.sleep(5)
    print('Wake up!')


threadObj = threading.Thread(target=takeANap)
threadObj.start()

print('End of program.')

# Passing Arguments to the Thread’s Target Function
#  in order to pass use in new thread a function with params, like :
# print('Cats', 'Dogs', 'Frogs', sep=' & ')
# have to pass kwargs={'sep': ' & '}

threadObj2 = threading.Thread(target=print,
                              args=['Cats', 'Dogs', 'Frogs'],
                              kwargs={'sep': ' & '})
threadObj2.start()

#  ---------------------
# Another way is to extend the threading.Thread class and start it like that

class AsyncThread(threading.Thread):
    def run(self):
        pass
AsyncThread().start()
