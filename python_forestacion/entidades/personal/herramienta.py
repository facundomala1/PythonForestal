class Herramienta:
    """
    Entidad que representa una herramienta de trabajo.
    """
    def __init__(self, id_herramienta: int, nombre: str, certificado_hys: bool):
        """
        Args:
            id_herramienta (int): ID único de la herramienta.
            nombre (str): Nombre de la herramienta (ej. "Pala").
            certificado_hys (bool): True si tiene certificación de Higiene y Seguridad.
        """
        self._id_herramienta = id_herramienta
        self._nombre = nombre
        self._certificado_hys = certificado_hys

    def get_nombre(self) -> str:
        return self._nombre