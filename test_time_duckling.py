# https://github.com/facebook/duckling/blob/master/Duckling/TimeGrain/ZH/Rules.hs
# https://github.com/facebook/duckling/blob/master/Duckling/Time/ZH/Rules.hs
# https://github.com/facebook/duckling/blob/master/Duckling/Time/ZH/Corpus.hs
# grains = [ ("second (grain)", "秒(钟|鐘)?", TG.Second)
#          , ("minute (grain)", "分(钟|鐘)?", TG.Minute)
#          , ("hour (grain)",
#              "小时|小時|鐘(\x982d)?", TG.Hour)
#          , ("day (grain)", "天|日", TG.Day)
#          , ("week (grain)",
#              "周|週|礼拜|禮拜|星期", TG.Week)
#          , ("month (grain)", "月", TG.Month)
#          , ("year (grain)", "年", TG.Year)
#          ]


# pip install duckling
# https://github.com/FraBle/python-duckling


from duckling import Duckling
d = Duckling()
d.load() # always load the model first
print(d.parse('now'))
print(d.parse('Tuesday'))
print(d.parse('4 a.m.'))
print(d.parse('everyday 10 p.m.'))
print(d.parse('from 4 a.m. to 10 p.m.'))
print(d.parse('this quarter'))
print(d.parse('After a quarter of an hour'))

