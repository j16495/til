# %%
from IPython.display import HTML
from natto import MeCab

nm = MeCab()
a = ""
text = "こんにちは！野球は走る、打つ、投げるスポーツです。"
print(text)

with MeCab('-F%m,%f[0],%h,%f[8]') as nm:
    for n in nm.parse(text, as_nodes=True):
        lis = n.feature.split(",")
        try: 
            if lis[1] == "動詞":
                b = ("<span style='background-color:#ffcc99'>{0}</span>".format(lis[0]))
            else:
                b = ("<span style='background-color:#ffffff'>{0}</span>".format(lis[0]))
            a = a + b    
        except IndexError:
            pass

display(HTML(a))
            

        