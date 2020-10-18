"""
Downloads raw imf data and stores in mongodb 
    This script is meant to be run from the data-collection directory
"""

"""
adding to sys.path to import data-collection/mongodb_helper.py
"""
import sys

here = sys.path[0]
sys.path.append(here[:len(here)-len("/imf")])

from helpers.download_raw_helper import *
from mongodb_helper import *

if __name__ == "__main__":

    all_mapping = dictionary_mapping(get_dataflow_parameters())

    npl_countries = get_npl_countries()

    print(npl_countries)

    chosen_indicators = {'APDREO':['LUR','PCPI_PCH','PCPIE_PCH','NGDP_R_PPP_PC_PCH'],
                     'CPI':['PCPI_IX'], 
     'FAS':['FCIODD_NUM','FCIOFI_NUM','FCIODU_NUM','FCIODMF_NUM','FCNODC_NUM','FCRODC_PE_NUM' ,'FCRODU_PE_NUM',
            'FCSODCG_GDP_PT' ,'FCBODC_NUM'], 
     'FDI':['FD_FD_IX', 'FD_FIA_IX', 'FD_FID_IX', 'FD_FIE_IX', 'FD_FI_IX','FD_FMA_IX' ,'FD_FMD_IX','FD_FME_IX', 
            'FD_FM_IX'], 'FSI': ['FSANL_PT', 'FSKNL_PT', 'FSBPNL_PT']}
    
    all_data = get_data(chosen_indicators, 'A' , npl_countries)

    converted = convert_dictionary(all_data, all_mapping)

    COLLECTION_NAME = "imf"
    mongo_clear(COLLECTION_NAME)

    for cname, cdata in converted.items():
        out = {
        "_id": cname,
        "data": cdata
        }

        print("inserting into mongodb:", cname, " "*50, end="\r")
        mongo_insert(out, COLLECTION_NAME)

        print("\ndone")