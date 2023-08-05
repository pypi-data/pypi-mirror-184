from nazca4sdk.datahandling.knowledge.knowledge_data_type import KnowledgeDataType
from nazca4sdk.sdk import SDK
from nazca4sdk import FormatChart, FormatText
import requests

sdk = SDK(False)
# odczyt dla danego klucza
values = sdk.read_knowledge("test")
#print(values)

# result = sdk.write_knowledge("blob", "pliczek", "/2022-07-07_14-31.png", KnowledgeDataType.BLOB)
#result = sdk.write_knowledge("gruby", "sekcjaGruby", "test", KnowledgeDataType.TEXT)
#print(result)










