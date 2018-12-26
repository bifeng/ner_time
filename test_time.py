from TimeNormalizer import TimeNormalizer

tn = TimeNormalizer(isPreferFuture=False)


class TestTime:

    def test_single(self):

        values = [
            ['6号',['6号']],
            ['今天',['今天']],
            ['下午3点',['下午3点']],
            ['今天下午三点',['今天下午三点']],
            ['二月十号', ['二月十号']],

            ['冬至',['冬至']],
            ['今年儿童节晚上9点1刻',['今年儿童节晚上9点1刻']],
            ['2013年二月二十八日下午四点三十分二十九秒',['2013年二月二十八日下午四点三十分二十九秒']],


            ['晚上8点到上午10点之间',['晚上8点','上午10点']],
            ['周六3点到5点',['周六3点','5点']],
            ['晚上八点到九点，明天中午给我',['晚上八点','九点','明天中午']],
            ['33天2分钟4秒,33天2分钟8秒, 星期五',['33天2分钟4秒','33天2分钟8秒', '星期五']],
            ['星期三下午至星期五上午起飞，星期四',['星期三下午','星期五上午','星期四']],
            ['今天星期几',['今天']],
            ['今天几月',['今天']],
            ['昨天深夜',['昨天深夜']],
            ['今年好几月',['今年']],
            ['今年下月',['今年下月']],
            ['今年晚些时候',['今年']]

        ]

        for index in range(len(values)):
            except_res = values[index]

            sentence = except_res[0]

            res = tn.parse(target=sentence)

            assert except_res[1] == res.get('text'), f'{sentence} fail'

