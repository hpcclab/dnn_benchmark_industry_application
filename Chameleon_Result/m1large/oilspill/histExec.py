import matplotlib.pyplot as plt
 
x = [22.130889177322388,
22.417392253875732,
22.22549319267273,
21.892558336257935,
28.89919114112854,
28.98982548713684,
29.105448961257935,
23.279357194900513,
26.47338557243347,
25.27138900756836,
23.084238529205322,
27.52405095100403,
26.776782512664795,
25.625970363616943,
23.282896041870117,
26.544692754745483,
26.443381547927856,
22.887561559677124,
22.35875391960144,
22.242623567581177,
22.678915977478027,
22.380940198898315,
22.398021697998047,
22.362915754318237,
22.02607560157776,
22.70144772529602,
22.76207685470581,
22.499225616455078,
22.80807399749756,
22.746512413024902
]

plt.hist(x, bins=10)
plt.savefig("pysitHistogramExecML.pdf")
#plt.show()
