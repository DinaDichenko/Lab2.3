#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = input("Enter a suggestion: ")
    count = 0

    if s.count(',') == 0:
        print("There are no commas in the sentence")

    else:
        for i in range(0, len(s)):
            if s[i] == 'н':
                count += 1
            if s[i] == ',':
                break

    print(count)
