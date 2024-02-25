from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.jobstores.memory import MemoryJobStore
from db import client

# jobstores = {
#     "default": MongoDBJobStore("giveaways-bot", client=client)
# }
jobstores = {
    "default": MemoryJobStore()
}

class SchedulerWrapper:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.scheduler = AsyncIOScheduler(
                jobstores=jobstores,
                serializer="json"
            )
            cls._instance.scheduler.start()
            print("Scheduler started")
        return cls._instance

    def add_job(self, *args, **kwargs):
        print("[scheduler] adding new job")
        return self.scheduler.add_job(*args, **kwargs)

    def shutdown(self):
        self.scheduler.shutdown()

