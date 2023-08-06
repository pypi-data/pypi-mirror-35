# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import getopt
import sys
from builtins import input

from lxml import etree
from zeep import Client

from NUAAiCal.settings import DEBUG, VERSION
from NUAAiCal.FindFirstDayofSemester import get_semester_start_date
from NUAAiCal.GenerateICS import create_ics, export_ics
from NUAAiCal.Lesson import Lesson


def usage():
    print('''Usage:
    -v, --version   Check NUAAiCal version
    -h, --help      Display this help text
    ''')


def main():
    shortopts = "hv"
    longopts = ['help', 'version']
    try:
        options, args = getopt.getopt(sys.argv[1:], shortopts, longopts)
        for opt, arg in options:
            if opt in ('-v', '--version'):
                print('NUAAiCal ' + VERSION)
                exit(0)
            elif opt in ('-h', '--help'):
                usage()
                exit(0)

    except getopt.GetoptError:
        pass

    client = Client(
        'http://ded.nuaa.edu.cn/NetEa/Services/WebService.asmx?WSDL')

    print("======== NUAA iCal Python ========")
    print("Repo: https://github.com/Triple-Z/NUAA-iCal-Python")
    print("Please help me STAR this project if it is useful~")
    print("Pull requests (PR) welcome!")

    if DEBUG:
        xn = '2017-2018'
        xq = '2'
        xh = '161540121'
        # semester_start_date = datetime(2018, 2, 26, 0, 0, 0)
        print("==================================================")
    else:
        print("\n输入提示：")
        print('学年: 2017-2018')
        print('学期: 1 (上学期) / 2 (下学期)')
        print('学号: 你的南京航空航天大学学号')
        print("-------- 请填写以下信息 --------")

        try:
            xn = input("学年: ")
        except UnicodeEncodeError:
            # fucking python 2.7 unicode
            xn = input("学年: ".encode('utf-8'))

    if '-' in xn:

        try:
            years = xn.split('-')
            start_year = int(years[0])
            end_year = int(years[1])
        except ValueError:
            print("学年输入错误: " + xn)
        else:

            if not DEBUG:
                try:
                    xq = input('学期: ')
                except UnicodeEncodeError:
                    xq = input('学期: '.encode('utf-8'))

                if not (xq == '1' or xq == '2'):
                    print("学期输入错误！ 提示：1为上学期，2为下学期！")
                    exit()

                try:
                    xh = input('学号: ')
                except UnicodeEncodeError:
                    xh = input('学号: '.encode('utf-8'))

                print("==================================================")

            semester_start_date = get_semester_start_date(years, xq, client)

            if not semester_start_date:
                print("未能获得学年 " + xn + " 的校历信息")
                exit()

            request_data = {
                'xn': xn,
                'xq': xq,
                'xh': xh,
            }

            with client.options(raw_response=True):
                response = client.service.GetCourseTableByXh(**request_data)
                root = etree.fromstring(response.content)
                body = root[0]
                GetCourseTableByXhResponse = body[0]
                GetCourseTableByXhResult = GetCourseTableByXhResponse[0]
                try:
                    NewDataSet = list(GetCourseTableByXhResult[1][1])
                except IndexError:
                    print(xn + '学年第' + xq + '学期没有课程！')
                else:
                    # print(len(NewDataSet))

                    lessons = list()

                    # Add lessons
                    for ds in NewDataSet:
                        # Explain XML
                        year = ds.find('xn').text
                        semester = ds.find('xq').text
                        student_number = ds.find('xh').text
                        lesson_order_number = ds.find('kcxh').text
                        lesson_number = ds.find('kch').text
                        name = ds.find('kcm').text
                        teacher_number = ds.find('jsh').text
                        teacher_name = ds.find('jsm').text
                        school_distinct = ds.find('xiaoqu').text
                        day_of_week = ds.find('week').text
                        unit = ds.find('unit').text
                        lsjs = ds.find('lsjs').text  # what is this???
                        room_number = ds.find('roomid').text
                        weeks = list(map(int, ds.find('weeks').text.split(',')))

                        new_lesson = Lesson(year, semester, student_number,
                                            lesson_order_number,
                                            lesson_number, name, teacher_number,
                                            teacher_name,
                                            school_distinct, day_of_week, unit,
                                            lsjs,
                                            room_number, weeks)

                        lessons.append(new_lesson)

                    # Print all lessons in cli
                    # for lesson in lessons:
                    #     lesson._print()

                    cal = create_ics(lessons, semester_start_date)
                    export_ics(cal, xn, xq, xh)
                    return True
    else:
        print("学年输入错误: " + xn)
