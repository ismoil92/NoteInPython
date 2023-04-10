import pandas as pd
class CRUD_CSV:
    def __init__(self):
        pass


    def write_file_csv(self, data):
        df = pd.DataFrame([[data.get_ID(),
                           data.get_header(),
                          data.get_note_body(),
                         data.get_date_time()]],
                         columns=["ID", "Header", "Body", "Date Time"]).to_csv("nodes.csv")

    def read_file_csv(self):
        df = pd.read_csv("nodes.csv", encoding='utf-8') 
        print(df)





