from datetime import date
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


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
