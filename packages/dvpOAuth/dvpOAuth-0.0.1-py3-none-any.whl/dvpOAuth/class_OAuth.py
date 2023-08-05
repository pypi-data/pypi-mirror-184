import requests, json, os, logging, re

from functools import wraps
from .error import AuthClientError, MissingTokenError

from .util import SEARCH_BASE_URL, SEARCH_PAR
from collections import defaultdict

from datetime import datetime

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

py_handler = logging.FileHandler(f"{__name__}.log", mode='a')
py_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

py_handler.setFormatter(py_formatter)
logger.addHandler(py_handler)


def singleton(cls):
    @wraps(cls)
    def wrapper(*args, **kwargs):
        if not wrapper.instance:
            wrapper.instance = cls(*args, **kwargs)
        return wrapper.instance

    wrapper.instance = None
    return wrapper


def request_new_token():
    session = requests.Session()
    session.proxies = {
        "http": os.environ['QUOTAGUARDSTATIC_URL'], 
        "https": os.environ['QUOTAGUARDSTATIC_URL']
    }

    my_headers = {
          'Content-Type': 'application/x-www-form-urlencoded', 
          }
    params = {'grant_type': 'client_credentials'}

    resp = session.post(
              os.environ['Authentication'],
              params = params,
              headers = my_headers, 
              data = {
                  'client_id':	os.environ['client_id'],
                  'client_secret':	os.environ['client_secret']
              }
          )
    
    a = json.loads(resp.content)
    token = a['access_token']
    return session, token


@singleton
class DVPOAuth:
    '''OAuth API for dvp app'''
    def __init__(self, token = None, session = None):
        self.token = token
        self.session = session
        

    ''' class decorator '''
    def _renew_token(foo):
        ''' private decorator '''
        def wrapper(self, *args, **kwargs):
            try:
                # print(f'token : {self.token}')
                logger.info(f'Existing token : {self.token}')
                return foo(self, *args, **kwargs)
            except (MissingTokenError, AuthClientError) as e:
                self.session, self.token = request_new_token()
                logger.info(f'New token : {self.token}')
                return foo(self, *args, **kwargs)
        return wrapper
    
    @_renew_token
    def call_eligibility(self, account = None):
        if not self.token: raise MissingTokenError

        auth = 'Bearer '+ self.token
        eligibility_params = {
            'ContractAccountID': "\'" + account + "\'",
            'DUNSNumber': "\'" + os.environ['DUNSNumber'] + "\'",
            '$format': 'json'
        }

        resp_query = self.session.get(
            os.environ["Eligibility"],
            params=eligibility_params,
            headers={'Authorization': auth}
        )

        logger.info(f'Eligibiity status code : {resp_query.status_code}')
        logger.info(f'Response content : {resp_query.content}')

        if resp_query.status_code == 401:
            logger.exception("Eligibility 401 error.")
            raise AuthClientError
        
        resp = json.loads(resp_query.content)
        logger.info(f'Response : {resp["d"]["ZDSMInquiry"]}')
        return resp_query.status_code, resp

    def check_eligibility(self, account = None):
        _, resp = self.call_eligibility(account)
        return True if resp['d']['ZDSMInquiry']['RejectionReasonDsm'] == '' else False
    
    
    def convert_eligibility_json_from_oauth_to_soap(self, status_code = None, resp = None):
        data = resp["d"]["ZDSMInquiry"]

        res = {
                'AccountNumber': data['AccountNumber'],
                'AccountStatusCode': data['AccountStatus'],
                'AccountType': data['AccountClass'],
                'BusinessName': data['BusinessName'],
                'FirstName': data['CustomerFirstName'],
                'Header': {
                    'DateTimeStamp': datetime.now().strftime("%Y-%m-%d-%H.%M.%S.%f"),
                    'MessageText': data['RejectionReasonDsm'],
                    'Result': 'S' if data['RejectionReasonDsm'] == '' else 'N',
                    'ReturnCode': status_code
                },
                'LastName': data['CustomerLastName'],
                'LastSmartCoolCreditAmt': '.00',
                'LastSmartCoolCreditDate': None,
                'Latitude': data['LatitudeOfPremise'],
                'Longitude': data['LongitudeOfPremise'],
                'MailingAddressCity': data['MailingAddressCity'],
                'MailingAddressLine1': data['MailingAddressStreet'],
                'MailingAddressState': data['MailingAddressState'],
                'MailingAddressZipCode': data['MailingAddressZipCode'],
                'MedicalFlag': data['LifeSupportFlag'],
                'MiddleName': data['CustomerMiddleName'],
                'NameSuffix': data['NameSuffix'],
                'NonStandardAddressLine1': data['MailingAddressStreet1'],
                'NonStandardAddressLine2': data['MailingAddressStreet2'],
                'NonStandardAddressLine3': data['MailingAddressStreet3'],
                'OfficeCode': data['OfficeId'],
                'OpenAccess': data['ChoiceEnrolledFlag'],
                'OptOut': data['OptOutFlag'],
                'OtherAccountNames': data['BpRelation1']['FullName'],
                'PremiseId': data['PremiseId'],
                'PremisePhoneAreaCode': data['AreaCode'],
                'PremisePhoneNumber': data['PhoneNumber'],
                'ServiceAddressLine1': data['ServiceStreetAddress'],
                'ServiceCity': data['ServiceAddressCity'],
                'ServicePoint': {
                    'ServicePoint': [
                        {
                            'AmiMeter': data['MeterData1']['AmiFlag'],
                            'MeterNumber': data['MeterData1']['MeterId'],
                            'RateCode': [data['MeterData1']['RateCode']]
                        }
                    ]
                },
                'ServiceState': data['ServiceAddressState'],
                'ServiceZipCode': data['ServiceAddressZipCode'],
                'SwitchActive': 'N',
                'SwitchInstalled': 'N'
            }
        return res 

        # Eligibility OAuth API format
        # {
        #     '__metadata': {
        #         'type': 'ZISU_UMC_DSM_SRV.ZDSMEligibility'
        #     },
        #     'PremiseId': '0971564200',
        #     'PippFlag': 'N',
        #     'VendorId': 'DS',
        #     'AccountNumber': '9714010007',
        #     'BusinessName': '',
        #     'CustomerFullName': 'CLAUDIA J MCCANN',
        #     'CustomerMiddleName': 'J',
        #     'CustomerLastName': 'MCCANN',
        #     'NameSuffix': '',
        #     'CustomerFirstName': 'CLAUDIA',
        #     'AreaCode': '434',
        #     'PhoneNumber': '296-5296',
        #     'ServiceStreetAddress': '1001 FERN CT',
        #     'ServiceAddressCity': 'CHARLOTTESVILLE',
        #     'ServiceAddressState': 'VA',
        #     'ServiceAddressZipCode': '22901',
        #     'OfficeId': '8100',
        #     'AccountClass': 'R',
        #     'LifeSupportFlag': 'Y',
        #     'ChoiceEnrolledFlag': '',
        #     'AccountStatus': 'A',
        #     'LatitudeOfPremise': '3.8044151907E1',
        #     'LongitudeOfPremise': '-7.8468137877999993E1',
        #     'MailingAddressStreet': '1001 FERN CT',
        #     'MailingAddressCity': 'CHARLOTTESVILLE',
        #     'MailingAddressState': 'VA',
        #     'MailingAddressZipCode': '22901',
        #     'MailingAddressStreet1': '',
        #     'MailingAddressStreet2': '',
        #     'MailingAddressStreet3': '',
        #     'ApartmentFlag': 'N',
        #     'DeviceInstalledFlag': 'N',
        #     'DeviceActiveFlag': 'N',
        #     'OptOutFlag': 'N',
        #     'RejectionReasonDsm': '',
        #     'BpRelation1': {
        #         '__metadata': {
        #         'type': 'ZISU_UMC_DSM_SRV.BpRelation1'
        #         },
        #         'FullName': '',
        #         'MiddleName': '',
        #         'LastName': '',
        #         'FirstName': ''
        #     },
        #     'BpRelation2': {
        #         '__metadata': {
        #         'type': 'ZISU_UMC_DSM_SRV.BpRelation2'
        #         },
        #         'FullName': '',
        #         'MiddleName': '',
        #         'LastName': '',
        #         'FirstName': ''
        #     },
        #     'BpRelation3': {
        #         '__metadata': {
        #         'type': 'ZISU_UMC_DSM_SRV.BpRelation3'
        #         },
        #         'FullName': '',
        #         'MiddleName': '',
        #         'LastName': '',
        #         'FirstName': ''
        #     },
        #     'MeterData1': {
        #         '__metadata': {
        #         'type': 'ZISU_UMC_DSM_SRV.MeterData1'
        #         },
        #         'RateCode': 'VR-1',
        #         'AmiFlag': 'Y',
        #         'MeterId': '000000000260633362'
        #     },
        #     'MeterData2': {
        #         '__metadata': {
        #         'type': 'ZISU_UMC_DSM_SRV.MeterData2'
        #         },
        #         'RateCode': '',
        #         'AmiFlag': '',
        #         'MeterId': ''
        #     },
        #     'MeterData3': {
        #         '__metadata': {
        #         'type': 'ZISU_UMC_DSM_SRV.MeterData3'
        #         },
        #         'RateCode': '',
        #         'AmiFlag': '',
        #         'MeterId': ''
        #     },
        #     'MeterData4': {
        #         '__metadata': {
        #         'type': 'ZISU_UMC_DSM_SRV.MeterData4'
        #         },
        #         'RateCode': '',
        #         'AmiFlag': '',
        #         'MeterId': ''
        #     },
        #     'MeterData5': {
        #         '__metadata': {
        #         'type': 'ZISU_UMC_DSM_SRV.MeterData5'
        #         },
        #         'RateCode': '',
        #         'AmiFlag': '',
        #         'MeterId': ''
        #     }
        #     }

    def convert_account_search_json_from_oauth_to_soap(self, status_code = None, resp = None):
        if not resp['d']['results']:
            return None

        
        resp_parent = resp["d"]["results"][0]
        data = resp_parent['ZAcctSearchNav']['results'][0]

        # {
        #     "__metadata":{
        #         "id":"http://ccapimqa.dominionnet.com:8443/sap/opu/odata/sap/ZISU_UMC_DSM_SRV/ZACCTSRCHDataSet('9714010007')",
        #         "uri":"http://ccapimqa.dominionnet.com:8443/sap/opu/odata/sap/ZISU_UMC_DSM_SRV/ZACCTSRCHDataSet('9714010007')",
        #         "type":"ZISU_UMC_DSM_SRV.ZACCTSRCHData"
        #     },
        #     "IdBa":"9714010007",
        #     "ParentAccount":"",
        #     "BillingAccountStat":"A",
        #     "AcctStatusDescription":"Active",
        #     "BadDebtFlag":"N",
        #     "BusinessPartner":"1100298105",
        #     "CustomerName":"CLAUDIA J MCCANN",
        #     "AddressLine1":"1001 FERN CT",
        #     "City":"CHARLOTTESVILLE",
        #     "State":"VA",
        #     "Country":"US",
        #     "Zip":"22901-4001",
        #     "AdditionalAddr":"",
        #     "Town":"8100",
        #     "Premise":"971564200",
        #     "MeterId":"000000000260633362",
        #     "MeterStatus":"A",
        #     "ServiceType":"01",
        #     "CustomerFirstName":"CLAUDIA",
        #     "CustomerMiddleName":"J",
        #     "CustomerLastName":"MCCANN",
        #     "CustomerSuffix":"",
        #     "PrimaryPhoneNumber":"+14342965296",
        #     "PrimaryEmail":"",
        #     "ApplicationType":"IN",
        #     "IVREligIndicator":"Y",
        #     "DisconnectExpireDate":"None",
        #     "DelinquencyIndicator":"N",
        #     "AMIIndicator":"Y",
        #     "ThirdPartyAmount":"0.000",
        #     "AccountActive":"Y",
        #     "AccountCloseDate":"None",
        #     "AccountType":"MM"
        #     }
        
        return_dict = {
            'AccountSearchSequence': {
                'AccountSearchSequence': [
                    {
                        'AccountFirstName': data["CustomerFirstName"],
                        'AccountLastName': data["CustomerLastName"],
                        'AccountMiddleName': data["CustomerMiddleName"],
                        'AccountName': data['CustomerName'],
                        'AccountNameSuffix': data['CustomerSuffix'],
                        'AccountNumber': data["IdBa"],
                        'AccountStatus': data["BillingAccountStat"],
                        'AccountStatusDesc': data['AcctStatusDescription'],
                        'AdditionalAddressInfo': data["AdditionalAddr"],
                        'Address': data['AddressLine1'],
                        'City': data["City"],
                        'CompanyNumber': None,
                        'State': data["State"],
                        'ZipCode': data["Zip"]
                    }
                ]
            },
            'Header': {
                'DateTimeStamp': datetime.fromtimestamp(eval(re.findall(r'\(.*?\)', resp_parent["ActiveTimeStamp"])[0])/1000), # ??? need parse the timestamp /Date(1672174552000)/
                'MessageText': resp_parent["ReturnMessageText"],  # "Business Account details retrived successfully!"
                'Result': resp_parent["InternetReturnCode"],
                'ReturnCode': resp_parent["ErrorCode"] # Error code?
            },
            'MoreData': resp_parent["MoreData"],
            'RowsReturned': resp_parent["RowsReturned"]
        }
        return return_dict
    

    @_renew_token
    def account_search(self, *args, **kwargs):
        '''search account based on the account number'''
        if not self.token: raise MissingTokenError

        auth = 'Bearer '+ self.token
        
        # search API

    
        dict = defaultdict(str, args[0])
        
        try:
            if dict['account']:
                account = dict['account'] if dict['account'] else None
                filter = SEARCH_PAR + "SearchType eq 'ACC' and BillAccount eq '" + account + "' and CallingApplication eq 'SEW' and ActiveBaOnly eq 'N' and QuantityRowsRequested eq 10 "
            elif dict['first_name'] and dict['last_name']:
                filter = SEARCH_PAR + "SearchType eq 'NAM' and CustomerFirstName eq '" + \
                    dict['first_name'] + "' and CustomerLastName eq '" + dict['last_name'] + "'  and ActiveBaOnly eq 'N'"
            elif dict['meter_number']:
                filter = SEARCH_PAR + "SearchType eq 'MET' and Meter eq '" + dict['meter_number'] + "'"
            elif dict['last_four_ssn']:
                filter = SEARCH_PAR + "CallingApplication eq 'DSM' and ActiveBaOnly eq 'Y' and SearchType eq 'SSN' and SSN eq '" + dict['last_four_ssn'] + "'"
            elif dict['premise_number']:
                filter = SEARCH_PAR + "SearchType eq 'PRE' and Premise eq '" + dict['premise_number'] + "' and ActiveBaOnly eq 'N'"
            else:
                raise ValueError
        except:
            pass
            '''handle exception here'''
        
        search_params = {
            '$format': 'json',
            '$filter': filter,
            '$expand': 'ZAcctSearchNav'
        }

        resp_query = requests.get(
            SEARCH_BASE_URL,
            params=search_params,
            headers={'Authorization': auth}
        )
        print(resp_query.content)

        logger.info(f'Search status code : {resp_query.status_code}')

        if resp_query.status_code == 401:
            logger.exception("Account search error.")
            raise AuthClientError

        resp = json.loads(resp_query.content)
        logger.info(f'Search response : {resp}')

        return resp_query.status_code, resp

# business name
    # "raw": "InternetFunctionCode eq 'ACCTSRCH' and SearchType eq 'BIZ' and CorporateName eq 'COMCAST' and ActiveBaOnly eq 'Y'&$expand=ZAcctSearchNav&$format=json",

    # first and last name
    # "raw": "InternetFunctionCode eq 'ACCTSRCH' and SearchType eq 'NAM' and CustomerFirstName eq 'John' and CustomerLastName eq 'Doe' and ActiveBaOnly eq 'N'&$expand=ZAcctSearchNav&$format=xml",

    # account number
    # "raw": "InternetFunctionCode eq 'ACCTSRCH' and SearchType eq 'ACC' and BillAccount eq '2533333635' and CallingApplication eq 'SEW' and ActiveBaOnly eq 'N' and QuantityRowsRequested eq 10 &$expand=ZAcctSearchNav&$format=json",

    # meter number
    # "raw": "InternetFunctionCode eq 'ACCTSRCH' and SearchType eq 'MET' and Meter eq '92441962' and ActiveBaOnly eq 'Y' and QuantityRowsRequested eq 50&$expand=ZAcctSearchNav&$format=json",

    # Telephone Number
    # "raw": "InternetFunctionCode eq 'ACCTSRCH' and SearchType eq 'TEL' and PhoneNumber eq '@1820' and AreaCode eq '489' and CallingApplication eq 'TEL' and ActiveBaOnly eq 'Y' and QuantityRowsRequested eq 4&$expand=ZAcctSearchNav&$format=json",

    # SSN Last 4
    # "raw": "InternetFunctionCode eq 'ACCTSRCH' and SearchType eq 'SSN' and SSN eq '1400'  and ActiveBaOnly eq 'N' and QuantityRowsRequested eq 50&$expand=ZAcctSearchNav&$format=json",

    # Tax Number
    # "raw": "InternetFunctionCode eq 'ACCTSRCH' and SearchType eq 'TAX' and FederalTaxId eq '854907359' and CallingApplication eq 'SUM' and ActiveBaOnly eq 'Y' and QuantityRowsRequested eq 100&$expand=ZAcctSearchNav&$format=json",

    # Premise Number
    # "raw": "InternetFunctionCode eq 'ACCTSRCH' and SearchType eq 'PRE' and Premise eq '253564000' and ActiveBaOnly eq 'N'&$expand=ZAcctSearchNav&$format=json",

    # Address City State
    # "raw": "InternetFunctionCode eq 'ACCTSRCH' and SearchType eq 'ADR' and City eq 'HENRICO' and State eq 'VA' and CallingApplication eq 'GCC' and ActiveBaOnly eq 'Y'&$expand=ZAcctSearchNav&$format=json",
    # "raw": "InternetFunctionCode eq 'ACCTSRCH' and SearchType eq 'ADR' and City eq 'HENRICO' and State eq 'VA' and CallingApplication eq 'GCC' and ActiveBaOnly eq 'Y'&$expand=ZAcctSearchNav&$format=json",

    # Address Street
    # "raw": "InternetFunctionCode eq 'ACCTSRCH' and SearchType eq 'ADR' and StreetName eq 'Main' and StreetType eq 'St' and City eq 'Richmond' and State eq 'VA' and ActiveBaOnly eq 'Y'&$expand=ZAcctSearchNav&$format=json",

    # Usage by Account Number - JSON
    # "raw": "https://ccapimqa.apimanagement.us21.hana.ondemand.com/v1/cc/DSMVendorsInboundServices/ZAccountBalanceCASet?$filter=ContractAccount eq '519809982' and Action eq '5' and DateRange/StartDate eq datetime'2022-01-01T00:00:00' and DateRange/EndDate eq datetime'2022-10-30T00:00:00'&$expand=ZUsageStatement&$format=json",

########################
    # business name
    # "raw": "https://ccapimqa.apimanagement.us21.hana.ondemand.com/v1/cc/DSMVendorsInboundServices/ZAcctSearchAndRetrieveSet?$filter=InternetFunctionCode eq 'ACCTSRCH' and SearchType eq 'BIZ' and CorporateName eq 'COMCAST' and ActiveBaOnly eq 'Y'&$expand=ZAcctSearchNav&$format=json",

    # first and last name
    # "raw": "https://ccapimqa.apimanagement.us21.hana.ondemand.com/v1/cc/DSMVendorsInboundServices/ZAcctSearchAndRetrieveSet?$filter=InternetFunctionCode eq 'ACCTSRCH' and SearchType eq 'NAM' and CustomerFirstName eq 'John' and CustomerLastName eq 'Doe' and ActiveBaOnly eq 'N'&$expand=ZAcctSearchNav&$format=xml",

    # account number
    # "raw": "https://ccapimqa.apimanagement.us21.hana.ondemand.com/v1/cc/DSMVendorsInboundServices/ZAcctSearchAndRetrieveSet?=&$filter=InternetFunctionCode eq 'ACCTSRCH' and SearchType eq 'ACC' and BillAccount eq '2533333635' and CallingApplication eq 'SEW' and ActiveBaOnly eq 'N' and QuantityRowsRequested eq 10 &$expand=ZAcctSearchNav&$format=json",

    # meter number
    # "raw": "https://ccapimqa.apimanagement.us21.hana.ondemand.com/v1/cc/DSMVendorsInboundServices/ZAcctSearchAndRetrieveSet?=&$filter=InternetFunctionCode eq 'ACCTSRCH' and SearchType eq 'MET' and Meter eq '92441962' and ActiveBaOnly eq 'Y' and QuantityRowsRequested eq 50&$expand=ZAcctSearchNav&$format=json",

    # Telephone Number
    # "raw": "https://ccapimqa.apimanagement.us21.hana.ondemand.com/v1/cc/DSMVendorsInboundServices/ZAcctSearchAndRetrieveSet?=&$filter=InternetFunctionCode eq 'ACCTSRCH' and SearchType eq 'TEL' and PhoneNumber eq '@1820' and AreaCode eq '489' and CallingApplication eq 'TEL' and ActiveBaOnly eq 'Y' and QuantityRowsRequested eq 4&$expand=ZAcctSearchNav&$format=json",

    # SSN Last 4
    # "raw": "https://ccapimqa.apimanagement.us21.hana.ondemand.com/v1/cc/DSMVendorsInboundServices/ZAcctSearchAndRetrieveSet?=&$filter=InternetFunctionCode eq 'ACCTSRCH' and SearchType eq 'SSN' and SSN eq '1400'  and ActiveBaOnly eq 'N' and QuantityRowsRequested eq 50&$expand=ZAcctSearchNav&$format=json",

    # Tax Number
    # "raw": "https://ccapimqa.apimanagement.us21.hana.ondemand.com/v1/cc/DSMVendorsInboundServices/ZAcctSearchAndRetrieveSet?=&$filter=InternetFunctionCode eq 'ACCTSRCH' and SearchType eq 'TAX' and FederalTaxId eq '854907359' and CallingApplication eq 'SUM' and ActiveBaOnly eq 'Y' and QuantityRowsRequested eq 100&$expand=ZAcctSearchNav&$format=json",

    # Premise Number
    # "raw": "https://ccapimqa.apimanagement.us21.hana.ondemand.com/v1/cc/DSMVendorsInboundServices/ZAcctSearchAndRetrieveSet?$filter=InternetFunctionCode eq 'ACCTSRCH' and SearchType eq 'PRE' and Premise eq '253564000' and ActiveBaOnly eq 'N'&$expand=ZAcctSearchNav&$format=json",

    # Address City State
    # "raw": "https://ccapimqa.apimanagement.us21.hana.ondemand.com/v1/cc/DSMVendorsInboundServices/ZAcctSearchAndRetrieveSet?=&$filter=InternetFunctionCode eq 'ACCTSRCH' and SearchType eq 'ADR' and City eq 'HENRICO' and State eq 'VA' and CallingApplication eq 'GCC' and ActiveBaOnly eq 'Y'&$expand=ZAcctSearchNav&$format=json",
    # "raw": "https://ccapimqa.apimanagement.us21.hana.ondemand.com/v1/cc/DSMVendorsInboundServices/ZAcctSearchAndRetrieveSet?=&$filter=InternetFunctionCode eq 'ACCTSRCH' and SearchType eq 'ADR' and City eq 'HENRICO' and State eq 'VA' and CallingApplication eq 'GCC' and ActiveBaOnly eq 'Y'&$expand=ZAcctSearchNav&$format=json",

    # Address Street
    # "raw": "https://ccapimqa.apimanagement.us21.hana.ondemand.com/v1/cc/DSMVendorsInboundServices/ZAcctSearchAndRetrieveSet?$filter=InternetFunctionCode eq 'ACCTSRCH' and SearchType eq 'ADR' and StreetName eq 'Main' and StreetType eq 'St' and City eq 'Richmond' and State eq 'VA' and ActiveBaOnly eq 'Y'&$expand=ZAcctSearchNav&$format=json",

    # Usage by Account Number - JSON
    # "raw": "https://ccapimqa.apimanagement.us21.hana.ondemand.com/v1/cc/DSMVendorsInboundServices/ZAccountBalanceCASet?$filter=ContractAccount eq '519809982' and Action eq '5' and DateRange/StartDate eq datetime'2022-01-01T00:00:00' and DateRange/EndDate eq datetime'2022-10-30T00:00:00'&$expand=ZUsageStatement&$format=json",


# {
#    "d":{
#       "results":[
#          {
#             "__metadata":{
#                "id":"http://ccapimqa.dominionnet.com:8443/sap/opu/odata/sap/ZISU_UMC_DSM_SRV/ZAcctSearchAndRetrieveSet('RETRACCT')",
#                "uri":"http://ccapimqa.dominionnet.com:8443/sap/opu/odata/sap/ZISU_UMC_DSM_SRV/ZAcctSearchAndRetrieveSet('RETRACCT')",
#                "type":"ZISU_UMC_DSM_SRV.ZAcctSearchAndRetrieve"
#             },
#             "RETRACCTData":{
#                "__metadata":{
#                   "type":"ZISU_UMC_DSM_SRV.RetrAcctData"
#                },
#                "AccountClass":"Z001",
#                "AccountCloseDate":"None",
#                "AccountRepFlag":"",
#                "AccountRepName":"",
#                "AccountActive":"Y",
#                "AccountType":"MM",
#                "AcctOpenDate":"/Date(1660953600000)/",
#                "ActivityTimestamp":"/Date(1672174552000)/",
#                "AdditionalAddressInfo":"",
#                "AlternateRate":"",
#                "AltMailAddrSeq":"",
#                "AMIIndicator":"Y",
#                "ApplicationType":"IN",
#                "BillAccountStatusCode":"A",
#                "BillCycle":"16",
#                "CodeNpso":"0",
#                "CollectionAgencyStatus":"",
#                "CurrentConversationId":"",
#                "CustomerId":"1100298105",
#                "CustomerName1":"CLAUDIA J MCCANN",
#                "CustomerName2":"",
#                "CustomerName3":"",
#                "CustomerName4":"",
#                "CustomerName5":"",
#                "CustomerPin1":"",
#                "CustomerPin2":"",
#                "CustomerPin3":"",
#                "CustomerPin4":"",
#                "CustomerPin5":"",
#                "CustomerSsn1":"4564",
#                "CustomerSsn2":"",
#                "CustomerSsn3":"",
#                "CustomerSsn4":"",
#                "CustomerSsn5":"",
#                "DateEndMm":"",
#                "DateEndYyyy":"",
#                "DateStartMm":"",
#                "DateStartYyyy":"",
#                "DelinquencyIndicator":"N",
#                "DisconnectExpireDate":"None",
#                "FederalTaxId":"",
#                "InternetUserId":"",
#                "IVREligIndicator":"Y",
#                "MailAddrCity":"CHARLOTTESVILLE",
#                "MailAddrDateEffective":"None",
#                "MailAddrDateTerm":"None",
#                "MailAddrDirection":"",
#                "MailAddrDirSuffix":"",
#                "MailAddrHouseMod":"",
#                "MailAddrHouseNumber":"1001",
#                "MailAddrModifier":"",
#                "MailAddrName":"",
#                "MailAddrNonStd1":"",
#                "MailAddrNonStd2":"",
#                "MailAddrNonStd3":"",
#                "MailAddrState":"VA",
#                "MailAddrStreetName":"FERN CT",
#                "MailAddrStreetType":"",
#                "MailAddrZipcode":"22901",
#                "MailAddrZipSuffix":"4001",
#                "MeterIdNumber":"000000000260633362",
#                "NameCustFirst":"CLAUDIA",
#                "NameCustLast":"MCCANN",
#                "NameCustMiddle":"J",
#                "Password":"",
#                "PasswordIndicator":"N",
#                "Phone":"434-296-5296",
#                "PhoneAreaCode":"434",
#                "PhoneExt":"",
#                "PhoneNumberSeq":"",
#                "PremiseId":"971564200",
#                "RateCode":"VR-1",
#                "RateCodeDescription":"VA Resi Sch-1",
#                "RevenueClass":"",
#                "ServicePointId":"7003208876",
#                "ServicePointSpecialUse":"",
#                "SpecialContractDemand":"",
#                "SvcAddrCardinalDir":"",
#                "SvcAddrCity":"CHARLOTTESVILLE",
#                "SvcAddrCountry":"US",
#                "SvcAddrDirSuffix":"",
#                "SvcAddrHouse":"1001",
#                "SvcAddrHouseMod":"",
#                "SvcAddrModifier":"",
#                "SvcAddrSt":"VA",
#                "SvcAddrStreetName":"FERN CT",
#                "SvcAddrStreetSuffix":"",
#                "SvcAddrZip":"22901",
#                "SvcAddrZipSuffix":"4001",
#                "TerminalId":"",
#                "ThirdPartyAmount":"0.000",
#                "TownCode":"8100",
#                "Contract":"",
#                "UserId":"",
#                "MailingAddress":{
#                   "__metadata":{
#                      "type":"ZISU_UMC_DSM_SRV.ZContractAccMaintMailAdress"
#                   },
#                   "CareOf":"",
#                   "City":"CHARLOTTESVILLE",
#                   "Country":"US",
#                   "HouseNum1":"1001",
#                   "HouseNum2":"",
#                   "InternationAddrx":"",
#                   "Location":"",
#                   "MailingaddrType":"ST",
#                   "PoBoxAdress":"",
#                   "Region":"VA",
#                   "Street":"FERN CT",
#                   "ZipCode":"22901-4001",
#                   "InternationAddr":{
#                      "__metadata":{
#                         "type":"ZISU_UMC_DSM_SRV.ZmailingAddr"
#                      },
#                      "Line1":"",
#                      "Line2":"",
#                      "Line3":"",
#                      "Line4":"",
#                      "Line5":"",
#                      "Line6":""
#                   }
#                }
#             },
#             "SearchType":"",
#             "InternetFunctionCode":"RETRACCT",
#             "UserId":"",
#             "CallingApplication":"",
#             "QuantityRowsRequested":0,
#             "AreaCode":"",
#             "PhoneNumber":"",
#             "Email":"",
#             "OfficeCode":"",
#             "TownCode":"",
#             "CustomerFirstName":"",
#             "CustomerMidName":"",
#             "CustomerLastName":"",
#             "CorporateName":"",
#             "HouseNumber":"",
#             "HouseNumberMod":"",
#             "CardinalDirection":"",
#             "StreetName":"",
#             "StreetType":"",
#             "DirectionSuffix":"",
#             "AddressModifier":"",
#             "City":"",
#             "State":"",
#             "Zip":"",
#             "Meter":"",
#             "Premise":"",
#             "FederalTaxId":"",
#             "SSN":"",
#             "Pin":"",
#             "BusinessPartner":"",
#             "BillAccount":"9714010007",
#             "ActiveBaOnly":"",
#             "ServiceAccountsOnly":"",
#             "InternetReturnCode":"S",
#             "ReturnMessageText":"Business Account details retrived successfully!",
#             "ResultCode":"00",
#             "ErrorCode":"",
#             "ActiveTimeStamp":"/Date(1672174552000)/",
#             "MoreData":"N",
#             "RowsReturned":1,
#             "ZAcctSearchNav":{
#                "results":[
                  
#                ]
#             },
#             "ZRetrContractsNav":{
#                "__deferred":{
#                   "uri":"http://ccapimqa.dominionnet.com:8443/sap/opu/odata/sap/ZISU_UMC_DSM_SRV/ZAcctSearchAndRetrieveSet('RETRACCT')/ZRetrContractsNav"
#                }
#             }
#          }
#       ]
#    }
# }
    

#2 
# {
#    "d":{
#       "results":[
#          {
#             "__metadata":{
#                "id":"http://ccapimqa.dominionnet.com:8443/sap/opu/odata/sap/ZISU_UMC_DSM_SRV/ZAcctSearchAndRetrieveSet(\\'RETRACCT\\')",
#                "uri":"http://ccapimqa.dominionnet.com:8443/sap/opu/odata/sap/ZISU_UMC_DSM_SRV/ZAcctSearchAndRetrieveSet(\\'RETRACCT\\')",
#                "type":"ZISU_UMC_DSM_SRV.ZAcctSearchAndRetrieve"
#             },
#             "RETRACCTData":{
#                "__metadata":{
#                   "type":"ZISU_UMC_DSM_SRV.RetrAcctData"
#                },
#                "AccountClass":"Z001",
#                "AccountCloseDate":null,
#                "AccountRepFlag":"",
#                "AccountRepName":"",
#                "AccountActive":"Y",
#                "AccountType":"MM",
#                "AcctOpenDate":"\\/Date(1660953600000)\\/",
#                "ActivityTimestamp":"\\/Date(1672168317000)\\/",
#                "AdditionalAddressInfo":"",
#                "AlternateRate":"",
#                "AltMailAddrSeq":"",
#                "AMIIndicator":"Y",
#                "ApplicationType":"IN",
#                "BillAccountStatusCode":"A",
#                "BillCycle":"16",
#                "CodeNpso":"0",
#                "CollectionAgencyStatus":"",
#                "CurrentConversationId":"",
#                "CustomerId":"1100298105",
#                "CustomerName1":"CLAUDIA J MCCANN",
#                "CustomerName2":"",
#                "CustomerName3":"",
#                "CustomerName4":"",
#                "CustomerName5":"",
#                "CustomerPin1":"",
#                "CustomerPin2":"",
#                "CustomerPin3":"",
#                "CustomerPin4":"",
#                "CustomerPin5":"",
#                "CustomerSsn1":"4564",
#                "CustomerSsn2":"",
#                "CustomerSsn3":"",
#                "CustomerSsn4":"",
#                "CustomerSsn5":"",
#                "DateEndMm":"",
#                "DateEndYyyy":"",
#                "DateStartMm":"",
#                "DateStartYyyy":"",
#                "DelinquencyIndicator":"N",
#                "DisconnectExpireDate":null,
#                "FederalTaxId":"",
#                "InternetUserId":"",
#                "IVREligIndicator":"Y",
#                "MailAddrCity":"CHARLOTTESVILLE",
#                "MailAddrDateEffective":null,
#                "MailAddrDateTerm":null,
#                "MailAddrDirection":"",
#                "MailAddrDirSuffix":"",
#                "MailAddrHouseMod":"",
#                "MailAddrHouseNumber":"1001",
#                "MailAddrModifier":"",
#                "MailAddrName":"",
#                "MailAddrNonStd1":"",
#                "MailAddrNonStd2":"",
#                "MailAddrNonStd3":"",
#                "MailAddrState":"VA",
#                "MailAddrStreetName":"FERN CT",
#                "MailAddrStreetType":"",
#                "MailAddrZipcode":"22901",
#                "MailAddrZipSuffix":"4001",
#                "MeterIdNumber":"000000000260633362",
#                "NameCustFirst":"CLAUDIA",
#                "NameCustLast":"MCCANN",
#                "NameCustMiddle":"J",
#                "Password":"",
#                "PasswordIndicator":"N",
#                "Phone":"434-296-5296",
#                "PhoneAreaCode":"434",
#                "PhoneExt":"",
#                "PhoneNumberSeq":"",
#                "PremiseId":"971564200",
#                "RateCode":"VR-1",
#                "RateCodeDescription":"VA Resi Sch-1",
#                "RevenueClass":"",
#                "ServicePointId":"7003208876",
#                "ServicePointSpecialUse":"",
#                "SpecialContractDemand":"",
#                "SvcAddrCardinalDir":"",
#                "SvcAddrCity":"CHARLOTTESVILLE",
#                "SvcAddrCountry":"US",
#                "SvcAddrDirSuffix":"",
#                "SvcAddrHouse":"1001",
#                "SvcAddrHouseMod":"",
#                "SvcAddrModifier":"",
#                "SvcAddrSt":"VA",
#                "SvcAddrStreetName":"FERN CT",
#                "SvcAddrStreetSuffix":"",
#                "SvcAddrZip":"22901",
#                "SvcAddrZipSuffix":"4001",
#                "TerminalId":"",
#                "ThirdPartyAmount":"0.000",
#                "TownCode":"8100",
#                "Contract":"",
#                "UserId":"",
#                "MailingAddress":{
#                   "__metadata":{
#                      "type":"ZISU_UMC_DSM_SRV.ZContractAccMaintMailAdress"
#                   },
#                   "CareOf":"",
#                   "City":"CHARLOTTESVILLE",
#                   "Country":"US",
#                   "HouseNum1":"1001",
#                   "HouseNum2":"",
#                   "InternationAddrx":"",
#                   "Location":"",
#                   "MailingaddrType":"ST",
#                   "PoBoxAdress":"",
#                   "Region":"VA",
#                   "Street":"FERN CT",
#                   "ZipCode":"22901-4001",
#                   "InternationAddr":{
#                      "__metadata":{
#                         "type":"ZISU_UMC_DSM_SRV.ZmailingAddr"
#                      },
#                      "Line1":"",
#                      "Line2":"",
#                      "Line3":"",
#                      "Line4":"",
#                      "Line5":"",
#                      "Line6":""
#                   }
#                }
#             },
#             "SearchType":"",
#             "InternetFunctionCode":"RETRACCT",
#             "UserId":"",
#             "CallingApplication":"",
#             "QuantityRowsRequested":0,
#             "AreaCode":"",
#             "PhoneNumber":"",
#             "Email":"",
#             "OfficeCode":"",
#             "TownCode":"",
#             "CustomerFirstName":"",
#             "CustomerMidName":"",
#             "CustomerLastName":"",
#             "CorporateName":"",
#             "HouseNumber":"",
#             "HouseNumberMod":"",
#             "CardinalDirection":"",
#             "StreetName":"",
#             "StreetType":"",
#             "DirectionSuffix":"",
#             "AddressModifier":"",
#             "City":"",
#             "State":"",
#             "Zip":"",
#             "Meter":"",
#             "Premise":"",
#             "FederalTaxId":"",
#             "SSN":"",
#             "Pin":"",
#             "BusinessPartner":"",
#             "BillAccount":"9714010007",
#             "ActiveBaOnly":"",
#             "ServiceAccountsOnly":"",
#             "InternetReturnCode":"S",
#             "ReturnMessageText":"Business Account details retrived successfully!",
#             "ResultCode":"00",
#             "ErrorCode":"",
#             "ActiveTimeStamp":"\\/Date(1672168317000)\\/",
#             "MoreData":"N",
#             "RowsReturned":1,
#             "ZAcctSearchNav":{
#                "results":[
                  
#                ]
#             },
#             "ZRetrContractsNav":{
#                "__deferred":{
#                   "uri":"http://ccapimqa.dominionnet.com:8443/sap/opu/odata/sap/ZISU_UMC_DSM_SRV/ZAcctSearchAndRetrieveSet(\\'RETRACCT\\')/ZRetrContractsNav"
#                }
#             }
#          }
#       ]
#    }
# }


#3
# {
#    "d":{
#       "results":[
#          {
#             "__metadata":{
#                "id":"http://ccapimqa.dominionnet.com:8443/sap/opu/odata/sap/ZISU_UMC_DSM_SRV/ZAcctSearchAndRetrieveSet(\\'ACCTSRCH\\')",
#                "uri":"http://ccapimqa.dominionnet.com:8443/sap/opu/odata/sap/ZISU_UMC_DSM_SRV/ZAcctSearchAndRetrieveSet(\\'ACCTSRCH\\')",
#                "type":"ZISU_UMC_DSM_SRV.ZAcctSearchAndRetrieve"
#             },
#             "RETRACCTData":{
#                "__metadata":{
#                   "type":"ZISU_UMC_DSM_SRV.RetrAcctData"
#                },
#                "AccountClass":"",
#                "AccountCloseDate":null,
#                "AccountRepFlag":"",
#                "AccountRepName":"",
#                "AccountActive":"",
#                "AccountType":"",
#                "AcctOpenDate":null,
#                "ActivityTimestamp":null,
#                "AdditionalAddressInfo":"",
#                "AlternateRate":"",
#                "AltMailAddrSeq":"",
#                "AMIIndicator":"",
#                "ApplicationType":"",
#                "BillAccountStatusCode":"",
#                "BillCycle":"",
#                "CodeNpso":"",
#                "CollectionAgencyStatus":"",
#                "CurrentConversationId":"",
#                "CustomerId":"",
#                "CustomerName1":"",
#                "CustomerName2":"",
#                "CustomerName3":"",
#                "CustomerName4":"",
#                "CustomerName5":"",
#                "CustomerPin1":"",
#                "CustomerPin2":"",
#                "CustomerPin3":"",
#                "CustomerPin4":"",
#                "CustomerPin5":"",
#                "CustomerSsn1":"",
#                "CustomerSsn2":"",
#                "CustomerSsn3":"",
#                "CustomerSsn4":"",
#                "CustomerSsn5":"",
#                "DateEndMm":"",
#                "DateEndYyyy":"",
#                "DateStartMm":"",
#                "DateStartYyyy":"",
#                "DelinquencyIndicator":"",
#                "DisconnectExpireDate":null,
#                "FederalTaxId":"",
#                "InternetUserId":"",
#                "IVREligIndicator":"",
#                "MailAddrCity":"",
#                "MailAddrDateEffective":null,
#                "MailAddrDateTerm":null,
#                "MailAddrDirection":"",
#                "MailAddrDirSuffix":"",
#                "MailAddrHouseMod":"",
#                "MailAddrHouseNumber":"",
#                "MailAddrModifier":"",
#                "MailAddrName":"",
#                "MailAddrNonStd1":"",
#                "MailAddrNonStd2":"",
#                "MailAddrNonStd3":"",
#                "MailAddrState":"",
#                "MailAddrStreetName":"",
#                "MailAddrStreetType":"",
#                "MailAddrZipcode":"",
#                "MailAddrZipSuffix":"",
#                "MeterIdNumber":"",
#                "NameCustFirst":"",
#                "NameCustLast":"",
#                "NameCustMiddle":"",
#                "Password":"",
#                "PasswordIndicator":"",
#                "Phone":"",
#                "PhoneAreaCode":"",
#                "PhoneExt":"",
#                "PhoneNumberSeq":"",
#                "PremiseId":"",
#                "RateCode":"",
#                "RateCodeDescription":"",
#                "RevenueClass":"",
#                "ServicePointId":"",
#                "ServicePointSpecialUse":"",
#                "SpecialContractDemand":"",
#                "SvcAddrCardinalDir":"",
#                "SvcAddrCity":"",
#                "SvcAddrCountry":"",
#                "SvcAddrDirSuffix":"",
#                "SvcAddrHouse":"",
#                "SvcAddrHouseMod":"",
#                "SvcAddrModifier":"",
#                "SvcAddrSt":"",
#                "SvcAddrStreetName":"",
#                "SvcAddrStreetSuffix":"",
#                "SvcAddrZip":"",
#                "SvcAddrZipSuffix":"",
#                "TerminalId":"",
#                "ThirdPartyAmount":"0.000",
#                "TownCode":"",
#                "Contract":"",
#                "UserId":"",
#                "MailingAddress":{
#                   "__metadata":{
#                      "type":"ZISU_UMC_DSM_SRV.ZContractAccMaintMailAdress"
#                   },
#                   "CareOf":"",
#                   "City":"",
#                   "Country":"",
#                   "HouseNum1":"",
#                   "HouseNum2":"",
#                   "InternationAddrx":"",
#                   "Location":"",
#                   "MailingaddrType":"",
#                   "PoBoxAdress":"",
#                   "Region":"",
#                   "Street":"",
#                   "ZipCode":"",
#                   "InternationAddr":{
#                      "__metadata":{
#                         "type":"ZISU_UMC_DSM_SRV.ZmailingAddr"
#                      },
#                      "Line1":"",
#                      "Line2":"",
#                      "Line3":"",
#                      "Line4":"",
#                      "Line5":"",
#                      "Line6":""
#                   }
#                }
#             },
#             "SearchType":"",
#             "InternetFunctionCode":"ACCTSRCH",
#             "UserId":"",
#             "CallingApplication":"",
#             "QuantityRowsRequested":200,
#             "AreaCode":"",
#             "PhoneNumber":"",
#             "Email":"",
#             "OfficeCode":"",
#             "TownCode":"",
#             "CustomerFirstName":"David",
#             "CustomerMidName":"",
#             "CustomerLastName":"Ashley",
#             "CorporateName":"",
#             "HouseNumber":"",
#             "HouseNumberMod":"",
#             "CardinalDirection":"",
#             "StreetName":"",
#             "StreetType":"",
#             "DirectionSuffix":"",
#             "AddressModifier":"",
#             "City":"",
#             "State":"",
#             "Zip":"",
#             "Meter":"",
#             "Premise":"",
#             "FederalTaxId":"",
#             "SSN":"",
#             "Pin":"",
#             "BusinessPartner":"",
#             "BillAccount":"",
#             "ActiveBaOnly":"",
#             "ServiceAccountsOnly":"",
#             "InternetReturnCode":"U",
#             "ReturnMessageText":"Invalid Calling Acitivty!Missing Inputs Y or N",
#             "ResultCode":"02",
#             "ErrorCode":"A0015",
#             "ActiveTimeStamp":null,
#             "MoreData":"",
#             "RowsReturned":0,
#             "ZAcctSearchNav":{
#                "results":[
                  
#                ]
#             },
#             "ZRetrContractsNav":{
#                "__deferred":{
#                   "uri":"http://ccapimqa.dominionnet.com:8443/sap/opu/odata/sap/ZISU_UMC_DSM_SRV/ZAcctSearchAndRetrieveSet(\\'ACCTSRCH\\')/ZRetrContractsNav"
#                }
#             }
#          }
#       ]
#    }
# }