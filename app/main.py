from fastapi import FastAPI
from app.api.v1 import api_router
from app.db.session import Base, engine

app = FastAPI(
    title="FastAPI Demo",
    version="1.0.0"
)

app.include_router(api_router)


def main():
    import uvicorn

    # # Create DB tables
    # Base.metadata.create_all(bind=engine)

    # Run the app
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    main()