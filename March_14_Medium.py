{\rtf1\ansi\ansicpg1252\cocoartf2821
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue255;\red255\green255\blue255;\red0\green0\blue0;
\red32\green108\blue135;\red101\green76\blue29;\red0\green0\blue109;\red19\green118\blue70;\red157\green0\blue210;
}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c100000;\cssrgb\c100000\c100000\c100000;\cssrgb\c0\c0\c0;
\cssrgb\c14902\c49804\c60000;\cssrgb\c47451\c36863\c14902;\cssrgb\c0\c6275\c50196;\cssrgb\c3529\c52549\c34510;\cssrgb\c68627\c0\c85882;
}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs26 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 class\cf0 \strokec4  \cf5 \strokec5 Solution\cf0 \strokec4 :\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf2 \strokec2 def\cf0 \strokec4  \cf6 \strokec6 maximumCandies\cf0 \strokec4 (\cf7 \strokec7 self\cf0 \strokec4 , \cf7 \strokec7 candies\cf0 \strokec4 : List[\cf5 \strokec5 int\cf0 \strokec4 ], \cf7 \strokec7 k\cf0 \strokec4 : \cf5 \strokec5 int\cf0 \strokec4 ) -> \cf5 \strokec5 int\cf0 \strokec4 :\cb1 \
\cb3         left, right = \cf8 \strokec8 1\cf0 \strokec4 , \cf6 \strokec6 min\cf0 \strokec4 (\cf6 \strokec6 max\cf0 \strokec4 (candies),\cf6 \strokec6 sum\cf0 \strokec4 (candies) // k)\cb1 \
\cb3         \cb1 \
\cb3         \cf9 \strokec9 while\cf0 \strokec4  left<=right:\cb1 \
\cb3             mid = left + (right - left) \cb1 \
\cb3             total_k = \cf8 \strokec8 0\cf0 \cb1 \strokec4 \
\cb3             \cb1 \
\cb3             \cf9 \strokec9 for\cf0 \strokec4  i \cf9 \strokec9 in\cf0 \strokec4  candies:\cb1 \
\cb3                 total_k += i // mid\cb1 \
\cb3             \cb1 \
\cb3             \cf9 \strokec9 if\cf0 \strokec4  total_k >= k:\cb1 \
\cb3                 left = mid + \cf8 \strokec8 1\cf0 \cb1 \strokec4 \
\
\cb3             \cf9 \strokec9 else\cf0 \strokec4 :\cb1 \
\cb3                 right = mid - \cf8 \strokec8 1\cf0 \cb1 \strokec4 \
\cb3         \cf9 \strokec9 return\cf0 \strokec4  right\cb1 \
}