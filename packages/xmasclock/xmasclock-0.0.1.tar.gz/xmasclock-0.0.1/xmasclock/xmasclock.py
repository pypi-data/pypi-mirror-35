#!/usr/bin/env python
import argparse
from datetime import datetime


SECONDS_IN_DAY = 86400
DAYS = 'days'
SECONDS = 'seconds'


def get_next_xmas(now):
    this_years_xmas = datetime(now.year, 12, 25)
    if this_years_xmas <= now:
        return datetime(now.year + 1, 12, 25)
    return this_years_xmas


def count_days_til_xmas(now):
    next_xmas = get_next_xmas(now)
    return (next_xmas - now).days


def count_seconds_til_xmas(now):
    next_xmas_day = get_next_xmas(now)
    diff = next_xmas_day - now
    return diff.seconds + diff.days * SECONDS_IN_DAY


def build_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('measurement', choices=[DAYS, SECONDS], help='which measurement to use when calculating the countdown')
    return parser


def handle_args(parser):
    args = parser.parse_args()
    now = datetime.now()
    if args.measurement == DAYS:
        print('days until xmas: {}'.format(count_days_til_xmas(now)))
    if args.measurement == SECONDS:
        print('seconds until xmas: {}'.format(count_seconds_til_xmas(now)))


if __name__ == '__main__':
    parser = build_argparser()
    handle_args(parser)
