import PyPDF2 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer 
  
lemmatizer = WordNetLemmatizer() 
filename = 'A.pdf'

pdfFileObj = open(filename,'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

num_pages = pdfReader.numPages
count = 0
text = ""

while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()

if text != "":
   text = text

stopWords=set(stopwords.words('english'))
tokens = word_tokenize(text)
ps=PorterStemmer()
punctuations = ['(',')',';',':','[',']',',','.']

keywords = [word for word in tokens if not word in punctuations and not word in stopWords]
final=[]
for w in keywords:
	final.append(lemmatizer.lemmatize(w.lower()))
print(final)
