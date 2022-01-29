#!/usr/bin/env python
# coding: utf-8

# In[41]:


class Calculate_Class:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        print('{0} + {1} = {2}\n'.format(self.first, self.second, result))
    def mul(self):
        result = self.first * self.second
        print('{0} * {1} = {2}\n'.format(self.first, self.second, result))
    def sub(self):
        result = self.first - self.second
        print('{0} - {1} = {2}\n'.format(self.first, self.second, result))
    def div(self):
        result = self.first / self.second
        print('{0} / {1} = {2}\n'.format(self.first, self.second, result))

