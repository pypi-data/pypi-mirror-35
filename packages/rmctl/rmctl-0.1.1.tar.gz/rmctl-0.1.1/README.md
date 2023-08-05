# rmctl
A simple  controller for Broadlink IR device

## Installation
+ Manually connect for broadlink device to wifi
+ pip install rmctl
 ## Using
 + Make a Device File    
      + Use -m or --make_device option, -d option is device file name
      + ex:) rmctl -m -d myroom
 + Learn a command IR data
      + Use -l or --learn option, -c option is command name
      + ex:) rmctl -l -d myroom -c light_on
      + Then send IR data to Broadlink device from your remote controller 
 + Send a coomand
      + Use -s or --send option 
      + ex:) rmctl -s -d myroom -c light_on
 
