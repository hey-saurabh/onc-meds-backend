import logging
from fastapi import APIRouter, Request, Response
from app.models.models import MedicinalPlants
from app.models.schema import MedicinalPlantSchema
from utils.util import create_query
import json

router = APIRouter()


@router.get('/get_data')
async def get_data(filters = "{}"):
    filters = json.loads(filters)
    data = {}
    query = create_query(filters)
    try:
        data = await MedicinalPlants.filter(query)
        if data:
            return({"success": True, "data": data})
        else:
            return({"success": True, "data": data})
    except Exception as e:
        logging.info(f"Error while getting data, Error occured: {str(e)}")


@router.post('/upload_file')
async def upload_data(plant_type: str):
    try:
        import pandas as pd
        df = pd.read_csv('app/new_data2.csv', encoding='utf-8')
        list_of_dicts = df.to_dict('records')
        print(df)
        created_data = []
        for temp_data in list_of_dicts:

            temp_data['plant_type'] = plant_type
            data  = MedicinalPlantSchema(**temp_data)
            
            insert_data = data.dict()
            createdData = await MedicinalPlants.create(insert_data)

            created_data.append(createdData)
                
        return({"success": True, "message": "Successfully Inserted Data"})
    
    except Exception as e:
        logging.info(e)


