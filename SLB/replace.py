import os
import sys
import fileinput
import pandas as pd
from itertools import islice


fileToSearch = 'TimeLog From 2022-08-01To 2022-08-04.csv'
header1= "Time,Channel-1,Channel-2,Channel-3,Channel-4,Channel-5,Channel-6,Channel-7,Channel-8,Channel-9,Channel-10,Channel-11,Channel-12,Channel-13,Channel-14,Channel-15,Channel-16,Channel-17,Channel-18,Channel-19,Channel-20,Channel-21,Channel-22,Channel-23,Channel-24,Channel-25,Channel-26,Channel-27,Channel-28,Channel-29,Channel-30,Channel-31,Channel-32,Channel-33,Channel-34,Channel-35,Channel-36,Channel-37,Channel-38,Channel-39,Channel-40,Channel-41,Channel-42,Channel-43,Channel-44,Channel-45,Channel-46,Channel-47,Channel-48,Channel-49,Channel-50,Channel-51,Channel-52,Channel-53,Channel-54,Channel-55,Channel-56,Channel-57,Channel-58,Channel-59,Channel-60,Channel-61,Channel-62,Channel-63,Channel-64,Channel-65,Channel-66,Channel-67,Channel-68,Channel-69,Channel-70,Channel-71,Channel-72,Channel-73,Channel-74,Channel-75,Channel-76,Channel-77,Channel-78,Channel-79,Channel-80,Channel-81,Channel-82,Channel-83,Channel-84,Channel-85,Channel-86,Channel-87,Channel-88,Channel-89,Channel-90,Channel-91,Channel-92,Channel-93,Channel-94,Channel-95,Channel-96,Channel-97,Channel-98,Channel-99,Channel-100,Channel-101,Channel-102,Channel-103,Channel-104,Channel-105,Channel-106,Channel-107,Channel-108,Channel-109,Channel-110,Channel-111,Channel-112,Channel-113,Channel-114,Channel-115,Channel-116,Channel-117,Channel-118,Channel-119,Channel-120,Channel-121,Channel-122,Channel-123,Channel-124,Channel-125,Channel-126,Channel-127,Channel-128,Channel-129,Channel-130,Channel-131,Channel-132,Channel-133,Channel-134,Channel-135,Channel-136,Channel-137,Channel-138,Channel-139,Channel-140,Channel-141,Channel-142,Channel-143,Channel-144,Channel-145,Channel-146,Channel-147,Channel-148,Channel-149,Channel-150,Channel-151,Channel-152,Channel-153,Channel-154,Channel-155,Channel-156,Channel-157,Channel-158,Channel-159,Channel-160,Channel-161,Channel-162,Channel-163,Channel-164,Channel-165,Channel-166,Channel-167,Channel-168,Channel-169,Channel-170,Channel-171,Channel-172,Channel-173,Channel-174,Channel-175,Channel-176,Channel-177,Channel-178,Channel-179,Channel-180,Channel-181,Channel-182,Channel-183,Channel-184,Channel-185,Channel-186,Channel-187,Channel-188,Channel-189,Channel-190,Channel-191,Channel-192,Channel-193,Channel-194,Channel-195,Channel-196,Channel-197,Channel-198,Channel-199,Channel-200,Channel-201,Channel-202,Channel-203,Channel-204,Channel-205,Channel-206,Channel-207,Channel-208,Channel-209,Channel-210,Channel-211,Channel-212,Channel-213,Channel-214,Channel-215,Channel-216,Channel-217,Channel-218,Channel-219,Channel-220,Channel-221,Channel-222,Channel-223,Channel-224,Channel-225,Channel-226,Channel-227,Channel-228,Channel-229,Channel-230,Channel-231,Channel-232,Channel-233,Channel-234,Channel-235,Channel-236,Channel-237,Channel-238,Channel-239,Channel-240,Channel-241,Channel-242,Channel-243,Channel-244,Channel-245,Channel-246,Channel-247,Channel-248,Channel-249,Channel-250,Channel-251,Channel-252,Channel-253,Channel-254,Channel-255,Channel-256,Channel-257,Channel-258,Channel-259,Channel-260,Channel-261,Channel-262,Channel-263,Channel-264,Channel-265,Channel-266,Channel-267,Channel-268,Channel-269,Channel-270,Channel-271,Channel-272,Channel-273,Channel-274,Channel-275,Channel-276,Channel-277,Channel-278,Channel-279,Channel-280,Channel-281,Channel-282,Channel-283,Channel-284,Channel-285,Channel-286,Channel-287,Channel-288,Channel-289,Channel-290,Channel-291,Channel-292,Channel-293,Channel-294,Channel-295,Channel-296,Channel-297,Channel-298,Channel-299,Channel-300"
header2= "s,Unit-1,Unit-2,Unit-3,Unit-4,Unit-5,Unit-6,Unit-7,Unit-8,Unit-9,Unit-10,Unit-11,Unit-12,Unit-13,Unit-14,Unit-15,Unit-16,Unit-17,Unit-18,Unit-19,Unit-20,Unit-21,Unit-22,Unit-23,Unit-24,Unit-25,Unit-26,Unit-27,Unit-28,Unit-29,Unit-30,Unit-31,Unit-32,Unit-33,Unit-34,Unit-35,Unit-36,Unit-37,Unit-38,Unit-39,Unit-40,Unit-41,Unit-42,Unit-43,Unit-44,Unit-45,Unit-46,Unit-47,Unit-48,Unit-49,Unit-50,Unit-51,Unit-52,Unit-53,Unit-54,Unit-55,Unit-56,Unit-57,Unit-58,Unit-59,Unit-60,Unit-61,Unit-62,Unit-63,Unit-64,Unit-65,Unit-66,Unit-67,Unit-68,Unit-69,Unit-70,Unit-71,Unit-72,Unit-73,Unit-74,Unit-75,Unit-76,Unit-77,Unit-78,Unit-79,Unit-80,Unit-81,Unit-82,Unit-83,Unit-84,Unit-85,Unit-86,Unit-87,Unit-88,Unit-89,Unit-90,Unit-91,Unit-92,Unit-93,Unit-94,Unit-95,Unit-96,Unit-97,Unit-98,Unit-99,Unit-100,Unit-101,Unit-102,Unit-103,Unit-104,Unit-105,Unit-106,Unit-107,Unit-108,Unit-109,Unit-110,Unit-111,Unit-112,Unit-113,Unit-114,Unit-115,Unit-116,Unit-117,Unit-118,Unit-119,Unit-120,Unit-121,Unit-122,Unit-123,Unit-124,Unit-125,Unit-126,Unit-127,Unit-128,Unit-129,Unit-130,Unit-131,Unit-132,Unit-133,Unit-134,Unit-135,Unit-136,Unit-137,Unit-138,Unit-139,Unit-140,Unit-141,Unit-142,Unit-143,Unit-144,Unit-145,Unit-146,Unit-147,Unit-148,Unit-149,Unit-150,Unit-151,Unit-152,Unit-153,Unit-154,Unit-155,Unit-156,Unit-157,Unit-158,Unit-159,Unit-160,Unit-161,Unit-162,Unit-163,Unit-164,Unit-165,Unit-166,Unit-167,Unit-168,Unit-169,Unit-170,Unit-171,Unit-172,Unit-173,Unit-174,Unit-175,Unit-176,Unit-177,Unit-178,Unit-179,Unit-180,Unit-181,Unit-182,Unit-183,Unit-184,Unit-185,Unit-186,Unit-187,Unit-188,Unit-189,Unit-190,Unit-191,Unit-192,Unit-193,Unit-194,Unit-195,Unit-196,Unit-197,Unit-198,Unit-199,Unit-200,Unit-201,Unit-202,Unit-203,Unit-204,Unit-205,Unit-206,Unit-207,Unit-208,Unit-209,Unit-210,Unit-211,Unit-212,Unit-213,Unit-214,Unit-215,Unit-216,Unit-217,Unit-218,Unit-219,Unit-220,Unit-221,Unit-222,Unit-223,Unit-224,Unit-225,Unit-226,Unit-227,Unit-228,Unit-229,Unit-230,Unit-231,Unit-232,Unit-233,Unit-234,Unit-235,Unit-236,Unit-237,Unit-238,Unit-239,Unit-240,Unit-241,Unit-242,Unit-243,Unit-244,Unit-245,Unit-246,Unit-247,Unit-248,Unit-249,Unit-250,Unit-251,Unit-252,Unit-253,Unit-254,Unit-255,Unit-256,Unit-257,Unit-258,Unit-259,Unit-260,Unit-261,Unit-262,Unit-263,Unit-264,Unit-265,Unit-266,Unit-267,Unit-268,Unit-269,Unit-270,Unit-271,Unit-272,Unit-273,Unit-274,Unit-275,Unit-276,Unit-277,Unit-278,Unit-279,Unit-280,Unit-281,Unit-282,Unit-283,Unit-284,Unit-285,Unit-286,Unit-287,Unit-288,Unit-289,Unit-290,Unit-291,Unit-292,Unit-293,Unit-294,Unit-295,Unit-296,Unit-297,Unit-298,Unit-299,Unit-300"


print ("Text to search for:")
textsToSearch = ["2022-08-01","2022-08-02","2022-08-03","2022-08-04"]

print ("Text to replace it with:")
textsToReplace = ["2022-08-05","2022-08-06","2022-08-07","2022-08-08"]
# textsToReplace = ["2022-08-09","2022-08-10","2022-08-11","2022-08-12"]
# textsToReplace = ["2022-08-13","2022-08-14","2022-08-15","2022-08-16"]
# textsToReplace = ["2022-08-05","2022-08-06","2022-08-07","2022-08-08"]

print ("File to perform Search-Replace on:")

# i = 0
# fin = open( fileToSearch, 'rt' )
# fout = open( 'new_1.csv', 'wt')

for i in range(0,len(textsToSearch)):
    fin = open( fileToSearch, 'rt' )
    fout = open( 'new_1.csv', 'a')
    textToSearch = textsToSearch[i]
    textToReplace = textsToReplace[i]
    
    #copy first 2 header row
    if(i ==0): 
        fout.write(header1+'\n')
        fout.write(header2+'\n')
        
    for line in fin:
        if textToSearch in line :
            print('Match Found:'+ textToSearch)
            fout.write(line.replace(textToSearch,textToReplace))
            # else:
            #     print('Match Not Found!!')
fin.close()
fout.close()

print("FINISHED...")

# input( '\n\n Press Enter to exit...' )