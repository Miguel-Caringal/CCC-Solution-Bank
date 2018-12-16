from collections import Counter, defaultdict
from datetime import datetime

s = """[1518-04-22 00:52] wakes up
[1518-05-16 00:00] Guard #1319 begins shift
[1518-03-24 00:50] wakes up
[1518-11-12 00:47] wakes up
[1518-08-18 00:42] falls asleep
[1518-04-24 00:49] wakes up
[1518-06-03 00:52] wakes up
[1518-10-08 00:52] wakes up
[1518-10-14 23:56] Guard #3359 begins shift
[1518-04-07 00:41] wakes up
[1518-11-03 00:07] wakes up
[1518-07-08 00:29] falls asleep
[1518-09-27 00:04] Guard #547 begins shift
[1518-09-26 00:35] falls asleep
[1518-07-15 00:52] wakes up
[1518-06-08 00:36] wakes up
[1518-04-23 23:47] Guard #607 begins shift
[1518-03-24 23:57] Guard #1289 begins shift
[1518-07-19 00:00] Guard #1783 begins shift
[1518-09-21 00:00] falls asleep
[1518-09-03 23:56] Guard #691 begins shift
[1518-07-28 00:19] falls asleep
[1518-08-25 23:49] Guard #2843 begins shift
[1518-07-26 00:40] wakes up
[1518-06-20 00:01] falls asleep
[1518-08-06 23:56] Guard #2143 begins shift
[1518-07-03 00:14] falls asleep
[1518-04-13 00:15] falls asleep
[1518-07-02 00:36] falls asleep
[1518-10-29 00:51] wakes up
[1518-07-18 00:00] Guard #1289 begins shift
[1518-07-03 00:34] wakes up
[1518-07-07 00:41] falls asleep
[1518-05-03 00:24] wakes up
[1518-04-09 00:38] wakes up
[1518-08-12 00:13] falls asleep
[1518-05-19 23:51] Guard #577 begins shift
[1518-07-17 00:46] wakes up
[1518-08-21 00:58] wakes up
[1518-07-23 00:48] wakes up
[1518-06-08 00:03] Guard #163 begins shift
[1518-05-20 00:42] wakes up
[1518-04-18 23:59] Guard #3359 begins shift
[1518-04-27 00:00] Guard #547 begins shift
[1518-10-26 00:27] falls asleep
[1518-11-07 00:03] falls asleep
[1518-07-05 00:39] falls asleep
[1518-03-21 00:03] falls asleep
[1518-10-15 23:49] Guard #383 begins shift
[1518-08-08 00:44] falls asleep
[1518-05-31 23:59] Guard #691 begins shift
[1518-08-31 00:44] falls asleep
[1518-04-01 00:39] falls asleep
[1518-04-05 00:42] wakes up
[1518-08-11 00:57] wakes up
[1518-07-22 00:49] wakes up
[1518-05-23 23:58] Guard #1531 begins shift
[1518-07-05 00:51] wakes up
[1518-05-04 23:57] Guard #2503 begins shift
[1518-07-27 00:44] wakes up
[1518-06-22 00:55] falls asleep
[1518-06-14 00:33] wakes up
[1518-03-27 00:22] wakes up
[1518-08-05 00:50] wakes up
[1518-10-21 00:41] wakes up
[1518-06-26 00:13] falls asleep
[1518-09-27 00:36] falls asleep
[1518-08-15 00:48] wakes up
[1518-03-20 00:50] wakes up
[1518-11-08 23:57] Guard #383 begins shift
[1518-02-24 00:49] wakes up
[1518-10-23 00:27] wakes up
[1518-09-02 00:01] Guard #3359 begins shift
[1518-06-06 00:56] wakes up
[1518-04-07 00:26] falls asleep
[1518-03-04 00:49] falls asleep
[1518-09-14 00:14] falls asleep
[1518-09-19 00:08] falls asleep
[1518-04-26 00:53] falls asleep
[1518-03-06 00:35] falls asleep
[1518-06-11 00:32] wakes up
[1518-06-10 00:49] wakes up
[1518-05-10 00:11] falls asleep
[1518-09-20 00:53] wakes up
[1518-10-12 00:39] falls asleep
[1518-09-22 00:40] wakes up
[1518-03-18 00:56] falls asleep
[1518-04-13 00:12] wakes up
[1518-10-22 00:44] falls asleep
[1518-06-08 00:31] falls asleep
[1518-11-08 00:55] falls asleep
[1518-08-17 00:42] wakes up
[1518-10-22 00:57] wakes up
[1518-11-21 00:54] wakes up
[1518-03-29 00:35] wakes up
[1518-06-30 00:49] falls asleep
[1518-05-18 23:53] Guard #607 begins shift
[1518-06-14 00:01] Guard #2143 begins shift
[1518-04-27 00:36] falls asleep
[1518-11-20 00:00] Guard #2647 begins shift
[1518-09-17 00:27] falls asleep
[1518-11-02 00:36] falls asleep
[1518-06-29 00:48] wakes up
[1518-03-15 00:02] Guard #2503 begins shift
[1518-11-09 23:57] Guard #1289 begins shift
[1518-07-13 00:57] wakes up
[1518-07-18 00:54] wakes up
[1518-09-30 00:03] Guard #2843 begins shift
[1518-08-01 00:43] wakes up
[1518-10-13 00:56] falls asleep
[1518-11-05 00:00] Guard #2503 begins shift
[1518-09-01 00:38] wakes up
[1518-08-26 00:28] wakes up
[1518-08-23 00:00] Guard #1531 begins shift
[1518-05-30 00:53] wakes up
[1518-07-13 00:27] falls asleep
[1518-10-12 00:53] wakes up
[1518-10-07 00:02] Guard #2803 begins shift
[1518-04-26 00:39] wakes up
[1518-05-02 00:41] wakes up
[1518-07-04 00:10] falls asleep
[1518-06-27 00:29] falls asleep
[1518-07-01 00:50] wakes up
[1518-09-08 00:28] wakes up
[1518-07-28 00:29] wakes up
[1518-02-28 00:04] Guard #2803 begins shift
[1518-06-10 00:25] falls asleep
[1518-09-29 00:59] wakes up
[1518-06-18 00:29] wakes up
[1518-07-28 00:40] falls asleep
[1518-08-11 23:56] Guard #577 begins shift
[1518-04-23 00:44] falls asleep
[1518-04-08 00:28] falls asleep
[1518-06-15 00:55] falls asleep
[1518-08-06 00:07] falls asleep
[1518-04-10 00:38] falls asleep
[1518-07-29 00:38] falls asleep
[1518-05-26 00:46] falls asleep
[1518-04-28 00:41] wakes up
[1518-10-03 00:43] falls asleep
[1518-07-06 23:56] Guard #797 begins shift
[1518-05-31 00:46] wakes up
[1518-10-04 00:05] falls asleep
[1518-04-13 00:11] falls asleep
[1518-10-25 00:18] falls asleep
[1518-08-31 00:29] wakes up
[1518-06-12 00:56] falls asleep
[1518-06-13 00:01] Guard #577 begins shift
[1518-03-16 00:16] falls asleep
[1518-08-15 00:01] Guard #797 begins shift
[1518-05-31 00:42] falls asleep
[1518-04-19 00:53] wakes up
[1518-08-15 00:33] falls asleep
[1518-07-07 00:10] falls asleep
[1518-06-11 00:52] falls asleep
[1518-09-18 00:38] falls asleep
[1518-09-17 00:23] wakes up
[1518-10-28 00:52] wakes up
[1518-08-09 00:18] falls asleep
[1518-08-01 00:40] falls asleep
[1518-06-30 00:00] Guard #2503 begins shift
[1518-07-18 00:33] wakes up
[1518-07-30 00:06] falls asleep
[1518-08-27 00:25] wakes up
[1518-04-03 23:53] Guard #691 begins shift
[1518-03-17 00:19] falls asleep
[1518-09-27 00:59] wakes up
[1518-05-30 00:42] falls asleep
[1518-10-03 00:04] Guard #577 begins shift
[1518-09-12 00:51] wakes up
[1518-10-16 00:32] falls asleep
[1518-03-15 00:27] falls asleep
[1518-09-09 23:57] Guard #797 begins shift
[1518-03-06 00:53] falls asleep
[1518-09-16 00:02] falls asleep
[1518-09-11 00:00] Guard #547 begins shift
[1518-03-20 00:02] Guard #1783 begins shift
[1518-08-11 00:45] falls asleep
[1518-07-15 00:19] falls asleep
[1518-09-14 00:00] Guard #2699 begins shift
[1518-04-30 00:14] wakes up
[1518-10-18 00:35] falls asleep
[1518-06-07 00:51] wakes up
[1518-11-17 00:48] falls asleep
[1518-09-18 00:25] wakes up
[1518-10-21 00:54] wakes up
[1518-05-17 00:13] falls asleep
[1518-08-24 00:47] wakes up
[1518-06-04 00:16] falls asleep
[1518-05-11 00:10] falls asleep
[1518-09-05 23:56] Guard #577 begins shift
[1518-07-04 00:50] wakes up
[1518-04-23 00:01] Guard #163 begins shift
[1518-04-12 00:00] Guard #547 begins shift
[1518-09-20 00:28] wakes up
[1518-03-16 00:43] wakes up
[1518-10-14 00:36] falls asleep
[1518-10-14 00:00] Guard #691 begins shift
[1518-02-24 00:27] wakes up
[1518-04-21 00:15] falls asleep
[1518-02-26 00:14] falls asleep
[1518-05-28 00:43] wakes up
[1518-03-03 00:01] falls asleep
[1518-05-05 00:43] wakes up
[1518-08-22 00:50] wakes up
[1518-03-08 00:20] falls asleep
[1518-06-23 00:58] wakes up
[1518-08-08 00:56] falls asleep
[1518-10-02 00:57] wakes up
[1518-09-10 00:14] falls asleep
[1518-11-01 00:54] falls asleep
[1518-04-13 23:48] Guard #2699 begins shift
[1518-11-22 23:59] Guard #1319 begins shift
[1518-10-13 00:58] wakes up
[1518-06-09 00:03] Guard #2843 begins shift
[1518-08-03 23:59] Guard #163 begins shift
[1518-05-25 00:03] Guard #1319 begins shift
[1518-09-14 00:37] falls asleep
[1518-07-03 00:00] Guard #2647 begins shift
[1518-09-30 23:58] Guard #691 begins shift
[1518-03-10 00:24] falls asleep
[1518-04-03 00:30] falls asleep
[1518-09-18 00:59] wakes up
[1518-08-13 23:49] Guard #1783 begins shift
[1518-05-10 00:40] wakes up
[1518-06-29 00:29] falls asleep
[1518-06-04 00:04] Guard #431 begins shift
[1518-03-08 23:58] Guard #2741 begins shift
[1518-11-01 00:28] wakes up
[1518-05-16 00:20] falls asleep
[1518-03-07 00:51] wakes up
[1518-05-19 00:44] wakes up
[1518-10-25 00:55] falls asleep
[1518-06-19 00:04] Guard #431 begins shift
[1518-11-12 00:56] wakes up
[1518-08-29 00:41] falls asleep
[1518-04-22 00:31] wakes up
[1518-06-23 00:03] falls asleep
[1518-02-26 00:25] wakes up
[1518-11-14 00:39] wakes up
[1518-09-14 00:54] wakes up
[1518-10-12 00:36] wakes up
[1518-06-27 23:57] Guard #1531 begins shift
[1518-07-17 00:54] wakes up
[1518-07-27 00:39] falls asleep
[1518-05-11 00:03] Guard #163 begins shift
[1518-11-22 00:52] wakes up
[1518-07-08 00:48] wakes up
[1518-08-15 00:34] wakes up
[1518-06-13 00:14] falls asleep
[1518-05-13 00:17] falls asleep
[1518-05-23 00:02] falls asleep
[1518-08-05 00:01] Guard #691 begins shift
[1518-07-21 00:55] wakes up
[1518-04-02 00:34] falls asleep
[1518-06-14 00:56] falls asleep
[1518-10-14 00:55] wakes up
[1518-10-09 00:36] wakes up
[1518-10-08 00:36] wakes up
[1518-03-12 23:56] Guard #797 begins shift
[1518-07-17 00:40] falls asleep
[1518-04-29 23:56] Guard #1319 begins shift
[1518-06-09 00:24] falls asleep
[1518-08-27 23:48] Guard #2741 begins shift
[1518-10-28 00:20] falls asleep
[1518-05-11 00:19] wakes up
[1518-04-17 00:43] falls asleep
[1518-04-18 00:00] Guard #547 begins shift
[1518-06-05 00:03] falls asleep
[1518-11-23 00:50] falls asleep
[1518-07-25 00:47] falls asleep
[1518-07-24 00:16] falls asleep
[1518-08-30 00:29] falls asleep
[1518-07-07 00:30] wakes up
[1518-03-11 00:41] falls asleep
[1518-09-06 00:43] wakes up
[1518-10-19 00:03] Guard #2741 begins shift
[1518-05-21 23:57] Guard #797 begins shift
[1518-04-17 00:32] wakes up
[1518-05-03 00:56] wakes up
[1518-08-25 00:13] falls asleep
[1518-11-03 00:05] falls asleep
[1518-09-12 23:57] Guard #2741 begins shift
[1518-03-02 00:01] Guard #2647 begins shift
[1518-07-11 00:30] falls asleep
[1518-02-23 00:51] wakes up
[1518-06-07 00:03] Guard #383 begins shift
[1518-07-25 00:03] Guard #2503 begins shift
[1518-04-06 00:23] wakes up
[1518-11-19 00:11] falls asleep
[1518-07-09 23:58] Guard #2843 begins shift
[1518-04-26 00:56] wakes up
[1518-06-20 23:56] Guard #521 begins shift
[1518-10-05 00:04] falls asleep
[1518-04-05 00:56] wakes up
[1518-06-30 00:56] wakes up
[1518-05-17 00:03] Guard #1319 begins shift
[1518-11-12 00:53] falls asleep
[1518-08-16 00:31] falls asleep
[1518-07-24 00:50] falls asleep
[1518-06-26 23:59] Guard #1319 begins shift
[1518-03-29 00:27] falls asleep
[1518-04-06 00:03] falls asleep
[1518-10-20 00:54] wakes up
[1518-05-28 00:40] falls asleep
[1518-10-24 00:05] falls asleep
[1518-09-17 00:02] Guard #797 begins shift
[1518-04-18 00:51] falls asleep
[1518-04-22 00:39] falls asleep
[1518-08-15 23:56] Guard #431 begins shift
[1518-11-02 00:04] falls asleep
[1518-09-20 00:57] falls asleep
[1518-08-10 00:53] wakes up
[1518-09-20 00:00] Guard #431 begins shift
[1518-03-05 00:30] wakes up
[1518-04-12 00:42] wakes up
[1518-03-26 00:29] falls asleep
[1518-03-04 00:10] falls asleep
[1518-10-23 00:35] falls asleep
[1518-11-13 00:44] falls asleep
[1518-11-04 00:00] falls asleep
[1518-08-23 00:48] falls asleep
[1518-08-25 00:53] falls asleep
[1518-08-20 00:55] falls asleep
[1518-03-10 00:52] wakes up
[1518-04-03 00:57] falls asleep
[1518-11-08 00:59] wakes up
[1518-06-04 23:50] Guard #1531 begins shift
[1518-06-06 00:47] falls asleep
[1518-06-20 00:50] wakes up
[1518-03-21 23:59] Guard #2699 begins shift
[1518-04-19 00:40] falls asleep
[1518-09-23 00:11] falls asleep
[1518-05-04 00:05] falls asleep
[1518-09-13 00:48] wakes up
[1518-10-04 00:59] wakes up
[1518-08-30 00:58] wakes up
[1518-06-08 00:55] wakes up
[1518-06-10 00:52] falls asleep
[1518-05-09 00:54] wakes up
[1518-05-21 00:03] falls asleep
[1518-07-05 00:35] wakes up
[1518-10-06 00:11] falls asleep
[1518-08-05 00:22] falls asleep
[1518-09-03 00:55] wakes up
[1518-07-20 00:32] wakes up
[1518-04-16 00:45] falls asleep
[1518-08-17 00:14] falls asleep
[1518-03-03 00:30] wakes up
[1518-07-09 00:58] wakes up
[1518-10-23 00:00] Guard #797 begins shift
[1518-05-07 00:05] falls asleep
[1518-02-26 00:33] falls asleep
[1518-03-27 00:08] falls asleep
[1518-10-16 00:50] wakes up
[1518-09-23 00:00] Guard #577 begins shift
[1518-02-24 00:00] Guard #691 begins shift
[1518-08-10 00:17] falls asleep
[1518-08-10 23:57] Guard #1531 begins shift
[1518-11-09 00:57] falls asleep
[1518-06-19 23:50] Guard #3359 begins shift
[1518-11-09 00:49] falls asleep
[1518-04-21 23:58] Guard #521 begins shift
[1518-02-25 00:56] wakes up
[1518-09-28 00:41] wakes up
[1518-03-21 00:57] wakes up
[1518-08-08 00:38] wakes up
[1518-03-08 00:58] wakes up
[1518-10-31 23:58] Guard #1531 begins shift
[1518-10-26 23:46] Guard #163 begins shift
[1518-06-06 00:42] falls asleep
[1518-03-30 00:44] wakes up
[1518-03-25 00:43] falls asleep
[1518-07-17 00:52] falls asleep
[1518-04-28 00:58] wakes up
[1518-07-12 00:03] Guard #691 begins shift
[1518-05-08 00:04] Guard #2143 begins shift
[1518-03-17 00:00] Guard #1783 begins shift
[1518-07-08 00:04] Guard #577 begins shift
[1518-08-19 23:56] Guard #1783 begins shift
[1518-09-04 00:33] wakes up
[1518-10-23 00:15] falls asleep
[1518-05-01 00:39] wakes up
[1518-10-19 00:31] wakes up
[1518-04-14 00:52] wakes up
[1518-08-14 00:54] wakes up
[1518-09-20 00:59] wakes up
[1518-11-14 00:01] Guard #383 begins shift
[1518-03-30 23:54] Guard #2647 begins shift
[1518-10-14 00:28] falls asleep
[1518-08-29 00:31] falls asleep
[1518-07-27 23:58] Guard #547 begins shift
[1518-09-03 00:49] falls asleep
[1518-10-29 00:43] wakes up
[1518-07-24 00:54] wakes up
[1518-04-02 00:55] wakes up
[1518-11-15 00:58] wakes up
[1518-11-05 00:56] wakes up
[1518-04-18 00:44] wakes up
[1518-06-22 00:27] falls asleep
[1518-09-20 00:40] falls asleep
[1518-07-12 00:25] falls asleep
[1518-03-07 00:01] falls asleep
[1518-05-27 00:00] Guard #431 begins shift
[1518-07-24 00:32] wakes up
[1518-10-23 23:46] Guard #2741 begins shift
[1518-08-28 00:01] falls asleep
[1518-08-25 00:46] wakes up
[1518-11-20 23:48] Guard #2843 begins shift
[1518-07-10 00:26] wakes up
[1518-03-28 23:58] Guard #2699 begins shift
[1518-05-26 00:09] falls asleep
[1518-09-13 00:19] falls asleep
[1518-06-24 00:09] falls asleep
[1518-04-25 23:56] Guard #521 begins shift
[1518-09-11 00:53] wakes up
[1518-05-17 23:52] Guard #1783 begins shift
[1518-08-03 00:29] falls asleep
[1518-08-23 00:58] wakes up
[1518-10-08 00:09] falls asleep
[1518-07-21 00:02] Guard #1531 begins shift
[1518-08-12 00:30] wakes up
[1518-10-28 00:25] wakes up
[1518-04-28 00:46] falls asleep
[1518-10-03 00:59] wakes up
[1518-11-05 00:47] falls asleep
[1518-04-21 00:47] falls asleep
[1518-05-01 00:10] falls asleep
[1518-08-22 00:39] wakes up
[1518-10-08 00:01] Guard #2741 begins shift
[1518-04-23 00:56] wakes up
[1518-07-18 00:15] falls asleep
[1518-08-03 00:59] wakes up
[1518-11-06 00:51] wakes up
[1518-05-17 00:37] falls asleep
[1518-11-23 00:22] wakes up
[1518-11-20 00:06] falls asleep
[1518-03-06 00:24] wakes up
[1518-04-12 00:06] falls asleep
[1518-04-07 00:59] wakes up
[1518-03-15 00:48] wakes up
[1518-11-18 00:51] falls asleep
[1518-03-25 00:32] falls asleep
[1518-05-30 00:29] wakes up
[1518-03-02 00:08] falls asleep
[1518-03-19 00:50] wakes up
[1518-09-14 23:56] Guard #2801 begins shift
[1518-07-11 00:03] Guard #431 begins shift
[1518-05-19 00:11] wakes up
[1518-10-02 00:03] falls asleep
[1518-03-14 00:37] falls asleep
[1518-10-11 00:10] falls asleep
[1518-06-03 00:21] falls asleep
[1518-11-04 00:51] wakes up
[1518-03-16 00:55] wakes up
[1518-08-31 00:27] falls asleep
[1518-05-11 00:27] falls asleep
[1518-09-17 23:46] Guard #691 begins shift
[1518-05-14 00:10] falls asleep
[1518-06-25 00:05] falls asleep
[1518-02-26 00:00] Guard #691 begins shift
[1518-07-23 00:02] Guard #607 begins shift
[1518-11-17 00:49] wakes up
[1518-06-01 00:10] falls asleep
[1518-11-15 00:34] falls asleep
[1518-02-23 00:15] falls asleep
[1518-10-10 00:02] falls asleep
[1518-03-16 00:19] wakes up
[1518-08-14 00:51] falls asleep
[1518-04-05 23:53] Guard #577 begins shift
[1518-04-16 00:57] wakes up
[1518-09-29 00:51] falls asleep
[1518-08-07 00:50] wakes up
[1518-09-06 00:39] falls asleep
[1518-11-02 00:29] wakes up
[1518-10-30 00:17] falls asleep
[1518-07-26 00:27] wakes up
[1518-10-12 23:58] Guard #2699 begins shift
[1518-10-09 00:08] falls asleep
[1518-05-12 00:13] falls asleep
[1518-03-06 00:44] wakes up
[1518-10-17 23:56] Guard #547 begins shift
[1518-04-24 23:50] Guard #607 begins shift
[1518-04-25 00:44] wakes up
[1518-07-30 00:25] wakes up
[1518-10-22 00:04] Guard #521 begins shift
[1518-10-25 00:49] wakes up
[1518-06-19 00:31] wakes up
[1518-11-05 00:39] wakes up
[1518-09-22 00:35] falls asleep
[1518-09-26 00:58] wakes up
[1518-07-17 00:03] Guard #1531 begins shift
[1518-03-18 23:56] Guard #2843 begins shift
[1518-06-28 00:56] falls asleep
[1518-05-13 00:53] wakes up
[1518-10-01 23:48] Guard #691 begins shift
[1518-06-22 23:52] Guard #1319 begins shift
[1518-04-23 00:33] falls asleep
[1518-11-11 23:56] Guard #1289 begins shift
[1518-11-08 00:03] Guard #2143 begins shift
[1518-05-30 23:59] Guard #2503 begins shift
[1518-11-17 00:31] wakes up
[1518-07-13 23:59] Guard #1319 begins shift
[1518-04-28 00:04] Guard #1289 begins shift
[1518-04-14 23:58] Guard #2803 begins shift
[1518-06-24 00:00] Guard #577 begins shift
[1518-02-27 00:01] falls asleep
[1518-10-11 00:47] wakes up
[1518-03-05 00:03] Guard #383 begins shift
[1518-05-21 00:50] wakes up
[1518-08-02 00:02] Guard #607 begins shift
[1518-11-10 00:10] falls asleep
[1518-09-30 00:59] wakes up
[1518-11-10 00:54] wakes up
[1518-10-16 00:04] falls asleep
[1518-05-25 00:36] falls asleep
[1518-05-28 23:56] Guard #2143 begins shift
[1518-03-10 00:03] Guard #163 begins shift
[1518-08-28 00:31] wakes up
[1518-06-29 00:24] wakes up
[1518-03-28 00:55] wakes up
[1518-10-28 00:30] falls asleep
[1518-03-06 00:18] falls asleep
[1518-09-07 00:18] falls asleep
[1518-09-17 00:12] falls asleep
[1518-06-11 00:14] falls asleep
[1518-08-13 00:35] falls asleep
[1518-06-28 00:58] wakes up
[1518-05-20 00:51] falls asleep
[1518-08-01 00:25] wakes up
[1518-11-12 00:11] falls asleep
[1518-06-18 00:13] falls asleep
[1518-08-13 00:36] wakes up
[1518-07-12 00:40] wakes up
[1518-03-17 00:56] wakes up
[1518-04-20 00:00] Guard #3359 begins shift
[1518-03-31 00:27] wakes up
[1518-09-11 00:45] falls asleep
[1518-05-08 00:29] falls asleep
[1518-08-22 00:54] falls asleep
[1518-06-17 00:03] Guard #577 begins shift
[1518-05-27 23:57] Guard #547 begins shift
[1518-09-01 00:08] falls asleep
[1518-10-19 00:20] falls asleep
[1518-08-21 23:59] Guard #163 begins shift
[1518-11-17 23:59] Guard #2843 begins shift
[1518-05-04 00:13] wakes up
[1518-08-26 00:50] wakes up
[1518-09-18 00:00] falls asleep
[1518-08-04 00:31] falls asleep
[1518-03-26 00:04] Guard #1319 begins shift
[1518-11-18 23:47] Guard #2647 begins shift
[1518-05-20 00:04] falls asleep
[1518-04-17 00:03] Guard #431 begins shift
[1518-05-17 00:16] wakes up
[1518-02-26 00:55] falls asleep
[1518-10-27 00:32] falls asleep
[1518-04-06 00:47] wakes up
[1518-06-22 00:02] Guard #1531 begins shift
[1518-11-19 00:53] wakes up
[1518-03-30 00:09] falls asleep
[1518-11-17 00:02] falls asleep
[1518-07-12 23:57] Guard #1319 begins shift
[1518-05-03 00:01] falls asleep
[1518-06-06 00:44] wakes up
[1518-05-20 00:53] wakes up
[1518-07-14 00:39] falls asleep
[1518-07-28 00:51] wakes up
[1518-05-27 00:45] wakes up
[1518-07-18 00:37] falls asleep
[1518-03-28 00:48] falls asleep
[1518-09-24 00:00] Guard #2699 begins shift
[1518-08-15 00:39] falls asleep
[1518-10-10 23:59] Guard #2699 begins shift
[1518-11-01 00:14] falls asleep
[1518-10-12 00:05] falls asleep
[1518-06-01 00:34] wakes up
[1518-05-17 00:44] wakes up
[1518-09-02 00:21] falls asleep
[1518-09-04 00:40] wakes up
[1518-10-24 00:18] wakes up
[1518-03-01 00:03] Guard #2143 begins shift
[1518-03-19 00:54] falls asleep
[1518-09-18 00:21] falls asleep
[1518-03-06 00:03] Guard #2843 begins shift
[1518-03-27 23:59] Guard #547 begins shift
[1518-08-03 00:45] falls asleep
[1518-11-14 00:19] falls asleep
[1518-08-06 00:37] falls asleep
[1518-06-05 00:28] wakes up
[1518-02-25 00:01] Guard #2503 begins shift
[1518-09-06 00:55] wakes up
[1518-11-16 23:50] Guard #2699 begins shift
[1518-08-23 23:59] Guard #1783 begins shift
[1518-04-10 00:26] falls asleep
[1518-06-10 00:40] falls asleep
[1518-08-26 00:44] falls asleep
[1518-08-29 00:35] wakes up
[1518-11-15 23:58] Guard #1319 begins shift
[1518-10-31 00:01] Guard #2699 begins shift
[1518-11-06 23:46] Guard #2503 begins shift
[1518-10-01 00:42] wakes up
[1518-04-08 00:49] wakes up
[1518-10-06 00:00] Guard #163 begins shift
[1518-07-11 00:24] wakes up
[1518-03-13 00:31] falls asleep
[1518-03-10 23:58] Guard #1531 begins shift
[1518-05-24 00:25] wakes up
[1518-02-22 23:59] Guard #1319 begins shift
[1518-06-02 00:37] wakes up
[1518-09-24 00:11] falls asleep
[1518-08-11 00:09] falls asleep
[1518-03-23 23:57] Guard #3359 begins shift
[1518-08-06 00:08] wakes up
[1518-06-20 00:10] wakes up
[1518-07-25 23:54] Guard #163 begins shift
[1518-06-02 23:58] Guard #431 begins shift
[1518-03-12 00:51] wakes up
[1518-03-09 00:57] wakes up
[1518-11-09 00:59] wakes up
[1518-03-24 00:58] wakes up
[1518-03-17 23:46] Guard #2741 begins shift
[1518-06-20 00:41] falls asleep
[1518-03-02 00:57] wakes up
[1518-06-25 00:38] falls asleep
[1518-10-03 00:39] wakes up
[1518-10-20 00:14] falls asleep
[1518-08-19 00:00] Guard #577 begins shift
[1518-06-22 00:59] wakes up
[1518-08-06 00:03] Guard #1531 begins shift
[1518-08-18 00:26] wakes up
[1518-10-13 00:27] falls asleep
[1518-10-08 23:59] Guard #797 begins shift
[1518-07-27 00:01] falls asleep
[1518-04-28 00:57] falls asleep
[1518-10-27 00:47] wakes up
[1518-07-15 23:57] Guard #1693 begins shift
[1518-06-04 00:49] falls asleep
[1518-11-02 00:54] wakes up
[1518-10-21 00:04] Guard #2143 begins shift
[1518-03-23 00:44] falls asleep
[1518-08-14 00:03] falls asleep
[1518-03-05 00:42] wakes up
[1518-02-26 00:57] wakes up
[1518-08-24 00:12] falls asleep
[1518-10-06 00:51] wakes up
[1518-05-08 00:36] wakes up
[1518-07-02 00:50] wakes up
[1518-10-26 00:58] wakes up
[1518-08-09 00:47] wakes up
[1518-08-02 00:29] falls asleep
[1518-09-09 00:12] falls asleep
[1518-10-22 00:34] falls asleep
[1518-09-08 00:26] falls asleep
[1518-06-16 00:29] wakes up
[1518-05-09 23:56] Guard #797 begins shift
[1518-04-30 00:46] falls asleep
[1518-09-30 00:33] wakes up
[1518-09-17 00:34] wakes up
[1518-09-12 00:39] falls asleep
[1518-04-16 00:00] Guard #2503 begins shift
[1518-08-01 00:19] falls asleep
[1518-04-08 00:03] Guard #431 begins shift
[1518-09-14 00:19] wakes up
[1518-04-29 00:16] falls asleep
[1518-07-06 00:23] falls asleep
[1518-09-30 00:37] falls asleep
[1518-11-21 00:03] falls asleep
[1518-05-22 00:28] wakes up
[1518-10-21 00:49] falls asleep
[1518-11-20 00:32] wakes up
[1518-09-09 00:49] wakes up
[1518-08-27 00:04] Guard #2843 begins shift
[1518-08-06 00:52] wakes up
[1518-08-02 00:49] falls asleep
[1518-05-11 00:43] wakes up
[1518-10-30 00:00] Guard #691 begins shift
[1518-11-18 00:34] wakes up
[1518-09-28 00:22] falls asleep
[1518-10-09 23:51] Guard #163 begins shift
[1518-03-03 23:59] Guard #1319 begins shift
[1518-10-14 00:32] wakes up
[1518-05-04 00:29] wakes up
[1518-07-20 00:01] Guard #607 begins shift
[1518-05-06 00:02] Guard #1319 begins shift
[1518-10-29 00:00] Guard #1783 begins shift
[1518-07-31 00:04] Guard #383 begins shift
[1518-08-13 00:06] falls asleep
[1518-09-29 00:12] falls asleep
[1518-06-22 00:44] wakes up
[1518-11-19 00:01] falls asleep
[1518-07-20 00:31] falls asleep
[1518-05-29 00:24] wakes up
[1518-10-11 23:50] Guard #2503 begins shift
[1518-08-06 00:59] wakes up
[1518-03-07 23:59] Guard #577 begins shift
[1518-07-15 00:00] Guard #1319 begins shift
[1518-05-04 00:16] falls asleep
[1518-06-02 00:45] falls asleep
[1518-10-31 00:56] wakes up
[1518-03-04 00:32] wakes up
[1518-06-27 00:48] wakes up
[1518-05-30 00:03] Guard #1531 begins shift
[1518-05-26 00:58] wakes up
[1518-09-28 00:00] Guard #521 begins shift
[1518-08-18 00:22] falls asleep
[1518-06-09 00:39] wakes up
[1518-10-25 00:59] wakes up
[1518-11-07 00:55] wakes up
[1518-06-10 00:54] wakes up
[1518-06-27 00:39] falls asleep
[1518-11-13 00:55] wakes up
[1518-11-16 00:26] falls asleep
[1518-06-13 00:11] wakes up
[1518-05-07 00:54] wakes up
[1518-04-06 00:17] falls asleep
[1518-08-06 00:26] wakes up
[1518-05-22 00:35] falls asleep
[1518-10-30 00:43] wakes up
[1518-07-04 00:23] wakes up
[1518-05-20 00:41] falls asleep
[1518-03-27 00:38] falls asleep
[1518-09-29 00:02] Guard #521 begins shift
[1518-02-25 00:32] falls asleep
[1518-04-24 00:35] falls asleep
[1518-06-05 00:32] falls asleep
[1518-05-09 00:15] falls asleep
[1518-08-25 00:56] wakes up
[1518-05-15 00:03] falls asleep
[1518-10-03 23:50] Guard #691 begins shift
[1518-09-04 23:58] Guard #2647 begins shift
[1518-04-03 00:59] wakes up
[1518-11-02 23:50] Guard #2647 begins shift
[1518-05-18 00:54] wakes up
[1518-03-29 00:53] falls asleep
[1518-08-08 00:57] wakes up
[1518-04-10 00:56] wakes up
[1518-06-19 00:20] falls asleep
[1518-04-07 00:44] falls asleep
[1518-08-14 00:35] wakes up
[1518-11-03 23:47] Guard #163 begins shift
[1518-10-27 00:07] wakes up
[1518-08-15 00:06] falls asleep
[1518-07-31 00:33] falls asleep
[1518-09-25 00:05] falls asleep
[1518-04-20 00:51] falls asleep
[1518-05-28 00:11] falls asleep
[1518-06-13 00:10] falls asleep
[1518-06-28 23:59] Guard #431 begins shift
[1518-05-15 00:31] wakes up
[1518-11-22 00:03] Guard #2843 begins shift
[1518-05-02 23:48] Guard #1783 begins shift
[1518-05-06 23:47] Guard #2647 begins shift
[1518-09-16 00:09] wakes up
[1518-03-22 00:26] falls asleep
[1518-09-01 00:03] Guard #2843 begins shift
[1518-05-03 00:34] falls asleep
[1518-07-25 00:55] wakes up
[1518-06-11 00:59] wakes up
[1518-05-14 23:46] Guard #1289 begins shift
[1518-08-24 00:56] falls asleep
[1518-11-16 00:48] wakes up
[1518-10-05 00:46] wakes up
[1518-08-03 00:41] wakes up
[1518-07-20 00:13] falls asleep
[1518-07-26 23:51] Guard #691 begins shift
[1518-09-18 23:57] Guard #1319 begins shift
[1518-07-24 00:03] Guard #2741 begins shift
[1518-09-05 00:59] wakes up
[1518-03-31 00:01] falls asleep
[1518-04-25 00:39] falls asleep
[1518-05-19 00:26] falls asleep
[1518-09-18 00:12] wakes up
[1518-08-22 00:34] falls asleep
[1518-04-18 00:56] wakes up
[1518-04-13 00:54] wakes up
[1518-07-22 00:40] falls asleep
[1518-07-14 00:57] wakes up
[1518-07-26 00:33] falls asleep
[1518-06-21 00:13] falls asleep
[1518-05-08 00:43] falls asleep
[1518-11-05 00:07] falls asleep
[1518-04-01 00:04] falls asleep
[1518-03-09 00:18] falls asleep
[1518-09-20 23:50] Guard #431 begins shift
[1518-04-06 00:14] wakes up
[1518-10-03 00:53] wakes up
[1518-04-03 00:45] wakes up
[1518-04-08 00:54] wakes up
[1518-07-02 00:04] Guard #2503 begins shift
[1518-06-10 00:04] Guard #547 begins shift
[1518-03-17 00:48] falls asleep
[1518-11-03 00:27] falls asleep
[1518-10-15 00:59] wakes up
[1518-04-18 00:40] falls asleep
[1518-05-29 00:20] falls asleep
[1518-08-24 00:58] wakes up
[1518-05-24 00:15] falls asleep
[1518-08-07 00:24] falls asleep
[1518-08-02 00:59] wakes up
[1518-03-16 00:53] falls asleep
[1518-03-04 00:56] wakes up
[1518-06-13 00:19] wakes up
[1518-03-27 00:03] Guard #521 begins shift
[1518-03-20 23:50] Guard #2843 begins shift
[1518-10-28 00:03] Guard #521 begins shift
[1518-10-27 00:04] falls asleep
[1518-07-05 00:13] falls asleep
[1518-03-14 00:29] wakes up
[1518-11-19 00:41] falls asleep
[1518-04-24 00:03] falls asleep
[1518-04-25 00:21] wakes up
[1518-05-16 00:50] wakes up
[1518-07-21 23:57] Guard #383 begins shift
[1518-04-08 00:53] falls asleep
[1518-03-14 00:57] wakes up
[1518-06-26 00:00] Guard #2503 begins shift
[1518-04-25 00:04] falls asleep
[1518-05-27 00:11] falls asleep
[1518-08-21 00:55] falls asleep
[1518-09-19 00:45] wakes up
[1518-03-14 00:04] falls asleep
[1518-08-18 00:56] wakes up
[1518-09-09 00:04] Guard #521 begins shift
[1518-04-21 00:37] wakes up
[1518-03-26 00:56] wakes up
[1518-06-25 00:51] wakes up
[1518-08-29 00:53] wakes up
[1518-07-31 00:44] wakes up
[1518-06-29 00:51] falls asleep
[1518-06-10 00:29] wakes up
[1518-05-08 00:56] wakes up
[1518-10-16 00:24] wakes up
[1518-03-19 00:49] falls asleep
[1518-03-11 00:36] wakes up
[1518-08-01 00:00] Guard #2647 begins shift
[1518-03-01 00:52] wakes up
[1518-09-05 00:20] falls asleep
[1518-11-19 00:30] wakes up
[1518-06-11 00:00] Guard #2503 begins shift
[1518-09-13 00:39] falls asleep
[1518-11-01 23:52] Guard #607 begins shift
[1518-03-05 00:33] falls asleep
[1518-06-06 00:38] wakes up
[1518-03-24 00:35] falls asleep
[1518-03-12 00:37] falls asleep
[1518-03-03 00:51] wakes up
[1518-07-23 00:29] falls asleep
[1518-06-18 00:55] wakes up
[1518-05-04 00:49] wakes up
[1518-09-29 00:42] wakes up
[1518-09-02 00:39] wakes up
[1518-05-06 00:47] wakes up
[1518-06-17 00:59] wakes up
[1518-11-18 00:54] wakes up
[1518-08-25 00:00] Guard #2843 begins shift
[1518-06-04 00:44] wakes up
[1518-03-23 00:54] wakes up
[1518-06-18 00:34] falls asleep
[1518-06-12 00:59] wakes up
[1518-08-22 00:58] wakes up
[1518-03-24 00:11] falls asleep
[1518-04-30 00:47] wakes up
[1518-08-29 23:57] Guard #1783 begins shift
[1518-06-07 00:44] falls asleep
[1518-09-11 00:14] falls asleep
[1518-09-22 00:53] wakes up
[1518-09-03 00:01] Guard #2503 begins shift
[1518-11-18 00:32] falls asleep
[1518-08-26 00:02] falls asleep
[1518-09-30 00:06] falls asleep
[1518-08-08 23:59] Guard #383 begins shift
[1518-05-25 00:57] wakes up
[1518-03-20 00:12] falls asleep
[1518-03-27 00:54] wakes up
[1518-06-04 00:51] wakes up
[1518-04-27 00:57] wakes up
[1518-08-06 00:57] falls asleep
[1518-08-15 00:19] wakes up
[1518-06-26 00:43] wakes up
[1518-03-16 00:03] Guard #691 begins shift
[1518-04-21 00:56] wakes up
[1518-08-29 00:03] Guard #1783 begins shift
[1518-07-09 00:56] falls asleep
[1518-05-06 00:07] falls asleep
[1518-03-03 00:49] falls asleep
[1518-09-23 00:14] wakes up
[1518-10-03 00:37] falls asleep
[1518-07-04 00:42] falls asleep
[1518-09-11 00:29] wakes up
[1518-04-26 00:20] falls asleep
[1518-06-30 23:50] Guard #691 begins shift
[1518-09-04 00:10] falls asleep
[1518-10-29 00:30] falls asleep
[1518-05-12 00:52] wakes up
[1518-03-24 00:23] wakes up
[1518-07-10 00:15] falls asleep
[1518-07-29 00:04] Guard #163 begins shift
[1518-04-11 00:01] Guard #2801 begins shift
[1518-07-11 00:11] falls asleep
[1518-03-25 00:50] wakes up
[1518-04-08 23:58] Guard #163 begins shift
[1518-06-27 00:30] wakes up
[1518-05-08 23:57] Guard #607 begins shift
[1518-10-17 00:01] Guard #2801 begins shift
[1518-08-04 00:46] wakes up
[1518-06-16 00:11] falls asleep
[1518-03-25 00:40] wakes up
[1518-08-19 00:20] falls asleep
[1518-04-01 00:34] wakes up
[1518-03-18 00:47] wakes up
[1518-06-28 00:44] wakes up
[1518-07-21 00:16] falls asleep
[1518-10-22 00:36] wakes up
[1518-04-05 00:02] Guard #547 begins shift
[1518-08-20 00:59] wakes up
[1518-07-19 00:40] wakes up
[1518-04-05 00:29] falls asleep
[1518-05-21 00:48] falls asleep
[1518-05-22 00:14] falls asleep
[1518-08-07 23:58] Guard #2503 begins shift
[1518-08-16 23:57] Guard #383 begins shift
[1518-06-11 23:56] Guard #2143 begins shift
[1518-04-28 00:12] falls asleep
[1518-10-15 00:56] falls asleep
[1518-05-12 00:32] wakes up
[1518-08-31 00:56] wakes up
[1518-07-05 00:04] Guard #547 begins shift
[1518-06-05 00:56] wakes up
[1518-09-20 00:15] falls asleep
[1518-08-18 00:03] Guard #1319 begins shift
[1518-04-01 00:51] falls asleep
[1518-05-23 00:56] wakes up
[1518-05-18 00:05] falls asleep
[1518-10-04 23:50] Guard #2503 begins shift
[1518-08-02 00:44] wakes up
[1518-06-02 00:32] falls asleep
[1518-11-06 00:12] falls asleep
[1518-06-14 00:59] wakes up
[1518-05-21 00:17] wakes up
[1518-07-19 00:24] falls asleep
[1518-03-11 00:11] falls asleep
[1518-07-29 23:57] Guard #607 begins shift
[1518-09-06 00:48] falls asleep
[1518-08-02 00:19] wakes up
[1518-05-12 00:37] falls asleep
[1518-06-17 00:06] falls asleep
[1518-11-23 00:56] wakes up
[1518-07-06 00:03] Guard #797 begins shift
[1518-06-15 23:59] Guard #797 begins shift
[1518-11-11 00:07] falls asleep
[1518-08-27 00:07] falls asleep
[1518-05-26 00:00] Guard #607 begins shift
[1518-06-25 00:30] wakes up
[1518-04-04 00:33] wakes up
[1518-05-05 00:26] falls asleep
[1518-09-07 00:54] wakes up
[1518-05-22 23:48] Guard #383 begins shift
[1518-07-09 00:03] Guard #2503 begins shift
[1518-09-24 00:42] wakes up
[1518-02-26 23:46] Guard #797 begins shift
[1518-05-02 00:05] falls asleep
[1518-10-03 00:57] falls asleep
[1518-05-27 00:42] falls asleep
[1518-02-27 00:58] wakes up
[1518-04-28 00:54] wakes up
[1518-06-14 23:56] Guard #1783 begins shift
[1518-05-03 23:50] Guard #163 begins shift
[1518-11-11 00:17] wakes up
[1518-02-26 00:49] wakes up
[1518-04-04 00:04] falls asleep
[1518-03-16 00:25] falls asleep
[1518-04-17 00:56] wakes up
[1518-07-20 00:20] wakes up
[1518-04-12 23:59] Guard #1783 begins shift
[1518-11-06 00:02] Guard #797 begins shift
[1518-05-12 00:03] Guard #577 begins shift
[1518-04-06 00:42] falls asleep
[1518-10-18 00:47] wakes up
[1518-11-19 00:05] wakes up
[1518-05-14 00:15] wakes up
[1518-08-10 00:00] Guard #797 begins shift
[1518-06-24 00:56] wakes up
[1518-05-19 00:02] falls asleep
[1518-05-27 00:21] wakes up
[1518-04-05 00:51] falls asleep
[1518-08-21 00:00] Guard #2699 begins shift
[1518-03-06 00:57] wakes up
[1518-11-01 00:57] wakes up
[1518-03-18 00:58] wakes up
[1518-03-22 00:48] wakes up
[1518-06-29 00:16] falls asleep
[1518-10-10 00:37] wakes up
[1518-04-22 00:19] falls asleep
[1518-03-31 23:53] Guard #797 begins shift
[1518-11-10 23:57] Guard #2647 begins shift
[1518-06-02 00:54] wakes up
[1518-09-10 00:54] wakes up
[1518-08-08 00:51] wakes up
[1518-03-05 00:24] falls asleep
[1518-11-23 00:06] falls asleep
[1518-09-08 00:00] Guard #691 begins shift
[1518-08-06 00:14] falls asleep
[1518-04-09 00:17] falls asleep
[1518-10-31 00:28] falls asleep
[1518-04-21 00:00] Guard #431 begins shift
[1518-03-29 00:57] wakes up
[1518-08-08 00:33] falls asleep
[1518-02-24 00:40] falls asleep
[1518-04-01 00:58] wakes up
[1518-04-07 00:00] Guard #1319 begins shift
[1518-05-28 00:22] wakes up
[1518-04-20 00:56] wakes up
[1518-03-22 23:57] Guard #607 begins shift
[1518-05-13 23:56] Guard #607 begins shift
[1518-07-29 00:49] wakes up
[1518-08-26 00:07] falls asleep
[1518-09-21 00:43] wakes up
[1518-10-13 00:28] wakes up
[1518-06-29 00:52] wakes up
[1518-03-19 00:58] wakes up
[1518-03-13 00:46] wakes up
[1518-08-26 00:04] wakes up
[1518-03-17 00:39] wakes up
[1518-09-26 00:01] Guard #547 begins shift
[1518-07-06 00:47] wakes up
[1518-09-15 23:54] Guard #577 begins shift
[1518-03-13 23:54] Guard #577 begins shift
[1518-08-02 00:17] falls asleep
[1518-10-01 00:33] falls asleep
[1518-04-14 00:04] falls asleep
[1518-06-24 23:46] Guard #2843 begins shift
[1518-03-13 00:49] falls asleep
[1518-09-06 23:58] Guard #383 begins shift
[1518-03-01 00:12] falls asleep
[1518-11-20 00:45] falls asleep
[1518-08-02 23:58] Guard #383 begins shift
[1518-10-08 00:50] falls asleep
[1518-11-13 00:00] Guard #547 begins shift
[1518-08-13 00:01] Guard #163 begins shift
[1518-03-30 00:01] Guard #1319 begins shift
[1518-08-22 00:46] falls asleep
[1518-06-01 23:56] Guard #163 begins shift
[1518-11-14 23:56] Guard #383 begins shift
[1518-08-13 00:11] wakes up
[1518-04-17 00:30] falls asleep
[1518-04-01 00:48] wakes up
[1518-04-24 00:31] wakes up
[1518-04-23 00:38] wakes up
[1518-07-09 00:48] falls asleep
[1518-10-25 00:03] Guard #797 begins shift
[1518-11-22 00:25] falls asleep
[1518-03-18 00:05] falls asleep
[1518-07-11 00:46] wakes up
[1518-04-01 23:56] Guard #577 begins shift
[1518-05-04 00:38] falls asleep
[1518-09-22 00:00] Guard #163 begins shift
[1518-08-19 00:42] wakes up
[1518-08-30 23:58] Guard #607 begins shift
[1518-07-27 00:33] wakes up
[1518-06-15 00:56] wakes up 
[1518-06-14 00:08] falls asleep
[1518-10-29 00:50] falls asleep
[1518-05-12 23:57] Guard #577 begins shift
[1518-07-01 00:00] falls asleep
[1518-09-24 23:49] Guard #2741 begins shift
[1518-03-11 00:59] wakes up
[1518-05-20 23:53] Guard #2843 begins shift
[1518-05-30 00:19] falls asleep
[1518-07-07 00:53] wakes up
[1518-11-03 00:57] wakes up
[1518-05-20 00:38] wakes up
[1518-07-26 00:01] falls asleep
[1518-06-06 00:29] falls asleep
[1518-06-21 00:52] wakes up
[1518-02-24 00:12] falls asleep
[1518-08-16 00:51] wakes up
[1518-04-10 00:02] Guard #163 begins shift
[1518-09-22 00:52] falls asleep
[1518-03-23 00:37] wakes up
[1518-10-23 00:46] wakes up
[1518-03-06 23:46] Guard #3359 begins shift
[1518-07-09 00:51] wakes up
[1518-03-11 23:56] Guard #547 begins shift
[1518-11-09 00:50] wakes up
[1518-03-13 00:58] wakes up
[1518-10-20 00:00] Guard #547 begins shift
[1518-06-08 00:39] falls asleep
[1518-11-20 00:57] wakes up
[1518-06-06 00:04] Guard #797 begins shift
[1518-08-11 00:35] wakes up
[1518-04-30 00:13] falls asleep
[1518-07-03 23:59] Guard #2647 begins shift
[1518-05-26 00:38] wakes up
[1518-09-25 00:20] wakes up
[1518-05-22 00:45] wakes up
[1518-04-10 00:32] wakes up
[1518-04-29 00:04] Guard #1531 begins shift
[1518-10-26 00:00] Guard #2843 begins shift
[1518-06-18 00:03] Guard #2699 begins shift
[1518-03-24 00:57] falls asleep
[1518-09-13 00:27] wakes up
[1518-03-02 23:52] Guard #2647 begins shift
[1518-04-30 23:58] Guard #163 begins shift
[1518-04-29 00:28] wakes up
[1518-09-04 00:39] falls asleep
[1518-06-28 00:25] falls asleep
[1518-10-21 00:32] falls asleep
[1518-03-23 00:33] falls asleep
[1518-09-11 23:58] Guard #1783 begins shift
[1518-04-03 00:02] Guard #1531 begins shift
[1518-05-01 23:46] Guard #2503 begins shift"""


guards = defaultdict(Counter)
for t, m in [l.split('] ') for l in sorted(s.splitlines()) if l]:
    t = datetime.strptime(t, '[%Y-%m-%d %H:%M')
    if '#' in m:     g = int(m.split('#')[1].split()[0])
    if 'falls' in m: start = t
    if 'wakes' in m:
        minutes = int((t - start).total_seconds() // 60)
        guards[g].update(Counter((start.minute+i)%60 for i in range(minutes)))

_, id = max((sum(c.values()), id) for id, c in guards.items())
part1 = id * guards[id].most_common()[0][0]

(_, minute), id = max((c.most_common()[0][::-1], id) for id, c in guards.items())
part2 = id * minute

print (part2)