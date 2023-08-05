# -*- coding: utf-8 -*-

from sheetfu.utils import convert_a1_to_coordinates, convert_coordinates_to_a1, check_size
from sheetfu.exceptions import SheetNameNoMatchError, SheetIdNoMatchError, NoDataRangeError
from sheetfu.config import dimensions


class Spreadsheet:
    """Spreadsheet object from which we can access its sheets.
    """

    def __init__(self, client, spreadsheet_id):     # only one of those is allowed to be None.
        """
        :param client: A SpreadsheetApp instance.
        :param spreadsheet_id: The spreadsheet ID
        """
        self.client = client
        self.id = spreadsheet_id
        self.sheets = self.get_sheets()

    def __repr__(self):
        return '<Spreadsheet object {}>'.format(self.id)

    def get_sheet(self, name, sid):
        """
        Create a sheet object from sheet ID and sheet name
        :param name: The name of the sheet.
        :param sid: the sheet ID of the sheet.
        :return Sheet object
        """
        return Sheet(
            client=self.client,
            spreadsheet_id=self.id,
            name=name,
            sid=sid
        )

    def get_sheets(self):
        """
        Requests every sheets associated to spreadsheets
        :return List of sheets object
        """
        request = self.client.sheet_service.spreadsheets().get(spreadsheetId=self.id, includeGridData=False)
        response = request.execute()
        sheets = [
            self.get_sheet(sheet['properties']['title'], sheet['properties']['sheetId'])
            for sheet in response['sheets']
        ]
        return sheets

    def get_sheet_by_name(self, name):
        """
        Find sheet by name.
        :param name: name of the sheet we want to access.
        :return: Sheet object matching name.
        """
        for sheet in self.sheets:
            if sheet.name == name:
                return sheet
        else:
            raise SheetNameNoMatchError

    def get_sheet_by_id(self, sid):
        """
        Find sheet by sheet id.
        :param sid: id of the sheet we want to access.
        :return: Sheet object matching id.
        """
        for sheet in self.sheets:
            if sheet.sid == sid:
                return sheet
        else:
            raise SheetIdNoMatchError


class Sheet:

    def __init__(self, client, spreadsheet_id, name, sid):
        self.client = client
        self.spreadsheet_id = spreadsheet_id
        self.name = name
        self.sid = sid

    def __repr__(self):
        return '<Sheet object {}>'.format(self.name)

    def get_range(self, row, column, number_of_row=1, number_of_column=1):
        a1 = convert_coordinates_to_a1(row, column, number_of_row, number_of_column)
        return Range(
            client=self.client,
            sheet=self,
            a1=a1,
        )

    def get_range_from_a1(self, a1_notification):
        return Range(
            client=self.client,
            sheet=self,
            a1=a1_notification,
        )

    def get_data_range(self):
        return Range(
            client=self.client,
            sheet=self,
        )

    def clear(self):
        sheet_range = self.get_data_range()
        sheet_range.clear()


class Range:

    def __init__(self, client, sheet, a1=None):
        self.client = client
        self.sheet = sheet
        self.a1 = a1
        self.coordinates = None if self.a1 is None else convert_a1_to_coordinates(self.a1)

        # we may extract the values when instantiating in case we do not have the A1 range.
        self.values = None
        if self.a1 is None:
            self.values = self.get_values()

    def __repr__(self):
        a1 = self.a1
        if a1 is None:
            a1 = self.sheet.name
        return '<Range object {}>'.format(a1)

    def get_values(self, from_cache=True):
        if self.values and from_cache:
            return self.values
        target_range = self.a1 if self.a1 is not None else self.sheet.name
        request = self.client.sheet_service.spreadsheets().values().get(
            spreadsheetId=self.sheet.spreadsheet_id,
            range=target_range
        )
        response = request.execute()
        self.persist_a1(response)     # very important, so we know the range sizes.
        data = []
        for row in range(0, self.coordinates.number_of_rows):
            data_row = []
            for column in range(0, self.coordinates.number_of_columns):
                try:
                    data_row.append(response["values"][row][column])
                except (KeyError, IndexError):
                    data_row.append("")
            data.append(data_row)
        return data

    @check_size
    def set_values(self, values):
        body_request = {
            'range': self.a1,
            'majorDimension': 'ROWS',
            'values': values
        }
        request = self.client.sheet_service.spreadsheets().values().update(
            spreadsheetId=self.sheet.spreadsheet_id,
            range=self.a1,
            valueInputOption="USER_ENTERED",
            body=body_request
        )
        return request.execute()

    def get_backgrounds(self):
        response = self.make_get_request('background')
        data = []
        values = response["sheets"][0]["data"]
        for row in range(0, self.coordinates.number_of_rows):
            data_row = []
            for column in range(0, self.coordinates.number_of_columns):
                try:
                    background_value = values[0]["rowData"][row]["values"][column]["effectiveFormat"]["backgroundColor"]
                    if background_value == {"red": 1, "green": 1, "blue": 1}:
                        background_value = ""
                    data_row.append(background_value)
                except (KeyError, IndexError):
                    data_row.append("")
            data.append(data_row)
        return data

    @check_size
    def set_backgrounds(self, backgrounds):
        self.make_set_request(field='backgroundColor', rows=backgrounds)

    def get_notes(self):
        response = self.make_get_request('note')
        data = []
        values = response["sheets"][0]["data"]
        for row in range(0, self.coordinates.number_of_rows):
            data_row = []
            for column in range(0, self.coordinates.number_of_columns):
                try:
                    note = values[0]["rowData"][row]["values"][column]["note"]
                    data_row.append(note)
                except (KeyError, IndexError):
                    data_row.append("")
            data.append(data_row)
        return data

    @check_size
    def set_notes(self, notes):
        rows = []
        for row in notes:
            row_data = {'values': []}
            for note in row:
                if note:
                    row_data['values'].append({'note': note})
                else:
                    row_data['values'].append({'note': ''})
            rows.append(row_data)
        return self.make_set_request(field='note', rows=rows)

    def get_formulas(self):
        data = self.make_get_request('formula')
        return data

    @check_size
    def set_formulas(self, formulas):
        return formulas

    def make_get_request(self, dimension):
        request = self.client.sheet_service.spreadsheets().get(
            spreadsheetId=self.sheet.spreadsheet_id,
            includeGridData=True,
            ranges=[self.a1],
            fields=dimensions[dimension]
        )
        response = request.execute()
        return response

    def make_set_request(self, field, rows):
        body = {
            'requests': [
                {'updateCells': {
                    'range': {
                        "sheetId": self.sheet.sid,
                        "startRowIndex": self.coordinates.row - 1,
                        "endRowIndex": self.coordinates.row + self.coordinates.number_of_rows,
                        "startColumnIndex": self.coordinates.column - 1,
                        "endColumnIndex": self.coordinates.column + self.coordinates.number_of_columns
                    },
                    'field': field,
                    'rows': rows
                }}
            ]
        }
        response = self.client.sheet_service.spreadsheets().batchUpdate(
            spreadsheetId=self.sheet.spreadsheet_id,
            body=body
        ).execute()
        return response

    def persist_a1(self, response):
        if self.a1 is not None:
            return

        display_a1 = response["range"]
        first_cell_a1 = display_a1.split('!')[1].split(':')[0]

        if response.get("values") is None:
            raise NoDataRangeError('No data found in sheet "{}"'.format(self.sheet.name))

        number_of_rows = len(response["values"])
        number_of_columns = 0
        for row in response["values"]:
            if len(row) > number_of_columns:
                number_of_columns = len(row)

        first_cell_coordinates = convert_a1_to_coordinates(first_cell_a1)
        self.a1 = convert_coordinates_to_a1(
            row=first_cell_coordinates.row,
            column=first_cell_coordinates.column,
            number_of_row=number_of_rows,
            number_of_column=number_of_columns,
            sheet_name=self.sheet.name
        )
        self.coordinates = convert_a1_to_coordinates(self.a1)

