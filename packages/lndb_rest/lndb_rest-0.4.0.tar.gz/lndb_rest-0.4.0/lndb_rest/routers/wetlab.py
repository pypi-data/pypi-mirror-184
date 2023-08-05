import pandas as pd
from fastapi import APIRouter, HTTPException, UploadFile
from lnschema_wetlab.dev import parse_and_insert_df

router = APIRouter(prefix="/wetlab")


@router.post("/")
def add_samplesheet(samplesheet: UploadFile):
    df = pd.read_csv(samplesheet.file)
    try:
        added_entries = parse_and_insert_df(df, "biosample")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return added_entries
