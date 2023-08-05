# coding: utf-8

"""
    Web API Swagger specification

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PageSetup(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'link': 'Link',
        'is_hf_diff_first': 'bool',
        'fit_to_pages_wide': 'int',
        'print_quality': 'int',
        'print_draft': 'bool',
        'first_page_number': 'int',
        'paper_size': 'str',
        'print_comments': 'str',
        'print_errors': 'str',
        'center_vertically': 'bool',
        'is_percent_scale': 'bool',
        'black_and_white': 'bool',
        'print_title_columns': 'str',
        'is_hf_align_margins': 'bool',
        'print_area': 'str',
        'footer_margin': 'float',
        'left_margin': 'float',
        'center_horizontally': 'bool',
        'header_margin': 'float',
        'top_margin': 'float',
        'footer': 'list[PageSection]',
        'fit_to_pages_tall': 'int',
        'is_hf_scale_with_doc': 'bool',
        'print_headings': 'bool',
        'zoom': 'int',
        'print_title_rows': 'str',
        'order': 'str',
        'print_copies': 'int',
        'orientation': 'str',
        'right_margin': 'float',
        'print_gridlines': 'bool',
        'is_auto_first_page_number': 'bool',
        'header': 'list[PageSection]',
        'is_hf_diff_odd_even': 'bool',
        'bottom_margin': 'float'
    }

    attribute_map = {
        'link': 'link',
        'is_hf_diff_first': 'IsHFDiffFirst',
        'fit_to_pages_wide': 'FitToPagesWide',
        'print_quality': 'PrintQuality',
        'print_draft': 'PrintDraft',
        'first_page_number': 'FirstPageNumber',
        'paper_size': 'PaperSize',
        'print_comments': 'PrintComments',
        'print_errors': 'PrintErrors',
        'center_vertically': 'CenterVertically',
        'is_percent_scale': 'IsPercentScale',
        'black_and_white': 'BlackAndWhite',
        'print_title_columns': 'PrintTitleColumns',
        'is_hf_align_margins': 'IsHFAlignMargins',
        'print_area': 'PrintArea',
        'footer_margin': 'FooterMargin',
        'left_margin': 'LeftMargin',
        'center_horizontally': 'CenterHorizontally',
        'header_margin': 'HeaderMargin',
        'top_margin': 'TopMargin',
        'footer': 'Footer',
        'fit_to_pages_tall': 'FitToPagesTall',
        'is_hf_scale_with_doc': 'IsHFScaleWithDoc',
        'print_headings': 'PrintHeadings',
        'zoom': 'Zoom',
        'print_title_rows': 'PrintTitleRows',
        'order': 'Order',
        'print_copies': 'PrintCopies',
        'orientation': 'Orientation',
        'right_margin': 'RightMargin',
        'print_gridlines': 'PrintGridlines',
        'is_auto_first_page_number': 'IsAutoFirstPageNumber',
        'header': 'Header',
        'is_hf_diff_odd_even': 'IsHFDiffOddEven',
        'bottom_margin': 'BottomMargin'
    }
    
    @staticmethod
    def get_swagger_types():
        return PageSetup.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return PageSetup.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, link=None, is_hf_diff_first=None, fit_to_pages_wide=None, print_quality=None, print_draft=None, first_page_number=None, paper_size=None, print_comments=None, print_errors=None, center_vertically=None, is_percent_scale=None, black_and_white=None, print_title_columns=None, is_hf_align_margins=None, print_area=None, footer_margin=None, left_margin=None, center_horizontally=None, header_margin=None, top_margin=None, footer=None, fit_to_pages_tall=None, is_hf_scale_with_doc=None, print_headings=None, zoom=None, print_title_rows=None, order=None, print_copies=None, orientation=None, right_margin=None, print_gridlines=None, is_auto_first_page_number=None, header=None, is_hf_diff_odd_even=None, bottom_margin=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        PageSetup - a model defined in Swagger
        """

        self.container['link'] = None
        self.container['is_hf_diff_first'] = None
        self.container['fit_to_pages_wide'] = None
        self.container['print_quality'] = None
        self.container['print_draft'] = None
        self.container['first_page_number'] = None
        self.container['paper_size'] = None
        self.container['print_comments'] = None
        self.container['print_errors'] = None
        self.container['center_vertically'] = None
        self.container['is_percent_scale'] = None
        self.container['black_and_white'] = None
        self.container['print_title_columns'] = None
        self.container['is_hf_align_margins'] = None
        self.container['print_area'] = None
        self.container['footer_margin'] = None
        self.container['left_margin'] = None
        self.container['center_horizontally'] = None
        self.container['header_margin'] = None
        self.container['top_margin'] = None
        self.container['footer'] = None
        self.container['fit_to_pages_tall'] = None
        self.container['is_hf_scale_with_doc'] = None
        self.container['print_headings'] = None
        self.container['zoom'] = None
        self.container['print_title_rows'] = None
        self.container['order'] = None
        self.container['print_copies'] = None
        self.container['orientation'] = None
        self.container['right_margin'] = None
        self.container['print_gridlines'] = None
        self.container['is_auto_first_page_number'] = None
        self.container['header'] = None
        self.container['is_hf_diff_odd_even'] = None
        self.container['bottom_margin'] = None

        if link is not None:
          self.link = link
        if is_hf_diff_first is not None:
          self.is_hf_diff_first = is_hf_diff_first
        if fit_to_pages_wide is not None:
          self.fit_to_pages_wide = fit_to_pages_wide
        if print_quality is not None:
          self.print_quality = print_quality
        if print_draft is not None:
          self.print_draft = print_draft
        if first_page_number is not None:
          self.first_page_number = first_page_number
        if paper_size is not None:
          self.paper_size = paper_size
        if print_comments is not None:
          self.print_comments = print_comments
        if print_errors is not None:
          self.print_errors = print_errors
        if center_vertically is not None:
          self.center_vertically = center_vertically
        if is_percent_scale is not None:
          self.is_percent_scale = is_percent_scale
        if black_and_white is not None:
          self.black_and_white = black_and_white
        if print_title_columns is not None:
          self.print_title_columns = print_title_columns
        if is_hf_align_margins is not None:
          self.is_hf_align_margins = is_hf_align_margins
        if print_area is not None:
          self.print_area = print_area
        if footer_margin is not None:
          self.footer_margin = footer_margin
        if left_margin is not None:
          self.left_margin = left_margin
        if center_horizontally is not None:
          self.center_horizontally = center_horizontally
        if header_margin is not None:
          self.header_margin = header_margin
        if top_margin is not None:
          self.top_margin = top_margin
        if footer is not None:
          self.footer = footer
        if fit_to_pages_tall is not None:
          self.fit_to_pages_tall = fit_to_pages_tall
        if is_hf_scale_with_doc is not None:
          self.is_hf_scale_with_doc = is_hf_scale_with_doc
        if print_headings is not None:
          self.print_headings = print_headings
        if zoom is not None:
          self.zoom = zoom
        if print_title_rows is not None:
          self.print_title_rows = print_title_rows
        if order is not None:
          self.order = order
        if print_copies is not None:
          self.print_copies = print_copies
        if orientation is not None:
          self.orientation = orientation
        if right_margin is not None:
          self.right_margin = right_margin
        if print_gridlines is not None:
          self.print_gridlines = print_gridlines
        if is_auto_first_page_number is not None:
          self.is_auto_first_page_number = is_auto_first_page_number
        if header is not None:
          self.header = header
        if is_hf_diff_odd_even is not None:
          self.is_hf_diff_odd_even = is_hf_diff_odd_even
        if bottom_margin is not None:
          self.bottom_margin = bottom_margin

    @property
    def link(self):
        """
        Gets the link of this PageSetup.

        :return: The link of this PageSetup.
        :rtype: Link
        """
        return self.container['link']

    @link.setter
    def link(self, link):
        """
        Sets the link of this PageSetup.

        :param link: The link of this PageSetup.
        :type: Link
        """

        self.container['link'] = link

    @property
    def is_hf_diff_first(self):
        """
        Gets the is_hf_diff_first of this PageSetup.
        True means that the header/footer of the first page is different with other pages.

        :return: The is_hf_diff_first of this PageSetup.
        :rtype: bool
        """
        return self.container['is_hf_diff_first']

    @is_hf_diff_first.setter
    def is_hf_diff_first(self, is_hf_diff_first):
        """
        Sets the is_hf_diff_first of this PageSetup.
        True means that the header/footer of the first page is different with other pages.

        :param is_hf_diff_first: The is_hf_diff_first of this PageSetup.
        :type: bool
        """

        self.container['is_hf_diff_first'] = is_hf_diff_first

    @property
    def fit_to_pages_wide(self):
        """
        Gets the fit_to_pages_wide of this PageSetup.
        Represents the number of pages wide the worksheet will be scaled to when it's printed.

        :return: The fit_to_pages_wide of this PageSetup.
        :rtype: int
        """
        return self.container['fit_to_pages_wide']

    @fit_to_pages_wide.setter
    def fit_to_pages_wide(self, fit_to_pages_wide):
        """
        Sets the fit_to_pages_wide of this PageSetup.
        Represents the number of pages wide the worksheet will be scaled to when it's printed.

        :param fit_to_pages_wide: The fit_to_pages_wide of this PageSetup.
        :type: int
        """

        self.container['fit_to_pages_wide'] = fit_to_pages_wide

    @property
    def print_quality(self):
        """
        Gets the print_quality of this PageSetup.
        Represents the print quality.

        :return: The print_quality of this PageSetup.
        :rtype: int
        """
        return self.container['print_quality']

    @print_quality.setter
    def print_quality(self, print_quality):
        """
        Sets the print_quality of this PageSetup.
        Represents the print quality.

        :param print_quality: The print_quality of this PageSetup.
        :type: int
        """

        self.container['print_quality'] = print_quality

    @property
    def print_draft(self):
        """
        Gets the print_draft of this PageSetup.
        Represents if the sheet will be printed without graphics.

        :return: The print_draft of this PageSetup.
        :rtype: bool
        """
        return self.container['print_draft']

    @print_draft.setter
    def print_draft(self, print_draft):
        """
        Sets the print_draft of this PageSetup.
        Represents if the sheet will be printed without graphics.

        :param print_draft: The print_draft of this PageSetup.
        :type: bool
        """

        self.container['print_draft'] = print_draft

    @property
    def first_page_number(self):
        """
        Gets the first_page_number of this PageSetup.
        Represents the first page number that will be used when this sheet is printed.

        :return: The first_page_number of this PageSetup.
        :rtype: int
        """
        return self.container['first_page_number']

    @first_page_number.setter
    def first_page_number(self, first_page_number):
        """
        Sets the first_page_number of this PageSetup.
        Represents the first page number that will be used when this sheet is printed.

        :param first_page_number: The first_page_number of this PageSetup.
        :type: int
        """

        self.container['first_page_number'] = first_page_number

    @property
    def paper_size(self):
        """
        Gets the paper_size of this PageSetup.
        Represents the size of the paper.

        :return: The paper_size of this PageSetup.
        :rtype: str
        """
        return self.container['paper_size']

    @paper_size.setter
    def paper_size(self, paper_size):
        """
        Sets the paper_size of this PageSetup.
        Represents the size of the paper.

        :param paper_size: The paper_size of this PageSetup.
        :type: str
        """

        self.container['paper_size'] = paper_size

    @property
    def print_comments(self):
        """
        Gets the print_comments of this PageSetup.
        Represents the way comments are printed with the sheet.

        :return: The print_comments of this PageSetup.
        :rtype: str
        """
        return self.container['print_comments']

    @print_comments.setter
    def print_comments(self, print_comments):
        """
        Sets the print_comments of this PageSetup.
        Represents the way comments are printed with the sheet.

        :param print_comments: The print_comments of this PageSetup.
        :type: str
        """

        self.container['print_comments'] = print_comments

    @property
    def print_errors(self):
        """
        Gets the print_errors of this PageSetup.
        Specifies the type of print error displayed.

        :return: The print_errors of this PageSetup.
        :rtype: str
        """
        return self.container['print_errors']

    @print_errors.setter
    def print_errors(self, print_errors):
        """
        Sets the print_errors of this PageSetup.
        Specifies the type of print error displayed.

        :param print_errors: The print_errors of this PageSetup.
        :type: str
        """

        self.container['print_errors'] = print_errors

    @property
    def center_vertically(self):
        """
        Gets the center_vertically of this PageSetup.
        Represent if the sheet is printed centered vertically.

        :return: The center_vertically of this PageSetup.
        :rtype: bool
        """
        return self.container['center_vertically']

    @center_vertically.setter
    def center_vertically(self, center_vertically):
        """
        Sets the center_vertically of this PageSetup.
        Represent if the sheet is printed centered vertically.

        :param center_vertically: The center_vertically of this PageSetup.
        :type: bool
        """

        self.container['center_vertically'] = center_vertically

    @property
    def is_percent_scale(self):
        """
        Gets the is_percent_scale of this PageSetup.
        If this property is False, the FitToPagesWide and FitToPagesTall properties control how the worksheet is scaled.

        :return: The is_percent_scale of this PageSetup.
        :rtype: bool
        """
        return self.container['is_percent_scale']

    @is_percent_scale.setter
    def is_percent_scale(self, is_percent_scale):
        """
        Sets the is_percent_scale of this PageSetup.
        If this property is False, the FitToPagesWide and FitToPagesTall properties control how the worksheet is scaled.

        :param is_percent_scale: The is_percent_scale of this PageSetup.
        :type: bool
        """

        self.container['is_percent_scale'] = is_percent_scale

    @property
    def black_and_white(self):
        """
        Gets the black_and_white of this PageSetup.
        Represents if elements of the document will be printed in black and white. True/False

        :return: The black_and_white of this PageSetup.
        :rtype: bool
        """
        return self.container['black_and_white']

    @black_and_white.setter
    def black_and_white(self, black_and_white):
        """
        Sets the black_and_white of this PageSetup.
        Represents if elements of the document will be printed in black and white. True/False

        :param black_and_white: The black_and_white of this PageSetup.
        :type: bool
        """

        self.container['black_and_white'] = black_and_white

    @property
    def print_title_columns(self):
        """
        Gets the print_title_columns of this PageSetup.
        Represents the columns that contain the cells to be repeated on the left side of each page.

        :return: The print_title_columns of this PageSetup.
        :rtype: str
        """
        return self.container['print_title_columns']

    @print_title_columns.setter
    def print_title_columns(self, print_title_columns):
        """
        Sets the print_title_columns of this PageSetup.
        Represents the columns that contain the cells to be repeated on the left side of each page.

        :param print_title_columns: The print_title_columns of this PageSetup.
        :type: str
        """

        self.container['print_title_columns'] = print_title_columns

    @property
    def is_hf_align_margins(self):
        """
        Gets the is_hf_align_margins of this PageSetup.
        Indicates whether header and footer margins are aligned with the page margins.Only applies for Excel 2007.

        :return: The is_hf_align_margins of this PageSetup.
        :rtype: bool
        """
        return self.container['is_hf_align_margins']

    @is_hf_align_margins.setter
    def is_hf_align_margins(self, is_hf_align_margins):
        """
        Sets the is_hf_align_margins of this PageSetup.
        Indicates whether header and footer margins are aligned with the page margins.Only applies for Excel 2007.

        :param is_hf_align_margins: The is_hf_align_margins of this PageSetup.
        :type: bool
        """

        self.container['is_hf_align_margins'] = is_hf_align_margins

    @property
    def print_area(self):
        """
        Gets the print_area of this PageSetup.
        Represents the range to be printed.

        :return: The print_area of this PageSetup.
        :rtype: str
        """
        return self.container['print_area']

    @print_area.setter
    def print_area(self, print_area):
        """
        Sets the print_area of this PageSetup.
        Represents the range to be printed.

        :param print_area: The print_area of this PageSetup.
        :type: str
        """

        self.container['print_area'] = print_area

    @property
    def footer_margin(self):
        """
        Gets the footer_margin of this PageSetup.
        Represents the distance from the bottom of the page to the footer, in unit of centimeters.

        :return: The footer_margin of this PageSetup.
        :rtype: float
        """
        return self.container['footer_margin']

    @footer_margin.setter
    def footer_margin(self, footer_margin):
        """
        Sets the footer_margin of this PageSetup.
        Represents the distance from the bottom of the page to the footer, in unit of centimeters.

        :param footer_margin: The footer_margin of this PageSetup.
        :type: float
        """

        self.container['footer_margin'] = footer_margin

    @property
    def left_margin(self):
        """
        Gets the left_margin of this PageSetup.
        Represents the size of the left margin, in unit of centimeters.

        :return: The left_margin of this PageSetup.
        :rtype: float
        """
        return self.container['left_margin']

    @left_margin.setter
    def left_margin(self, left_margin):
        """
        Sets the left_margin of this PageSetup.
        Represents the size of the left margin, in unit of centimeters.

        :param left_margin: The left_margin of this PageSetup.
        :type: float
        """

        self.container['left_margin'] = left_margin

    @property
    def center_horizontally(self):
        """
        Gets the center_horizontally of this PageSetup.
        Represent if the sheet is printed centered horizontally.

        :return: The center_horizontally of this PageSetup.
        :rtype: bool
        """
        return self.container['center_horizontally']

    @center_horizontally.setter
    def center_horizontally(self, center_horizontally):
        """
        Sets the center_horizontally of this PageSetup.
        Represent if the sheet is printed centered horizontally.

        :param center_horizontally: The center_horizontally of this PageSetup.
        :type: bool
        """

        self.container['center_horizontally'] = center_horizontally

    @property
    def header_margin(self):
        """
        Gets the header_margin of this PageSetup.
        Represents the distance from the top of the page to the header, in unit of centimeters.

        :return: The header_margin of this PageSetup.
        :rtype: float
        """
        return self.container['header_margin']

    @header_margin.setter
    def header_margin(self, header_margin):
        """
        Sets the header_margin of this PageSetup.
        Represents the distance from the top of the page to the header, in unit of centimeters.

        :param header_margin: The header_margin of this PageSetup.
        :type: float
        """

        self.container['header_margin'] = header_margin

    @property
    def top_margin(self):
        """
        Gets the top_margin of this PageSetup.
        Represents the size of the top margin, in unit of centimeters.

        :return: The top_margin of this PageSetup.
        :rtype: float
        """
        return self.container['top_margin']

    @top_margin.setter
    def top_margin(self, top_margin):
        """
        Sets the top_margin of this PageSetup.
        Represents the size of the top margin, in unit of centimeters.

        :param top_margin: The top_margin of this PageSetup.
        :type: float
        """

        self.container['top_margin'] = top_margin

    @property
    def footer(self):
        """
        Gets the footer of this PageSetup.
        Represents the page footor.

        :return: The footer of this PageSetup.
        :rtype: list[PageSection]
        """
        return self.container['footer']

    @footer.setter
    def footer(self, footer):
        """
        Sets the footer of this PageSetup.
        Represents the page footor.

        :param footer: The footer of this PageSetup.
        :type: list[PageSection]
        """

        self.container['footer'] = footer

    @property
    def fit_to_pages_tall(self):
        """
        Gets the fit_to_pages_tall of this PageSetup.
        Represents the number of pages tall the worksheet will be scaled to when it's printed.

        :return: The fit_to_pages_tall of this PageSetup.
        :rtype: int
        """
        return self.container['fit_to_pages_tall']

    @fit_to_pages_tall.setter
    def fit_to_pages_tall(self, fit_to_pages_tall):
        """
        Sets the fit_to_pages_tall of this PageSetup.
        Represents the number of pages tall the worksheet will be scaled to when it's printed.

        :param fit_to_pages_tall: The fit_to_pages_tall of this PageSetup.
        :type: int
        """

        self.container['fit_to_pages_tall'] = fit_to_pages_tall

    @property
    def is_hf_scale_with_doc(self):
        """
        Gets the is_hf_scale_with_doc of this PageSetup.
        Indicates whether header and footer are scaled with document scaling.Only applies for Excel 2007. 

        :return: The is_hf_scale_with_doc of this PageSetup.
        :rtype: bool
        """
        return self.container['is_hf_scale_with_doc']

    @is_hf_scale_with_doc.setter
    def is_hf_scale_with_doc(self, is_hf_scale_with_doc):
        """
        Sets the is_hf_scale_with_doc of this PageSetup.
        Indicates whether header and footer are scaled with document scaling.Only applies for Excel 2007. 

        :param is_hf_scale_with_doc: The is_hf_scale_with_doc of this PageSetup.
        :type: bool
        """

        self.container['is_hf_scale_with_doc'] = is_hf_scale_with_doc

    @property
    def print_headings(self):
        """
        Gets the print_headings of this PageSetup.
        Represents if row and column headings are printed with this page.

        :return: The print_headings of this PageSetup.
        :rtype: bool
        """
        return self.container['print_headings']

    @print_headings.setter
    def print_headings(self, print_headings):
        """
        Sets the print_headings of this PageSetup.
        Represents if row and column headings are printed with this page.

        :param print_headings: The print_headings of this PageSetup.
        :type: bool
        """

        self.container['print_headings'] = print_headings

    @property
    def zoom(self):
        """
        Gets the zoom of this PageSetup.
        Represents the scaling factor in percent. It should be between 10 and 400.

        :return: The zoom of this PageSetup.
        :rtype: int
        """
        return self.container['zoom']

    @zoom.setter
    def zoom(self, zoom):
        """
        Sets the zoom of this PageSetup.
        Represents the scaling factor in percent. It should be between 10 and 400.

        :param zoom: The zoom of this PageSetup.
        :type: int
        """

        self.container['zoom'] = zoom

    @property
    def print_title_rows(self):
        """
        Gets the print_title_rows of this PageSetup.
        Represents the rows that contain the cells to be repeated at the top of each page.

        :return: The print_title_rows of this PageSetup.
        :rtype: str
        """
        return self.container['print_title_rows']

    @print_title_rows.setter
    def print_title_rows(self, print_title_rows):
        """
        Sets the print_title_rows of this PageSetup.
        Represents the rows that contain the cells to be repeated at the top of each page.

        :param print_title_rows: The print_title_rows of this PageSetup.
        :type: str
        """

        self.container['print_title_rows'] = print_title_rows

    @property
    def order(self):
        """
        Gets the order of this PageSetup.
        Represents the order that Microsoft Excel uses to number pages when printing a large worksheet.

        :return: The order of this PageSetup.
        :rtype: str
        """
        return self.container['order']

    @order.setter
    def order(self, order):
        """
        Sets the order of this PageSetup.
        Represents the order that Microsoft Excel uses to number pages when printing a large worksheet.

        :param order: The order of this PageSetup.
        :type: str
        """

        self.container['order'] = order

    @property
    def print_copies(self):
        """
        Gets the print_copies of this PageSetup.
        Get and sets number of copies to print.

        :return: The print_copies of this PageSetup.
        :rtype: int
        """
        return self.container['print_copies']

    @print_copies.setter
    def print_copies(self, print_copies):
        """
        Sets the print_copies of this PageSetup.
        Get and sets number of copies to print.

        :param print_copies: The print_copies of this PageSetup.
        :type: int
        """

        self.container['print_copies'] = print_copies

    @property
    def orientation(self):
        """
        Gets the orientation of this PageSetup.
        Represents page print orientation.

        :return: The orientation of this PageSetup.
        :rtype: str
        """
        return self.container['orientation']

    @orientation.setter
    def orientation(self, orientation):
        """
        Sets the orientation of this PageSetup.
        Represents page print orientation.

        :param orientation: The orientation of this PageSetup.
        :type: str
        """

        self.container['orientation'] = orientation

    @property
    def right_margin(self):
        """
        Gets the right_margin of this PageSetup.
        Represents the size of the right margin, in unit of centimeters.

        :return: The right_margin of this PageSetup.
        :rtype: float
        """
        return self.container['right_margin']

    @right_margin.setter
    def right_margin(self, right_margin):
        """
        Sets the right_margin of this PageSetup.
        Represents the size of the right margin, in unit of centimeters.

        :param right_margin: The right_margin of this PageSetup.
        :type: float
        """

        self.container['right_margin'] = right_margin

    @property
    def print_gridlines(self):
        """
        Gets the print_gridlines of this PageSetup.
        Represents if cell gridlines are printed on the page.

        :return: The print_gridlines of this PageSetup.
        :rtype: bool
        """
        return self.container['print_gridlines']

    @print_gridlines.setter
    def print_gridlines(self, print_gridlines):
        """
        Sets the print_gridlines of this PageSetup.
        Represents if cell gridlines are printed on the page.

        :param print_gridlines: The print_gridlines of this PageSetup.
        :type: bool
        """

        self.container['print_gridlines'] = print_gridlines

    @property
    def is_auto_first_page_number(self):
        """
        Gets the is_auto_first_page_number of this PageSetup.
        Indicates whether the first the page number is automatically assigned.

        :return: The is_auto_first_page_number of this PageSetup.
        :rtype: bool
        """
        return self.container['is_auto_first_page_number']

    @is_auto_first_page_number.setter
    def is_auto_first_page_number(self, is_auto_first_page_number):
        """
        Sets the is_auto_first_page_number of this PageSetup.
        Indicates whether the first the page number is automatically assigned.

        :param is_auto_first_page_number: The is_auto_first_page_number of this PageSetup.
        :type: bool
        """

        self.container['is_auto_first_page_number'] = is_auto_first_page_number

    @property
    def header(self):
        """
        Gets the header of this PageSetup.
        Represents the page header.

        :return: The header of this PageSetup.
        :rtype: list[PageSection]
        """
        return self.container['header']

    @header.setter
    def header(self, header):
        """
        Sets the header of this PageSetup.
        Represents the page header.

        :param header: The header of this PageSetup.
        :type: list[PageSection]
        """

        self.container['header'] = header

    @property
    def is_hf_diff_odd_even(self):
        """
        Gets the is_hf_diff_odd_even of this PageSetup.
        True means that the header/footer of the odd pages is different with odd pages.

        :return: The is_hf_diff_odd_even of this PageSetup.
        :rtype: bool
        """
        return self.container['is_hf_diff_odd_even']

    @is_hf_diff_odd_even.setter
    def is_hf_diff_odd_even(self, is_hf_diff_odd_even):
        """
        Sets the is_hf_diff_odd_even of this PageSetup.
        True means that the header/footer of the odd pages is different with odd pages.

        :param is_hf_diff_odd_even: The is_hf_diff_odd_even of this PageSetup.
        :type: bool
        """

        self.container['is_hf_diff_odd_even'] = is_hf_diff_odd_even

    @property
    def bottom_margin(self):
        """
        Gets the bottom_margin of this PageSetup.
        Represents the size of the bottom margin, in unit of centimeters.

        :return: The bottom_margin of this PageSetup.
        :rtype: float
        """
        return self.container['bottom_margin']

    @bottom_margin.setter
    def bottom_margin(self, bottom_margin):
        """
        Sets the bottom_margin of this PageSetup.
        Represents the size of the bottom margin, in unit of centimeters.

        :param bottom_margin: The bottom_margin of this PageSetup.
        :type: float
        """

        self.container['bottom_margin'] = bottom_margin

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.get_swagger_types()):
            value = self.get_from_container(attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, PageSetup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
