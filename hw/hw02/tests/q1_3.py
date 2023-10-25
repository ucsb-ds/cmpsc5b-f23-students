OK_FORMAT = True

test = {   'name': 'q1_3',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> 40 <= meunfan_lower_bound <= meunfan_upper_bound <= 60\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> all([meunfan_lower_bound == percentile(2.5, resampled_percentages), meunfan_upper_bound == percentile(97.5, resampled_percentages)])\nTrue',
                                       'hidden': True,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
