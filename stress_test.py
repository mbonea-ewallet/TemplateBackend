import asyncio
import aiohttp


async def send_post_request(session,number=0):
    async with session.post(
        url="https://fastapi-mbonea-mjema.cloud.okteto.net/comment/create",
        json={"userId": 1, "content": f"comment {number}", "postId": 1},
    ) as response:
        response_text = await response.text()
        print(f"Response from {number}: {response_text}")


async def send_post_requests_async():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for number in range(1000):
            tasks.append(asyncio.ensure_future(send_post_request(session,number)))
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(send_post_requests_async())
