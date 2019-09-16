columns_to_merge = {
    "company": ['公司 / 組織名稱 ( Company )', '公司/組織名稱'],
    "gender": ['性別', '性別 ( Gender )'],
    "nickname": ['慣用暱稱 ( ID )', '慣用暱稱/ID', '暱稱/慣用ID (6個中文字或10個英文字母)'],
    "work_south": ['在南部地區工作之意願 ( Will to work in South in Taiwan )', 
                   '在南部地區工作之意願 ( Would you like to work in Southern Taiwan )'],
    "working_city": ['工作地區', '工作地區 ( Work Conutry )'],
    "job_title": ['職稱', '職稱 ( Job Title )'],
    "job_type": ['職稱類型', '職務類型'],
    "apply_support": ['幫忙MOPCON 2015申請『高雄市會議展覽活動獎勵辦法』',
       '幫忙MOPCON 2016申請『高雄市會議展覽活動獎勵辦法』',
       '幫忙MOPCON 2017申請『高雄市會議展覽活動獎勵辦法』',
       '幫忙MOPCON 2018申請『高雄市會議展覽活動獎勵辦法』'],
    "phone_number": ['手機', '手機 ( Phone )'],
    "real_name": ['姓名']
    # , '真實姓名 ( Real Name ) ( 如願意幫忙 MOPCON 申請補助，同身分證或護照 )',
    #    '真實姓名(如願意幫忙MOPCON申請補助，請填寫。同身分證或護照)']
}


synoniums = {
  "companies": {
      "foxconn": ['鴻海', 'Foxconn', 'foxconn', '鴻海精密', '鴻海精密工業股份有限公司'],
      "newegg": ['台灣新蛋', 'Newegg', 'newegg', '新蛋', '新蛋科技'],
      "TVBS": ['聯意製作股份有限公司'],
      "wistron": ['緯創資通', '緯創資通股份有限公司', 'wistron', 'Wistron', '緯創']
  },
  "schools": {
      "NCKU": ['NCKU', '成大', '國立成功大學', '成功大學', 'ncku'],
      "NSYSU": ['中山大學', '國立中山大學', 'NSYSU'],
      "NKUAS": ['國立高雄應用科技大學', '高雄應用科技大學', '高應大'],
      "NKFUST": ['高雄第一科技大學', '國立高雄第一科技大學'],
      "NUK": ['高雄大學', '國立高雄大學'],
      "STUST": ['南臺科技大學', '南台科技大學']
  },
  "skip": {
    "none": ['無', '', 'none', 'no', 'com', '自由業', '待業中', '個人', '自由工作者', 
             'freelancer', 'soho', 'No', '.', '暫無', '123', '暫不公開', 'HH', 
             'Freelancer', '自營', 'X', 'Pc', 'Null', 'test', '略', '', '測試', 
             '無業', '畢業生', 'na', '私人', '替代役', 'Nomads', '1', 'TEST', 'home',
             '接案', '獨立開發者', 'Soho']
  },
  "job_type": {
    "PM": ['企劃/專案管理', '企劃/專案管理 ( Project Management )'],
    "Programmer": ['軟體技術', '軟體技術 ( Software Tech )'],
    "Design": ['美術設計', '美術設計 ( Art Design )'],
    "Management": ['決策管理 (  Decision Management )', '決策管理'],
    "Education": ['教育相關 ( Education )', '教育相關'],
    "Student": ['學生 ( Student )', '學生'],
    "Others": ['其他 ( Others )', '其他']
  },
  "job_titles": {
    "ceo": ['ceo', 'coo', '創辦人', '總經理', '老闆', '董事長', 'ceo & co-founder', 'ceo / co-founder', 'co-founder', 'cofounder', 'founder', '共同創辦人', '創辦人', '創業家', '執行長', '營運長', '理事長'],
    "cto": ['cto', '技術總監', '技術長', 'chief programme', 'cio', 'cio', 'cloud engineering lead', 'co-founder & technical director', 'frontend tech lead & team lead'],
    "community": ['community manager', 'community manger'],
    "data": ['data analyst', 'data engineer', 'data scientist', '大數據工程師'],
    "design": ['design', 'design manager', 'design technologist', 'ui designer', 'ui/ux developer', '使用者經驗研究員', '使用者經驗設計師'],
    "engineer": ['全端工程師', '前端工程師', '副工程師', '實習工程師', '工程師', '後端工程師', '應用軟體工程師', '攻城獅', '測試工程師', '研發工程師', '程序員', '程式工程師', '程式開發工程師', '資深軟體工程師', '軟體工程師'],
    "scholar": ['副教授', '博士候選人', '博士後研究員', '博士生', '碩士生']
  }
}

fields_to_merge = {
    # should revese its key / value to minimize the manual part and generate the mapping automatically
    'job_type': {'企劃/專案管理': 'pm', '企劃/專案管理 ( Project Management )': 'pm',
                 '其他': 'other', '其他 ( Others )': 'other',
                 '學生': 'student', '學生 ( Student )': 'student',
                 '教育相關': 'edu', '教育相關 ( Education )': 'edu',
                 '決策管理': 'gm', '決策管理 (  Decision Management )': 'gm',
                 '美術設計': 'design', '美術設計 ( Art Design )': 'design',
                 '軟體技術': 'programmer', '軟體技術 ( Software Tech )': 'programmer'
    }

}

# interesting data
# 驣星軟體, 迪卡儂, 