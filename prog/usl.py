#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = input("Enter the 1-st world: ")
    a = input("Enter the 2-nd world: ")

    i = 0
    while i < len(s):
        j = 0
        while j < len(a):
            if s[i] == a[j]:
                k = 0
                while k < len(s):
                    if s[i] == s[k] and i != k:
                        s = s[:k] + s[k + 1:]
                        k = 0
                    k += 1
                s = s[:i] + s[i + 1:]
                k = 0
                while k < len(a):
                    if a[j] == a[k] and j != k:
                        a = a[:k] + a[k + 1:]
                        k = 0
                    k += 1
                a = a[:j] + a[j + 1:]
                i = 0
                j = 0
            j += 1
        i += 1
    print(s + a)



