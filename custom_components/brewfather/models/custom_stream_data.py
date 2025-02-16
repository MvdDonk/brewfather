from typing import Optional

class custom_stream_data:
    name: str
    temp: Optional[float]
    temp_unit: Optional[str]

    def __init__(self, name: str) -> None:
        self.name = name
