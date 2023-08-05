#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#    This file is part of the pwv_kpno software package.
#
#    The pwv_kpno package is free software: you can redistribute it and/or
#    modify it under the terms of the GNU General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    The pwv_kpno package is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
#    Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with pwv_kpno. If not, see <http://www.gnu.org/licenses/>.

"""This file provides tests for the function "transmission"."""

import unittest
from datetime import datetime, timedelta

import numpy as np
from astropy.table import Table
from pytz import utc

from ._create_mock_data import create_mock_pwv_model
from pwv_kpno import pwv_atm

__authors__ = ['Daniel Perrefort']
__copyright__ = 'Copyright 2017, Daniel Perrefort'

__license__ = 'GPL V3'
__email__ = 'djperrefort@pitt.edu'
__status__ = 'Release'


def _check_attrs(iterable, **kwargs):
    """Check the attribute values of objects in an iterable

    Iterate through the contents of a given iterable and check that all
    attribute values match those specified by **kwargs.

    Args:
        table    (Table): A table with a 'date' column
        **kwargs        : datetime attributes and values

    Returns:
        True or False
    """

    assert len(kwargs), 'No attributes specified'
    for obj in iterable:
        for param_name, param_value in kwargs.items():
            if getattr(obj, param_name) != param_value:
                return False

    return True


class SearchArgumentErrors(unittest.TestCase):
    """Test that _check_search_args raises the appropriate errors

    _check_search_args is responsible for checking the arguments for both
    pwv_kpno.pwv_atm.measured_pwv and pwv_kpno.pwv_atm.modeled_pwv"""

    def assert_raises_iter(self, iterable, error):
        for val in iterable:
            self.assertRaises(error, pwv_atm._check_date_time_args, val)

    def test_checks_for_valid_year(self):
        """Test for correct errors due to bad year argument"""

        next_year = datetime.now().year + 1
        self.assert_raises_iter([-2010, 2009, next_year], ValueError)

    def test_checks_for_valid_month(self):
        """Test for correct errors due to bad month argument"""

        self.assert_raises_iter([-3, 0, 13], ValueError)

    def test_checks_for_valid_day(self):
        """Test for correct errors due to bad day argument"""

        self.assert_raises_iter([-3, 0, 32], ValueError)

    def test_checks_for_valid_hour(self):
        """Test for correct errors due to bad hour argument"""

        self.assert_raises_iter([-3, 24, 30], ValueError)


class MeasuredPWV(unittest.TestCase):
    """Tests for the 'pwv_atm.measured_pwv' function"""

    data_table = pwv_atm.measured_pwv()

    def test_returned_tz_info(self):
        """Test if datetimes in the returned data are timezone aware"""

        tzinfo = self.data_table[0][0].tzinfo
        error_msg = 'Datetimes should be UTC aware (found "{}")'
        self.assertTrue(tzinfo == utc, error_msg.format(tzinfo))

    def test_returned_column_order(self):
        """Test the column order of the table returned by pwv_atm.measured_pwv()

        The first two columns should be 'date' and 'KITT'
        """

        col_0 = self.data_table.colnames[0]
        col_1 = self.data_table.colnames[1]
        error_msg = 'column {} should be "{}", found "{}"'
        self.assertEqual(col_0, 'date', error_msg.format(0, 'date', col_0))
        self.assertEqual(col_1, 'KITT', error_msg.format(1, 'KITT', col_1))

    def test_filtering_by_args(self):
        """Test if results are correctly filtered by kwarg arguments"""

        test_cases = [{'year': 2010}, {'month': 7}, {'day': 21}, {'hour': 5},
                      {'year': 2011, 'month': 4, 'day': 30, 'hour': 21}]

        error_msg = 'pwv_atm.measured_pwv returned incorrect dates. kwargs: {}'
        for kwargs in test_cases:
            good_attr = _check_attrs(pwv_atm.measured_pwv(**kwargs)['date'],
                                     **kwargs)
            self.assertTrue(good_attr, error_msg.format(kwargs))

    def test_units(self):
        """Test columns for appropriate units"""

        for column in self.data_table.itercols():
            if column.name == 'date':
                self.assertEqual(column.unit, 'UTC')

            else:
                self.assertEqual(column.unit, 'mm')


class ModeledPWV(unittest.TestCase):
    """Tests for the 'pwv_atm.modeled_pwv' function"""

    data_table = pwv_atm.modeled_pwv()
    test_returned_tz_info = MeasuredPWV.__dict__["test_returned_tz_info"]
    test_units = MeasuredPWV.__dict__["test_units"]


class PwvDate(unittest.TestCase):
    """Tests for the pwv_date function"""

    kitt_peak_pwv_model = pwv_atm.modeled_pwv()

    def test_known_dates(self):
        """Tests that pwv_date"""

        test_date_0 = self.kitt_peak_pwv_model['date'][0]
        test_pwv_0 = self.kitt_peak_pwv_model['pwv'][0]
        test_date_100 = self.kitt_peak_pwv_model['date'][100]
        test_pwv_100 = self.kitt_peak_pwv_model['pwv'][100]

        error_msg = "pwv_date returned incorrect PWV value for tabulated date"
        self.assertEqual(test_pwv_0, pwv_atm._pwv_date(test_date_0), error_msg)
        self.assertEqual(test_pwv_100, pwv_atm._pwv_date(test_date_100),
                         error_msg)

    def test_data_gap_handling(self):
        """Test errors raised from function call for datetime without PWV data

        pwv_date should raise an error if it is asked for the PWV at a datetime
        that falls within a gap in available data spanning one day or more.
        """

        # Start dates for data gaps
        one_day_start = datetime(year=2010, month=1, day=11, tzinfo=utc)
        three_day_start = datetime(year=2010, month=4, day=11, tzinfo=utc)

        gaps = [(one_day_start, 1), (three_day_start, 3)]
        mock_model = create_mock_pwv_model(year=2010, gaps=gaps)

        self.assertRaises(ValueError, pwv_atm._pwv_date,
                          one_day_start, 1, mock_model)
        self.assertRaises(ValueError, pwv_atm._pwv_date,
                          three_day_start, 1, mock_model)


class TransmissionErrors(unittest.TestCase):
    """Test pwv_kpno.transmission for raised errors due to bad arguments"""

    def test_argument_types(self):
        """Test errors raised from function call with wrong argument types"""

        test_date = datetime(2011, 1, 5, 12, 47, tzinfo=utc)

        # TypeError for date argument (should be datetime)
        self.assertRaises(TypeError, pwv_atm._raise_transmission_args, "1", 1)

        # TypeError for airmass argument (should be float or int)
        self.assertRaises(TypeError, pwv_atm._raise_transmission_args,
                          test_date, "1")

        # ValueError due to naive datetime with no time zone info
        self.assertRaises(ValueError, pwv_atm._raise_transmission_args,
                          datetime.now(), 1)

    def test_argument_values(self):
        """Test errors raise from function call with date out of data range

        An error should be raised for dates that are not covered by the locally
        available data files. For the release version of the package, the
        acceptable date range begins with 2010 through the current date.
        """

        early_day = datetime(year=2009, month=12, day=31, tzinfo=utc)
        self.assertRaises(ValueError, pwv_atm._raise_transmission_args,
                          early_day, 1)

        now = datetime.now()
        late_day = now + timedelta(days=1)
        self.assertRaises(ValueError, pwv_atm._raise_transmission_args,
                          late_day, 1)

        late_year = datetime(year=now.year + 1, month=1, day=1, tzinfo=utc)
        self.assertRaises(ValueError, pwv_atm._raise_transmission_args,
                          late_year, 1)


class TransmissionResults(unittest.TestCase):
    """Test pwv_kpno.transmission for the expected returns"""

    mock_model = create_mock_pwv_model(2010)

    def test_argument_values(self):
        """Test errors raised from function call with out of range values

        PWV concentrations should be between 0 and 30.1 mm (inclusive). This
        is due to the range of the atmospheric models.
        """

        self.assertRaises(ValueError, pwv_atm.trans_for_pwv, -1)

        # Check value that uses interpolation
        self.assertIsNotNone(pwv_atm.trans_for_pwv(15.0))

        # Check value outside domain that uses extrapolation
        self.assertIsNotNone(pwv_atm.trans_for_pwv(30.5))

    def test_airmass_dependence(self):
        """Test that line of sight pwv is directly proportional to airmass"""

        date_35 = self.mock_model['date'][35]
        date_35 = datetime.utcfromtimestamp(date_35).replace(tzinfo=utc)

        date_40 = self.mock_model['date'][40]
        date_40 = datetime.utcfromtimestamp(date_40).replace(tzinfo=utc)

        print(date_35)
        print(date_40)

        airmass_2_transm = pwv_atm._trans_for_date(date_35, 2, test_model=self.mock_model)
        airmass_1_transm = pwv_atm._trans_for_date(date_40, 1, test_model=self.mock_model)

        same_transmission = np.equal(airmass_1_transm['transmission'],
                                     airmass_2_transm['transmission'])

        self.assertTrue(all(same_transmission))

    def test_column_units(self):
        """Test columns of the returned transmission table for correct units

        Perform the test for the transmission at 2011/01/01 00:00 and an
        airmass of 1.
        """

        sample_transm = pwv_atm.trans_for_date(
            datetime(2011, 1, 1, tzinfo=utc), 1)
        w_units = sample_transm['wavelength'].unit
        t_units = sample_transm['transmission'].unit

        error_msg = 'Wrong units for column "{}"'
        self.assertEqual(w_units, 'angstrom', error_msg.format('wavelength'))
        self.assertEqual(t_units, None, error_msg.format('transmission'))
