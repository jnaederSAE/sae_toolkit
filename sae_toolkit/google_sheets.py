import os
import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build


def parse_dataframe(dataframe: pd.DataFrame) -> list:
    values = dataframe.values.tolist()
    header = dataframe.columns.tolist()
    output = [header, *values]
    return output


class GoogleSheets:
    """Class for importing and exporting data to Google Sheets."""

    def __init__(self, sheet_id: str) -> None:
        self._sheet_id = sheet_id
        self._scopes = ['https://www.googleapis.com/auth/spreadsheets']
        self.current_file = os.path.abspath(__file__)
        self.current_dir = os.path.dirname(self.current_file)
        self.cred_file = 'google_credentials.json'
        self._account_file = os.path.join(self.current_dir, self.cred_file)
        self._creds = service_account.Credentials.from_service_account_file(self._account_file,
                                                                            scopes=self._scopes)
        self._service = build('sheets', 'v4', credentials=self._creds)
        self._value_input_option = "RAW"
        self._insert_data_option = "OVERWRITE"

    def set_google_credentials(self, path_to_file: str) -> None:
        self._account_file = path_to_file

    def get_data_by_worksheet_name(self, worksheet_name: str, sheet_range: str = None) -> list:
        worksheet_range = f"!{sheet_range}" if sheet_range else ""
        request = self._service.spreadsheets().values().get(spreadsheetId=self._sheet_id,
                                                            range=f"{worksheet_name}{worksheet_range}")
        response = request.execute()
        return response["values"] if "values" in response else []

    def get_id_cards_by_campus(self, campus: str) -> pd.DataFrame:
        sheet_name = f"Cards - {campus}"
        results = self.get_data_by_worksheet_name(sheet_name, "A2:A")
        output = [result[0] for result in results]
        return pd.DataFrame(output)

    def clear_worksheet(self, sheet_name: str) -> None:
        request = self._service.spreadsheets().values().clear(spreadsheetId=self._sheet_id, range=sheet_name, body={})
        request.execute()

    def write_student_data_by_group(self, group_name: str, student_data: pd.DataFrame) -> None:
        sheet_name = f"Student List - {group_name}"
        self.clear_worksheet(sheet_name)
        the_range = f"{sheet_name}!A1:A"
        the_values = parse_dataframe(student_data)
        body = {
            "range": the_range,
            "values": the_values
        }
        request = self._service.spreadsheets().values().append(spreadsheetId=self._sheet_id, range=the_range,
                                                               valueInputOption=self._value_input_option,
                                                               insertDataOption=self._insert_data_option, body=body)
        request.execute()
        print(f"Wrote student data to {sheet_name}")
