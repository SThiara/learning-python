import asyncio

async def add_nums(n1, n2):
  sum = n1 + n2  
  await asyncio.sleep(3)
  return sum
  
loop = asyncio.get_event_loop()

answer = loop.run_until_complete(add_nums(2, 3))
print(answer)

loop.close()