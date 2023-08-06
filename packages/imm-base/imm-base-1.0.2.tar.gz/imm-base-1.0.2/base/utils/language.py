from datetime import date, datetime
from pydantic import BaseModel
from typing import Union, Optional


class Language(BaseModel):
    """Base class for IELTS, CELPIP, TEF AND TCF"""

    reading: float
    writting: float
    listening: float
    speaking: float
    test_date: Optional[date]
    sign_date: Optional[date]

    def is_valid(self, the_day=date.today()):
        if not self.sign_date:
            raise ValueError("There is no sign data in Language object")
        if not isinstance(the_day, date):
            the_day = datetime.strptime(the_day, "%Y-%m-%d").date()
        return True if (the_day - self.sign_date).days < 730 else False

    def __str__(self):
        return f"{self.reading},{self.writting},{self.listening},{self.speaking}"

    class Meta:
        abstract = True


class CLB:
    """CLB to IELTS., CELPIP, TEF and TCF converter"""

    # 1. IELTS->CLB level, Reading	Writing	Listening	Speaking
    ielts_table = [
        [10, 8.0, 7.5, 8.5, 7.5],
        [9, 7.0, 7.0, 8.0, 7.0],
        [8, 6.5, 6.5, 7.5, 6.5],
        [7, 6.0, 6.0, 6.0, 6.0],
        [6, 5.0, 5.5, 5.5, 5.5],
        [5, 4.0, 5.0, 5.0, 5.0],
        [4, 3.5, 4.0, 4.5, 4.0],
    ]
    tef_table = [
        [10, 263, 277, 393, 415, 316, 333, 393, 415],
        [9, 248, 262, 371, 392, 298, 315, 371, 392],
        [8, 233, 247, 349, 370, 280, 297, 349, 370],
        [7, 207, 232, 310, 348, 249, 279, 310, 348],
        [6, 181, 206, 271, 309, 217, 248, 271, 309],
        [5, 151, 180, 226, 270, 181, 216, 226, 270],
        [4, 121, 150, 181, 225, 145, 180, 181, 225],
    ]
    tcf_table = [
        [10, 549, 699, 16, 20, 549, 699, 16, 20],
        [9, 524, 548, 14, 15, 523, 548, 14, 15],
        [8, 499, 523, 12, 13, 503, 522, 12, 13],
        [7, 453, 498, 10, 11, 458, 502, 10, 11],
        [6, 406, 452, 7, 9, 398, 457, 7, 9],
        [5, 375, 405, 6, 6, 369, 397, 6, 6],
        [4, 342, 374, 4, 5, 331, 368, 4, 5],
    ]

    def __init__(self, clb_level):
        self.level = clb_level
        self.level = 10 if self.level > 10 else self.level

    # input CLB level, return r w l s of IELTS
    def to_ielts(self):
        if self.level < 4:
            return [0, 0, 0, 0]
        index = 10 - self.level
        return CLB.ielts_table[index][1:5]

    # 输入CLB值 返回对应的tef r w l s分数列表
    def to_tef(self):
        if self.level < 4:
            return [0, 0, 0, 0, 0, 0, 0, 0]
        index = 10 - self.level
        return CLB.tef_table[index][1:9]

        # 输入CLB值 返回对应的tef r w l s分数列表

    def to_tcf(self):
        if self.level < 4:
            return [0, 0, 0, 0, 0, 0, 0, 0]
        index = 10 - self.level
        return CLB.tcf_table[index][1:9]


class IELTS(Language):
    reading: float
    writting: float
    listening: float
    speaking: float
    type_of_test: Optional[str] = "General"
    report_number: Optional[str]

    # def __init__(self, ielts: dict):
    #     super().__init__(**ielts)
    #     self.type_of_test = ielts.get("type_of_test") or "General"
    #     self.report_number = ielts.get("report_number") or ""

    def _ielts_2_clbs(self):
        ielts = [self.reading, self.writting, self.listening, self.speaking]
        clb_level = []
        for column in range(1, 5):  # 从读到说，4个列，从1开始，开始找对应的clb级别
            factor = float(ielts[column - 1])  # r w l s每个子项
            for level in range(0, 7):  # 从CLB 级别10一直找到4 7行
                if factor > CLB.ielts_table[0][column]:  # 如果语言成绩高于最高分，按照最高分算
                    clb_level.append(10)
                    break
                if factor < CLB.ielts_table[6][column]:  # 如果低于最低分，则CLB Level =0 跳出本列循环
                    clb_level.append(0)
                    break
                # 要算每个子项的CLB值
                if CLB.ielts_table[level][column] == ielts[column - 1]:
                    clb_level.append(CLB.ielts_table[level][0])  # 得到该雅思成绩对应的CLB 级别
                    break
            # 如果某项分数不在阵列中
            for level in range(1, 7):
                if (
                    CLB.ielts_table[level][column]
                    < factor
                    < CLB.ielts_table[level - 1][column]
                ):
                    clb_level.append(CLB.ielts_table[level][0])  # 得到该雅思成绩对应的CLB 级别
                    break
        return clb_level

    # public class mothod for returning single factor's clb level. reading:0, writing:1, listening:2, speaking:3
    @classmethod
    def ielts_2_clb(self, score, factor_index):
        column = factor_index + 1
        for level in range(0, 7):  # 从CLB 级别10一直找到4 7行
            if score > CLB.ielts_table[0][column]:  # 如果语言成绩高于最高分，按照最高分算
                return 10
            if score < CLB.ielts_table[6][column]:  # 如果低于最低分，则CLB Level =0 跳出本列循环
                return 0
            # 要算每个子项的CLB值
            if CLB.ielts_table[level][column] == score:
                return CLB.ielts_table[level][0]  # 得到该雅思成绩对应的CLB 级别
        # 如果某项分数不在阵列中
        for level in range(1, 7):
            if (
                CLB.ielts_table[level][column]
                < score
                < CLB.ielts_table[level - 1][column]
            ):
                return CLB.ielts_table[level][0]  # 得到该雅思成绩对应的CLB 级别

    @property
    def clb_r(self):
        return self._ielts_2_clbs()[0]

    @property
    def clb_w(self):
        return self._ielts_2_clbs()[1]

    @property
    def clb_l(self):
        return self._ielts_2_clbs()[2]

    @property
    def clb_s(self):
        return self._ielts_2_clbs()[3]

    @property
    def clb(self):
        return min(self.clb_r, self.clb_w, self.clb_l, self.clb_s)


class CELPIP(Language):
    reading: int
    writting: int
    listening: int
    speaking: int
    registration_number: Optional[str]
    pin_number: Optional[str]

    # def __init__(self, celpip: dict):
    #     super().__init__(**celpip)
    #     self.registration_number = celpip.get("registration_number") or ""
    #     self.pin_number = celpip.get("pin_number") or ""

    @property
    def clb_r(self):
        return self.reading

    @property
    def clb_w(self):
        return self.writting

    @property
    def clb_l(self):
        return self.listening

    @property
    def clb_s(self):
        return self.speaking

    @property
    def clb(self):
        return min(self.reading, self.writting, self.listening, self.speaking)


class TEF(Language):
    # def __init__(self, tef: dict):
    #     super().__init__(**tef)

    def _tef_2_clbs(self):
        if self.reading not in range(121, 278):
            raise ValueError("TEF reading score is invalid")
        if self.writting not in range(181, 416):
            raise ValueError("TEF writing score is invalid")
        if self.listening not in range(145, 334):
            raise ValueError("TEF listening score is invalid")
        if self.speaking not in range(181, 416):
            raise ValueError("TEF speaking score is invalid")

        rwls = [self.reading, self.writting, self.listening, self.speaking]
        clb = []
        for column in range(0, 4):  # r w l s
            for row in range(0, 7):
                start = (column + 1) * 2 - 1
                end = (column + 1) * 2
                if rwls[column] in range(
                    CLB.tef_table[row][start], CLB.tef_table[row][end] + 1
                ):
                    clb.append(CLB.tef_table[row][0])
                    break
        return clb

    @property
    def clb_r(self):
        return self._tef_2_clbs()[0]

    @property
    def clb_w(self):
        return self._tef_2_clbs()[1]

    @property
    def clb_l(self):
        return self._tef_2_clbs()[2]

    @property
    def clb_s(self):
        return self._tef_2_clbs()[3]

    @property
    def clb(self):
        return min(self.clb_r, self.clb_w, self.clb_l, self.clb_s)


class TCF(Language):
    # def __init__(self, tcf: dict):
    #     super().__init__(**tcf)

    def _tcf_2_clbs(self):
        if self.reading not in range(342, 700):
            raise ValueError("TCF reading score is invalid")
        if self.writting not in range(4, 21):
            raise ValueError("TCF writing score is invalid")
        if self.listening not in range(331, 700):
            raise ValueError("TCF listening score is invalid")
        if self.speaking not in range(4, 21):
            raise ValueError("TCF speaking score is invalid")

        rwls = [self.reading, self.writting, self.listening, self.speaking]
        clb = []
        for column in range(0, 4):  # r w l s
            for row in range(0, 7):
                start = (column + 1) * 2 - 1
                end = (column + 1) * 2
                if rwls[column] in range(
                    CLB.tcf_table[row][start], CLB.tcf_table[row][end] + 1
                ):
                    clb.append(CLB.tcf_table[row][0])
                    break
        return clb

    @property
    def clb_r(self):
        return self._tcf_2_clbs()[0]

    @property
    def clb_w(self):
        return self._tcf_2_clbs()[1]

    @property
    def clb_l(self):
        return self._tcf_2_clbs()[2]

    @property
    def clb_s(self):
        return self._tcf_2_clbs()[3]

    @property
    def clb(self):
        return min(self.clb_r, self.clb_w, self.clb_l, self.clb_s)
