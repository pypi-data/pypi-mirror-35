import time
from .utils import find_request
import asyncio

def execution_timer(func, oms, event_name="EXEC"):
    async def wrap(*args, **kwargs):
        start_time = time.time()
        result = await func(*args, **kwargs)
        exec_time = time.time() - start_time
        req = await find_request()
        asyncio.ensure_future(oms.create_event(
            log_type="serverLog",
            name=event_name,
            request=req,
            event_data={
                'execution': exec_time,
                'api': getattr(func, '__name__', '_ModuleError'),
                'controller': getattr(func, '__module__', '_ModuleError')
            }))
        return result
    return wrap
