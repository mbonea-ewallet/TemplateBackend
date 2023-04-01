import asyncio
import aiohttp

analysis = {'failed':0,'passed':0}

async def send_post_request(session,number=0):
    async with session.post(
        url="https://app-mbonea-mjema.cloud.okteto.net/post/create",
        json={
  "content": {},
  "recommendations": {}
}
    ) as response:
        response_text = await response.text()
        if response.status == 200:
            analysis['passed'] += 1
            print(f"Response from {number}: {response_text}")
        else:
            analysis['failed'] += 1


async def send_post_requests_async():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for number in range(1_000):
            tasks.append(asyncio.ensure_future(send_post_request(session,number)))
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(send_post_requests_async())
    print(analysis)
