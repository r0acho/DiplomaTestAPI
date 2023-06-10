import pandas as pd 
import requests
import numpy as np

with open("operation_reports.json", 'w', encoding='UTF-8') as fhanlder:
    fhanlder.flush()

with open("session_reports.json", 'w', encoding='UTF-8') as fhanlder:
    fhanlder.flush()

MODULE_URL_KAFKA = 'http://localhost:52112/KafkaProducer/RecurMessage'
MODULE_URL_BANK = 'http://localhost:52112/Bank/'

COUNT_OF_MODELS = 10

data = pd.read_csv("test_data.csv").reset_index(drop=True)

    
shuffled_indexes = list(range(len(data)))
np.random.shuffle(shuffled_indexes)

for i, row in data.iloc[shuffled_indexes].iterrows():
    new_bank_operation = row.to_dict()
    new_bank_operation["Email клиента"] = 'vanya.linzov@gmail.com'
    new_bank_operation["Email владельца станции"] = 'vanya.linzov@gmail.com'
    new_bank_operation["Номер ТСП"] = '000599979036777'
    new_bank_operation["Номер устройства"] = '79036777'
    new_bank_operation['Уникальный идентификатор операции на ПШ'] = '376DA4F64B383797'
    new_bank_operation['Уникальный идентификатор операции'] = '918591493536'
    requests.post(MODULE_URL_KAFKA, json=new_bank_operation)



# for i, row in data.iterrows():
#     new_bank_operation = row.to_dict()
#     new_bank_operation["Email клиента"] = 'vanya.lincov@gmail.com'
#     new_bank_operation["Email владельца станции"] = 'vanya.lincov@gmail.com'
#     new_bank_operation["Номер ТСП"] = '000599979036777'
#     new_bank_operation["Номер устройства"] = '79036777'
#     new_bank_operation['Уникальный идентификатор операции на ПШ'] = '376DA4F64B383797'
#     new_bank_operation['Уникальный идентификатор операции'] = '918591493536'
#     requests.post(MODULE_URL_KAFKA, json=new_bank_operation)
    
    