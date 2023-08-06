# __init__.py
__authors__ = ["tsalazar"]
__version__ = "0.2"

# v0.1 (tsalazar) -- 2018/08/21 Initial version.
# v0.2 (tsalazar) -- 2018/08/27 Moved workbook formatting to be after workbook creation.


import logging
import xlsxwriter
import pandas as pd


class Excel:
    """Create an Excel workbook with worksheets.

    Attributes:
        workbook: Excel workbook object.
        header_format_definition (dict): Cell and font format settings for the worksheet header.
        row_format_definition (dict): Cell and font format settings for worksheet rows.
        alternate_row_format_definition (dict): Cell and font format settings for alternating worksheet rows.
    """

    def __init__(self, output_file=None):
        """Initialize an instance of the Excel class

        Args:
            output_file (str): Name of the Excel workbook file.
        """

        self.__logger = logging.getLogger(__name__)
        self.__logger.debug('Initializing Excel object')

        if output_file is None:
            self.__logger.critical('No output file defined.')
            exit(0)
        else:
            self._output_file = output_file  # Output file name

        self.header_format_definition = {
            # == Font ==
            'font_name': 'Calibri',  # Font type (i.e. 'Consolas', 'Times New Roman', 'Calibri', 'Courier New')
            'font_size': 10,  # Font size
            'font_color': 'black',  # Font color
            'bold': True,  # Bold
            'italic': False,  # Italic
            'underline': 0,  # Underline (0, 1 = Single, 2 = Double, 33 = Single Accounting, 34 = Double Accounting)
            'font_strikeout': False,  # Strikeout
            'font_script': 0,  # Super/Subscript (0 = Off, 1 = Superscript, 2 = Subscript)

            # == Number ==
            # 'num_format': '',  # Numeric/Date format and Conditional formatting

            # == Protection ==
            'locked': False,  # Lock cells
            'hidden': False,  # Hide formulas

            # == Alignment ==
            'align': 'center',  # Horizontal align ('center', 'right', 'fill', 'justify', 'center_across')
            'valign': 'vcenter',  # Vertical align ('top', 'vcenter', 'bottom', 'vjustify')
            'rotation': 0,  # Rotation
            'text_wrap': False,  # Text wrap
            # 'text_justlast': False,  # Justify last. For Eastern languages
            # 'center_across': False,  # Center across
            'indent': 0,  # Indentation
            'shrink': False,  # Shrink to fit

            # == Pattern ==
            'pattern': 1,  # Cell Pattern (1 = solid fill of bg_color)
            'bg_color': '#D7E4BC',  # Background color
            # 'fg_color': '#D7E4BC',  # Foreground color

            # == Border ==
            'border': 1,  # Cell border
            # 'bottom': '',  # Bottom border
            # 'top': '',  # Top border
            # 'left': '',  # Left border
            # 'right': '',  # Right border
            'border_color': 'white',  # Border color
            # 'bottom_color': '',  # Bottom color
            # 'top_color': '',  # Top color
            # 'left_color': '',  # Left color
            # 'right_color': '',  # Right color
        }

        self.row_format_definition = {
            # == Font ==
            'font_name': 'Calibri Light',  # Font type (i.e. 'Consolas', 'Times New Roman', 'Calibri', 'Courier New')
            'font_size': 11,  # Font size
            'font_color': 'black',  # Font color
            'bold': False,  # Bold
            'italic': False,  # Italic
            'underline': 0,  # Underline (0, 1 = Single, 2 = Double, 33 = Single Accounting, 34 = Double Accounting)
            'font_strikeout': False,  # Strikeout
            'font_script': 0,  # Super/Subscript (0 = Off, 1 = Superscript, 2 = Subscript)

            # == Number ==
            # 'num_format': '',  # Numeric/Date format and Conditional formatting

            # == Protection ==
            'locked': False,  # Lock cells
            'hidden': False,  # Hide formulas

            # == Alignment ==
            # 'align': 'left',  # Horizontal align ('center', 'right', 'fill', 'justify', 'center_across')
            # 'valign': 'vcenter',  # Vertical align ('top', 'vcenter', 'bottom', 'vjustify')
            # 'rotation': 0,  # Rotation
            'text_wrap': False,  # Text wrap
            # 'text_justlast': False,  # Justify last. For Eastern languages
            # 'center_across': False,  # Center across
            'indent': 0,  # Indentation
            'shrink': False,  # Shrink to fit

            # == Pattern ==
            'pattern': 1,  # Cell Pattern (1 = solid fill of bg_color)
            'bg_color': '#FFFFFF',  # Background color
            'fg_color': 'black',  # Foreground color

            # == Border ==
            'border': 1,  # Cell border
            # 'bottom': '',  # Bottom border
            # 'top': '',  # Top border
            # 'left': '',  # Left border
            # 'right': '',  # Right border
            'border_color': '080851',  # Border color
            # 'bottom_color': '',  # Bottom color
            # 'top_color': '',  # Top color
            # 'left_color': '',  # Left color
            # 'right_color': '',  # Right color
        }

        self.alternate_row_format_definition = {
            # == Font ==
            'font_name': 'Consolas',  # Font type (i.e. 'Consolas', 'Times New Roman', 'Calibri', 'Courier New')
            'font_size': 11,  # Font size
            'font_color': 'black',  # Font color
            'bold': False,  # Bold
            'italic': False,  # Italic
            'underline': 0,  # Underline (0, 1 = Single, 2 = Double, 33 = Single Accounting, 34 = Double Accounting)
            'font_strikeout': False,  # Strikeout
            'font_script': 0,  # Super/Subscript (0 = Off, 1 = Superscript, 2 = Subscript)

            # == Number ==
            # 'num_format': '',  # Numeric/Date format and Conditional formatting

            # == Protection ==
            'locked': False,  # Lock cells
            'hidden': False,  # Hide formulas

            # == Alignment ==
            # 'align': 'left',  # Horizontal align ('center', 'right', 'fill', 'justify', 'center_across')
            # 'valign': 'vcenter',  # Vertical align ('top', 'vcenter', 'bottom', 'vjustify')
            # 'rotation': 0,  # Rotation
            'text_wrap': False,  # Text wrap
            # 'text_justlast': False,  # Justify last. For Eastern languages
            # 'center_across': False,  # Center across
            'indent': 0,  # Indentation
            'shrink': False,  # Shrink to fit

            # == Pattern ==
            'pattern': 1,  # Cell Pattern (1 = solid fill of bg_color)
            'bg_color': '#D4D3FF',  # Background color
            'fg_color': 'black',  # Foreground color

            # == Border ==
            'border': 1,  # Cell border
            # 'bottom': '',  # Bottom border
            # 'top': '',  # Top border
            # 'left': '',  # Left border
            # 'right': '',  # Right border
            'border_color': '080851',  # Border color
            # 'bottom_color': '',  # Bottom color
            # 'top_color': '',  # Top color
            # 'left_color': '',  # Left color
            # 'right_color': '',  # Right color
        }

        self.workbook = None
        self.__writer = None

        self.__logger.debug('Excel class object initialized')

    @staticmethod
    def __adjust_column_width(column_widths, worksheet):

        column_number = 0
        for column_width in column_widths:
            worksheet.set_column(column_number, column_number, column_width + 6)
            column_number += 1

        worksheet.freeze_panes(1, 0)  # Freeze the first row

    def __create_dataframe_worksheet(self, worksheet_name, content, header_format):
        """Add a worksheet to the workbook using dataframe data.

        Args:
            worksheet_name (str): Excel worksheet name.
            content: Worksheet content.
            header_format: Worksheet header.
        """
        content.to_excel(self.__writer, index=False, sheet_name=worksheet_name)
        worksheet = self.__writer.sheets[worksheet_name]

        column_widths = []
        column_number = 0

        # Draw header
        for column_number, value in enumerate(content.columns.values):
            worksheet.write(0, column_number, value, header_format)

        worksheet.autofilter(0, 0, 0, column_number)  # Add filter buttons to the top row

        # Find column widths
        for column_name in content.columns:
            column_widths.append(content[column_name].map(lambda x: len(str(x))).max())

        self.__adjust_column_width(column_widths, worksheet)

    def __create_nondataframe_worksheet(self, worksheet_name, header, content, header_format, row_format):
        """Add a worksheet to the workbook using dict data.

        Args:
            worksheet_name (str): Excel worksheet name.
            content: Worksheet content.
            header: Worksheet header.
        """
        worksheet = self.workbook.add_worksheet(worksheet_name)

        column_widths = []
        column = 0

        # Draw header
        if header is not None:
            for header_item in header:
                self.__logger.debug(f'Writing row: column={column}, header_item={header_item}')
                worksheet.write(0, column, header_item, header_format)
                column_widths.append(len(header_item))
                column += 1

            worksheet.autofilter(0, 0, 0, column - 1)  # Add filter buttons to the top row
            column = 0

        # Iterate over the data and write it out row by row.
        if content is not None:
            if header is None:
                # Start from the first cell. Rows and columns are zero indexed.
                row = 0
                column_widths = [5] * len(content[0])
            else:
                row = 1

            for result in content:
                for key, data in result.items():
                    if type(data) is int or type(data) is float:
                        worksheet.write(row, column, data, row_format)
                    else:
                        worksheet.write(row, column, str(data), row_format)

                    if len(str(data)) > column_widths[column]:
                        column_widths[column] = len(str(data))

                    column += 1

                # Move to next row and reset to first column
                row += 1
                column = 0

        self.__adjust_column_width(column_widths, worksheet)

    def create_worksheet(self, worksheet_name='Worksheet', content=None, header=None):
        """Add a worksheet to the workbook

        Args:
            worksheet_name (str): Excel worksheet name.
            content: Worksheet content.
            header: Worksheet header.
        """

        content_type = type(content)

        # Keep worksheet name under 31 character limit
        worksheet_name = worksheet_name[:30]

        # Sanity check
        if content is None:
            self.__logger.warning('No worksheet content defined')

        if header is None and content_type is not pd.DataFrame:
            self.__logger.warning('No worksheet header defined')

        self.__logger.debug('Creating worksheet: ' + worksheet_name)

        # Start a workbook if it doesn't yet exist
        if self.workbook is None:

            self.__logger.debug(f'Creating workbook: {self._output_file}')

            if content_type is dict:
                self.workbook = xlsxwriter.Workbook(self._output_file)
            elif content_type is pd.DataFrame:
                self.__writer = pd.ExcelWriter(self._output_file, engine='xlsxwriter')
                self.workbook = self.__writer.book
            else:
                self.__logger.critical('Unknown data type for worksheet content.')
                exit(0)

        # Define cell formats
        self.__logger.debug('header_format:')
        self.__logger.debug(self.header_format_definition)
        header_format = self.workbook.add_format(self.header_format_definition)

        self.__logger.debug('body_row_format:')
        self.__logger.debug(self.row_format_definition)
        row_format = self.workbook.add_format(self.row_format_definition)

        # self.__logger.debug('alternate_row_format:')
        # self.__logger.debug(self.alternate_row_format_definition)
        # alternate_row_format = self.workbook.add_format(self.alternate_row_format_definition)

        # Create the worksheet
        if content_type is dict:
            self.__create_nondataframe_worksheet(worksheet_name, header, content, header_format, row_format)
        elif content_type is pd.DataFrame:
            self.__create_dataframe_worksheet(worksheet_name, content, header_format)
        else:
            self.__logger.critical('Unknown data type for worksheet content.')
            exit(0)

    def close_workbook(self):
        """Gracefully wrap up the workbook"""

        self.__logger.debug('Workbook created.')
        self.workbook.close()
