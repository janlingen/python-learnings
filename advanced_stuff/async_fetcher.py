import asyncio
class BatchFetcher:
    def __init__(self, database):
        self.database = database

    async def fetch_records(self, record_ids):
        lst = []
        for i in record_ids:
            lst.append(self.database.async_fetch(i))
        return await asyncio.gather(*lst)