# 2024-11-26 18:00 втр Нвг Win10
# https://www.youtube.com/watch?v=o8p7uQCGD0U&t=243s

# 2024-11-27 20:20 срд Нвг вар _1

import streamlit as st
from datetime import datetime
import numpy as np
import pandas as pd
import os
import xlsxwriter
import openpyxl

#-----------------
st.title("Тест страница изучения Streamlit", anchor="Apress")
st.subheader("2024-11-27 20:00. Smolenishev Oleg")

st.write('[otter-finance.ru](https://otter-finance.ru)')




st.sidebar.markdown('''
# Оглавление
- [Продажи и маржа](#section-1)
- [Section 2](#section-2)
''', unsafe_allow_html=True)

st.markdown("[Продажи м маржа](#Продажи-1)")

st.header('Section 1')
st.write('''
consectetur.
''')


st.header('Section 2')
st.write('''
consectetur.
''')




now = datetime.now()

st.markdown("[Заголовок](#section-3)")

st.markdown("[Заголовок2](#section-4)")

now_2 = now.strftime("%Y-%m-%d %H:%M")

st.write(now)
st.write(now_2)

st.divider()
st.subheader("Таблицы")

df = pd.DataFrame({
    'Наименование': ["Первый", "Второй"],
    'Значение': [10, 20]
})

st.table(df)

df2 = st.data_editor(df)

#st.table(df2)

st.metric(label="Количество строк таблицы: ", value=len(df))
st.metric(label="Сумма по столбцу Значение: ", value=df['Значение'].sum())

st.divider()

st.subheader("Графики")

df3 = pd.DataFrame(
    np.random.rand(10, 4),
    columns=['A', 'B', 'C', 'D']
)

st.table(df3)
st.area_chart(df3)
st.line_chart(df3)
st.scatter_chart(df3[['A', 'B']])

st.divider()
st.subheader("Изображение")
st.image(os.path.join(os.getcwd(), "static", "otter.jpg"), width=100)

st.divider()

# -----------------------
st.subheader("Чтение xlsx файла и построние отчета по продажам. Источник данных: база ДЕМО")

st.write("2024-11-29 10:00 Нвг")

# pd.set_option('display.float_format', '{:.1f}'.format)

# df = pd.read_excel('C:\\Users\\smole\\OneDrive\Documents\\02_Streamlit\Tutorial\\base1.xlsx', sheet_name='base')

# df.rename(columns={'Дата': 'DATA', 'Счет Дт': 'SD', 'Субконто1 Дт': 'SKD1', 'Субконто2 Дт': 'SKD2', 'Субконто3 Дт': 'SKD3', 'Счет Кт': 'SK', 
#         'Субконто1 Кт': 'SKK1', 'Субконто2 Кт': 'SKK2', 'Субконто3 Кт': 'SKK3', 'Сумма': 'SUMMA'}, inplace=True)

# df = df[(df['SK']=='90.01.1') | (df['SD']=='90.02.1')]

# df['ST'] = (df['SUMMA']/1000).round(2)
# df['DATA'] = pd.to_datetime(df['DATA'], dayfirst=True)
# df['Год']=pd.DatetimeIndex(df['DATA']).year.astype('object')
# df['Месяц'] = pd.DatetimeIndex(df['DATA']).month.astype('object')
# df['День'] = pd.DatetimeIndex(df['DATA']).day.astype('object')
# df['Квартал'] = pd.DatetimeIndex(df['DATA']).quarter.astype('object')
# df['YM'] = df['DATA'].dt.to_period('M')

# df = df[df['Год']>=2021]

# df['Статья'] = ''
# df.loc[df['SK']=='90.01.1', 'Статья'] = 'Продажи'
# df.loc[df['SD']=='90.02.1', 'Статья'] = 'Себестоимость'

# df['Номенклатура'] = ''
# df.loc[df['SK']=='90.01.1', 'Номенклатура'] = df['SKK3']
# df.loc[((df['SD']=='90.02.1') & (df['SK']=='41.01')), 'Номенклатура'] = df['SKK1']
# df.loc[((df['SD']=='90.02.1') & (df['SK']=='45.01')), 'Номенклатура'] = df['SKK2']

# df['ДС'] = 0
# df.loc[df['SK']=='90.01.1', 'ДС'] = df['ST'] /1.2
# df.loc[df['SD']=='90.02.1', 'ДС'] = df['ST']*-1

# df['Продажи'] = 0
# df.loc[df['SK']=='90.01.1', 'Продажи'] = df['ST'] /1.2

# df['Себестоимость'] = 0
# df.loc[df['SD']=='90.02.1', 'Себестоимость'] = df['ST']*-1

# pt00 = pd.pivot_table(df, index=['Статья'], values=['ДС'], columns=['Год'], aggfunc='sum', fill_value='', margins=False).round(2)

# pt00 = pt00['ДС']

# pt00 = pt00.transpose()

# pt00['Марж.прибыль'] = pt00['Продажи'] + pt00['Себестоимость']

# # pt00 = pt00[pt00["Статья"]=="Продажи"]

# st.write("Таблица продаж, себестоимости и марж.прибыли (тыс.руб.)")
# st.table(pt00)

# st.write("График продаж, себестоимости и марж.прибыли (тыс.руб.)")
# st.markdown("***График продаж, себестоимости и марж.прибыли (тыс.руб.)***")

# st.bar_chart(pt00, stack=False, width=200, height=500)
# # st.area_chart(pt00)
# # st.line_chart(pt00)

st.divider()
st.subheader("Слайдер")

x = st.slider("Установить значение ", 1, 10)
st.write("Установлено значение: ", x)


st.divider()
st.subheader("Разделение на столбцы")

col1, col2 = st.columns(2)

with col1:
    st.write("Столбец 1")

with col2:
    st.write("Столбец 2")



st.header('Продажи')

st.write('''
что-то
''')


st.subheader("Section 3")


st.subheader("Section 4")