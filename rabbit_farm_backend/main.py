from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import rabbits  # Import the router from the 'routes/rabbits.py' file
from database.db import Base, engine  # Import SQLAlchemy Base and engine
from sqlalchemy.orm import Session

app = FastAPI()
# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins. Replace with a specific domain in production.
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.).
    allow_headers=["*"],  # Allows all headers.
)

# Define the root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to Rabbit Farm Management!"}

# Ensure all database tables are created at startup
@app.on_event("startup")
async def startup_event():
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)

# Close the database session at shutdown
@app.on_event("shutdown")
async def shutdown_event():
    print("Shutting down...")

# Include the router for rabbit management
app.include_router(rabbits.router)

# Example endpoint to fetch rabbit data (if needed)
@app.get("/rabbits/")
def get_rabbits():
    # Logic to get rabbits from the database (e.g., querying the database)
    # Placeholder for rabbit data
    rabbit_data = [
        {"id": 1, "name": "Thumper", "breed": "Netherland Dwarf", "age": 2, "health_status": "Healthy", "weight": 1.5, "last_vaccination": "2024-11-20"},
        {"id": 2, "name": "Bunny", "breed": "Holland Lop", "age": 1, "health_status": "Healthy", "weight": 2.5, "last_vaccination": "2024-11-20"}
    ]
    return {"rabbits": rabbit_data}