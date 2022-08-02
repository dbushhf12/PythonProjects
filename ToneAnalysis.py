from operator import index
import pandas as pd
import numpy as np
import scipy
import sklearn 
import statistics 

myData = pd.read_csv('[FileLocation]')    #import csv data file

azErr = myData["error_az_abs"][myData["stim_name"] != "Training"]   #create array called azErr that holds all absolute azimuth error scores excluding training block
elvErr = myData["error_el_abs"][myData["stim_name"] != "Training"]  #create array called elvErr that holds all absolute elevation error scores excluding training block

##DESCRIPTIVES##
azErr_mean = round(statistics.mean(azErr), 2)
elvErr_mean = round(statistics.mean(elvErr), 2)

#Mean azimuth error by tone 
#region 
T1_filt = myData["stim_name"] == "Tone_1"
azErr_T1_filt = myData.loc[T1_filt]["error_az_abs"]
mean_azErr_T1 = round(statistics.mean(azErr_T1_filt), 2)

T2_filt = myData["stim_name"] == "Tone_2"
azErr_T2_filt = myData.loc[T2_filt]["error_az_abs"]
mean_azErr_T2 = round(statistics.mean(azErr_T2_filt), 2)

T3_filt = myData["stim_name"] == "Tone_3"
azErr_T3_filt = myData.loc[T3_filt]["error_az_abs"]
mean_azErr_T3 = round(statistics.mean(azErr_T3_filt), 2)

T4_filt = myData["stim_name"] == "Tone_4"
azErr_T4_filt = myData.loc[T4_filt]["error_az_abs"]
mean_azErr_T4 = round(statistics.mean(azErr_T4_filt), 2)
#endregion

#Mean elevation error by tone
#region 
elvErr_T1_filt = myData.loc[T1_filt]["error_el_abs"]
mean_elvErr_T1 = round(statistics.mean(elvErr_T1_filt), 2)

elvErr_T2_filt = myData.loc[T2_filt]["error_el_abs"]
mean_elvErr_T2 = round(statistics.mean(elvErr_T2_filt), 2)

elvErr_T3_filt = myData.loc[T3_filt]["error_el_abs"]
mean_elvErr_T3 = round(statistics.mean(elvErr_T3_filt), 2)

elvErr_T4_filt = myData.loc[T4_filt]["error_el_abs"]
mean_elvErr_T4 = round(statistics.mean(elvErr_T4_filt), 2)
#endregion

#Mean azimuth error by actual azimuth location
#region
az1_filt = myData["stim_az"] == 0
azErr_az1_filt = myData.loc[az1_filt]["error_az_abs"]
mean_azErr_az1 = round(statistics.mean(azErr_az1_filt), 2)

az2_filt = myData["stim_az"] == 24
azErr_az2_filt = myData.loc[az2_filt]["error_az_abs"]
mean_azErr_az2 = round(statistics.mean(azErr_az2_filt), 2)

az3_filt = myData["stim_az"] == -48
azErr_az3_filt = myData.loc[az3_filt]["error_az_abs"]
mean_azErr_az3 = round(statistics.mean(azErr_az3_filt), 2)

az4_filt = myData["stim_az"] == 72
azErr_az4_filt = myData.loc[az4_filt]["error_az_abs"]
mean_azErr_az4 = round(statistics.mean(azErr_az4_filt), 2)

az5_filt = myData["stim_az"] == -96
azErr_az5_filt = myData.loc[az5_filt]["error_az_abs"]
mean_azErr_az5 = round(statistics.mean(azErr_az5_filt), 2)

az6_filt = myData["stim_az"] == 120
azErr_az6_filt = myData.loc[az6_filt]["error_az_abs"]
mean_azErr_az6 = round(statistics.mean(azErr_az6_filt), 2)

az7_filt = myData["stim_az"] == -144
azErr_az7_filt = myData.loc[az7_filt]["error_az_abs"]
mean_azErr_az7 = round(statistics.mean(azErr_az7_filt), 2)

az8_filt = myData["stim_az"] == 168
azErr_az8_filt = myData.loc[az8_filt]["error_az_abs"]
mean_azErr_az8 = round(statistics.mean(azErr_az8_filt), 2)
#endregion

#Mean azimuth error by actual elevation location
#region
elv1_filt = myData["stim_el"] == -30
azErr_elv1_filt = myData.loc[elv1_filt]["error_az_abs"]
mean_azErr_elv1 = round(statistics.mean(azErr_elv1_filt), 2)

elv2_filt = myData["stim_el"] == 0
azErr_elv2_filt = myData.loc[elv2_filt]["error_az_abs"]
mean_azErr_elv2 = round(statistics.mean(azErr_elv2_filt), 2)

elv3_filt = myData["stim_el"] == 30
azErr_elv3_filt = myData.loc[elv3_filt]["error_az_abs"]
mean_azErr_elv3 = round(statistics.mean(azErr_elv3_filt), 2)
#endregion

#Mean elevation error by actual azimuth location
#region
elvErr_az1_filt = myData.loc[az1_filt]["error_el_abs"]
mean_elvErr_az1 = round(statistics.mean(elvErr_az1_filt), 2)

elvErr_az2_filt = myData.loc[az2_filt]["error_el_abs"]
mean_elvErr_az2 = round(statistics.mean(elvErr_az2_filt), 2)

elvErr_az3_filt = myData.loc[az3_filt]["error_el_abs"]
mean_elvErr_az3 = round(statistics.mean(elvErr_az3_filt), 2)

elvErr_az4_filt = myData.loc[az4_filt]["error_el_abs"]
mean_elvErr_az4 = round(statistics.mean(elvErr_az4_filt), 2)

elvErr_az5_filt = myData.loc[az5_filt]["error_el_abs"]
mean_elvErr_az5 = round(statistics.mean(elvErr_az5_filt), 2)

elvErr_az6_filt = myData.loc[az6_filt]["error_el_abs"]
mean_elvErr_az6 = round(statistics.mean(elvErr_az6_filt), 2)

elvErr_az7_filt = myData.loc[az7_filt]["error_el_abs"]
mean_elvErr_az7 = round(statistics.mean(elvErr_az7_filt), 2)

elvErr_az8_filt = myData.loc[az8_filt]["error_el_abs"]
mean_elvErr_az8 = round(statistics.mean(elvErr_az8_filt), 2)
#endregion

#Mean elevation error by actual elevation location
#region
elvErr_elv1_filt = myData.loc[elv1_filt]["error_el_abs"]
mean_elvErr_elv1 = round(statistics.mean(elvErr_elv1_filt), 2)

elvErr_elv2_filt = myData.loc[elv2_filt]["error_el_abs"]
mean_elvErr_elv2 = round(statistics.mean(elvErr_elv2_filt), 2)

elvErr_elv3_filt = myData.loc[elv3_filt]["error_el_abs"]
mean_elvErr_elv3 = round(statistics.mean(elvErr_elv3_filt), 2)
#endregion

##plot error values by tones
#elevation error
elvErr_plot = pd.DataFrame({"lab" :["Tone 1", "Tone 2", "Tone 3", "Tone 4"], "val" :[mean_elvErr_T1, mean_elvErr_T2, mean_elvErr_T3, mean_elvErr_T4]})
ax = elvErr_plot.plot.bar(x="lab", y="val", rot=0)
print(ax)


##INFERENTIAL STATS##
azErr_elvErr = scipy.stats.ttest_ind(azErr, elvErr, nan_policy='propagate') #run independant samples T-Test comparing mean absolute azimuth error and absolute elevation error scores

azErr_Tone = scipy.stats.f_oneway(myData["error_az_abs"][myData["stim_name"] == "Tone_1"],      #one way ANOVA comparing absolute azimuth error across tones
                                myData["error_az_abs"][myData["stim_name"] == "Tone_2"],
                                myData["error_az_abs"][myData["stim_name"] == "Tone_3"],
                                myData["error_az_abs"][myData["stim_name"] == "Tone_4"],)

elvErr_Tone = scipy.stats.f_oneway(myData["error_el_abs"][myData["stim_name"] == "Tone_1"],     #one way ANOVA comparing absolute elevation error across tones
                                myData["error_el_abs"][myData["stim_name"] == "Tone_2"],
                                myData["error_el_abs"][myData["stim_name"] == "Tone_3"],
                                myData["error_el_abs"][myData["stim_name"] == "Tone_4"],)

azErr_azActual = scipy.stats.f_oneway(myData["error_az_abs"][myData["stim_az"] == 0],       #one way ANOVA comparing absolute azimuth error across actual azimuth locations
                                myData["error_az_abs"][myData["stim_az"] == 24],
                                myData["error_az_abs"][myData["stim_az"] == -48],
                                myData["error_az_abs"][myData["stim_az"] == 72],
                                myData["error_az_abs"][myData["stim_az"] == -96],
                                myData["error_az_abs"][myData["stim_az"] == 120],
                                myData["error_az_abs"][myData["stim_az"] == -144],
                                myData["error_az_abs"][myData["stim_az"] == 168],)

azErr_elvActual = scipy.stats.f_oneway(myData["error_az_abs"][myData["stim_el"] == -30],       #one way ANOVA comparing absolute azimuth error across actual elevation locations
                                myData["error_az_abs"][myData["stim_el"] == 0],
                                myData["error_az_abs"][myData["stim_el"] == 30],)

elvErr_azActual = scipy.stats.f_oneway(myData["error_el_abs"][myData["stim_az"] == 0],      #one way ANOVA comparing absolute elevation error across actual azimuth locations
                                myData["error_el_abs"][myData["stim_az"] == 24],
                                myData["error_el_abs"][myData["stim_az"] == -48],
                                myData["error_el_abs"][myData["stim_az"] == 72],
                                myData["error_el_abs"][myData["stim_az"] == -96],
                                myData["error_el_abs"][myData["stim_az"] == 120],
                                myData["error_el_abs"][myData["stim_az"] == -144],
                                myData["error_el_abs"][myData["stim_az"] == 168],)

elvErr_elvActual = scipy.stats.f_oneway(myData["error_el_abs"][myData["stim_el"] == -30],       #one way ANOVA comparing absolute elevation error across actual elevation locations
                                myData["error_el_abs"][myData["stim_el"] == 0],
                                myData["error_el_abs"][myData["stim_el"] == 30],)

##COMPILE RESULTS##
#Interential
results_dict = {"AzErr X ElvErr" : [azErr_elvErr], "Tone x ElvErr" : [elvErr_Tone], "Tone x AzErr" : [azErr_Tone], "elvErr x elvActual" : [elvErr_elvActual],       #populate dictionary with results
                "elvErr x azActual" : [elvErr_azActual], "azErr x elvActual" : [azErr_elvActual], "azErr x azActual" : [azErr_azActual]}

results_df = pd.DataFrame(results_dict,     #convert to dictionary to data frame with row label
                        index=pd.Index(['test statistic, p-value:']))

#Descriptive
descriptive_dict = {"Mean azErr" : [azErr_mean], "Mean elvErr" : [elvErr_mean], "Mean azErr Tone 1" : [mean_azErr_T1], "Mean azErr Tone 2" : [mean_azErr_T2],   #populate dictionary with results
                    "Mean azErr Tone 3" : [mean_azErr_T3], "Mean azErr Tone 4" : [mean_azErr_T4],  "Mean azErr az 0" : [mean_azErr_az1],
                    "Mean azErr az 24" : [mean_azErr_az2], "Mean azErr az -48" : [mean_azErr_az3], "Mean azErr az 72" : [mean_azErr_az4], 
                    "Mean azErr az -96" : [mean_azErr_az5], "Mean azErr az 120" : [mean_azErr_az6], "Mean azErr az -144" : [mean_azErr_az7], 
                    "Mean azErr az 168" : [mean_azErr_az7], "Mean azErr elv -30" : [mean_azErr_elv1], "Mean azErr elv 0" : [mean_azErr_elv2], 
                    "Mean azErr elv 30" : [mean_azErr_elv3],"Mean elvErr Tone 1" : [mean_elvErr_T1], "Mean elvErr Tone 2" : [mean_elvErr_T2], 
                    "Mean elvErr Tone 3" : [mean_elvErr_T3], "Mean elvErr Tone 4" : [mean_elvErr_T4], "Mean elvErr az 0" : [mean_elvErr_az1],
                    "Mean elvErr az 24" : [mean_elvErr_az2], "Mean elvErr az -48" : [mean_elvErr_az3], "Mean elvErr az 72" : [mean_elvErr_az4], 
                    "Mean elvErr az -96" : [mean_elvErr_az5], "Mean elvErr az 120" : [mean_elvErr_az6], "Mean elvErr az -144" : [mean_elvErr_az7], 
                    "Mean elvErr az 168" : [mean_elvErr_az7], "Mean elvErr elv -30" : [mean_elvErr_elv1], "Mean elvErr elv 0" : [mean_elvErr_elv2], 
                    "Mean elvErr elv 30" : [mean_elvErr_elv3]}

descriptive_df = pd.DataFrame(descriptive_dict,     #convert to dictionary to data frame with row label
                    index=pd.Index(["mean absolute error"]))

results_df.to_csv('[FileLocation]')       #save data frame as a csv at specified file location 
descriptive_df.to_csv('[FileLocation]')       #save data frame as a csv at specified file location 
