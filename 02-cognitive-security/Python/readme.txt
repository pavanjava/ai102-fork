This folder contains Python code for accessing services using key-vault

Step1: use below command to generate rbac details
az ad sp create-for-rbac -n "api://<unique-app-name>" --role owner --scopes subscriptions/<subscription-id>/resourceGroups/<rg-name>

response could be as below
{
  "appId": "201a43b3-2b7a-49b8-b23f-2d8b0327ff4a",
  "displayName": "api://<sample-app>",
  "password": "jhgsjhdgasjdgjasgdjhagsdjhgasjhdgjasgd",
  "tenant": "kjashdkjashdkjhaskjdhaskjdhkajhsd"
}

Step2: az ad sp show --id 201a43b3-2b7a-49b8-b23f-2d8b0327ff4a --query id --out tsv

Step3: az keyvault set-policy -n <key-vault-name> --object-id <id-from-above-cmd> --secret-permissions get list