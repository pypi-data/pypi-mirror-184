import numpy as np
import pandas as pd
# pd.set_option('display.max_columns', None)
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")
import ppscore as pps
from minepy import MINE

import os

#######################################################################
### Correlation
#######################################################################
def correlation_analysis(df, corr_threshold):
  print("===== Computing Correlation =====\n")
  df_corr_spearman = calculate_corr(df, corr_threshold, "spearman")
  df_corr_pearson = calculate_corr(df, corr_threshold, "pearson")   
  df_corr = (pd.concat([df_corr_spearman,df_corr_pearson],axis=0)
            .reset_index(drop=True)
            )
  print("* Completed!\n")
  return df_corr


def calculate_corr(df, corr_threshold, corr_type):
  df_corr = (df
             .corr(method=corr_type)
             .stack()
             .reset_index()
             .rename({"level_0":'Column1',"level_1":'Column2',0:'Score'}, axis=1)
             .query("Column1 != Column2") # drop if col1 and col2 are the same
             .assign(AnalysisType = corr_type.capitalize())
             )
  df_corr = df_corr[df_corr['Score'].abs() >= corr_threshold] # filter based on threshold
  df_corr.reset_index(drop=True, inplace=True)

  # remove duplicated pairs (based on Col1 and Col2 levels)
  # https://stackoverflow.com/questions/47051854/remove-duplicates-based-on-the-content-of-two-columns-not-the-order
  # improvement? https://stackoverflow.com/questions/48395350/how-to-remove-duplicates-from-correlation-in-pandas
  mask = ~pd.DataFrame(np.sort(df_corr[['Column1','Column2']], axis=1)).duplicated()
  df_corr = df_corr[mask]

  return df_corr.sort_values(by='Score', key=abs, ascending=False)


#######################################################################
### PPS
#######################################################################
def pps_analysis(df, pps_threshold):
  print("===== Computing PPS =====\n")
  pps_matrix_raw = pps.matrix(df)
  pps_matrix = (pps_matrix_raw
                .filter(['x', 'y', 'ppscore'])
                .pivot(columns='x', index='y', values='ppscore')
                .stack()
                .reset_index()
                .rename({"y":'Column1',"x":'Column2',0:'Score'}, axis=1)
                .query("Column1 != Column2") # drop if col1 and col2 are the same
                .assign(AnalysisType = "PPS")
                )
  
  pps_matrix = pps_matrix[pps_matrix['Score'].abs() >= pps_threshold] # filter based on threshold
  pps_matrix.reset_index(drop=True, inplace=True)
  print("* Completed!\n")
  return pps_matrix.sort_values(by='Score', key=abs, ascending=False).reset_index(drop=True)


#######################################################################
### MIC
#######################################################################
def mic_analysis(df_corr, df_pps, df, target_vars):
  # https://minepy.readthedocs.io/en/latest/
  print("===== Computing MIC =====\n")
  df_relevant_pairs = get_relevant_pairs(df_corr, df_pps, target_vars)
  df_mic = compute_mic(df, df_relevant_pairs)
  print("\n* Completed! \n")
  return df_mic


def get_relevant_pairs(df_corr, df_pps, target_vars):
  df_relevant_pairs = pd.concat([df_pps,df_corr], axis=0).reset_index(drop=True)
  mask = ~pd.DataFrame(np.sort(df_relevant_pairs[['Column1','Column2']], axis=1)).duplicated()
  df_relevant_pairs = df_relevant_pairs[mask].filter(["Column1","Column2"],axis=1).reset_index(drop=True)
  
  # subset only pairs where target_vars is present
  if None in target_vars:
    return df_relevant_pairs
  else:
    return df_relevant_pairs.query(f"Column1 in {target_vars} or Column2 in {target_vars}").reset_index(drop=True)
  

def compute_mic(df, df_relevant_pairs):
  df_mic = pd.DataFrame([])
  for index, row in df_relevant_pairs.iterrows():
    print(f"Computation {index + 1} / {df_relevant_pairs.shape[0]}")
    try:
        feature1,feature2 = row['Column1'], row['Column2']
        mine = MINE(alpha=0.6, c=15, est="mic_approx")
        mine.compute_score(df[feature1],df[feature2])
        mic_data = pd.DataFrame(data={"Column1":[feature1], "Column2":[feature2],
                                      "Score":[mine.mic()], "AnalysisType":"MIC"})
        df_mic = df_mic.append(mic_data)

    except: 
      print(f"MIC computation error :{feature1} and {feature2} on index {index + 1}")
      pass
  
  return df_mic.sort_values(by='Score', key=abs, ascending=False).reset_index(drop=True)


#######################################################################
### pipeline for encoding categorical variables
#######################################################################
from sklearn.pipeline import Pipeline
from feature_engine.encoding import OrdinalEncoder
def pipeline_encode_categorical_variables(df):
  """
  * if df has categorical variables
      df has original data, df_encoded has encoded categories to number
  * otherwise
      df_encoded is df, df is df
  """
  
  cat_cols = df.select_dtypes(exclude=['int64','float64']).columns.to_list()
  if cat_cols:
    pipeline = Pipeline([
        ("OrdinalEncoder", OrdinalEncoder(encoding_method='arbitrary', variables=cat_cols ) )
    ])
    df_encoded = pipeline.fit_transform(df)
  else:
    df_encoded = df.copy()

  return df, df_encoded


#######################################################################
### supporting functions to the class
#######################################################################
def data_validation(self, df):
    if len(df.columns) == 1: 
      raise ValueError(f'The dataframe should have more than 1 column. \nCurrent dataset column: {df.columns.to_list()}')

    if df.isna().sum().sum() > 0:
      raise ValueError("Your dataset has missing values, you should handle first.")

    for var in self.target_vars:
      if var not in df.columns.to_list() and var != None:
        raise ValueError(f"{var} is not found at dataframe columns: {df.columns.to_list()}")


def check_flags(self):
  if self.flag_compute_score == None:
    raise ValueError(f'The method .compute_score() should be run first')

  if self.flag_summary_report == None:
    raise ValueError(f'The method .summary_report() should be run first')

  if self.flag_plot_relationship == None:
    raise ValueError(f'The method .plot_relationships() should be run first')
  


#######################################################################
### summary report
#######################################################################
def show_summary_report(relevant_cols_pairs, df_summary):
    print(f"\n* There are {len(relevant_cols_pairs)} pairs of columns with relevant Corr, PPS, and MIC \n")
    print(relevant_cols_pairs)

    print(f"\n\n* Top 10 MIC scores\n")
    print((df_summary
          .query("AnalysisType == 'MIC'")
          .sort_values(by=['Score'],ascending=False)
          .head(10)
          .reset_index(drop=True) 
          ) )


def save_report(df, file_path):
  if file_path == None:
      file_path = "Report Summary.csv"
  else:
    if not os.path.isdir(file_path): os.makedirs(file_path)
    file_path = f"{file_path}/Report Summary.csv"
  
  df.to_csv(file_path, index=False)


def show_full_report(show_full_report_flag, df_summary):
    if show_full_report_flag:
      print(f"\n\n\n* Scores for each Column Pair per Analysis Type\n")
      print(df_summary.to_string()) 


#######################################################################
### plot relationship
#######################################################################
def plot_relationship(df, relevant_cols_pairs,df_summary, alpha_scatter=0.7):
  
  for index, row in relevant_cols_pairs.iterrows():
    print(f"========  {index + 1}: {row['Column1']} and {row['Column2']}  ========\n")
    print(f"* {show_scores(row,df_summary)}\n") # df_summary gets score (corr, pps, mic) for each column pair

    # decide plot type for each columns' combination
    x, y = row['Column1'] , row['Column2']
    var_type_x , var_type_y = df[x].dtype, df[y].dtype
    if var_type_x not in [object,"category"] and var_type_y not in [object,'category'] :
      plot_type = "scatterplot"
    elif var_type_x in [object, "category"] and var_type_y in [object, "category"] :
      plot_type = "barplot"
    else:
      plot_type = "boxplot"

    # plot accoriding to columns' type
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(18,6))
    if plot_type == "scatterplot":
      sns.scatterplot(data=df, x=x, y=y, alpha=alpha_scatter, ax=axes[0])
      sns.scatterplot(data=df, x=y, y=x, alpha=alpha_scatter, ax=axes[1])
    elif plot_type == 'boxplot':
      if var_type_x in [object,"category"]:
        sns.boxplot(data=df, x=x, y=y, ax=axes[0])
      if var_type_y in [object,"category"]:
        sns.boxplot(data=df, x=y, y=x, ax=axes[1])
    elif plot_type == 'barplot':
      df.groupby([x,y]).size().unstack().plot(kind='bar', stacked=True, ax=axes[0]).legend(loc='best')
      df.groupby([y,x]).size().unstack().plot(kind='bar', stacked=True,ax=axes[1]).legend(loc='best')

    axes[0].set_title(f"{y}  x  {x}", fontsize=14, y=1.05)
    axes[0].set_xlabel(x)
    axes[0].set_ylabel(y)
    axes[1].set_title(f"{x}  x  {y}", fontsize=14, y=1.05)
    axes[1].set_xlabel(y)
    axes[1].set_ylabel(x)
    plt.show()
    print("\n\n")


def show_scores(row,df_summary):
  subset = df_summary.query(f"(Column1 == '{row['Column1']}' and Column2 == '{row['Column2']}') or (Column2 == '{row['Column1']}' and Column1 == '{row['Column2']}') ")
  statement = ""
  for analysis_type in subset['AnalysisType'].unique():
    if analysis_type != "PPS": score = subset.query(f"AnalysisType == '{analysis_type}'")['Score'].round(3).values[0]
    else: score = subset.query(f"AnalysisType == '{analysis_type}'")['Score'].round(3).values
    statement = statement + analysis_type + " " + str(score) + "  "

  return statement


############################################################
### Heatmaps: Corr, PPS, and MIC
############################################################

def process_data_for_heatmap(df, analysis_type):
  df_part1 = df.query(f"AnalysisType == '{analysis_type}'").drop("AnalysisType",axis=1)
  df_part2 =  df_part1.copy()
  df_part2['Column1'] , df_part2['Column2'] = df_part1['Column2'] , df_part1['Column1']
  
  if analysis_type != 'PPS':
    df_combined = pd.concat([df_part1,df_part2],axis=0).reset_index(drop=True)
  else: 
    df_combined = df_part1.copy()

  df_pivot = pd.pivot_table(data=df_combined,
                            index=['Column1'],
                            columns=['Column2'],
                            values='Score')
  
  return df_pivot


def plot_heatmap(df, analysis_type, self, figsize):
  print(f"\n\n\n===== Heatmap: {analysis_type} =====")
  if analysis_type in ['Spearman','Pearson']:
    heatmap_lower_triangle_only(df,self.corr_threshold, figsize)
  elif analysis_type in ['PPS']:
    heatmap_remove_diagonal(df, self.pps_threshold, figsize)
  elif analysis_type in ['MIC']:
    heatmap_lower_triangle_only(df, self.mic_threshold, figsize)
  else:
    print(f"** {analysis_type} is not found as analysis type!")


def heatmap_lower_triangle_only(df, threshold, figsize=(20, 12), font_annot=8):
  mask = np.zeros_like(df, dtype=np.bool)
  mask[np.triu_indices_from(mask)] = True
  mask[abs(df) < threshold] = True

  fig, axes = plt.subplots(figsize=figsize)
  sns.heatmap(df, annot=True, xticklabels=True, yticklabels=True,
              mask=mask, cmap='viridis', annot_kws={"size": font_annot}, 
              ax=axes,linewidth=0.5)
  axes.set_yticklabels(df.columns, rotation=0)
  plt.ylim(len(df.columns), 0)
  plt.ylabel('')
  plt.xlabel('')
  plt.show()


def heatmap_remove_diagonal(df, threshold, figsize=(20, 12), font_annot=8):
  mask = np.zeros_like(df, dtype=np.bool)
  mask[abs(df) < threshold] = True

  fig, ax = plt.subplots(figsize=figsize)
  ax = sns.heatmap(df, annot=True, xticklabels=True, yticklabels=True,
                    mask=mask, cmap='viridis', annot_kws={"size": font_annot},
                    linewidth=0.05, linecolor='grey')
  plt.ylim(len(df.columns), 0)
  plt.ylabel('')
  plt.xlabel('')
  plt.show()



class CorrPpsMicAnalytics:

  def __init__(self, corr_threshold=0.0, pps_threshold=0.0, target_vars=None):
    self.corr_threshold = corr_threshold
    self.pps_threshold = pps_threshold
    self.mic_threshold = 0
    if not isinstance(target_vars, list): 
      target_vars = [target_vars]
    self.target_vars = target_vars
    # flags to check if previous methods were run
    # self.flag_compute_score = None
    # self.flag_summary_report = None
    # self.flag_plot_relationship = None


  def compute_score(self, dataframe):
    # self.flag_compute_score = 1
    data_validation(self, dataframe)

    self.df, df_numerical = pipeline_encode_categorical_variables(dataframe)

    self.df_corr = correlation_analysis(df_numerical, self.corr_threshold)
    self.df_pps = pps_analysis(df_numerical, self.pps_threshold)
    self.df_mic = mic_analysis(self.df_corr, self.df_pps, df_numerical, self.target_vars)

    
  def summary_report(self, show_full_report_flag=False, file_path=None):
    # self.flag_summary_report = 1
    # check_flags(self)

    self.df_summary = (pd.concat([self.df_mic, self.df_pps, self.df_corr], axis=0).reset_index(drop=True))
    self.df_summary = self.df_summary.sort_values(by=['AnalysisType','Score'],ascending=False)
    self.relevant_cols_pairs = get_relevant_pairs(self.df_corr, self.df_pps, self.target_vars)

    show_summary_report(self.relevant_cols_pairs, self.df_summary)    
    save_report(self.df_summary, file_path)
    show_full_report(show_full_report_flag, self.df_summary)


  def plot_relationships(self):
    # self.flag_plot_relationship = 1
    # check_flags(self)
    plot_relationship(self.df, self.relevant_cols_pairs, self.df_summary)
    

  def plot_heatmaps(self, figsize=(10, 12)):
    # check_flags(self)

    for analysis_type in self.df_summary['AnalysisType'].unique():
      (self.df_summary
       .pipe(process_data_for_heatmap,analysis_type) 
       .pipe(plot_heatmap, analysis_type, self, figsize)
       )
