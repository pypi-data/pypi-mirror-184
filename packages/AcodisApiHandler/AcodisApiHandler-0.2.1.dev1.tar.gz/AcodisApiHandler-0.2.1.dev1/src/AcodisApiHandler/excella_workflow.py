from xml.etree import ElementTree

from pandas import DataFrame, read_html

from _acodis_logger import HandlerLog
from acodis_handler import AcodisAPIHandler
from acodis_parser import extract_tags

log = HandlerLog().get_log(__name__)

# Acodis instance URL
endpoint = 'https://roche-pharma-poc.service.acodis.io/workbench/api/transaction'

# Authentication for Excella Metadata workflow
user_meta = 'en__20221222143158324'
password_meta = 'f3b3ea3d77bd7a35a93bba22865c1709866038f3'

# Authentication for Excella Table workflow
user_table = 'en__20221227113542799'
password_table = 'ae99f505b46add100895714e3806ed52d99b3b08'

pdf_path = 'C:\\Users\\santor72\\dev\\acodis-api-handler\\excella_test.pdf'

# Data structures for Excella Metadata workflow

excella_metadata = [
    'product',
    'batch_number',
    'analysis_number',
    'temperature',
    'package',
    'start_of_stab_study',
    'time_weeks'
]


# def get_excella_metadata(xml):
#     for key in excella_metadata.keys():
#         try:
#             excella_metadata[key] = xml.find('.//p/span[@class="{key}"]'.format(key=key)).text.strip()
#         except:
#             pass
#
#     return excella_metadata


def get_excella_table(xml):
    tables = xml.findall('table')
    dfs = []
    df = DataFrame()

    for table in tables:
        html_table = ElementTree.tostring(table, encoding='unicode')
        log.debug(html_table)
        try:
            df = read_html(html_table)[0]
        except:
            pass
        finally:
            dfs.append(df)


# Start Excella metadata workflow
idp = AcodisAPIHandler(endpoint)

# Set authentication
idp.authenticate(
    user=user_meta,
    password=password_meta
)

# Run workflow for Excella metadata (defined by the user and password)
idp.workflow(pdf_path)

result = extract_tags(idp, excella_metadata)

for key in result.keys():
    print("{key}: \"{result}\"".format(key=key, result=result[key]))

# # Start Excella table workflow using the AcodisAPIHandler object
# idp.authenticate(
#     user=user_table,
#     password=password_table
# )
#
# # Run the table workflow
# idp.workflow(pdf_path)
#
# print(get_excella_table(idp.xml))
