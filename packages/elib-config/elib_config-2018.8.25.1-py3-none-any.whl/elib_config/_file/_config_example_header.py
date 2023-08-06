# coding=utf-8
"""
Header template for the example config file
"""

# flake8: noqa

HEADER = r'''This is an example configuration file for {app_name}.

Version: {app_version}.

WARNING: this example file will be overwritten every time {app_name} starts. Make sure to save your work under another 
name!

It must be renamed to "{config_file_path}" in order to come into effect.

The configuration file follows the YAML format.

Mandatory and optional values
=============================

Some values are mandatory, some aren't. Mandatory values are marked with the "MANDATORY VALUE" tag. If mandatory values
are missing, {app_name} will not start.

Note that, while not necessary for {app_name} to function, failing to provide non-mandatory may prevent non-essential 
modules to start. This will be indicated as such in the log and in the console.

Assigning values to keys
========================

A key is a name followed by a colon. For example: "key:". The value is what follows the colon. For example, here's
how to assign the value "some_value" to the key "some_key:

    some_key: some_value
    
Indentation
===========

Indentation matters in YAML. Keys are grouped under a common parent. For example, a set of keys "key1", "key2" and 
"key3" belonging to a group "Group", with their dummy values, would look like:

group:
  key1: dummy
  key2: dummy
  key3: dummy
  
Flat keys
=========
  
In addition to this grouping format, keys and values can also be expressed in a flat manner. This example would result
in the same configuration as the one above:

group{sep}key1: dummy
group{sep}key2: dummy
group{sep}key3: dummy

The different levels are separated with: "{sep}". 

OS environment
==============

All configuration values may also be given using the OS environment instead of the config file. However, 
the "{app_name}_" prefix must be added (this is to prevent any potential conflict with other application.

For example, the configuration "dummy_key: dummy_value" would be set in the OS environment using the variable
"setx {app_name}_DUMMY_KEY=dummy_value".

In the case of grouped key, a key that is expressed like this in YAML:

group1:
  group2:
    group3:
       dummy_key: dummy_value
       
would be translated into an OS environment value like this:
"setx {app_name}_GROUP1{sep}GROUP2{sep}GROUP3{sep}DUMMY_KEY=dummy_value"

Please not that all configuration key given using OS environment should be UPPER CASE.

Values types
=============
Value types will be checked at runtime.

Possible values are: 
    - string
        A string is simple text. To protect special characters such as numbers or newlines, use single quotes.
        example_key_1: this is a valid string
        example_key_2: 'this is also a valid string'
        example_key_3: 10 # this is NOT a string and will result in an error
        example_key_4: '10' # this is the correct way to use an integer as a string
        example_key_5: '\n' # this is the correct way to have a newline character as a string
        
        Multiline strings are simple to write. If you want to convert newlines into spaces, you can use the ">" marker.
        For example:
        example_key: >
          This is
          not
          a multi
          line
          string
          
        will result in "This is not a multi line string".
        
        If you want to preserve the new lines, use the "|" character:
        example_key: |
          This is
          a true
          multi line
          string
          
    - integer
        An integer is a number without decimals.
        
        example_integer_1: 1
        example_integer_1: -1
        example_integer_1: 1000
    
    - float
        A float is a number with decimals.
        
        example_float_1: 1.1
        example_float_2: 1.12345
        example_float_3: -1.12345
        
    - boolean
        A boolean is either "true" or "false".
        
        For example:
        dogs_are_awesome: true
        enough_boosters: false
        
        Note: despite the YAML specification, the only values accepted by {app_name} are "true" or "false". This is to 
        prevent type casting from confusing the end-user, when any non-empty string or positive integer would yield 
        "true".
        
    - list
        A list in YAML is expressed as multiple lines beginning with a dash. For example, a list of strings:
        strings:
          - string1
          - string2
          - 'string3'
          
        A list of integers:
        integers:
          - 1
          - 2
          - 3
          
        Note the indentation for each line under the main key.
'''
