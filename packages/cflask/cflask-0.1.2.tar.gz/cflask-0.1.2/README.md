# cFlask
Simple wrapper to Flask for simple versioned APIs. Supported on Python 2.7 and Python 3.2 and greater.

## Example
```
class _ExampleCFlask(cFlask):
    '''
    example of a simple cFlask server.
    '''
    def handleV1(self, info):
        '''
        handles v1. If the passed info is "False" return False.
            Returning False will lead to the default handler getting called.
        '''
        if info == 'False':
            return False

        return 'V1: %s' % info

    def handleV2(self, info):
        '''
        handles v2
        '''
        return 'V2: %s' % info

    def handleVDefault(self, fullPath):
        '''
        handles unversioned / default requests
        '''
        return 'VDefault: %s' % fullPath
```

### What Happens When The URL Is Called:
- example.com/anything/else -> handleVDefault('anything/else') is called
- example.com/1/callingv1 -> handleV1('callingv1') is called
- example.com/2/callingv2 -> handleV2('callingv2') is called
- example.com/3/callingv3 -> handlerVDefault('3/callingv3') is called since there isn't a handler for v3

### How to Install
```
pip install cflask
```

