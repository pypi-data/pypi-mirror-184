from fastapi import FastAPI
#from fastapi_profiler.profiler_middleware import PyInstrumentProfilerMiddleware

import uvicorn
from api.routers import user, case, authentication,prwebform

app = FastAPI()
#app.add_middleware(PyInstrumentProfilerMiddleware)

app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(case.router)
app.include_router(prwebform.router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
