# encoding: UTF-8

from __future__ import absolute_import
from vnpy.trader import vtConstant
from .cshshlpGateway import CshshlpGateway

gatewayClass = CshshlpGateway
gatewayName = 'CSHSHLP'
gatewayDisplayName = u'中信期权'
gatewayType = vtConstant.GATEWAYTYPE_EQUITY
gatewayQryEnabled = True

