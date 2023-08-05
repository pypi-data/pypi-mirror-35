# encoding: UTF-8

from __future__ import absolute_import
from vnpy.trader import vtConstant
from .shzdGateway import ShzdGateway

gatewayClass = ShzdGateway
gatewayName = 'SHZD'
gatewayDisplayName = u'直达'
gatewayType = vtConstant.GATEWAYTYPE_INTERNATIONAL
gatewayQryEnabled = True

