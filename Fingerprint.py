from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import hashlib
from difflib import SequenceMatcher


def longestSubstring(str1, str2):
    # initialize SequenceMatcher object with
    # input string
    seqMatch = SequenceMatcher(None, str1, str2)

    # find match of longest sub-string
    # output will be like Match(a=0, b=0, size=5)
    match = seqMatch.find_longest_match(0, len(str1), 0, len(str2))
    ans=""
    ans=str1[match.a: match.a + match.size]
    #print(ans)
    return ans

lemmatizer = WordNetLemmatizer()
text=""
with open('g0pA_taska.txt','r',encoding="utf8") as f:
    for line in f:
        for word in line.split():
           text=text+" "+word

text1=""
with open('g0pA_taskb.txt','r',encoding="utf8") as f:
    for line in f:
        for word in line.split():
           text1=text1+" "+word

stopWords=set(stopwords.words('english'))
tokens = word_tokenize(text)
tokens1 = word_tokenize(text1)
ps=PorterStemmer()
punctuations = ['(',')',';',':','[',']',',','.','”',',','-','“','‘','’']

keywords = [word for word in tokens if not word in punctuations and not word in stopWords]
keywords1 = [word for word in tokens1 if not word in punctuations and not word in stopWords]
str=""
str1=""
for w in keywords:
	str+=(lemmatizer.lemmatize(w.lower()))

for w in keywords1:
	str1+=(lemmatizer.lemmatize(w.lower()))

result = hashlib.md5(str.encode())
b=result.hexdigest()

result1 = hashlib.md5(str1.encode())
b1=result1.hexdigest()
print(b+"\n"+b1)
res=""
res = longestSubstring(b,b1)

print(res)
res1=b+b1

ans=len(res)/len(res1)
print(ans)