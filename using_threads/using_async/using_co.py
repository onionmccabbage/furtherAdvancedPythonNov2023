import asyncio
import timeit
# asyncio has been available since 3.5 but only use in 3.7+

# we tend not to use this
# @asyncio.coroutine
# def fn():
#     '''old way'''
#     print('I aman async co-routine')

# insteads we use async-await in part because this is the pattern other languages also use
async def count():
    '''when we make something async we can then use await'''
    print('first')
    await asyncio.sleep(0.5) # sleep within async is thread safe
    print('second')

async def main():
    '''call several async versions of our function (run them at the same time)'''
    await asyncio.gather( count(), count(), count(), count() )

if __name__ == '__main__':
    '''  await means let the main thread et on with other stuff. await will interrupt when its ready'''
    start = timeit.default_timer()
    asyncio.run(main())
    end = timeit.default_timer()
    print(f'Total time {end-start}')