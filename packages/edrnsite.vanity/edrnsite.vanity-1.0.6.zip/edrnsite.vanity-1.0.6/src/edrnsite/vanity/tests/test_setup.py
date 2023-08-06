# encoding: utf-8
#
# Copyright 2013–2016 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

'''Tests for the setup of Plone by this package.'''

from edrnsite.vanity.testing import EDRN_SITE_VANITY_INTEGRATION_TESTING
from Products.CMFCore.utils import getToolByName
from zope.component import getUtility
from plone.registry.interfaces import IRegistry
import unittest


class SetupTest(unittest.TestCase):
    layer = EDRN_SITE_VANITY_INTEGRATION_TESTING
    def setUp(self):
        super(SetupTest, self).setUp()
        self.portal = self.layer['portal']
    def testActions(self):
        '''Ensure our custom actions are available and in the correct order'''
        actionsTool = getToolByName(self.portal, 'portal_actions')
        self.failUnless('user' in actionsTool.keys(), 'no user actions installed')
        userActions = actionsTool['user'].keys()
        self.failUnless('vanity' in userActions, 'no vanity user action installed')
        vanity, logout = userActions.index('vanity'), userActions.index('logout')
        self.failUnless(vanity < logout, 'vanity action must appear above logout')
    def testRegistry(self):
        '''Check registry'''
        registry = getUtility(IRegistry)
        enable = registry['edrnsite.vanity.enable']
        self.failIf(enable, 'edrnsite.vanity.enable should default to False')
