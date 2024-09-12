import numpy as np
from autogluon.tabular  import TabularDataset,TabularPredictor
import pandas as pd

id, label = 'Patient ID', 'label'

predictor = TabularPredictor.load('AutogluonModels\\model365')
test_csv=pd.read_csv('4.all.csv')
test_csv['surg'] = 'None'
preds=predictor.predict(test_csv.drop(columns=[id]))
submission=predictor.predict_proba(test_csv.drop(columns=[id])) #输出概率
submission_1 = submission[1]
submission_1 = submission_1.to_frame(name="None")
test_csv=pd.read_csv('4.all.csv')
test_csv['surg'] = 'Partial or subtotal nephrectomy'
preds=predictor.predict(test_csv.drop(columns=[id]))
submission=predictor.predict_proba(test_csv.drop(columns=[id])) #输出概率
submission_2 = submission[1]
submission_2 = submission_2.to_frame(name="Partial or subtotal nephrectomy")
test_csv=pd.read_csv('4.all.csv')
test_csv['surg'] = 'Complete/total/simple nephrectomy'
preds=predictor.predict(test_csv.drop(columns=[id]))
submission=predictor.predict_proba(test_csv.drop(columns=[id])) #输出概率
submission_3 = submission[1]
submission_3 = submission_3.to_frame(name="Complete/total/simple nephrectomy")
test_csv=pd.read_csv('4.all.csv')
test_csv['surg'] = 'Radical nephrectomy'
preds=predictor.predict(test_csv.drop(columns=[id]))
submission=predictor.predict_proba(test_csv.drop(columns=[id])) #输出概率
submission_4 = submission[1]
submission_4 = submission_4.to_frame(name="Radical nephrectomy")
# 合并四个 submission DataFrame  
combined_submission = pd.concat([submission_1, submission_2, submission_3, submission_3], axis=1)   
combined_submission ['result'] = combined_submission.apply(lambda row: row.idxmin(), axis=1) 
combined_submission.to_csv('submission.csv', index=False)  

predictor = TabularPredictor.load('AutogluonModels\\model1095')
test_csv=pd.read_csv('4.all.csv')
test_csv['surg'] = 'None'
preds=predictor.predict(test_csv.drop(columns=[id]))
submission=predictor.predict_proba(test_csv.drop(columns=[id])) #输出概率
submission_1 = submission[1]
submission_1 = submission_1.to_frame(name="None")
test_csv=pd.read_csv('4.all.csv')
test_csv['surg'] = 'Partial or subtotal nephrectomy'
preds=predictor.predict(test_csv.drop(columns=[id]))
submission=predictor.predict_proba(test_csv.drop(columns=[id])) #输出概率
submission_2 = submission[1]
submission_2 = submission_2.to_frame(name="Partial or subtotal nephrectomy")
test_csv=pd.read_csv('4.all.csv')
test_csv['surg'] = 'Complete/total/simple nephrectomy'
preds=predictor.predict(test_csv.drop(columns=[id]))
submission=predictor.predict_proba(test_csv.drop(columns=[id])) #输出概率
submission_3 = submission[1]
submission_3 = submission_3.to_frame(name="Complete/total/simple nephrectomy")
test_csv=pd.read_csv('4.all.csv')
test_csv['surg'] = 'Radical nephrectomy'
preds=predictor.predict(test_csv.drop(columns=[id]))
submission=predictor.predict_proba(test_csv.drop(columns=[id])) #输出概率
submission_4 = submission[1]
submission_4 = submission_4.to_frame(name="Radical nephrectomy")
# 合并四个 submission DataFrame  
combined_submission = pd.concat([submission_1, submission_2, submission_3, submission_3], axis=1)   
combined_submission ['result'] = combined_submission.apply(lambda row: row.idxmin(), axis=1) 
combined_submission.to_csv('submission.csv', index=False)  

predictor = TabularPredictor.load('AutogluonModels\\model1825')
test_csv=pd.read_csv('4.all.csv')
test_csv['surg'] = 'None'
preds=predictor.predict(test_csv.drop(columns=[id]))
submission=predictor.predict_proba(test_csv.drop(columns=[id])) #输出概率
submission_1 = submission[1]
submission_1 = submission_1.to_frame(name="None")
test_csv=pd.read_csv('4.all.csv')
test_csv['surg'] = 'Partial or subtotal nephrectomy'
preds=predictor.predict(test_csv.drop(columns=[id]))
submission=predictor.predict_proba(test_csv.drop(columns=[id])) #输出概率
submission_2 = submission[1]
submission_2 = submission_2.to_frame(name="Partial or subtotal nephrectomy")
test_csv=pd.read_csv('4.all.csv')
test_csv['surg'] = 'Complete/total/simple nephrectomy'
preds=predictor.predict(test_csv.drop(columns=[id]))
submission=predictor.predict_proba(test_csv.drop(columns=[id])) #输出概率
submission_3 = submission[1]
submission_3 = submission_3.to_frame(name="Complete/total/simple nephrectomy")
test_csv=pd.read_csv('4.all.csv')
test_csv['surg'] = 'Radical nephrectomy'
preds=predictor.predict(test_csv.drop(columns=[id]))
submission=predictor.predict_proba(test_csv.drop(columns=[id])) #输出概率
submission_4 = submission[1]
submission_4 = submission_4.to_frame(name="Radical nephrectomy")
# 合并四个 submission DataFrame  
combined_submission = pd.concat([submission_1, submission_2, submission_3, submission_3], axis=1)   
combined_submission ['result'] = combined_submission.apply(lambda row: row.idxmin(), axis=1) 
combined_submission.to_csv('submission.csv', index=False)  

predictor = TabularPredictor.load('AutogluonModels\\model2555')
test_csv=pd.read_csv('4.all.csv')
test_csv['surg'] = 'None'
preds=predictor.predict(test_csv.drop(columns=[id]))
submission=predictor.predict_proba(test_csv.drop(columns=[id])) #输出概率
submission_1 = submission[1]
submission_1 = submission_1.to_frame(name="None")
test_csv=pd.read_csv('4.all.csv')
test_csv['surg'] = 'Partial or subtotal nephrectomy'
preds=predictor.predict(test_csv.drop(columns=[id]))
submission=predictor.predict_proba(test_csv.drop(columns=[id])) #输出概率
submission_2 = submission[1]
submission_2 = submission_2.to_frame(name="Partial or subtotal nephrectomy")
test_csv=pd.read_csv('4.all.csv')
test_csv['surg'] = 'Complete/total/simple nephrectomy'
preds=predictor.predict(test_csv.drop(columns=[id]))
submission=predictor.predict_proba(test_csv.drop(columns=[id])) #输出概率
submission_3 = submission[1]
submission_3 = submission_3.to_frame(name="Complete/total/simple nephrectomy")
test_csv=pd.read_csv('4.all.csv')
test_csv['surg'] = 'Radical nephrectomy'
preds=predictor.predict(test_csv.drop(columns=[id]))
submission=predictor.predict_proba(test_csv.drop(columns=[id])) #输出概率
submission_4 = submission[1]
submission_4 = submission_4.to_frame(name="Radical nephrectomy")
# 合并四个 submission DataFrame  
combined_submission = pd.concat([submission_1, submission_2, submission_3, submission_3], axis=1)   
combined_submission ['result'] = combined_submission.apply(lambda row: row.idxmin(), axis=1) 
combined_submission.to_csv('submission.csv', index=False)  

predictor = TabularPredictor.load('AutogluonModels\\model3285')
test_csv=pd.read_csv('4.all.csv')
test_csv['surg'] = 'None'
preds=predictor.predict(test_csv.drop(columns=[id]))
submission=predictor.predict_proba(test_csv.drop(columns=[id])) #输出概率
submission_1 = submission[1]
submission_1 = submission_1.to_frame(name="None")
test_csv=pd.read_csv('4.all.csv')
test_csv['surg'] = 'Partial or subtotal nephrectomy'
preds=predictor.predict(test_csv.drop(columns=[id]))
submission=predictor.predict_proba(test_csv.drop(columns=[id])) #输出概率
submission_2 = submission[1]
submission_2 = submission_2.to_frame(name="Partial or subtotal nephrectomy")
test_csv=pd.read_csv('4.all.csv')
test_csv['surg'] = 'Complete/total/simple nephrectomy'
preds=predictor.predict(test_csv.drop(columns=[id]))
submission=predictor.predict_proba(test_csv.drop(columns=[id])) #输出概率
submission_3 = submission[1]
submission_3 = submission_3.to_frame(name="Complete/total/simple nephrectomy")
test_csv=pd.read_csv('4.all.csv')
test_csv['surg'] = 'Radical nephrectomy'
preds=predictor.predict(test_csv.drop(columns=[id]))
submission=predictor.predict_proba(test_csv.drop(columns=[id])) #输出概率
submission_4 = submission[1]
submission_4 = submission_4.to_frame(name="Radical nephrectomy")
# 合并四个 submission DataFrame  
combined_submission = pd.concat([submission_1, submission_2, submission_3, submission_3], axis=1)   
combined_submission ['result'] = combined_submission.apply(lambda row: row.idxmin(), axis=1) 
combined_submission.to_csv('submission.csv', index=False)  
