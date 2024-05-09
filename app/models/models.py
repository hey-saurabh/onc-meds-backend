from config.db import DB

class MedicinalPlants(DB):
    def object(item):
        return {
            "_id": str(item.get('_id')),
            "scientific_name": item.get("scientific_name"),
            "common_name": item.get("common_name"),
            "type_of_cancer": item.get("type_of_cancer"),
            "components": item.get("components"),
            "compound": item.get("compound"),
            "part": item.get("part"),
            "region_found": item.get("region_found"),
            "reference": item.get("reference"),
            "image": item.get("image"),
            "fda_approved_drug": item.get("fda_approved_drug"),
            "plant_type": item.get("plant_type")
        }