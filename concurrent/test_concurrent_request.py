import aiohttp
import asyncio
import time

# 配置请求的目标 URL 和并发数量
# TARGET_URL = "http://localhost:8865/api/search/person/rerank"
TARGET_URL = "http://localhost/search/api/search/person/rerank"
CONCURRENT_REQUESTS = 100  # 并发请求数量

HEADERS = {
    "Content-Type": "application/json",
    "x-traceid": "288c973d-0095-4325-9452-1ce1e90b422b"
}

DATA = {
    "query": "王岩",
    "user_info": {
        "user_name": "魏东",
        "full_dept_name": "标准化默认-北京市-北京市人民政府-北京市政务服务和数据管理局-北京市大数据中心-数据应用部",
        "user_id": "mulzxfsVIBmwXz2K1cALT"
    },
    "cand_list": [
        {
            "user_id": "0",
            "user_name": "王岩",
            "remark": "王岩局长的秘书",
            "full_dept_name": [
                "北京市-北京市人民政府-市人力资源社会保障局-北京市劳动能力鉴定中心-数据管理部",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心",
                "北京市-北京市人民政府-市投资促进服务中心-区域促进处（信息数据处）",
                "北京市-北京市辖区-北京经济技术开发区-档案数据中心",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-节能与综合利用科"
            ],
            "positions": [
                "暂未填写"
            ],
            "is_friend": True,
            "is_top": True,
            "is_follower": True,
            "session_time": 1748655185,
            "base_score": 59.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "1",
            "user_name": "王岩",
            "remark": "王艳丽局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京市大兴区-政府口单位-大兴区审计局-电子数据审计科",
                "北京市-北京市辖区-北京市门头沟区-门头沟区政府-门头沟区审计局-电子数据审计科"
            ],
            "positions": [
                "测试负责人",
                "暂未填写"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": True,
            "session_time": 1749173585,
            "base_score": 64.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "2",
            "user_name": "王岩",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-综合部",
                "北京市-北京市辖区-北京市密云区-密云区政府-密云区审计局-电子数据审计科",
                "北京市-中共北京市委员会-市委组织部-干部信息管理处（数据中心）",
                "北京市-北京市辖区-北京市延庆区-延庆区政府工作部门-延庆区经济和信息化局-大数据中心-信息技术科",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）"
            ],
            "positions": [
                "九级管理岗",
                "暂未填写"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": False,
            "session_time": 1749432785,
            "base_score": 22.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "3",
            "user_name": "汪研",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市人民政府-市人力资源社会保障局-北京市劳动能力鉴定中心-数据管理部",
                "北京市-北京市辖区-北京市大兴区-其他单位-疫情防控工作领导小组-疫情防控办公室-信息数据组",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-办公室",
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-标准与安全部",
                "北京市-北京市辖区-北京市怀柔区-北京市怀柔区人民政府-怀柔区审计局-区审计局电子数据审计中心"
            ],
            "positions": [
                "测试负责人",
                "暂未填写"
            ],
            "is_friend": True,
            "is_top": True,
            "is_follower": True,
            "session_time": 1749778385,
            "base_score": 60.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "4",
            "user_name": "王岩",
            "remark": "王岩局长的秘书",
            "full_dept_name": [
                "北京市-北京市人民政府-市人力资源社会保障局-北京市社会保险基金管理中心-数据管理部"
            ],
            "positions": [
                "九级管理岗"
            ],
            "is_friend": False,
            "is_top": True,
            "is_follower": True,
            "session_time": 1749864785,
            "base_score": 28.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "5",
            "user_name": "王岩",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心"
            ],
            "positions": [
                "九级管理岗",
                "暂未填写"
            ],
            "is_friend": False,
            "is_top": True,
            "is_follower": False,
            "session_time": 1749432785,
            "base_score": 31.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "6",
            "user_name": "王艳",
            "remark": "王岩局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京市朝阳区-朝阳区政府-朝阳区城管指挥中心-数据分析科",
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-综合部",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-政研组",
                "北京市-北京市辖区-北京市石景山区-石景山区区政府-石景山区统计局-数据应用科",
                "北京市-北京市辖区-北京市延庆区-延庆区政府工作部门-延庆区审计局-数据审计分析中心"
            ],
            "positions": [
                "测试负责人",
                "九级管理岗"
            ],
            "is_friend": False,
            "is_top": True,
            "is_follower": False,
            "session_time": 1749000785,
            "base_score": 58.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "7",
            "user_name": "王岩",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-创新发展科"
            ],
            "positions": [
                "暂未填写",
                "九级管理岗"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": False,
            "session_time": 1748741585,
            "base_score": 74.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "8",
            "user_name": "王艳",
            "remark": "王岩局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京市大兴区-镇、街道-长子营镇-科室站所-长子营镇政府机关数据组"
            ],
            "positions": [
                "暂未填写"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": True,
            "session_time": 1749605585,
            "base_score": 49.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "9",
            "user_name": "汪研",
            "remark": "王岩局长的秘书",
            "full_dept_name": [
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-综合部",
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区科技和信息化局（区大数据局）-办公室",
                "北京市-北京市辖区-北京经济技术开发区-行政审批局-大数据处",
                "北京市-北京市人民政府-市卫生健康委-市属医院-北京天坛医院-信息管理与数据中心"
            ],
            "positions": [
                "测试负责人",
                "九级管理岗"
            ],
            "is_friend": False,
            "is_top": True,
            "is_follower": True,
            "session_time": 1749864785,
            "base_score": 53.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "10",
            "user_name": "汪研",
            "remark": "王岩局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-经济运行科",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-编辑室",
                "北京市-北京市辖区-北京市西城区-西城区政府-西城区审计局-电子数据科"
            ],
            "positions": [
                "暂未填写",
                "测试负责人"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": False,
            "session_time": 1748741585,
            "base_score": 53.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "11",
            "user_name": "王岩",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-软件和信息产业科",
                "北京市-北京市辖区-北京市昌平区-昌平区属企业-回天大脑试点-大数据中心",
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心",
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区科技和信息化局（区大数据局）-大数据应用科"
            ],
            "positions": [
                "测试负责人"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": False,
            "session_time": 1749778385,
            "base_score": 56.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "12",
            "user_name": "王艳",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-节能与综合利用科",
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区统计局-数据应用科",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-区制造业创新发展促进中心"
            ],
            "positions": [
                "测试负责人"
            ],
            "is_friend": False,
            "is_top": True,
            "is_follower": True,
            "session_time": 1748655185,
            "base_score": 16.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "13",
            "user_name": "王艳",
            "remark": "王艳丽局长的秘书",
            "full_dept_name": [
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心"
            ],
            "positions": [
                "九级管理岗",
                "暂未填写"
            ],
            "is_friend": True,
            "is_top": True,
            "is_follower": False,
            "session_time": 1749259985,
            "base_score": 78.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "14",
            "user_name": "王岩臣",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市辖区-北京市朝阳区-朝阳区政府-朝阳区卫生健康系统-直属行政和事业单位-朝阳区卫生信息中心-信息安全与数据服务部",
                "北京市-北京市辖区-北京市西城区-西城区政府-西城区科技和信息化局-数据资源管理科"
            ],
            "positions": [
                "暂未填写",
                "测试负责人"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": True,
            "session_time": 1749691985,
            "base_score": 100.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "15",
            "user_name": "王艳",
            "remark": "王艳丽局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京市大兴区-镇、街道-长子营镇-科室站所-长子营镇政府机关数据组",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-软件和信息产业科",
                "北京市-北京市辖区-北京经济技术开发区-档案数据中心-档案数据处"
            ],
            "positions": [
                "九级管理岗"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": True,
            "session_time": 1749432785,
            "base_score": 88.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "16",
            "user_name": "王艳",
            "remark": "王岩局长的秘书",
            "full_dept_name": [
                "北京市-临时-北京市运行保障指挥部-技术服务保障组-市公安局-办公室-办公室数据中心（科信办）",
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区科技和信息化局（区大数据局）-大数据应用科"
            ],
            "positions": [
                "测试负责人"
            ],
            "is_friend": True,
            "is_top": True,
            "is_follower": True,
            "session_time": 1749000785,
            "base_score": 91.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "17",
            "user_name": "王艳",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市辖区-北京市丰台区-丰台区政府-丰台区科技信息化局-大数据管理科",
                "北京市-北京市辖区-北京市朝阳区-朝阳区政府-朝阳区卫生健康系统-直属行政和事业单位-朝阳区卫生信息中心-信息安全与数据服务部",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-办公室"
            ],
            "positions": [
                "测试负责人"
            ],
            "is_friend": False,
            "is_top": True,
            "is_follower": True,
            "session_time": 1749691985,
            "base_score": 95.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "18",
            "user_name": "汪研",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-财务室",
                "北京市-北京市辖区-北京经济技术开发区-档案数据中心-史志综合处",
                "北京市-北京市辖区-北京经济技术开发区-档案数据中心-领导",
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-发展规划部"
            ],
            "positions": [
                "九级管理岗",
                "暂未填写"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": False,
            "session_time": 1749864785,
            "base_score": 4.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "19",
            "user_name": "王岩",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-财务室",
                "北京市-北京市辖区-北京市昌平区-昌平区属企业-回天大脑试点-大数据中心"
            ],
            "positions": [
                "测试负责人"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": False,
            "session_time": 1748655185,
            "base_score": 50.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "20",
            "user_name": "王艳",
            "remark": "王艳丽局长的秘书",
            "full_dept_name": [
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-数据管理部"
            ],
            "positions": [
                "九级管理岗"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": False,
            "session_time": 1749087185,
            "base_score": 89.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "21",
            "user_name": "王艳",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）",
                "北京市-北京市人民政府-市水务局-局属单位-北京市智慧水务发展研究院-数据管理中心",
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区科技和信息化局（区大数据局）-办公室",
                "北京市-北京市人民政府-市经济和信息化局-内设机构-大数据建设处"
            ],
            "positions": [
                "测试负责人"
            ],
            "is_friend": True,
            "is_top": True,
            "is_follower": False,
            "session_time": 1748741585,
            "base_score": 36.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "22",
            "user_name": "王艳",
            "remark": "王岩局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京市密云区-密云区政府-密云区审计局-电子数据审计科"
            ],
            "positions": [
                "暂未填写"
            ],
            "is_friend": False,
            "is_top": True,
            "is_follower": True,
            "session_time": 1748741585,
            "base_score": 42.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "23",
            "user_name": "王岩臣",
            "remark": "王岩局长的秘书",
            "full_dept_name": [
                "北京市-北京市人民政府-市人力资源社会保障局-北京市社会保险基金管理中心-数据管理部",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-领导",
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-中心领导"
            ],
            "positions": [
                "暂未填写",
                "测试负责人"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": False,
            "session_time": 1748914385,
            "base_score": 82.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "24",
            "user_name": "王岩",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区科技和信息化局（区大数据局）-大数据应用科",
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区科技和信息化局（区大数据局）-中小企业促进科"
            ],
            "positions": [
                "九级管理岗"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": False,
            "session_time": 1749259985,
            "base_score": 37.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "25",
            "user_name": "王岩臣",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市辖区-北京市延庆区-延庆区政府工作部门-延庆区经济和信息化局-大数据中心-大数据管理科"
            ],
            "positions": [
                "九级管理岗"
            ],
            "is_friend": False,
            "is_top": True,
            "is_follower": False,
            "session_time": 1749000785,
            "base_score": 22.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "26",
            "user_name": "王艳",
            "remark": "王艳丽局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京经济技术开发区-档案数据中心-领导",
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区科技和信息化局（区大数据局）",
                "北京市-北京市辖区-北京市怀柔区-北京市怀柔区人民政府-怀柔区审计局-区审计局电子数据审计中心"
            ],
            "positions": [
                "暂未填写",
                "九级管理岗"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": False,
            "session_time": 1749000785,
            "base_score": 5.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "27",
            "user_name": "王艳",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市辖区-北京市门头沟区-门头沟区政府-门头沟区审计局-电子数据审计科",
                "北京市-北京市辖区-北京市石景山区-石景山区区政府-石景山区审计局-电子数据审计科",
                "北京市-北京市辖区-北京市延庆区-延庆区政府工作部门-延庆区审计局-数据审计分析中心"
            ],
            "positions": [
                "测试负责人"
            ],
            "is_friend": True,
            "is_top": True,
            "is_follower": False,
            "session_time": 1749000785,
            "base_score": 38.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "28",
            "user_name": "汪研",
            "remark": "王艳丽局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-创新发展科",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-综合产业科",
                "北京市-中共北京市委员会-市委组织部-干部信息管理处（数据中心）"
            ],
            "positions": [
                "测试负责人"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": True,
            "session_time": 1748914385,
            "base_score": 61.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "29",
            "user_name": "王岩臣",
            "remark": "王岩局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-区制造业创新发展促进中心",
                "北京市-北京市辖区-北京市石景山区-石景山区区政府-石景山区经济和信息化局-大数据中心"
            ],
            "positions": [
                "测试负责人"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": False,
            "session_time": 1749346385,
            "base_score": 43.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "30",
            "user_name": "王艳",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区审计局-数据科",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-办公室",
                "北京市-北京市人民政府-市经济和信息化局-内设机构-大数据建设处"
            ],
            "positions": [
                "九级管理岗",
                "测试负责人"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": False,
            "session_time": 1749432785,
            "base_score": 99.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "31",
            "user_name": "王艳",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市辖区-北京市大兴区-政府口单位-大兴区审计局-电子数据审计科",
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-发展规划部",
                "北京市-北京市辖区-北京经济技术开发区-档案数据中心-领导"
            ],
            "positions": [
                "九级管理岗"
            ],
            "is_friend": False,
            "is_top": True,
            "is_follower": True,
            "session_time": 1748655185,
            "base_score": 4.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "32",
            "user_name": "王艳",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市辖区-北京市昌平区-昌平区属企业-回天大脑试点-大数据中心",
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-数据开放部"
            ],
            "positions": [
                "九级管理岗"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": True,
            "session_time": 1749778385,
            "base_score": 65.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "33",
            "user_name": "汪研",
            "remark": "王艳丽局长的秘书",
            "full_dept_name": [
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-发展规划部",
                "北京市-北京市辖区-北京市大兴区-其他单位-疫情防控工作领导小组-社区防控组-数据组",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-区制造业创新发展促进中心",
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区科技和信息化局（区大数据局）-产业发展科"
            ],
            "positions": [
                "测试负责人"
            ],
            "is_friend": False,
            "is_top": True,
            "is_follower": False,
            "session_time": 1749432785,
            "base_score": 20.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "34",
            "user_name": "汪研",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-都市产业科",
                "北京市-北京市辖区-北京经济技术开发区-档案数据中心-档案数据处",
                "北京市-北京市辖区-北京市通州区-通州区政府-通州区经信局-大数据科"
            ],
            "positions": [
                "九级管理岗",
                "暂未填写"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": True,
            "session_time": 1749259985,
            "base_score": 95.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "35",
            "user_name": "王岩臣",
            "remark": "王艳丽局长的秘书",
            "full_dept_name": [
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-大数据支撑部",
                "北京市-北京市辖区-北京市丰台区-丰台区政府-丰台区科技信息化局-大数据管理科"
            ],
            "positions": [
                "九级管理岗",
                "暂未填写"
            ],
            "is_friend": False,
            "is_top": True,
            "is_follower": False,
            "session_time": 1749864785,
            "base_score": 59.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "36",
            "user_name": "王艳",
            "remark": "王艳丽局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京经济技术开发区-档案数据中心",
                "北京市-北京市人民政府-市经济和信息化局-内设机构-大数据标准与安全处",
                "北京市-北京市辖区-北京市石景山区-石景山区区政府-石景山区经济和信息化局-大数据中心"
            ],
            "positions": [
                "暂未填写",
                "九级管理岗"
            ],
            "is_friend": True,
            "is_top": True,
            "is_follower": True,
            "session_time": 1749259985,
            "base_score": 90.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "37",
            "user_name": "王岩",
            "remark": "王艳丽局长的秘书",
            "full_dept_name": [
                "北京市-中共北京市委员会-市委组织部-干部信息管理处（数据中心）",
                "北京市-北京市辖区-北京市朝阳区-朝阳区政府-朝阳区卫生健康系统-直属行政和事业单位-朝阳区卫生信息中心-信息安全与数据服务部",
                "北京市-北京市人民政府-市人力资源社会保障局-大数据中心",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）"
            ],
            "positions": [
                "测试负责人"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": False,
            "session_time": 1749864785,
            "base_score": 12.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "38",
            "user_name": "汪研",
            "remark": "王岩局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京市昌平区-昌平区政府-昌平区经信局-大数据管理科"
            ],
            "positions": [
                "九级管理岗"
            ],
            "is_friend": True,
            "is_top": True,
            "is_follower": True,
            "session_time": 1748914385,
            "base_score": 11.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "39",
            "user_name": "王艳",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-数统部",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-区制造业创新发展促进中心",
                "北京市-北京市辖区-北京市密云区-密云区政府-密云区审计局-电子数据审计科"
            ],
            "positions": [
                "暂未填写"
            ],
            "is_friend": False,
            "is_top": True,
            "is_follower": True,
            "session_time": 1748655185,
            "base_score": 75.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "40",
            "user_name": "王岩",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市辖区-北京经济技术开发区-档案数据中心-史志综合处",
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-运维保障部",
                "北京市-北京市辖区-北京市西城区-西城区政府-西城区审计局-电子数据科",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-综合产业科"
            ],
            "positions": [
                "九级管理岗",
                "测试负责人"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": False,
            "session_time": 1749519185,
            "base_score": 52.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "41",
            "user_name": "王岩",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市辖区-北京市大兴区-政府口单位-大兴区审计局-电子数据审计科",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-领导",
                "北京市-北京市辖区-北京市大兴区-镇、街道-长子营镇-科室站所-长子营镇政府机关数据组",
                "北京市-北京市辖区-北京市朝阳区-朝阳区政府-朝阳区统计局-数据应用科"
            ],
            "positions": [
                "测试负责人",
                "暂未填写"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": False,
            "session_time": 1749864785,
            "base_score": 29.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "42",
            "user_name": "王艳",
            "remark": "王艳丽局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区审计局-数据科",
                "北京市-北京市辖区-北京市大兴区-其他单位-疫情防控工作领导小组-疫情防控办公室-信息数据组"
            ],
            "positions": [
                "暂未填写"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": True,
            "session_time": 1748655185,
            "base_score": 68.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "43",
            "user_name": "汪研",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市辖区-北京市密云区-密云区政府-密云区审计局-电子数据审计科",
                "北京市-北京市人民政府-市人力资源社会保障局-北京市劳动能力鉴定中心-数据管理部",
                "北京市-中共北京市委员会-市委网信办-网络数据与技术处"
            ],
            "positions": [
                "暂未填写",
                "测试负责人"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": True,
            "session_time": 1749691985,
            "base_score": 97.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "44",
            "user_name": "王岩",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-综合部",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-办公室",
                "北京市-北京市人民政府-市发展改革委-市疏整促专项办数据信息处"
            ],
            "positions": [
                "暂未填写",
                "测试负责人"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": True,
            "session_time": 1748914385,
            "base_score": 95.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "45",
            "user_name": "王岩臣",
            "remark": "王艳丽局长的秘书",
            "full_dept_name": [
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-领导",
                "北京市-北京市辖区-北京市密云区-密云区政府-密云区审计局-电子数据审计科",
                "北京市-北京市人民政府-市发展改革委-市疏整促专项办数据信息处"
            ],
            "positions": [
                "测试负责人"
            ],
            "is_friend": False,
            "is_top": True,
            "is_follower": False,
            "session_time": 1749778385,
            "base_score": 83.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "46",
            "user_name": "王岩",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-都市产业科",
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区统计局-数据中心",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-节能与综合利用科"
            ],
            "positions": [
                "测试负责人"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": False,
            "session_time": 1749346385,
            "base_score": 79.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "47",
            "user_name": "王岩臣",
            "remark": "王艳丽局长的秘书",
            "full_dept_name": [
                "北京市-北京市人民政府-市人力资源社会保障局-北京市社会保险基金管理中心-数据管理部",
                "北京市-北京市人民政府-市卫生健康委-市属医院-北京天坛医院-信息管理与数据中心",
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-项目评审部",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-办公室"
            ],
            "positions": [
                "暂未填写",
                "九级管理岗"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": False,
            "session_time": 1748827985,
            "base_score": 82.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "48",
            "user_name": "王岩臣",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心",
                "北京市-北京市人民政府-市经济和信息化局-内设机构-大数据应用与产业处",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-区制造业创新发展促进中心"
            ],
            "positions": [
                "九级管理岗",
                "测试负责人"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": False,
            "session_time": 1749864785,
            "base_score": 60.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "49",
            "user_name": "王岩臣",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市辖区-北京市石景山区-石景山区区政府-石景山区审计局-电子数据审计科",
                "北京市-北京市辖区-北京市海淀区-海淀区区委-海淀区区委组织部-区疫情防控社区防控组-区数据组",
                "北京市-北京市人民政府-市人力资源社会保障局-北京市劳动能力鉴定中心-数据管理部"
            ],
            "positions": [
                "暂未填写"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": False,
            "session_time": 1749087185,
            "base_score": 94.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "50",
            "user_name": "汪研",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-区制造业创新发展促进中心",
                "北京市-北京市辖区-北京市西城区-西城区政府-西城区统计局-数据中心"
            ],
            "positions": [
                "九级管理岗"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": False,
            "session_time": 1749259985,
            "base_score": 99.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "51",
            "user_name": "王岩臣",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市辖区-北京市延庆区-延庆区政府工作部门-延庆区经济和信息化局-大数据中心-信息技术科",
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-数据应用部",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-办公室",
                "北京市-北京市辖区-北京市大兴区-镇、街道-魏善庄镇-科室站所-科室大数据核查组"
            ],
            "positions": [
                "九级管理岗",
                "测试负责人"
            ],
            "is_friend": False,
            "is_top": True,
            "is_follower": True,
            "session_time": 1749519185,
            "base_score": 82.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "52",
            "user_name": "王岩臣",
            "remark": "王艳丽局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京市密云区-密云区政府-密云区审计局-电子数据审计科",
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-标准与安全部",
                "北京市-北京市人民政府-市经济和信息化局-内设机构-大数据建设处",
                "北京市-北京市辖区-北京市大兴区-政府口单位-大兴区审计局-电子数据审计科"
            ],
            "positions": [
                "暂未填写",
                "测试负责人"
            ],
            "is_friend": False,
            "is_top": True,
            "is_follower": True,
            "session_time": 1749000785,
            "base_score": 43.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "53",
            "user_name": "王岩",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市辖区-北京市石景山区-石景山区区政府-石景山区审计局-电子数据审计科",
                "北京市-北京市辖区-北京市通州区-通州区政府-通州区经信局-大数据科",
                "北京市-北京市辖区-北京市丰台区-丰台区政府-丰台区科技信息化局-大数据管理科",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-规划科"
            ],
            "positions": [
                "暂未填写"
            ],
            "is_friend": False,
            "is_top": True,
            "is_follower": False,
            "session_time": 1748827985,
            "base_score": 15.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "54",
            "user_name": "王艳",
            "remark": "王岩局长的秘书",
            "full_dept_name": [
                "北京市-北京市人民政府-市经济和信息化局-内设机构-大数据标准与安全处",
                "北京市-北京市辖区-北京市朝阳区-朝阳区政府-朝阳区城管指挥中心-数据分析科",
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-中心领导",
                "北京市-北京市人民政府-市投资促进服务中心-区域促进处（信息数据处）",
                "北京市-北京市辖区-北京市大兴区-其他单位-疫情防控工作领导小组-社区防控组-数据组"
            ],
            "positions": [
                "九级管理岗"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": False,
            "session_time": 1749864785,
            "base_score": 39.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "55",
            "user_name": "王艳",
            "remark": "王岩局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京市大兴区-镇、街道-长子营镇-科室站所-长子营镇政府机关数据组",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-办公室"
            ],
            "positions": [
                "九级管理岗"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": True,
            "session_time": 1749864785,
            "base_score": 24.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "56",
            "user_name": "王岩臣",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市辖区-北京市朝阳区-朝阳区政府-朝阳区卫生健康系统-直属行政和事业单位-朝阳区卫生信息中心-信息安全与数据服务部",
                "北京市-北京市人民政府-市卫生健康委-市属医院-北京天坛医院-信息管理与数据中心",
                "北京市-北京市辖区-北京市朝阳区-朝阳区政府-朝阳区审计局-数据科"
            ],
            "positions": [
                "测试负责人",
                "九级管理岗"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": True,
            "session_time": 1749432785,
            "base_score": 17.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "57",
            "user_name": "汪研",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市辖区-北京市怀柔区-北京市怀柔区人民政府-怀柔区审计局-区审计局电子数据审计中心",
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-中心领导"
            ],
            "positions": [
                "测试负责人",
                "暂未填写"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": False,
            "session_time": 1749691985,
            "base_score": 14.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "58",
            "user_name": "汪研",
            "remark": "王艳丽局长的秘书",
            "full_dept_name": [
                "北京市-北京市人民政府-市人力资源社会保障局-北京市劳动能力鉴定中心-数据管理部",
                "北京市-北京市辖区-北京市延庆区-延庆区政府工作部门-延庆区经济和信息化局-大数据中心-网络管理科",
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区科技和信息化局（区大数据局）-产业发展科",
                "北京市-中共北京市委员会-市委网信办-网络数据与技术处",
                "北京市-北京市辖区-北京市延庆区-延庆区政府工作部门-延庆区经济和信息化局-大数据中心-大数据管理科"
            ],
            "positions": [
                "九级管理岗"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": True,
            "session_time": 1748827985,
            "base_score": 69.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "59",
            "user_name": "汪研",
            "remark": "王岩局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京市延庆区-延庆区政府工作部门-延庆区经济和信息化局-大数据中心-信息技术科",
                "北京市-北京市辖区-北京市门头沟区-门头沟区政府-门头沟区审计局-电子数据审计科",
                "北京市-中共北京市委员会-市委网信办-网络数据与技术处",
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-发展规划部",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-数统部"
            ],
            "positions": [
                "暂未填写",
                "测试负责人"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": False,
            "session_time": 1749691985,
            "base_score": 24.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "60",
            "user_name": "王艳",
            "remark": "王岩局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-都市产业科",
                "北京市-北京市人民政府-市水务局-局属单位-北京市智慧水务发展研究院-软件与数据研究所",
                "北京市-北京市辖区-北京市丰台区-丰台区政府-丰台区审计局-电子数据审计科",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-财务室"
            ],
            "positions": [
                "九级管理岗",
                "暂未填写"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": False,
            "session_time": 1749173585,
            "base_score": 21.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "61",
            "user_name": "王岩",
            "remark": "王艳丽局长的秘书",
            "full_dept_name": [
                "北京市-北京市人民政府-市人力资源社会保障局-北京市劳动能力鉴定中心-数据管理部"
            ],
            "positions": [
                "测试负责人",
                "暂未填写"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": True,
            "session_time": 1749259985,
            "base_score": 35.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "62",
            "user_name": "汪研",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市辖区-北京市大兴区-其他单位-疫情防控工作领导小组-社区防控组-数据组",
                "北京市-北京市辖区-北京市延庆区-延庆区政府工作部门-延庆区城市管理指挥中心-数据管理科",
                "北京市-北京市人民政府-市卫生健康委-市属医院-北京天坛医院-信息管理与数据中心"
            ],
            "positions": [
                "暂未填写",
                "九级管理岗"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": True,
            "session_time": 1749173585,
            "base_score": 10.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "63",
            "user_name": "王岩",
            "remark": "王艳丽局长的秘书",
            "full_dept_name": [
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-中心领导",
                "北京市-北京市辖区-北京市朝阳区-朝阳区政府-朝阳区统计局-数据应用科",
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-运维保障部",
                "北京市-北京市辖区-北京市延庆区-延庆区政府工作部门-延庆区经济和信息化局-大数据中心-信息技术科",
                "北京市-北京市辖区-北京市延庆区-延庆区政府工作部门-延庆区经济和信息化局-大数据中心-网络管理科"
            ],
            "positions": [
                "测试负责人",
                "九级管理岗"
            ],
            "is_friend": False,
            "is_top": True,
            "is_follower": False,
            "session_time": 1749087185,
            "base_score": 13.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "64",
            "user_name": "王岩臣",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）"
            ],
            "positions": [
                "暂未填写",
                "测试负责人"
            ],
            "is_friend": True,
            "is_top": True,
            "is_follower": False,
            "session_time": 1749691985,
            "base_score": 10.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "65",
            "user_name": "王岩臣",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-软件和信息产业科",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-创新发展科",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-编辑室"
            ],
            "positions": [
                "暂未填写"
            ],
            "is_friend": False,
            "is_top": True,
            "is_follower": True,
            "session_time": 1749259985,
            "base_score": 5.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "66",
            "user_name": "王艳",
            "remark": "王艳丽局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京市延庆区-延庆区政府工作部门-延庆区经济和信息化局-大数据中心",
                "北京市-中共北京市委员会-市委网信办-网络数据与技术处",
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区科技和信息化局（区大数据局）-科学技术发展科",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-节能与综合利用科"
            ],
            "positions": [
                "九级管理岗",
                "测试负责人"
            ],
            "is_friend": False,
            "is_top": True,
            "is_follower": False,
            "session_time": 1748741585,
            "base_score": 65.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "67",
            "user_name": "王艳",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市人民政府-市审计局-电子数据处"
            ],
            "positions": [
                "测试负责人"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": False,
            "session_time": 1749259985,
            "base_score": 38.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "68",
            "user_name": "王岩",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-中心领导",
                "北京市-北京市辖区-北京经济技术开发区-档案数据中心-档案数据处"
            ],
            "positions": [
                "九级管理岗",
                "测试负责人"
            ],
            "is_friend": True,
            "is_top": True,
            "is_follower": False,
            "session_time": 1748914385,
            "base_score": 83.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "69",
            "user_name": "王岩",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-标评部",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-领导",
                "北京市-北京市人民政府-市经济和信息化局-内设机构-大数据建设处"
            ],
            "positions": [
                "暂未填写"
            ],
            "is_friend": False,
            "is_top": True,
            "is_follower": False,
            "session_time": 1749432785,
            "base_score": 68.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "70",
            "user_name": "王岩",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市辖区-北京市怀柔区-北京市怀柔区人民政府-怀柔区审计局-区审计局电子数据审计中心",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-标评部",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-政研组",
                "北京市-北京市辖区-北京市海淀区-海淀区区委-海淀区区委组织部-区疫情防控社区防控组-区数据组",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-规划科"
            ],
            "positions": [
                "测试负责人",
                "九级管理岗"
            ],
            "is_friend": False,
            "is_top": True,
            "is_follower": True,
            "session_time": 1749778385,
            "base_score": 50.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "71",
            "user_name": "王岩臣",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市人民政府-市人力资源社会保障局-大数据中心",
                "北京市-北京市辖区-北京市延庆区-延庆区政府工作部门-延庆区经济和信息化局-大数据中心-信息技术科",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-工业发展科",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-财务室",
                "北京市-北京市辖区-北京市石景山区-石景山区区政府-石景山区审计局-电子数据审计科"
            ],
            "positions": [
                "测试负责人"
            ],
            "is_friend": True,
            "is_top": True,
            "is_follower": False,
            "session_time": 1748914385,
            "base_score": 43.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "72",
            "user_name": "汪研",
            "remark": "王艳丽局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-工业发展科",
                "北京市-北京市辖区-北京经济技术开发区-档案数据中心-档案数据处",
                "北京市-北京市人民政府-市水务局-局属单位-北京市智慧水务发展研究院-数据管理中心"
            ],
            "positions": [
                "测试负责人"
            ],
            "is_friend": True,
            "is_top": True,
            "is_follower": False,
            "session_time": 1749346385,
            "base_score": 61.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "73",
            "user_name": "王岩臣",
            "remark": "王岩局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京市海淀区-海淀区区委-海淀区区委组织部-区疫情防控社区防控组-区数据组"
            ],
            "positions": [
                "九级管理岗"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": False,
            "session_time": 1749000785,
            "base_score": 51.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "74",
            "user_name": "汪研",
            "remark": "王艳丽局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京市延庆区-延庆区政府工作部门-延庆区经济和信息化局-大数据中心-网络管理科"
            ],
            "positions": [
                "测试负责人",
                "九级管理岗"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": False,
            "session_time": 1748914385,
            "base_score": 72.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "75",
            "user_name": "王艳",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市辖区-北京市朝阳区-朝阳区政府-朝阳区统计局-数据应用科",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心"
            ],
            "positions": [
                "测试负责人",
                "九级管理岗"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": True,
            "session_time": 1749000785,
            "base_score": 88.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "76",
            "user_name": "王岩",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）",
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区科技和信息化局（区大数据局）-科学技术发展科",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-标评部",
                "北京市-北京市辖区-北京市丰台区-丰台区政府-丰台区科技信息化局-大数据管理科"
            ],
            "positions": [
                "测试负责人",
                "暂未填写"
            ],
            "is_friend": True,
            "is_top": True,
            "is_follower": True,
            "session_time": 1749864785,
            "base_score": 99.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "77",
            "user_name": "王艳",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市人民政府-市经济和信息化局-内设机构-大数据应用与产业处",
                "北京市-北京市辖区-北京市怀柔区-北京市怀柔区人民政府-怀柔区审计局-区审计局电子数据审计中心",
                "北京市-北京市人民政府-市人力资源社会保障局-大数据中心"
            ],
            "positions": [
                "九级管理岗",
                "测试负责人"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": True,
            "session_time": 1748827985,
            "base_score": 6.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "78",
            "user_name": "王岩",
            "remark": "王艳丽局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）",
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区科技和信息化局（区大数据局）",
                "北京市-北京市辖区-北京市丰台区-丰台区政府-丰台区科技信息化局-大数据管理科",
                "北京市-北京市辖区-北京市延庆区-延庆区政府工作部门-延庆区审计局-数据审计分析中心"
            ],
            "positions": [
                "九级管理岗",
                "暂未填写"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": True,
            "session_time": 1749346385,
            "base_score": 19.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "79",
            "user_name": "汪研",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市辖区-北京市西城区-西城区政府-西城区审计局-电子数据科",
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-平台管理部",
                "北京市-中共北京市委员会-市委网信办-网络数据与技术处"
            ],
            "positions": [
                "九级管理岗"
            ],
            "is_friend": True,
            "is_top": True,
            "is_follower": True,
            "session_time": 1749432785,
            "base_score": 18.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "80",
            "user_name": "王岩臣",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-研究部"
            ],
            "positions": [
                "测试负责人",
                "九级管理岗"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": False,
            "session_time": 1749432785,
            "base_score": 99.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "81",
            "user_name": "王岩",
            "remark": "王艳丽局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区科技和信息化局（区大数据局）-信息化促进科",
                "北京市-北京市辖区-北京市延庆区-延庆区政府工作部门-延庆区审计局-数据审计分析中心"
            ],
            "positions": [
                "测试负责人"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": True,
            "session_time": 1749519185,
            "base_score": 34.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "82",
            "user_name": "王岩",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-综合部",
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区统计局-数据中心",
                "北京市-北京市人民政府-市经济和信息化局-内设机构-大数据应用与产业处"
            ],
            "positions": [
                "九级管理岗"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": True,
            "session_time": 1749864785,
            "base_score": 52.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "83",
            "user_name": "汪研",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心"
            ],
            "positions": [
                "测试负责人"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": False,
            "session_time": 1749691985,
            "base_score": 25.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "84",
            "user_name": "汪研",
            "remark": "王艳丽局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区科技和信息化局（区大数据局）",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-研究部",
                "北京市-北京市人民政府-市水务局-局属单位-北京市智慧水务发展研究院-软件与数据研究所"
            ],
            "positions": [
                "测试负责人"
            ],
            "is_friend": False,
            "is_top": True,
            "is_follower": False,
            "session_time": 1748741585,
            "base_score": 16.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "85",
            "user_name": "王岩臣",
            "remark": "王岩局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-工业发展科",
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区科技和信息化局（区大数据局）-办公室",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心",
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区科技和信息化局（区大数据局）-中小企业促进科"
            ],
            "positions": [
                "暂未填写"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": False,
            "session_time": 1748655185,
            "base_score": 69.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "86",
            "user_name": "王岩臣",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市辖区-北京市西城区-西城区政府-西城区审计局-电子数据科",
                "北京市-中共北京市委员会-市委网信办-网络数据与技术处",
                "北京市-北京市辖区-北京市延庆区-延庆区政府工作部门-延庆区经济和信息化局-大数据中心",
                "北京市-北京市人民政府-市投资促进服务中心-区域促进处（信息数据处）"
            ],
            "positions": [
                "九级管理岗"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": False,
            "session_time": 1749173585,
            "base_score": 88.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "87",
            "user_name": "王岩臣",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-项目评审部",
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区科技和信息化局（区大数据局）-科学技术发展科",
                "北京市-北京市人民政府-市人力资源社会保障局-北京市社会保险基金管理中心-数据管理部"
            ],
            "positions": [
                "九级管理岗"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": True,
            "session_time": 1748914385,
            "base_score": 77.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "88",
            "user_name": "王岩臣",
            "remark": "王岩局长的秘书",
            "full_dept_name": [
                "北京市-北京市人民政府-市人力资源社会保障局-北京市劳动能力鉴定中心-数据管理部",
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-数据开放部",
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区科技和信息化局（区大数据局）-产业发展科"
            ],
            "positions": [
                "测试负责人",
                "九级管理岗"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": False,
            "session_time": 1749259985,
            "base_score": 29.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "89",
            "user_name": "王岩臣",
            "remark": "王艳丽局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京市石景山区-石景山区区政府-石景山区审计局-电子数据审计科",
                "北京市-北京市辖区-北京市海淀区-海淀区区委-海淀区区委组织部-区疫情防控社区防控组-区数据组"
            ],
            "positions": [
                "暂未填写"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": False,
            "session_time": 1749864785,
            "base_score": 36.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "90",
            "user_name": "汪研",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-研究部"
            ],
            "positions": [
                "九级管理岗",
                "暂未填写"
            ],
            "is_friend": True,
            "is_top": True,
            "is_follower": False,
            "session_time": 1748741585,
            "base_score": 39.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "91",
            "user_name": "王岩",
            "remark": "王岩局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京市石景山区-石景山区区政府-石景山区统计局-数据应用科",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-创新发展科"
            ],
            "positions": [
                "九级管理岗",
                "测试负责人"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": True,
            "session_time": 1749000785,
            "base_score": 11.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "92",
            "user_name": "王艳",
            "remark": "测试",
            "full_dept_name": [
                "北京市-中共北京市委员会-市委组织部-干部信息管理处（数据中心）",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）",
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-平台管理部",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-都市产业科",
                "北京市-北京市人民政府-市水务局-局属单位-北京市智慧水务发展研究院-数据管理中心"
            ],
            "positions": [
                "九级管理岗",
                "测试负责人"
            ],
            "is_friend": True,
            "is_top": True,
            "is_follower": True,
            "session_time": 1749519185,
            "base_score": 19.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "93",
            "user_name": "王岩",
            "remark": "王岩局长的秘书",
            "full_dept_name": [
                "北京市-中共北京市委员会-市委组织部-干部信息管理处（数据中心）",
                "北京市-北京市辖区-北京市海淀区-海淀区政府-海淀区城管指挥中心-大数据科",
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-发展规划部",
                "北京市-北京市辖区-北京市门头沟区-门头沟区政府-门头沟区审计局-电子数据审计科"
            ],
            "positions": [
                "暂未填写",
                "测试负责人"
            ],
            "is_friend": True,
            "is_top": True,
            "is_follower": True,
            "session_time": 1748914385,
            "base_score": 83.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "94",
            "user_name": "王岩",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-大数据建设管理科"
            ],
            "positions": [
                "九级管理岗"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": True,
            "session_time": 1748914385,
            "base_score": 65.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "95",
            "user_name": "汪研",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-办公室",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）",
                "北京市-中共北京市委员会-市委组织部-干部信息管理处（数据中心）",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-工业发展科",
                "北京市-北京市辖区-北京市海淀区-海淀区区委-海淀区区委组织部-区疫情防控社区防控组-区数据组"
            ],
            "positions": [
                "测试负责人"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": False,
            "session_time": 1749864785,
            "base_score": 65.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "96",
            "user_name": "王岩臣",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-都市产业科",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）"
            ],
            "positions": [
                "九级管理岗",
                "暂未填写"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": False,
            "session_time": 1748655185,
            "base_score": 3.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "97",
            "user_name": "王岩臣",
            "remark": "王岩局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京市延庆区-延庆区政府工作部门-延庆区经济和信息化局-大数据中心-信息技术科"
            ],
            "positions": [
                "暂未填写"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": False,
            "session_time": 1748914385,
            "base_score": 93.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "98",
            "user_name": "王岩",
            "remark": "王岩局长的秘书",
            "full_dept_name": [
                "北京市-北京市人民政府-市人力资源社会保障局-北京市社会保险基金管理中心-数据管理部",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-大数据建设管理科",
                "北京市-北京市辖区-北京市延庆区-延庆区政府工作部门-延庆区经济和信息化局-大数据中心-信息技术科"
            ],
            "positions": [
                "暂未填写",
                "九级管理岗"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": True,
            "session_time": 1749000785,
            "base_score": 70.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "99",
            "user_name": "王岩臣",
            "remark": "王岩局长的秘书",
            "full_dept_name": [
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-数据应用部",
                "北京市-北京市人民政府-市发展改革委-市疏整促专项办数据信息处",
                "北京市-北京市辖区-北京市朝阳区-朝阳区政府-朝阳区统计局-数据应用科",
                "北京市-北京市辖区-北京市海淀区-海淀区区委-海淀区区委组织部-区疫情防控社区防控组-区数据组"
            ],
            "positions": [
                "测试负责人",
                "九级管理岗"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": True,
            "session_time": 1748827985,
            "base_score": 69.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "100",
            "user_name": "汪研",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-综合产业科",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-大数据建设管理科"
            ],
            "positions": [
                "九级管理岗"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": True,
            "session_time": 1749864785,
            "base_score": 84.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "101",
            "user_name": "王艳",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区科技和信息化局（区大数据局）-科学技术发展科"
            ],
            "positions": [
                "暂未填写",
                "测试负责人"
            ],
            "is_friend": True,
            "is_top": True,
            "is_follower": True,
            "session_time": 1749000785,
            "base_score": 54.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "102",
            "user_name": "王岩臣",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市辖区-北京市大兴区-其他单位-疫情防控工作领导小组-社区防控组-数据组",
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区科技和信息化局（区大数据局）-大数据应用科",
                "北京市-北京市人民政府-市审计局-电子数据处"
            ],
            "positions": [
                "暂未填写",
                "九级管理岗"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": False,
            "session_time": 1749346385,
            "base_score": 47.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "103",
            "user_name": "王艳",
            "remark": "王岩局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区科技和信息化局（区大数据局）-大数据应用科",
                "北京市-北京市人民政府-市人力资源社会保障局-大数据中心",
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区科技和信息化局（区大数据局）-科学技术发展科",
                "北京市-北京市辖区-北京市门头沟区-门头沟区政府-门头沟区审计局-电子数据审计科"
            ],
            "positions": [
                "暂未填写"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": False,
            "session_time": 1749346385,
            "base_score": 19.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "104",
            "user_name": "汪研",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市人民政府-市经济和信息化局-内设机构-大数据建设处",
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心",
                "北京市-北京市辖区-北京市延庆区-延庆区政府工作部门-延庆区经济和信息化局-大数据中心-大数据管理科",
                "北京市-北京市人民政府-市人力资源社会保障局-大数据中心",
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-中心领导"
            ],
            "positions": [
                "暂未填写"
            ],
            "is_friend": False,
            "is_top": True,
            "is_follower": True,
            "session_time": 1749778385,
            "base_score": 30.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "105",
            "user_name": "王艳",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市辖区-北京市怀柔区-北京市怀柔区人民政府-怀柔区审计局-区审计局电子数据审计中心",
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-平台管理部",
                "北京市-北京市辖区-北京经济技术开发区-档案数据中心-领导",
                "北京市-北京市辖区-北京市昌平区-昌平区政府-昌平区经信局-大数据管理科",
                "北京市-北京市辖区-北京市海淀区-海淀区区委-海淀区区委组织部-区疫情防控社区防控组-区数据组"
            ],
            "positions": [
                "测试负责人"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": False,
            "session_time": 1749519185,
            "base_score": 91.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "106",
            "user_name": "王岩臣",
            "remark": "王岩局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京经济技术开发区-档案数据中心-领导",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-领导",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-数统部",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-综合产业科"
            ],
            "positions": [
                "测试负责人"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": False,
            "session_time": 1749087185,
            "base_score": 40.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "107",
            "user_name": "王艳",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-创新发展科",
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-发展规划部",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-大数据建设与应用创新部",
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-运维保障部"
            ],
            "positions": [
                "九级管理岗",
                "暂未填写"
            ],
            "is_friend": True,
            "is_top": True,
            "is_follower": False,
            "session_time": 1749605585,
            "base_score": 30.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "108",
            "user_name": "王艳",
            "remark": "王艳丽局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京经济技术开发区-档案数据中心"
            ],
            "positions": [
                "测试负责人"
            ],
            "is_friend": False,
            "is_top": True,
            "is_follower": True,
            "session_time": 1749605585,
            "base_score": 51.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "109",
            "user_name": "汪研",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区科技和信息化局（区大数据局）"
            ],
            "positions": [
                "测试负责人"
            ],
            "is_friend": False,
            "is_top": True,
            "is_follower": False,
            "session_time": 1749605585,
            "base_score": 24.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "110",
            "user_name": "王岩",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市辖区-北京市延庆区-延庆区政府工作部门-延庆区经济和信息化局-大数据中心-信息技术科",
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-综合部",
                "北京市-北京市人民政府-市民政局-委局直属单位-北京市困难群众救助服务指导中心（北京市居民经济状况核对中心）-数据管理科",
                "北京市-北京市辖区-北京经济技术开发区-行政审批局-大数据处",
                "北京市-北京市人民政府-市人力资源社会保障局-北京市劳动能力鉴定中心-数据管理部"
            ],
            "positions": [
                "测试负责人"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": False,
            "session_time": 1749087185,
            "base_score": 63.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "111",
            "user_name": "王岩臣",
            "remark": "王艳丽局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京市密云区-密云区政府-密云区审计局-电子数据审计科",
                "北京市-北京市辖区-北京市石景山区-石景山区区政府-石景山区审计局-电子数据审计科",
                "北京市-北京市辖区-北京市大兴区-镇、街道-魏善庄镇-科室站所-科室大数据核查组",
                "北京市-北京市人民政府-市水务局-局属单位-北京市智慧水务发展研究院-数据管理中心",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-工业发展科"
            ],
            "positions": [
                "测试负责人",
                "暂未填写"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": True,
            "session_time": 1748914385,
            "base_score": 26.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "112",
            "user_name": "汪研",
            "remark": "王艳丽局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京市西城区-西城区政府-西城区审计局-电子数据科",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-编辑室"
            ],
            "positions": [
                "暂未填写"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": False,
            "session_time": 1749691985,
            "base_score": 81.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "113",
            "user_name": "王岩",
            "remark": "王艳丽局长的秘书",
            "full_dept_name": [
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-评审部",
                "北京市-北京市辖区-北京经济技术开发区-档案数据中心-领导",
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-平台管理部",
                "北京市-北京市辖区-北京市石景山区-石景山区区政府-石景山区审计局-电子数据审计科",
                "北京市-北京市人民政府-市发展改革委-市疏整促专项办数据信息处"
            ],
            "positions": [
                "九级管理岗",
                "暂未填写"
            ],
            "is_friend": False,
            "is_top": True,
            "is_follower": False,
            "session_time": 1748914385,
            "base_score": 20.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "114",
            "user_name": "王艳",
            "remark": "王岩局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京市西城区-西城区政府-西城区统计局-数据中心",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-数统部"
            ],
            "positions": [
                "暂未填写",
                "九级管理岗"
            ],
            "is_friend": True,
            "is_top": True,
            "is_follower": True,
            "session_time": 1749259985,
            "base_score": 21.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "115",
            "user_name": "汪研",
            "remark": "王岩局长的秘书",
            "full_dept_name": [
                "北京市-北京市人民政府-市经济和信息化局-内设机构-大数据应用与产业处",
                "北京市-北京市辖区-北京市丰台区-丰台区政府-丰台区科技信息化局-大数据管理科",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-评审部",
                "北京市-北京市辖区-北京经济技术开发区-档案数据中心"
            ],
            "positions": [
                "暂未填写"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": True,
            "session_time": 1749691985,
            "base_score": 4.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "116",
            "user_name": "王岩臣",
            "remark": "王岩局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京市大兴区-其他单位-疫情防控工作领导小组-社区防控组-数据组",
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-发展规划部",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-办公室",
                "北京市-北京市辖区-北京市石景山区-石景山区区政府-石景山区经济和信息化局-大数据中心"
            ],
            "positions": [
                "九级管理岗"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": True,
            "session_time": 1748741585,
            "base_score": 48.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "117",
            "user_name": "王岩臣",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市人民政府-市民政局-委局直属单位-北京市困难群众救助服务指导中心（北京市居民经济状况核对中心）-数据管理科",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-办公室"
            ],
            "positions": [
                "九级管理岗",
                "暂未填写"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": False,
            "session_time": 1749346385,
            "base_score": 99.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "118",
            "user_name": "王岩",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市人民政府-市投资促进服务中心-区域促进处（信息数据处）"
            ],
            "positions": [
                "测试负责人",
                "九级管理岗"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": True,
            "session_time": 1748914385,
            "base_score": 68.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "119",
            "user_name": "王岩臣",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市辖区-北京市延庆区-延庆区政府工作部门-延庆区审计局-数据审计分析中心",
                "北京市-北京市辖区-北京市石景山区-石景山区区政府-石景山区统计局-数据应用科",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-镇村企业科"
            ],
            "positions": [
                "暂未填写"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": False,
            "session_time": 1749691985,
            "base_score": 26.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "120",
            "user_name": "王岩",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市辖区-北京市石景山区-石景山区区政府-石景山区审计局-电子数据审计科",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-研究部"
            ],
            "positions": [
                "暂未填写",
                "测试负责人"
            ],
            "is_friend": True,
            "is_top": True,
            "is_follower": True,
            "session_time": 1748741585,
            "base_score": 10.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "121",
            "user_name": "汪研",
            "remark": "无",
            "full_dept_name": [
                "北京市-中共北京市委员会-市委组织部-干部信息管理处（数据中心）",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-大数据建设与应用创新部",
                "北京市-北京市辖区-北京市丰台区-丰台区政府-丰台区审计局-电子数据审计科"
            ],
            "positions": [
                "九级管理岗"
            ],
            "is_friend": False,
            "is_top": True,
            "is_follower": False,
            "session_time": 1749173585,
            "base_score": 45.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "122",
            "user_name": "王岩臣",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-标评部",
                "北京市-临时-北京市运行保障指挥部-技术服务保障组-市公安局-办公室-办公室数据中心（科信办）",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-财务室",
                "北京市-北京市辖区-北京市延庆区-延庆区政府工作部门-延庆区审计局-数据审计分析中心",
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-数据管理部"
            ],
            "positions": [
                "暂未填写",
                "测试负责人"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": True,
            "session_time": 1749346385,
            "base_score": 64.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "123",
            "user_name": "王艳",
            "remark": "王艳丽局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京市大兴区-政府口单位-大兴区审计局-电子数据审计科",
                "北京市-北京市人民政府-市经济和信息化局-内设机构-大数据标准与安全处",
                "北京市-北京市人民政府-市审计局-电子数据处"
            ],
            "positions": [
                "暂未填写"
            ],
            "is_friend": True,
            "is_top": True,
            "is_follower": False,
            "session_time": 1749864785,
            "base_score": 64.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "124",
            "user_name": "汪研",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市辖区-北京市通州区-通州区政府-通州区经信局-大数据科",
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-项目评审部"
            ],
            "positions": [
                "九级管理岗"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": True,
            "session_time": 1749605585,
            "base_score": 18.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "125",
            "user_name": "汪研",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区统计局-数据中心"
            ],
            "positions": [
                "九级管理岗",
                "测试负责人"
            ],
            "is_friend": False,
            "is_top": True,
            "is_follower": True,
            "session_time": 1748827985,
            "base_score": 44.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "126",
            "user_name": "王岩",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市人民政府-市民政局-委局直属单位-北京市困难群众救助服务指导中心（北京市居民经济状况核对中心）-数据管理科",
                "北京市-北京市辖区-北京市门头沟区-门头沟区政府-门头沟区审计局-电子数据审计科",
                "北京市-北京市辖区-北京市密云区-密云区政府-密云区审计局-电子数据审计科",
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-信用信息部"
            ],
            "positions": [
                "测试负责人"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": False,
            "session_time": 1748741585,
            "base_score": 65.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "127",
            "user_name": "王岩臣",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-大数据建设管理科"
            ],
            "positions": [
                "暂未填写",
                "九级管理岗"
            ],
            "is_friend": False,
            "is_top": True,
            "is_follower": True,
            "session_time": 1748655185,
            "base_score": 19.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "128",
            "user_name": "王岩",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心",
                "北京市-北京市人民政府-市发展改革委-市疏整促专项办数据信息处"
            ],
            "positions": [
                "测试负责人"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": False,
            "session_time": 1749087185,
            "base_score": 32.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "129",
            "user_name": "汪研",
            "remark": "王岩局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京经济技术开发区-档案数据中心-领导",
                "北京市-北京市辖区-北京市延庆区-延庆区政府工作部门-延庆区经济和信息化局-大数据中心-信息技术科",
                "北京市-北京市辖区-北京市延庆区-延庆区政府工作部门-延庆区审计局-数据审计分析中心",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-节能与综合利用科"
            ],
            "positions": [
                "测试负责人"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": True,
            "session_time": 1748914385,
            "base_score": 39.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "130",
            "user_name": "汪研",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-综合部",
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区科技和信息化局（区大数据局）-大数据应用科"
            ],
            "positions": [
                "测试负责人"
            ],
            "is_friend": True,
            "is_top": True,
            "is_follower": True,
            "session_time": 1749432785,
            "base_score": 70.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "131",
            "user_name": "王艳",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-编辑室",
                "北京市-北京市辖区-北京市大兴区-其他单位-疫情防控工作领导小组-疫情防控办公室-信息数据组",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-经济运行科",
                "北京市-北京市辖区-北京市大兴区-镇、街道-长子营镇-科室站所-长子营镇政府机关数据组"
            ],
            "positions": [
                "九级管理岗",
                "测试负责人"
            ],
            "is_friend": True,
            "is_top": True,
            "is_follower": True,
            "session_time": 1748827985,
            "base_score": 35.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "132",
            "user_name": "王岩臣",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市人民政府-市人力资源社会保障局-北京市社会保险基金管理中心-数据管理部",
                "北京市-北京市人民政府-市民政局-委局直属单位-北京市困难群众救助服务指导中心（北京市居民经济状况核对中心）-数据管理科",
                "北京市-北京市辖区-北京市通州区-通州区政府-通州区经信局-大数据科",
                "北京市-北京市辖区-北京市西城区-西城区政府-西城区科技和信息化局-数据资源管理科"
            ],
            "positions": [
                "测试负责人"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": True,
            "session_time": 1749864785,
            "base_score": 64.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "133",
            "user_name": "王艳",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市人民政府-市审计局-电子数据处",
                "北京市-北京市辖区-北京市大兴区-政府口单位-大兴区审计局-电子数据审计科"
            ],
            "positions": [
                "暂未填写",
                "九级管理岗"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": True,
            "session_time": 1748741585,
            "base_score": 46.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "134",
            "user_name": "王艳",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-经济运行科"
            ],
            "positions": [
                "测试负责人",
                "九级管理岗"
            ],
            "is_friend": False,
            "is_top": True,
            "is_follower": False,
            "session_time": 1748827985,
            "base_score": 11.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "135",
            "user_name": "汪研",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区科技和信息化局（区大数据局）-办公室",
                "北京市-中共北京市委员会-市委组织部-干部信息管理处（数据中心）",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-节能与综合利用科",
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区统计局-数据中心"
            ],
            "positions": [
                "暂未填写"
            ],
            "is_friend": False,
            "is_top": True,
            "is_follower": True,
            "session_time": 1749778385,
            "base_score": 63.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "136",
            "user_name": "王岩",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市辖区-北京市大兴区-其他单位-疫情防控工作领导小组-社区防控组-数据组",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-大数据建设与应用创新部",
                "北京市-北京市人民政府-市投资促进服务中心-区域促进处（信息数据处）",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-工业发展科",
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区科技和信息化局（区大数据局）"
            ],
            "positions": [
                "九级管理岗"
            ],
            "is_friend": False,
            "is_top": True,
            "is_follower": True,
            "session_time": 1749087185,
            "base_score": 82.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "137",
            "user_name": "汪研",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市辖区-北京市海淀区-海淀区区委-海淀区区委组织部-区疫情防控社区防控组-区数据组"
            ],
            "positions": [
                "测试负责人",
                "暂未填写"
            ],
            "is_friend": False,
            "is_top": True,
            "is_follower": False,
            "session_time": 1749432785,
            "base_score": 55.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "138",
            "user_name": "汪研",
            "remark": "王岩局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京市石景山区-石景山区区政府-石景山区统计局-数据应用科",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-经济运行科"
            ],
            "positions": [
                "九级管理岗"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": True,
            "session_time": 1748655185,
            "base_score": 58.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "139",
            "user_name": "王岩",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-数据开放部",
                "北京市-北京市辖区-北京市丰台区-丰台区政府-丰台区科技信息化局-大数据管理科",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-标评部"
            ],
            "positions": [
                "测试负责人",
                "暂未填写"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": True,
            "session_time": 1749778385,
            "base_score": 63.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "140",
            "user_name": "王艳",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-编辑室",
                "北京市-北京市辖区-北京市朝阳区-朝阳区政府-朝阳区统计局-数据应用科",
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-平台管理部",
                "北京市-北京市辖区-北京市延庆区-延庆区政府工作部门-延庆区经济和信息化局-大数据中心-网络管理科",
                "北京市-北京市辖区-北京经济技术开发区-行政审批局-大数据处"
            ],
            "positions": [
                "测试负责人",
                "九级管理岗"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": True,
            "session_time": 1749778385,
            "base_score": 77.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "141",
            "user_name": "王岩",
            "remark": "王艳丽局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京市丰台区-丰台区政府-丰台区审计局-电子数据审计科",
                "北京市-北京市人民政府-市经济和信息化局-内设机构-大数据应用与产业处",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-规划科",
                "北京市-北京市人民政府-市卫生健康委-市属医院-北京天坛医院-信息管理与数据中心",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-政研组"
            ],
            "positions": [
                "测试负责人",
                "九级管理岗"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": False,
            "session_time": 1749346385,
            "base_score": 25.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "142",
            "user_name": "王岩",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市辖区-北京市海淀区-海淀区政府-海淀区城管指挥中心-大数据科",
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-发展规划部",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-工业发展科",
                "北京市-北京市人民政府-市审计局-电子数据处"
            ],
            "positions": [
                "暂未填写",
                "测试负责人"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": True,
            "session_time": 1749346385,
            "base_score": 55.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "143",
            "user_name": "王岩",
            "remark": "王艳丽局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京市延庆区-延庆区政府工作部门-延庆区城市管理指挥中心-数据管理科",
                "北京市-北京市辖区-北京市海淀区-海淀区区委-海淀区区委组织部-区疫情防控社区防控组-区数据组"
            ],
            "positions": [
                "九级管理岗"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": True,
            "session_time": 1748827985,
            "base_score": 98.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "144",
            "user_name": "王岩",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市人民政府-市经济和信息化局-内设机构-大数据标准与安全处"
            ],
            "positions": [
                "暂未填写"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": True,
            "session_time": 1749519185,
            "base_score": 18.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "145",
            "user_name": "王艳",
            "remark": "王艳丽局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京市朝阳区-朝阳区政府-朝阳区统计局-数据应用科",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-财务室",
                "北京市-北京市辖区-北京市石景山区-石景山区区政府-石景山区审计局-电子数据审计科"
            ],
            "positions": [
                "测试负责人",
                "九级管理岗"
            ],
            "is_friend": False,
            "is_top": True,
            "is_follower": True,
            "session_time": 1749000785,
            "base_score": 29.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "146",
            "user_name": "王岩臣",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市辖区-北京市朝阳区-朝阳区政府-朝阳区审计局-数据科",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-规划科",
                "北京市-临时-北京市运行保障指挥部-技术服务保障组-市公安局-办公室-办公室数据中心（科信办）",
                "北京市-北京市辖区-北京市大兴区-其他单位-疫情防控工作领导小组-社区防控组-数据组",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-研究部"
            ],
            "positions": [
                "测试负责人",
                "九级管理岗"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": False,
            "session_time": 1749259985,
            "base_score": 47.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "147",
            "user_name": "王岩臣",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市辖区-北京市朝阳区-朝阳区政府-朝阳区审计局-数据科",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-软件和信息产业科"
            ],
            "positions": [
                "九级管理岗"
            ],
            "is_friend": True,
            "is_top": True,
            "is_follower": True,
            "session_time": 1749346385,
            "base_score": 55.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "148",
            "user_name": "王艳",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市辖区-北京市怀柔区-北京市怀柔区人民政府-怀柔区审计局-区审计局电子数据审计中心",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-大数据支撑部"
            ],
            "positions": [
                "九级管理岗",
                "暂未填写"
            ],
            "is_friend": True,
            "is_top": True,
            "is_follower": False,
            "session_time": 1749519185,
            "base_score": 28.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "149",
            "user_name": "王岩臣",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-标准与安全部",
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-平台管理部",
                "北京市-北京市辖区-北京市怀柔区-北京市怀柔区人民政府-怀柔区审计局-区审计局电子数据审计中心"
            ],
            "positions": [
                "暂未填写"
            ],
            "is_friend": False,
            "is_top": True,
            "is_follower": False,
            "session_time": 1749432785,
            "base_score": 61.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "150",
            "user_name": "王艳",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-数据管理部",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-节能与综合利用科",
                "北京市-北京市辖区-北京市昌平区-昌平区属企业-回天大脑试点-大数据中心",
                "北京市-北京市辖区-北京市密云区-密云区政府-密云区审计局-电子数据审计科",
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-数据应用部"
            ],
            "positions": [
                "测试负责人",
                "九级管理岗"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": True,
            "session_time": 1749605585,
            "base_score": 14.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "151",
            "user_name": "王艳",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-软件和信息产业科",
                "北京市-北京市辖区-北京市延庆区-延庆区政府工作部门-延庆区审计局-数据审计分析中心",
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区科技和信息化局（区大数据局）-中小企业促进科",
                "北京市-北京市人民政府-市发展改革委-市疏整促专项办数据信息处"
            ],
            "positions": [
                "暂未填写"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": False,
            "session_time": 1748914385,
            "base_score": 76.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "152",
            "user_name": "王艳",
            "remark": "王艳丽局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京市海淀区-海淀区区委-海淀区区委组织部-区疫情防控社区防控组-区数据组",
                "北京市-北京市辖区-北京市密云区-密云区政府-密云区审计局-电子数据审计科",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-财务室",
                "北京市-北京市辖区-北京市大兴区-镇、街道-魏善庄镇-科室站所-科室大数据核查组",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-区制造业创新发展促进中心"
            ],
            "positions": [
                "九级管理岗"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": True,
            "session_time": 1749519185,
            "base_score": 92.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "153",
            "user_name": "王岩臣",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-数据管理部",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-都市产业科",
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区科技和信息化局（区大数据局）-大数据应用科"
            ],
            "positions": [
                "九级管理岗"
            ],
            "is_friend": False,
            "is_top": True,
            "is_follower": True,
            "session_time": 1749605585,
            "base_score": 10.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "154",
            "user_name": "王岩臣",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-政研组",
                "北京市-北京市辖区-北京市大兴区-国有企业-北京大兴经济开发区-大兴经济开发区防控办-数据排查组"
            ],
            "positions": [
                "测试负责人"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": False,
            "session_time": 1749087185,
            "base_score": 6.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "155",
            "user_name": "王岩",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-领导",
                "北京市-北京市辖区-北京市大兴区-国有企业-北京大兴经济开发区-大兴经济开发区防控办-数据排查组",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-大数据支撑部",
                "北京市-北京市人民政府-市发展改革委-市疏整促专项办数据信息处"
            ],
            "positions": [
                "暂未填写"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": True,
            "session_time": 1749778385,
            "base_score": 55.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "156",
            "user_name": "王岩臣",
            "remark": "王艳丽局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京经济技术开发区-档案数据中心",
                "北京市-北京市人民政府-市投资促进服务中心-区域促进处（信息数据处）",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-大数据建设管理科",
                "北京市-北京市人民政府-市经济和信息化局-内设机构-大数据建设处",
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区科技和信息化局（区大数据局）-产业发展科"
            ],
            "positions": [
                "暂未填写",
                "测试负责人"
            ],
            "is_friend": False,
            "is_top": True,
            "is_follower": False,
            "session_time": 1748827985,
            "base_score": 47.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "157",
            "user_name": "王艳",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区科技和信息化局（区大数据局）-大数据应用科",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-办公室",
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区科技和信息化局（区大数据局）-科学技术发展科"
            ],
            "positions": [
                "测试负责人"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": True,
            "session_time": 1749259985,
            "base_score": 60.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "158",
            "user_name": "王艳",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市辖区-北京市石景山区-石景山区区政府-石景山区经济和信息化局-大数据中心",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-都市产业科",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-办公室"
            ],
            "positions": [
                "九级管理岗"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": False,
            "session_time": 1749432785,
            "base_score": 24.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "159",
            "user_name": "王岩",
            "remark": "王艳丽局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京市朝阳区-朝阳区政府-朝阳区城管指挥中心-数据分析科",
                "北京市-北京市辖区-北京市大兴区-国有企业-北京大兴经济开发区-大兴经济开发区防控办-数据排查组"
            ],
            "positions": [
                "九级管理岗"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": False,
            "session_time": 1748827985,
            "base_score": 97.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "160",
            "user_name": "王艳",
            "remark": "王岩局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-区制造业创新发展促进中心",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-评审部",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-节能与综合利用科",
                "北京市-北京市辖区-北京市西城区-西城区政府-西城区科技和信息化局-数据资源管理科",
                "北京市-北京市辖区-北京市大兴区-镇、街道-长子营镇-科室站所-长子营镇政府机关数据组"
            ],
            "positions": [
                "暂未填写"
            ],
            "is_friend": False,
            "is_top": True,
            "is_follower": False,
            "session_time": 1749605585,
            "base_score": 41.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "161",
            "user_name": "王岩臣",
            "remark": "王岩局长的秘书",
            "full_dept_name": [
                "北京市-北京市人民政府-市卫生健康委-市属医院-北京天坛医院-信息管理与数据中心",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-数统部",
                "北京市-北京市辖区-北京市密云区-密云区政府-密云区审计局-电子数据审计科"
            ],
            "positions": [
                "暂未填写"
            ],
            "is_friend": False,
            "is_top": True,
            "is_follower": False,
            "session_time": 1749605585,
            "base_score": 38.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "162",
            "user_name": "王岩臣",
            "remark": "王艳丽局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京经济技术开发区-档案数据中心-领导",
                "北京市-北京市人民政府-市投资促进服务中心-区域促进处（信息数据处）",
                "北京市-北京市辖区-北京市延庆区-延庆区政府工作部门-延庆区城市管理指挥中心-数据管理科"
            ],
            "positions": [
                "测试负责人",
                "暂未填写"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": True,
            "session_time": 1748914385,
            "base_score": 74.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "163",
            "user_name": "王岩",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市辖区-北京市朝阳区-朝阳区政府-朝阳区城管指挥中心-数据分析科",
                "北京市-北京市辖区-北京市延庆区-延庆区政府工作部门-延庆区经济和信息化局-大数据中心",
                "北京市-北京市辖区-北京市密云区-密云区政府-密云区审计局-电子数据审计科"
            ],
            "positions": [
                "九级管理岗"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": True,
            "session_time": 1748741585,
            "base_score": 17.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "164",
            "user_name": "王艳",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-节能与综合利用科",
                "北京市-北京市辖区-北京市西城区-西城区政府-西城区审计局-电子数据科",
                "北京市-北京市人民政府-市水务局-局属单位-北京市智慧水务发展研究院-数据管理中心",
                "北京市-北京市人民政府-市民政局-委局直属单位-北京市困难群众救助服务指导中心（北京市居民经济状况核对中心）-数据管理科"
            ],
            "positions": [
                "暂未填写"
            ],
            "is_friend": True,
            "is_top": True,
            "is_follower": True,
            "session_time": 1749519185,
            "base_score": 46.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "165",
            "user_name": "王岩",
            "remark": "王艳丽局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京市朝阳区-朝阳区政府-朝阳区统计局-数据应用科"
            ],
            "positions": [
                "测试负责人",
                "九级管理岗"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": False,
            "session_time": 1749519185,
            "base_score": 76.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "166",
            "user_name": "王岩臣",
            "remark": "王岩局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京经济技术开发区-档案数据中心-领导",
                "北京市-北京市人民政府-市卫生健康委-市属医院-北京天坛医院-信息管理与数据中心",
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-项目评审部",
                "北京市-北京市辖区-北京市延庆区-延庆区政府工作部门-延庆区经济和信息化局-大数据中心-信息技术科"
            ],
            "positions": [
                "暂未填写"
            ],
            "is_friend": True,
            "is_top": True,
            "is_follower": True,
            "session_time": 1748827985,
            "base_score": 31.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "167",
            "user_name": "王岩",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-领导",
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区科技和信息化局（区大数据局）-办公室",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-政研组",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-软件和信息产业科",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-规划科"
            ],
            "positions": [
                "测试负责人",
                "暂未填写"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": True,
            "session_time": 1749605585,
            "base_score": 64.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "168",
            "user_name": "王岩臣",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市辖区-北京经济技术开发区-档案数据中心-史志综合处",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-评审部",
                "北京市-北京市人民政府-市人力资源社会保障局-北京市社会保险基金管理中心-数据管理部"
            ],
            "positions": [
                "暂未填写",
                "九级管理岗"
            ],
            "is_friend": True,
            "is_top": True,
            "is_follower": True,
            "session_time": 1749519185,
            "base_score": 61.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "169",
            "user_name": "王艳",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-工业发展科"
            ],
            "positions": [
                "九级管理岗"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": False,
            "session_time": 1749173585,
            "base_score": 65.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "170",
            "user_name": "王艳",
            "remark": "王艳丽局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京市石景山区-石景山区区政府-石景山区统计局-数据应用科",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-标评部",
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区科技和信息化局（区大数据局）-产业发展科",
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-发展规划部",
                "北京市-北京市辖区-北京市西城区-西城区政府-西城区科技和信息化局-数据资源管理科"
            ],
            "positions": [
                "九级管理岗"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": False,
            "session_time": 1749087185,
            "base_score": 100.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "171",
            "user_name": "汪研",
            "remark": "王岩局长的秘书",
            "full_dept_name": [
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-标评部",
                "北京市-北京市辖区-北京市大兴区-其他单位-疫情防控工作领导小组-社区防控组-数据组",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-政研组",
                "北京市-北京市辖区-北京市延庆区-延庆区政府工作部门-延庆区经济和信息化局-大数据中心-大数据管理科"
            ],
            "positions": [
                "九级管理岗",
                "暂未填写"
            ],
            "is_friend": True,
            "is_top": True,
            "is_follower": True,
            "session_time": 1748741585,
            "base_score": 91.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "172",
            "user_name": "王岩臣",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-规划科"
            ],
            "positions": [
                "测试负责人",
                "九级管理岗"
            ],
            "is_friend": True,
            "is_top": True,
            "is_follower": True,
            "session_time": 1748914385,
            "base_score": 35.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "173",
            "user_name": "王岩臣",
            "remark": "王艳丽局长的秘书",
            "full_dept_name": [
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-财务室",
                "北京市-中共北京市委员会-市委网信办-网络数据与技术处",
                "北京市-北京市辖区-北京市延庆区-延庆区政府工作部门-延庆区经济和信息化局-大数据中心-网络管理科",
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-信用信息部",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-软件和信息产业科"
            ],
            "positions": [
                "测试负责人",
                "九级管理岗"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": True,
            "session_time": 1749346385,
            "base_score": 39.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "174",
            "user_name": "王岩",
            "remark": "王岩局长的秘书",
            "full_dept_name": [
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-发展规划部",
                "北京市-北京市辖区-北京市通州区-通州区政府-通州区经信局-大数据科",
                "北京市-北京市辖区-北京市延庆区-延庆区政府工作部门-延庆区城市管理指挥中心-数据管理科"
            ],
            "positions": [
                "测试负责人",
                "九级管理岗"
            ],
            "is_friend": False,
            "is_top": True,
            "is_follower": True,
            "session_time": 1749864785,
            "base_score": 50.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "175",
            "user_name": "王艳",
            "remark": "王岩局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-镇村企业科"
            ],
            "positions": [
                "测试负责人"
            ],
            "is_friend": True,
            "is_top": True,
            "is_follower": True,
            "session_time": 1749605585,
            "base_score": 24.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "176",
            "user_name": "汪研",
            "remark": "王艳丽局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-办公室",
                "北京市-北京市辖区-北京市大兴区-镇、街道-长子营镇-科室站所-长子营镇政府机关数据组",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-大数据建设与应用创新部",
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-项目评审部"
            ],
            "positions": [
                "测试负责人"
            ],
            "is_friend": True,
            "is_top": True,
            "is_follower": False,
            "session_time": 1749000785,
            "base_score": 53.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "177",
            "user_name": "王岩臣",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市人民政府-市卫生健康委-市属医院-北京天坛医院-信息管理与数据中心",
                "北京市-北京市辖区-北京市石景山区-石景山区区政府-石景山区审计局-电子数据审计科",
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区科技和信息化局（区大数据局）"
            ],
            "positions": [
                "测试负责人",
                "暂未填写"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": True,
            "session_time": 1749173585,
            "base_score": 92.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "178",
            "user_name": "王岩臣",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区科技和信息化局（区大数据局）-信息化促进科"
            ],
            "positions": [
                "暂未填写",
                "九级管理岗"
            ],
            "is_friend": True,
            "is_top": True,
            "is_follower": False,
            "session_time": 1748914385,
            "base_score": 73.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "179",
            "user_name": "王岩",
            "remark": "王岩局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区统计局-数据中心",
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-平台管理部",
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区科技和信息化局（区大数据局）-信息化促进科",
                "北京市-北京市人民政府-市人力资源社会保障局-大数据中心",
                "北京市-北京市辖区-北京经济技术开发区-档案数据中心-档案数据处"
            ],
            "positions": [
                "测试负责人"
            ],
            "is_friend": False,
            "is_top": True,
            "is_follower": False,
            "session_time": 1749864785,
            "base_score": 7.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "180",
            "user_name": "汪研",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市人民政府-市经济和信息化局-内设机构-大数据标准与安全处",
                "北京市-北京市辖区-北京经济技术开发区-档案数据中心-史志综合处",
                "北京市-北京市人民政府-市投资促进服务中心-区域促进处（信息数据处）",
                "北京市-北京市辖区-北京市密云区-密云区政府-密云区审计局-电子数据审计科",
                "北京市-北京市辖区-北京市延庆区-延庆区政府工作部门-延庆区城市管理指挥中心-数据管理科"
            ],
            "positions": [
                "暂未填写"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": True,
            "session_time": 1749173585,
            "base_score": 35.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "181",
            "user_name": "汪研",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-数据管理部",
                "北京市-北京市辖区-北京市朝阳区-朝阳区政府-朝阳区城管指挥中心-数据分析科",
                "北京市-北京市辖区-北京市昌平区-昌平区政府-昌平区经信局-大数据管理科"
            ],
            "positions": [
                "暂未填写",
                "九级管理岗"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": False,
            "session_time": 1749605585,
            "base_score": 9.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "182",
            "user_name": "王艳",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市人民政府-市经济和信息化局-内设机构-大数据应用与产业处",
                "北京市-北京市人民政府-市水务局-局属单位-北京市智慧水务发展研究院-数据管理中心",
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区科技和信息化局（区大数据局）-科学技术发展科",
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区统计局-数据应用科",
                "北京市-中共北京市委员会-市委组织部-干部信息管理处（数据中心）"
            ],
            "positions": [
                "九级管理岗"
            ],
            "is_friend": False,
            "is_top": True,
            "is_follower": False,
            "session_time": 1748741585,
            "base_score": 44.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "183",
            "user_name": "汪研",
            "remark": "王岩局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京市大兴区-其他单位-疫情防控工作领导小组-社区防控组-数据组",
                "北京市-北京市辖区-北京市延庆区-延庆区政府工作部门-延庆区审计局-数据审计分析中心",
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-项目评审部"
            ],
            "positions": [
                "测试负责人",
                "暂未填写"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": True,
            "session_time": 1749778385,
            "base_score": 38.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "184",
            "user_name": "汪研",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-软件和信息产业科",
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区审计局-数据科"
            ],
            "positions": [
                "测试负责人"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": True,
            "session_time": 1749259985,
            "base_score": 57.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "185",
            "user_name": "王岩",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市人民政府-市经济和信息化局-内设机构-大数据建设处",
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-数据开放部",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-规划科",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-财务室",
                "北京市-北京市辖区-北京市丰台区-丰台区政府-丰台区科技信息化局-大数据管理科"
            ],
            "positions": [
                "九级管理岗"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": True,
            "session_time": 1748827985,
            "base_score": 99.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "186",
            "user_name": "王岩",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市辖区-北京市大兴区-其他单位-疫情防控工作领导小组-疫情防控办公室-信息数据组",
                "北京市-北京市辖区-北京市石景山区-石景山区区政府-石景山区审计局-电子数据审计科"
            ],
            "positions": [
                "测试负责人"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": True,
            "session_time": 1749691985,
            "base_score": 31.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "187",
            "user_name": "王岩",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市辖区-北京市怀柔区-北京市怀柔区人民政府-怀柔区审计局-区审计局电子数据审计中心",
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-运维保障部",
                "北京市-北京市人民政府-市发展改革委-市疏整促专项办数据信息处"
            ],
            "positions": [
                "九级管理岗",
                "暂未填写"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": False,
            "session_time": 1748914385,
            "base_score": 46.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "188",
            "user_name": "王艳",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-数据开放部",
                "北京市-北京市人民政府-市人力资源社会保障局-北京市社会保险基金管理中心-数据管理部",
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-平台管理部",
                "北京市-北京市辖区-北京市怀柔区-北京市怀柔区人民政府-怀柔区审计局-区审计局电子数据审计中心",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-研究部"
            ],
            "positions": [
                "九级管理岗",
                "暂未填写"
            ],
            "is_friend": False,
            "is_top": True,
            "is_follower": False,
            "session_time": 1749000785,
            "base_score": 53.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "189",
            "user_name": "王岩",
            "remark": "王艳丽局长的秘书",
            "full_dept_name": [
                "北京市-中共北京市委员会-市委组织部-干部信息管理处（数据中心）",
                "北京市-北京市辖区-北京市延庆区-延庆区政府工作部门-延庆区经济和信息化局-大数据中心-大数据管理科",
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区科技和信息化局（区大数据局）-大数据应用科",
                "北京市-北京市人民政府-市投资促进服务中心-区域促进处（信息数据处）",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-都市产业科"
            ],
            "positions": [
                "测试负责人",
                "九级管理岗"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": False,
            "session_time": 1749605585,
            "base_score": 87.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "190",
            "user_name": "王岩臣",
            "remark": "王岩局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京市延庆区-延庆区政府工作部门-延庆区审计局-数据审计分析中心",
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区科技和信息化局（区大数据局）-办公室"
            ],
            "positions": [
                "测试负责人",
                "九级管理岗"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": True,
            "session_time": 1749605585,
            "base_score": 1.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "191",
            "user_name": "汪研",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-创新发展科",
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-中心领导",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-领导"
            ],
            "positions": [
                "九级管理岗",
                "暂未填写"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": False,
            "session_time": 1749864785,
            "base_score": 87.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "192",
            "user_name": "王岩臣",
            "remark": "测试",
            "full_dept_name": [
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-信用信息部",
                "北京市-北京市人民政府-市民政局-委局直属单位-北京市困难群众救助服务指导中心（北京市居民经济状况核对中心）-数据管理科"
            ],
            "positions": [
                "暂未填写"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": False,
            "session_time": 1748655185,
            "base_score": 17.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "193",
            "user_name": "王岩臣",
            "remark": "王艳丽局长的秘书",
            "full_dept_name": [
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-大数据支撑部",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-综合产业科",
                "北京市-北京市人民政府-市经济和信息化局-内设机构-大数据标准与安全处",
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-运维保障部",
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-发展规划部"
            ],
            "positions": [
                "九级管理岗"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": True,
            "session_time": 1749864785,
            "base_score": 10.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "194",
            "user_name": "王艳",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区科技和信息化局（区大数据局）-办公室",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-编辑室",
                "北京市-北京市辖区-北京市门头沟区-门头沟区政府-门头沟区审计局-电子数据审计科"
            ],
            "positions": [
                "测试负责人",
                "暂未填写"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": True,
            "session_time": 1749259985,
            "base_score": 62.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "195",
            "user_name": "王岩臣",
            "remark": "王岩局长的秘书",
            "full_dept_name": [
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区科技和信息化局（区大数据局）-中小企业促进科",
                "北京市-北京市辖区-北京市怀柔区-北京市怀柔区人民政府-怀柔区审计局-区审计局电子数据审计中心",
                "北京市-北京市辖区-北京市大兴区-其他单位-疫情防控工作领导小组-社区防控组-数据组"
            ],
            "positions": [
                "九级管理岗",
                "暂未填写"
            ],
            "is_friend": True,
            "is_top": True,
            "is_follower": False,
            "session_time": 1748827985,
            "base_score": 37.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "196",
            "user_name": "王岩",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市辖区-北京市东城区-东城区政府-东城区科技和信息化局（区大数据局）-中小企业促进科",
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-研究部",
                "北京市-北京市辖区-北京市通州区-通州区政府-通州区经信局-大数据科",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）-都市产业科"
            ],
            "positions": [
                "九级管理岗",
                "测试负责人"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": True,
            "session_time": 1749432785,
            "base_score": 96.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "197",
            "user_name": "汪研",
            "remark": "无",
            "full_dept_name": [
                "北京市-北京市辖区-北京市密云区-密云区政府-密云区审计局-电子数据审计科"
            ],
            "positions": [
                "暂未填写",
                "测试负责人"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": True,
            "session_time": 1749087185,
            "base_score": 69.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "198",
            "user_name": "王岩",
            "remark": "王岩局长的秘书",
            "full_dept_name": [
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-发展规划部",
                "北京市-北京市人民政府-市经济和信息化局-直属机构及事业单位-北京市大数据中心-数据开放部",
                "北京市-北京市辖区-北京市顺义区-顺义区政府-区经济和信息化局（区大数据局、区创新办）"
            ],
            "positions": [
                "暂未填写"
            ],
            "is_friend": False,
            "is_top": False,
            "is_follower": False,
            "session_time": 1749087185,
            "base_score": 44.0,
            "re_rank_score": 0.0
        },
        {
            "user_id": "199",
            "user_name": "王艳",
            "remark": "王艳丽局长的秘书",
            "full_dept_name": [
                "北京市-北京市人民政府-市卫生健康委-直属单位-北京市卫生健康大数据与政策研究中心-编辑室",
                "北京市-北京市辖区-北京市石景山区-石景山区区政府-石景山区统计局-数据应用科"
            ],
            "positions": [
                "暂未填写",
                "九级管理岗"
            ],
            "is_friend": True,
            "is_top": False,
            "is_follower": True,
            "session_time": 1749087185,
            "base_score": 68.0,
            "re_rank_score": 0.0
        }
    ]
}


async def fetch(session, url):
    """异步发送请求并返回响应内容"""
    async with session.get(url) as response:
        # 获取响应状态码和响应内容
        status = response.status
        content = await response.text()
        return status, content


async def post(session, url, headers=None, data=None):
    """异步发送 POST 请求并返回响应内容"""
    async with session.post(url, headers=headers, json=data) as response:
        status = response.status
        content = await response.text()
        return status, content


async def main():
    """主函数，负责并发请求的调度"""
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(CONCURRENT_REQUESTS):
            task = asyncio.create_task(post(session, TARGET_URL, headers=HEADERS, data=DATA))
            tasks.append(task)

        # 等待所有任务完成
        results = await asyncio.gather(*tasks)

        # 打印结果
        for i, (status, content) in enumerate(results):
            print(f"Request {i + 1}: Status {status}, Content: {content[:100]}...")


if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    end_time = time.time()
    print(f"Total time taken: {(end_time - start_time) * 1000} ms")
