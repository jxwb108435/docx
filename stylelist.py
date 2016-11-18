"""
style

0 Normal
1 Heading 1
2 Heading 2
3 Heading 3
4 Heading 4
5 Heading 5
6 Heading 6
7 Heading 7
8 Heading 8
9 Heading 9
10 Default Paragraph Font
11 Normal Table
12 No List
13 No Spacing
14 Heading 1 Char
15 Heading 2 Char
16 Heading 3 Char
17 Title
18 Title Char
19 Subtitle
20 Subtitle Char
21 List Paragraph
22 Body Text
23 Body Text Char
24 Body Text 2
25 Body Text 2 Char
26 Body Text 3
27 Body Text 3 Char
28 List
29 List 2
30 List 3
31 List Bullet
32 List Bullet 2
33 List Bullet 3
34 List Number
35 List Number 2
36 List Number 3
37 List Continue
38 List Continue 2
39 List Continue 3
40 macro
41 Macro Text Char
42 Quote
43 Quote Char
44 Heading 4 Char
45 Heading 5 Char
46 Heading 6 Char
47 Heading 7 Char
48 Heading 8 Char
49 Heading 9 Char
50 Caption
51 Strong
52 Emphasis
53 Intense Quote
54 Intense Quote Char
55 Subtle Emphasis
56 Intense Emphasis
57 Subtle Reference
58 Intense Reference
59 Book Title
60 TOC Heading
61 Table Grid
62 Light Shading
63 Light Shading Accent 1
64 Light Shading Accent 2
65 Light Shading Accent 3
66 Light Shading Accent 4
67 Light Shading Accent 5
68 Light Shading Accent 6
69 Light List
70 Light List Accent 1
71 Light List Accent 2
72 Light List Accent 3
73 Light List Accent 4
74 Light List Accent 5
75 Light List Accent 6
76 Light Grid
77 Light Grid Accent 1
78 Light Grid Accent 2
79 Light Grid Accent 3
80 Light Grid Accent 4
81 Light Grid Accent 5
82 Light Grid Accent 6
83 Medium Shading 1
84 Medium Shading 1 Accent 1
85 Medium Shading 1 Accent 2
86 Medium Shading 1 Accent 3
87 Medium Shading 1 Accent 4
88 Medium Shading 1 Accent 5
89 Medium Shading 1 Accent 6
90 Medium Shading 2
91 Medium Shading 2 Accent 1
92 Medium Shading 2 Accent 2
93 Medium Shading 2 Accent 3
94 Medium Shading 2 Accent 4
95 Medium Shading 2 Accent 5
96 Medium Shading 2 Accent 6
97 Medium List 1
98 Medium List 1 Accent 1
99 Medium List 1 Accent 2
100 Medium List 1 Accent 3
101 Medium List 1 Accent 4
102 Medium List 1 Accent 5
103 Medium List 1 Accent 6
104 Medium List 2
105 Medium List 2 Accent 1
106 Medium List 2 Accent 2
107 Medium List 2 Accent 3
108 Medium List 2 Accent 4
109 Medium List 2 Accent 5
110 Medium List 2 Accent 6
111 Medium Grid 1
112 Medium Grid 1 Accent 1
113 Medium Grid 1 Accent 2
114 Medium Grid 1 Accent 3
115 Medium Grid 1 Accent 4
116 Medium Grid 1 Accent 5
117 Medium Grid 1 Accent 6
118 Medium Grid 2
119 Medium Grid 2 Accent 1
120 Medium Grid 2 Accent 2
121 Medium Grid 2 Accent 3
122 Medium Grid 2 Accent 4
123 Medium Grid 2 Accent 5
124 Medium Grid 2 Accent 6
125 Medium Grid 3
126 Medium Grid 3 Accent 1
127 Medium Grid 3 Accent 2
128 Medium Grid 3 Accent 3
129 Medium Grid 3 Accent 4
130 Medium Grid 3 Accent 5
131 Medium Grid 3 Accent 6
132 Dark List
133 Dark List Accent 1
134 Dark List Accent 2
135 Dark List Accent 3
136 Dark List Accent 4
137 Dark List Accent 5
138 Dark List Accent 6
139 Colorful Shading
140 Colorful Shading Accent 1
141 Colorful Shading Accent 2
142 Colorful Shading Accent 3
143 Colorful Shading Accent 4
144 Colorful Shading Accent 5
145 Colorful Shading Accent 6
146 Colorful List
147 Colorful List Accent 1
148 Colorful List Accent 2
149 Colorful List Accent 3
150 Colorful List Accent 4
151 Colorful List Accent 5
152 Colorful List Accent 6
153 Colorful Grid
154 Colorful Grid Accent 1
155 Colorful Grid Accent 2
156 Colorful Grid Accent 3
157 Colorful Grid Accent 4
158 Colorful Grid Accent 5
159 Colorful Grid Accent 6
"""
from docx import Document


doc = Document()

# list all styles
all_styles = [s for s in doc.styles]
_id = 0
for style in all_styles:
    print(_id, style.name)
    _id += 1
