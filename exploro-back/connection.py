from dotenv import load_dotenv
load_dotenv()

import os
from supabase import create_client


url= os.environ.get("SUPABASE_URL")
key= os.environ.get("SUPABASE_KEY")
def create_supabase_client():
    supabase = create_client(url, key)
    return supabase


# data =supabase.table("yodo").select("*").execute()
# print(data)