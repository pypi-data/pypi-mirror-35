[0]

repeat = range(4)
input: for_each='repeat'

task: concurrent=True

import time
print('I am {}, waited {} seconds'.format(_index, _repeat + 1))
time.sleep(_repeat + 1)
print('I am {}, done'.format(_index))
