from typing import Union
from pydantic import BaseModel

class MedicinalPlantSchema(BaseModel):
    scientific_name: str
    common_name: str
    type_of_cancer: str
    components: str
    compound: str
    part: str
    region_found: str
    reference: str
    image: str
    fda_approved_drug: str
    plant_type: str