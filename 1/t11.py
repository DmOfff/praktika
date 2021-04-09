# Вычислите значение выражения |x−5|−sinx3+x2+2014−−−−−−−−√cos2x−3 при x=−2.34. Ответ: -1.76911 (проверено!)
# http://www.itmathrepetitor.ru/prog/zadachi-na-vychisleniya/

import math

x = -2.34
print((abs(x - 5) - math.sin(x))/3 + math.sqrt(x*x + 2014) * math.cos(2 * x) - 3)
