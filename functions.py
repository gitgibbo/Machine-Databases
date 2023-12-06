import sqlite3 as sq
import pandas as pd

def dbparser(input):
    con = sq.connect(input)
    cur = con.cursor()
    StatisticsRecipeCup = pd.read_sql_query('SELECT * FROM StatisticsRecipeHeader', con)
    RecipeHeader = pd.read_sql_query('SELECT * FROM RecipeHeader', con)
    RecipeHeader = RecipeHeader[['RecipeHeaderID', 'CustomName']]
    RecipeHeader['CustomName'] = RecipeHeader['CustomName'].astype('str')
    RecipeHeader = RecipeHeader[RecipeHeader['CustomName'] != 'None']
    RecipeHeader.columns = ['RecipeHeaderID', 'RecipeName']
    joined_table = pd.merge(StatisticsRecipeCup, RecipeHeader, on='RecipeHeaderID', how='left')
    joined_table = joined_table[joined_table['StatisticsTypeID'] == 1]
    joined_table = joined_table[['RecipeName', 'TotalCount']].reset_index(drop=True)
    

    return joined_table

def get_serial(input):
    con = sq.connect(input)
    cur = con.cursor()
    SwConfigValue = pd.read_sql_query('SELECT * FROM SwConfigValue', con)
    result = SwConfigValue.loc[SwConfigValue['Name'] == 'MachineNumber', 'Value'].iloc[0]
    return result


                                 