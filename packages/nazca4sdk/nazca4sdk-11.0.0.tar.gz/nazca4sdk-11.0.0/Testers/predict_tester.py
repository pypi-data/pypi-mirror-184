from nazca4sdk.sdk import SDK

sdk = SDK(False)

print(sdk.predict('Socomec_Stacja', ['V1'], 15, 'DAY', 15, '1min', 'prophet'))
