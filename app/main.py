from app.app_builder import AppBuilder

builder = AppBuilder()
app = builder.run()

if __name__ == "__main__":
    builder.start_uvicorn()
