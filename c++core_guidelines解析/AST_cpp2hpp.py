'''
适合直接写cpp的懒人,单元测试需要.h
'''

#TODO: argparse infile outfile
#TODO: meson test auto deduce hppfile from samename.cpp
infile = r'/home/pi/c23tests/t2/test2.cpp'
outfile = r"ttttt.hpp"

import sys

from  clang.cindex import CursorKind
import clang.cindex as CX
from  clang.cindex import TypeKind
from  clang.cindex import Config
from  clang.cindex import Index
from  clang.cindex import TranslationUnit

def preorder_travers_AST(cursor):
    #先序遍历
    for cur in cursor.get_children():
        print(cur.spelling,'\t',cur.kind,'\t')

        # print(' ')
        # time.sleep(1)
        preorder_travers_AST(cur)



def find_typerefs(cursor):

    """通过识别cursorKind 以及TypeKind 来进行语法单元的识别 """
    for cur in cursor.get_children():
        #print(cur.kind)
        if cur.kind==CursorKind.CLASS_DECL\
            and "test2.cpp" in str(cur.extent):
            print(cur.displayname,'\t',str(cur.kind).removeprefix("CursorKind."),'\t',
                  )
            print('line ',cur.location.line,'\t','Column ',
                  cur.location.column)
            #print(iter_cursor_content(cur))
            print(list(cur.get_tokens())[0].spelling)
            print('==========--------------')
            for cur_sub in cur.get_children():
                print(cur_sub.spelling,'\t',str(cur_sub.kind).removeprefix("CursorKind."),'\t')

            pass
            # print(cur.spelling,'\t',cur.kind,'\t')
            # print(iter_cursor_content(cur))
            # #do something
            # 
            #     if cur_sub.kind==CursorKind.CALL_EXPR:
            #         #do something
            #         pass
            #         #分析函数定义调用的其他函数
            #         #print(cur.spelling,'\t',cur.kind,'\t')


        # elif cur.kind ==CursorKind.FIELD_DECL\
        #     and "test2.cpp" in str(cur.extent):
        #     print(cur.displayname,'\t',cur.kind,'\t',
        #           )
        #     print('line ',cur.location.line,'\t','Column ',
        #           cur.location.column)
        #     print(iter_cursor_content(cur))
        #     print('-')
        #     pass


        elif cur.type.kind ==TypeKind.UCHAR:
            #print(cur.spelling,'\t',cur.kind,'\t')
            #do somethin
            pass

        # elif cur.kind in (CursorKind.MACRO_INSTANTIATION,CursorKind.MACRO_DEFINITION) \
        #     and "test2.cpp" in str(cur.extent) :
        #     print(cur.displayname,'\t',cur.kind,'\t',
        #           )
        #     print(cur.location.line,'\t',
        #           cur.location.column)
        #     print(iter_cursor_content(cur))
        #     print('-')



        find_typerefs(cur)





def traverse(node: CX.Cursor, prefix="", is_last=True):
    branch = "└──" if is_last else "├──"

    text = f"{str(node.kind).removeprefix('CursorKind.')}: {node.spelling}"

    if node.kind == CX.CursorKind.INTEGER_LITERAL:
        if len(list(node.get_tokens()))!=0:
            value = list(node.get_tokens())[0].spelling
        else:
            value =""
        text = f"{text}{value}"
    if "test2" in str(node.extent):
        print(f"{prefix}{branch} {text}")
        print(f"{prefix + '   '}{iter_cursor_content(node)}")
    new_prefix = prefix + ("    " if is_last else "│   ")
    children = list(node.get_children())

    # 遍历子节点
    for child in children:

        traverse(child, new_prefix, child is children[-1])



def global_param_count_get():
    global param_count
    return param_count
def global_param_count_set(value:int):
    global param_count
    param_count = value

def global_param_count_clear():
    global param_count
    param_count=0



def traverse_interface_assamble(node: CX.Cursor, prefix="", is_last=True,to_closeBprt=False,father_type=0):
    """ AST提取class ，function 函数头 """
    global _file_name
    #branch = "    " if is_last else "├──"

    _to_close_big_paranthe = to_closeBprt
    _father_type = node.kind
    _param_dec_count = global_param_count_get()

    if _file_name in str(node.extent):# 在指定文件内，通常为cpp
        if node.kind == CursorKind.INCLUSION_DIRECTIVE:
            output_list.append(iter_cursor_content(node))
        elif node.kind == CursorKind.CLASS_DECL:#修建{前
            output_list.append(f"{prefix + '    '}{iter_cursor_content(node).split('{',1)[0]}{'{'}")
            #_to_close_big_paranthe= True

            pass
        elif node.kind == CursorKind.CXX_ACCESS_SPEC_DECL:#private public
            output_list.append(f"{prefix + '    '}{iter_cursor_content(node)}")
            pass
        elif node.kind == CursorKind.FIELD_DECL:
            output_list.append(f"{prefix + '    '}{iter_cursor_content(node)}{';'}")
            pass
        elif node.kind == CursorKind.CONSTRUCTOR:#修剪
            output_list.append(f"{prefix + '    '}{iter_cursor_content(node).split('(',1)[0]}{'('}")#切括号前，修剪默认值
            pass

        elif node.kind == CursorKind.PARM_DECL:#修剪 =后默认值
            global_param_count_set(_param_dec_count+1)
            _str = iter_cursor_content(node)
            #output_list.append(_str)
            #output_list.append(f"                    _param_dec_count is {_param_dec_count}")
            if '=' in _str:
                output_list.append(f"{prefix + '    '}{('',',')[_param_dec_count>0]}{_str.split('=',1)[0]}")
            else:
                output_list.append(f"{prefix + '    '}{('',',')[_param_dec_count>0]}{_str}")

            pass
        elif node.kind == CursorKind.DESTRUCTOR:#修剪 )后内容+{}
            output_list.append(f"{prefix + '    '}{iter_cursor_content(node).split(')',1)[0]}{'){}'}")#切括号前，修剪默认值
            pass

        elif node.kind == CursorKind.CXX_METHOD:#修剪 )后内容 +{}
            output_list.append(f"{prefix + '    '}{iter_cursor_content(node).split('(',1)[0]}{'('}")#切括号前，修剪默认值
            pass


        elif node.kind == CursorKind.FUNCTION_DECL:#修剪 )后内容 +{}，如果函数名为main，均不要
            output_list.append(f"{prefix + '    '}{iter_cursor_content(node).split('(',1)[0]}{'('}")#切括号前，修剪默认值
            pass



        else:
            text = f"{str(node.kind).removeprefix('CursorKind.')}: {node.spelling}"

            #output_list.append(f"{prefix}{branch} {text}")
            #output_list.append(f"{prefix + '   '}{iter_cursor_content(node)}")

        #闭合括号，完成声明
        #清空计数器
        if is_last:
 
            if father_type ==CursorKind.CONSTRUCTOR :#闭合class constructor
                output_list.append(f"{prefix}{'){};'}")
                global_param_count_clear()
                if _to_close_big_paranthe==True:
                    output_list.append(f"{prefix[:-4]}{'};'}")#闭合class 

            elif father_type ==CursorKind.CXX_METHOD :#闭合 class method
                output_list.append(f"{prefix}{'){};'}")
                global_param_count_clear()
                if _to_close_big_paranthe==True:
                    output_list.append(f"{prefix[:-4]}{'};'}")#闭合class

            elif father_type ==CursorKind.DESTRUCTOR :#闭合class destructor
                if _to_close_big_paranthe==True:
                    output_list.append(f"{prefix[:-4]}{'};'}")#闭合class
               


            elif father_type ==CursorKind.FUNCTION_DECL :#闭合constructor
                output_list.append(f"{prefix + '   '}{'){};'}")
                global_param_count_clear()



            elif father_type == CursorKind.CLASS_DECL:
                """当父级为class decl,iter到最后,需推迟至最后一个class成员闭合后,再闭合class本身
                """
                #output_list.append(f"{prefix + '   '}  {'};'}")
                
                _to_close_big_paranthe=True#推迟闭合class标志
                



        
    #new_prefix = prefix + ("    " if is_last else "│   ")
    new_prefix = prefix + ("    ")
    children = list(node.get_children())

    # 遍历子节点


            
    for child in children:
        #
        
        traverse_interface_assamble(child, new_prefix, child is children[-1],_to_close_big_paranthe,_father_type)






def iter_cursor_content(cur):
    cursor_content=""
    for token in cur.get_tokens():
        str_token = token.spelling+" "
        cursor_content = cursor_content+str_token
    return cursor_content


if __name__ == '__main__':
    _file_name = "test2.cpp"
    file_path = infile

    index =Index.create()
    tu = index.parse(file_path,args=["-std=c++17"],
                     options=TranslationUnit.PARSE_DETAILED_PROCESSING_RECORD
                     )#args 选项 _DUSE_LIBPNG1
    print(f"Translation unit: {tu.spelling}")
    print('===============')

    AST_root_node = tu.cursor
    #print(AST_root_node)
    #find_typerefs(tu.cursor,"Rpi5Gpios")
    #preorder_travers_AST(AST_root_node)
    
    
    #find_typerefs(AST_root_node)


    #initial numbers
    global_param_count_clear()
    

    output_list = []
    traverse_interface_assamble(tu.cursor)
    

    #修复, 移动到上一行尾部
    for index,line in enumerate(output_list):
        if line.strip().startswith(','):
            output_list[index-1]=output_list[index-1]+','
            output_list[index]=line.replace(',','')



    #output_list3 = []
    #输出文件
    f=open(outfile,'w')
    for i in output_list:
        #修正格式
        i = i.replace('< ','<')
        i = i.replace(' >','>')
        i = i.replace('# ','#')
        i = i.replace(' :',':')
        i = i.replace(': ',':')
        i = i.replace(' *','*')
        i = i.replace(' &','&')
        i = i.replace('~ ','~')
        i = i.replace(' ;',';')
        i = i.replace(' (','(')

        i = i.replace(' ,',',')


        print(i)
        #output_list3.append(i)
        f.write(i+'\n')
    f.close()
    






