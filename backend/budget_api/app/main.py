from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psycopg
from mangum import Mangum
from .routers import transactions
from .database import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Budget Planning API",
    description="API for budget planning and transaction management",
    version="1.0.0"
)

# Disable CORS. Do not remove this for full-stack development.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Include routers
app.include_router(transactions.router, prefix="/api/v1", tags=["transactions"])

@app.get("/healthz")
async def healthz():
    return {"status": "ok"}

# AWS Lambda handler
handler = Mangum(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
