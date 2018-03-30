import itertools
import scipy.misc
import math
all_tokens=['water', 'vapor', u'gaseou', 'state', 'water', u'invis', 'human', u'humid', u'indic', 'likelihood', u'precipit', 'higher', u'humid', u'reduc', u'effect', u'sweat', u'cool', u'bodi', u'reduc', 'rate', u'evapor', u'moistur', 'skin', u'rel', u'humid', 'ratio', 'partial', u'pressur', 'water', 'vapor', 'equilibrium', 'vapor', u'pressur', 'water', 'given', u'temperatur', 'hear', 'weather', u'forecast', 'talk', u'humid', 'hear', 'talk', u'differ', u'term', u'absolut', u'humid', u'rel', u'humid', u'absolut', u'humid', 'amount', 'water', 'vapor', u'divid', 'amount', 'certain', u'volum', 'particular', u'temperatur', 'hotter', 'water', 'vapor', u'rel', u'humid', 'ratio', 'current', u'absolut', u'humid', 'highest', u'possibl', u'absolut', u'humid', u'depend', 'current', u'temperatur', u'read', 'percent', u'rel', u'humid', u'mean', u'total', u'satur', 'water', 'vapor', 'hold', u'creat', u'possibl', 'rain', u'simplifi', u'descript', u'rel', u'absolut', u'humid', u'humid', u'definit', 'humid', u'condit', u'moist', u'damp', 'weather', u'report', u'humid', u'usual', u'explain', u'rel', u'humid', u'rel', u'humid', 'amount', 'water', 'vapor', u'actual', u'express', u'percentag', 'maximum', 'amount', 'water', 'vapor', 'hold', u'temperatur', 'think', u'chilli', u'degre', u'celsiu', u'degre', 'fahrenheit', 't-shirt', 'kind', 'washington', u'degre', 'percent', u'humid', 'know', u'number', 'mean', u'exactli', u'humid', u'percentag', 'tell', 'care', u'fact', u'humid', u'affect', u'daili', u'live', u'fifti', 'percent', u'humid', u'spong', 'half', u'rel', u'humid', 'amount', u'moistur', u'compar', 'hold', u'temperatur', 'hold', u'moistur', u'condens', 'indoor', u'qualiti', u'environment', u'protect', u'agenc', u'list', 'indoor', u'qualiti', 'among', u'environment', 'health', u'threat', 'three', u'compon', u'healthi', 'must', 'fresh', 'clean', 'proper', u'humid', u'less', u'rel', u'humid', 'fresh', u'outsid', 'rich', 'oxygen', u'flush', 'home', u'humid', u'presenc', 'water', 'vapour', 'high', u'humidti', u'mean', 'water', 'vapour', u'humid', u'mean', u'littl', 'said', u'satur', u'contain', 'maximum', 'amount', 'vapour', u'possibl', 'particular', u'temperatur', 'given', 'time', 'amount', 'water', 'vapour', u'humid', u'import', 'aspect', u'atmospher', u'affect', 'weather', u'climat', 'video', 'lesson', 'learn', u'differ', u'type', u'humid', 'understand', u'temperatur', u'affect', 'water', 'vapor', u'humid', u'import', 'thing', 'understand', u'temperatur', 'drop', 'winter', 'weather', u'arriv', u'thing', 'know', 'home', u'humid', u'level', 'winter', 'term', u'humid', u'gener', u'refer', 'amount', 'water', 'vapor', u'atmospher', u'atmospher', 'vapor', u'pressur', u'measur', 'number', u'molecul', 'present', 'given', u'temperatur', 'vapor', u'pressur', 'water', u'thu', u'measur', 'amount', 'water', 'vapor', u'satur', 'vapor', u'pressur', u'defin', u'humid', u'moder', u'degre', u'wet', u'especi', u'atmospher', u'humid', u'sentenc', 'english', 'edit', u'etymolog', 'edit', u'middl', 'english', u'humidit', 'french', u'mediev', 'latin', u'humidita', 'latin', u'umidu', 'damp', 'moist', u'pronunci', 'edit', '/hjumdti/', 'noun', 'edit', u'humid', u'usual', u'uncount', 'plural', u'humid', u'damp', u'especi', 'amount', 'water', 'vapour', u'use', 'cbse', u'ics', 'ncert', u'intern', u'student', 'grade', 'subject', u'geographi', 'lesson', 'topic', u'turn', u'scientif', u'explan', 'behind', u'say', 'heat', u'humid', 'learn', 'matter', 'type', u'climat', 'live', u'level', u'rel', u'humid', 'affect', 'comfort', 'home', 'well', 'proper', u'function', u'heat', u'condit', u'unit', u'manag', 'ideal', 'indoor', u'humid', u'prioriti', u'everi', u'homeown', u'especi', u'come', u'tailor', u'heat', u'humid', u'mean', u'definit', u'humid', u'qualiti', 'humid', 'learn', u'humid', u'humid', 'amount', 'water', 'vapour', u'variabl', u'atmospher', u'constitut', 'major', 'factor', u'climat', 'weather', 'brief', 'treatment', u'humid', u'follow', 'full', 'treatment', u'climat', u'atmospher', u'humid', u'precipit', u'atmospher', 'water', 'vapour', u'humid', u'measur', 'amount', 'water', 'vapour', 'find', u'differ', u'type', u'humid', u'complaint', u'humid', 'peak', 'summer', 'd.c.', 'nation', 'swamp', u'turn', 'hard', 'drain', u'sometim', u'complaint', u'heavi', u'feel', u'sultri', u'moistur', u'sticki', u'cloth', 'though', u'sometim', 'humid', u'peopl', 'need', u'rel', u'humid', u'usual', u'contain', 'water', 'vapour', 'amount', u'depend', u'primarili', u'temperatur', 'warm', 'hold', u'moistur', 'cold', u'temperatur', u'fall', 'maximum', 'amount', 'water', 'hold', 'also', u'fall', 'ratio', 'water', 'vapour', 'maximum', 'cubic', u'metr', u'outsid', 'zero', u'degre', u'rel', u'humid', u'contain', u'gram', 'water', 'vapour', u'heat', u'twenti', u'degre', u'averag', u'temperatur', u'insid', 'home', 'without', u'ad', 'water', 'vapour', u'rel', u'humid', u'comfort', u'inde', 'minimum', u'humid', u'concentr', 'water', 'vapor', u'concentr', u'express', u'absolut', u'humid', u'specif', u'humid', u'rel', u'humid', u'rel', u'humid', u'frequent', u'encount', u'measur', u'humid', u'regularli', u'use', 'weather', u'forecast', u'import', 'part', 'weather', u'report', u'publish', '2009.', 'zealand', u'sometim', u'affect', 'weather', 'pattern', u'feed', u'subtrop', 'onto', 'north', 'island', 'even', 'whole', u'countri', u'subtrop', u'peopl', 'often', 'comment', u"'muggi", 'blog', 'meteorologist', 'tunster', u'explain', u'differ', u'rel', u'discov', 'role', u'humid', u'play', u'keep', 'cool', u'comfort', u'readi', 'sleep', 'summer', 'heat', 'peak', 'sweat', 'start', 'pour', u'everi', 'pore', u'normal', u'stinki', u'process', u'bodi', u'cool', 'high', u'humid', u'turn', 'heat', u'sticki', 'start', 'feel', u'uncomfort', 'sweat', u'nowher', 'higher', u'humid', 'local', 'weather', 'radar', u'rainfal', u'advisori', u'temperatur', 'dewpoint', u'humid', 'ground', 'water', 'past', 'data', u'file', u'pressur', 'soil', u'moistur', 'soil', u'temperatur', 'solar', u'radiat', u'satellit', 'station', u'meteogram', 'station', u'plot', 'upper', 'wind', u'extrem', u'temperatur', u'heatwav', u'bring', 'problem', u'humid', 'burden', 'water', 'vapor', u'mercuri', u'climb', u'extrem', 'data', u'except', u'visibl', u'collect', u'autom', 'weather', u'instrument', u'automat', u'publish', 'soon', u'gener', 'could', u'instanc', u'gap', 'data', u'technic', u'problem', 'data', 'subject', u'correct', u'subsequ', u'necessari', u'object', u'observ', 'relationship', u'temperatur', u'rel', u'humid', u'humid', 'control', u'system', u'remov', 'water', 'vapor', 'indoor', 'learn', u'help', 'thermal', 'comfort', u'prevent', 'mold', 'mildew', u'save', u'energi', 'cabin', u'humid', u'dehydr', u'humid', 'aircraft', u'cabin', u'usual', u'less', u'humid', 'home', u'normal', u'humid', u'caus', 'skin', u'dryness', 'discomfort', u'eye', 'mouth', 'nose', u'present', 'risk', 'health', 'skin', u'moistur', 'lotion', u'salin', 'nasal', 'spray', u'moistur', u'humid', 'present', u'everi', 'home', u'build', 'amount', u'humid', u'benefici', 'higher', 'lead', u'condens', 'mould', u'develop', u'increas', u'awar', u'caus', u'place', u'condens', u'like', 'collect', u'reduc', 'amount', u'effect', u'level', u'humid', u'appropri', 'airway', u'optim', u'humid', u'essenti', u'humid', u'synonym', u'humid', 'thesaurus.com', 'free', u'onlin', u'thesauru', u'antonym', u'definit', u'dictionari', 'word', 'learn', u'import', 'control', u'humid', 'among', u'factor', u'critic', 'care', u'area', 'like', u'hospit', u'compound', u'center', 'road', 'weather', u'inform', u'know', u'exactli', u'go', 'roadway', u'futur', u'success', u'decis', u'make', 'read', 'ptu300', u'combin', u'pressur', u'humid', u'temperatur', u'transmitt', u'combin', u'pressur', u'humid', u'temperatur', u'transmitt', 'ptu300', u'demand', 'ideal', u'daytim', u'humid', u'orchid', 'summer', u'day', 'warm', u'humid', u'increas', u'place', u'plant', 'shallow', 'dish', 'tray', u'contain', u'pebbl', 'water', 'sure', 'keep', 'water', u'top', u'pebbl', 'never', 'water', 'touch', 'bottom', u'capillari', u'rel', u'humid', 'amount', u'moistur', u'percentag', 'amount', u'actual', 'hold', 'warmer', 'hold', u'moistur', 'cooler', u'mean', 'given', 'amount', u'atmospher', u'moistur', 'lower', 'warm', 'would', 'cool', 'seen', u'compar', u'humid', u'humid', u'product', u'discontinu', 'found', 'support', u'literatur', u'seri', '2-wire', 'design', 'duct', 'wall', 'mount', u'transmitt', u'seri', 'rh/rhl', u'accuraci', u'option', 'display', u'transmitt', u'divis', 'love', 'mercoid', u'humid', 'part', 'weather', u'forecast', 'long', 'gotten', u'news', u'begin', 'weather', u'forecast', u'friendli', 'neighborhood', 'weatherperson', u'tell', u'condit', 'moment', 'current', u'temperatur', u'rel', u'humid', 'past', u'coupl', u'decad', u'humid', u'rel', 'proper', u'humid', u'level', 'keep', 'healthier', u'comfort', u'heat', u'ventil', u'condit', 'hvac', 'system', 'heat', 'cool', 'home', 'also', 'keep', u'humid', u'comfort', 'level', 'winter', 'summer', u'delic', u'balanc', 'feel', u'choke', u'stifl', u'inescap', 'think', u'humid', u'abhorr', u'go', 'much', u'wors', u'research', u'warn', u'becom', 'major', 'killer', 'within', u'year', u'measur', u'control', u'rel', u'humid', u'humid', 'option', u'consist', 'special', u'humid', 'chamber', u'circul', u'heat', 'bath', u'humid', u'gener', u'allow', 'perform', u'measur', 'optimum', u'condit', u'everi', u'deform', 'mode', 'special', u'readjust', u'necessari', u'instal', u'humid', 'know', u'keep', u'humid', 'home', 'winter', u'import', 'skin', 'throat', u'overal', 'health', 'also', 'know', 'vital', 'health', 'home', u'humid', u'level', u'furnitur', u'hous', u'deterior', 'certain', u'germ', 'thrive', 'talk', u'climat', u'model', u'simul', 'strong', 'landocean', 'contrast', u'respons', u'near-surfac', u'rel', u'humid', 'global', u'warm', u'rel', u'humid', u'tend', u'increas', u'slightli', u'ocean', u'decreas', u'substanti', 'land', u'surfac', u'energi', u'balanc', u'argument', u'use', 'understand', u'respons', 'ocean', 'difficult']
dpw=['water', 'vapor', u'gaseou', 'state', 'water', u'invis', 'human', u'indic', 'likelihood', u'precipit', 'higher', u'humid', u'reduc', u'effect', u'invis', 'human', u'humid', u'indic', 'likelihood', u'precipit', 'higher', u'reduc', u'effect', u'sweat', u'cool', u'bodi', u'reduc', 'rate', u'bodi', u'reduc', 'rate', u'evapor', u'moistur', 'skin', u'rel', 'ratio', 'partial', u'pressur', 'water', 'vapor', 'equilibrium', 'vapor', 'water', 'given', u'temperatur', 'hear', 'weather', u'forecast', 'talk', 'hear', 'talk', u'differ', u'term', u'absolut', u'humid', u'rel', 'talk', u'humid', 'hear', 'talk', u'differ', u'term', u'absolut', u'rel', u'humid', u'absolut', u'humid', 'amount', 'water', 'vapor', 'hear', 'talk', u'differ', u'term', u'absolut', u'humid', u'rel', u'absolut', u'humid', 'amount', 'water', 'vapor', u'divid', 'amount', u'differ', u'term', u'absolut', u'humid', u'rel', u'humid', u'absolut', 'amount', 'water', 'vapor', u'divid', 'amount', 'certain', u'volum', u'volum', 'particular', u'temperatur', 'hotter', 'water', 'vapor', u'rel', 'ratio', 'current', u'absolut', u'humid', 'highest', u'possibl', u'absolut', 'water', 'vapor', u'rel', u'humid', 'ratio', 'current', u'absolut', 'highest', u'possibl', u'absolut', u'humid', u'depend', 'current', u'temperatur', 'ratio', 'current', u'absolut', u'humid', 'highest', u'possibl', u'absolut', u'depend', 'current', u'temperatur', u'read', 'percent', u'rel', u'humid', u'humid', u'depend', 'current', u'temperatur', u'read', 'percent', u'rel', u'mean', u'total', u'satur', 'water', 'vapor', 'hold', u'creat', u'creat', u'possibl', 'rain', u'simplifi', u'descript', u'rel', u'absolut', u'humid', u'definit', 'humid', u'condit', u'moist', u'damp', 'weather', u'possibl', 'rain', u'simplifi', u'descript', u'rel', u'absolut', u'humid', u'definit', 'humid', u'condit', u'moist', u'damp', 'weather', u'report', u'simplifi', u'descript', u'rel', u'absolut', u'humid', u'humid', u'definit', u'condit', u'moist', u'damp', 'weather', u'report', u'humid', u'usual', u'definit', 'humid', u'condit', u'moist', u'damp', 'weather', u'report', u'usual', u'explain', u'rel', u'humid', u'rel', u'humid', 'amount', u'damp', 'weather', u'report', u'humid', u'usual', u'explain', u'rel', u'rel', u'humid', 'amount', 'water', 'vapor', u'actual', u'express', u'report', u'humid', u'usual', u'explain', u'rel', u'humid', u'rel', 'amount', 'water', 'vapor', u'actual', u'express', u'percentag', 'maximum', u'degre', 'fahrenheit', 't-shirt', 'kind', 'washington', u'degre', 'percent', 'know', u'number', 'mean', u'exactli', u'humid', u'percentag', 'tell', u'degre', 'percent', u'humid', 'know', u'number', 'mean', u'exactli', u'percentag', 'tell', 'care', u'fact', u'humid', u'affect', u'daili', 'mean', u'exactli', u'humid', u'percentag', 'tell', 'care', u'fact', u'affect', u'daili', u'live', u'fifti', 'percent', u'humid', u'spong', u'fact', u'humid', u'affect', u'daili', u'live', u'fifti', 'percent', u'spong', 'half', u'rel', u'humid', 'amount', u'moistur', u'compar', u'live', u'fifti', 'percent', u'humid', u'spong', 'half', u'rel', 'amount', u'moistur', u'compar', 'hold', u'temperatur', 'hold', u'moistur', 'three', u'compon', u'healthi', 'must', 'fresh', 'clean', 'proper', u'less', u'rel', u'humid', 'fresh', u'outsid', 'rich', 'oxygen', 'must', 'fresh', 'clean', 'proper', u'humid', u'less', u'rel', 'fresh', u'outsid', 'rich', 'oxygen', u'flush', 'home', u'humid', u'humid', 'fresh', u'outsid', 'rich', 'oxygen', u'flush', 'home', u'presenc', 'water', 'vapour', 'high', u'humidti', u'mean', 'water', 'water', 'vapour', 'high', u'humidti', u'mean', 'water', 'vapour', u'mean', u'littl', 'said', u'satur', u'contain', 'maximum', 'amount', 'particular', u'temperatur', 'given', 'time', 'amount', 'water', 'vapour', u'import', 'aspect', u'atmospher', u'affect', 'weather', u'climat', 'video', 'weather', u'climat', 'video', 'lesson', 'learn', u'differ', u'type', 'understand', u'temperatur', u'affect', 'water', 'vapor', u'humid', u'import', u'type', u'humid', 'understand', u'temperatur', u'affect', 'water', 'vapor', u'import', 'thing', 'understand', u'temperatur', 'drop', 'winter', 'weather', 'drop', 'winter', 'weather', u'arriv', u'thing', 'know', 'home', u'level', 'winter', 'term', u'humid', u'gener', u'refer', 'amount', u'thing', 'know', 'home', u'humid', u'level', 'winter', 'term', u'gener', u'refer', 'amount', 'water', 'vapor', u'atmospher', u'atmospher', 'amount', 'water', 'vapor', u'satur', 'vapor', u'pressur', u'defin', u'moder', u'degre', u'wet', u'especi', u'atmospher', u'humid', u'sentenc', u'defin', u'humid', u'moder', u'degre', u'wet', u'especi', u'atmospher', u'sentenc', 'english', 'edit', u'etymolog', 'edit', u'middl', 'english', 'damp', 'moist', u'pronunci', 'edit', '/hjumdti/', 'noun', 'edit', u'usual', u'uncount', 'plural', u'humid', u'damp', u'especi', 'amount', '/hjumdti/', 'noun', 'edit', u'humid', u'usual', u'uncount', 'plural', u'damp', u'especi', 'amount', 'water', 'vapour', u'use', 'cbse', 'topic', u'turn', u'scientif', u'explan', 'behind', u'say', 'heat', 'learn', 'matter', 'type', u'climat', 'live', u'level', u'rel', 'learn', 'matter', 'type', u'climat', 'live', u'level', u'rel', 'affect', 'comfort', 'home', 'well', 'proper', u'function', u'heat', u'function', u'heat', u'condit', u'unit', u'manag', 'ideal', 'indoor', u'prioriti', u'everi', u'homeown', u'especi', u'come', u'tailor', u'heat', u'prioriti', u'everi', u'homeown', u'especi', u'come', u'tailor', u'heat', u'mean', u'definit', u'humid', u'qualiti', 'humid', 'learn', u'humid', u'especi', u'come', u'tailor', u'heat', u'humid', u'mean', u'definit', u'qualiti', 'humid', 'learn', u'humid', u'humid', 'amount', 'water', u'tailor', u'heat', u'humid', u'mean', u'definit', u'humid', u'qualiti', 'learn', u'humid', u'humid', 'amount', 'water', 'vapour', u'variabl', u'humid', u'mean', u'definit', u'humid', u'qualiti', 'humid', 'learn', u'humid', 'amount', 'water', 'vapour', u'variabl', u'atmospher', u'constitut', u'mean', u'definit', u'humid', u'qualiti', 'humid', 'learn', u'humid', 'amount', 'water', 'vapour', u'variabl', u'atmospher', u'constitut', 'major', u'constitut', 'major', 'factor', u'climat', 'weather', 'brief', 'treatment', u'follow', 'full', 'treatment', u'climat', u'atmospher', u'humid', u'precipit', 'treatment', u'humid', u'follow', 'full', 'treatment', u'climat', u'atmospher', u'precipit', u'atmospher', 'water', 'vapour', u'humid', u'measur', 'amount', u'climat', u'atmospher', u'humid', u'precipit', u'atmospher', 'water', 'vapour', u'measur', 'amount', 'water', 'vapour', 'find', u'differ', u'type', u'measur', 'amount', 'water', 'vapour', 'find', u'differ', u'type', u'complaint', u'humid', 'peak', 'summer', 'd.c.', 'nation', 'swamp', 'water', 'vapour', 'find', u'differ', u'type', u'humid', u'complaint', 'peak', 'summer', 'd.c.', 'nation', 'swamp', u'turn', 'hard', u'feel', u'sultri', u'moistur', u'sticki', u'cloth', 'though', u'sometim', u'peopl', 'need', u'rel', u'humid', u'usual', u'contain', 'water', u'cloth', 'though', u'sometim', 'humid', u'peopl', 'need', u'rel', u'usual', u'contain', 'water', 'vapour', 'amount', u'depend', u'primarili', 'maximum', 'cubic', u'metr', u'outsid', 'zero', u'degre', u'rel', u'contain', u'gram', 'water', 'vapour', u'heat', u'twenti', u'degre', u'insid', 'home', 'without', u'ad', 'water', 'vapour', u'rel', u'comfort', u'inde', 'minimum', u'humid', u'concentr', 'water', 'vapor', 'water', 'vapour', u'rel', u'humid', u'comfort', u'inde', 'minimum', u'concentr', 'water', 'vapor', u'concentr', u'express', u'absolut', u'humid', u'humid', u'concentr', 'water', 'vapor', u'concentr', u'express', u'absolut', u'specif', u'humid', u'rel', u'humid', u'rel', u'humid', u'frequent', 'water', 'vapor', u'concentr', u'express', u'absolut', u'humid', u'specif', u'rel', u'humid', u'rel', u'humid', u'frequent', u'encount', u'measur', u'concentr', u'express', u'absolut', u'humid', u'specif', u'humid', u'rel', u'rel', u'humid', u'frequent', u'encount', u'measur', u'humid', u'regularli', u'absolut', u'humid', u'specif', u'humid', u'rel', u'humid', u'rel', u'frequent', u'encount', u'measur', u'humid', u'regularli', u'use', 'weather', u'rel', u'humid', u'rel', u'humid', u'frequent', u'encount', u'measur', u'regularli', u'use', 'weather', u'forecast', u'import', 'part', 'weather', 'meteorologist', 'tunster', u'explain', u'differ', u'rel', u'discov', 'role', u'play', u'keep', 'cool', u'comfort', u'readi', 'sleep', 'summer', 'pore', u'normal', u'stinki', u'process', u'bodi', u'cool', 'high', u'turn', 'heat', u'sticki', 'start', 'feel', u'uncomfort', 'sweat', u'sticki', 'start', 'feel', u'uncomfort', 'sweat', u'nowher', 'higher', 'local', 'weather', 'radar', u'rainfal', u'advisori', u'temperatur', 'dewpoint', 'local', 'weather', 'radar', u'rainfal', u'advisori', u'temperatur', 'dewpoint', 'ground', 'water', 'past', 'data', u'file', u'pressur', 'soil', 'upper', 'wind', u'extrem', u'temperatur', u'heatwav', u'bring', 'problem', 'burden', 'water', 'vapor', u'mercuri', u'climb', u'extrem', 'data', u'subsequ', u'necessari', u'object', u'observ', 'relationship', u'temperatur', u'rel', u'humid', 'control', u'system', u'remov', 'water', 'vapor', 'indoor', u'necessari', u'object', u'observ', 'relationship', u'temperatur', u'rel', u'humid', 'control', u'system', u'remov', 'water', 'vapor', 'indoor', 'learn', 'comfort', u'prevent', 'mold', 'mildew', u'save', u'energi', 'cabin', u'dehydr', u'humid', 'aircraft', u'cabin', u'usual', u'less', u'humid', 'mold', 'mildew', u'save', u'energi', 'cabin', u'humid', u'dehydr', 'aircraft', u'cabin', u'usual', u'less', u'humid', 'home', u'normal', u'humid', u'dehydr', u'humid', 'aircraft', u'cabin', u'usual', u'less', 'home', u'normal', u'humid', u'caus', 'skin', u'dryness', 'discomfort', 'aircraft', u'cabin', u'usual', u'less', u'humid', 'home', u'normal', u'caus', 'skin', u'dryness', 'discomfort', u'eye', 'mouth', 'nose', 'skin', u'moistur', 'lotion', u'salin', 'nasal', 'spray', u'moistur', 'present', u'everi', 'home', u'build', 'amount', u'humid', u'benefici', u'moistur', u'humid', 'present', u'everi', 'home', u'build', 'amount', u'benefici', 'higher', 'lead', u'condens', 'mould', u'develop', u'increas', u'condens', u'like', 'collect', u'reduc', 'amount', u'effect', u'level', u'appropri', 'airway', u'optim', u'humid', u'essenti', u'humid', u'synonym', 'amount', u'effect', u'level', u'humid', u'appropri', 'airway', u'optim', u'essenti', u'humid', u'synonym', u'humid', 'thesaurus.com', 'free', u'onlin', u'level', u'humid', u'appropri', 'airway', u'optim', u'humid', u'essenti', u'synonym', u'humid', 'thesaurus.com', 'free', u'onlin', u'thesauru', u'antonym', u'appropri', 'airway', u'optim', u'humid', u'essenti', u'humid', u'synonym', 'thesaurus.com', 'free', u'onlin', u'thesauru', u'antonym', u'definit', u'dictionari', u'antonym', u'definit', u'dictionari', 'word', 'learn', u'import', 'control', 'among', u'factor', u'critic', 'care', u'area', 'like', u'hospit', u'success', u'decis', u'make', 'read', 'ptu300', u'combin', u'pressur', u'temperatur', u'transmitt', u'combin', u'pressur', u'humid', u'temperatur', u'transmitt', u'combin', u'pressur', u'humid', u'temperatur', u'transmitt', u'combin', u'pressur', u'temperatur', u'transmitt', 'ptu300', u'demand', 'ideal', u'daytim', u'humid', u'humid', u'temperatur', u'transmitt', 'ptu300', u'demand', 'ideal', u'daytim', u'orchid', 'summer', u'day', 'warm', u'humid', u'increas', u'place', 'ideal', u'daytim', u'humid', u'orchid', 'summer', u'day', 'warm', u'increas', u'place', u'plant', 'shallow', 'dish', 'tray', u'contain', u'pebbl', 'never', 'water', 'touch', 'bottom', u'capillari', u'rel', 'amount', u'moistur', u'percentag', 'amount', u'actual', 'hold', 'warmer', u'moistur', 'lower', 'warm', 'would', 'cool', 'seen', u'compar', u'humid', u'product', u'discontinu', 'found', 'support', u'literatur', u'seri', 'lower', 'warm', 'would', 'cool', 'seen', u'compar', u'humid', u'product', u'discontinu', 'found', 'support', u'literatur', u'seri', '2-wire', u'accuraci', u'option', 'display', u'transmitt', u'divis', 'love', 'mercoid', 'part', 'weather', u'forecast', 'long', 'gotten', u'news', u'begin', 'weatherperson', u'tell', u'condit', 'moment', 'current', u'temperatur', u'rel', 'past', u'coupl', u'decad', u'humid', u'rel', 'proper', u'humid', 'current', u'temperatur', u'rel', u'humid', 'past', u'coupl', u'decad', u'rel', 'proper', u'humid', u'level', 'keep', 'healthier', u'comfort', u'humid', 'past', u'coupl', u'decad', u'humid', u'rel', 'proper', u'level', 'keep', 'healthier', u'comfort', u'heat', u'ventil', u'condit', 'hvac', 'system', 'heat', 'cool', 'home', 'also', 'keep', u'comfort', 'level', 'winter', 'summer', u'delic', u'balanc', 'feel', u'delic', u'balanc', 'feel', u'choke', u'stifl', u'inescap', 'think', u'abhorr', u'go', 'much', u'wors', u'research', u'warn', u'becom', 'major', 'killer', 'within', u'year', u'measur', u'control', u'rel', u'humid', 'option', u'consist', 'special', u'humid', 'chamber', u'circul', 'killer', 'within', u'year', u'measur', u'control', u'rel', u'humid', 'option', u'consist', 'special', u'humid', 'chamber', u'circul', u'heat', u'control', u'rel', u'humid', u'humid', 'option', u'consist', 'special', 'chamber', u'circul', u'heat', 'bath', u'humid', u'gener', u'allow', u'consist', 'special', u'humid', 'chamber', u'circul', u'heat', 'bath', u'gener', u'allow', 'perform', u'measur', 'optimum', u'condit', u'everi', u'everi', u'deform', 'mode', 'special', u'readjust', u'necessari', u'instal', 'know', u'keep', u'humid', 'home', 'winter', u'import', 'skin', 'special', u'readjust', u'necessari', u'instal', u'humid', 'know', u'keep', 'home', 'winter', u'import', 'skin', 'throat', u'overal', 'health', u'overal', 'health', 'also', 'know', 'vital', 'health', 'home', u'level', u'furnitur', u'hous', u'deterior', 'certain', u'germ', 'thrive', u'simul', 'strong', 'landocean', 'contrast', u'respons', u'near-surfac', u'rel', 'global', u'warm', u'rel', u'humid', u'tend', u'increas', u'slightli', u'respons', u'near-surfac', u'rel', u'humid', 'global', u'warm', u'rel', u'tend', u'increas', u'slightli', u'ocean', u'decreas', u'substanti', 'land']
c={'partial': 1, 'global': 2, 'sleep': 1, 'skin': 6, 'dish': 1, u'follow': 2, u'middl': 1, u'depend': 4, u'decis': 1, u'stinki': 1, u'everi': 6, 'tunster': 1, u'capillari': 1, u'volum': 2, u'affect': 7, u'cool': 6, u'level': 11, u'stifl': 1, u'homeown': 2, 'upper': 1, 'pore': 1, 'past': 4, u'go': 1, 'rate': 2, u'pressur': 7, 'video': 2, u'precipit': 5, 'dewpoint': 2, u'compar': 4, 'brief': 1, 'current': 8, 'ground': 1, 'contrast': 1, 'full': 2, u'gener': 4, 'never': 1, 'water': 45, u'becom': 1, u'invis': 2, u'deterior': 1, 'amount': 31, 'healthier': 2, u'healthi': 1, u'extrem': 2, u'climb': 1, 'love': 1, u'gaseou': 1, u'instal': 2, u'total': 1, u'unit': 1, u'use': 3, u'eye': 1, 'would': 2, u'germ': 1, u'live': 5, 'radar': 2, u'type': 7, 'tell': 4, u'peopl': 2, 'meteorologist': 1, 'warm': 6, 'particular': 2, 'hold': 4, 'must': 2, 'high': 3, 'word': 1, u'hous': 1, 'local': 2, u'wors': 1, 'learn': 10, 'control': 6, u'climat': 8, u'process': 1, u'heatwav': 1, u'indic': 2, u'choke': 1, 'topic': 1, u'critic': 1, 'minimum': 2, u'onlin': 3, u'inescap': 1, 'winter': 7, 'thing': 3, 'comfort': 8, u'divis': 1, 'vital': 1, 'mould': 1, u'plant': 1, 'discomfort': 2, 'data': 2, u'antonym': 3, 'noun': 2, u'divid': 2, u'caus': 2, u'combin': 4, u'thesauru': 2, u'allow': 2, 'vapor': 23, 'wind': 1, u'deform': 1, u'report': 5, '/hjumdti/': 2, u'decad': 3, u'sentenc': 2, u'overal': 2, 'nation': 2, 'half': 2, u'day': 2, u'term': 6, 'oxygen': 3, 'edit': 5, 'drop': 2, 'mode': 1, 'found': 2, 'tray': 1, u'mean': 12, u'metr': 1, 'hard': 1, u'product': 2, u'year': 2, u'energi': 2, 'special': 6, u'variabl': 3, u'research': 1, 'health': 3, u'rel': 55, 'plural': 2, u'insid': 1, u'differ': 9, 'free': 3, u'dictionari': 2, 'airway': 4, 'likelihood': 2, 'care': 3, u'success': 1, u'keep': 6, u'turn': 3, u'place': 2, u'outsid': 4, 'think': 1, u'frequent': 5, 'major': 3, u'prevent': 1, u'feel': 5, u'qualiti': 5, u'number': 2, u'system': 3, u'etymolog': 1, u'prioriti': 2, u'mercuri': 1, 'given': 2, u'sometim': 2, 'fahrenheit': 1, u'twenti': 1, 'cabin': 6, u'option': 4, 'relationship': 2, u'especi': 7, 'shallow': 1, 'part': 2, u'pronunci': 1, u'essenti': 4, u'exactli': 3, 'kind': 1, 'gotten': 1, u'remov': 2, u'sultri': 1, 'matter': 2, u'balanc': 2, u'seri': 2, u'delic': 2, u'atmospher': 12, 'weatherperson': 1, u'say': 1, u'ventil': 1, 'seen': 2, u'dryness': 2, 'zero': 1, u'accuraci': 1, 'also': 2, 'ideal': 4, u'build': 2, u'dehydr': 3, u'simplifi': 3, u'begin': 1, 'though': 2, u'object': 2, 'nasal': 1, u'discov': 1, 'mouth': 1, u'synonym': 4, u'hospit': 1, u'inde': 2, 'swamp': 2, 'talk': 5, u'readjust': 2, u'satur': 3, u'fact': 3, u'humid': 144, 'indoor': 3, u'bring': 1, u'forecast': 3, 'find': 3, u'fifti': 3, u'absolut': 21, 'ratio': 4, u'explain': 4, 'behind': 1, 'rich': 3, 'factor': 2, u'discontinu': 2, 'equilibrium': 1, u'express': 6, u'regularli': 3, u'tailor': 4, u'increas': 5, u'uncomfort': 2, u'uncount': 2, '2-wire': 1, u'rainfal': 2, u'gram': 1, u'contain': 5, u'nowher': 1, u'pebbl': 1, u'transmitt': 6, u'respons': 2, 'optimum': 1, 'said': 1, u'tend': 2, 'state': 1, u'import': 7, 'thrive': 1, 'mildew': 2, 'lotion': 1, 'aircraft': 4, u'news': 1, u'come': 3, u'bodi': 3, 'spray': 1, 'among': 1, 'aspect': 1, u'arriv': 1, u'moistur': 10, 'strong': 1, 'hvac': 1, u'coupl': 3, u'damp': 8, 'three': 1, u'compon': 1, 'much': 1, u'presenc': 1, 'understand': 3, u'demand': 2, u'furnitur': 1, 'present': 2, u'subsequ': 1, u'defin': 2, u'circul': 4, u'observ': 2, u'readi': 1, 'soil': 1, 'need': 2, u'spong': 3, u'substanti': 1, u'abhorr': 1, 'mercoid': 1, u'develop': 1, 'perform': 1, u'make': 1, 'higher': 4, 'killer': 2, 'd.c.': 2, 'cubic': 1, u'optim': 4, u'effect': 4, 'rain': 2, 'moment': 1, 'lower': 2, u'appropri': 4, u'moder': 2, 'well': 1, u'ocean': 1, 'without': 1, 'english': 2, u'usual': 12, u'explan': 1, 'summer': 6, u'less': 6, u'humidti': 2, 'human': 2, 'touch': 1, u'concentr': 7, u'advisori': 2, u'moist': 5, u'littl': 1, 'treatment': 4, u'wet': 2, u'save': 2, 'thesaurus.com': 3, u'complaint': 2, u'read': 3, u'temperatur': 22, 'know': 7, 'burden': 1, 'vapour': 17, u'measur': 10, u'like': 2, u'specif': 4, 'chamber': 4, u'necessari': 4, 'nose': 1, u'manag': 1, 'ptu300': 3, u'encount': 4, u'salin': 1, u'play': 1, u'percentag': 5, 'warmer': 1, u'flush': 2, 'proper': 6, 'home': 15, u'constitut': 3, u'orchid': 2, 'lead': 1, 'collect': 1, u'condens': 2, u'definit': 11, 'throat': 1, u'condit': 8, u'evapor': 1, u'refer': 2, u'actual': 3, u'slightli': 2, u'literatur': 2, u'simul': 1, u'degre': 7, u'sweat': 3, u'near-surfac': 2, u'primarili': 1, 'within': 2, 'washington': 1, 'bath': 2, 'weather': 17, 'lesson': 1, u'area': 1, 'support': 2, 'landocean': 1, 'long': 1, 'start': 2, u'function': 2, u'daytim': 3, 't-shirt': 1, u'cloth': 2, 'heat': 14, 'hear': 4, 'cbse': 1, 'highest': 3, u'consist': 4, u'possibl': 5, 'maximum': 3, 'problem': 1, 'display': 1, 'hotter': 1, u'ad': 1, u'creat': 2, 'certain': 2, u'decreas': 1, u'file': 1, 'mold': 2, u'sticki': 3, 'percent': 7, 'role': 1, u'normal': 4, 'clean': 2, u'benefici': 2, 'peak': 2, u'reduc': 5, u'warn': 1, 'land': 1, u'scientif': 1, 'bottom': 1, u'descript': 3, 'time': 1, 'fresh': 5, u'daili': 3}

for item in c.keys():
    k=c[item]
    p=len(dpw)
    v=len(c.keys())*1.0
    s=0
    for i in range(1,k+1):
        r=scipy.misc.comb(p,i)
        for index in range(p-i):
            r=r*((v-1)/v)
        for j in range(i):
            r=r/v
        s+=r
        # s+=itertools.combinations(p,i)*math.pow(v-1,p-i)

    print item,1-s