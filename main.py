#!/usr/bin/env python
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_assets import Environment, Bundle

import torch
import transformers
from transformers import AutoTokenizer,TextClassificationPipeline,RobertaForSequenceClassification

import underthesea,re

app = Flask(__name__)

#Load model
tokenizer = AutoTokenizer.from_pretrained('vinai/phobert-base', use_fast=False)

modelp = RobertaForSequenceClassification.from_pretrained('nqcccccc/phobert-vlsp-absa-qab')
pipe = TextClassificationPipeline(model=modelp, tokenizer=tokenizer)

assets = Environment(app)
assets.url = app.static_url_path
assets.debug = True

scss = Bundle('scss/main.scss', filters='pyscss', output='gen/all.css')
assets.register('scss_all', scss)

aux_sen = {'drinks#quality-neutral': 'cảm_xúc về chất_lượng của thức_uống là trung_tính',
 'drinks#quality-positive': 'cảm_xúc về chất_lượng của thức_uống là tích_cực',
 'drinks#quality-negative': 'cảm_xúc về chất_lượng của thức_uống là tiêu_cực',
 'drinks#style&options-neutral': 'cảm_xúc về phong_cách và sự lựa_chọn của thức_uống là trung_tính',
 'drinks#style&options-positive': 'cảm_xúc về phong_cách và sự lựa_chọn của thức_uống là tích_cực',
 'drinks#style&options-negative': 'cảm_xúc về phong_cách và sự lựa_chọn của thức_uống là tiêu_cực',
 'food#style&options-neutral': 'cảm_xúc về phong_cách và sự lựa_chọn của thức_ăn là trung_tính',
 'food#style&options-positive': 'cảm_xúc về phong_cách và sự lựa_chọn của thức_ăn là tích_cực',
 'food#style&options-negative': 'cảm_xúc về phong_cách và sự lựa_chọn của thức_ăn là tiêu_cực',
 'restaurant#prices-neutral': 'cảm_xúc về giá_cả của nhà_hàng là trung_tính',
 'restaurant#prices-positive': 'cảm_xúc về giá_cả của nhà_hàng là tích_cực',
 'restaurant#prices-negative': 'cảm_xúc về giá_cả của nhà_hàng là tiêu_cực',
 'food#prices-neutral': 'cảm_xúc về giá_cả của thức_ăn là trung_tính',
 'food#prices-positive': 'cảm_xúc về giá_cả của thức_ăn là tích_cực',
 'food#prices-negative': 'cảm_xúc về giá_cả của thức_ăn là tiêu_cực',
 'food#quality-neutral': 'cảm_xúc về chất_lượng của thức_ăn là trung_tính',
 'food#quality-positive': 'cảm_xúc về chất_lượng của thức_ăn là tích_cực',
 'food#quality-negative': 'cảm_xúc về chất_lượng của thức_ăn là tiêu_cực',
 'service#general-neutral': 'cảm_xúc về tổng_quan của dịch_vụ là trung_tính',
 'service#general-positive': 'cảm_xúc về tổng_quan của dịch_vụ là tích_cực',
 'service#general-negative': 'cảm_xúc về tổng_quan của dịch_vụ là tiêu_cực',
 'restaurant#general-neutral': 'cảm_xúc về tổng_quan của nhà_hàng là trung_tính',
 'restaurant#general-positive': 'cảm_xúc về tổng_quan của nhà_hàng là tích_cực',
 'restaurant#general-negative': 'cảm_xúc về tổng_quan của nhà_hàng là tiêu_cực',
 'restaurant#miscellaneous-neutral': 'cảm_xúc về những thứ khác của nhà_hàng là trung_tính',
 'restaurant#miscellaneous-positive': 'cảm_xúc về những thứ khác của nhà_hàng là tích_cực',
 'restaurant#miscellaneous-negative': 'cảm_xúc về những thứ khác của nhà_hàng là tiêu_cực',
 'location#general-neutral': 'cảm_xúc về tổng_quan của địa_điểm là trung_tính',
 'location#general-positive': 'cảm_xúc về tổng_quan của địa_điểm là tích_cực',
 'location#general-negative': 'cảm_xúc về tổng_quan của địa_điểm là tiêu_cực',
 'drinks#prices-neutral': 'cảm_xúc về giá_cả của thức_uống là trung_tính',
 'drinks#prices-positive': 'cảm_xúc về giá_cả của thức_uống là tích_cực',
 'drinks#prices-negative': 'cảm_xúc về giá_cả của thức_uống là tiêu_cực',
 'ambience#general-neutral': 'cảm_xúc về tổng_quan của không_gian là trung_tính',
 'ambience#general-positive': 'cảm_xúc về tổng_quan của không_gian là tích_cực',
 'ambience#general-negative': 'cảm_xúc về tổng_quan của không_gian là tiêu_cực'}


@app.route('/', methods=['GET'])
def index():
    return render_template('main.html')

@app.route('/result' , methods=['POST'])
def result():
    rf = request.form
    print('start')
    print(rf)
    for key in rf.keys():
        data = key
    print(data)
    data_dict = json.loads(data)
    return 'nothing'

def predict_qab(input,aux_sen,pipe):
    emoji_pattern = re.compile('['
          u'\U0001F600-\U0001F64F'  # emoticons
          u'\U0001F300-\U0001F5FF'  # symbols & pictographs
          u'\U0001F680-\U0001F6FF'  # transport & map symbols
          u'\U0001F1E0-\U0001F1FF'  # flags (iOS)
          u'\U00002500-\U00002BEF'  # chinese char
          u'\U00002702-\U000027B0'
          u'\U000024C2-\U0001F251'
          u'\U0001f926-\U0001f937'
          u'\U00010000-\U0010ffff'
          u'\u2640-\u2642' 
          u'\u2600-\u2B55'
          u'\u200d'
          u'\u23cf'
          u'\u23e9'
          u'\u231a'
          u'\ufe0f'  # dingbats
          u'\u3030'
                        ']+', re.UNICODE)

    text = re.sub(r'(?<=\d)((\s+k)|k)', '.000',input)
    text = re.sub(r'((09|03|07|08|05)+([0-9]+)\b)',' ',text)
    text = re.sub(r'#\w+h*',' ',text)
    text = re.sub(r'([a-z])\1*', r'\1', text)
    text = emoji_pattern.sub('',text)
    text = re.sub(r'(?<!\d)[!?#%^&*()_+=\-\'";:/><,}{\[\]|/](?!\d)',' ',text)
    text = re.sub(' +', ' ', text)
    text = underthesea.word_tokenize(text, format='text')

    result = []
    tmp_label = []

    

    for i in (aux_sen.keys()):
        tmp_result = pipe('<s>'+text+'</s>'+aux_sen[i]+'</s>')
        if(tmp_result[0]['label'] == 'LABEL_1'):
          tmp_label.append(1)
        else:
          tmp_label.append(0)


    all_label = list(aux_sen.keys())

    for i in range(0,len(tmp_label)):
        if(tmp_label[i] == 1):
            result.append(all_label[i])
    
    return result

if __name__=='__main__':
    app.run(debug=True)