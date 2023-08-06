from collections import namedtuple

MatchType = namedtuple("MatchType", ["open", "close"])
brace = MatchType("{", "}")
bracket = MatchType("[", "]")
parentheses = MatchType("(", ")")
gt_lt = MatchType("<", ">")