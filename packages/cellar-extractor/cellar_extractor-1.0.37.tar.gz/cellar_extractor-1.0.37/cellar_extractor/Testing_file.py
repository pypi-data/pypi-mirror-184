"""

This file is purely a testing file for trying out separate parts of code, testing if everything works and such.
Can be also used to develop future code.



"""
import pandas as pd
from cellar import get_cellar_extra
def extract_containing_subject_matter(df,phrase):
    returner = df[df["LEGAL RESOURCE IS ABOUT SUBJECT MATTER"].str.contains(phrase, na=False)]
    return returner
def get_df_with_celexes(df,celexes):
    returner = df[df['CELEX IDENTIFIER'].isin(celexes)]
    return returner
def get_edges_list(df):
    extraction = df[['CELEX IDENTIFIER','citing']]
    extraction.reset_index(inplace=True)
    keys = extraction['CELEX IDENTIFIER']
    vals = extraction['citing']
    s_list = list()
    t_list = list()
    all_celexes=set()
    edges = {'Source' :  s_list,
             'Target' :  t_list
             }
    for i in range(len(keys)):
        k = keys[i]
        val = vals[i]
        if val == val:
            val_unpacked = val.split(";")
            final_val = [i for i in val_unpacked if i.startswith("6")]
            if len(final_val) == 0:
                s_list.append(k)
                all_celexes.add(k)
                t_list.append("")
            else:
                for val in final_val:
                    s_list.append(k)
                    all_celexes.add(val)
                    t_list.append(str(val))
        else:
            s_list.append(k)
            all_celexes.add(k)
            t_list.append("")
    return pd.DataFrame(edges), all_celexes
def get_nodes_and_edges(df):
    df_mod = extract_containing_subject_matter(df, "Consumer protection")
    edges, celexes = get_edges_list(df_mod)
    nodes = get_df_with_celexes(df,celexes)
    return nodes,edges
from os.path import join
from json_to_csv import read_csv
import time
if __name__ == '__main__':

   # path = join("","data")
    #path_file = join(path,"tester.csv")
   # df = read_csv(path_file)
   # nodes,edges = get_nodes_and_edges(df)
   # path_nodes = join(path, "nodes.csv")
  #  path_edges = join(path, "edges.csv")
   # nodes.to_csv(path_nodes,index=False)
   # edges.to_csv(path_edges,index=False)
  #  b=2

  get_cellar_extra(save_file="y",username="n00ac9w5",password="",max_ecli=10,threads=10,sd="1900-01-01")
