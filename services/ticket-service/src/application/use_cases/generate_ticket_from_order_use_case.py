from fpdf import FPDF, HTMLMixin
import qrcode
import os
from src.domain.schemas.ticket_schema import TicketResponseSchema


# Classe extendida com HTML
class MyFPDF(FPDF, HTMLMixin):
    pass


class GenerateTicketFromOrderUseCase:

    def execute(self, payload) -> TicketResponseSchema:
        ticket_id = payload.ticket_id
        order_id = payload.order_id

        # Cria diretório
        os.makedirs("tickets", exist_ok=True)

        # Gerar QRCode
        qr_data = f"https://meusite.com/ticket/{ticket_id}"
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.ERROR_CORRECT_H,
            box_size=8,
            border=2,
        )
        qr.add_data(qr_data)
        img = qr.make_image(fill_color="black", back_color="white").get_image()

        qr_path = f"tickets/qr_{ticket_id}.png"
        img.save(qr_path)

        # Monta PDF
        pdf = MyFPDF("P", "mm", (100, 180))  # formato "ticket"
        pdf.add_page()

        # Fonte
        font_path = "src/application/resources/fonts/DejaVuSans.ttf"
        pdf.add_font("DejaVu", "", font_path, uni=True)
        pdf.set_font("DejaVu", "", 12)

        # Borda
        pdf.set_line_width(1)
        pdf.set_draw_color(30, 144, 255)  # azul
        pdf.rect(5.0, 5.0, 90.0, 170.0, style="D")

        # HTML Template
        html = f"""
        <div align="center">
            <h2 style="color:#8A9E23;">🎫 {payload.event.title}</h2>
            <p style="font-size: 12px;">{payload.event.location}<br>
            {payload.event.date}</p>
            <hr width="80%">
            <h3 style="color:black;">Pedido: {order_id}</h3>
            <p style="font-size: 14px;">{payload.user.name} ({payload.user.email})</p>
            <hr width="80%">
            <h4 style="color:#333;">Produtos</h4>
        </div>
        """

        pdf.write_html(html)

        # Lista de produtos
        pdf.set_font("DejaVu", "", 12)
        for p in payload.products:
            pdf.cell(
                0, 8, f"- {p.name} (Qtd: {p.quantity}) - R$ {p.price:.2f}", ln=True
            )

        pdf.ln(5)
        pdf.cell(0, 10, f"Total: R$ {payload.total_price:.2f}", ln=True, align="C")

        # QR Code
        pdf.image(qr_path, x=30, y=130, w=40)

        pdf.ln(10)
        pdf.set_font("DejaVu", "", 10)
        pdf.cell(0, 10, f"Código: TK-{ticket_id:06d}", ln=True, align="C")

        # Salvar PDF
        filepath = f"tickets/ticket_{ticket_id}.pdf"
        pdf.output(filepath)

        return TicketResponseSchema(
            ticket_id=ticket_id, order_id=order_id, pdf_path=filepath
        )
