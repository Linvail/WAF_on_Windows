#!/usr/bin/env python
 
APPNAME = 'waf-practice'
VERSION = '0.1'
 
top = '.'
out = 'build'
 
def options(ctx):
    ctx.load('compiler_cxx')
     
def configure(ctx):
    ctx.load('compiler_cxx')
 
def build(ctx):
    print( ctx.out_dir + "/bin" )
    ctx.recurse('Lib')
    print( ctx.env['INCLUDES'])
    ctx.recurse('Main')
    
