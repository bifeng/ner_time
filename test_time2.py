import arrow
from datetime import datetime
from TimeNormalizer import TimeNormalizer
from pprint import pprint as print

tn = TimeNormalizer(isPreferFuture=False)

base_time = arrow.Arrow.fromdatetime(datetime(2018, 12, 24, 14, 50, 00))


sentence = '晚上8点到上午10点之间'
sentence = '今天'
# sentence = '现在'
out = tn.parse(target=sentence, timeBase=base_time)
print(out)

