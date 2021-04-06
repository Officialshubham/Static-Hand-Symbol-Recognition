from fastai import *
from fastai.vision import *
from fastai.metrics import error_rate
from fastai.vision import load_learner
import pathlib



def load_model():
    path = pathlib.Path.cwd()
    learn = load_learner(path, 'export.pkl')
    return learn

def pred_ch(img_path):
    pred_class,_,_=l.predict(open_image(img_path))
    #print(f'Predicted Character:{pred_class}')
    if str(pred_class)=='space' or str(pred_class)=='nothing':
            print(" ")
    else:
        print(str(pred_class))
    
if __name__=="__main__":
    l=load_model()
    
    pred_ch('A.jpg')
    
