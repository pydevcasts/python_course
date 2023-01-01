import pandas as pd
import numpy as np

# data = np.array(['g','r','t','y'])
# ser = pd.Series(data)
# ================================
# ser = pd.Series([1., 2., 3.], index=['a', 'b', 'c'])
# print(ser)
# my_series=pd.Series([1., 2., 3.], index=['a', 'b', 'c'])
# print(my_series.values)
# print(my_series.index)
# ======================================
# data = {'a' : 0., 'b' : 1., 'c' : 2.}
# s = pd.Series(data)
# print (s)
# ============================================
# data = {'a' : 0., 'b' : 1., 'c' : 2.}
# s = pd.Series(data,index=['b','c','d','a'])
# print (s)
# ========================================
# creating simple array
# data = np.array(['g','e','e','k','s','f', 'o','r','g','e','e','k','s'])
# ser = pd.Series(data)
# #retrieve the first element
# print(ser[:5])
# ========================================
# # creating simple array
# data = np.array(['g','e','e','k','s','f', 'o','r','g','e','e','k','s'])
# ser = pd.Series(data,index=[10,11,12,13,14,15,16,17,18,19,20,21,22])
# # accessing a element using index element
# print(ser[16])
# ===================================
# df = pd.read_csv("nba.csv")  
# ser = pd.Series(df['Name']) 
# data = ser.head(10)
# # print(data)
# print(data[2:4])
# print(data.loc[2:4])
# print(data.iloc[2:4])
# ================================
# data = pd.Series([5, 2, 3,7], index=['a', 'b', 'c', 'd'])
# print(data)
# # creating a series
# data1 = pd.Series([1, 6, 4, 9], index=['a', 'b', 'd', 'e'])
# print(data1)
# print(data.add(data1, fill_value=0))
# ============================================
# lst = ['this', 'is', 'a', 'practial', 
# 			'article', 'for', 'Pandas'] 
# # Calling DataFrame constructor on list 
# df = pd.DataFrame(lst) 
# print(df)
# ======================================
# lst = ['this', 'is', 'a', 'practical', 
# 			'article', 'for', 'Pandas'] 
# # Calling DataFrame constructor on list 
# df = pd.DataFrame(lst, index=['row1','row2','row3','row4','row5','row6','row7'], columns=['col1']) 
# print(df)
# ===========================================
# data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18]} 
# # Create DataFrame 
# df = pd.DataFrame(data) 
# # Print the output. 
# print(df) 
# ===============================================
# data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
#         'Age':[27, 24, 22, 32],
#         'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
#         'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
# # Convert the dictionary into DataFrame 
# df = pd.DataFrame(data)
# # select two columns
# print(df[['Name', 'Qualification']])
# =================================================
# data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
#         'Age':[27, 24, 22, 32],
#         'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
#         'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
# # Convert the dictionary into DataFrame 
# df = pd.DataFrame(data,index=('Person1','Person2','Person3','Person4'))
# print(df)
# #with loc
# df.loc[['Person1']]
# #with iloc
# df.iloc[[0]]
# #with loc
# df.loc['Person1':'Person2']
# #or
# df.loc[['Person1','Person2']]
# #with iloc
# df.iloc[0:2]
#with loc
# df.loc['Person1':'Person2','Age':'Address']
# #or
# df.loc[['Person1','Person2'],['Age','Address']]
# #with iloc
# df.iloc[0:2,1:3]
# =======================================
# dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"], 
#         'degree': ["MBA", "BCA", "M.Tech", "MBA"], 
#         'score':[90, 40, 80, 98]} 
# df = pd.DataFrame(dict, index = [True, False, True, False]) 
# print(df) 
# ===========================================
# dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"], 
#         'degree': ["MBA", "BCA", "M.Tech", "MBA"], 
#         'score':[90, 40, 80, 98]} 
# # creating a dataframe with boolean index  
# df = pd.DataFrame(dict, index = [True, False, True, False]) 
# # accessing a dataframe using .loc[] function  
# print(df.loc[True])
# =========================================
# dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"], 
#         'degree': ["BCA", "BCA", "M.Tech", "BCA"], 
#         'score':[90, 40, 80, 98]} 
# # creating a dataframe  
# df = pd.DataFrame(dict) 
# # using a comparsion operator for filtering of data 
# print(df['degree'] == 'BCA') 
# ============================================
# dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"], 
#         'degree': ["BCA", "BCA", "M.Tech", "BCA"], 
#         'score':[90, 40, 80, 98]} 
# df = pd.DataFrame(dict, index = [0, 1, 2, 3])
# # print(df[df.index>=2])
# # =============================================
# df.sort_values("score", axis = 0, ascending = True, 
#                  inplace = True, na_position ='first') 
# # display 
# print(df )
# ==========================================\
# dict = {'First Score':[100, 90, np.nan, 95],
#         'Second Score': [30, 45, 56, np.nan],
#         'Third Score':[np.nan, 40, 80, 98]}
# # creating a dataframe from list
# df = pd.DataFrame(dict)
# # using isnull() function  
# df.isnull()
# ======================================
# dict = {'First Score':[100, 90, np.nan, 95],
#         'Second Score': [30, 45, 56, np.nan],
#         'Third Score':[np.nan, 40, 80, 98]}
# # creating a dataframe from dictionary
# df = pd.DataFrame(dict)
# # filling missing value using fillna()  
# df.fillna(0)
# =========================================
# dict = {'First Score':[100, 90, np.nan, 95],
#         'Second Score': [30, np.nan, 45, 56],
#         'Third Score':[52, 40, 80, 98],
#         'Fourth Score':[np.nan, np.nan, np.nan, 65]}
# # creating a dataframe from dictionary
# df = pd.DataFrame(dict)
# # using dropna() function  
# df.dropna()
# ==========================================
# dictionary of lists 
# dict = {'First Score':[100, np.nan, np.nan, 95], 
#         'Second Score': [30, np.nan, 45, 56], 
#         'Third Score':[52, np.nan, 80, 98], 
#         'Fourth Score':[np.nan, np.nan, np.nan, 65]} 
# df = pd.DataFrame(dict) 
# # using dropna() function     
# df.dropna(how = 'all')
# ==============================================
# dict = {'First Score':[100, np.nan, np.nan, 95], 
#         'Second Score': [30, np.nan, 45, 56], 
#         'Third Score':[52, np.nan, 80, 98], 
#         'Fourth Score':[60, 67, 68, 65]} 
# # creating a dataframe from dictionary   
# df = pd.DataFrame(dict) 
# # using dropna() function      
# df.dropna(axis = 1)
# =====================================
