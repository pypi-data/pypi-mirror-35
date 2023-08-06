# -*- coding: utf-8 -*-
"""
:created on: 5-11-2017

:copyright: 
:author: leo
:contact:
"""

import logging
import re
import lxml.etree
from robot.libraries.XML import XML
from exception import TAFileException


class XmlHandler(object):
    """find and modify value in .xml file
    """
    def __init__(self):
        self._log = logging.getLogger(__name__)
        self._log.setLevel(logging.DEBUG)
        self._xml_parser = None
        self._xml_inst = None
        self._src_path = None
        self._save_path = None

    def setup(self, src_file, save_path, **kwargs):
        """src_file: the xml file you want parser
           save_path: where the xml file you want save after parser
        """
        self._src_path = src_file
        self._save_path = save_path
        self._xml_inst = XML()
        self._xml_parser = self._xml_inst.parse_xml(self._src_path)
        #lxml_parser = lxml.etree.ETCompatXMLParser()
        #self._lxml_parser = lxml.etree.parse(self._src_path)

    def teardown(self, **kwargs):
        """pair up the function setup
        """
        self._xml_inst.save_xml(self._xml_parser, self._save_path)

    def _get_child_absolute_node_by_xpath(self, current_node, x_path, name, node_index):
        elements = self._xml_inst.get_elements(current_node, x_path)
        element_atts_dict = {}
        for ele in elements:
            element_atts_dict[(self._xml_inst.get_element_attribute(ele, name))] = ele
        return self._xml_inst.get_element_attributes(element_atts_dict[sorted(element_atts_dict.keys())[int(node_index)]])[name]

    def _re_config_path(self, path):

        while True:
            ret = re.search(r'\[@\w+\="\S+"]\[@(\w+)="(\d)"\]', path)
            if ret:
                self._log.debug("ret group:%s", ret.groups())
                self._log.debug(path[:path.index('[@%s' % ret.group(1))])
                node_new = self._get_child_absolute_node_by_xpath(self._xml_parser,
                                                                  path[:path.index('[@%s' % ret.group(1))],
                                                                  ret.group(1), ret.group(2))
                self._log.debug("%s--%s", node_new, ret.groups())
                path = path.replace('%s="%s"' % (ret.groups()), '%s="%s"' % (ret.group(1), node_new))
                self._log.info("path:%s", path)
            else:
                return path

    def modify_node_text(self, *args):
        """arg should be like this: './/managedObject[@class="LNBTS"]/p[@name="actDLCAggr"]:false'
        """
        for each_node in args:
            ret_temp = each_node.split(":")
            node_path = ":".join(ret_temp[:-1])
            node_path = self._re_config_path(node_path)
            value = ret_temp[-1]
            self._log.debug("node_path:%s, value:%s", node_path, value)
            elements = self._xml_inst.get_elements(self._xml_parser, node_path)
            if not elements:
                raise TAFileException("not found any elements, please check your xpath!--%s." % node_path)
            for ele in elements:
                self._xml_inst.set_element_text(ele, value)

    def modify_node_attribute(self, *args):
        """arg should be like this: './/managedObject[@class\="LNCEL"]:@version\=TL16B'
        """
        for arg in args:
            node_path = self._re_config_path(arg.split(':@')[0])
            value = arg.split("=")[-1]
            attr_name = arg.split(':@')[-1].split('=')[0]
            try:
                self._xml_inst.set_elements_attribute(self._xml_parser, attr_name, value, node_path)
            except:
                self._log.debug("not found any elements, please check your xpath!--%s.", node_path)

    def add_node(self, *args):
        """arg should be like this: .//managedObject[@class="LNBTS"]:<list name="dlSectorBFWeightCusProf"><item>
           <p name="dlSectorBFWeightProfName">customized profile 1</p><p name="modulusOfWeighforAntGrp0">100</p>
           <p name="modulusOfWeighforAntGrp1">100</p><p name="modulusOfWeighforAntGrp2">100</p>
           <p name="modulusOfWeighforAntGrp3">100</p><p name="phaseOfWeighforAntGrp0">0</p>
           <p name="phaseOfWeighforAntGrp1">180</p><p name="phaseOfWeighforAntGrp2">180</p>
           <p name="phaseOfWeighforAntGrp3">180</p></item></list>
        """
        for each_node in args:
            if "cmData:" in each_node:
                ret_temp = each_node.split(":", 1)
            else:
                ret_temp = each_node.split(":")
            node_path = ":".join(ret_temp[:-1])
            value = ret_temp[-1]
            node_path = node_path.rstrip('/')
            node_path = self._re_config_path(node_path)
            self._log.debug("node_path:%s", node_path)
            elements = self._xml_inst.get_elements(self._xml_parser, node_path)
            if not elements:
                raise TAFileException("not found any elements, please check your xpath!--%s." % node_path)
            for ele in elements:
                self._xml_inst.add_element(ele, value)

    def delete_node(self, *args):
        """arg should be like this: .//managedObject[@class="LNCEL"][@distName="0"]/list/item/p[@name="dFpucchF1b"]
        """
        for each_node in args:
            each_node = self._re_config_path(each_node)
            self._log.debug("new_node_path:%s", each_node)
            elements = self._xml_inst.get_elements(self._xml_parser, each_node)
            if not elements:
                raise TAFileException("not found any elements, please check your xpath!--%s." % each_node)
            for ele in elements:
                self._xml_inst.remove_elements(self._xml_parser, each_node)

    def get_node_text(self, *args):
        """arg should be like this: .//managedObject[@class="LNCEL"][@distName="0"]/list/item/p[@name="dFpucchF1b"]
        """
        ret_list = []
        for each_node in args:
            each_node = self._re_config_path(each_node)
            try:
                elements = self._xml_inst.get_elements(self._xml_parser, each_node)
                if not elements:
                    raise TAFileException("not found any elements, please check your xpath!--%s." % each_node)
                for ele in elements:
                    ret_list.append(self._xml_inst.get_element_text(ele))
            except SyntaxError:
                print '****SyntaxError****'
                #root = self._lxml_parser.getroot()
                #elements = root.xpath(each_node)
                #if not elements:
                #    raise TAFileException("not found any elements, please check your xpath!--%s." % each_node)
                #for ele in elements:
                #    ret_list.append(ele.text)

        return ret_list

    def get_node_attribute(self, *args):
        """arg should be like this: .//managedObject[@class\="LNCEL"]:@version
        """
        ret_list = []
        for arg in args:
            attr_name = arg.split(':@')[-1]
            each_node = self._re_config_path(arg.split(':@')[0])
            elements = self._xml_inst.get_elements(self._xml_parser, each_node)
            if not elements:
                raise TAFileException("not found any elements, please check your xpath!--%s." % each_node)
            for ele in elements:
                ret_list.append(self._xml_inst.get_element_attribute(ele, attr_name))
        return ret_list


if __name__ == '__main__':
    pass
