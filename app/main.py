from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.core.settings import settings
from app.core.logging import configure_logging
from app.core.database import engine, Base
from app.routes import auth, users, vehicles, payments, reports, dashboard, payment_rates, web
from app import models  # noqa: F401

configure_logging()

app = FastAPI(title=settings.app_name)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(vehicles.router)
app.include_router(payments.router)
app.include_router(reports.router)
app.include_router(dashboard.router)
app.include_router(payment_rates.router)
app.include_router(web.router)


@app.get("/")
async def root():
    return RedirectResponse(url="/app/login")


@app.on_event("startup")
async def on_startup() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
