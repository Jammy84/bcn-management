from datetime import date
from functools import lru_cache
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from supabase import Client, create_client
from app.core.settings import settings


@lru_cache(maxsize=1)
def _get_supabase_client() -> Client | None:
    if not settings.supabase_url or not settings.supabase_service_role_key:
        return None
    return create_client(settings.supabase_url, settings.supabase_service_role_key)


def upload_pdf_to_supabase(pdf_path: Path, object_name: str) -> str | None:
    if not settings.supabase_storage_bucket:
        return None
    client = _get_supabase_client()
    if client is None:
        return None
    storage_path = f"reports/{object_name}.pdf"
    with pdf_path.open("rb") as file:
        client.storage.from_(settings.supabase_storage_bucket).upload(
            storage_path,
            file,
            {
                "content-type": "application/pdf",
                "upsert": "true",
            },
        )
    public_url = client.storage.from_(settings.supabase_storage_bucket).get_public_url(storage_path)
    return public_url


def generate_report_pdf(
    output_dir: Path,
    report_name: str,
    period_start: date,
    period_end: date,
    total_vehicles: int,
    total_collected: float,
    company_share: float,
    responsible_name: str,
    logo_path: Path | None = None,
) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    pdf_path = output_dir / f"{report_name}.pdf"
    c = canvas.Canvas(str(pdf_path), pagesize=A4)
    width, height = A4

    y = height - 50
    if logo_path and logo_path.exists():
        c.drawImage(str(logo_path), 40, y - 40, width=80, height=40, preserveAspectRatio=True, mask='auto')
    c.setFont("Helvetica-Bold", 16)
    c.drawString(140, y - 20, "Rapport Bombacar Nayo")

    c.setFont("Helvetica", 11)
    y -= 80
    c.drawString(40, y, f"Période: {period_start} au {period_end}")
    y -= 20
    c.drawString(40, y, f"Nombre de véhicules: {total_vehicles}")
    y -= 20
    c.drawString(40, y, f"Total collecté: {total_collected:.2f}")
    y -= 20
    c.drawString(40, y, f"Part entreprise (12%): {company_share:.2f}")
    y -= 40
    c.drawString(40, y, f"Responsable: {responsible_name}")

    c.showPage()
    c.save()
    return pdf_path
