{\rtf1\ansi\ansicpg1252\cocoartf2821
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue255;\red255\green255\blue255;\red0\green0\blue0;
\red32\green108\blue135;\red101\green76\blue29;\red0\green0\blue109;\red19\green118\blue70;\red157\green0\blue210;
\red15\green112\blue1;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c100000;\cssrgb\c100000\c100000\c100000;\cssrgb\c0\c0\c0;
\cssrgb\c14902\c49804\c60000;\cssrgb\c47451\c36863\c14902;\cssrgb\c0\c6275\c50196;\cssrgb\c3529\c52549\c34510;\cssrgb\c68627\c0\c85882;
\cssrgb\c0\c50196\c0;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs26 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 class\cf0 \strokec4  \cf5 \strokec5 Solution\cf0 \strokec4 :\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf2 \strokec2 def\cf0 \strokec4  \cf6 \strokec6 minZeroArray\cf0 \strokec4 (\cf7 \strokec7 self\cf0 \strokec4 , \cf7 \strokec7 nums\cf0 \strokec4 : List[\cf5 \strokec5 int\cf0 \strokec4 ], \cf7 \strokec7 queries\cf0 \strokec4 : List[List[\cf5 \strokec5 int\cf0 \strokec4 ]]) -> \cf5 \strokec5 int\cf0 \strokec4 :\cb1 \
\cb3         n = \cf6 \strokec6 len\cf0 \strokec4 (nums)\cb1 \
\cb3         \cf2 \strokec2 def\cf0 \strokec4  \cf6 \strokec6 checkzeroarray\cf0 \strokec4 (\cf7 \strokec7 k\cf0 \strokec4 ):\cb1 \
\
\cb3             diffarray = [\cf8 \strokec8 0\cf0 \strokec4 ]* (n+\cf8 \strokec8 1\cf0 \strokec4 )\cb1 \
\
\cb3             \cf9 \strokec9 for\cf0 \strokec4  i \cf9 \strokec9 in\cf0 \strokec4  \cf6 \strokec6 range\cf0 \strokec4 (k):\cb1 \
\cb3                 left, right, val = queries[i]\cb1 \
\cb3                 diffarray[left]+= val\cb1 \
\cb3                 diffarray[right+\cf8 \strokec8 1\cf0 \strokec4 ] -= val\cb1 \
\cb3             curr_sum =\cf8 \strokec8 0\cf0 \cb1 \strokec4 \
\cb3             \cf9 \strokec9 for\cf0 \strokec4  i \cf9 \strokec9 in\cf0 \strokec4  \cf6 \strokec6 range\cf0 \strokec4 (n):\cb1 \
\cb3                 curr_sum += diffarray[i]\cb1 \
\cb3                 \cf9 \strokec9 if\cf0 \strokec4  curr_sum < nums[i]:\cb1 \
\cb3                     \cf9 \strokec9 return\cf0 \strokec4  \cf2 \strokec2 False\cf0 \cb1 \strokec4 \
\cb3             \cf9 \strokec9 return\cf0 \strokec4  \cf2 \strokec2 True\cf0 \cb1 \strokec4 \
\
\cb3         \cf9 \strokec9 if\cf0 \strokec4  \cf6 \strokec6 all\cf0 \strokec4 (x == \cf8 \strokec8 0\cf0 \strokec4  \cf9 \strokec9 for\cf0 \strokec4  x \cf9 \strokec9 in\cf0 \strokec4  nums):\cb1 \
\cb3                 \cf9 \strokec9 return\cf0 \strokec4  \cf8 \strokec8 0\cf0 \cb1 \strokec4 \
\cb3             \cb1 \
\cb3     \cf10 \strokec10 #binary search\cf0 \cb1 \strokec4 \
\cb3         l,r = \cf8 \strokec8 1\cf0 \strokec4 , \cf6 \strokec6 len\cf0 \strokec4 (queries)\cb1 \
\cb3         \cf9 \strokec9 if\cf0 \strokec4  \cf2 \strokec2 not\cf0 \strokec4  checkzeroarray(r):\cb1 \
\cb3             \cf9 \strokec9 return\cf0 \strokec4  -\cf8 \strokec8 1\cf0 \cb1 \strokec4 \
\cb3         \cb1 \
\cb3         \cf9 \strokec9 while\cf0 \strokec4  l<r:\cb1 \
\cb3             mid =l+ (r -l)//\cf8 \strokec8 2\cf0 \cb1 \strokec4 \
\
\cb3             \cf9 \strokec9 if\cf0 \strokec4 (checkzeroarray(mid)):\cb1 \
\cb3                 r = mid\cb1 \
\cb3             \cf9 \strokec9 else\cf0 \strokec4 :\cb1 \
\cb3                 l = mid + \cf8 \strokec8 1\cf0 \cb1 \strokec4 \
\cb3         \cf9 \strokec9 return\cf0 \strokec4  l\cb1 \
\
}