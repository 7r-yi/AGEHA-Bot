import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import json


def road_spreadsheet(name):
    file = json.load(open('./src/SpreadsheetAPI.json', 'r'))

    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credential = {
        "type": 'service_account',
        "project_id": file['project_id'],
        "private_key_id": file['private_key_id'],
        "private_key": file['private_key'].replace("\\n", "\n"),
        "client_email": file['client_email'],
        "client_id": file['client_id'],
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": file['client_x509_cert_url']
    }
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(credential, scope)
    gc = gspread.authorize(credentials)

    return gc.open_by_key('1d6sItuYsdscSQkYMwqj3a0AflKtxoH8ObhgynQpb6AQ').worksheet(name)


def get_times(enemy):
    sheet = road_spreadsheet("チーム戦結果")
    data = sheet.get_all_values()

    if enemy == "":
        return ""

    for i in reversed(range(len(data))):
        if enemy == data[i][1].split("(")[0]:
            try:
                # 過去に2回以上対戦したことがある場合
                if "(" in data[i][1]:
                    if data[i][2] != "":
                        return int(data[i][1].split("(")[1][:-1]) + 1
                    # 実施前にスプレッドシートに記載されている場合は、その()内の数が正しい対戦回数
                    else:
                        return int(data[i][1].split("(")[1][:-1])
                # 過去に1回だけ対戦したことがある場合
                else:
                    if data[i][2] != "":
                        return 2
                    # 実施前にスプレッドシートに記載されている場合は、その()内の数が正しい対戦回数
                    else:
                        return 1
            # エラー処理
            except:
                return "?"
    # 1回も対戦したことが無い場合
    return 1
