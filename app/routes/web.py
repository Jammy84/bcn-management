from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter(prefix="/app", tags=["web"])

templates = Jinja2Templates(directory="templates")


@router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.get("/bootstrap", response_class=HTMLResponse)
async def bootstrap_page(request: Request):
    return templates.TemplateResponse("bootstrap.html", {"request": request})


@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard_page(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})


@router.get("/users", response_class=HTMLResponse)
async def users_page(request: Request):
    return templates.TemplateResponse("users.html", {"request": request})


@router.get("/vehicles", response_class=HTMLResponse)
async def vehicles_page(request: Request):
    return templates.TemplateResponse("vehicles.html", {"request": request})


@router.get("/payments", response_class=HTMLResponse)
async def payments_page(request: Request):
    return templates.TemplateResponse("payments.html", {"request": request})


@router.get("/reports", response_class=HTMLResponse)
async def reports_page(request: Request):
    return templates.TemplateResponse("reports.html", {"request": request})


@router.get("/rates", response_class=HTMLResponse)
async def rates_page(request: Request):
    return templates.TemplateResponse("rates.html", {"request": request})
