import streamlit as st
#import numpy  as np
#import pandas as pd
#from   PIL import Image
import time

st.title('Streamlit超入門')

st.write('プログレスバーの表示')
'Start!!!'

#プログレスバーの表示
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.01)

'Done!!!!'

# df = pd.DataFrame(
#     np.random.rand(100,2)/[50, 50] + [35.69, 139.70],
#     columns=['lat','lon']
#     )


#st.write(df)

left_column, right_column = st.columns(2)
button = False
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

expander = st.expander('問い合わせ')
for _ in range(5):
    expander.write('問い合わせ内容を書く')


#st.dataframe(df)

#st.dataframeメソッドだと引数が指定できる。
#st.dataframe(df, width=100, height=100)

#列中で最も大きい値を持つ行をハイライトする
#st.dataframe(df.style.highlight_max(axis=0))

#静的なテーブルを作成する場合はtableを使用する
#st.table(df.style.highlight_max(axis=0))

#折れ線グラフ
#st.line_chart(df)

#折れ線グラフ
#st.area_chart(df)

#棒グラフ
#st.bar_chart(df)

#地図データをマッピング
#st.map(df)

#チェックボックスにチェックが入っていたら画像を表示
# if st.checkbox('Show Image'):

#     #画像表示
#     img = Image.open(r"D:\spreadsheets.jpg")
#     st.image(img, caption='Test',use_column_width=True)

#チェックボックスにチェックが入っていたら画像を表示
# option = st.selectbox(
#     'あなたが好きな数字を教えてください。', 
#     [_ for _ in range(1,11,1)]
# )
# 'あなたの好きな数字は、',option,'です。'

# #テキスト入力した内容を憑依
option = st.text_input(
    'あなたの趣味を教えてください。'
)
'あなたの趣味は、',option,'です。'

#スライダー
condition = st.slider('あなたの今の調子は？',0,100,50)
'あなたのコンディションは、',condition,'です。'