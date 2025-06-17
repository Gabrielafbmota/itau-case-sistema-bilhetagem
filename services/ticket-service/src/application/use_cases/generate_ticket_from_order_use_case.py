from fpdf import FPDF
import os
from src.domain.schemas.ticket_schema import TicketResponseSchema, TicketFromOrderSchema


class GenerateTicketFromOrderUseCase:

    def execute(self, payload: TicketFromOrderSchema) -> TicketResponseSchema:
        ticket_id = payload.ticket_id
        order_id = payload.order_id

        pdf = FPDF()
        pdf.add_page()

        font_path = "src/application/resources/fonts/DejaVuSans.ttf"
        pdf.add_font("DejaVu", "", font_path, uni=True)
        pdf.set_font("DejaVu", "", 14)

        pdf.cell(0, 10, f"Ticket ID: {ticket_id}", ln=True)
        pdf.cell(0, 10, f"Pedido: {order_id}", ln=True)
        pdf.cell(0, 10, f"Cliente: {payload.user.name} ({payload.user.email})", ln=True)
        pdf.cell(
            0, 10, f"Evento: {payload.event.title} - {payload.event.location}", ln=True
        )
        pdf.cell(0, 10, f"Data: {payload.event.date}", ln=True)

        pdf.ln(10)
        pdf.cell(0, 10, "Produtos:", ln=True)

        for p in payload.products:
            pdf.cell(
                0, 10, f"- {p.name} (Qtd: {p.quantity}) - R$ {p.price:.2f}", ln=True
            )

        pdf.ln(10)
        pdf.cell(0, 10, f"Total Pago: R$ {payload.total_price:.2f}", ln=True)

        # Salvar PDF
        os.makedirs("tickets", exist_ok=True)
        filepath = f"tickets/ticket_{ticket_id}.pdf"
        pdf.output(filepath)

        return TicketResponseSchema(
            ticket_id=ticket_id, order_id=order_id, pdf_path=filepath
        )
