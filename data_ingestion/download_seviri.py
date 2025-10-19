import eumdac, os

def query_and_download_seviri(dt, bbox, download_dir):
    """Query and download SEVIRI data for a given datetime and bounding box."""
    client = eumdac.Client(os.getenv("EUMETSAT_USERNAME"), os.getenv("EUMETSAT_PASSWORD"))
    coll = client.get_collection("EO:EUM:DAT:MSG:HRSEVIRI")
    timestamp = dt.strftime("%Y-%m-%dT%H:%M:%S")
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    products = coll.search(start=timestamp, end=timestamp, bbox=bbox)
    for prod in products:
        file_path = os.path.join(download_dir, prod.name)
        if not os.path.exists(file_path):
            prod.download(file_path)
