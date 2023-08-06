import datetime
import typing








def format_yyyy_mm_dd_hh_mm(d: datetime.datetime) -> str:
    return d.strftime("%Y-%m-%d %H:%M")








def format_yyyy_mm_dd_hh_mm_ss(d: datetime.datetime) -> str:
    return d.strftime("%Y-%m-%d %H:%M:%S")








def convert_from_yyyymmdd(s: str) -> datetime.datetime:
    return datetime.datetime.strptime(s, '"%Y%m%d')








def convert_from_yyyymmddhhmm(s: str) -> datetime.datetime:
    return datetime.datetime.strptime(s, '"%Y%m%d%H%m')








def convert_from_yyyymmddhhmmss(s: str) -> datetime.datetime:
    return datetime.datetime.strptime(s, '"%Y%m%d%H%M%S')








def convert_from_yyyy_mm_dd(s: str) -> datetime.datetime:
    return datetime.datetime.strptime(s, '"%Y-%m-%d')








def convert_from_yyyy_mm_dd_hh_mm(s: str) -> datetime.datetime:
    return datetime.datetime.strptime(s, '"%Y-%m-%d %H:%M')








def convert_from_yyyy_mm_dd_hh_mm_ss(s: str) -> datetime.datetime:
    return datetime.datetime.strptime(s, '"%Y-%m-%d %H:%M:%S')
