from typing import Optional

class custom_stream_data:
    name: str
    temp: Optional[float]
    aux_temp: Optional[float]
    ext_temp: Optional[float]
    temp_unit: Optional[str]
    gravity: Optional[float]
    comment: Optional[str]

    def __init__(self, name: str) -> None:
        self.name = name
        self.temp = None
        self.aux_temp = None
        self.ext_temp = None
        self.temp_unit = None
        self.gravity = None
        self.comment = None
