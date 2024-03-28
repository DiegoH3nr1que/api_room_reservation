from typing import Any
from django.db import models

class ClassromEntity:

    def __init__(self, id,  name, date, description,discipline= [
        "LP", "ML", "IOT", "BIGDATA", "WEB", "MOBILE"
    ]) -> None:
        self.id = id
        self.name = name
        self.date = date
        self.description = description
        self.discipline = discipline

    def __str__(self) -> str:
        return (f"Classroom <{self.name}")
    
    def __getattribute__(self, __name: str) -> Any:
        if (__name=='date'):
            return object.__getattribute__(self, __name).strftime("%d/%m/%Y %H:%M:%S")
        else:
            return object.__getattribute__(self,__name)

        
