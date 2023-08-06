from datetime import datetime, date
from enum import Enum, unique
from difflib import Differ
import re
from fuzzywuzzy import fuzz
from typing import Union, List
from json import JSONEncoder
from pydantic import ValidationError
import json
from .context import DATADIR
from datetime import datetime, date, timedelta
from pydantic import BaseModel
from typing import List, Optional
import re
from rich.table import Table

# This function used to check a list's continuity of date. The list must have two columns as start date and end date.
# The fromat must be "yyyy-mm-dd" or "yyy-mm".  The list has to be from most recent to past. You can force sort it by assign sort =True
# The output will be True or False, plus sorted input list and message.
# start_line is set start number in list. normally is 0, but in source excel, it starts from 4
def checkContinuity(data_set: list, sort=False, start_line=1):
    if sort:
        data_set = sorted(data_set, key=lambda x: (x[0], x[1]), reverse=True)
    ok = []
    errors = []

    def difference(l1, l2):
        if type(l1) == date:
            l1 = l1.strftime("%Y-%m-%d")
        if type(l2) == date:
            l2 = l2.strftime("%Y-%m-%d")

        if l2 == None or l2 == "Present":
            l2 = (
                datetime.today().strftime("%Y-%m-%d")
                if bool(re.search(r"^\d{4}-\d{2}-\d{2}", l1))
                else datetime.today().strftime("%Y-%m")
            )
        if bool(re.search(r"^\d{4}-\d{2}-\d{2}", l1)) and bool(
            re.search(r"^\d{4}-\d{2}-\d{2}", l2)
        ):
            current_start = datetime.strptime(l1, "%Y-%m-%d")
            previous_end = datetime.strptime(l2, "%Y-%m-%d")
            return (current_start - previous_end).days, "day(s)"
        if bool(re.search(r"^\d{4}-\d{2}", l1)) and bool(
            re.search(r"^\d{4}-\d{2}", l2)
        ):
            y1, m1 = l1.split("-")
            y2, m2 = l2.split("-")
            return (int(y1) - int(y2)) * 12 + int(m1) - int(m2), "month(s)"

    for i in range(len(data_set) - 1):
        diff, unit = difference(data_set[i][0], data_set[i + 1][1])
        if diff > 1:
            ok.append(False)
            errors.append(
                f"{'List sorted. ' if sort else ''}The date is not continuous between row {i+start_line}: {data_set[i][0]} to row {i+start_line+1}:  {data_set[i+1][1]} (missed {diff-1} {unit})"
            )
        elif diff < 0:
            ok.append(False)
            errors.append(
                f"{'List sorted. ' if sort else ''}The date is not continuous between row {i++start_line}: {data_set[i][0]} to row {i+start_line+1}: {data_set[i+1][1]} (overlapped {diff} {unit})"
            )
        else:
            ok.append(True)
    if all(ok):
        return True, data_set, "date is continuous"
    else:
        return False, data_set, errors


# newe version for date continuity check
class DateRange(BaseModel):
    start_date: date
    end_date: Optional[date]

    def print(self):
        print(self.start_date, self.end_date)


def check_date_continuity(date_list: list, start_line=1):
    date_ranges = [DateRange(start_date=d[0], end_date=d[1]) for d in date_list]
    ok = []
    errors = []

    for i in range(0, len(date_ranges) - 1):
        the_end_date = date_ranges[i + 1].end_date
        the_end_date = the_end_date if the_end_date else datetime.today().date()
        the_start_date = date_ranges[i].start_date
        diff = the_start_date - the_end_date
        if diff.days > 1:
            ok.append(False)
            errors.append(
                f"The date is not continious between row {i+start_line}: {the_start_date} to row {i+start_line+1}:  {the_end_date} (missed {diff.days} day(s))"
            )
        else:
            ok.append(True)

    if all(ok):
        return True, "date is continious"
    else:
        return False, errors


#  Used to find different between two text strings. Initialize with tc=TextChanged(t1,t2), and get differences by tc.text_added or tc.text_deleted
class TextChanged:
    def __init__(self, text1, text2):
        self.text1 = text1
        self.text2 = text2

    def __get_changed(self):

        t1_lines = self.text1.splitlines()
        t2_lines = self.text2.splitlines()

        diff = Differ().compare(t1_lines, t2_lines)
        changed = list(diff)

        added = r"^\+\s(.+)"
        deleted = r"^\-\s(.+)"
        text_added = [
            d[2:] for d in changed if re.findall(added, d)
        ]  # d[2:] delete '+ ' at the begining
        text_added = "\n".join(text_added)
        text_deleted = [d[2:] for d in changed if re.findall(deleted, d)]
        text_deleted = "\n".join(text_deleted)

        return {"text_added": text_added, "text_deleted": text_deleted}

    @property
    def text_added(self):
        return self.__get_changed()["text_added"]

    @property
    def text_deleted(self):
        return self.__get_changed()["text_deleted"]


def best_match(term, list_names, min_score=0, return_score=False, to_lowercase=False):
    max_score = -1
    max_name = ""
    for term2 in list_names:
        if to_lowercase:
            term = term.lower()
            score = fuzz.ratio(term, term2.lower())
        else:
            score = fuzz.ratio(term, term2)
        if (score > min_score) and (score > max_score):
            max_name = term2
            max_score = score
    if return_score:
        return max_name, max_score
    else:
        return max_name


def append_ext(filename: Union[str, List[str]], ext):
    def convert(fn):
        names = fn.split(".")
        if len(names) == 2:
            return fn
        elif len(names) == 1:
            return names[0] + ext
        else:
            raise ValueError(f"{filename} is invalid filename")

    if type(filename) == list:
        return [convert(fn) for fn in filename]
    else:
        return convert(filename)


def remove_ext(filename: Union[str, List[str]]):
    def convert(fn):
        names = fn.split(".")
        if len(names) >= 1:
            return names[0]
        else:
            raise ValueError(f"{filename} is invalid filename")

    if type(filename) == list:
        return [convert(fn) for fn in filename]
    else:
        return convert(filename)


def markdown_title_list(ds: list[str], title=None, title_level=4):
    output = ""
    if title:
        output += "#" * title_level + " " + title + "\n"
    for data in ds:
        output += "- " + data + "\n"
    return output

# input list and outpout markdown table text
def markdown_table(ds: list):
    head = ds[0]
    head_str = "|"
    head_sep = "|"
    for col in range(0, len(ds[0])):
        head_str += str(head[col]) + "|"
        head_sep += "------------- " + "|"
    # print(head_str)
    # print(head_sep)
    output = head_str + "\n" + head_sep + "\n"

    row_data = "|"
    for row in range(1, len(ds)):
        for col in range(0, len(ds[0])):
            row_data += str(ds[row][col]) + "|"
        # print(row_data)
        output += row_data + "\n"
        row_data = "|"

    return output


# Some common input functions
def multi_line_input():
    print("Ctrl-D  to save it.")
    contents = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        contents.append(line)
    return "\n".join(contents)


# 打印1D的列表为多行
def printList(ls, index=True, sep="\t"):  # 打印list，默认在前面加上index，用tab分割
    i = 0
    for l in ls:
        item = f"{i}{sep}{l}" if index == True else f"{l}"
        print(item)
        i += 1


# 将列表变成一行字符串
def ListInline(ls, sep="\t"):
    item = ""
    for l in ls:
        item = item + f"{l}{sep}"
    return item


# 打印2D的列表
def printList2D(ls, index=False, sep="\t"):
    i = 0
    item = ""
    for l in ls:
        line = ListInline(l, sep)
        item = f"{i}{sep}{line}" if index == True else f"{line}{sep}"
        print(item)
        i += 1


# 使用tabulate 打印formatted 2D的list为表格
def printFList2D(ls, index=False):
    # API_CLEAN: only client code use this function, move import here in stead of at the top
    from tabulate import tabulate

    i = 0
    items = []
    for l in ls:
        if index == True:
            l.insert(0, i)
            items.append(l)

        else:
            items.append(l)
        i += 1
    print(tabulate(items))


# formatter of money
def formatMoney(number: float, currency_type="$"):
    return currency_type + "{:,.2f}".format(number)


# join string as speaking language
def speaking_list(l: list):
    if len(l) == 1:
        result = l[0]
    elif len(l) == 2:
        result = " and ".join(l)
    elif len(l) > 2:
        result = ", ".join(l[:-1]) + " and " + l[-1]
    else:
        result = ""
    return result


# make table based on rich
def makeTable(table_name, table_list: list,with_footer:bool=False,highlight_rows:Union[List[int],None]=None,highlight_style="bold green"):
    """ 
    Make a rich table
    - highlight_rows refers only to data list, header or footer doesn't count
    """
    if len(table_list)==0:
        raise ValueError("The table has no data")
 
    table = Table(title=table_name,show_footer=with_footer)
    titles = table_list.pop(0) 
    if with_footer:
        if len(table_list)==0:
            raise ValueError("The table has no data")
        footers=table_list.pop(-1) 
        for i,title in enumerate(titles):
            table.add_column(header=title,footer=footers[i], justify="left", style="cyan", no_wrap=False)
    else:
        for i,title in enumerate(titles):
            table.add_column(header=title, justify="left", style="cyan", no_wrap=False)        

    for i,content in enumerate(table_list):
        content_strings=[str(c) for c in content]
        style=highlight_style if highlight_rows and i in highlight_rows else None
        table.add_row(*content_strings,style=style)

    return table


class DateEncoder(JSONEncoder):
    # Override the default method
    def default(self, obj):
        if isinstance(obj, (date)):
            return obj.strftime("%Y-%m-%d")


def print_validation_error(e: ValidationError, language="English"):
    dict_file = (
        DATADIR / "excel" / "sysdict.json"
        if language.lower() == "english"
        else DATADIR / "excel" / language.lower() / "sysdict.json"
    )
    with open(dict_file, "r") as f:
        sysdict = json.load(f)

    loc_msg = ""
    error_msg = ""
    for err in e.errors():
        """
        match len(err['loc']):
            case 1:
                loc_msg=f'sheet {err["loc"][0]} is not existed: '
            case 2: # sheet error
                sheet,variable=err['loc']
                description=sysdict[sheet].get(variable) or variable# get description to replace variable
                loc_msg=f"info-{sheet}->{description}: "
            case 3: # table error
                table,row,variable=err['loc']
                description=sysdict[table].get(variable) or variable # get description to replace variable
                loc_msg=f"table-{table}->{description}->row {row}: "
            case  _:
                locs=[]
                for loc in err['loc']:
                    locs.append(str(loc))
                loc_msg="->".join(locs)+": "
        """
        err_len = len(err["loc"])
        if err_len == 1:
            loc_msg = f'sheet {err["loc"][0]} is not existed: '
        elif err_len == 2:
            sheet, variable = err["loc"]
            description = (
                sysdict[sheet].get(variable) or variable
            )  # get description to replace variable
            loc_msg = f"info-{sheet}->{description}: "
        elif err_len == 3:
            table, row, variable = err["loc"]
            description = (
                sysdict[table].get(variable) or variable
            )  # get description to replace variable
            loc_msg = f"table-{table}->{description}->row {row+4}: "
        else:
            locs = []
            for loc in err["loc"]:
                locs.append(str(loc))
            loc_msg = "->".join(locs) + ": "
        error_msg += loc_msg + err["msg"] + "\n"
    return error_msg


def age(original_dob):
    the_day = date.today()
    dob = (
        datetime.strptime(original_dob, "%Y-%m-%d")
        if not isinstance(original_dob, date)
        else original_dob
    )
    return (
        the_day.year - dob.year - ((the_day.month, the_day.day) < (dob.month, dob.day))
    )


def remove_non_ascii(string: Union[str, List[str]]):
    if type(string) == str:
        return re.sub(r"[^\x00-\x7F]+", " ", string)
    elif type(string) == list:
        return [re.sub(r"[^\x00-\x7F]+", " ", s) for s in string]

# to check if the_tags all in tags
def is_in_tags(the_tags: Union[str, list[str]], tags):
    if type(the_tags) == str:
        the_tags = the_tags.split(" ")

    is_in = []
    for the_tage in the_tags:
        is_in.append(True) if the_tage in tags else is_in.append(False)

    return all(is_in)


""" Transpose a 2D list """
def transpose_list(list2d:list):
    # Zip the data and transpose it
    transposed = [list(row) for row in zip(*list2d)]
    return transposed


def sort_list_by_index(list2d:list,index:int):
    # Sort the list by index
    return sorted(list2d, key=lambda x: x[index])

    
