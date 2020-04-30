# feye_detection.FilesApi

All URIs are relative to *https://feapi.marketplace.apps.fireeye.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_file**](FilesApi.md#post_file) | **POST** /files | Submit a single file for analysis


# **post_file**
> object post_file(file)

Submit a single file for analysis

This endpoint submits a binary file for analysis. **Your file must be less than 32MB.**

### Example

* Api Key Authentication (FireEyeAPIKey):
```python
from __future__ import print_function
import time
import feye_detection
from feye_detection.rest import ApiException
from pprint import pprint
configuration = feye_detection.Configuration()
# Configure API key authorization: FireEyeAPIKey
configuration.api_key['feye-auth-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['feye-auth-key'] = 'Bearer'

# Defining host is optional and default to https://feapi.marketplace.apps.fireeye.com
configuration.host = "https://feapi.marketplace.apps.fireeye.com"
# Create an instance of the API class
api_instance = feye_detection.FilesApi(feye_detection.ApiClient(configuration))
file = '/path/to/file' # file | This is the binary file that you want to submit for malware analysis.

try:
    # Submit a single file for analysis
    api_response = api_instance.post_file(file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->post_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| This is the binary file that you want to submit for malware analysis. | 

### Return type

**object**

### Authorization

[FireEyeAPIKey](../README.md#FireEyeAPIKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**413** | Request Entity Too Large -- The file you provided was more than 32MB. |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
