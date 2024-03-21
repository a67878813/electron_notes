project('hello-proj','cpp',
    version:'0.1',
    default_options:['warning_level=3','cpp_std=c++20'])

#libfmt = dependency('libfmt')

gtest_dep = dependency('gtest',main:true,required:false)
zdep = dependency('zlib',version:'>=1.2.8')
rpi5gpiodep=dependency('libgpiodcxx')
opencv4dep=dependency('opencv4')






#======opt dependency
opt_dep = dependency('somedep', required : false)
if opt_dep.found()
  # Do something.
else
  # Do something else.
endif


fmt_dep = dependency('fmt-10',required:false)
if not fmt_dep.found()
    fmt_proj= subproject('fmt')
    fmt_dep = fmt_proj.get_variable('fmt_dep')
endif



# opt dependency end


gtk3 = dependency('gtk+-3.0')
gtest = dependency('gtest')


#at meson ,we do NOT need t oadd any source headers to the list of sources.
e = executable('hello-example.e','test2.cpp',
                
                dependencies:[gtk3,gtest,zdep,
                rpi5gpiodep,opencv4dep,
                fmt_dep
                ])

e2 = executable('testprog.e','test.cc',dependencies:gtest_dep)

test('gtest tests',e2)