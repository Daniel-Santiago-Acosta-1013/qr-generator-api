import qrcode
from io import BytesIO
from domain.services.qr_generator import QRGenerator

class QRGeneratorService(QRGenerator):
    def generate(self, data: str) -> bytes:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img_byte_arr = BytesIO()
        img.save(img_byte_arr, format="PNG")
        return img_byte_arr.getvalue()