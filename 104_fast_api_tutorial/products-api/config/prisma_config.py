from prisma import Prisma
import logging

prisma = Prisma()
logger = logging.getLogger(__name__)

async def connectPrisma():
    if not prisma.is_connected():
        await prisma.connect()
        logger.info("------- connect prisma worked--------")



async def disconnectPrisma():
    if prisma.is_connected():
        await prisma.disconnect()
        logger.error("------connection closed------")
        