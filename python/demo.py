def douyu_rank(rankName, statType):
    '''
        斗鱼主播排行数据抓取
        [数据地址](https://www.douyu.com/directory/rank_list/game)

        * `rankName` anchor(巨星主播榜),fans(主播粉丝榜),haoyou(土豪实力榜),user(主播壕友榜)
        * `statType` day(日),week(周),month(月)
    '''
    if not isinstance(rankName, ERankName):
        raise Exception("rankName 类型错误，必须是ERankName枚举")
    if not isinstance(statType, EStatType):
        raise Exception("statType 类型错误，必须是EStatType枚举")

    rankName = '%sListData' % rankName.name
    statType = '%sListData' % statType.name
    # 请求获取html源码
    rs = rq.get(
        "https://www.douyu.com/directory/rank_list/game",
        headers={'User-Agent': 'Mozilla/5.0'})
    # 正则解析出数据
    mt = re.search(r'rankListData\s+?=(.*?);', rs, re.S)
    if (not mt):
        print
        u"无法解析rankListData数据"
        return
    grps = mt.groups()
    # 数据转json
    rankListDataStr = grps[0]
    rankListData = json.loads(rankListDataStr)
    dayList = rankListData[rankName][statType]
    # 修改排序
    dayList.sort(key=lambda k: (k.get('id', 0)), reverse=False)
    return dayList


def douyu_room(romm_id):
    '''
        主播房间信息解析
        [数据地址](https://www.douyu.com/xxx)
        'romm_id' 主播房号
    '''
    rs = rq.get(
        ("https://www.douyu.com/%s" % romm_id),
        headers={'User-Agent': 'Mozilla/5.0'})
    mt = re.search(r'\$ROOM\s+?=\s+?({.*?});', rs, re.S)
    if (not mt):
        print
        u"无法解析ROOM数据"
        return
    grps = mt.groups()
    roomDataStr = grps[0]
    roomData = json.loads(roomDataStr)
    return roomData


def run():
    '''
        测试爬虫
    '''
    datas = douyu_rank(ERankName.anchor, EStatType.month)
    print
    '\r\n主播排行榜：'
    for item in datas:
        room_id = item['room_id']
        roomData = douyu_room(room_id)
        rommName = None
        if roomData is not None:
            rommName = roomData['room_name']
        roomInfo = (u'房间(%s):%s' % (item['room_id'], rommName))
        print
        item['id'], item[
            'nickname'], roomInfo, '[' + item['catagory'] + ']'

