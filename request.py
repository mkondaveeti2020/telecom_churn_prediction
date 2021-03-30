import requests
data = {
    "total_ic_mou_8": 5.49,
    "loc_ic_mou_8": -206,
    "loc_ic_t2m_mou_8": 0,
    "loc_ic_t2t_mou_8": 656.3919999999999,
    "total_og_mou_8": 0,
    "last_day_rch_amt_8": 0,
    "total_rech_amt_8": 0,
    "loc_og_t2m_mou_8": 708.893089087563,
    "total_rech_amt_Diff": 0,
    "loc_og_mou_8": 5.49,
    "arpu_Diff": -206,
    "roam_og_mou_8": 0,
    "arpu_8": 656.3919999999999,
    "max_rech_amt_8": 0,
    "total_og_mou_Diff": 0
  }

url = "http://127.0.0.1:5000/predict_api"
response = requests.post(url, json=data)
print("Churn: "+ str(response.json()))
