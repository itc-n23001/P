import os #osをインポート
import shutil

for a,b,c in os.walk("test"):
    for f in c: 
      if f.endswith((".jpg",".pdf")): 
            print(os.path.join(a,f)) 