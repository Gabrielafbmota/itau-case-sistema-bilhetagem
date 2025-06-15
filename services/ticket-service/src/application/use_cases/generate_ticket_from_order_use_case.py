from fpdf import FPDF
from datetime import datetime
import os
import uuid
from src.domain.schemas.ticket_schema import TicketFromOrderSchema, TicketResponseSchema


class GenerateTicketFromOrderUseCase:
    def __init__(self, output_dir: str = "tickets"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def execute(self, data: TicketFromOrderSchema) -> TicketResponseSchema:
        ticket_id = str(uuid.uuid4())
        filename = f"ticket_{ticket_id}.pdf"
        filepath = os.path.join(self.output_dir, filename)

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, txt="🎟️ Ticket de Ingresso", ln=True, align="C")
        pdf.ln(10)
        pdf.cell(200, 10, txt=f"Pedido ID: {data.order_id}", ln=True)
        pdf.cell(200, 10, txt=f"Usuário: {data.user.name} - {data.user.email}", ln=True)
        pdf.cell(
            200, 10, txt=f"Evento: {data.event.title} - {data.event.date}", ln=True
        )

        pdf.ln(10)
        pdf.cell(200, 10, txt="Produtos:", ln=True)
        for p in data.products:
            pdf.cell(200, 10, txt=f"- {p.name}: R$ {p.price}", ln=True)

        pdf.ln(10)
        pdf.cell(200, 10, txt=f"Valor total: R$ {data.total_price}", ln=True)
        pdf.cell(
            200,
            10,
            txt=f"Emitido em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}",
            ln=True,
        )

        pdf.output(filepath)

        return TicketResponseSchema(
            ticket_id=ticket_id, order_id=data.order_id, pdf_path=filepath
        )
