import numpy as np
from autogluon.tabular  import TabularDataset,TabularPredictor
import pandas as pd
from dash import Dash, dcc, html, Input, Output, callback

predictor = TabularPredictor.load('AutogluonModels\\ag-20230626_042217')
#命名id列和label列
id, label = 'ID', 'OS'

app = Dash(__name__)

app.layout = html.Div([
    html.Div(children=[
        ], style={'padding': 10, 'flex': 1}),
    html.Div(children=[
    html.H6("Please fill in the patient's baseline information:"),
    html.H6(" "),
    html.H6(" "),
    html.Div([
        html.Label('MARITAL_STATUS'),
        dcc.Dropdown(['Coupled', 'Single'], 'Single',id='MARITAL_STATUS'),
    ]),
    html.H6(" "),
    html.Div([
        html.Label('GENDER'),
        dcc.Dropdown(['Female', 'Male'], 'Male',id='GENDER'),
    ]),
    html.H6(" "),
    html.Div([
        html.Label('AGE'),
        dcc.Dropdown(['<50', '50–60', '60–70', '≥70'], '<50',id='AGE'),
    ]),
    html.H6(" "),
    html.Div([
        html.Label('NUMBER_OF_SITEMALIGNANT_TUMORS'),
        dcc.Input(id='NUMBER_OF_SITEMALIGNANT_TUMORS', value='1', type='number')
    ]),
    html.H6(" "),
    html.Div([
        html.Label('grade'),
        dcc.Dropdown(['Ⅰ', 'Ⅱ', 'Ⅲ', 'Ⅳ'], 'Ⅰ',id='grade'),
    ]),
    html.H6(" "),
    html.Div([
        html.Label('stage'),
        dcc.Dropdown(['Ⅰ', 'Ⅱ', 'Ⅲ', 'Ⅳ'], 'Ⅰ',id='stage'),
    ]),
    html.H6(" "),
    html.Div([
        html.Label('Tstage'),
        dcc.Dropdown(['T1', 'T2', 'T3', 'T4'], 'T1',id='Tstage'),
    ]),
    html.H6(" "),
    html.Div([
        html.Label('Nstage'),
        dcc.Dropdown(['N0', 'N1', 'N2'], 'N0',id='Nstage'),
    ]),
    html.H6(" "),
    html.Div([
        html.Label('Mstage'),
        dcc.Dropdown(['M0', 'M1'], 'M1',id='Mstage'),
    ]),
    ], style={'padding': 10, 'flex': 1}),

    html.Div(children=[
    html.H6("Please fill in the surgical method and predicted survival time:"),
    html.Div([
        html.Label('surgery'),
        dcc.Dropdown(['Complete/total nephrectomy', 'Partial/subtotal nephrectomy'], 'Complete/total nephrectomy',id='surgery'),  
    ]),
    html.H6(" "),
    html.Div([
        html.Label('Prepare the predicted survival time'),
        dcc.Input(id='Prepare the predicted survival time', value='30', type='number')
    ]),

    html.Br(),
    html.H6("The probability of survival:"),
    html.H6(""),
    html.H6(""),
    html.Div(id='my-output'),
    ], style={'padding': 10, 'flex': 1}),
    html.Div(children=[
        ], style={'padding': 10, 'flex': 1})
], style={'display': 'flex', 'flex-direction': 'row'})


@callback(
    Output('my-output', 'children'),
    Input('MARITAL_STATUS', 'value'),
    Input('GENDER', 'value'),
    Input('AGE', 'value'),
    Input('NUMBER_OF_SITEMALIGNANT_TUMORS', 'value'),
    Input('grade', 'value'),
    Input('stage', 'value'),
    Input('Tstage', 'value'),
    Input('Nstage', 'value'),
    Input('Mstage', 'value'),
    Input('surgery', 'value'),
    Input('Prepare the predicted survival time', 'value'))
def update_output_div(APP2, APP3, 
                      APP4, APP6, 
                      APP7, APP8, 
                      APP9, APP10, 
                      APP11, APP5, 
                      APP1):
    test_csv=pd.read_csv('mod.csv')
    test_csv.iloc[:,1]=APP1
    test_csv.iloc[:,2]=APP2
    test_csv.iloc[:,3]=APP3
    test_csv.iloc[:,4]=APP4
    test_csv.iloc[:,5]=APP5
    test_csv.iloc[:,6]=APP6
    test_csv.iloc[:,7]=APP7
    test_csv.iloc[:,8]=APP8
    test_csv.iloc[:,9]=APP9
    test_csv.iloc[:,10]=APP10
    test_csv.iloc[:,11]=APP11
    output_value=predictor.predict_proba(test_csv.drop(columns=[id]))
    output_value=output_value.loc[0,0]
    return output_value


if __name__ == '__main__':
    app.run_server(debug=True)
