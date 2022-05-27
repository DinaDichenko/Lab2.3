#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = input("Enter the world: ")
    g = 0
    i = 0
    j = 1

    while i < len(s):
        while j < len(s):
            if i != j and s[i] == s[j]:
                s = s[:j] + s[j + 1:]
                i = 0
                j = 1
            j += 1
        i += 1
        j = 0
    print(s)
