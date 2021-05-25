from typing import Optional
from fastapi import FastAPI
import asyncpg


app = FastAPI()
# Create a database connection pool
app['pool'] = asyncpg.create_pool(database='postgres', user='postgres', host='localhost')
# Configure service routes


@app.get("/items/{power}")
async def read_items(power: Optional[int] = 10):
    pool = app['pool']
    # Take a connection from the pool.
    async with pool.acquire() as connection:
        # Open a transaction.
        async with connection.transaction():
            # Run the query passing the request argument.
            result = await connection.fetchval('select 2 ^ $1', power)
            text = "2 ^ {} is {}".format(power, result)
            return {"result": text}

