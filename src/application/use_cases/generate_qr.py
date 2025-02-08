class GenerateQRUseCase:
    def __init__(self, qr_generator, qr_repository):
        self.qr_generator = qr_generator
        self.qr_repository = qr_repository
    
    def execute(self, data: str) -> str:
        qr_image = self.qr_generator.generate(data)
        qr_id = self.qr_repository.save(qr_image)
        return qr_id